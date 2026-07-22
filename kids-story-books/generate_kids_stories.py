#!/usr/bin/env python3
"""
Kids Story Books Generator - 10 Illustrated Storybooks with Morals
Author: Daniel Tesfamariam
Target Ages: 4-10 years old
Each book: 30-35 pages with complete narratives
"""

import os
import sys

# Import PurePDF from the etsy strategy project
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'etsy-digital-products-strategy', 'generate_pdfs.py')).read())

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pdf-output')
os.makedirs(OUTPUT_DIR, exist_ok=True)

AUTHOR = "Daniel Tesfamariam"


def create_cover_page(pdf, title, moral_theme):
    """Create the cover page for a story book."""
    pdf.add_blank_line()
    pdf.add_blank_line()
    pdf.add_blank_line()
    pdf.add_title(title)
    pdf.add_blank_line()
    pdf.add_paragraph(f"A story about {moral_theme}")
    pdf.add_blank_line()
    pdf.add_blank_line()
    pdf.add_paragraph(f"Written by {AUTHOR}")
    pdf.add_blank_line()
    pdf.add_paragraph("For children ages 4-10")
    pdf.add_blank_line()
    pdf.add_paragraph("[Illustration: Beautiful, colorful cover art depicting the main character]")
    pdf.add_page_break()


def create_dedication_page(pdf, dedication_text):
    """Create a dedication page."""
    pdf.add_blank_line()
    pdf.add_blank_line()
    pdf.add_blank_line()
    pdf.add_heading2("Dedication")
    pdf.add_blank_line()
    pdf.add_paragraph(dedication_text)
    pdf.add_page_break()


def create_moral_page(pdf, moral_title, moral_text):
    """Create the moral of the story page."""
    pdf.add_heading1("The Moral of the Story")
    pdf.add_blank_line()
    pdf.add_heading2(moral_title)
    pdf.add_blank_line()
    pdf.add_paragraph(moral_text)
    pdf.add_page_break()



def create_discussion_page(pdf, questions):
    """Create discussion questions for parents."""
    pdf.add_heading1("Discussion Questions for Parents")
    pdf.add_blank_line()
    pdf.add_paragraph("After reading this story together, talk about these questions:")
    pdf.add_blank_line()
    for i, q in enumerate(questions, 1):
        pdf.add_paragraph(f"{i}. {q}")
        pdf.add_blank_line()
    pdf.add_page_break()


def create_about_author_page(pdf):
    """Create about the author page."""
    pdf.add_heading1("About the Author")
    pdf.add_blank_line()
    pdf.add_paragraph(f"{AUTHOR} is a storyteller who believes every child deserves")
    pdf.add_paragraph("stories that spark imagination, build character, and fill hearts with wonder.")
    pdf.add_blank_line()
    pdf.add_paragraph("His stories are crafted to help children understand important life lessons")
    pdf.add_paragraph("through adventure, friendship, and the magic of imagination.")
    pdf.add_blank_line()
    pdf.add_paragraph("When not writing, Daniel enjoys spending time with family, exploring nature,")
    pdf.add_paragraph("and dreaming up new worlds for young readers to discover.")
    pdf.add_blank_line()
    pdf.add_paragraph("Thank you for reading! If your child enjoyed this story,")
    pdf.add_paragraph("please look for other books in the collection.")


def add_story_page(pdf, page_num, text_paragraphs, illustration_desc):
    """Add a story page with text and illustration description."""
    pdf.add_heading3(f"Page {page_num}")
    pdf.add_blank_line()
    for para in text_paragraphs:
        pdf.add_paragraph(para)
    pdf.add_blank_line()
    pdf.add_paragraph(f"[Illustration: {illustration_desc}]")
    pdf.add_page_break()



# ============================================================
# BOOK 1: The Little Star Who Lost Her Sparkle
# ============================================================
def generate_book_01():
    """The Little Star Who Lost Her Sparkle - Moral: You are special just as you are."""
    pdf = PurePDF(title="The Little Star Who Lost Her Sparkle", author=AUTHOR)

    create_cover_page(pdf, "The Little Star Who Lost Her Sparkle", "self-worth and being special just as you are")
    create_dedication_page(pdf, "To every child who has ever felt small or unseen — you shine brighter than you know.")

    # Page 1
    add_story_page(pdf, 1,
        ["High above the world, in a sky full of twinkling lights, there lived a little star named Stella.",
         "Stella lived on the very edge of the Milky Way, far from the big, bright stars in the center.",
         "Every night, she would flicker her tiny light and wonder if anyone down on Earth could see her.",
         "She tried her very best to shine, but her glow was soft and gentle, like a whisper in the dark."],
        "A vast night sky with hundreds of bright stars, and one small, pale star sitting alone at the edge, looking wistful")

    # Page 2
    add_story_page(pdf, 2,
        ["The other stars around Stella were dazzling. There was Blaze, who burned bright orange and could be seen from every continent.",
         "And Shimmer, whose silver light made the ocean sparkle like diamonds at night.",
         "Even little Twinkle, who was younger than Stella, had a cheerful golden glow that made children point and smile.",
         "Stella watched them all and sighed. 'Why can't I shine like that?' she whispered to the darkness."],
        "Three magnificent stars shining brilliantly in different colors — orange, silver, and gold — while tiny Stella watches from the corner")


    # Page 3
    add_story_page(pdf, 3,
        ["One night, the Moon floated by on her silver path across the sky.",
         "'Why so sad, little one?' the Moon asked in her deep, gentle voice.",
         "'I'm not bright enough,' Stella said. 'No one on Earth can see me. I'm useless.'",
         "The Moon smiled kindly. 'Every star has a purpose, dear. Perhaps you just haven't found yours yet.'"],
        "A large, gentle crescent moon with a wise face leaning down to talk to tiny Stella, surrounded by soft moonbeams")

    # Page 4
    add_story_page(pdf, 4,
        ["That gave Stella an idea. 'If I can't find my purpose up here, maybe I should go looking for it!'",
         "She had heard old stories about stars that fell to Earth — shooting stars, the humans called them.",
         "But no star had ever gone looking for their purpose before. It was unheard of!",
         "'Be brave, little one,' the Moon called after her. 'And remember — you already have everything you need.'"],
        "Stella leaping off her spot in the sky, beginning to fall toward Earth like a tiny shooting star, with the Moon waving goodbye")

    # Page 5
    add_story_page(pdf, 5,
        ["Stella tumbled through the atmosphere, spinning and swirling until she landed softly in a meadow.",
         "Her light was even dimmer now on the ground, just a faint warm glow around her small form.",
         "She looked around at the dark field stretching in every direction. The grass was wet with dew.",
         "Above her, she could see all the other stars twinkling brightly. They looked so far away now.",
         "'Okay,' she told herself. 'Time to find out what makes me special.'"],
        "A tiny glowing star sitting in a dark meadow at night, looking up at the sky full of bright stars above, dewdrops on the grass reflecting her faint light")


    # Page 6
    add_story_page(pdf, 6,
        ["Stella wandered through a dark forest, her glow lighting only a tiny circle around her.",
         "She met a firefly named Flash who was zooming between trees.",
         "'Wow, you're not very bright, are you?' Flash said, blinking his green light rapidly.",
         "'I know,' Stella said sadly. 'I'm looking for what makes me special. Can you help?'",
         "Flash laughed. 'Special? You need to be BRIGHT to be special! Watch this!' He zoomed away in a burst of green."],
        "Stella walking through a dark forest path, meeting a cocky firefly who is showing off his bright green flashing light")

    # Page 7
    add_story_page(pdf, 7,
        ["Next, Stella came to a river where the water was dark and rushing.",
         "On the bank sat a little girl, hugging her knees and crying.",
         "'Are you okay?' Stella asked softly, floating closer.",
         "The girl looked up with tear-stained cheeks. 'I'm lost! I was camping with my family and I wandered too far. It's so dark and I can't find my way back!'"],
        "A scared little girl sitting by a dark river bank at night, crying, with tiny Stella floating nearby casting a gentle warm glow")

    # Page 8
    add_story_page(pdf, 8,
        ["Stella's heart ached for the frightened girl. 'Don't worry,' she said. 'I'll help you.'",
         "But then she remembered — her light was so dim. How could she possibly help?",
         "Still, she floated up above the girl's head, trying her very hardest to glow.",
         "Something strange happened. Her light didn't get brighter, but it got warmer. It was soft and steady, like a nightlight.",
         "The girl stopped crying. 'Your light... it's so gentle. It makes me feel safe.'"],
        "Stella floating above the girl's head, casting a soft warm golden glow like a nightlight, the girl looking up with hope replacing her tears")


    # Page 9
    add_story_page(pdf, 9,
        ["'Follow my light,' Stella said gently. She floated slowly along the riverbank.",
         "The girl stood up and walked beneath Stella's warm glow. It wasn't bright enough to light up the whole forest.",
         "But it was just enough to see the next step. Just enough to not feel alone in the dark.",
         "They walked together, one small step at a time, the girl's hand reaching up toward Stella's warmth."],
        "The girl walking along a forest path at night, following Stella who floats just ahead, creating a small warm circle of light around them both")

    # Page 10
    add_story_page(pdf, 10,
        ["After a while, they heard voices calling in the distance. 'Maya! Maya, where are you?'",
         "'That's my mom and dad!' the girl — Maya — cried with joy.",
         "She ran toward the voices, then stopped and turned back to Stella.",
         "'Thank you, little star. Your light is the most beautiful light I've ever seen. It found me when I was lost.'",
         "Stella felt something warm bloom inside her. For the first time, she didn't feel dim at all."],
        "Maya running toward flashlight beams in the distance where her parents are searching, turning back to wave at Stella with a grateful smile")

    # Page 11
    add_story_page(pdf, 11,
        ["Stella continued her journey, now feeling a tiny bit better about herself.",
         "She came to a village where all the houses were dark. The power had gone out.",
         "On one porch sat an old man, staring into the blackness. He looked lonely and afraid.",
         "'The dark is so heavy tonight,' the old man muttered. 'I wish I had just a small light to keep me company.'"],
        "A dark village with no lights in any window, an elderly man sitting alone on his porch looking worried, Stella approaching from the road")


    # Page 12
    add_story_page(pdf, 12,
        ["Stella floated over and settled on the porch railing beside the old man.",
         "Her soft glow was like a candle in the darkness — not blinding, not overwhelming, just... peaceful.",
         "'Well now,' the old man smiled, 'where did you come from, little light?'",
         "He reached out his wrinkled hand and Stella nestled closer. 'You're just what I needed tonight.'",
         "They sat together in comfortable silence, Stella's warmth keeping the loneliness away."],
        "The old man smiling peacefully on his porch with tiny Stella glowing on the railing beside him like a small candle, casting a warm intimate light")

    # Page 13
    add_story_page(pdf, 13,
        ["As the night went on, other people in the village noticed the small, steady light on the old man's porch.",
         "One by one, neighbors came outside. 'Is that a star?' they whispered to each other.",
         "Soon, a small crowd had gathered around the gentle glow, sharing stories and laughter.",
         "A mother brought her baby, who had been crying in the dark. The baby saw Stella's light and giggled, reaching out tiny fingers."],
        "Villagers gathering around the old man's porch, drawn to Stella's gentle glow, neighbors talking and smiling, a baby reaching toward the light")

    # Page 14
    add_story_page(pdf, 14,
        ["'Your light brings people together,' the old man told Stella. 'That's a wonderful gift.'",
         "Stella thought about this. Blaze was bright enough to see from far away, but his light was harsh — you couldn't look directly at him.",
         "Shimmer was beautiful, but cold and distant. Nobody gathered around Shimmer to share stories.",
         "Maybe being gentle wasn't a weakness at all. Maybe it was exactly right."],
        "Stella having a realization, her glow brightening slightly as she looks at the happy community gathered in the warm light around her")


    # Page 15
    add_story_page(pdf, 15,
        ["Stella said goodbye to the village and continued floating along a dark country road.",
         "She came across a boy riding his bicycle, wobbling nervously in the pitch-black night.",
         "'I have to get home,' the boy said, his voice shaky. 'But I can't see the road!'",
         "Stella floated down and hovered just above his front wheel, lighting the path ahead — just enough to see the next few feet."],
        "A boy on a bicycle at night on a dark road, with Stella glowing softly above his front wheel, illuminating just enough road ahead to ride safely")

    # Page 16
    add_story_page(pdf, 16,
        ["'You're perfect!' the boy laughed as he pedaled. 'Not too bright to blind me, not too dim to miss the bumps.'",
         "Together they rode through the night, Stella guiding him over potholes and around curves.",
         "When they reached his house, the boy's mother was waiting at the door, worried.",
         "'Mom! Look! A star helped me get home!' he exclaimed, pointing at Stella.",
         "His mother smiled. 'What a special little star. Thank you for bringing my boy home safe.'"],
        "The boy arriving home safely on his bicycle, his relieved mother at the door, Stella glowing proudly above the bike wheel")

    # Page 17
    add_story_page(pdf, 17,
        ["By now, Stella was beginning to understand something important.",
         "She had helped Maya find her parents. She had kept the old man company. She had brought a village together. She had guided the boy home safely.",
         "None of those things needed a blinding, powerful light.",
         "They needed exactly what she had — a soft, warm, steady glow that made people feel safe and loved.",
         "Her kind of light was not less than the other stars. It was different. And different was exactly what the world needed."],
        "Stella floating in the night sky with a montage of all the people she helped visible below — Maya, the old man, the villagers, the boy — all smiling up at her")


    # Page 18
    add_story_page(pdf, 18,
        ["Stella decided it was time to go home, back up to the sky where she belonged.",
         "She rose higher and higher, past the treetops and clouds, back toward the stars.",
         "As she climbed, she noticed something amazing — she was leaving a trail of soft golden light behind her.",
         "Down below, people pointed and gasped. 'A shooting star! Make a wish!'"],
        "Stella rising up from the Earth back toward the sky, leaving a beautiful golden trail, people on the ground pointing up in wonder")

    # Page 19
    add_story_page(pdf, 19,
        ["When Stella returned to her spot at the edge of the Milky Way, the Moon was waiting.",
         "'Welcome home, little one,' the Moon said with a knowing smile. 'Did you find your purpose?'",
         "Stella glowed — and this time, her glow was warm and proud. 'I did! I'm not meant to light up the whole sky.'",
         "'I'm meant to light up the spaces in between — the dark, lonely, scary places where people need a gentle friend.'"],
        "Stella back in her place in the sky, talking to the smiling Moon, with a warm confident glow around her")

    # Page 20
    add_story_page(pdf, 20,
        ["The other stars gathered around, curious about Stella's adventure.",
         "'You went to Earth?' Blaze asked, impressed. 'I've never been brave enough to do that!'",
         "'People actually LIKED your dim light?' Shimmer asked, confused.",
         "'It's not dim,' Stella said firmly. 'It's gentle. And gentle is exactly what scared people need in the dark.'",
         "For the first time, the other stars looked at Stella with admiration instead of pity."],
        "Stella surrounded by the other stars who are listening with interest and amazement, their expressions showing new respect for her")


    # Page 21
    add_story_page(pdf, 21,
        ["From that night on, Stella never wished to be different again.",
         "She was the star that travelers looked for when they were lost — her steady, gentle light guided them home.",
         "She was the star that children saw from their bedroom windows and whispered goodnight to.",
         "She was the star that reminded people: you don't have to be the biggest or brightest to matter."],
        "A peaceful night sky scene showing Stella in her spot, with a child in a window below looking up and smiling at her gentle light")

    # Page 22
    add_story_page(pdf, 22,
        ["And sometimes, when a child felt small or invisible, they would look up and find Stella's soft light.",
         "It seemed to whisper: 'I see you. You are enough. You are special just as you are.'",
         "Because that's what Stella had learned on her great journey —",
         "the world doesn't just need bright lights. It needs gentle ones too.",
         "And being gentle, being soft, being exactly who you are... that is the most special thing of all."],
        "A child lying in bed, looking out the window at Stella's gentle star, with a peaceful smile, feeling comforted and seen")

    # Page 23
    add_story_page(pdf, 23,
        ["Now, whenever you look up at the night sky, see if you can find Stella.",
         "She's the small, steady light at the edge — not the flashiest, not the biggest.",
         "But she's the one that makes you feel warm inside. The one that makes the dark feel less scary.",
         "And she wants you to know: your light matters too, no matter how small it seems.",
         "So shine your own way, little one. The world needs exactly the kind of light that only you can give."],
        "A beautiful panoramic night sky filled with stars of all sizes, with Stella's soft warm glow visible at the edge, and a child standing in a field looking up peacefully")

    # Page 24
    add_story_page(pdf, 24,
        ["Because here is the beautiful truth about light:",
         "A candle in a dark room is more precious than a bonfire in broad daylight.",
         "A whisper of comfort is more powerful than a shout that nobody hears.",
         "And a gentle glow that says 'you are not alone' can change someone's entire night.",
         "That is who you are. That is what you give. And it is more than enough."],
        "A single candle glowing in a dark room, illuminating a child's peaceful sleeping face, showing that small lights can be the most precious and comforting of all")

    # Page 25
    add_story_page(pdf, 25,
        ["And if you ever forget — if you ever feel dim or small or invisible —",
         "just look up at the night sky and find the softest, warmest star you can see.",
         "That is Stella, smiling down at you, reminding you:",
         "You are special. You are enough. You are loved.",
         "Just exactly as you are."],
        "A final peaceful nighttime image — a child tucked in bed, starlight streaming through the window, Stella's gentle glow among the stars, warmth and love and belonging in every detail")

    # Moral page
    create_moral_page(pdf, "You Are Special Just As You Are",
        "Stella learned that she didn't need to shine like everyone else to be important. Her gentle, soft light was exactly what scared and lonely people needed. You don't have to be the loudest, fastest, or brightest to matter. Your unique gifts — whether they're kindness, gentleness, listening, or simply being there — are exactly what someone in the world needs. Never wish to be someone else. The world needs you, just as you are.")

    # Discussion Questions
    create_discussion_page(pdf, [
        "Have you ever felt like you weren't as good as someone else at something? How did that feel?",
        "What are some things that make YOU special and different from everyone else?",
        "Why do you think gentle things (like a nightlight or a quiet friend) are sometimes better than loud, bright things?",
        "If you could help someone with your own special gift, who would you help and how?",
        "Can you think of a time when someone's kindness (not loudness or brightness) made you feel better?"
    ])

    # About Author
    create_about_author_page(pdf)

    filepath = os.path.join(OUTPUT_DIR, "01-The-Little-Star-Who-Lost-Her-Sparkle.pdf")
    size = pdf.save(filepath)
    return filepath, size



