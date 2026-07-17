#!/usr/bin/env python3
"""
Pure Python PDF Generator for KDP Book Materials
No external dependencies required - generates valid PDF 1.4 files directly.
"""

import os
import re
import zlib
from datetime import datetime


class PurePDF:
    """Generates PDF files using raw PDF specification (no external libraries)."""

    def __init__(self, title="Document", author="Selam Fesehaye"):
        self.title = title
        self.author = author
        self.pages = []
        self.current_page_content = []
        self.page_width = 612  # 8.5" in points
        self.page_height = 792  # 11" in points
        self.margin_left = 54  # 0.75"
        self.margin_right = 54
        self.margin_top = 72  # 1"
        self.margin_bottom = 72
        self.font_size = 10
        self.line_height = 14
        self.y_position = self.page_height - self.margin_top
        self.objects = []
        self.object_offsets = []

        # Start first page
        self._new_page()

    def _new_page(self):
        """Start a new page."""
        if self.current_page_content:
            self.pages.append(self.current_page_content)
        self.current_page_content = []
        self.y_position = self.page_height - self.margin_top

    def _check_page_break(self, lines_needed=1):
        """Check if we need a page break."""
        space_needed = lines_needed * self.line_height
        if self.y_position - space_needed < self.margin_bottom:
            self._new_page()

    def _escape_pdf_text(self, text):
        """Escape special characters for PDF text strings."""
        text = text.replace('\\', '\\\\')
        text = text.replace('(', '\\(')
        text = text.replace(')', '\\)')
        # Remove non-ASCII characters (emojis, special chars)
        text = ''.join(c if ord(c) < 128 else ' ' for c in text)
        return text

    def _add_text_line(self, text, font_size=10, bold=False, indent=0):
        """Add a single line of text to the current page."""
        self._check_page_break()

        escaped = self._escape_pdf_text(text)
        font = "/F2" if bold else "/F1"
        x = self.margin_left + indent

        cmd = f"BT {font} {font_size} Tf {x} {self.y_position:.1f} Td ({escaped}) Tj ET"
        self.current_page_content.append(cmd)
        self.y_position -= self.line_height

    def _wrap_text(self, text, max_chars=90):
        """Wrap text to fit within page width."""
        if len(text) <= max_chars:
            return [text]

        lines = []
        words = text.split()
        current_line = ""

        for word in words:
            if len(current_line) + len(word) + 1 <= max_chars:
                current_line += (" " + word if current_line else word)
            else:
                if current_line:
                    lines.append(current_line)
                current_line = word

        if current_line:
            lines.append(current_line)

        return lines if lines else [""]

    def add_title(self, text):
        """Add a document title."""
        self._check_page_break(3)
        self.line_height = 20
        self._add_text_line(text, font_size=18, bold=True)
        self.line_height = 14
        self.y_position -= 10  # extra space after title

    def add_heading1(self, text):
        """Add H1 heading."""
        self._check_page_break(3)
        self.y_position -= 8  # space before heading
        self.line_height = 18
        self._add_text_line(text, font_size=14, bold=True)
        self.line_height = 14
        self.y_position -= 4

    def add_heading2(self, text):
        """Add H2 heading."""
        self._check_page_break(2)
        self.y_position -= 6
        self.line_height = 16
        self._add_text_line(text, font_size=12, bold=True)
        self.line_height = 14
        self.y_position -= 2

    def add_heading3(self, text):
        """Add H3 heading."""
        self._check_page_break(2)
        self.y_position -= 4
        self._add_text_line(text, font_size=11, bold=True)
        self.y_position -= 2

    def add_paragraph(self, text):
        """Add a paragraph of text with word wrapping."""
        lines = self._wrap_text(text)
        self._check_page_break(len(lines))
        for line in lines:
            self._add_text_line(line, font_size=10)

    def add_bullet(self, text, level=0):
        """Add a bullet point."""
        indent = level * 18
        bullet = "  - " if level > 0 else "- "
        lines = self._wrap_text(bullet + text, max_chars=85 - (level * 3))
        self._check_page_break(len(lines))
        for i, line in enumerate(lines):
            self._add_text_line(line, font_size=10, indent=indent)

    def add_code_line(self, text):
        """Add a code/monospace line."""
        self._check_page_break()
        self._add_text_line("  " + text, font_size=9, indent=18)

    def add_blank_line(self):
        """Add vertical space."""
        self.y_position -= self.line_height * 0.7

    def add_separator(self):
        """Add a horizontal separator."""
        self.y_position -= 6
        x1 = self.margin_left
        x2 = self.page_width - self.margin_right
        cmd = f"{x1} {self.y_position:.1f} m {x2} {self.y_position:.1f} l 0.5 w S"
        self.current_page_content.append(cmd)
        self.y_position -= 10

    def add_page_break(self):
        """Force a page break."""
        self._new_page()

    def parse_markdown(self, markdown_text):
        """Parse markdown text and add it to the PDF."""
        lines = markdown_text.split('\n')
        in_code_block = False
        i = 0

        while i < len(lines):
            line = lines[i]

            # Code block
            if line.strip().startswith('```'):
                in_code_block = not in_code_block
                i += 1
                continue

            if in_code_block:
                self.add_code_line(line)
                i += 1
                continue

            # Empty line
            if not line.strip():
                self.add_blank_line()
                i += 1
                continue

            # Horizontal rule
            if line.strip() in ('---', '***', '___'):
                self.add_separator()
                i += 1
                continue

            # Headings
            stripped = line.strip()
            if stripped.startswith('# '):
                self.add_heading1(stripped[2:].strip('# '))
                i += 1
                continue
            elif stripped.startswith('## '):
                self.add_heading2(stripped[3:].strip('# '))
                i += 1
                continue
            elif stripped.startswith('### '):
                self.add_heading3(stripped[4:].strip('# '))
                i += 1
                continue
            elif stripped.startswith('#### '):
                self.add_heading3(stripped[5:].strip('# '))
                i += 1
                continue

            # Bullet points
            if stripped.startswith('- ') or stripped.startswith('* '):
                text = stripped[2:]
                # Clean markdown formatting
                text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
                text = re.sub(r'\*(.+?)\*', r'\1', text)
                self.add_bullet(text)
                i += 1
                continue

            # Numbered list
            if re.match(r'^\d+\.\s', stripped):
                text = re.sub(r'^\d+\.\s', '', stripped)
                text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
                text = re.sub(r'\*(.+?)\*', r'\1', text)
                self.add_bullet(text)
                i += 1
                continue

            # Checkbox items
            if stripped.startswith('- [ ] ') or stripped.startswith('- [x] '):
                text = stripped[6:]
                text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
                self.add_bullet("[ ] " + text)
                i += 1
                continue

            # Table rows (simple handling)
            if '|' in stripped and stripped.startswith('|'):
                # Skip separator rows
                if re.match(r'^\|[\s\-:|]+\|$', stripped):
                    i += 1
                    continue
                cells = [c.strip() for c in stripped.split('|')[1:-1]]
                row_text = '  |  '.join(cells)
                self.add_code_line(row_text)
                i += 1
                continue

            # Regular paragraph
            # Clean markdown formatting
            text = re.sub(r'\*\*(.+?)\*\*', r'\1', stripped)
            text = re.sub(r'\*(.+?)\*', r'\1', text)
            text = re.sub(r'`(.+?)`', r'\1', text)
            text = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', text)
            self.add_paragraph(text)
            i += 1

    def _build_pdf(self):
        """Build the final PDF file content."""
        # Finalize last page
        if self.current_page_content:
            self.pages.append(self.current_page_content)

        output = []
        self.objects = []
        self.object_offsets = []

        # PDF Header
        output.append(b'%PDF-1.4\n%\xe2\xe3\xcf\xd3\n')

        # Object 1: Catalog
        self._add_object(output, b'<< /Type /Catalog /Pages 2 0 R >>')

        # Object 2: Pages (placeholder - we'll update)
        page_count = len(self.pages)
        kids = ' '.join([f'{i+4} 0 R' for i in range(page_count)])
        pages_obj = f'<< /Type /Pages /Kids [{kids}] /Count {page_count} >>'.encode()
        self._add_object(output, pages_obj)

        # Object 3: Font resources
        font_obj = (
            b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica '
            b'/Encoding /WinAnsiEncoding >>'
        )
        self._add_object(output, font_obj)

        # Object 3b: Bold font
        font_bold_obj = (
            b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold '
            b'/Encoding /WinAnsiEncoding >>'
        )
        self._add_object(output, font_bold_obj)

        # Now we have objects 1-4 (catalog, pages, font, font-bold)
        # Pages start at object 5 (index 4)
        # But we said kids start at 4+1=5... let's recalculate
        # Objects so far: 1=Catalog, 2=Pages, 3=Font, 4=FontBold
        # Page objects start at 5
        # Each page needs 2 objects: page dict + content stream

        # Rebuild pages reference
        self.objects = []
        self.object_offsets = []
        output = []
        output.append(b'%PDF-1.4\n%\xe2\xe3\xcf\xd3\n')

        # Calculate object numbers
        # 1: Catalog
        # 2: Pages
        # 3: Font (Helvetica)
        # 4: Font Bold (Helvetica-Bold)
        # 5,6: Page 1 (page dict, content stream)
        # 7,8: Page 2...
        # etc.

        base_page_obj = 5
        page_obj_nums = []
        for i in range(page_count):
            page_obj_nums.append(base_page_obj + i * 2)

        # Object 1: Catalog
        self._add_object(output, b'<< /Type /Catalog /Pages 2 0 R >>')

        # Object 2: Pages
        kids = ' '.join([f'{n} 0 R' for n in page_obj_nums])
        pages_content = f'<< /Type /Pages /Kids [{kids}] /Count {page_count} >>'.encode()
        self._add_object(output, pages_content)

        # Object 3: Font
        self._add_object(output, font_obj)

        # Object 4: Font Bold
        self._add_object(output, font_bold_obj)

        # Page objects
        for idx, page_content in enumerate(self.pages):
            page_obj_num = base_page_obj + idx * 2
            content_obj_num = page_obj_num + 1

            # Build content stream
            stream_text = '\n'.join(page_content)
            stream_bytes = stream_text.encode('latin-1', errors='replace')

            # Page dictionary
            page_dict = (
                f'<< /Type /Page /Parent 2 0 R '
                f'/MediaBox [0 0 {self.page_width} {self.page_height}] '
                f'/Contents {content_obj_num} 0 R '
                f'/Resources << /Font << /F1 3 0 R /F2 4 0 R >> >> >>'
            ).encode()
            self._add_object(output, page_dict)

            # Content stream
            stream_obj = (
                f'<< /Length {len(stream_bytes)} >>\n'
                f'stream\n'
            ).encode() + stream_bytes + b'\nendstream'
            self._add_object(output, stream_obj)

        # Cross-reference table
        xref_offset = sum(len(b) for b in output)
        output.append(b'xref\n')
        output.append(f'0 {len(self.object_offsets) + 1}\n'.encode())
        output.append(b'0000000000 65535 f \n')
        for offset in self.object_offsets:
            output.append(f'{offset:010d} 00000 n \n'.encode())

        # Trailer
        output.append(b'trailer\n')
        output.append(f'<< /Size {len(self.object_offsets) + 1} /Root 1 0 R >>\n'.encode())
        output.append(b'startxref\n')
        output.append(f'{xref_offset}\n'.encode())
        output.append(b'%%EOF\n')

        return b''.join(output)

    def _add_object(self, output, content):
        """Add a PDF object and track its offset."""
        obj_num = len(self.object_offsets) + 1
        offset = sum(len(b) for b in output)
        self.object_offsets.append(offset)

        obj_header = f'{obj_num} 0 obj\n'.encode()
        obj_footer = b'\nendobj\n'

        output.append(obj_header)
        if isinstance(content, str):
            output.append(content.encode())
        else:
            output.append(content)
        output.append(obj_footer)

    def save(self, filepath):
        """Save the PDF to a file."""
        pdf_data = self._build_pdf()
        os.makedirs(os.path.dirname(filepath) if os.path.dirname(filepath) else '.', exist_ok=True)
        with open(filepath, 'wb') as f:
            f.write(pdf_data)
        return len(pdf_data)