# ============================================================
# BOOK 2: Kalu the Brave Little Elephant
# ============================================================
def generate_book_02():
    """Kalu the Brave Little Elephant - Moral: Courage isn't being fearless."""
    pdf = PurePDF(title="Kalu the Brave Little Elephant", author=AUTHOR)

    create_cover_page(pdf, "Kalu the Brave Little Elephant", "courage and doing the right thing even when you're scared")
    create_dedication_page(pdf, "To every child who has ever been afraid — being brave doesn't mean you're not scared. It means you keep going anyway.")

    # Page 1
    add_story_page(pdf, 1,
        ["In the golden savanna of Africa, where the grass grew tall and the sun painted everything amber, there lived a baby elephant named Kalu.",
         "Kalu was the smallest elephant in his herd. His ears were too big, his trunk was too short, and his legs were a little wobbly.",
         "But the thing that made Kalu different from every other elephant was this: Kalu was terrified of water.",
         "Every other elephant loved splashing in rivers and lakes. But not Kalu. Water made his knees shake."],
        "A small baby elephant with oversized ears standing at the edge of the savanna, looking nervously at a distant river while other elephants play in the water happily")

    # Page 2
    add_story_page(pdf, 2,
        ["'Come in, Kalu! The water is wonderful!' his mother called from the river every afternoon.",
         "But Kalu would shake his big ears and back away. 'N-no thank you, Mama. I'll just stay here.'",
         "The other young elephants teased him. 'Kalu is a scaredy-elephant! Kalu is afraid of a little water!'",
         "Kalu's ears drooped with shame. He wished he could be brave, but when he looked at the rushing water, his whole body froze."],
        "Young elephants splashing and playing in a river while Kalu stands far back on the bank, ears drooped, looking embarrassed as other baby elephants laugh")


    # Page 3
    add_story_page(pdf, 3,
        ["One day, Kalu asked his grandmother, the oldest and wisest elephant in the herd, 'Grandma, why am I so scared?'",
         "Grandmother Elephant wrapped her trunk around him gently. 'Everyone is afraid of something, little one.'",
         "'Even you?' Kalu asked, his eyes wide.",
         "'Even me,' she said. 'I'm afraid of losing the ones I love. But fear doesn't make you weak, Kalu. What you DO with your fear — that's what matters.'"],
        "An ancient, wise grandmother elephant with kind eyes wrapping her trunk lovingly around small Kalu under an acacia tree at sunset")

    # Page 4
    add_story_page(pdf, 4,
        ["One morning, the herd's leader, Big Tembo, raised his trunk and trumpeted loudly.",
         "'The dry season is coming! We must cross the Great River to reach the green lands on the other side!'",
         "All the elephants nodded. They had made this journey every year. The Great River was wide and deep, but the herd always crossed together.",
         "Kalu's heart sank to his toes. The Great River? That was the biggest, scariest water he could imagine!"],
        "A massive bull elephant trumpeting an announcement to the gathered herd on a dry golden plain, with a wide blue river visible in the distance")

    # Page 5
    add_story_page(pdf, 5,
        ["For three days, the herd walked toward the Great River. Kalu walked at the very back, his steps getting slower and slower.",
         "His best friend, a young elephant named Zuri, walked beside him. 'Are you okay, Kalu?'",
         "'I can't do it, Zuri,' Kalu whispered. 'I can't cross that river. I'll drown. I just know it.'",
         "Zuri bumped him gently with her trunk. 'I'll be right beside you. We'll do it together, okay?'"],
        "The elephant herd marching in a line across the golden savanna toward a distant river, with Kalu trailing behind, a slightly larger young elephant named Zuri walking supportively beside him")


    # Page 6
    add_story_page(pdf, 6,
        ["When they finally reached the Great River, Kalu gasped. It was even bigger than he imagined.",
         "The water rushed past, brown and powerful, churning with white foam over hidden rocks.",
         "One by one, the adult elephants waded in, their strong legs fighting the current.",
         "The babies rode on their mothers' backs. But Kalu was too big to ride on his mother anymore.",
         "He stood at the edge, trembling, his feet planted firmly on dry ground."],
        "The herd entering a wide, rushing brown river with white water rapids, adult elephants wading in bravely, while Kalu stands frozen at the water's edge trembling")

    # Page 7
    add_story_page(pdf, 7,
        ["'Come on, Kalu!' his mother called from the middle of the river. 'Just walk in slowly! I'm right here!'",
         "Kalu put one foot forward. The cold water touched his toes and he jumped back with a trumpet of fear.",
         "The other young elephants were already across, watching from the far bank. Some were giggling.",
         "Kalu felt hot tears in his eyes. He wanted to run away. He wanted to disappear.",
         "'I can't,' he whispered. 'I just can't.'"],
        "Kalu at the very edge of the rushing river with one foot barely touching the water, pulling back in fear, his mother reaching her trunk toward him from the middle of the river")

    # Page 8
    add_story_page(pdf, 8,
        ["Just then, a terrible sound echoed through the air. CRACK! RUMBLE!",
         "Everyone looked upstream. A wall of water was racing down the river — a flash flood from the rains far away in the mountains!",
         "Big Tembo trumpeted in alarm. 'Everyone out! Get to higher ground!'",
         "The elephants in the river scrambled for the far bank. But in the chaos, Kalu heard a small, terrified cry."],
        "A massive wall of brown flood water rushing downstream toward the elephants in the river, adults scrambling to get out, a scene of urgent chaos")


    # Page 9
    add_story_page(pdf, 9,
        ["It was Zuri's baby brother, tiny Kofi! He had fallen off his mother's back in the panic.",
         "The little calf was floundering in the shallow water near the bank — the same bank where Kalu still stood.",
         "Kofi was too small to fight the current. And the flood was coming fast.",
         "His mother was on the other side, screaming. The adults couldn't get back in time.",
         "There was only one elephant close enough to save Kofi. And that elephant was Kalu."],
        "Tiny baby elephant Kofi flailing in shallow rushing water near the riverbank, with the flood wall approaching in the background, and Kalu on the bank nearby, the only one close enough to help")

    # Page 10
    add_story_page(pdf, 10,
        ["Kalu's whole body was shaking. His heart pounded so hard he could hear it in his ears.",
         "The water. The terrible, scary water. It was right there, rushing and roaring.",
         "But so was Kofi. A baby. A helpless baby who would be swept away forever if no one helped him.",
         "Kalu thought of his grandmother's words: 'What you DO with your fear — that's what matters.'",
         "And in that moment, Kalu made a choice."],
        "Close-up of Kalu's face showing intense fear but also determination in his eyes, the rushing water reflected in them, at the moment of his brave decision")

    # Page 11
    add_story_page(pdf, 11,
        ["Kalu charged into the water.",
         "The cold hit him like a slap. The current pulled at his legs. Everything in his body screamed to turn back.",
         "But he didn't turn back. He pushed forward, step by step, his eyes fixed on little Kofi.",
         "The water rose to his belly, then his chest. He was terrified. His legs were shaking. But he kept going.",
         "'I'm coming, Kofi! Hold on!' he trumpeted through his short trunk."],
        "Kalu charging bravely into the rushing river water, water splashing around him, his face showing fear but absolute determination, reaching toward baby Kofi")


    # Page 12
    add_story_page(pdf, 12,
        ["Kalu reached Kofi just as the flood surge arrived. The water rose and swirled around them both.",
         "Kalu wrapped his trunk around the tiny calf and held on with all his strength.",
         "The current tried to pull them downstream. Kalu planted his wobbly legs as firmly as he could.",
         "He was scared. So, so scared. But he would NOT let go of Kofi. Not ever."],
        "Kalu in chest-deep rushing water, trunk wrapped tightly around baby Kofi, bracing against the powerful current of the flood surge, water churning around them")

    # Page 13
    add_story_page(pdf, 13,
        ["With Kofi held safely in his trunk, Kalu turned back toward the bank he'd come from.",
         "Each step was a battle against the current. The water pushed and pulled and tried to knock him down.",
         "His big ears — the ones he'd always been embarrassed about — caught the water like sails, actually helping him balance.",
         "His short trunk held Kofi high above the waterline. His wobbly legs, spread wide, kept him steady like a tripod.",
         "Everything about Kalu that he thought was wrong was helping him now."],
        "Kalu pushing through chest-high water back toward the bank, trunk holding baby Kofi up above the water, his big ears spread for balance, showing strength and determination")

    # Page 14
    add_story_page(pdf, 14,
        ["With one final, mighty push, Kalu hauled himself and Kofi onto the muddy bank.",
         "They collapsed together on the grass, safe and exhausted, as the flood waters raged past them in the river.",
         "Kofi was crying but unhurt. He nuzzled against Kalu's side, trembling.",
         "'You saved me,' the tiny calf whispered. 'You came in the water even though you were scared.'",
         "Kalu was still shaking. But he managed a small smile. 'Yeah,' he said. 'I guess I did.'"],
        "Kalu and baby Kofi collapsed safely on the grassy riverbank, both exhausted and wet, the flood raging in the river behind them, Kofi nuzzling gratefully against Kalu")


    # Page 15
    add_story_page(pdf, 15,
        ["When the flood waters went down, the herd was able to cross back to Kalu's side.",
         "Zuri's mother rushed to Kofi, wrapping her trunk around him and crying with relief.",
         "'Kalu saved him!' Zuri shouted. 'He ran right into the water! The water he's afraid of!'",
         "Every elephant in the herd turned to look at Kalu — the small, scared elephant who had done the bravest thing any of them had ever seen."],
        "The herd reuniting on the bank, Zuri's mother embracing Kofi, all elephants looking at Kalu with amazement and admiration")

    # Page 16
    add_story_page(pdf, 16,
        ["Big Tembo, the herd leader, walked slowly up to Kalu and touched the young elephant's head with his trunk.",
         "'Today,' Big Tembo said in his deep, rumbling voice, 'I saw true courage.'",
         "'But I was scared the whole time,' Kalu said quietly. 'I was shaking. I was crying. That's not brave.'",
         "Big Tembo shook his massive head. 'No, young one. That is the BRAVEST kind of brave there is.'"],
        "The massive herd leader Big Tembo touching Kalu's head with his trunk in a gesture of honor and respect, the whole herd watching")

    # Page 17
    add_story_page(pdf, 17,
        ["'Anyone can do something when they're not afraid,' Big Tembo continued.",
         "'But to do the right thing when every part of you is screaming with fear? When your legs are shaking and your heart is pounding?'",
         "'That, Kalu, is real courage. Courage isn't the absence of fear. Courage is action in the presence of fear.'",
         "Kalu stood a little taller. He had never thought about it that way before."],
        "Kalu standing taller and prouder as Big Tembo speaks wise words, the other young elephants watching with new respect in their eyes")


    # Page 18
    add_story_page(pdf, 18,
        ["That night, Grandmother Elephant found Kalu and wrapped her trunk around him again.",
         "'I'm so proud of you,' she whispered. 'You found out what to do with your fear.'",
         "'I'm still afraid of water, Grandma,' Kalu admitted. 'My legs still shake when I see the river.'",
         "'And that's perfectly okay,' she said. 'Being brave doesn't mean the fear goes away. It means you don't let it stop you from doing what's right.'"],
        "Grandmother Elephant and Kalu under a starry night sky, her trunk around him lovingly, a peaceful nighttime savanna scene")

    # Page 19
    add_story_page(pdf, 19,
        ["The next day, when the flood waters had calmed and it was time to cross the river again, Kalu walked to the front of the line.",
         "His legs were still wobbly. His heart was still thumping. The water still scared him.",
         "But this time, he didn't stand frozen on the bank. He took a deep breath, thought of little Kofi, and stepped in.",
         "One step. Then another. Then another. Scared the whole time. But moving forward anyway."],
        "Kalu at the front of the elephant line, bravely stepping into the now-calm river, still visibly nervous but determined, with the whole herd watching proudly behind him")

    # Page 20
    add_story_page(pdf, 20,
        ["And the most beautiful thing happened: the young elephants who used to tease him fell into step beside him.",
         "'We'll cross together,' they said. No more teasing. No more laughing.",
         "Because they had learned something too — they learned that courage isn't about having no fear.",
         "It's about having a heart big enough to act even when fear fills it up.",
         "And Kalu? Kalu had the biggest heart of all."],
        "Kalu crossing the river surrounded by supportive young elephant friends on all sides, all walking together through the water, a scene of solidarity and friendship")


    # Page 21
    add_story_page(pdf, 21,
        ["From that day on, Kalu was known as the bravest elephant in the herd — not because he stopped being afraid.",
         "He was still afraid of water. He was still afraid of thunder. He was still afraid of the dark.",
         "But whenever someone needed help, whenever something right needed to be done, Kalu was always the first to step forward.",
         "Shaking legs and all."],
        "Kalu grown slightly bigger, leading the herd confidently past a river, still with slightly nervous eyes but head held high, a hero among his people")

    # Page 22
    add_story_page(pdf, 22,
        ["And whenever a young elephant came to him and said, 'Kalu, I'm too scared. I can't be brave.'",
         "Kalu would wrap his trunk around them and say what his grandmother had taught him:",
         "'Being brave doesn't mean you're not scared. Being brave means you do the right thing EVEN when you're scared.'",
         "'So be scared. Shake and tremble and cry if you need to. But then take that step anyway.'",
         "'That's what courage really is. And you have more of it than you know.'"],
        "Kalu as a young adult elephant, trunk wrapped around a small scared baby elephant, giving wisdom and comfort under an acacia tree at sunset, a beautiful passing-on-wisdom scene")

    # Page 23
    add_story_page(pdf, 23,
        ["And here is what Kalu wants to whisper in YOUR ear, dear reader:",
         "You are braver than you believe. There will be rivers in your life — things that scare you, things that seem impossible.",
         "Maybe it is the first day at a new school. Maybe it is standing up to a bully. Maybe it is trying something you have never done before.",
         "When that river comes, remember Kalu. Remember his shaking legs and pounding heart.",
         "And remember that he crossed anyway. Because courage is not the absence of fear. Courage is one step forward, even when you are terrified."],
        "A child facing something scary in their own life — perhaps the first day of school — with an imaginary Kalu standing behind them supportively, giving them strength")

    # Page 24
    add_story_page(pdf, 24,
        ["So when you feel scared, do not run from the feeling. Let it be there.",
         "Say to yourself: 'I am scared. And that is okay. I am still going to try.'",
         "Because every brave person who ever lived was scared first. Every hero trembled before they acted.",
         "The difference between a hero and everyone else is not that heroes feel no fear.",
         "It is that heroes feel the fear and move forward anyway. Just like Kalu. Just like you."],
        "A powerful final image of Kalu silhouetted against a sunset, standing tall at a river crossing, water flowing beneath him, strong and brave, an inspiration for all children facing their fears")

    # Page 25
    add_story_page(pdf, 25,
        ["What is YOUR river, dear reader? What is the thing that makes your knees shake and your heart pound?",
         "Maybe it is speaking in front of your class. Maybe it is making new friends. Maybe it is the dark, or heights, or trying something new.",
         "Whatever your river is — know this: you can cross it. Not because the fear will go away.",
         "But because YOU are brave enough to take that first step, even with shaking legs.",
         "Kalu believes in you. And so do I."],
        "A child standing at the edge of their own 'river' — something scary they must face — with the spirit of brave Kalu standing supportively behind them, giving them courage")

    # Moral page
    create_moral_page(pdf, "Courage Isn't Being Fearless",
        "Kalu taught us that being brave doesn't mean you're never scared. Real courage means doing the right thing even when you're terrified. Everyone is afraid of something — and that's okay! What matters is what you choose to do with your fear. You can let it freeze you in place, or you can take a deep breath, plant your feet, and step forward anyway. That's true bravery. And YOU are braver than you think.")

    # Discussion Questions
    create_discussion_page(pdf, [
        "What is something that makes you feel scared? Is it okay to feel that way?",
        "Can you think of a time when you did something even though you were afraid? How did it feel afterward?",
        "Why do you think the other elephants stopped teasing Kalu after he saved Kofi?",
        "What does Big Tembo mean when he says 'Courage is action in the presence of fear'?",
        "How can you be brave for someone else, even when you feel scared inside?"
    ])

    # About Author
    create_about_author_page(pdf)

    filepath = os.path.join(OUTPUT_DIR, "02-Kalu-the-Brave-Little-Elephant.pdf")
    size = pdf.save(filepath)
    return filepath, size



# ============================================================
# BOOK 3: The Garden of Kindness
# ============================================================
def generate_book_03():
    """The Garden of Kindness - Moral: Kindness grows when you share it."""
    pdf = PurePDF(title="The Garden of Kindness", author=AUTHOR)

    create_cover_page(pdf, "The Garden of Kindness", "how kindness grows when you share it with others")
    create_dedication_page(pdf, "To every child whose small act of kindness made someone's day brighter — you are planting beautiful flowers in the world.")

    # Page 1
    add_story_page(pdf, 1,
        ["In a cozy little town called Willowbrook, there lived a girl named Lina who loved two things: flowers and helping people.",
         "Every morning, Lina watered the small flower box outside her window and said good morning to each bloom.",
         "She knew all their names — Rose, Daisy, and her favorite, a tiny forget-me-not she called Blue.",
         "But lately, Lina had noticed something sad. The people in her town didn't smile much anymore."],
        "A cheerful young girl with braids watering a colorful window box of flowers outside a cozy cottage in a quaint small town, morning sunlight on her face")

    # Page 2
    add_story_page(pdf, 2,
        ["Mr. Abram at the bakery grumbled when customers came in. Mrs. Chen rushed past without saying hello.",
         "Even the children at school sat alone at lunch, staring at their plates in silence.",
         "Willowbrook used to be a happy place, but everyone seemed to have forgotten how to be kind to each other.",
         "'Why is everyone so grumpy?' Lina asked her grandmother one afternoon."],
        "A sad-looking small town street with people walking past each other without smiling, looking down at the ground, a gloomy gray atmosphere despite sunshine")

    # Page 3
    add_story_page(pdf, 3,
        ["Grandmother smiled her wise smile. 'Kindness is like a garden, dear. If no one plants seeds, nothing blooms.'",
         "'Then I'll plant seeds!' Lina declared. 'I'll be kind to everyone and maybe it will grow!'",
         "That night, Lina could barely sleep. She was going to bring kindness back to Willowbrook.",
         "She didn't know yet just how magical her plan would turn out to be."],
        "Grandmother and Lina sitting together on a porch swing, grandmother gesturing wisely, Lina looking determined and excited, evening golden light")


    # Page 4
    add_story_page(pdf, 4,
        ["The next morning, Lina started with Mr. Abram at the bakery.",
         "'Good morning, Mr. Abram! Your bread smells wonderful today!' she said with her brightest smile.",
         "Mr. Abram looked surprised. No one had complimented his bread in a long time.",
         "A tiny smile crept onto his flour-dusted face. 'Why... thank you, Lina. Would you like a fresh roll?'",
         "Lina skipped away with a warm roll and a warm feeling in her heart."],
        "Lina standing at a bakery counter, smiling up at a surprised older baker with flour on his apron, the bakery warm and full of bread loaves")

    # Page 5
    add_story_page(pdf, 5,
        ["That afternoon, something extraordinary happened.",
         "Lina was walking home through the old park when she noticed a path she'd never seen before.",
         "It was overgrown with vines and hidden behind a crumbling stone wall.",
         "Curious, Lina pushed through the vines and gasped. Behind the wall was a garden — but like no garden she'd ever seen.",
         "It was completely empty. Just dark, bare earth in a perfect circle, with a stone fountain in the center that had no water."],
        "Lina pushing through vines to discover a hidden circular garden behind a stone wall, the garden completely bare with dark earth and a dry stone fountain in the center")

    # Page 6
    add_story_page(pdf, 6,
        ["In the center of the fountain was a small carved sign. Lina brushed the dirt away and read:",
         "'THE GARDEN OF KINDNESS — Every kind act plants a seed. Every seed becomes a flower. Fill this garden with beauty.'",
         "Lina looked around the empty space. Not a single flower anywhere. Just bare, waiting earth.",
         "'Plant seeds of kindness,' she whispered. 'I wonder...'",
         "She thought about the kind thing she'd done that morning — complimenting Mr. Abram's bread."],
        "Close-up of Lina kneeling by the stone fountain, reading the carved sign about kindness planting seeds, her eyes wide with wonder and curiosity")


    # Page 7
    add_story_page(pdf, 7,
        ["As if the garden could hear her thoughts, a tiny green sprout pushed up through the dark earth.",
         "Lina gasped and knelt down to look closer. A perfect little stem with two small leaves unfurled before her eyes.",
         "It was real! Her kind act had literally planted something in this magical garden!",
         "Lina's heart danced. If one kind act made one sprout, what would happen if she was kind all day long?"],
        "A single tiny green sprout emerging from the dark bare earth while Lina watches in amazement, kneeling down close to it, magical sparkles around the sprout")

    # Page 8
    add_story_page(pdf, 8,
        ["The next day, Lina went to school on a kindness mission.",
         "She sat next to Tomás, a quiet boy who always ate lunch alone. 'Can I sit with you?' she asked.",
         "Tomás looked shocked, then slowly smiled. 'Really? You want to sit with me?'",
         "They talked about his favorite dinosaurs and her favorite flowers. By the end of lunch, Tomás was laughing for the first time in weeks.",
         "That afternoon, Lina ran to the secret garden. A beautiful blue flower had bloomed beside the sprout."],
        "Lina sitting happily at a lunch table with a shy boy who is smiling and talking excitedly about dinosaurs, both having a wonderful time together")

    # Page 9
    add_story_page(pdf, 9,
        ["Every day, Lina found new ways to be kind.",
         "She helped Mrs. Chen carry her heavy grocery bags. A purple flower appeared in the garden.",
         "She drew a cheerful picture for the school librarian who seemed sad. A yellow flower grew.",
         "She let her little brother choose the TV show, even though it wasn't the one she wanted. A pink flower bloomed.",
         "Day by day, the Garden of Kindness was coming to life — and so was Willowbrook."],
        "A montage showing Lina doing different kind acts — carrying bags, drawing pictures, being patient — with colorful flowers growing in the garden for each act")


    # Page 10
    add_story_page(pdf, 10,
        ["But then something even more magical started happening.",
         "Mr. Abram, who Lina had complimented, started giving free cookies to children who came into his shop.",
         "A red flower appeared in the garden — and Lina hadn't even been kind that day! Mr. Abram had!",
         "Mrs. Chen started saying hello to everyone on her street. Two more flowers bloomed.",
         "Lina realized: kindness was SPREADING. Other people's kind acts were growing the garden too!"],
        "The garden now having about fifteen colorful flowers, with new ones appearing magically as Lina watches with joyful surprise, sparkling with magic")

    # Page 11
    add_story_page(pdf, 11,
        ["Tomás, the boy she'd sat with at lunch, started inviting other lonely kids to join their table.",
         "Soon, their lunch table was the happiest in the whole cafeteria, full of laughter and new friendships.",
         "For each new friendship formed, another flower bloomed in the secret garden.",
         "The garden was half-full now, a riot of colors — roses, lilies, daisies, sunflowers, and flowers Lina had never even seen before."],
        "A crowded, happy lunch table full of laughing children who all look like they belong, with Tomás at the center welcoming a new kid to join them")

    # Page 12
    add_story_page(pdf, 12,
        ["One morning, Lina noticed something wonderful. The stone fountain in the center of the garden had started flowing!",
         "Crystal clear water bubbled up from the top and cascaded down the sides into a little pool.",
         "Around the pool, the most gorgeous flowers grew — deep blue forget-me-nots, just like her favorite flower, Blue.",
         "The garden was no longer bare and dark. It was becoming the most beautiful place in all of Willowbrook."],
        "The stone fountain now flowing with sparkling clear water, surrounded by gorgeous blue forget-me-nots, the garden lush and colorful, magical light filtering through")


    # Page 13
    add_story_page(pdf, 13,
        ["But then came a hard day. A girl named Petra said mean things about Lina's dress at school.",
         "'Your dress is old and ugly,' Petra sneered. 'My mom buys me new clothes every week.'",
         "Lina's eyes stung with tears. She wanted to say something mean back. She wanted to make Petra feel as bad as she felt.",
         "She opened her mouth to say something hurtful... but then she stopped. She remembered the garden."],
        "Lina at school looking hurt while a mean girl points at her dress and laughs, other kids watching uncomfortably, Lina's eyes filled with tears but her expression changing to thoughtfulness")

    # Page 14
    add_story_page(pdf, 14,
        ["Instead of being mean back, Lina took a deep breath and said, 'That hurt my feelings, Petra.'",
         "Then she said something that surprised everyone, including herself: 'Are you okay? People usually say mean things when they're hurting inside.'",
         "Petra's mouth fell open. Nobody had ever responded to her meanness with kindness before.",
         "Her tough expression cracked, and for just a moment, Lina saw sadness in Petra's eyes.",
         "'I... my parents are fighting a lot,' Petra whispered. 'I'm sorry about your dress. It's actually pretty.'"],
        "Lina reaching out her hand to Petra, who has dropped her mean facade and looks vulnerable and sad, a moment of connection between the two girls")

    # Page 15
    add_story_page(pdf, 15,
        ["That afternoon, Lina visited the garden and found the most amazing sight yet.",
         "Where she had been kind to Petra — kind even when it was hard — a massive sunflower had grown.",
         "It was taller than all the other flowers, golden and magnificent, standing proud in the center.",
         "Lina understood: kindness is easy when people are nice to you. But being kind when someone hurts you? That grows the biggest, most beautiful flower of all."],
        "An enormous, stunning golden sunflower towering over all the other flowers in the garden, glowing with warm light, Lina gazing up at it in awe")


    # Page 16
    add_story_page(pdf, 16,
        ["Weeks passed, and kindness became contagious in Willowbrook.",
         "Neighbors helped each other rake leaves. Children shared their snacks. The librarian started a free book exchange.",
         "Mr. Abram's bakery became a gathering place where people shared coffee and conversation.",
         "The garden behind the stone wall was now completely full — every inch of earth covered in gorgeous, colorful blooms."],
        "The town of Willowbrook transformed — people waving, helping each other, sharing food, children playing together, a bright and cheerful atmosphere")

    # Page 17
    add_story_page(pdf, 17,
        ["One day, Lina brought Tomás to see the secret garden. She wanted to share her discovery.",
         "'Whoa!' Tomás breathed. 'This is REAL? Every flower is a kind act?'",
         "'Every single one,' Lina smiled. 'And look — that blue one grew when you invited Marcus to sit with us. And that orange one was when you helped Sara with her math.'",
         "Tomás's eyes were shining. 'My kindness did that? My kindness made something beautiful grow?'"],
        "Tomás standing in the magnificent garden with Lina, mouth open in wonder, looking at specific flowers she's pointing to, the garden lush and spectacular")

    # Page 18
    add_story_page(pdf, 18,
        ["Soon, all the children in town knew about the Garden of Kindness.",
         "They visited every day, watching new flowers appear as kindness spread through Willowbrook.",
         "Every child wanted to grow the biggest, most beautiful flower. But not by competing —",
         "by being the most genuinely kind they could be. The garden had turned kindness into the most exciting game in town."],
        "A group of excited children of all ages in the beautiful garden, pointing at new flowers appearing, some high-fiving each other, joy and excitement everywhere")


    # Page 19
    add_story_page(pdf, 19,
        ["Even Petra became one of the kindest kids in Willowbrook.",
         "After Lina's kindness had reached her, Petra started being gentle with others too.",
         "She apologized to the kids she'd teased. She shared her new clothes with a girl whose family couldn't afford many.",
         "And in the garden, Petra's flowers were some of the most beautiful — deep purple roses that smelled like forgiveness."],
        "Petra happily sharing clothes with another girl, both laughing together, with a purple rose blooming in a small inset image of the garden")

    # Page 20
    add_story_page(pdf, 20,
        ["By the end of that year, the Garden of Kindness was the most beautiful place anyone had ever seen.",
         "It had overflowed its stone walls and flowers were growing all through the park, along the streets, in window boxes all over town.",
         "The whole town of Willowbrook was a garden now, because the whole town had become kind.",
         "And it all started with one girl, one smile, and one compliment about bread."],
        "An aerial view of Willowbrook completely covered in flowers — growing from buildings, along streets, in every window — the whole town transformed into a garden of color")

    # Page 21
    add_story_page(pdf, 21,
        ["Grandmother found Lina sitting in the garden one evening, surrounded by a thousand flowers.",
         "'You did this, my sweet girl,' Grandmother said, sitting beside her.",
         "'No,' Lina shook her head with a smile. 'I only planted the first seed. Everyone else grew the garden.'",
         "'And that,' said Grandmother, 'is the most beautiful thing about kindness. One small seed can grow into a whole world of flowers.'",
         "'All you have to do is plant it.'"],
        "Grandmother and Lina sitting together on a bench in the magnificent garden at sunset, surrounded by thousands of colorful flowers, a peaceful and beautiful closing scene")


    # Page 22
    add_story_page(pdf, 22,
        ["Now here's a secret just for you, dear reader:",
         "There's a Garden of Kindness in YOUR town too. You can't see it with your eyes, but it's there.",
         "Every time you're kind — every smile, every helping hand, every gentle word — a flower blooms somewhere invisible.",
         "And when you're kind, you inspire others to be kind too. That's how the garden grows.",
         "So go ahead. Plant your first seed today. Say something nice. Help someone. Share what you have. And watch your world bloom."],
        "A child reader looking out at their own neighborhood, imagining invisible flowers blooming everywhere people are being kind, a magical overlay of the reader's own world becoming a garden")

    # Page 23
    add_story_page(pdf, 23,
        ["Here are some seeds you can plant right now, today:",
         "Smile at someone who looks lonely. Hold the door for a stranger. Say thank you and really mean it.",
         "Draw a picture for someone who is sad. Share your snack with a friend. Listen when someone needs to talk.",
         "Tell someone what you love about them. Help without being asked. Forgive someone who hurt you.",
         "Every single one of these is a flower waiting to bloom. And YOU are the gardener."],
        "A child planting invisible seeds of kindness that grow into beautiful flowers around them — each kind act depicted as a colorful bloom, the child surrounded by a garden of their own making")

    # Page 24
    add_story_page(pdf, 24,
        ["And remember what Lina learned: the hardest kindness grows the biggest flowers.",
         "Being kind to someone who is mean to you. Forgiving someone who hurt you. Helping someone who never helped you back.",
         "Those are the sunflower seeds — the ones that grow tall and golden and spectacular.",
         "You do not have to be perfect. You do not have to be kind every single second. But every time you choose kindness over cruelty, love over anger, gentleness over harshness...",
         "Your garden grows. And so does the world."],
        "A final beautiful image of a garden in full bloom with the sun shining through, a quote carved in stone: 'Kindness grows when you share it,' Lina and her grandmother visible in the distance")

    # Page 25
    add_story_page(pdf, 25,
        ["One more thing from Lina to you:",
         "You will have days when being kind feels hard. Days when someone is mean and you want to be mean back.",
         "On those days, remember the sunflower — the biggest, most beautiful flower in the whole garden. The one that grew when Lina chose kindness even when it was difficult.",
         "Difficult kindness grows the most spectacular flowers. So on hard days, choose kindness anyway.",
         "Your garden is counting on you. And it will be magnificent."],
        "A single spectacular sunflower standing tall in a garden, representing the beauty that grows from choosing kindness on difficult days, golden and radiant, inspiring and warm")

    # Moral page
    create_moral_page(pdf, "Kindness Grows When You Share It",
        "Lina showed us that one small act of kindness can start something incredible. When you're kind to someone, they feel good and want to be kind to someone else. And that person passes it along too! Before you know it, one tiny seed of kindness has grown into a whole garden that makes everyone's life more beautiful. You don't have to do big, grand things. Just smile. Just help. Just be gentle. The garden will do the rest.")

    # Discussion Questions
    create_discussion_page(pdf, [
        "What kind thing could you do tomorrow to 'plant a seed' in your own garden of kindness?",
        "Has someone ever been kind to you when you were having a bad day? How did it make you feel?",
        "Why do you think Lina's kindness to Petra (who was mean to her) grew the biggest flower?",
        "Can you think of a time when one person's kindness made lots of other people happier too?",
        "If you had a Garden of Kindness, what colors do you think your flowers would be?"
    ])

    # About Author
    create_about_author_page(pdf)

    filepath = os.path.join(OUTPUT_DIR, "03-The-Garden-of-Kindness.pdf")
    size = pdf.save(filepath)
    return filepath, size



# ============================================================
# BOOK 4: Tiko and the Treasure of Friendship
# ============================================================
def generate_book_04():
    """Tiko and the Treasure of Friendship - Moral: True treasure is the friends we make."""
    pdf = PurePDF(title="Tiko and the Treasure of Friendship", author=AUTHOR)

    create_cover_page(pdf, "Tiko and the Treasure of Friendship", "friendship being the greatest treasure of all")
    create_dedication_page(pdf, "To every child who has a best friend — and to every child still looking for one. Your treasure is closer than you think.")

    # Page 1
    add_story_page(pdf, 1,
        ["Deep in the Whispering Woods, where the trees told secrets and the streams sang songs, there lived a young fox named Tiko.",
         "Tiko had orange fur, a bushy tail, and one big dream: to find the legendary Golden Treasure of the Forest.",
         "His grandfather had told him stories about it — a chest of gold hidden at the top of Sunset Mountain, guarded by ancient magic.",
         "'Whoever finds it,' Grandfather had said, 'will have everything they ever need.'"],
        "A young orange fox with bright curious eyes standing at the edge of a mystical forest, looking toward a distant mountain peak, dreamy golden light in the sky")

    # Page 2
    add_story_page(pdf, 2,
        ["'I'm going to find it!' Tiko announced one morning, packing a small bag with berries and a water flask.",
         "His mother looked worried. 'The journey to Sunset Mountain is long and dangerous, Tiko.'",
         "'I'll be fine on my own!' Tiko said confidently. 'I don't need anyone's help. I'm fast and clever!'",
         "With a wave of his bushy tail, Tiko set off alone into the woods, thinking only of the gold that waited at the end."],
        "Tiko with a small adventure pack setting off into the forest alone, his mother watching worriedly from their den entrance, morning mist in the woods")

    # Page 3
    add_story_page(pdf, 3,
        ["By midday, Tiko reached the Tangled Thicket — a maze of thorny bushes so thick that light couldn't get through.",
         "He tried to push through but the thorns scratched his nose and caught his fur. He tried going around, but it stretched for miles.",
         "'This is impossible!' Tiko growled, tugging his tail free from a particularly grabby bramble.",
         "Then he heard a small voice from above. 'Excuse me! If you need to get through, I can help!'"],
        "Tiko stuck in a dense thorny thicket, thorns catching his fur, looking frustrated, with a small voice coming from above in the tree branches")


    # Page 4
    add_story_page(pdf, 4,
        ["Looking up, Tiko saw a tiny bluebird perched on a branch. Her name was Pip.",
         "'I know every path through this thicket!' Pip chirped. 'I fly over it every day. Follow me!'",
         "Tiko hesitated. He didn't want help. He wanted to find the treasure by himself.",
         "But another thorn poked his ear, and he sighed. 'Okay, fine. Show me the way.'",
         "Pip fluttered ahead, guiding Tiko through a hidden gap in the thorns that he never would have found alone."],
        "A cheerful small bluebird named Pip hovering near Tiko, pointing with her wing toward a hidden path through the thorny thicket")

    # Page 5
    add_story_page(pdf, 5,
        ["'There you go!' Pip said as they emerged on the other side. 'Where are you headed?'",
         "'Sunset Mountain,' Tiko said. 'I'm finding the Golden Treasure. And I'm doing it alone,' he added pointedly.",
         "Pip's eyes went wide. 'Sunset Mountain! Oh, that sounds like an adventure! Can I come? Please please please?'",
         "Tiko sighed. He didn't want company. But Pip had helped him, so he mumbled, 'I guess. Just don't slow me down.'",
         "Pip sang with joy and fluttered alongside him as they walked deeper into the woods."],
        "Tiko walking out of the thicket into open forest with Pip flying excitedly beside him, Tiko looking slightly annoyed but Pip beaming with happiness")

    # Page 6
    add_story_page(pdf, 6,
        ["By evening, they reached the Rushing River — wide, deep, and fast.",
         "Tiko stared at it. He was a good swimmer, but this current was incredibly strong.",
         "As he paced the bank, wondering how to cross, a deep voice rumbled from the rocks.",
         "'Need to cross? I can carry you.' A large, gentle turtle named Shelly emerged from the reeds.",
         "'I cross this river every day. Hop on my shell!'"],
        "A large friendly turtle emerging from river reeds, offering her wide flat shell to Tiko and Pip, the river rushing powerfully behind her")


    # Page 7
    add_story_page(pdf, 7,
        ["Again, Tiko didn't want help. But the river really was too dangerous to cross alone.",
         "He and Pip climbed onto Shelly's broad, steady shell, and the old turtle swam them safely across.",
         "'Thank you,' Tiko said, a little embarrassed that he'd needed help twice already.",
         "'Where are you all going?' Shelly asked, climbing onto the far bank.",
         "'SUNSET MOUNTAIN!' Pip chirped excitedly. 'For the Golden Treasure!'",
         "'Oh my!' said Shelly. 'May I come along? I've always dreamed of seeing that mountain.'"],
        "Tiko and Pip riding on Shelly's shell across the rushing river, water splashing around them, all three looking like an unlikely adventure team")

    # Page 8
    add_story_page(pdf, 8,
        ["So now they were three — a fox, a bird, and a turtle, heading for Sunset Mountain.",
         "Tiko was grumpy about it. This was supposed to be HIS adventure. HIS treasure.",
         "But he had to admit, traveling wasn't so boring anymore. Pip sang songs. Shelly told stories about the river.",
         "And that night, when they camped under the stars, Shelly's big shell made the perfect windbreak.",
         "Maybe having companions wasn't the worst thing in the world."],
        "The three friends camping under stars at night — Tiko curled up by a small fire, Pip nestled in a tree, Shelly providing shelter with her shell, a cozy scene")

    # Page 9
    add_story_page(pdf, 9,
        ["The next morning, they entered the Dark Caverns — a maze of underground tunnels they had to pass through.",
         "Inside, it was pitch black. Tiko couldn't see his own paw in front of his face.",
         "'I'm scared of the dark,' Shelly admitted quietly. Her voice echoed in the cave.",
         "'Don't worry!' came a new voice. A small firefly named Glow appeared, lighting up the darkness around them.",
         "'I live in these caves. I can light your way through!'"],
        "Inside a dark cave with a tiny firefly glowing bright green, illuminating the faces of Tiko, Pip, and Shelly who look relieved to have light in the darkness")


    # Page 10
    add_story_page(pdf, 10,
        ["Glow guided them through the winding tunnels, his light bouncing off crystal walls that sparkled like diamonds.",
         "'It's beautiful in here!' Pip gasped.",
         "'Most creatures are too scared to see it,' Glow said. 'But with friends, the dark isn't so scary.'",
         "They emerged on the other side of the mountain range, and Sunset Mountain was now visible — close and golden in the afternoon light.",
         "Glow joined their group. Now they were four."],
        "The group emerging from the cave into sunlight, Sunset Mountain now visible and close, golden afternoon light, all four friends looking up at it excitedly")

    # Page 11
    add_story_page(pdf, 11,
        ["As they climbed Sunset Mountain, the path grew steep and dangerous.",
         "Rocks crumbled. Wind howled. Tiko's legs ached and his pack felt like it weighed a hundred pounds.",
         "But Pip scouted ahead and warned them of loose stones. Shelly's steady pace kept them from rushing and making mistakes.",
         "Glow lit the shadowy overhangs so they could see where to step.",
         "Together, they were stronger than any of them alone."],
        "The four friends climbing a steep mountain path together, each helping in their own way — Pip flying ahead, Glow lighting dark spots, Shelly steady and sure, Tiko climbing bravely")

    # Page 12
    add_story_page(pdf, 12,
        ["Near the top, they hit the final obstacle: the Windy Bridge — a narrow rope bridge over a terrifying drop.",
         "The wind screamed and the bridge swayed wildly. Even brave Tiko's stomach lurched.",
         "'I can't,' Shelly said, trembling. 'I'm too heavy. The bridge will break.'",
         "'I'll fly across and check it,' Pip said. She fluttered over and tested each rope. 'It's strong enough! But go one at a time!'",
         "One by one, cheering each other on, they crossed the bridge. Shelly went last, eyes squeezed shut, while her friends called encouragement from the other side."],
        "The narrow rope bridge swaying over a misty chasm, Pip flying alongside a terrified Shelly who is slowly crossing while Tiko and Glow cheer from the far side")


    # Page 13
    add_story_page(pdf, 13,
        ["And then — they were there. The very top of Sunset Mountain.",
         "The sun was setting, painting everything gold and orange and pink. The view stretched forever in every direction.",
         "And there, sitting on a flat rock in the golden light, was an old wooden chest with a golden lock.",
         "'THE TREASURE!' Tiko yelled, racing toward it. His heart pounded. All his dreams were about to come true!",
         "His friends followed, excited to see what was inside."],
        "The mountaintop at sunset, bathed in golden light, a weathered wooden chest with a gold lock sitting on a flat rock, Tiko racing toward it with his friends behind")

    # Page 14
    add_story_page(pdf, 14,
        ["Tiko reached the chest and found the lock already open. He lifted the heavy lid with trembling paws.",
         "Inside... was a mirror.",
         "Just a simple mirror, lying in the bottom of the chest. No gold. No jewels. No coins.",
         "Tiko stared at it, confused and disappointed. 'That's it? A stupid mirror? This can't be the treasure!'",
         "He picked it up angrily — and then he saw what the mirror was showing."],
        "Tiko looking into the chest with a shocked and disappointed expression, seeing only a mirror inside, his friends gathered curiously behind him")

    # Page 15
    add_story_page(pdf, 15,
        ["The mirror didn't show Tiko's reflection. It showed HIS JOURNEY.",
         "He saw Pip, guiding him through the Tangled Thicket. He saw Shelly, carrying him across the Rushing River.",
         "He saw Glow, lighting the way through the Dark Caverns. He saw all four of them crossing the Windy Bridge together.",
         "And written in golden letters across the mirror were the words: 'THE REAL TREASURE IS BESIDE YOU.'",
         "Tiko's eyes went wide. He slowly turned around and looked at his friends."],
        "The mirror showing magical images of the journey — all the friends helping each other at different stages — with golden text glowing across it, Tiko's amazed face reflected at the edge")


    # Page 16
    add_story_page(pdf, 16,
        ["Pip. Shelly. Glow. They were standing there in the golden sunset light, looking at him with curious, kind eyes.",
         "These animals who had helped him at every turn. Who had made the journey possible. Who had made it FUN.",
         "Without Pip, he'd still be stuck in thorns. Without Shelly, he'd never have crossed the river.",
         "Without Glow, he'd be lost in the dark. Without all of them cheering, he'd never have crossed that bridge.",
         "THEY were the treasure. They had been the treasure all along."],
        "Tiko looking at his three friends bathed in golden sunset light, realization dawning on his face, seeing them as the precious treasures they truly are")

    # Page 17
    add_story_page(pdf, 17,
        ["'I... I think I understand now,' Tiko said softly. His voice was thick with emotion.",
         "'What is it?' Pip asked, tilting her head.",
         "Tiko set down the mirror and walked to his friends. 'I came here looking for gold. I didn't want anyone's help. I wanted to do it alone.'",
         "'But the real treasure was never in this chest. The real treasure was making friends with all of you.'",
         "He looked at each of them. 'YOU are my treasure. And you're better than any gold in the world.'"],
        "Tiko standing before his three friends with open paws, emotional and honest, the sunset behind them painting everything gold, a moment of deep connection")

    # Page 18
    add_story_page(pdf, 18,
        ["Pip flew to Tiko's shoulder and nuzzled his cheek. 'And you're OUR treasure too, Tiko.'",
         "Shelly smiled her slow, warm smile. 'I never had friends before this journey. You gave me that gift.'",
         "Glow buzzed around them all, his light pulsing with happiness. 'None of us could have made it alone. But together we did the impossible!'",
         "They stood on that mountaintop as the sun set, four unlikely friends who had found something far more valuable than gold."],
        "All four friends in a group hug on the mountaintop — Pip on Tiko's shoulder, Shelly beside them, Glow circling above casting warm light — the sunset spectacular behind them")


    # Page 19
    add_story_page(pdf, 19,
        ["The journey home was the best part of all.",
         "Now that Tiko wasn't rushing to find treasure, he could actually enjoy the walk.",
         "They stopped to splash in streams, rest in sunny meadows, and tell each other stories at night.",
         "Tiko realized he'd been so focused on the destination that he'd almost missed the joy of the journey — and the friends he'd made along the way."],
        "The four friends walking happily through a beautiful meadow on the way home, laughing and playing, no rush, enjoying each other's company, flowers and butterflies around them")

    # Page 20
    add_story_page(pdf, 20,
        ["When Tiko finally got home, his mother rushed out to meet him.",
         "'Did you find the Golden Treasure?' she asked.",
         "Tiko smiled the biggest smile of his life. 'I found something even better.'",
         "He introduced Pip, Shelly, and Glow. 'I found the best friends in the whole world.'",
         "His mother hugged him and whispered, 'Now THAT is a treasure worth having, my dear.'"],
        "Tiko arriving home with his three friends, his mother hugging him at the entrance to their fox den, all the friends waving hello, a warm homecoming scene")

    # Page 21
    add_story_page(pdf, 21,
        ["From that day on, Tiko, Pip, Shelly, and Glow were inseparable.",
         "They had adventures every day — exploring caves, crossing rivers, climbing hills — but now the adventures were the fun part, not the treasure at the end.",
         "And whenever someone asked Tiko if he was sad about not finding gold, he would laugh.",
         "'Gold can be lost or stolen,' he'd say. 'But true friends? True friends are a treasure that lasts forever.'"],
        "The four friends having a new adventure together in the Whispering Woods, happy and confident, clearly the best of friends, exploring with joy")

    # Page 22
    add_story_page(pdf, 22,
        ["So remember, dear reader: treasures come in many forms.",
         "Some treasures shine like gold. But the most precious treasures have heartbeats.",
         "They're the friends who help you through thorny times, carry you across rough waters, light your way in the dark, and cheer you on when you're scared.",
         "Look around you. Your greatest treasures might already be sitting right beside you.",
         "Take care of them. They're worth more than all the gold on Sunset Mountain."],
        "A final image of a child reading this book, with their friends sitting beside them, a warm glow around the group, connecting the story to the reader's own life")

    # Page 23
    add_story_page(pdf, 23,
        ["And here is one more thing Tiko learned on his journey:",
         "You cannot find treasure alone. Life's best adventures need companions.",
         "So be a good friend yourself. Be someone's Pip — guide them when they are lost. Be someone's Shelly — carry them when they are tired.",
         "Be someone's Glow — light the way when things are dark. The treasure of friendship only works when BOTH friends are treasures to each other.",
         "Be the kind of friend you wish to have. And you will never be poor in the ways that matter."],
        "Four children walking together on an adventure, each helping the other in small ways, representing real-life versions of Pip, Shelly, Glow, and Tiko, friendship in action")

    # Page 24
    add_story_page(pdf, 24,
        ["One last secret from the top of Sunset Mountain:",
         "The best part of any adventure is not the destination — it is who walks beside you.",
         "The laughs along the way. The stories shared under stars. The hands that pull you up when you fall.",
         "So go on adventures. Dream big dreams. Climb mountains. But never forget:",
         "The real gold is in the hearts of those who journey with you. Always."],
        "A sunset view from a mountain top with silhouettes of friends standing together looking at the horizon, arms around each other, the sky painted gold and pink, a perfect ending")

    # Page 25
    add_story_page(pdf, 25,
        ["So start your treasure hunt today, dear reader. But here is the secret map:",
         "The treasure is not in a chest at the top of a mountain. It is in the person sitting next to you right now.",
         "It is in your best friend's laugh. Your mother's hug. Your teacher's patience. Your pet's loyal eyes.",
         "Treasure surrounds you every single day. You just have to open your eyes and SEE it.",
         "And once you do? You will realize you have been the richest person alive all along."],
        "A child looking around at the people in their life — family, friends, pets — with golden treasure-glow around each person, realizing they are already surrounded by treasure")

    # Moral page
    create_moral_page(pdf, "True Treasure Is the Friends We Make Along the Way",
        "Tiko learned that the most valuable things in life aren't things at all — they're the people who walk beside us on our journey. Friends who help us, support us, make us laugh, and stand by us when things are hard. Gold might make you rich, but friends make you wealthy in the ways that really matter — love, laughter, belonging, and joy. Be a good friend, and you'll always be the richest person in the room.")

    # Discussion Questions
    create_discussion_page(pdf, [
        "Who are the 'treasures' in YOUR life? (Friends, family, pets?)",
        "Why do you think Tiko didn't want help at first? Have you ever felt like you had to do something alone?",
        "How did each friend help Tiko with their unique gift? What unique gifts do YOUR friends have?",
        "What's more important: winning a prize or having fun with friends along the way? Why?",
        "Can you think of a time when a friend helped you do something you couldn't do alone?"
    ])

    # About Author
    create_about_author_page(pdf)

    filepath = os.path.join(OUTPUT_DIR, "04-Tiko-and-the-Treasure-of-Friendship.pdf")
    size = pdf.save(filepath)
    return filepath, size