def convert_markdown_to_pdf(md_filepath, pdf_filepath, title="Document"):
    """Convert a markdown file to PDF."""
    with open(md_filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    pdf = PurePDF(title=title)
    pdf.add_title(title)
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.parse_markdown(content)

    size = pdf.save(pdf_filepath)
    return size


def main():
    """Generate all PDFs."""
    base_dir = '/projects/sandbox/CLAUDE/kdp-childrens-bible-strategy'
    pdf_dir = os.path.join(base_dir, 'pdf-downloads')
    os.makedirs(pdf_dir, exist_ok=True)

    print("=" * 60)
    print("  KDP Bible Book Series — PDF Generator")
    print("  Author: Selam Fesehaye")
    print("=" * 60)
    print()

    files_to_convert = [
        {
            'title': 'KDP Publishing Strategy - Selam Fesehaye',
            'input': os.path.join(base_dir, 'KDP-Strategy-Selam-Fesehaye.md'),
            'output': os.path.join(pdf_dir, '01-KDP-Strategy-Overview.pdf'),
        },
        {
            'title': 'Book #1: Bible Activity Book - Complete Manuscript',
            'input': 'COMBINED',  # We'll combine all 4 sections
            'sections': [
                os.path.join(base_dir, 'book-01-bible-activity-book/section-1-coloring-pages.md'),
                os.path.join(base_dir, 'book-01-bible-activity-book/section-2-handwriting-practice.md'),
                os.path.join(base_dir, 'book-01-bible-activity-book/section-3-word-searches-puzzles.md'),
                os.path.join(base_dir, 'book-01-bible-activity-book/section-4-mazes-fun-pages.md'),
            ],
            'output': os.path.join(pdf_dir, '02-Book1-Bible-Activity-Book-Manuscript.pdf'),
        },
        {
            'title': 'Book #1: Illustration Prompts (AI Image Generation)',
            'input': os.path.join(base_dir, 'book-01-bible-activity-book/illustration-prompts.md'),
            'output': os.path.join(pdf_dir, '03-Book1-Illustration-Prompts.pdf'),
        },
        {
            'title': 'Book #2: My First Bible ABC Book - Complete Manuscript',
            'input': os.path.join(base_dir, 'book-02-bible-abc/complete-manuscript.md'),
            'output': os.path.join(pdf_dir, '04-Book2-Bible-ABC-Manuscript.pdf'),
        },
        {
            'title': 'Amazon Ads Keyword Strategy',
            'input': os.path.join(base_dir, 'amazon-ads-keywords.md'),
            'output': os.path.join(pdf_dir, '05-Amazon-Ads-Keywords.pdf'),
        },
    ]

    results = []

    for i, item in enumerate(files_to_convert, 1):
        print(f"[{i}/{len(files_to_convert)}] Generating: {item['title']}")

        try:
            if item['input'] == 'COMBINED':
                # Combine multiple markdown files
                pdf = PurePDF(title=item['title'])
                pdf.add_title(item['title'])
                pdf.add_paragraph("By Selam Fesehaye | Little Believers Series")
                pdf.add_separator()

                for section_path in item['sections']:
                    if os.path.exists(section_path):
                        with open(section_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        pdf.add_page_break()
                        pdf.parse_markdown(content)
                        print(f"    + Added: {os.path.basename(section_path)}")
                    else:
                        print(f"    ! Missing: {section_path}")

                size = pdf.save(item['output'])
            else:
                if not os.path.exists(item['input']):
                    print(f"    ! File not found: {item['input']}")
                    continue
                size = convert_markdown_to_pdf(item['input'], item['output'], item['title'])

            size_kb = size / 1024
            print(f"    -> Saved: {item['output']}")
            print(f"    -> Size: {size_kb:.1f} KB")
            results.append({'title': item['title'], 'path': item['output'], 'size': size_kb})
            print()

        except Exception as e:
            print(f"    ! ERROR: {str(e)}")
            import traceback
            traceback.print_exc()
            print()

    # Print summary
    print()
    print("=" * 60)
    print("  GENERATION COMPLETE")
    print("=" * 60)
    print()
    print(f"  PDFs generated: {len(results)}/{len(files_to_convert)}")
    print(f"  Output directory: {pdf_dir}/")
    print()
    print("  Files:")
    for r in results:
        print(f"    [{r['size']:.0f} KB] {os.path.basename(r['path'])}")
    print()
    total_size = sum(r['size'] for r in results)
    print(f"  Total size: {total_size:.0f} KB ({total_size/1024:.1f} MB)")
    print()

    return results


if __name__ == '__main__':
    main()