# ============================================================
# BOOK 5: The Boy Who Couldn't Stop Lying
# ============================================================
def generate_book_05():
    """The Boy Who Couldn't Stop Lying - Moral: Honesty builds trust; lies break it."""
    pdf = PurePDF(title="The Boy Who Couldn't Stop Lying", author=AUTHOR)

    create_cover_page(pdf, "The Boy Who Couldn't Stop Lying", "honesty, trust, and the power of truth")
    create_dedication_page(pdf, "To every child learning that the truth — even when it's hard — is always the bravest and best choice.")

    # Page 1
    add_story_page(pdf, 1,
        ["There once was a boy named Owen who discovered something strange on his seventh birthday.",
         "Every time he told a lie, a small dark shadow appeared behind him.",
         "Nobody else could see it at first — just Owen. It was small, like a dark smudge floating behind his back.",
         "The first time it happened, Owen had told his mom he'd brushed his teeth when he hadn't. A tiny shadow popped up like a puff of smoke."],
        "A young boy looking nervously over his shoulder at a small dark shadow floating behind him that no one else seems to notice, a bedroom scene with a toothbrush untouched on the sink")

    # Page 2
    add_story_page(pdf, 2,
        ["'That's weird,' Owen thought, but he didn't worry about it much.",
         "After all, it was just a tiny little lie. Everyone tells tiny lies, right?",
         "The next day at school, his teacher asked who had done the homework. Owen raised his hand, even though he hadn't done it.",
         "POOF. Another shadow appeared. Now there were two, floating behind him like dark little clouds."],
        "Owen at his school desk raising his hand with a guilty expression, two small dark cloud-like shadows floating behind his chair that his classmates don't notice")

    # Page 3
    add_story_page(pdf, 3,
        ["Owen found that lying was easy. Much easier than telling the truth.",
         "The truth meant getting in trouble. The truth meant doing hard work. The truth meant admitting mistakes.",
         "But lies? Lies were like shortcuts. They got him out of trouble instantly!",
         "So Owen lied more and more. 'Yes, I cleaned my room.' 'No, I didn't eat the cookies.' 'He started it, not me!'",
         "And with each lie, another shadow grew behind him. Three. Five. Ten. Twenty."],
        "Owen walking down a hallway with a growing collection of dark shadows trailing behind him like a dark cloud, getting larger and more numerous, Owen not looking back")


    # Page 4
    add_story_page(pdf, 4,
        ["After a few weeks, something changed. The shadows started getting bigger.",
         "They merged together into one large, dark shadow that loomed behind Owen like a storm cloud.",
         "And now, other people were starting to notice.",
         "'Owen, what's that behind you?' his friend Marcus asked at recess, squinting. 'It looks... dark back there.'",
         "'Nothing!' Owen said quickly (another lie). The shadow grew a little bigger."],
        "Owen at recess with a large dark shadow behind him, other children starting to notice and point, looking uncomfortable, Owen looking worried for the first time")

    # Page 5
    add_story_page(pdf, 5,
        ["The shadow began to do something terrible. It started whispering Owen's lies to the people around him.",
         "When Owen told his teacher, 'I finished my project!' the shadow hissed, 'He didn't even start it...'",
         "When Owen told his friend, 'Of course I'll come to your party!' the shadow whispered, 'He's not going to go...'",
         "People couldn't hear the words clearly, but they felt something wrong. A cold, uncomfortable feeling whenever Owen spoke."],
        "The dark shadow with a mouth forming behind Owen, dark wisps reaching toward the ears of people Owen is talking to, people looking uncomfortable and suspicious")

    # Page 6
    add_story_page(pdf, 6,
        ["One by one, Owen's friends started pulling away.",
         "'I don't know,' Marcus said when asked about Owen. 'Something about him makes me feel weird. Like I can't trust him.'",
         "The other kids felt it too. They stopped inviting Owen to play. They chose other partners for group projects.",
         "At lunch, the seat next to Owen was always empty now. His shadow sat there instead — cold, dark, and growing."],
        "Owen sitting alone at a lunch table, the dark shadow occupying the seat next to him like a companion, other kids at different tables glancing at him warily")


    # Page 7
    add_story_page(pdf, 7,
        ["Even Owen's family noticed. When he said 'I love you' to his mom, she hugged him back but looked uncertain.",
         "The shadow had poisoned those words too, because Owen had said so many untrue things that even his true words felt hollow now.",
         "That was the worst part. Owen really DID love his mom. But his lies had made it so no one believed anything he said anymore.",
         "Not even the truth."],
        "Owen hugging his mother who has a worried, uncertain expression, the dark shadow looming large behind Owen, creating a visual barrier between them")

    # Page 8
    add_story_page(pdf, 8,
        ["One night, Owen lay in bed and the shadow was so big it filled his entire room with darkness.",
         "He couldn't see the stars through his window anymore. He couldn't feel the warmth of his nightlight.",
         "He was surrounded by all his lies — cold, heavy, and suffocating.",
         "'Go away!' Owen cried. But the shadow just grew thicker. It was made of HIS words, after all. It wouldn't leave until he changed them."],
        "Owen in bed, his room completely dark and consumed by the shadow, trying to push it away but unable to, looking scared and alone, no light getting through")

    # Page 9
    add_story_page(pdf, 9,
        ["The next morning, Owen went to school feeling terrible. His shadow dragged behind him like a heavy black cape.",
         "In class, his teacher said, 'Owen, did you do last night's reading?'",
         "Owen opened his mouth to say yes — the easy lie, the comfortable shortcut.",
         "But then he looked at the shadow. It leaned forward hungrily, waiting to be fed another lie.",
         "And for the first time, Owen said something different. 'No,' he whispered. 'I didn't do it. I'm sorry.'"],
        "Owen in class with his mouth open, the shadow leaning forward eagerly, but Owen's expression changing to determination as he chooses truth, a pivotal moment")


    # Page 10
    add_story_page(pdf, 10,
        ["Something magical happened. The moment the truth left Owen's lips, a tiny piece of the shadow dissolved.",
         "Just a little bit — like a wisp of smoke blown away by a breeze.",
         "It was small, but Owen noticed. The truth had made the shadow shrink!",
         "His teacher looked surprised. 'Thank you for being honest, Owen. Please do it tonight, okay?'",
         "Owen nodded. It hadn't been easy. But something felt lighter."],
        "A tiny wisp of the shadow dissolving like smoke after Owen tells the truth, a small but visible difference, Owen looking surprised and hopeful")

    # Page 11
    add_story_page(pdf, 11,
        ["Owen decided to try again. At lunch, Marcus sat far away as usual.",
         "Owen walked over, his massive shadow trailing behind him. 'Marcus... I lied to you about coming to your birthday party. I went to the movies instead. I'm really sorry.'",
         "Marcus stared at him. Nobody expected Owen to admit that.",
         "More of the shadow evaporated — a big chunk this time. The truth about something that really mattered dissolved a lot more shadow than a small truth about homework."],
        "Owen standing bravely in front of Marcus in the cafeteria, a large portion of his shadow dissolving as he confesses the truth, Marcus looking shocked but listening")

    # Page 12
    add_story_page(pdf, 12,
        ["'Why are you telling me this now?' Marcus asked, arms crossed.",
         "'Because I've been lying about everything,' Owen said. 'And it's made everyone go away. I hate it. I miss my friends. I miss being trusted.'",
         "He took a shaky breath. 'I'm going to try to stop lying. But I might mess up sometimes. I just wanted you to know I'm trying.'",
         "Marcus didn't smile. But he nodded slowly. 'Okay. I'll watch and see.' It wasn't forgiveness yet. But it was a door, cracked open."],
        "Marcus with arms crossed but expression softening slightly, listening to Owen who looks vulnerable and honest, other kids at nearby tables watching curiously")


    # Page 13
    add_story_page(pdf, 13,
        ["Owen spent the next week telling the truth about everything — even when it was hard.",
         "'Did you break this vase?' his mom asked. Owen wanted so badly to say no. The word was right there on his tongue.",
         "But he looked at the shadow — still big, still dark — and said, 'Yes. I'm sorry. I was running inside.'",
         "He got in trouble. He had to do extra chores. But the shadow shrank again, and his mom hugged him tight.",
         "'I'm proud of you for telling the truth,' she said. And this time, her hug felt real and warm."],
        "Owen confessing to his mother about a broken vase, looking scared but honest, his mother's expression going from stern to proud, shadow visibly shrinking behind him")

    # Page 14
    add_story_page(pdf, 14,
        ["Day by day, truth by truth, the shadow got smaller.",
         "It wasn't easy. Sometimes the truth got Owen in trouble. Sometimes it was embarrassing.",
         "Sometimes he messed up and a small lie slipped out — and a tiny shadow puff would appear again.",
         "But Owen would catch himself, take a breath, and correct it. 'Actually, that's not true. Let me start over.'",
         "Each correction made the puff disappear. The shadow was shrinking steadily."],
        "A sequence showing the shadow getting progressively smaller over several days, Owen standing taller and more confident each day, light returning around him")

    # Page 15
    add_story_page(pdf, 15,
        ["The hardest truth came at school. Owen had copied from a friend's test two weeks ago.",
         "Nobody knew. He could have kept it secret. The shadow from that lie was deep and heavy.",
         "But Owen went to his teacher. 'I need to tell you something. I cheated on the last test. I copied answers.'",
         "His teacher was disappointed. Owen had to retake the test and got a much lower grade.",
         "But a HUGE chunk of shadow dissolved. The biggest piece yet. And Owen felt lighter than he had in months."],
        "Owen at his teacher's desk confessing about cheating, looking ashamed but brave, a massive piece of shadow dissolving dramatically, the teacher looking serious but respectful of his honesty")


    # Page 16
    add_story_page(pdf, 16,
        ["Slowly, people started trusting Owen again.",
         "It didn't happen overnight. Trust is like a tower of blocks — it takes a long time to build but falls down instantly.",
         "Owen had to prove himself with each honest word, each truthful day.",
         "But people noticed. They could feel the darkness around Owen getting lighter.",
         "'He seems different,' kids whispered. 'I think he's really changed.'"],
        "Owen in the schoolyard with other children starting to move closer to him, the shadow now much smaller, other kids cautiously approaching with curious smiles")

    # Page 17
    add_story_page(pdf, 17,
        ["One month later, Marcus sat next to Owen at lunch again.",
         "'You haven't lied once this whole month,' Marcus said. 'I've been watching.'",
         "Owen smiled. 'I've been trying really hard. The truth is harder than lying, but it feels so much better.'",
         "'Yeah,' Marcus said, unwrapping his sandwich. 'It does. Want half my cookie?'",
         "It was a small thing — sharing a cookie. But it meant everything. It meant trust was coming back."],
        "Marcus sitting next to Owen at lunch again, offering half a cookie, both smiling naturally, the shadow behind Owen now very small, other kids starting to join their table")

    # Page 18
    add_story_page(pdf, 18,
        ["By the end of the school year, Owen's shadow was almost gone.",
         "Just the tiniest wisp remained — a reminder that he'd always need to choose truth over lies.",
         "But it no longer scared people away. It no longer whispered. It was just a tiny reminder to be honest.",
         "Owen had his friends back. He had his family's trust back. He had himself back.",
         "And all it had taken was the hardest, simplest thing: telling the truth."],
        "Owen walking happily with friends, the shadow now just the tiniest wisp, barely visible, surrounded by laughing friends, sunshine bright around him")


    # Page 19
    add_story_page(pdf, 19,
        ["Years later, Owen became known as the most honest person in his school.",
         "When he said something, people believed him instantly — because they knew Owen always told the truth.",
         "Sometimes younger kids asked him, 'Isn't it easier to just lie?'",
         "Owen would smile and say, 'Lying is the easy shortcut that leads to a terrible place. Truth is the harder road that leads somewhere beautiful.'",
         "'Trust me,' he'd add with a wink. 'I learned the hard way.'"],
        "Owen as a slightly older boy, confident and trusted, surrounded by younger kids who look up to him, bright sunshine and no shadow at all, a respected and trustworthy figure")

    # Page 20
    add_story_page(pdf, 20,
        ["Owen's little sister, Emma, came to him one day looking scared.",
         "'Owen, I broke Mom's favorite plate. Should I tell the truth? I'm so scared of getting in trouble.'",
         "Owen knelt down beside her. 'I know it's scary. Your stomach probably feels like it has butterflies made of rocks.'",
         "Emma nodded, tears in her eyes. 'What if she gets really mad?'",
         "'She might be upset,' Owen said honestly. 'But she'll be proud of you for telling the truth. And you won't have to carry a heavy shadow.'"],
        "Owen kneeling beside his scared little sister Emma who is holding pieces of a broken plate, Owen looking kind and wise, helping her choose honesty")

    # Page 21
    add_story_page(pdf, 21,
        ["Together, they went to their mom. Emma was shaking, but Owen held her hand.",
         "'Mommy, I broke your plate. I'm really sorry,' Emma said in a tiny voice.",
         "Their mom looked at the broken plate, then at Emma's brave, trembling face.",
         "'Thank you for telling me, sweetheart. I'm disappointed about the plate, but I'm so proud of your honesty.'",
         "She hugged Emma tight. Owen smiled. His sister had just learned what he'd learned the hard way — but she learned it much sooner."],
        "Emma confessing to their mother about the plate while Owen stands supportively behind her, their mother hugging Emma, a warm family scene of truth and love")

    # Page 22
    add_story_page(pdf, 22,
        ["At school, Owen started a project he called 'Truth Tuesday.'",
         "Every Tuesday, his class would share one honest thing — something true that was hard to say.",
         "'I'm sorry I took your pencil without asking.' 'I actually need help with reading.' 'I feel left out sometimes.'",
         "The classroom became a place where honesty was celebrated, not punished.",
         "And those honest conversations built friendships deeper than anyone expected."],
        "Owen's classroom on Truth Tuesday, children bravely sharing honest truths with each other, some looking nervous but supported, a circle of trust forming")

    # Page 23
    add_story_page(pdf, 23,
        ["One day, Owen faced his hardest truth yet. His best friend Marcus asked him, 'Do you like my new haircut?'",
         "Owen didn't love it. But the old Owen would have said something mean, and the lying Owen would have said something false.",
         "Instead, he found the kind truth: 'I think you always look great because you're my friend. The haircut is different, but you pull it off!'",
         "Owen had learned something important: being honest doesn't mean being cruel. You can be truthful AND kind at the same time."],
        "Owen talking to Marcus about his haircut, finding the kind truth, both boys smiling, showing that honesty and kindness can coexist beautifully")

    # Page 24
    add_story_page(pdf, 24,
        ["The last wisp of Owen's shadow disappeared completely on a Tuesday in March.",
         "He was helping a younger kid who had been caught lying. 'I used to lie all the time,' Owen told him. 'I know how it feels.'",
         "'Doesn't the truth ever scare you?' the little boy asked.",
         "'Every single day,' Owen admitted. 'But I'll tell you a secret: the truth is like a muscle. The more you use it, the stronger it gets. And the lies? They're like sugar — sweet in the moment but they make you sick.'",
         "As he said those words, the last shadow puff dissolved into nothing. Owen was finally, completely free."],
        "Owen talking to a younger boy on the playground, the final tiny wisp of shadow dissolving into sunshine, Owen looking completely free and light, a full-circle moment")

    # Page 25
    add_story_page(pdf, 25,
        ["And here's the thing Owen learned that he wants YOU to know:",
         "Everyone is tempted to lie sometimes. It feels easier in the moment.",
         "But lies don't just disappear. They grow. They follow you. They push people away.",
         "The truth might be harder to say, but it builds something precious — trust.",
         "And trust, once you earn it, makes every relationship in your life stronger and more beautiful than any lie ever could."],
        "A final image showing Owen as a young boy looking directly at the reader with an honest, warm smile, no shadow in sight, standing in bright sunlight, a trustworthy and happy person")

    # Moral page
    create_moral_page(pdf, "Honesty Builds Trust; Lies Break It",
        "Owen learned that lies might seem like easy shortcuts, but they grow into something dark and heavy that pushes everyone away. The truth can be scary to tell, especially when you might get in trouble. But honesty builds trust — and trust is the foundation of every friendship, every family, and every relationship. When people trust you, they believe in you, count on you, and want to be near you. That's worth more than any 'easy' lie.")

    # Discussion Questions
    create_discussion_page(pdf, [
        "Have you ever told a lie that made you feel bad afterward? What happened?",
        "Why do you think people stop trusting someone who lies a lot?",
        "What's the difference between a time when telling the truth is easy and when it's hard?",
        "If Owen's shadow appeared behind YOUR lies, how big do you think it would be right now?",
        "How can you practice being more honest, even when the truth is hard to say?"
    ])

    # About Author
    create_about_author_page(pdf)

    filepath = os.path.join(OUTPUT_DIR, "05-The-Boy-Who-Couldnt-Stop-Lying.pdf")
    size = pdf.save(filepath)
    return filepath, size



# ============================================================
# BOOK 6: Amara's Magic Paintbrush
# ============================================================
def generate_book_06():
    """Amara's Magic Paintbrush - Moral: Use your gifts to help others."""
    pdf = PurePDF(title="Amara's Magic Paintbrush", author=AUTHOR)

    create_cover_page(pdf, "Amara's Magic Paintbrush", "using your gifts to help others, not just yourself")
    create_dedication_page(pdf, "To every child with a talent or gift — the world needs what only you can give. Use it well.")

    # Page 1
    add_story_page(pdf, 1,
        ["In a small village at the foot of the Purple Mountains, there lived a girl named Amara who loved to paint.",
         "She painted on scraps of paper, on smooth stones, on the walls of her house (which her mother wasn't thrilled about).",
         "Amara painted flowers and birds and sunsets and dragons and anything her imagination could dream up.",
         "But Amara's family was very poor. They couldn't afford real paints or canvases or brushes."],
        "A young girl painting with berry juice on a flat stone outside a small humble village home, her artwork beautiful despite the simple materials, Purple Mountains in the background")

    # Page 2
    add_story_page(pdf, 2,
        ["One evening, Amara found something extraordinary washed up in the stream behind her house.",
         "It was a paintbrush — but not an ordinary one. Its handle was carved from golden wood, and its bristles shimmered like they were made of pure starlight.",
         "When Amara picked it up, the brush tingled warmly in her hand, as if it had been waiting for her.",
         "'Hello, beautiful,' Amara whispered, running her thumb along the smooth handle."],
        "Amara kneeling by a stream at sunset, picking up a magnificent golden paintbrush that glows with starlight, her eyes wide with wonder")

    # Page 3
    add_story_page(pdf, 3,
        ["That night, Amara dipped the brush in a puddle and painted a picture of an apple on her stone floor.",
         "The moment she finished the last stroke, the painted apple shimmered, rose up from the floor, and became REAL.",
         "A perfect, red, delicious apple — solid and warm and smelling like an orchard in autumn.",
         "Amara dropped the brush in shock. She bit the apple. It was the sweetest, most delicious apple she'd ever tasted.",
         "'The brush makes things REAL,' she gasped. 'Whatever I paint comes to life!'"],
        "Amara staring in shock as a painted apple lifts off the floor and becomes three-dimensional and real, the magic brush glowing on the ground beside her, apple shining red")


    # Page 4
    add_story_page(pdf, 4,
        ["The next morning, Amara went wild with excitement. She painted a feast of food for her family.",
         "Bread, fruit, rice, vegetables, warm stew — it all came to life on the table.",
         "Her mother and little brother stared in disbelief. 'How?' her mother asked.",
         "'My paintbrush is magic!' Amara beamed. 'We'll never be hungry again!'",
         "Then she painted new clothes for everyone, and a warm blanket for her brother's bed."],
        "A humble table now overflowing with beautiful food that Amara has painted into existence, her mother and brother amazed, Amara proudly holding the golden brush")

    # Page 5
    add_story_page(pdf, 5,
        ["Amara's mind raced with possibilities. She could have ANYTHING she wanted!",
         "She painted herself a beautiful room with a soft bed. She painted toys and books and sweets.",
         "She painted a big house for her family with a garden and a swing.",
         "For three wonderful days, Amara painted everything her heart desired. Life was perfect!",
         "Or at least... she thought it was."],
        "Amara in a now-beautiful painted room full of toys and books and treats, painting more and more things for herself, surrounded by luxury, looking happy but a little excessive")

    # Page 6
    add_story_page(pdf, 6,
        ["On the fourth day, Amara's neighbor, old Mrs. Desta, knocked on their door.",
         "Her eyes were hollow with hunger. 'Please,' she said quietly. 'My grandchildren haven't eaten in two days. Can you spare anything?'",
         "Amara had a table full of painted food. More than her family could ever eat.",
         "She started to say yes — but then a selfish thought crept in. 'What if the brush's magic runs out? I should save everything for MY family.'",
         "'Sorry, Mrs. Desta,' Amara said. 'We don't have enough to share.' It was a lie."],
        "Old Mrs. Desta at the door looking thin and desperate, Amara with a conflicted guilty expression, a lavish table of food clearly visible behind her in the house")


    # Page 7
    add_story_page(pdf, 7,
        ["That night, something strange happened. When Amara tried to paint more food, the colors looked... duller.",
         "The bread she painted came out stale. The fruit was dry. The magic seemed weaker.",
         "'That's odd,' Amara thought. She tried painting a new dress. It appeared, but the colors were faded and the fabric was thin.",
         "The brush was losing its magic. Amara felt a prick of panic. What was happening?"],
        "Amara painting but the results looking dull and faded, a loaf of bread appearing stale and gray, the brush's glow dimmer than before, Amara looking worried")

    # Page 8
    add_story_page(pdf, 8,
        ["By the next day, the brush barely worked at all. Amara painted a bowl of soup and got a bowl of cold, tasteless water.",
         "She painted a warm coat and got a thin sheet of paper.",
         "'No! No no no!' Amara cried, shaking the brush. 'What happened? Why won't you work?!'",
         "Then she heard a gentle voice — coming from the brush itself.",
         "'I was given to you to help others,' the brush whispered. 'Magic that is only used for yourself... fades.'"],
        "Amara shaking the dimly glowing brush in frustration, failed paintings around her — watery soup, paper-thin coat — the brush glowing faintly with a gentle voice coming from it")

    # Page 9
    add_story_page(pdf, 9,
        ["'When you turned away Mrs. Desta and her hungry grandchildren, my magic began to die,' the brush said.",
         "'I'm meant to flow outward, like water from a spring. When you dam it up for yourself alone, I dry up.'",
         "Amara felt a deep shame settle in her stomach. She had been so focused on getting things for herself that she'd forgotten the people around her who needed help.",
         "'Can I fix it?' she asked in a small voice. 'Can the magic come back?'",
         "'Use me for others,' the brush said. 'And see what happens.'"],
        "Amara sitting on the floor, the dim brush in her lap, tears in her eyes, looking ashamed and thoughtful, the once-beautiful painted room now looking faded around her")


    # Page 10
    add_story_page(pdf, 10,
        ["Amara ran straight to Mrs. Desta's house. 'I'm so sorry!' she cried. 'I have something that can help.'",
         "She dipped the brush and painted a meal for Mrs. Desta and her grandchildren.",
         "As the brush swept across the stone, it glowed bright — brighter than it had in days!",
         "A magnificent feast appeared: warm injera bread, rich stew, fresh fruit, and cool water.",
         "The magic was back. And it was STRONGER than before. Helping others made the brush's power surge."],
        "Amara painting a beautiful feast at Mrs. Desta's humble table, the brush glowing brilliantly, Mrs. Desta's grandchildren cheering with joy, food appearing magical and vibrant")

    # Page 11
    add_story_page(pdf, 11,
        ["'Thank you, child!' Mrs. Desta wept with gratitude, hugging Amara tight.",
         "The grandchildren danced around the table. Their smiles lit up the room brighter than any magic.",
         "Amara felt something warm bloom in her chest — a feeling much better than having a big house or fancy clothes.",
         "It was the feeling of making someone else's life better. And it was addictive in the best way."],
        "Mrs. Desta hugging Amara while the grandchildren eat happily, everyone smiling, the room glowing with warmth and gratitude, Amara's face showing deep satisfaction")

    # Page 12
    add_story_page(pdf, 12,
        ["From that moment on, Amara used her brush for the village.",
         "She painted a new well so everyone had clean water. The brush blazed like gold!",
         "She painted a school building so the children had a place to learn. The brush hummed with power!",
         "She painted medicine for the sick, seeds for the farmers, and warm blankets for the cold nights.",
         "Every time she helped someone else, the brush grew more powerful, not less."],
        "A montage of Amara painting wonderful things for her village — a well, a school, medicine — the brush glowing more and more brilliantly with each selfless act")


    # Page 13
    add_story_page(pdf, 13,
        ["Word spread about Amara and her magical paintbrush. People came from far villages asking for help.",
         "A farmer whose crops had failed. A family whose house had burned. A child who needed medicine.",
         "Amara helped every single one. And with each act of generosity, the brush grew brighter and more powerful.",
         "She discovered something amazing: the more she gave away, the more magic she had to give. It never ran out when she used it for others."],
        "A line of people from various villages coming to Amara for help, Amara painting solutions for each one, the brush now blazing like a golden torch")

    # Page 14
    add_story_page(pdf, 14,
        ["But one day, a rich and greedy man named Mr. Hailu came to the village.",
         "'Give me that brush!' he demanded. 'I'll use it to paint myself a palace of gold!'",
         "'No,' Amara said calmly. 'The brush only works when used to help others. It dies when used for greed.'",
         "Mr. Hailu didn't believe her. He grabbed the brush from her hand and tried to paint gold coins.",
         "The brush was cold and dead in his hands. Nothing happened. Not even a flicker."],
        "A greedy-looking wealthy man trying to use the paintbrush to paint gold coins, the brush completely dark and lifeless in his hands, Amara watching with a knowing expression")

    # Page 15
    add_story_page(pdf, 15,
        ["'Why won't it work?!' Mr. Hailu shouted, shaking the brush furiously.",
         "'Because it knows your heart,' Amara said gently. 'The brush is powered by generosity. It can feel why you want to paint.'",
         "'If you paint to help others — it blazes like the sun. If you paint for selfish greed — it sleeps.'",
         "Mr. Hailu threw the brush down in frustration and stormed away.",
         "Amara picked it up, and it immediately warmed in her hands, glowing softly, happy to be home."],
        "Mr. Hailu angrily throwing the dead brush down and storming off, Amara calmly picking it up as it immediately glows warm and golden again in her gentle hands")


    # Page 16
    add_story_page(pdf, 16,
        ["One day, a terrible drought came to the region. The stream dried up and the fields cracked.",
         "Amara painted rain clouds above the fields — and real rain fell, soft and nourishing, saving the crops.",
         "The brush blazed so brightly it was hard to look at. 'This is what I'm for!' it seemed to sing.",
         "Amara laughed with joy, dancing in the rain she'd created for everyone."],
        "Amara painting rain clouds over dry cracked fields, real rain falling from the painted clouds, farmers dancing in the rain, the brush blazing like the sun")

    # Page 17
    add_story_page(pdf, 17,
        ["Then word came of a village across the mountains where children had no school.",
         "Amara traveled there with her brush and painted desks, books, chalkboards, and even a roof over their heads.",
         "The children cheered and hugged her. 'You're a miracle!' they cried.",
         "'No,' Amara said gently. 'I just have a tool. The miracle is what you'll learn and become. That's up to you.'",
         "She taught the oldest child to read, and left the village glowing with hope."],
        "Amara in a faraway village, painting a school into existence, children cheering and grabbing the books eagerly, the brush creating desks and supplies")

    # Page 18
    add_story_page(pdf, 18,
        ["As years passed, Amara's village became the most beautiful and prosperous in all the land.",
         "Not because everyone was rich — but because everyone had what they needed, and they all helped each other.",
         "Amara had painted the village back to life. But more than that, her generosity had inspired others.",
         "Farmers shared their harvests. Builders helped fix each other's homes. Children helped younger children learn.",
         "Amara's brush had started something, and the village's own kindness kept it going."],
        "A thriving, beautiful village with happy people working together, gardens blooming, children playing, a community transformed by generosity and mutual support")

    # Page 19
    add_story_page(pdf, 19,
        ["Amara learned that the happiest she ever felt was NOT when she painted things for herself.",
         "It was when she saw a child eat a meal she'd painted, or a family sleep warm under a blanket she'd created.",
         "The joy of helping others was like a light inside her chest that never went out.",
         "Her selfish wishes had given her a moment of happiness. But her generous acts gave her a lifetime of it.",
         "'This is what the brush was teaching me all along,' she realized. 'My gift is not FOR me. It's THROUGH me.'"],
        "Amara watching children play in a schoolyard she painted, her hand over her heart, a glow of deep contentment and purpose, understanding her role as a giver")

    # Page 20
    add_story_page(pdf, 20,
        ["One evening, Amara sat painting a sunset on the hillside — just for the joy of it.",
         "Her mother sat beside her. 'I remember when you only painted for yourself,' her mother said.",
         "'I'm glad I stopped,' Amara replied. 'Painting for myself made me feel full for a moment. But painting for others fills me up forever.'",
         "'That's because gifts are like seeds,' her mother said. 'When you plant them in others, they grow into something much bigger than what you started with.'"],
        "Amara and her mother sitting on a hillside at sunset, Amara painting the real sunset with her glowing brush, a peaceful reflective scene of contentment and wisdom")

    # Page 21
    add_story_page(pdf, 21,
        ["Amara also discovered something beautiful — the brush worked best when she was joyful while painting.",
         "If she painted while feeling grateful and happy, the colors were brighter, the food tastier, the blankets warmer.",
         "But if she painted out of duty or resentment, the results were ordinary.",
         "'Paint with love,' the brush whispered to her. 'That's the real ingredient. Not magic — love.'",
         "And Amara did. Every single day, with love."],
        "Amara painting with a huge smile, the brush producing spectacular vibrant creations when she paints with love, colors more vivid than a rainbow, love visible as golden sparkles")

    # Page 22
    add_story_page(pdf, 22,
        ["When Amara grew old, she passed the brush to a young boy in the village who loved to paint as much as she once had.",
         "'Remember,' she told him, 'this brush has one rule: use it for others, and it will never fail you. Use it only for yourself, and it will sleep.'",
         "The boy nodded seriously. 'I'll paint for everyone, Amara. I promise.'",
         "And he did. Generation after generation, the brush was passed to a new painter with a generous heart."],
        "An elderly Amara handing the golden brush to a young boy artist, both looking at each other with deep understanding, the brush glowing between them, a passing-of-the-torch moment")

    # Page 23
    add_story_page(pdf, 23,
        ["Now, dear reader, here's what Amara wants you to know:",
         "You may not have a magic paintbrush, but you DO have gifts.",
         "Maybe you're good at sports, or math, or making people laugh, or being a good listener, or drawing, or building things.",
         "Whatever your gift is — it works the same way as Amara's brush.",
         "Use it to help others, and it will grow stronger and bring you more joy than you can imagine. Keep it only for yourself, and it slowly fades away."],
        "A child looking at their own hands, realizing their hands hold invisible gifts, a warm glow emanating from them, inspired by Amara's story to use their talents for good")

    # Page 24
    add_story_page(pdf, 24,
        ["Here are some ways YOUR gifts can be a magic paintbrush:",
         "If you are good at reading, read to someone who is learning. If you are good at sports, teach a younger child to play.",
         "If you are funny, make someone laugh on their worst day. If you are a good listener, sit with someone who needs to talk.",
         "If you can draw, make art that makes people smile. If you are strong, carry something heavy for someone who cannot.",
         "Every gift shared is a painting brought to life. Every talent used for others is magic made real."],
        "Children using different gifts to help each other — reading together, teaching sports, making art for others — each child's hands glowing like they hold a magic brush")

    # Page 25
    add_story_page(pdf, 25,
        ["And remember Amara's most important lesson:",
         "The joy of using your gift for yourself lasts a moment. The joy of using it for others lasts forever.",
         "So paint your world with generosity. Use what you have been given to make life more beautiful for everyone around you.",
         "That is the real magic. Not in the brush. In the heart that chooses to share.",
         "Your heart. Your gift. Your magic. Go paint something wonderful."],
        "A final image of a golden paintbrush resting in a child's hand, the child looking at the world with determination to use their gifts for good, golden light streaming outward")

    # Moral page
    create_moral_page(pdf, "Use Your Gifts to Help Others, Not Just Yourself",
        "Amara discovered that her magic paintbrush grew stronger when she used it for others and faded when she used it selfishly. Our gifts and talents work the same way! When we share what we're good at with others — helping, teaching, creating, comforting — it brings us more happiness than keeping everything for ourselves. Your unique ability is meant to make the world better. So share it freely, and watch it grow.")

    # Discussion Questions
    create_discussion_page(pdf, [
        "What gifts or talents do YOU have? (Remember, a gift can be anything — kindness counts too!)",
        "How could you use your gift to help someone else this week?",
        "Why do you think the brush stopped working when Amara was selfish, and grew stronger when she was generous?",
        "Have you ever felt really good after helping someone? What did you do?",
        "If you had Amara's magic paintbrush for one day, what would you paint to help people?"
    ])

    # About Author
    create_about_author_page(pdf)

    filepath = os.path.join(OUTPUT_DIR, "06-Amaras-Magic-Paintbrush.pdf")
    size = pdf.save(filepath)
    return filepath, size



# ============================================================
# BOOK 7: The Tortoise Who Wanted Wings
# ============================================================
def generate_book_07():
    """The Tortoise Who Wanted Wings - Moral: Appreciate what makes you unique."""
    pdf = PurePDF(title="The Tortoise Who Wanted Wings", author=AUTHOR)

    create_cover_page(pdf, "The Tortoise Who Wanted Wings", "appreciating what makes you unique and not comparing yourself to others")
    create_dedication_page(pdf, "To every child who has ever wished to be someone else — you are wonderfully made, exactly as you are.")

    # Page 1
    add_story_page(pdf, 1,
        ["In the Emerald Valley, where waterfalls tumbled over mossy rocks and butterflies danced in the breeze, there lived a tortoise named Taro.",
         "Taro was a fine tortoise — strong shell, sturdy legs, a calm and patient heart.",
         "But every morning, Taro would look up at the sky and watch the birds soar overhead, and his heart would ache with longing.",
         "'Oh, how I wish I could fly,' he would sigh. 'Birds are so lucky. They can go anywhere. I'm just stuck on the ground.'"],
        "A tortoise looking longingly up at the sky where colorful birds soar freely overhead, standing in a beautiful valley with waterfalls, his expression wistful and envious")

    # Page 2
    add_story_page(pdf, 2,
        ["Taro's best friend was a cheerful robin named Ruby. She visited him every day, landing on his shell.",
         "'Good morning, Taro! Isn't it a beautiful day?' Ruby would chirp.",
         "'It would be more beautiful from up there,' Taro always replied, looking skyward.",
         "Ruby tilted her head. 'But you have such wonderful things down here! The flowers, the mushrooms, the—'",
         "'I'd trade them all for wings,' Taro interrupted. He said this every single day."],
        "A friendly red robin perched on Taro the tortoise's shell, chatting with him, Taro gazing upward at the sky instead of at the beautiful flowers and nature around him")

    # Page 3
    add_story_page(pdf, 3,
        ["One day, a strange old owl appeared in the valley. Her name was Wisdom, and she was known for granting one wish to those who truly desired it.",
         "'I hear you want wings, little tortoise,' Wisdom said, her amber eyes glowing.",
         "'More than anything!' Taro said eagerly.",
         "Wisdom studied him carefully. 'Very well. I will give you wings for three days. But listen carefully: you must give up your shell to make room for them.'",
         "'My shell?' Taro hesitated for only a moment. 'Deal!'"],
        "An ancient mystical owl with glowing amber eyes perched on a branch above Taro, offering a magical bargain, Taro looking excited and eager, magical sparkles in the air")


    # Page 4
    add_story_page(pdf, 4,
        ["WHOOSH! In a swirl of golden feathers, Taro's shell dissolved and two green wings sprouted from his back.",
         "He was lighter! He could feel the wind on his bare back. He flapped once, twice — and LIFTED OFF THE GROUND!",
         "'I'm FLYING!' Taro shouted with pure joy. 'I'm actually flying!'",
         "He soared above the trees, above the waterfall, up into the clouds. The world below was tiny and beautiful.",
         "Ruby flew beside him, laughing. 'How does it feel?'",
         "'INCREDIBLE!' Taro whooped, doing a loop in the air."],
        "Taro with green wings instead of his shell, flying joyfully above the Emerald Valley with Ruby beside him, the landscape stunning below, pure happiness on his face")

    # Page 5
    add_story_page(pdf, 5,
        ["The first day of flying was the best day of Taro's life.",
         "He saw the valley from above — the waterfall looked like a silver ribbon, the meadow like a green blanket.",
         "He raced Ruby through the clouds and chased butterflies over the treetops.",
         "He felt free. Light. Unlimited. Everything he'd ever dreamed of.",
         "When night came, Taro was exhausted but blissfully happy. 'This is the life,' he murmured, falling asleep on a high branch."],
        "Taro perched on a high tree branch at sunset after a day of flying, exhausted but ecstatic, the valley spread out beautifully below him, stars beginning to appear")

    # Page 6
    add_story_page(pdf, 6,
        ["But that night, it rained. Hard.",
         "Without his shell, Taro had nothing to protect him from the cold, driving rain. His bare skin was soaked and freezing.",
         "He shivered on the branch, unable to tuck himself away like he always used to.",
         "'Just one bad night,' Taro told himself through chattering teeth. 'It's worth it for the flying.'",
         "But a small seed of doubt had been planted."],
        "Taro on a tree branch in heavy rain, completely exposed without his shell, shivering and miserable, water dripping off him with no protection from the cold")


    # Page 7
    add_story_page(pdf, 7,
        ["On day two, Taro flew to visit his old friend, the hedgehog named Bramble.",
         "But when he landed, a hawk spotted him — a small, unprotected creature on the ground.",
         "SWOOOOSH! The hawk dove at him with razor talons. Taro screamed and tried to fly away, but he was too slow on the takeoff.",
         "Without his shell, there was nothing to protect him. He dove behind a rock just in time, the hawk's claws scraping stone.",
         "Taro's heart hammered. In all his years as a tortoise, he'd never once been afraid of hawks. His shell had always kept him safe."],
        "A terrified Taro with wings but no shell diving behind a rock as a hawk swoops down with sharp talons, a near-miss, showing how vulnerable he is without protection")

    # Page 8
    add_story_page(pdf, 8,
        ["That afternoon, Taro passed the meadow where the tortoises gathered to eat clover.",
         "His family and friends were there, slowly munching on the sweet plants, safe in their shells.",
         "'Come join us, Taro!' his mother called. But Taro looked at the clover and realized he couldn't.",
         "His new light body needed different food — seeds and insects, like the birds ate. He couldn't digest clover anymore.",
         "He flew away, feeling strangely homesick for a life he still technically had."],
        "Taro flying above a group of happy tortoises eating clover in a meadow, looking down at them longingly, unable to join, feeling isolated from his own family")

    # Page 9
    add_story_page(pdf, 9,
        ["On the evening of day two, a terrible storm rolled in. Thunder crashed and lightning split the sky.",
         "Every bird found shelter in holes and nests. But Taro didn't have a nest. He didn't fit in bird holes.",
         "He huddled under a leaf, shaking. If he'd had his shell, he would have simply pulled in and been safe.",
         "Ruby found him and tried to cover him with her wings, but she was too small.",
         "'I miss my shell,' Taro whispered. The words surprised him. But they were true."],
        "Taro huddling miserably under a large leaf during a thunderstorm, tiny Ruby trying to shelter him with her small wings, lightning flashing in the dark sky, Taro looking homesick")


    # Page 10
    add_story_page(pdf, 10,
        ["On day three — the last day — something happened that changed everything.",
         "Taro was flying over the river when he heard screaming. A family of baby mice had fallen into the rushing water!",
         "The birds flew overhead, wanting to help, but they couldn't dive into water — their wings would get waterlogged.",
         "Taro dove down to help. But without his shell, the current pushed him around like a leaf. He was too light!",
         "A real tortoise — heavy, steady, strong — could have waded in and carried the mice on their shell. But Taro couldn't."],
        "Baby mice struggling in a rushing stream, birds hovering helplessly above, Taro trying to dive in but being pushed away by the current, too light without his shell to be steady in water")

    # Page 11
    add_story_page(pdf, 11,
        ["Just then, old Uncle Bato, a tortoise from Taro's family, came walking by with his heavy, magnificent shell.",
         "Without hesitating, Uncle Bato waded into the stream. The current pushed against him but his heavy shell and strong legs held firm.",
         "One by one, he placed the baby mice on his broad shell and carried them safely to shore.",
         "The mother mouse wept with gratitude. The birds cheered from above.",
         "And Taro watched from the air, feeling something he'd never felt before: he wished he was a tortoise again."],
        "Uncle Bato the tortoise wading steadily into the stream, baby mice climbing onto his broad shell, the current unable to push him, while Taro watches from above feeling helpless and envious of the tortoise")

    # Page 12
    add_story_page(pdf, 12,
        ["Taro landed next to Uncle Bato. 'You saved them! Because of your shell! Because you're heavy and strong!'",
         "Uncle Bato smiled slowly, as tortoises do. 'Yes. My shell is my gift. It protects me, carries others, and keeps me steady.'",
         "'I gave mine up,' Taro said sadly. 'I thought wings were better. I thought flying was everything.'",
         "'Flying is wonderful,' Uncle Bato said. 'But so is being steady. So is being strong. So is being able to weather any storm.'",
         "'The things you thought were weaknesses, Taro — your shell, your slowness, your weight — they were strengths all along.'"],
        "Taro and Uncle Bato on the riverbank, the rescued mice safe and waving thank you, Uncle Bato wise and kind, Taro looking at him with new understanding and appreciation")


    # Page 13
    add_story_page(pdf, 13,
        ["When the sun set on day three, the owl Wisdom appeared again.",
         "'Your three days are up,' she said. 'Would you like to keep your wings? Or would you like your shell back?'",
         "Every day of his life before this, Taro would have chosen wings without hesitating.",
         "But now he knew what he'd lost. Protection. Strength. Steadiness. The ability to help in ways birds never could.",
         "'Please,' Taro said. 'Give me back my shell. I know now what I am — and what I am is wonderful.'"],
        "Wisdom the owl appearing at sunset, Taro looking up at her with peaceful certainty, choosing his shell over wings, the evening sky golden behind them")

    # Page 14
    add_story_page(pdf, 14,
        ["In another swirl of golden feathers, the wings dissolved and Taro's beautiful shell returned.",
         "It settled onto his back — heavy, solid, perfect. Like putting on a warm coat after being cold.",
         "Taro pulled his head and legs inside, just to feel the safety of it. The comfort. The protection.",
         "'I missed you,' he whispered to his shell. And he meant it with his whole heart.",
         "He had never appreciated his shell until it was gone. Now he would never take it for granted again."],
        "Taro's shell reforming on his back in a magical golden swirl, Taro pulling into his shell with a blissful smile, feeling safe and whole again, relief and happiness radiating from him")

    # Page 15
    add_story_page(pdf, 15,
        ["Ruby landed on his shell and tapped it with her beak. 'Welcome back, old friend!'",
         "'Thank you for flying with me, Ruby,' Taro said. 'Flying was amazing. But I belong on the ground.'",
         "'Of course you do!' Ruby chirped. 'I fly, and you walk. I'm fast, and you're steady. That's what makes us such good friends!'",
         "Taro smiled. 'I think I finally understand. We're not supposed to be the same. We're supposed to be ourselves.'"],
        "Ruby perched happily on Taro's restored shell, both friends smiling at each other, a perfect partnership of different abilities, sunny valley around them")


    # Page 16
    add_story_page(pdf, 16,
        ["From that day on, Taro never wished for wings again.",
         "Instead, he discovered all the amazing things about being a tortoise that he'd never noticed before.",
         "His shell was a shelter when it rained. A table when friends visited. A slide for baby mice to play on.",
         "His slowness meant he noticed tiny beautiful things the fast animals missed — dew drops, new mushrooms, shy caterpillars.",
         "His weight meant he was steady in storms, strong in currents, and an anchor for those who needed one."],
        "Taro happily being a tortoise — baby mice sliding down his shell, him studying a tiny mushroom up close, standing steady in wind — enjoying all the things that make him unique")

    # Page 17
    add_story_page(pdf, 17,
        ["And whenever Taro met a young animal who wished to be something different — a fish who wanted to climb trees, a rabbit who wanted to swim — he would share his story.",
         "'I once wanted wings,' he'd say. 'I even had them for three days.'",
         "'What happened?' they'd ask, wide-eyed.",
         "'I learned that what I thought were weaknesses were actually my greatest strengths. The things that make you different are the things that make you wonderful.'",
         "'Be yourself. Fully, proudly, wonderfully yourself. That's better than any wings in the world.'"],
        "Taro surrounded by young animals of various species listening to his wisdom, all looking inspired, in a beautiful meadow setting, Taro content and wise")

    # Page 18
    add_story_page(pdf, 18,
        ["That afternoon, Taro did something he'd never done before — he went swimming.",
         "Without wings weighing him down, his shell made him perfectly buoyant in the water.",
         "He floated on the pond's surface like a boat, gentle and steady, while fish swam beneath him and dragonflies rested on his shell.",
         "'I can do things birds can't!' he laughed. 'I can swim! I can carry things on my back! I'm waterproof!'",
         "He splashed and paddled, discovering a whole new joy he'd been too busy envying birds to notice."],
        "Taro happily swimming in a pond, floating perfectly on the water with his shell, fish swimming below, dragonflies resting on his shell, pure joy at discovering his water abilities")

    # Page 19
    add_story_page(pdf, 19,
        ["The next day, a rainstorm came, and all the other animals scrambled for shelter.",
         "Taro simply pulled into his shell and listened to the beautiful sound of rain drumming on his back.",
         "It was like having his own personal house wherever he went! Warm, dry, and safe.",
         "When the storm passed, Taro popped his head out refreshed while everyone else was soaked and shivering.",
         "'Best roof in the world,' he grinned, patting his shell proudly."],
        "Taro contentedly inside his shell during a rainstorm, rain drumming on his shell, other animals soaked nearby, Taro popping out after dry and happy")

    # Page 20
    add_story_page(pdf, 20,
        ["Taro also discovered the gift of slowness. Because he moved slowly, he noticed everything.",
         "He found rare herbs that the fast animals ran past. He spotted a beautiful crystal hidden in the moss.",
         "He watched a caterpillar build its cocoon from start to finish — something no bird would ever be patient enough to see.",
         "'Speed makes you miss things,' Taro realized. 'Slowness makes you find them.'"],
        "Taro discovering a beautiful crystal in the moss, watching a caterpillar spin its cocoon, noticing tiny wonders all around him that faster animals miss entirely")

    # Page 21
    add_story_page(pdf, 21,
        ["From that day on, Taro never wished for wings again.",
         "Instead, he discovered all the amazing things about being a tortoise that he'd never noticed before.",
         "His shell was a shelter when it rained. A table when friends visited. A slide for baby mice to play on.",
         "His slowness meant he noticed tiny beautiful things the fast animals missed — dew drops, new mushrooms, shy caterpillars.",
         "His weight meant he was steady in storms, strong in currents, and an anchor for those who needed one."],
        "Taro happily being a tortoise — baby mice sliding down his shell, him studying a tiny mushroom up close, standing steady in wind — enjoying all the things that make him unique")

    # Page 22
    add_story_page(pdf, 22,
        ["And whenever Taro met a young animal who wished to be something different — a fish who wanted to climb trees, a rabbit who wanted to swim — he would share his story.",
         "'I once wanted wings,' he'd say. 'I even had them for three days.'",
         "'What happened?' they'd ask, wide-eyed.",
         "'I learned that what I thought were weaknesses were actually my greatest strengths. The things that make you different are the things that make you wonderful.'",
         "'Be yourself. Fully, proudly, wonderfully yourself. That's better than any wings in the world.'"],
        "Taro surrounded by young animals of various species listening to his wisdom, all looking inspired, in a beautiful meadow setting, Taro content and wise")

    # Page 23
    add_story_page(pdf, 23,
        ["So remember: you are not supposed to be like everyone else.",
         "Maybe you're quiet in a world of loud people. Maybe you're slow in a world of fast ones. Maybe you're different in ways that feel awkward or strange.",
         "But those differences? They're your superpowers. Your shell. Your unique gift to the world.",
         "Don't wish them away. Discover why they're wonderful. Because they ARE wonderful.",
         "And so are you. Exactly as you are. Wings or no wings."],
        "A beautiful final image of the Emerald Valley with all the different animals — tortoises, birds, fish, rabbits — each doing what they do best, a celebration of diversity and being yourself")

    # Page 24
    add_story_page(pdf, 24,
        ["Here is something to try, dear reader:",
         "Instead of thinking about what you wish you could do, make a list of what you CAN do.",
         "Write down five things that make you YOU. Five things you are good at. Five things that make you different from everyone else.",
         "Maybe you are patient. Maybe you are creative. Maybe you are strong, or kind, or funny, or observant.",
         "Those are not just traits. Those are your superpowers. Your shell. Wear them proudly."],
        "A child writing a list of their own unique qualities and strengths, each one drawn as a shield or superpower emblem, celebrating their unique traits")

    # Page 25
    add_story_page(pdf, 25,
        ["And whenever you catch yourself wishing you were someone else — stop.",
         "Instead, ask: 'What can I do today that only I can do? What makes me special that I have not even discovered yet?'",
         "The answers might surprise you. Because you, dear reader, are wonderfully and uniquely made.",
         "There is no one else in the whole world exactly like you. And the world needs exactly what only YOU can give.",
         "So be yourself. Fully. Proudly. Beautifully. Just like Taro learned to be."],
        "A child looking at their own reflection in a pond with a smile, seeing their unique self clearly for the first time, accepting and loving who they are, sunshine and flowers around them")

    # Moral page
    create_moral_page(pdf, "Appreciate What Makes You Unique",
        "Taro learned that wishing to be someone else means losing what makes YOU special. His shell, his slowness, his weight — all the things he thought were weaknesses — turned out to be incredible strengths. The same is true for you! The things that make you different are not flaws. They are features. They are gifts. They are exactly what the world needs. Instead of wishing you were like someone else, discover the superpower hiding in what makes you, you.")

    # Discussion Questions
    create_discussion_page(pdf, [
        "What's something about yourself that you sometimes wish was different? Can you think of how it might actually be a strength?",
        "Why do you think Taro missed his shell after only two days without it?",
        "What are some things that tortoises can do that birds can't? What can birds do that tortoises can't?",
        "Is it bad to admire what other people can do? What's the difference between admiring others and wishing you were them?",
        "What makes YOU unique? What can you do that nobody else does quite the same way?"
    ])

    # About Author
    create_about_author_page(pdf)

    filepath = os.path.join(OUTPUT_DIR, "07-The-Tortoise-Who-Wanted-Wings.pdf")
    size = pdf.save(filepath)
    return filepath, size



# ============================================================
# BOOK 8: Little Cloud's Big Rainstorm
# ============================================================
def generate_book_08():
    """Little Cloud's Big Rainstorm - Moral: It's okay to cry / Emotions are natural."""
    pdf = PurePDF(title="Little Cloud's Big Rainstorm", author=AUTHOR)

    create_cover_page(pdf, "Little Cloud's Big Rainstorm", "feelings, emotions, and why it's okay to cry")
    create_dedication_page(pdf, "To every child who has been told to stop crying — your tears are not weakness. They are rain that helps you grow.")

    # Page 1
    add_story_page(pdf, 1,
        ["Up in the sky, above the tallest mountains and below the smiling sun, there lived a little cloud named Cumulus.",
         "Cumulus was the smallest cloud in the sky family. He was round and fluffy and white, and he loved floating along on the breeze.",
         "All around him, the big clouds did their important jobs — carrying rain to the farmers' fields, bringing snow to the mountains, making thunder for the storms.",
         "But Cumulus had never rained. Not once. And he was determined to keep it that way."],
        "A small, round, fluffy white cloud floating in a bright blue sky, surrounded by larger clouds, looking cheerful but slightly tense, trying to hold everything in")

    # Page 2
    add_story_page(pdf, 2,
        ["You see, Cumulus thought that raining was embarrassing.",
         "When the big clouds rained, they got smaller. They went from bright white to heavy gray. Sometimes they even rumbled and cried out with thunder.",
         "'I don't want to get all dark and heavy,' Cumulus told himself. 'I want to stay white and light and happy forever!'",
         "So whenever he felt water droplets building up inside him — whenever he felt the rain wanting to come — he squeezed tight and held it all in."],
        "Cumulus watching a large gray cloud raining heavily below, looking uncomfortable and turning away, squeezing himself smaller to hold in the moisture building inside him")

    # Page 3
    add_story_page(pdf, 3,
        ["His mother, a beautiful cloud named Nimbus, noticed. 'Cumulus, darling, you look a little heavy today. Do you need to rain?'",
         "'NO!' Cumulus said quickly. 'I'm fine! I'm totally fine! See? Still white! Still light!'",
         "But he wasn't fine. He was getting heavier and heavier inside, holding more and more water that needed to fall.",
         "His edges were turning gray, but he tried to puff himself up white to hide it."],
        "Mother cloud Nimbus, soft and beautiful, looking concerned at Cumulus who is visibly getting heavier and slightly gray at the edges, puffing himself up to appear okay")


    # Page 4
    add_story_page(pdf, 4,
        ["Days passed. Cumulus kept holding everything in. And he kept getting heavier.",
         "He couldn't float as high anymore. He sank lower in the sky, barely above the treetops.",
         "The breeze that used to carry him easily now struggled. 'Whew, you're getting heavy, little one!' the wind said.",
         "'I'm FINE,' Cumulus insisted stubbornly, even as he dipped lower and lower.",
         "But inside, he felt awful. Tight. Heavy. Like he might burst at any moment."],
        "Cumulus floating very low in the sky, visibly heavy and dark gray, just above the treetops, struggling to stay up, the wind looking strained trying to carry him")

    # Page 5
    add_story_page(pdf, 5,
        ["One morning, Cumulus looked down and saw something terrible.",
         "Below him was a beautiful valley, but it was bone dry. The flowers were wilting. The grass was turning brown.",
         "The river was just a trickle. The animals gathered around the last puddle, thirsty and tired.",
         "A farmer looked up at the sky desperately. 'Please, clouds — we need rain! The crops are dying!'",
         "Cumulus felt his water shift inside him. His rain wanted to fall. But he held tighter."],
        "A dried-out valley below with wilting flowers, brown grass, and thirsty animals by a nearly dry river, a farmer looking up hopefully at the sky, Cumulus floating above full of water but refusing to release it")

    # Page 6
    add_story_page(pdf, 6,
        ["'Why don't you just let go?' asked a passing cloud named Drizzle.",
         "'I can't,' Cumulus said. 'If I rain, I'll get all dark and small and everyone will see my feelings.'",
         "'What's wrong with that?' Drizzle asked gently. 'I rain every other day. It feels wonderful — like a big exhale after holding your breath.'",
         "'It looks... messy,' Cumulus said. 'And weak. Strong clouds don't need to rain.'",
         "Drizzle shook her misty head. 'Oh, Cumulus. You have it backwards. Holding it ALL in? THAT'S what will hurt you.'"],
        "A gentle gray cloud named Drizzle talking to the heavy, struggling Cumulus, Drizzle looking concerned and wise, trying to convince Cumulus to let go")


    # Page 7
    add_story_page(pdf, 7,
        ["That night, Cumulus sank so low he was resting on the top of a hill. He was so heavy he couldn't move.",
         "A little girl was sitting on that hill, crying. Tears streamed down her face.",
         "'What's wrong?' Cumulus asked softly.",
         "'My dog is very sick,' the girl said through her tears. 'I'm so sad. I keep crying and I can't stop.'",
         "'Aren't you embarrassed?' Cumulus asked. 'People can see you crying.'"],
        "Cumulus resting heavily on a hilltop, too heavy to float, a young girl sitting nearby crying, both of them dealing with heavy feelings, a twilight scene")

    # Page 8
    add_story_page(pdf, 8,
        ["The girl wiped her eyes and looked at him. 'My mom says crying is like rain for the heart.'",
         "'What does that mean?' Cumulus asked.",
         "'It means feelings need to come out. If you hold them in too long, they get heavy and hurt.' She sniffled. 'After I cry, I always feel a little better. Lighter.'",
         "Cumulus felt something crack inside him. Lighter. That's all he wanted to feel. Light again.",
         "'But isn't crying... weak?' he asked in a tiny voice."],
        "Close-up of the girl and Cumulus talking, the girl wisely explaining about tears and rain, Cumulus listening intently, understanding dawning on his face")

    # Page 9
    add_story_page(pdf, 9,
        ["'Crying is the bravest thing there is,' the girl said. 'My dad told me that. It means you're strong enough to feel your feelings instead of hiding them.'",
         "She smiled through her tears. 'I'd rather cry than hold it all inside until I feel like I'm going to explode.'",
         "Cumulus looked at her — this small, brave human who wasn't ashamed of her tears.",
         "And he thought about himself — a cloud so afraid of rain that he was crushing himself to hold it in.",
         "'Maybe...' he whispered. 'Maybe it's time.'"],
        "The girl reaching out to touch Cumulus who is now nearly on the ground, both of them sharing a moment of understanding, stars beginning to appear in the sky")


    # Page 10
    add_story_page(pdf, 10,
        ["Cumulus rose back into the sky — one final push of effort — and floated above the dry, thirsty valley.",
         "He looked down at the wilting flowers, the thirsty animals, the desperate farmer.",
         "They needed his rain. The world NEEDED what he'd been holding in.",
         "He took a deep breath... and let go.",
         "For the first time in his life, Cumulus let the rain fall."],
        "Cumulus floating above the dry valley, taking a deep breath, the moment before letting go, a dramatic pause before the rain comes, moonlight and stars around him")

    # Page 11
    add_story_page(pdf, 11,
        ["And oh, what a rain it was!",
         "Not a drizzle, not a sprinkle — a magnificent, glorious downpour. Weeks and weeks of held-in rain came pouring out all at once.",
         "Cumulus turned dark gray, then purple with the effort. Thunder rumbled from deep inside him — all the feelings he'd kept locked away.",
         "Lightning flickered — the sparks of emotion finally being released.",
         "It was loud. It was messy. It was overwhelming. And it was BEAUTIFUL."],
        "A dramatic rainstorm unleashed from Cumulus — heavy rain pouring down, lightning flickering, thunder rumbling — a powerful emotional release depicted as a magnificent storm")

    # Page 12
    add_story_page(pdf, 12,
        ["Below him, the world came alive!",
         "The flowers lifted their heads and drank. The grass turned green almost instantly.",
         "The river swelled and sang again. Animals danced in the puddles.",
         "The farmer fell to his knees with joy. 'RAIN! Beautiful rain! Our crops are saved!'",
         "Everything Cumulus had held inside — every drop he thought was embarrassing — was exactly what the world needed."],
        "The valley transformed by the rain — flowers blooming, river flowing, animals playing in puddles, the farmer celebrating with arms raised, everything coming back to life beautifully")


    # Page 13
    add_story_page(pdf, 13,
        ["When the rain finally stopped, Cumulus felt... incredible.",
         "He was lighter than he'd been in weeks. The heaviness was gone. The tight, compressed feeling had melted away.",
         "He looked at himself — smaller now, yes, and still a little gray at the edges. But he could float again! High and free!",
         "It was exactly what the girl had described. Like a big exhale after holding your breath for too, too long.",
         "'That felt AMAZING,' Cumulus said, doing a little spin in the breeze."],
        "Cumulus after the rain — smaller and lighter, floating high in the sky again, spinning happily, light gray but with a huge smile, feeling relieved and free")

    # Page 14
    add_story_page(pdf, 14,
        ["His mother Nimbus floated over and wrapped herself around him in a warm, misty hug.",
         "'I'm so proud of you,' she said. 'That was a beautiful rain, my love.'",
         "'I was scared,' Cumulus admitted. 'I thought raining would make me weak.'",
         "'Oh, sweetheart,' Nimbus said. 'Raining is the bravest thing a cloud can do. It's sharing yourself with the world. It makes everything grow.'",
         "'Holding it in forever — THAT'S what was making you sick.'"],
        "Mother cloud Nimbus wrapping around little Cumulus in a warm misty embrace, both smiling, the sky blue and calm after the storm, a comforting mother-child moment")

    # Page 15
    add_story_page(pdf, 15,
        ["From that day on, Cumulus rained whenever he needed to.",
         "Sometimes it was a gentle drizzle on a quiet afternoon. Sometimes it was a thunderstorm when big feelings built up.",
         "Sometimes it was just a few drops — and that was okay too.",
         "He learned that every kind of rain was normal. Every kind of feeling was valid.",
         "And after every rain, he always felt lighter, fresher, and ready to float high again."],
        "A sequence showing Cumulus in different states — light drizzle, thunderstorm, gentle rain — all perfectly natural and healthy, ending with him floating happily after each one")


    # Page 16
    add_story_page(pdf, 16,
        ["And the valley below? It became the most lush, green, alive place in the world.",
         "Because Cumulus rained when he needed to, the flowers always had water. The crops always grew. The river always flowed.",
         "His feelings — his rain — didn't just help HIM. They helped everything around him grow.",
         "That's the secret no one tells you about tears: they don't just empty you out. They water the garden of your life."],
        "The valley below absolutely thriving and green and lush, all because Cumulus learned to rain regularly, a paradise of growth fed by healthy emotional release")

    # Page 17
    add_story_page(pdf, 17,
        ["Cumulus even learned that different feelings make different kinds of rain.",
         "Sadness made gentle, steady rain that helped flowers grow slowly and strong.",
         "Frustration made quick thunderstorms that cleared the air and made room for sunshine.",
         "Joy made sparkling mist that painted rainbows across the sky.",
         "Every feeling had its own weather, and every weather was needed and beautiful."],
        "Different types of rain from Cumulus — gentle rain growing flowers, a quick thunderstorm clearing air, sparkling mist creating rainbows — all beautiful and purposeful")

    # Page 18
    add_story_page(pdf, 18,
        ["One day, Cumulus met another small cloud who was holding in his rain just like he used to.",
         "'I can't let anyone see me cry,' the little cloud said, puffing up to hide his gray edges.",
         "Cumulus floated beside him gently. 'I used to think that too. Want to know what happened to me?'",
         "He told his whole story — the holding, the heaviness, the girl on the hill, and finally letting go.",
         "'After I rained,' Cumulus said, 'I felt the best I'd ever felt. Lighter than air. Try it. I'll rain with you.'"],
        "Cumulus floating beside another small puffy cloud who looks heavy and gray, talking gently to him, offering to rain together, a supportive friend helping another open up")

    # Page 19
    add_story_page(pdf, 19,
        ["Together, the two clouds rained side by side. The little cloud's first rain was small and timid.",
         "But Cumulus cheered him on: 'That's it! Let it go! You're doing great!'",
         "The little cloud rained harder, and harder, until a beautiful storm poured down together from both of them.",
         "Afterward, the little cloud was light and floating high. 'That felt INCREDIBLE! Why did I wait so long?'",
         "'We all wait too long,' Cumulus smiled. 'But it's never too late to let it out.'"],
        "Two clouds raining together side by side, supporting each other, both looking relieved and happy afterward, floating high and light, a buddy system for emotional expression")

    # Page 20
    add_story_page(pdf, 20,
        ["The little girl on the hill? Her dog got better. And she still visited Cumulus whenever he floated low.",
         "'Thank you,' she told him once. 'Watching you rain taught me something too.'",
         "'What's that?' Cumulus asked.",
         "'That everyone needs to let their feelings out — even big, strong clouds. It doesn't make us weak. It makes us real.'",
         "They sat together in comfortable silence, the girl and the cloud, two beings who understood that feelings are meant to flow, not to be dammed up inside."],
        "The girl sitting on her hill, healthy dog beside her, waving up at Cumulus who floats happily above, both peaceful and emotionally healthy, a warm friendship scene")

    # Page 21
    add_story_page(pdf, 21,
        ["Cumulus also learned when to ask for help. Sometimes his feelings were too big for just rain.",
         "On those days, he'd float to his mother Nimbus, or find Drizzle, or seek out the girl on the hill.",
         "'I'm having a really hard day,' he'd say. And they would simply be there with him.",
         "He learned that you don't always have to weather the storm alone. Sometimes the bravest thing is saying: I need help. I need someone to be with me.",
         "And there was always someone willing to be there."],
        "Cumulus with friends around him on a hard day — Nimbus nearby, Drizzle, the girl below — supported and not alone, showing that asking for help is also okay")

    # Page 22
    add_story_page(pdf, 22,
        ["So here's what Cumulus wants you to know, little reader:",
         "It's okay to cry. It's okay to feel sad, or angry, or scared, or overwhelmed.",
         "Those feelings are not weakness — they are rain. And rain makes things grow.",
         "Don't hold everything in until you feel like you're going to burst. Let it out. Cry if you need to. Talk about it. Express it.",
         "After every storm, the sky is clearer. After every cry, your heart is lighter. That's just how it works."],
        "A child reading this book, perhaps with tears in their eyes, realizing it's okay to feel and express emotions, a gentle and validating final image with a rainbow after rain")

    # Page 23
    add_story_page(pdf, 23,
        ["Here is your permission slip, signed by Cumulus himself:",
         "You are allowed to cry. You are allowed to feel angry. You are allowed to be sad.",
         "You are allowed to have big feelings that feel too big for your body.",
         "You are allowed to need a hug, need a friend, need to talk, or need to be alone.",
         "All of it is okay. All of it is natural. All of it makes you beautifully, wonderfully human."],
        "A permission slip drawn beautifully with cloud borders, giving children permission to feel all their feelings, signed with a cloud stamp, warm and validating and empowering")

    # Page 24
    add_story_page(pdf, 24,
        ["And after the rain comes the rainbow. After the tears comes the lightness. After the storm comes the clearest sky you have ever seen.",
         "So let it rain when it needs to. Let the feelings flow.",
         "You are not broken. You are not weak. You are a cloud doing exactly what clouds are meant to do.",
         "And the garden of your life will be all the more beautiful for every drop of rain that falls.",
         "Rain on, little cloud. Rain on."],
        "A magnificent rainbow arching across the sky after a rainstorm, Cumulus floating happily and lightly above it, the valley below green and alive, a hopeful and beautiful final image")

    # Page 25
    add_story_page(pdf, 25,
        ["One last thing Cumulus wants you to remember:",
         "If someone you love is holding in their rain — if someone seems heavy and struggling — be gentle with them.",
         "You can be their safe place. You can say: 'It is okay to cry. I am here. I will not think less of you.'",
         "Sometimes the kindest thing you can do for someone is give them permission to let their feelings out.",
         "Be a safe sky for other people's clouds. That is one of the greatest gifts you can give."],
        "Two children sitting together, one crying and the other with an arm around them providing comfort, showing that being a safe space for others' feelings is a beautiful gift")

    # Moral page
    create_moral_page(pdf, "It's Okay to Cry - Emotions Are Natural and Helpful",
        "Cumulus learned that holding in your feelings doesn't make you strong — it makes you heavy. Tears, like rain, are natural and necessary. They help you process hard feelings, release tension, and make room for happiness again. Everyone cries sometimes — even grown-ups, even tough people, even clouds! After you let your feelings out, you always feel lighter. So never be ashamed of your tears. They are proof that you feel deeply, and that is a beautiful thing.")

    # Discussion Questions
    create_discussion_page(pdf, [
        "When was the last time you cried? Did you feel better afterward?",
        "Why do you think some people say 'don't cry' or 'be strong'? Do you agree that crying IS being strong?",
        "What are some ways to express feelings besides crying? (Talking, drawing, running, etc.)",
        "How did Cumulus's rain help the valley below? How might your feelings help people around you?",
        "What would you say to a friend who was embarrassed about crying?"
    ])

    # About Author
    create_about_author_page(pdf)

    filepath = os.path.join(OUTPUT_DIR, "08-Little-Clouds-Big-Rainstorm.pdf")
    size = pdf.save(filepath)
    return filepath, size



# ============================================================
# BOOK 9: The Sharing Tree
# ============================================================
def generate_book_09():
    """The Sharing Tree - Moral: Generosity brings more happiness than hoarding."""
    pdf = PurePDF(title="The Sharing Tree", author=AUTHOR)

    create_cover_page(pdf, "The Sharing Tree", "generosity and why sharing brings more happiness than keeping things for yourself")
    create_dedication_page(pdf, "To every child who knows the joy of sharing — and to those about to discover it. The more you give, the more you have.")

    # Page 1
    add_story_page(pdf, 1,
        ["In the heart of Sunflower Meadow stood the most magnificent tree anyone had ever seen.",
         "It was called the Sharing Tree, and for a hundred years it had fed every creature in the meadow.",
         "Its branches hung heavy with the most delicious fruit — golden apples, purple plums, ruby cherries, and honey pears.",
         "Every animal was welcome to eat as much as they needed. And the tree always grew more."],
        "A spectacular, enormous tree loaded with colorful fruit of every kind, animals of all types gathered around eating happily, a magical golden glow surrounding the tree")

    # Page 2
    add_story_page(pdf, 2,
        ["The rabbits came for breakfast. The deer came for lunch. The birds snacked all day long.",
         "No one ever went hungry in Sunflower Meadow because the Sharing Tree had enough for everyone.",
         "And here was the magical part: the more fruit the animals took, the more the tree grew.",
         "Every fruit that was picked was replaced by two more. Sharing made the tree stronger, not weaker."],
        "Happy animals of various types eating from the tree at different times — rabbits, deer, birds, mice — the tree visibly growing new fruit wherever some has been taken")

    # Page 3
    add_story_page(pdf, 3,
        ["But then one autumn, a new animal arrived in Sunflower Meadow. His name was Gritch, and he was a very greedy squirrel.",
         "Gritch had come from a place where food was scarce, and he had learned to grab everything he could.",
         "When he saw the Sharing Tree, his eyes went wide with hunger — and then narrowed with greed.",
         "'All this fruit!' he whispered. 'If I take it ALL, I'll never be hungry again! I'll be the richest squirrel in the world!'"],
        "A sneaky-looking squirrel with greedy narrow eyes arriving at the edge of Sunflower Meadow, staring at the fruit-laden tree with an expression of selfish calculation")


    # Page 4
    add_story_page(pdf, 4,
        ["That very night, while everyone slept, Gritch worked furiously.",
         "He picked every single fruit from the Sharing Tree and stored them in his hollow log.",
         "Apples, plums, cherries, pears — he stuffed them all away where no one else could reach them.",
         "Then he built a wall around his log with sticks and thorns. 'MINE!' he declared. 'All mine!'",
         "By morning, the Sharing Tree stood bare — not a single fruit remained on its branches."],
        "Gritch frantically stuffing fruit into his hollow log in the moonlight, the tree being stripped bare, a wall of thorns being built around his stash, greedy and secretive")

    # Page 5
    add_story_page(pdf, 5,
        ["When the animals woke and came for breakfast, they found nothing. Just empty branches reaching toward the sky.",
         "'Where's the fruit?' the young rabbit cried, his tummy growling.",
         "The old deer looked worried. 'In all my years, the tree has never been empty.'",
         "Then they noticed Gritch sitting on his thorn-wall, cheeks puffed with fruit. 'What are you all staring at? Get your own food!'",
         "The animals looked at each other in confusion. Get their OWN food? The tree had always shared."],
        "The bare tree with empty branches, confused and hungry animals gathered beneath it, Gritch visible on his pile of hoarded fruit behind thorns, eating selfishly while others go hungry")

    # Page 6
    add_story_page(pdf, 6,
        ["Something terrible began to happen to the Sharing Tree.",
         "Without animals eating its fruit and spreading its seeds, the tree started to wilt.",
         "Its leaves turned yellow, then brown. Its branches drooped. Its bark turned gray and dry.",
         "The Sharing Tree was dying. Not from having too much taken — but from having NOTHING shared.",
         "The tree needed to give. That was its magic. That was its life. And Gritch had stopped the giving."],
        "The once-magnificent tree now wilting, leaves turning brown, branches drooping sadly, bark cracking, a sick and dying tree compared to its former glory")


    # Page 7
    add_story_page(pdf, 7,
        ["Meanwhile, Gritch sat in his log surrounded by mountains of fruit. More than he could ever eat.",
         "But a strange thing happened — the fruit was rotting. Faster than normal.",
         "The apples turned brown and mushy. The pears went soft and smelly. The plums grew fuzzy mold.",
         "Gritch tried eating faster, but he couldn't keep up with the rot. Food meant for sharing spoils when hoarded.",
         "'No! My precious fruit!' Gritch wailed, watching his treasure turn to mush."],
        "Gritch inside his log surrounded by rotting, moldy fruit, looking panicked as his hoarded treasure decays around him, a disgusting mess of spoiled food")

    # Page 8
    add_story_page(pdf, 8,
        ["Outside, the meadow was growing sad and quiet. Animals were hungry and leaving to find food elsewhere.",
         "The birds flew away. The deer moved to distant forests. The rabbits dug deeper into their burrows.",
         "Sunflower Meadow, once full of life and laughter, was becoming empty and silent.",
         "Even the sunflowers drooped their golden heads, missing the cheerful energy that used to fill the air."],
        "A desolate Sunflower Meadow with animals leaving — birds flying away, deer walking into the distance, empty rabbit holes — the once-vibrant meadow now quiet and lonely")

    # Page 9
    add_story_page(pdf, 9,
        ["A young mouse named Pip (the bravest in the meadow) went to talk to Gritch.",
         "'Gritch, please share the fruit. The tree is dying. The meadow is empty. Everyone is hungry.'",
         "'NOT MY PROBLEM!' Gritch snapped. 'I need to protect what's MINE!'",
         "'But it's all rotting,' Pip pointed out. 'You can't eat it all. It's going to waste. If you shared, there would be enough for everyone — including you.'",
         "Gritch slammed his thorn-door shut. 'Go away!'"],
        "Tiny brave mouse Pip standing outside Gritch's thorn wall, trying to reason with the angry squirrel who peers through a gap with hostile eyes, rotting fruit visible behind him")


    # Page 10
    add_story_page(pdf, 10,
        ["Days passed. The Sharing Tree was nearly dead now — just a skeleton of branches against the gray sky.",
         "And Gritch? Gritch was miserable. All his fruit was rotten. He was actually hungry now too.",
         "Worse than hunger, though, was the loneliness. There were no other animals to talk to. No one to play with. No sounds of life.",
         "He had everything he'd wanted — all the fruit to himself — and he'd never been more unhappy.",
         "'What's the point of having everything if you're all alone?' he whispered to his empty meadow."],
        "Gritch sitting alone outside his log, surrounded by rotten fruit, looking at the empty quiet meadow with a devastated expression, the dead tree in the background, complete loneliness")

    # Page 11
    add_story_page(pdf, 11,
        ["That night, Gritch had a dream. In the dream, the Sharing Tree spoke to him.",
         "'I was happiest when I was giving,' the tree said in a creaky, ancient voice. 'That is my nature. To share.'",
         "'But you kept everything, and now look at us both — I am dying, your fruit is rotten, and the meadow is empty.'",
         "'Is this what you wanted? To have everything and enjoy nothing?'",
         "Gritch woke up with tears in his eyes. 'No,' he whispered. 'This isn't what I wanted at all.'"],
        "A dream sequence with a ghostly image of the Sharing Tree speaking to Gritch, its trunk forming a wise ancient face, Gritch looking small and ashamed before it")

    # Page 12
    add_story_page(pdf, 12,
        ["The next morning, Gritch did something that surprised everyone — especially himself.",
         "He tore down his thorn wall. He dragged out all the remaining fruit (what hadn't rotted) and piled it beneath the dying tree.",
         "Then he dug the seeds from the rotted fruit and planted them in the earth around the tree's roots.",
         "'I'm sorry,' he said to the tree, to the meadow, to the empty sky. 'I'm sorry I took everything. I'm sorry I was greedy.'",
         "'I don't want to be alone anymore. I want the meadow to be alive again.'"],
        "Gritch tearfully tearing down his thorn walls, carrying fruit to the base of the dying tree, planting seeds in the ground, apologizing with genuine remorse")


    # Page 13
    add_story_page(pdf, 13,
        ["The moment Gritch gave back what he'd taken, something magical happened.",
         "The Sharing Tree shuddered. Its dry bark softened. A single green leaf sprouted from a bare branch.",
         "Then another. And another. Slowly, beautifully, the tree began to come back to life.",
         "The seeds Gritch planted began to sprout around the base. Tiny saplings pushed up through the earth.",
         "Generosity was flowing again, and the tree could feel it."],
        "The Sharing Tree beginning to revive — new green leaves sprouting on bare branches, tiny saplings growing around its base, a miraculous rebirth, Gritch watching in amazement")

    # Page 14
    add_story_page(pdf, 14,
        ["Pip the mouse saw the change and raced to tell the other animals. 'Come back! The tree is growing again!'",
         "Slowly, cautiously, the animals returned. The birds flew back. The deer emerged from the forest. The rabbits hopped out of their burrows.",
         "When they saw Gritch sitting beneath the recovering tree with no walls around him, they were confused.",
         "'I'm sorry,' Gritch said to each one. 'I took what belonged to all of us. I was wrong. Please come back.'"],
        "Animals cautiously returning to the meadow — birds landing in branches, deer approaching, rabbits hopping back — Gritch with no walls looking humble and apologetic")

    # Page 15
    add_story_page(pdf, 15,
        ["The animals were wary at first. Could they trust Gritch?",
         "But the tree was growing back, and Gritch was helping — watering the saplings, clearing the dead leaves, making space for others to sit in the shade.",
         "Day by day, he proved with his actions that he had changed. He took only what he needed and helped others get theirs.",
         "Trust, like the tree, grew back slowly. But it grew back."],
        "Gritch helping tend the tree — watering saplings, sweeping up dead leaves — while other animals watch, gradually moving closer, trust slowly rebuilding")


    # Page 16
    add_story_page(pdf, 16,
        ["Within weeks, the Sharing Tree was more magnificent than ever.",
         "Its branches spread wide and welcoming, heavy with twice as much fruit as before.",
         "The saplings Gritch had planted grew into a whole grove of young sharing trees.",
         "Instead of one tree feeding the meadow, now there were MANY — enough fruit for every creature, with plenty left over.",
         "Gritch's mistake had actually led to something wonderful: MORE sharing, not less."],
        "The restored Sharing Tree now surrounded by young saplings growing into a grove, even more fruit than before, the meadow flourishing, animals happily eating from multiple trees")

    # Page 17
    add_story_page(pdf, 17,
        ["And Gritch? Gritch became the most generous animal in the meadow.",
         "He'd learned the hard way what greed does — it rots your treasure, kills what feeds you, and drives everyone away.",
         "Now he was always the first to help others find the ripest fruit, the first to share his acorns in winter, the first to welcome new animals to the meadow.",
         "'Aren't you afraid of running out?' a young squirrel once asked him.",
         "'No,' Gritch smiled. 'I learned something important: sharing never makes less. It always makes more.'"],
        "Gritch happily helping other animals reach fruit, sharing generously with a young squirrel, looking content and peaceful, a completely transformed character")

    # Page 18
    add_story_page(pdf, 18,
        ["One cold winter, a family of rabbits arrived in the meadow with nothing — no food stored, no warm burrow prepared.",
         "The old Gritch would have ignored them. But the new Gritch immediately shared his acorn stash.",
         "'Take what you need!' he said, opening his stores. 'There is plenty for everyone.'",
         "Other animals joined in — bringing bedding, extra food, warm moss. The rabbit family was safe within hours.",
         "'This is how a community works,' Gritch told the young squirrel watching. 'When we ALL share, nobody goes without.'"],
        "Gritch opening his acorn store to a cold rabbit family, other animals bringing supplies too, a warm community coming together in winter, generosity in action")

    # Page 19
    add_story_page(pdf, 19,
        ["Spring came, and the rabbit family planted a whole new section of wildflowers in the meadow as thanks.",
         "'You shared with us when we had nothing,' they said. 'So we want to add beauty to this place for everyone.'",
         "Gritch smiled. That was how it always worked now — every gift given came back multiplied.",
         "Not because the animals were keeping score, but because generosity creates a cycle of giving that never ends.",
         "The meadow had become a place where everyone looked out for everyone else."],
        "The rabbit family planting colorful wildflowers in the meadow as a thank-you, Gritch watching happily, the cycle of generosity continuing, spring flowers blooming everywhere")

    # Page 20
    add_story_page(pdf, 20,
        ["Pip the mouse became Gritch's best friend — she had been the one brave enough to talk to him when no one else would.",
         "'You know what I admire most about you?' Pip told Gritch one evening. 'You did not just stop being greedy. You became the most generous animal I know.'",
         "'I had to make up for lost time,' Gritch laughed. 'And honestly? Giving things away feels SO much better than hoarding them.'",
         "'It is like my heart has more room now. When I was grabbing everything, my heart was cramped. Now that I give freely, it feels enormous.'"],
        "Gritch and tiny Pip sitting together at sunset, good friends now, both content, the magnificent grove of sharing trees behind them, a beautiful friendship")

    # Page 21
    add_story_page(pdf, 21,
        ["The Sharing Tree lived for another hundred years, and the grove grew even bigger.",
         "A plaque was placed at its base that read: 'This tree thrives on generosity. Take what you need. Share what you can. And there will always be enough for everyone.'",
         "And it was true. When everyone shared, there was always plenty. Always.",
         "Because that's the beautiful secret about generosity: it multiplies what you have. Hoarding divides it."],
        "The magnificent grove of sharing trees with a beautiful plaque at the base of the original tree, all the meadow animals living in abundance and harmony")

    # Page 22
    add_story_page(pdf, 22,
        ["So here's what the Sharing Tree teaches us:",
         "When you share — your toys, your snacks, your time, your kindness — it doesn't leave you with less.",
         "It actually gives you MORE: more friends, more happiness, more love coming back to you.",
         "But when you hoard and keep everything for yourself, it spoils. Like Gritch's fruit. It rots when it's not shared.",
         "Be generous. Share freely. And watch your world grow into a beautiful grove of goodness."],
        "A child sharing toys with friends, snacks with siblings, time with someone lonely — showing that sharing in real life creates abundance and joy, warm and inviting final image")

    # Page 23
    add_story_page(pdf, 23,
        ["Here is a challenge from the Sharing Tree, just for you:",
         "This week, try sharing something every single day. It does not have to be big.",
         "Monday: share a smile with someone who looks sad. Tuesday: share your time by helping with a chore. Wednesday: share a compliment — tell someone what you like about them.",
         "Thursday: share your food — give a friend half your cookie. Friday: share your things — lend a toy or a book.",
         "Watch what happens. Watch how sharing makes YOU feel. Watch how it makes others feel. Watch how the garden grows."],
        "A weekly calendar showing different sharing acts for each day, drawn like a child's colorful planner, with small flowers growing beside each completed sharing act")

    # Page 24
    add_story_page(pdf, 24,
        ["And always remember: the Sharing Tree's greatest lesson was not just about fruit.",
         "It was about this: things that are hoarded die. Things that are shared multiply.",
         "Love shared becomes more love. Joy shared becomes more joy. Kindness shared becomes more kindness.",
         "You are a Sharing Tree too. Everything you give away comes back to you doubled.",
         "So share without fear. Give without counting. And grow without limits."],
        "A child standing with arms outstretched like tree branches, friends and family gathered around like animals around the Sharing Tree, love and kindness flowing outward and returning multiplied")

    # Page 25
    add_story_page(pdf, 25,
        ["And so the story of the Sharing Tree goes on forever — because sharing never ends.",
         "Every time a child shares a toy, the tree grows a new branch. Every time someone gives a hug, a flower blooms on that branch.",
         "Every time a family shares a meal, the roots grow deeper and stronger.",
         "The Sharing Tree lives in all of us. And as long as one person somewhere is generous, it will never, ever die.",
         "Be that person today. Be the one who keeps the tree alive. Share something. Anything. And watch the magic grow."],
        "The magnificent Sharing Tree alive and growing across generations, children of all ages contributing to its growth through acts of sharing, timeless and eternal, a never-ending story")

    # Moral page
    create_moral_page(pdf, "Generosity Brings More Happiness Than Keeping Things for Yourself",
        "The Sharing Tree showed us that keeping everything for yourself doesn't make you happier — it makes you lonely and your treasures rot. But sharing? Sharing makes everything grow. When you give generously, you get back more than you gave — in friendship, in love, in the joy of making others happy. So share your toys, share your snacks, share your time, share your smile. You'll never run out of good things when your heart is generous.")

    # Discussion Questions
    create_discussion_page(pdf, [
        "Have you ever NOT wanted to share something? What happened? How did you feel?",
        "Why do you think the fruit rotted when Gritch hoarded it, but stayed fresh on the Sharing Tree?",
        "Can you think of something you could share this week that would make someone else happy?",
        "What's the difference between sharing because you want to and sharing because someone made you?",
        "If you were an animal in Sunflower Meadow, would you have forgiven Gritch? Why or why not?"
    ])

    # About Author
    create_about_author_page(pdf)

    filepath = os.path.join(OUTPUT_DIR, "09-The-Sharing-Tree.pdf")
    size = pdf.save(filepath)
    return filepath, size



# ============================================================
# BOOK 10: Zara and the Golden Rule
# ============================================================
def generate_book_10():
    """Zara and the Golden Rule - Moral: Treat others as you want to be treated."""
    pdf = PurePDF(title="Zara and the Golden Rule", author=AUTHOR)

    create_cover_page(pdf, "Zara and the Golden Rule", "empathy, treating others the way you want to be treated")
    create_dedication_page(pdf, "To every child learning empathy — the world becomes a better place one kind action at a time. You have the power to change everything.")

    # Page 1
    add_story_page(pdf, 1,
        ["Zara was eight years old, and she thought she was pretty great. She was funny, smart, and the fastest runner in her class.",
         "The problem was, Zara wasn't always nice about it.",
         "She laughed when others tripped. She bragged when she won races. She told her classmates their ideas were dumb.",
         "Zara didn't think she was being mean. She thought she was just being honest. But the other kids didn't feel that way."],
        "A confident young girl with curly hair, arms crossed with a smirk, on a school playground, other children looking hurt or annoyed in the background")

    # Page 2
    add_story_page(pdf, 2,
        ["'Zara, why can't you be nicer?' her mother asked one evening after a phone call from school.",
         "'I AM nice!' Zara protested. 'I just say what I think! Everyone's too sensitive!'",
         "'How would you feel if someone laughed at YOUR mistakes?' her mother asked gently.",
         "Zara rolled her eyes. 'That's different. I don't make mistakes.'",
         "Her mother sighed and kissed her forehead. 'One day, sweetheart, you'll understand.'"],
        "Zara and her mother at the kitchen table, mother looking concerned, Zara looking dismissive and unbothered, a gentle confrontation")

    # Page 3
    add_story_page(pdf, 3,
        ["The very next day, something strange happened.",
         "Zara found a small golden mirror in her desk at school. It wasn't there before. No one saw who left it.",
         "It was beautiful — oval-shaped with a golden frame carved with the words: 'SEE WHAT THEY SEE. FEEL WHAT THEY FEEL.'",
         "When Zara looked into it, she didn't see her own reflection. She saw... someone else. Someone familiar.",
         "It was showing her classmate, Malik, and he looked upset."],
        "Zara finding a mysterious golden oval mirror in her school desk, the frame inscribed with golden words, looking into it and seeing not her own face but another child's face looking sad")


    # Page 4
    add_story_page(pdf, 4,
        ["As Zara watched the mirror, she felt a rush of emotion that wasn't hers.",
         "Embarrassment. Shame. A sinking feeling in the stomach. The burning of tears being held back.",
         "She FELT what Malik was feeling. And then she saw why — in the mirror, she watched herself from yesterday, laughing at Malik when he stuttered during his class presentation.",
         "'Ha! Can't even talk right!' Mirror-Zara had said. And Mirror-Malik's heart had crumpled like paper.",
         "Zara dropped the mirror in shock. 'That's... that's how he felt when I laughed?'"],
        "Zara looking into the mirror in shock, seeing a scene of herself laughing at Malik, with visible emotion waves coming from the mirror into her heart, feeling his pain for the first time")

    # Page 5
    add_story_page(pdf, 5,
        ["At recess, Zara raced to the swings — she always got there first because she was fastest.",
         "She pushed ahead of a smaller girl named Deepa. 'I'm first! Move!'",
         "Deepa stepped back, eyes down. Zara barely noticed. She was already swinging.",
         "But then she glanced at the mirror in her pocket. It was glowing softly.",
         "She peeked at it — and felt Deepa's feelings hit her like a wave: small, invisible, not important enough."],
        "Zara on the swing, the golden mirror glowing in her pocket, a small girl walking away looking dejected, Zara's face changing from smug to troubled as she peeks at the mirror")

    # Page 6
    add_story_page(pdf, 6,
        ["All day, the mirror showed Zara how her words and actions made others feel.",
         "When she told Leo his drawing was ugly: hurt. Pride crushed. The desire to never draw again.",
         "When she ignored Nina trying to tell a story: invisible. Unimportant. Like her words didn't matter.",
         "When she rolled her eyes at the teacher's joke: dismissed. Embarrassed in front of the whole class.",
         "By the end of the day, Zara had felt more sadness than she'd ever felt in her whole life. And it was all sadness SHE had caused."],
        "A montage of Zara throughout the day — making faces, saying mean things — with the mirror showing her the feelings she caused: crushed expressions, hurt hearts, invisible people")


    # Page 7
    add_story_page(pdf, 7,
        ["That night, Zara cried in bed. Not because anyone was mean to HER, but because she finally understood how mean SHE had been.",
         "'I didn't know,' she whispered to the mirror. 'I didn't know they felt like that.'",
         "The mirror glowed gently, and new words appeared on its frame: 'NOW YOU KNOW. WHAT WILL YOU DO?'",
         "Zara wiped her tears. She thought about how she'd want to be treated if she were Malik. Or Deepa. Or Leo. Or Nina.",
         "She'd want kindness. She'd want to feel seen. She'd want people to build her up, not tear her down."],
        "Zara in bed at night, crying, holding the golden mirror, new golden words appearing on its frame, Zara looking determined through her tears to change")

    # Page 8
    add_story_page(pdf, 8,
        ["The next morning, Zara made a decision. She would treat everyone the way she'd want to be treated.",
         "At school, when Malik raised his hand to answer a question and stuttered on a word, Zara didn't laugh.",
         "Instead, she waited patiently, and when he got his answer right, she said, 'Good answer, Malik!'",
         "She peeked at the mirror. Malik's feeling: surprised. Happy. Proud. Like sunshine after a storm.",
         "Zara smiled. Making someone feel GOOD felt way better than making them feel bad."],
        "Zara in class giving Malik a thumbs up after his answer, Malik looking surprised and happy, the mirror in Zara's pocket glowing with warm golden light, a positive moment")

    # Page 9
    add_story_page(pdf, 9,
        ["At recess, Zara arrived at the swings first as usual. Deepa was walking toward them slowly, expecting to be pushed aside.",
         "Instead, Zara stepped back. 'Want to go first today, Deepa?'",
         "Deepa's mouth fell open. 'Really?'",
         "'Really,' Zara smiled.",
         "The mirror showed Deepa's feeling: shocked. Valued. Important. Like she mattered.",
         "And Zara? Waiting for the swing didn't hurt at all. But Deepa's smile was worth a thousand turns."],
        "Zara stepping aside and gesturing for Deepa to take the swing first, Deepa's face lighting up with surprise and joy, other kids watching this unusual act of kindness")


    # Page 10
    add_story_page(pdf, 10,
        ["Day after day, Zara practiced the Golden Rule: treat others the way you want to be treated.",
         "She complimented Leo's drawing (his feeling: inspired, confident). She listened to Nina's whole story (feeling: heard, valued).",
         "She cheered for classmates who did well (feeling: supported, celebrated).",
         "She apologized to people she'd hurt before (feeling: healed, forgiven, relieved).",
         "Each act of kindness felt like planting a seed. And those seeds were growing fast."],
        "Zara being kind in multiple scenes — complimenting art, listening attentively, cheering for others — each person glowing with positive emotions, the mirror showing happy faces")

    # Page 11
    add_story_page(pdf, 11,
        ["Something incredible started happening. The kindness was spreading.",
         "Malik, who Zara had encouraged, started encouraging the shy kids in class.",
         "Deepa, who Zara had let go first, started sharing her snacks with others.",
         "Leo, whose art Zara had praised, started drawing pictures for lonely classmates to cheer them up.",
         "Zara's kindness had started a ripple that spread through the entire school."],
        "A ripple effect visualization — Zara's kindness spreading to Malik, then to others, then to even more people, like dominoes of good feelings cascading through the school")

    # Page 12
    add_story_page(pdf, 12,
        ["One afternoon, something happened that Zara never expected.",
         "She tripped during a race in gym class and fell flat on her face. The old Zara's biggest fear — looking foolish in front of everyone.",
         "She lay on the ground, cheeks burning with embarrassment, waiting for the laughter.",
         "But instead of laughing... everyone rushed to help her up.",
         "'Are you okay, Zara?' 'Nice try, that was a hard race!' 'You'll get it next time!'"],
        "Zara fallen on a gym track, classmates rushing to help her up instead of laughing, hands reaching out to her from every direction, surprised and touched by the kindness")


    # Page 13
    add_story_page(pdf, 13,
        ["Zara looked up at all those kind faces and felt tears prick her eyes — happy tears this time.",
         "They were treating her the way she'd been treating them. With kindness. With support. With love.",
         "The Golden Rule worked both ways — when you treat others well, they treat YOU well too.",
         "She looked at the mirror one more time. It showed her OWN feelings now: loved. Supported. Part of something beautiful.",
         "She didn't need the mirror to tell her that. She could feel it in her own heart."],
        "Zara on the ground looking up at smiling classmates with happy tears in her eyes, the mirror showing her own joyful feelings, a moment of beautiful realization")

    # Page 14
    add_story_page(pdf, 14,
        ["That evening, Zara tried to look at the mirror again. But it had changed.",
         "Instead of showing other people's feelings, it simply showed her own reflection — a girl with kind eyes and a gentle smile.",
         "The golden words now read: 'You no longer need me. You can feel what others feel on your own now. That's called empathy.'",
         "Zara hugged the mirror to her chest. 'Thank you,' she whispered. 'Thank you for showing me.'"],
        "Zara looking into the mirror which now shows her own kind reflection, the golden words about empathy glowing warmly, Zara holding it gratefully")

    # Page 15
    add_story_page(pdf, 15,
        ["The next day, the mirror was gone. Vanished from her desk like it had never been there.",
         "But Zara didn't need it anymore. She had learned to do what the mirror did — she could imagine how others felt before she acted.",
         "Before saying something, she'd think: 'How would I feel if someone said this to ME?'",
         "Before doing something, she'd think: 'Would I want someone to do this to ME?'",
         "It was that simple. And it changed everything."],
        "Zara at school without the mirror, pausing thoughtfully before speaking, an imaginary thought bubble showing herself in the other person's shoes, practicing empathy naturally")


    # Page 16
    add_story_page(pdf, 16,
        ["By the end of the school year, Zara's class was the kindest, happiest class in the whole school.",
         "They had the fewest arguments, the most laughter, and the strongest friendships.",
         "Their teacher called them 'The Golden Rule Class' and other teachers brought their students to observe.",
         "'What's your secret?' other kids asked.",
         "'It's simple,' Zara would say. 'Before you do anything, ask yourself: would I want someone to do this to me?'"],
        "Zara's classroom full of happy, kind children working together and laughing, a banner reading 'The Golden Rule Class,' other students peeking in curiously from the doorway")

    # Page 17
    add_story_page(pdf, 17,
        ["Zara's mother hugged her one evening. 'I'm so proud of who you're becoming,' she said.",
         "'I understand now, Mom,' Zara said. 'When I was mean, I thought I was being strong. But I was actually weak.'",
         "'Being kind when you could be mean — THAT'S strength. Thinking about others' feelings before your own — THAT'S courage.'",
         "'And the best part? When you treat people well, the whole world treats YOU well back. It's like magic.'",
         "Her mother smiled. 'It IS magic. It's the oldest magic there is. The Golden Rule.'"],
        "Zara and her mother hugging at home, both smiling warmly, evening light coming through the window, a scene of growth and pride and love between mother and daughter")

    # Page 18
    add_story_page(pdf, 18,
        ["One day, a new student arrived at school. His name was Omar, and he was shy and quiet.",
         "Some kids ignored him. Others whispered about his accent. Omar sat alone at lunch, staring at his food.",
         "Zara watched him and immediately thought: 'How would I feel on my first day at a new school with no friends?'",
         "She knew the answer. Lonely. Scared. Invisible. She walked straight over to his table.",
         "'Hi Omar! I am Zara. Want to sit with us? We have an empty spot and my friend Malik tells the funniest jokes.'"],
        "Zara walking confidently over to the new boy Omar who sits alone, reaching out her hand, other kids at her table waving welcomingly, Omar looking surprised and hopeful")

    # Page 19
    add_story_page(pdf, 19,
        ["Omar's face lit up. 'Really? You want me to sit with you?'",
         "'Of course!' Zara smiled. She remembered how Deepa had felt when someone finally noticed her. She remembered what it was like to feel included.",
         "By the end of lunch, Omar was laughing at Malik's jokes, sharing stories about his old country, and looking like he belonged.",
         "'Thank you, Zara,' Omar said quietly as the bell rang. 'I was so scared nobody would talk to me.'",
         "'I know that feeling,' Zara said. 'And I never want anyone to feel it if I can help.'"],
        "Omar laughing at the lunch table with Zara and her friends, completely included and happy, a transformation from lonely to belonging in one lunch period")

    # Page 20
    add_story_page(pdf, 20,
        ["Zara also learned that the Golden Rule wasn't just about big moments — it was about tiny ones too.",
         "Holding the door for someone carrying heavy things. Saying 'good morning' to the janitor. Picking up a dropped pencil.",
         "Smiling at someone who looks sad. Saying 'please' and 'thank you' like you mean it.",
         "These tiny acts didn't seem like much, but the mirror had shown her — even small kindnesses create big feelings in others.",
         "Every single interaction was a chance to make the world a tiny bit better."],
        "A montage of Zara doing small kind acts throughout her day — holding doors, greeting the janitor, picking up dropped items, smiling at people — each one creating a small golden glow")

    # Page 21
    add_story_page(pdf, 21,
        ["Sometimes, Zara messed up. She was still human, after all.",
         "Sometimes she said something without thinking and saw the hurt flash across someone's face.",
         "But the difference now was that she NOTICED. She felt it. And she fixed it immediately.",
         "'I am sorry. That came out wrong. What I meant to say was...' became one of her most-used phrases.",
         "And people always forgave her because they knew she genuinely cared about their feelings."],
        "Zara catching herself after saying something thoughtless, immediately apologizing with sincerity, the other person's expression softening from hurt to understanding")

    # Page 22
    add_story_page(pdf, 22,
        ["So here's what Zara learned — and what she wants YOU to know:",
         "You have more power than you think. Every word you say and every thing you do affects the people around you.",
         "You can make someone's day wonderful or terrible — with just one sentence, one action, one choice.",
         "So before you speak, before you act, ask yourself the Golden Rule question:",
         "'Would I want someone to treat ME this way?'",
         "If the answer is yes — go ahead. If the answer is no — choose differently. It really is that simple."],
        "A child looking directly at the reader with kind eyes and an open expression, a golden glow around them representing the power they have to affect others positively, empowering and warm")

    # Page 23
    add_story_page(pdf, 23,
        ["Here is your Golden Rule challenge:",
         "Tomorrow, before every single thing you say or do, pause for ONE second and ask: Would I want this done to me?",
         "Before you tease someone — pause. Before you ignore someone — pause. Before you grab something first — pause.",
         "Just one second of thinking can change everything. One second turns a hurtful moment into a kind one.",
         "Try it for one day. Then try it for a week. Then watch your whole world transform, just like Zara's did."],
        "A child pausing before speaking, a small golden clock showing one second, the moment of choice between kindness and unkindness, choosing the golden path")

    # Page 24
    add_story_page(pdf, 24,
        ["And remember: the Golden Rule is not just about being nice. It is about SEEING people.",
         "Seeing when someone is lonely. Seeing when someone is hurt. Seeing when someone needs a friend.",
         "You do not need a magic mirror to do this. You just need to pay attention.",
         "Look at the people around you — really look. What do they need? What would YOU need in their shoes?",
         "The answer to that question is always the right thing to do. Always."],
        "A child looking around their classroom or playground, truly SEEING the people around them — noticing who is lonely, who is hurt, who needs a friend — with a gentle golden glow of awareness around them")

    # Page 25
    add_story_page(pdf, 25,
        ["The Golden Rule is the oldest rule in the world. Every culture, every religion, every wise teacher has taught it.",
         "Treat others as you want to be treated. It is that simple. And it is that powerful.",
         "One person using this rule can change a classroom. A classroom can change a school. A school can change a town.",
         "And you? You are that one person. Start today. Start now.",
         "The mirror is in your heart. The gold is in your hands. The rule is yours to live."],
        "A golden rule emblem glowing in a child's heart, ripples of golden light spreading outward to their classroom, their school, their community, showing how one person changes everything")

    # Moral page
    create_moral_page(pdf, "Treat Others as You Want to Be Treated",
        "Zara discovered that every action has a ripple. When she was mean, everyone around her became mean. When she was kind, everyone became kind. The Golden Rule is the most powerful rule in the world: treat others the way YOU want to be treated. Before you speak, imagine those words being said to you. Before you act, imagine someone doing that to you. If it would hurt you, don't do it to others. If it would make you happy, go ahead and spread that joy! You have the power to change your whole world — one kind action at a time.")

    # Discussion Questions
    create_discussion_page(pdf, [
        "If you had Zara's mirror, what do you think it would show you about how your words make others feel?",
        "Can you think of a time when someone's words hurt you? How did it feel? How would you want them to have treated you instead?",
        "What does 'treat others as you want to be treated' mean in YOUR life? Give a specific example.",
        "Why do you think Zara's whole class became kinder after she changed? How does one person's behavior affect everyone?",
        "What's one thing you could change about how you treat others this week?"
    ])

    # About Author
    create_about_author_page(pdf)

    filepath = os.path.join(OUTPUT_DIR, "10-Zara-and-the-Golden-Rule.pdf")
    size = pdf.save(filepath)
    return filepath, size



# ============================================================
# MAIN - Generate All 10 Books
# ============================================================
def main():
    """Generate all 10 kids story books."""
    print("=" * 70)
    print("  KIDS STORY BOOKS GENERATOR")
    print("  10 Illustrated Storybooks with Morals")
    print(f"  Author: {AUTHOR}")
    print("  Target Ages: 4-10 years old")
    print("=" * 70)
    print()

    generators = [
        ("Book 1: The Little Star Who Lost Her Sparkle", generate_book_01),
        ("Book 2: Kalu the Brave Little Elephant", generate_book_02),
        ("Book 3: The Garden of Kindness", generate_book_03),
        ("Book 4: Tiko and the Treasure of Friendship", generate_book_04),
        ("Book 5: The Boy Who Couldn't Stop Lying", generate_book_05),
        ("Book 6: Amara's Magic Paintbrush", generate_book_06),
        ("Book 7: The Tortoise Who Wanted Wings", generate_book_07),
        ("Book 8: Little Cloud's Big Rainstorm", generate_book_08),
        ("Book 9: The Sharing Tree", generate_book_09),
        ("Book 10: Zara and the Golden Rule", generate_book_10),
    ]

    results = []
    for i, (title, gen_func) in enumerate(generators, 1):
        print(f"[{i}/10] Generating: {title}")
        try:
            filepath, size = gen_func()
            size_kb = size / 1024
            print(f"       -> Saved: {os.path.basename(filepath)}")
            print(f"       -> Size: {size_kb:.1f} KB")
            results.append((title, filepath, size_kb))
        except Exception as e:
            print(f"       -> ERROR: {e}")
            import traceback
            traceback.print_exc()
        print()

    # Summary
    print()
    print("=" * 70)
    print("  GENERATION COMPLETE!")
    print("=" * 70)
    print()
    print(f"  Books generated: {len(results)}/10")
    print(f"  Output directory: {OUTPUT_DIR}/")
    print()
    print("  Generated Files:")
    for title, filepath, size_kb in results:
        print(f"    [{size_kb:.0f} KB] {os.path.basename(filepath)}")
    print()
    total = sum(s for _, _, s in results)
    print(f"  Total size: {total:.0f} KB ({total/1024:.1f} MB)")
    print()

    return results


if __name__ == "__main__":
    main()
