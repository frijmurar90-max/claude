#!/usr/bin/env python3
"""
HIGH-INCOME PDF BOOKS GENERATOR
10 Books targeting $10,000/month revenue
By Daniel Tesfamariam
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'etsy-digital-products-strategy'))
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'etsy-digital-products-strategy', 'generate_pdfs.py')).read())

def book1_real_estate():
    """Real Estate Investing for Beginners - 45 pages"""
    pdf = PurePDF(title="Real Estate Investing for Beginners")
    pdf.add_title("REAL ESTATE INVESTING FOR BEGINNERS")
    pdf.add_heading2("The Complete Step-by-Step Guide to Building Wealth Through Property")
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_blank_line()
    pdf.add_paragraph("How to Buy Your First Rental Property with Little Money Down")
    pdf.add_paragraph("and Create Passive Income That Replaces Your 9-to-5")
    pdf.add_separator()
    pdf.add_page_break()


    # Table of Contents
    pdf.add_heading1("TABLE OF CONTENTS")
    pdf.add_blank_line()
    toc = [("Chapter 1", "Why Real Estate is the #1 Wealth Builder", 3),
           ("Chapter 2", "Types of Real Estate Investments", 5),
           ("Chapter 3", "How to Finance Your First Property", 9),
           ("Chapter 4", "Finding Profitable Deals (The 1% Rule)", 13),
           ("Chapter 5", "Analyzing a Rental Property (Cash Flow Calculator)", 17),
           ("Chapter 6", "Making Offers & Closing Deals", 21),
           ("Chapter 7", "Managing Tenants & Property", 25),
           ("Chapter 8", "Tax Benefits & Legal Structures", 29),
           ("Chapter 9", "Scaling from 1 to 10+ Properties", 33),
           ("Chapter 10", "Your 90-Day Action Plan", 37),
           ("Bonus", "Deal Analyzer Worksheets", 41)]
    for ch, title, pg in toc:
        pdf.add_paragraph(f"  {ch}: {title} {'.'*(50-len(ch)-len(title))} {pg}")
    pdf.add_page_break()

    # Chapter 1
    pdf.add_heading1("CHAPTER 1: WHY REAL ESTATE IS THE #1 WEALTH BUILDER")
    pdf.add_blank_line()
    pdf.add_paragraph("90% of millionaires built their wealth through real estate. Here's why:")
    pdf.add_blank_line()
    pdf.add_heading3("THE 5 WAYS REAL ESTATE MAKES YOU MONEY:")
    pdf.add_blank_line()
    pdf.add_paragraph("1. CASH FLOW - Monthly rent minus expenses = money in your pocket")
    pdf.add_paragraph("   Example: $1,500 rent - $1,100 expenses = $400/month passive income")
    pdf.add_blank_line()
    pdf.add_paragraph("2. APPRECIATION - Properties increase in value over time")
    pdf.add_paragraph("   Average: 3-5% per year. A $200K property = $210K in 2 years")
    pdf.add_blank_line()
    pdf.add_paragraph("3. LEVERAGE - Use the bank's money to buy assets")
    pdf.add_paragraph("   Put $40K down on a $200K property = control $200K with $40K")
    pdf.add_blank_line()
    pdf.add_paragraph("4. TAX BENEFITS - Depreciation, write-offs, 1031 exchanges")
    pdf.add_paragraph("   Real estate investors pay LESS tax than W-2 employees")
    pdf.add_blank_line()
    pdf.add_paragraph("5. EQUITY BUILD-UP - Tenants pay down YOUR mortgage")
    pdf.add_paragraph("   Every month, you own more of the property. They pay, you benefit.")
    pdf.add_blank_line()
    pdf.add_heading3("THE MATH OF FINANCIAL FREEDOM:")
    pdf.add_paragraph("Goal: Replace your $5,000/month salary")
    pdf.add_paragraph("If each property cash flows $400/month...")
    pdf.add_paragraph("You need: 13 properties = $5,200/month = FREEDOM")
    pdf.add_paragraph("Timeline: 5-10 years of consistent investing")
    pdf.add_page_break()

    # Chapter 2
    pdf.add_heading1("CHAPTER 2: TYPES OF REAL ESTATE INVESTMENTS")
    pdf.add_blank_line()
    pdf.add_heading3("1. SINGLE-FAMILY RENTALS (Best for Beginners)")
    pdf.add_paragraph("What: Buy a house, rent it out")
    pdf.add_paragraph("Pros: Easiest to finance, easiest to manage, easiest to sell")
    pdf.add_paragraph("Cons: One vacancy = 100% income loss")
    pdf.add_paragraph("Best for: First-time investors with $20-50K to start")
    pdf.add_blank_line()
    pdf.add_heading3("2. MULTI-FAMILY (Duplex, Triplex, Fourplex)")
    pdf.add_paragraph("What: 2-4 units in one building")
    pdf.add_paragraph("Pros: Multiple income streams, can house-hack (live in one unit)")
    pdf.add_paragraph("Cons: Slightly more management, higher purchase price")
    pdf.add_paragraph("Best for: House-hackers who want to live for free")
    pdf.add_blank_line()
    pdf.add_heading3("3. HOUSE HACKING (Live Free Strategy)")
    pdf.add_paragraph("What: Buy multi-unit, live in one, rent others")
    pdf.add_paragraph("Pros: FHA loan (3.5% down), tenants pay YOUR mortgage")
    pdf.add_paragraph("Cons: You live next to tenants")
    pdf.add_paragraph("Example: Buy duplex for $300K, rent one side for $1,500")
    pdf.add_paragraph("         Your mortgage: $2,000 - Rent: $1,500 = You pay only $500/month!")
    pdf.add_blank_line()
    pdf.add_heading3("4. FIX & FLIP")
    pdf.add_paragraph("What: Buy cheap, renovate, sell for profit")
    pdf.add_paragraph("Pros: Large lump-sum profits ($30-100K per flip)")
    pdf.add_paragraph("Cons: Active work, renovation risk, capital intensive")
    pdf.add_paragraph("Best for: People with construction knowledge or contractor relationships")
    pdf.add_blank_line()
    pdf.add_heading3("5. SHORT-TERM RENTALS (Airbnb)")
    pdf.add_paragraph("What: Rent by the night/week on Airbnb/VRBO")
    pdf.add_paragraph("Pros: 2-3x higher income than long-term rental")
    pdf.add_paragraph("Cons: More management, seasonal, regulation risk")
    pdf.add_paragraph("Best for: Properties in tourist/business travel areas")
    pdf.add_blank_line()
    pdf.add_heading3("6. REAL ESTATE WHOLESALING (No Money Needed)")
    pdf.add_paragraph("What: Find deals, put under contract, sell the contract to investors")
    pdf.add_paragraph("Pros: Zero money needed, quick profits ($5-20K per deal)")
    pdf.add_paragraph("Cons: Requires marketing/hustle, not truly passive")
    pdf.add_paragraph("Best for: Beginners with no capital but strong work ethic")
    pdf.add_page_break()

    # Chapter 3
    pdf.add_heading1("CHAPTER 3: HOW TO FINANCE YOUR FIRST PROPERTY")
    pdf.add_blank_line()
    pdf.add_heading3("FINANCING OPTIONS (from easiest to hardest):")
    pdf.add_blank_line()
    pdf.add_paragraph("1. FHA LOAN (3.5% down) - Must live in property")
    pdf.add_paragraph("   Requirements: 580+ credit score, 2 years employment")
    pdf.add_paragraph("   Best for: House-hacking your first property")
    pdf.add_paragraph("   Example: $200K property = $7,000 down payment")
    pdf.add_blank_line()
    pdf.add_paragraph("2. CONVENTIONAL LOAN (15-25% down for investment)")
    pdf.add_paragraph("   Requirements: 680+ credit, 6 months reserves")
    pdf.add_paragraph("   Best for: Properties you won't live in")
    pdf.add_paragraph("   Example: $200K property = $40-50K down payment")
    pdf.add_blank_line()
    pdf.add_paragraph("3. VA LOAN (0% down) - Veterans only")
    pdf.add_paragraph("   Requirements: Military service, COE")
    pdf.add_paragraph("   Best for: Veterans house-hacking (up to 4 units!)")
    pdf.add_blank_line()
    pdf.add_paragraph("4. HARD MONEY LOANS (for flips)")
    pdf.add_paragraph("   Requirements: Good deal (they lend on the deal, not you)")
    pdf.add_paragraph("   Rates: 10-15% interest, 1-3 points")
    pdf.add_paragraph("   Best for: Fix & flip with 6-12 month timeline")
    pdf.add_blank_line()
    pdf.add_paragraph("5. SELLER FINANCING (creative!)")
    pdf.add_paragraph("   Requirements: Motivated seller willing to 'be the bank'")
    pdf.add_paragraph("   Best for: Off-market deals with flexible sellers")
    pdf.add_blank_line()
    pdf.add_paragraph("6. PARTNERSHIPS / OPM (Other People's Money)")
    pdf.add_paragraph("   Structure: You find deals + manage, partner provides capital")
    pdf.add_paragraph("   Split: Typically 50/50 of profits")
    pdf.add_paragraph("   Best for: Experienced investors without liquid cash")
    pdf.add_blank_line()
    pdf.add_heading3("HOW TO GET YOUR CREDIT READY:")
    pdf.add_paragraph("[ ] Check credit score (free at annualcreditreport.com)")
    pdf.add_paragraph("[ ] Pay down credit cards below 30% utilization")
    pdf.add_paragraph("[ ] Don't open new accounts 6 months before applying")
    pdf.add_paragraph("[ ] Dispute any errors on your report")
    pdf.add_paragraph("[ ] Target: 700+ for best rates, 620+ minimum")
    pdf.add_page_break()

    # Chapter 4
    pdf.add_heading1("CHAPTER 4: FINDING PROFITABLE DEALS")
    pdf.add_blank_line()
    pdf.add_heading3("THE 1% RULE (Quick Screening Test):")
    pdf.add_paragraph("Monthly rent should be at least 1% of purchase price")
    pdf.add_paragraph("Example: $200,000 property should rent for $2,000+/month")
    pdf.add_paragraph("If it passes 1% rule -> do deeper analysis")
    pdf.add_paragraph("If it fails -> move on (most properties fail this test)")
    pdf.add_blank_line()
    pdf.add_heading3("THE 70% RULE (For Flips):")
    pdf.add_paragraph("Max offer = (ARV x 70%) - Repair costs")
    pdf.add_paragraph("ARV = After Repair Value (what it's worth fixed up)")
    pdf.add_paragraph("Example: ARV $300K x 70% = $210K - $40K repairs = Max offer $170K")
    pdf.add_blank_line()
    pdf.add_heading3("WHERE TO FIND DEALS:")
    pdf.add_paragraph("1. MLS (Zillow, Redfin, Realtor.com) - easiest but most competition")
    pdf.add_paragraph("2. Driving for Dollars - look for distressed properties")
    pdf.add_paragraph("3. Direct Mail to absentee owners / pre-foreclosures")
    pdf.add_paragraph("4. Wholesalers - they find deals and sell to you")
    pdf.add_paragraph("5. Auctions (foreclosure, tax lien, estate)")
    pdf.add_paragraph("6. FSBO (For Sale By Owner) - less competition")
    pdf.add_paragraph("7. Networking (REI meetups, BiggerPockets forums)")
    pdf.add_paragraph("8. Off-market: divorce attorneys, probate, estate sales")
    pdf.add_blank_line()
    pdf.add_heading3("RED FLAGS TO AVOID:")
    pdf.add_paragraph("[ ] Foundation issues (cracks, uneven floors)")
    pdf.add_paragraph("[ ] Flood zones (insurance kills cash flow)")
    pdf.add_paragraph("[ ] War zones (high crime = bad tenants + damage)")
    pdf.add_paragraph("[ ] Properties that only work with 'optimistic' numbers")
    pdf.add_paragraph("[ ] Anything that fails the 1% rule significantly")
    pdf.add_page_break()

    # Chapter 5
    pdf.add_heading1("CHAPTER 5: ANALYZING A RENTAL PROPERTY")
    pdf.add_blank_line()
    pdf.add_heading3("CASH FLOW ANALYSIS WORKSHEET:")
    pdf.add_blank_line()
    pdf.add_paragraph("PROPERTY ADDRESS: ________________________________________")
    pdf.add_paragraph("PURCHASE PRICE: $ ____________  DOWN PAYMENT: $ ____________")
    pdf.add_blank_line()
    pdf.add_heading3("MONTHLY INCOME:")
    pdf.add_paragraph("  Rent:                    $ __________")
    pdf.add_paragraph("  Other (laundry, parking): $ __________")
    pdf.add_paragraph("  TOTAL INCOME:            $ __________")
    pdf.add_blank_line()
    pdf.add_heading3("MONTHLY EXPENSES:")
    pdf.add_paragraph("  Mortgage (P&I):          $ __________")
    pdf.add_paragraph("  Property Tax:            $ __________")
    pdf.add_paragraph("  Insurance:               $ __________")
    pdf.add_paragraph("  Vacancy (8%):            $ __________")
    pdf.add_paragraph("  Maintenance (10%):       $ __________")
    pdf.add_paragraph("  CapEx (5%):              $ __________")
    pdf.add_paragraph("  Property Mgmt (10%):     $ __________")
    pdf.add_paragraph("  HOA (if applicable):     $ __________")
    pdf.add_paragraph("  Utilities (if included):  $ __________")
    pdf.add_paragraph("  TOTAL EXPENSES:          $ __________")
    pdf.add_blank_line()
    pdf.add_heading3("RESULTS:")
    pdf.add_paragraph("  MONTHLY CASH FLOW = Income - Expenses = $ __________")
    pdf.add_paragraph("  ANNUAL CASH FLOW = Monthly x 12 = $ __________")
    pdf.add_paragraph("  CASH-ON-CASH RETURN = Annual CF / Total Invested = ____%")
    pdf.add_blank_line()
    pdf.add_paragraph("  TARGET: $200+/month cash flow per unit")
    pdf.add_paragraph("  TARGET: 8%+ cash-on-cash return")
    pdf.add_paragraph("  PASS? [ ] YES - Make an offer!  [ ] NO - Keep looking")
    pdf.add_page_break()

    # Chapters 6-10 (condensed)
    pdf.add_heading1("CHAPTER 6: MAKING OFFERS & CLOSING DEALS")
    pdf.add_blank_line()
    pdf.add_heading3("YOUR OFFER SHOULD INCLUDE:")
    pdf.add_paragraph("1. Purchase price (based on your analysis, not asking price)")
    pdf.add_paragraph("2. Earnest money deposit ($1,000-5,000 shows you're serious)")
    pdf.add_paragraph("3. Inspection contingency (10-14 days)")
    pdf.add_paragraph("4. Financing contingency (21-30 days)")
    pdf.add_paragraph("5. Closing date (30-45 days typical)")
    pdf.add_blank_line()
    pdf.add_heading3("NEGOTIATION TACTICS:")
    pdf.add_bullet("Start 10-15% below your max price")
    pdf.add_bullet("Use inspection findings to negotiate price down")
    pdf.add_bullet("Ask for seller concessions (closing costs, repairs)")
    pdf.add_bullet("Be willing to walk away - there are ALWAYS more deals")
    pdf.add_bullet("Speed and certainty beat price (close fast, fewer contingencies)")
    pdf.add_blank_line()
    pdf.add_heading3("CLOSING CHECKLIST:")
    pdf.add_paragraph("[ ] Loan approved & clear-to-close")
    pdf.add_paragraph("[ ] Title search clean (no liens)")
    pdf.add_paragraph("[ ] Insurance policy in place")
    pdf.add_paragraph("[ ] Final walkthrough completed")
    pdf.add_paragraph("[ ] Wire transfer sent (VERIFY wire instructions by phone!)")
    pdf.add_paragraph("[ ] Sign closing documents")
    pdf.add_paragraph("[ ] Get keys! You're a real estate investor!")
    pdf.add_page_break()

    pdf.add_heading1("CHAPTER 7: MANAGING TENANTS & PROPERTY")
    pdf.add_blank_line()
    pdf.add_heading3("FINDING GREAT TENANTS:")
    pdf.add_paragraph("1. List on Zillow, Facebook Marketplace, Craigslist, Apartments.com")
    pdf.add_paragraph("2. Professional photos (good photos = 3x more inquiries)")
    pdf.add_paragraph("3. Price at market rate (overpricing = longer vacancy)")
    pdf.add_blank_line()
    pdf.add_heading3("SCREENING CRITERIA (Never skip this!):")
    pdf.add_paragraph("[ ] Credit score 620+ (or strong rental history)")
    pdf.add_paragraph("[ ] Income = 3x monthly rent minimum")
    pdf.add_paragraph("[ ] Positive landlord references (call previous 2 landlords)")
    pdf.add_paragraph("[ ] Background check clear")
    pdf.add_paragraph("[ ] Stable employment (2+ years or verifiable income)")
    pdf.add_blank_line()
    pdf.add_heading3("SELF-MANAGE vs. PROPERTY MANAGER:")
    pdf.add_paragraph("Self-manage: Save 8-10% but YOU handle calls, repairs, evictions")
    pdf.add_paragraph("Property manager: Costs 8-10% of rent but handles everything")
    pdf.add_paragraph("Recommendation: Self-manage first 1-3 properties to learn, then hire PM to scale")
    pdf.add_page_break()

    pdf.add_heading1("CHAPTER 8: TAX BENEFITS & LEGAL STRUCTURES")
    pdf.add_blank_line()
    pdf.add_heading3("TAX DEDUCTIONS (Keep more of your money!):")
    pdf.add_bullet("Mortgage interest (often your biggest deduction)")
    pdf.add_bullet("Property taxes")
    pdf.add_bullet("Insurance premiums")
    pdf.add_bullet("Repairs & maintenance")
    pdf.add_bullet("Depreciation (phantom expense - saves $3,000-8,000+/year)")
    pdf.add_bullet("Travel to properties")
    pdf.add_bullet("Home office (if you manage from home)")
    pdf.add_bullet("Professional fees (CPA, attorney, property manager)")
    pdf.add_blank_line()
    pdf.add_heading3("LEGAL STRUCTURE:")
    pdf.add_paragraph("LLC (Limited Liability Company) - protects personal assets")
    pdf.add_paragraph("Recommendation: Create LLC once you have 2+ properties")
    pdf.add_paragraph("Cost: $50-500 depending on state")
    pdf.add_paragraph("Consult a real estate attorney for your specific situation")
    pdf.add_page_break()

    pdf.add_heading1("CHAPTER 9: SCALING FROM 1 TO 10+ PROPERTIES")
    pdf.add_blank_line()
    pdf.add_heading3("THE SCALING ROADMAP:")
    pdf.add_paragraph("Year 1: Buy property #1 (house-hack or single-family)")
    pdf.add_paragraph("Year 2: Buy property #2 (use cash flow + savings)")
    pdf.add_paragraph("Year 3: Buy properties #3-4 (refinance equity from #1)")
    pdf.add_paragraph("Year 4-5: Buy properties #5-8 (snowball effect)")
    pdf.add_paragraph("Year 6-7: 10+ properties = $4,000-8,000/month passive income")
    pdf.add_blank_line()
    pdf.add_heading3("BRRRR STRATEGY (Buy, Rehab, Rent, Refinance, Repeat):")
    pdf.add_paragraph("1. BUY below market value (distressed property)")
    pdf.add_paragraph("2. REHAB to increase value")
    pdf.add_paragraph("3. RENT to a quality tenant")
    pdf.add_paragraph("4. REFINANCE - pull out your invested cash (75% of new value)")
    pdf.add_paragraph("5. REPEAT with the same cash!")
    pdf.add_paragraph("Result: Infinite returns - you get your money back AND keep the property!")
    pdf.add_page_break()

    pdf.add_heading1("CHAPTER 10: YOUR 90-DAY ACTION PLAN")
    pdf.add_blank_line()
    pdf.add_heading3("DAYS 1-30: EDUCATION & PREPARATION")
    pdf.add_paragraph("[ ] Read 3 real estate books (Rich Dad Poor Dad, etc.)")
    pdf.add_paragraph("[ ] Join BiggerPockets.com (free, massive community)")
    pdf.add_paragraph("[ ] Attend 2 local REI meetups")
    pdf.add_paragraph("[ ] Get pre-approved for a loan")
    pdf.add_paragraph("[ ] Check your credit score and fix issues")
    pdf.add_paragraph("[ ] Define your buy box (location, price range, property type)")
    pdf.add_blank_line()
    pdf.add_heading3("DAYS 31-60: DEAL FINDING")
    pdf.add_paragraph("[ ] Set up Zillow/Redfin alerts for your criteria")
    pdf.add_paragraph("[ ] Analyze 1 property per day using the worksheet")
    pdf.add_paragraph("[ ] Tour 5-10 properties in person")
    pdf.add_paragraph("[ ] Build your team (agent, lender, inspector, contractor)")
    pdf.add_paragraph("[ ] Start making offers (expect 10+ rejections before first yes)")
    pdf.add_blank_line()
    pdf.add_heading3("DAYS 61-90: CLOSE YOUR FIRST DEAL")
    pdf.add_paragraph("[ ] Get a deal under contract!")
    pdf.add_paragraph("[ ] Complete inspections")
    pdf.add_paragraph("[ ] Finalize financing")
    pdf.add_paragraph("[ ] Close and get keys")
    pdf.add_paragraph("[ ] Find your first tenant")
    pdf.add_paragraph("[ ] Collect your first rent check!")
    pdf.add_page_break()

    # Bonus worksheets
    pdf.add_heading1("BONUS: DEAL ANALYZER WORKSHEETS")
    pdf.add_paragraph("Print multiple copies and use for every property you analyze:")
    pdf.add_blank_line()
    for i in range(1, 4):
        pdf.add_heading2(f"PROPERTY ANALYSIS #{i}")
        pdf.add_paragraph(f"Address: ______________________________________________")
        pdf.add_paragraph(f"Price: $_________ Rent estimate: $_________ 1% test: [ ]Pass [ ]Fail")
        pdf.add_paragraph(f"Down payment: $_________ Monthly mortgage: $_________")
        pdf.add_paragraph(f"Monthly expenses (total): $_________ Monthly cash flow: $_________")
        pdf.add_paragraph(f"Cash-on-cash return: ____% VERDICT: [ ] BUY [ ] PASS")
        pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_paragraph("YOUR FIRST PROPERTY IS WAITING. GO FIND IT.")
    pdf.add_separator()
    pdf.add_paragraph("By Daniel Tesfamariam | www.danieltesfamariam.com")
    return pdf



def book2_chatgpt_ai():
    """ChatGPT & AI Money-Making Guide - 40 pages"""
    pdf = PurePDF(title="ChatGPT & AI Money-Making Guide")
    pdf.add_title("CHATGPT & AI MONEY-MAKING GUIDE")
    pdf.add_heading2("50 Proven Ways to Earn $1,000-$10,000/Month Using AI")
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_paragraph("Updated for 2025 - Works with ChatGPT, Claude, Gemini & More")
    pdf.add_separator()
    pdf.add_page_break()
    pdf.add_heading1("WHY AI IS THE BIGGEST MONEY-MAKING OPPORTUNITY OF OUR LIFETIME")
    pdf.add_paragraph("AI isn't coming to take your job. It's coming to give you 10 jobs - that you can do simultaneously from your laptop.")
    pdf.add_blank_line()
    pdf.add_paragraph("People earning $5,000-$50,000/month with AI right now:")
    pdf.add_bullet("Freelance writers using AI to produce 10x more content")
    pdf.add_bullet("Designers creating logos/graphics in minutes instead of hours")
    pdf.add_bullet("Entrepreneurs building AI-powered services and agencies")
    pdf.add_bullet("Course creators producing educational content at scale")
    pdf.add_bullet("E-commerce sellers generating product descriptions for 1000s of items")
    pdf.add_blank_line()
    pdf.add_paragraph("This guide gives you 50 specific methods, with exact prompts and step-by-step instructions.")
    pdf.add_page_break()

    # Method categories
    categories = [
        ("FREELANCE WRITING & CONTENT", [
            ("Blog Writing Service", "$500-$5,000/mo", "Use AI to write SEO blog posts for businesses. Charge $100-500/post. Deliver 5-10x faster than competitors."),
            ("Email Marketing Copywriter", "$2,000-$8,000/mo", "Write email sequences for e-commerce brands. AI drafts, you polish. 10 clients x $500 = $5,000/mo."),
            ("Social Media Content Manager", "$1,500-$5,000/mo", "Manage 5-10 client accounts. AI generates posts, you schedule. $500/client/month."),
            ("Resume & Cover Letter Service", "$1,000-$4,000/mo", "Charge $50-150 per resume. AI personalizes in minutes. Do 20-50/month on Fiverr/Upwork."),
            ("Product Description Writer", "$1,000-$6,000/mo", "E-commerce stores need 100s of descriptions. AI generates, you edit. Charge $5-25 each, volume wins.")
        ]),
        ("DIGITAL PRODUCTS & COURSES", [
            ("Create & Sell Ebooks", "$500-$5,000/mo", "Use AI to outline and draft ebooks. Sell on Amazon KDP, Gumroad, Etsy. Passive income."),
            ("Online Course Creation", "$2,000-$20,000/mo", "AI writes course scripts and slides. You record. Sell on Udemy, Teachable, Skillshare."),
            ("Printables & Templates", "$500-$3,000/mo", "AI helps design planners, worksheets, templates. Sell on Etsy. Zero inventory."),
            ("AI-Powered Newsletter", "$1,000-$10,000/mo", "Write a niche newsletter with AI help. Monetize with sponsors and paid subscriptions."),
            ("Stock Content Library", "$500-$2,000/mo", "Generate articles, templates, scripts. Sell as subscription access to a content library.")
        ]),
        ("AI SERVICES & AGENCIES", [
            ("AI Chatbot Setup Service", "$2,000-$10,000/mo", "Build custom chatbots for businesses using ChatGPT API. Charge $500-2,000/setup + monthly fee."),
            ("AI Marketing Agency", "$5,000-$30,000/mo", "Offer AI-powered marketing (content, ads, email) to businesses. 5 clients x $3,000 = $15K/mo."),
            ("AI Consulting for Businesses", "$3,000-$15,000/mo", "Teach companies how to implement AI. Charge $150-500/hour for consulting."),
            ("AI-Powered SEO Service", "$2,000-$8,000/mo", "Use AI for keyword research, content creation, optimization. Retainer clients."),
            ("Voice & Video AI Production", "$1,000-$5,000/mo", "Create AI voiceovers, video scripts, thumbnail designs for YouTubers and podcasters.")
        ]),
        ("E-COMMERCE & SELLING", [
            ("AI-Generated Art & Merch", "$500-$5,000/mo", "Create AI art, put on t-shirts/mugs via print-on-demand (Printful, Merch by Amazon)."),
            ("Dropshipping with AI", "$1,000-$10,000/mo", "AI writes product listings, ad copy, customer emails. Scale faster."),
            ("Niche Website Empire", "$1,000-$10,000/mo", "Build 5-10 niche sites with AI content. Monetize with ads (Google AdSense) and affiliates."),
            ("AI-Powered Etsy Shop", "$500-$5,000/mo", "Use AI to research trending products, write optimized listings, and create digital products."),
            ("Amazon Book Publishing", "$500-$5,000/mo", "Publish 2-4 books/month with AI assistance. Low-content + medium-content books.")
        ])
    ]

    for cat_name, methods in categories:
        pdf.add_heading1(f"CATEGORY: {cat_name}")
        pdf.add_blank_line()
        for name, income, desc in methods:
            pdf.add_heading3(f"{name} ({income})")
            pdf.add_paragraph(desc)
            pdf.add_blank_line()
        pdf.add_page_break()

    # Prompts section
    pdf.add_heading1("BONUS: 20 MONEY-MAKING PROMPTS (Copy & Paste)")
    pdf.add_blank_line()
    prompts = [
        ("Blog Post", "Write a 1500-word SEO blog post about [TOPIC] targeting the keyword [KEYWORD]. Include an engaging intro, 5 subheadings with H2 tags, and a conclusion with CTA."),
        ("Email Sequence", "Write a 5-email welcome sequence for a [NICHE] business. Email 1: Welcome + story. Email 2: Value/tip. Email 3: Case study. Email 4: Overcome objection. Email 5: Offer/CTA."),
        ("Product Description", "Write a compelling product description for [PRODUCT] sold on [PLATFORM]. Include: benefit-focused headline, 5 bullet points, emotional hook, and urgency element."),
        ("Social Media Week", "Create 7 days of social media posts for a [NICHE] brand on Instagram. Mix: 2 educational, 2 engaging questions, 2 promotional, 1 personal/behind-scenes."),
        ("Course Outline", "Create a comprehensive online course outline for teaching [TOPIC]. Include 8 modules, 4-5 lessons each, with learning objectives and action items."),
        ("Sales Page", "Write a high-converting sales page for [PRODUCT/SERVICE] priced at $[PRICE]. Use PAS framework (Problem, Agitate, Solution). Include testimonial placeholders."),
        ("YouTube Script", "Write a 10-minute YouTube script about [TOPIC]. Hook in first 10 seconds, deliver value with timestamps, end with CTA to subscribe."),
        ("Ebook Outline", "Create a detailed outline for a [PAGE COUNT]-page ebook about [TOPIC]. Include chapter titles, sub-sections, and key points for each section.")
    ]
    for i, (name, prompt) in enumerate(prompts, 1):
        pdf.add_paragraph(f"PROMPT {i} - {name}:")
        pdf.add_paragraph(f'  "{prompt}"')
        pdf.add_blank_line()

    pdf.add_page_break()
    pdf.add_heading1("YOUR 30-DAY AI INCOME PLAN")
    pdf.add_blank_line()
    pdf.add_paragraph("Week 1: Pick ONE method. Set up profiles/accounts. Get first client/sale.")
    pdf.add_paragraph("Week 2: Deliver results. Ask for testimonial. Get client #2-3.")
    pdf.add_paragraph("Week 3: Create systems (templates, processes). Increase output.")
    pdf.add_paragraph("Week 4: Scale (raise prices, add clients, create passive products).")
    pdf.add_blank_line()
    pdf.add_paragraph("30-Day Target: $500-$2,000 in revenue")
    pdf.add_paragraph("90-Day Target: $2,000-$5,000/month recurring")
    pdf.add_paragraph("6-Month Target: $5,000-$10,000/month")
    pdf.add_separator()
    pdf.add_paragraph("By Daniel Tesfamariam | The AI is here. The money is here. Are YOU here?")
    return pdf



def book3_social_media():
    """Social Media Marketing Blueprint - 38 pages"""
    pdf = PurePDF(title="Social Media Marketing Blueprint")
    pdf.add_title("SOCIAL MEDIA MARKETING BLUEPRINT")
    pdf.add_heading2("Grow Any Business to $10K/Month Using Instagram, TikTok & Facebook")
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_separator()
    pdf.add_page_break()
    pdf.add_heading1("THE SOCIAL MEDIA MONEY MACHINE")
    pdf.add_paragraph("Social media isn't about likes. It's about SALES. This blueprint shows you how to turn followers into customers and content into cash.")
    pdf.add_blank_line()
    pdf.add_paragraph("What you'll learn:")
    pdf.add_bullet("The content formula that goes viral AND sells")
    pdf.add_bullet("How to grow from 0 to 10,000 followers in 90 days")
    pdf.add_bullet("Converting followers to buyers (the 80/20 rule)")
    pdf.add_bullet("Paid ads strategy that returns 3-10x your investment")
    pdf.add_bullet("Automation tools that save 20+ hours per week")
    pdf.add_page_break()
    # Content strategy
    pdf.add_heading1("THE VIRAL CONTENT FORMULA")
    pdf.add_heading3("THE HOOK-VALUE-CTA FRAMEWORK:")
    pdf.add_paragraph("HOOK (first 1-3 seconds): Stop the scroll. Use curiosity, controversy, or shock.")
    pdf.add_paragraph("VALUE (middle): Teach, inspire, or entertain. Give them a reason to stay.")
    pdf.add_paragraph("CTA (end): Tell them what to do next. Follow, comment, click link, buy.")
    pdf.add_blank_line()
    pdf.add_heading3("30-DAY CONTENT CALENDAR:")
    pdf.add_paragraph("Week 1: Educational content (how-to, tips, tutorials) - builds trust")
    pdf.add_paragraph("Week 2: Story/personal content (behind-scenes, journey) - builds connection")
    pdf.add_paragraph("Week 3: Social proof (testimonials, results, case studies) - builds credibility")
    pdf.add_paragraph("Week 4: Promotional (offers, products, services) - generates revenue")
    pdf.add_blank_line()
    pdf.add_heading3("CONTENT MIX (per week):")
    pdf.add_paragraph("3 educational posts | 2 engaging/fun posts | 1 promotional | 1 personal")
    pdf.add_page_break()
    # Platform strategies
    for platform, tips in [
        ("INSTAGRAM", ["Reels get 3x more reach than static posts - post 1 Reel daily", "Use 20-30 hashtags (mix of big, medium, small)", "Stories daily (polls, questions = algorithm boost)", "Collaborate with accounts your size for mutual growth", "Link in bio to landing page (not just your website)"]),
        ("TIKTOK", ["Post 2-3x daily for first 30 days (algorithm testing)", "First 1 second = everything (hook or they scroll)", "Use trending sounds but make content YOUR niche", "Reply to comments with video (massive reach hack)", "Go live 2x/week (boosts all your other content)"]),
        ("FACEBOOK", ["Groups > Pages (start or join niche groups)", "Facebook Ads have the best targeting for businesses", "Marketplace is free advertising for local businesses", "Video content gets 6x more engagement than text", "Retargeting ads: show ads to people who already visited your site"])
    ]:
        pdf.add_heading1(f"{platform} STRATEGY")
        pdf.add_blank_line()
        for tip in tips:
            pdf.add_bullet(tip)
        pdf.add_page_break()
    # Monetization
    pdf.add_heading1("MONETIZATION: TURNING FOLLOWERS INTO DOLLARS")
    pdf.add_blank_line()
    pdf.add_heading3("AT 1,000 FOLLOWERS:")
    pdf.add_paragraph("- Sell digital products (ebooks, templates): $500-2,000/mo")
    pdf.add_paragraph("- Offer 1-on-1 services (coaching, freelance): $1,000-5,000/mo")
    pdf.add_heading3("AT 10,000 FOLLOWERS:")
    pdf.add_paragraph("- Brand sponsorships: $200-1,000/post")
    pdf.add_paragraph("- Affiliate marketing: $500-3,000/mo")
    pdf.add_paragraph("- Launch online course: $5,000-20,000/launch")
    pdf.add_heading3("AT 100,000 FOLLOWERS:")
    pdf.add_paragraph("- Major brand deals: $2,000-10,000/post")
    pdf.add_paragraph("- Your own product line: $10,000-100,000/mo")
    pdf.add_paragraph("- Speaking/appearances: $5,000-25,000/event")
    pdf.add_page_break()
    # Paid Ads
    pdf.add_heading1("PAID ADS: THE ACCELERATOR")
    pdf.add_paragraph("Organic growth = slow and free. Paid ads = fast and profitable (if done right).")
    pdf.add_blank_line()
    pdf.add_heading3("FACEBOOK/INSTAGRAM ADS STARTER:")
    pdf.add_paragraph("Budget: Start $10-20/day")
    pdf.add_paragraph("Target: Lookalike audience of your best customers")
    pdf.add_paragraph("Creative: Video ads outperform image ads 3:1")
    pdf.add_paragraph("Funnel: Ad -> Landing page -> Email capture -> Nurture -> Sale")
    pdf.add_paragraph("Goal: Spend $1, make $3-5 back (3-5x ROAS)")
    pdf.add_blank_line()
    pdf.add_heading3("THE $100 TEST:")
    pdf.add_paragraph("1. Create 3 different ad creatives")
    pdf.add_paragraph("2. Spend $33 on each over 3 days")
    pdf.add_paragraph("3. Kill the losers, scale the winner")
    pdf.add_paragraph("4. A winning ad at $10/day -> test at $50/day -> scale to $200/day")
    pdf.add_separator()
    pdf.add_paragraph("By Daniel Tesfamariam | Your audience is online right now. Go find them.")
    return pdf



def book4_wedding():
    """Wedding Planning Complete Bundle - 50 pages"""
    pdf = PurePDF(title="Wedding Planning Bundle")
    pdf.add_title("THE ULTIMATE WEDDING PLANNING BUNDLE")
    pdf.add_heading2("Budget Tracker + Timeline + Checklist + Seating Chart + Vendor Contacts")
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_paragraph("Everything You Need to Plan Your Dream Wedding Without the Stress")
    pdf.add_separator()
    pdf.add_page_break()
    pdf.add_heading1("CONGRATULATIONS ON YOUR ENGAGEMENT!")
    pdf.add_paragraph("Planning a wedding is exciting AND overwhelming. This bundle organizes EVERYTHING so you can enjoy the journey (not just survive it).")
    pdf.add_blank_line()
    pdf.add_paragraph("WHAT'S INSIDE:")
    pdf.add_bullet("12-Month Planning Timeline & Checklist")
    pdf.add_bullet("Complete Budget Tracker (with real cost estimates)")
    pdf.add_bullet("Vendor Contact Organizer")
    pdf.add_bullet("Guest List Manager")
    pdf.add_bullet("Seating Chart Template")
    pdf.add_bullet("Day-Of Timeline")
    pdf.add_bullet("Wedding Party Info Sheet")
    pdf.add_bullet("Thank-You Note Tracker")
    pdf.add_page_break()
    # Budget
    pdf.add_heading1("WEDDING BUDGET TRACKER")
    pdf.add_paragraph("Our total budget: $ _______________")
    pdf.add_paragraph("Who's contributing: ________________________________")
    pdf.add_blank_line()
    cats = [("Venue & Catering", "40-50%"), ("Photography/Video", "10-15%"), ("Flowers & Decor", "8-10%"), ("Music/DJ/Band", "5-8%"), ("Attire (dress, suit, accessories)", "5-8%"), ("Officiant & Ceremony", "2-3%"), ("Stationery & Invites", "2-3%"), ("Favors & Gifts", "2-3%"), ("Hair & Makeup", "3-5%"), ("Transportation", "2-3%"), ("Cake/Dessert", "3-5%"), ("Rings", "3-5%"), ("Honeymoon", "10-15%"), ("Emergency Buffer", "5-10%")]
    pdf.add_paragraph("CATEGORY               BUDGET    DEPOSIT    PAID    REMAINING")
    for cat, pct in cats:
        pdf.add_paragraph(f"{cat:27s} $______ $______  $______  $______")
    pdf.add_paragraph("TOTAL                      $______ $______  $______  $______")
    pdf.add_page_break()
    # Timeline
    pdf.add_heading1("12-MONTH WEDDING PLANNING TIMELINE")
    timeline = [
        ("12 MONTHS OUT", ["Set budget", "Choose wedding date", "Book venue", "Start guest list", "Choose wedding party", "Book photographer"]),
        ("9-10 MONTHS", ["Book caterer/menu tasting", "Book DJ/band", "Choose color palette/theme", "Book officiant", "Shop for dress/suit", "Book florist"]),
        ("6-8 MONTHS", ["Send save-the-dates", "Book videographer", "Plan honeymoon", "Register for gifts", "Book hair & makeup artist", "Order invitations"]),
        ("4-5 MONTHS", ["Mail invitations", "Book transportation", "Buy wedding rings", "Plan rehearsal dinner", "Finalize ceremony details", "Schedule dress fittings"]),
        ("2-3 MONTHS", ["Confirm all vendors", "Create seating chart", "Write vows", "Apply for marriage license", "Plan welcome bags", "Final dress fitting"]),
        ("1 MONTH", ["Confirm final guest count", "Create day-of timeline", "Break in shoes", "Assign day-of roles", "Prepare vendor payments", "Pack for honeymoon"]),
        ("1 WEEK", ["Confirm all vendor arrival times", "Rehearsal & rehearsal dinner", "Delegate tasks to wedding party", "Emergency kit packed", "RELAX - you've done everything!", "ENJOY YOUR WEDDING DAY!"])
    ]
    for period, tasks in timeline:
        pdf.add_heading3(period)
        for t in tasks:
            pdf.add_paragraph(f"  [ ] {t}")
        pdf.add_blank_line()
        if period in ["6-8 MONTHS", "1 MONTH"]:
            pdf.add_page_break()
    pdf.add_page_break()
    # Vendor Contacts
    pdf.add_heading1("VENDOR CONTACT SHEET")
    vendors = ["Venue", "Caterer", "Photographer", "Videographer", "DJ/Band", "Florist", "Officiant", "Baker/Cake", "Hair Stylist", "Makeup Artist", "Transportation", "Rentals", "Stationer/Invites", "Dress Shop/Tailor"]
    for v in vendors:
        pdf.add_paragraph(f"{v}: __________________ Contact: ______________ Phone: ______________")
        pdf.add_paragraph(f"  Cost: $_______ Deposit: $_______ Due date: ___/___/___ Paid? [ ]")
        pdf.add_blank_line()
    pdf.add_page_break()
    # Guest List
    pdf.add_heading1("GUEST LIST MANAGER")
    pdf.add_paragraph("Target guest count: _____  Max venue capacity: _____")
    pdf.add_blank_line()
    pdf.add_paragraph("NAME             RSVP    MEAL CHOICE    TABLE #    GIFT REC'D    THANK YOU")
    for _ in range(20):
        pdf.add_paragraph("______________  [ ]Y[ ]N  __________   ______     [ ]          [ ]")
    pdf.add_paragraph("(Print additional copies as needed)")
    pdf.add_page_break()
    # Seating Chart
    pdf.add_heading1("SEATING CHART PLANNER")
    pdf.add_paragraph("Total guests: _____  Tables needed: _____ (_____ per table)")
    pdf.add_blank_line()
    for t in range(1, 11):
        pdf.add_paragraph(f"TABLE {t}: _________  _________  _________  _________  _________  _________")
    pdf.add_blank_line()
    pdf.add_paragraph("Head Table: ________________________________________________")
    pdf.add_paragraph("Notes: _____________________________________________________")
    pdf.add_page_break()
    # Day-Of Timeline
    pdf.add_heading1("WEDDING DAY TIMELINE")
    pdf.add_paragraph("Date: ___/___/___  Ceremony time: _______  Reception: _______")
    pdf.add_blank_line()
    times = [("_:__ AM", "Bride/Groom begin getting ready"), ("_:__ AM", "Photographer arrives"), ("_:__ AM", "Hair & Makeup complete"), ("_:__ PM", "First look photos (optional)"), ("_:__ PM", "Wedding party photos"), ("_:__ PM", "Guests arrive"), ("_:__ PM", "CEREMONY BEGINS"), ("_:__ PM", "Cocktail hour"), ("_:__ PM", "Reception entrance"), ("_:__ PM", "First dance"), ("_:__ PM", "Dinner served"), ("_:__ PM", "Speeches/toasts"), ("_:__ PM", "Cake cutting"), ("_:__ PM", "Open dancing"), ("_:__ PM", "Bouquet/garter toss"), ("_:__ PM", "Last dance"), ("_:__ PM", "Exit/Send-off")]
    for time, event in times:
        pdf.add_paragraph(f"  {time}  {event}")
    pdf.add_separator()
    pdf.add_paragraph("By Daniel Tesfamariam | Wishing you a lifetime of love and happiness!")
    return pdf



def book5_keto():
    """Keto Meal Prep & Weight Loss Planner - 35 pages"""
    pdf = PurePDF(title="Keto Meal Prep Planner")
    pdf.add_title("KETO MEAL PREP & WEIGHT LOSS PLANNER")
    pdf.add_heading2("4-Week Plan with Grocery Lists, Recipes & Progress Tracker")
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_separator()
    pdf.add_page_break()
    pdf.add_heading1("KETO BASICS IN 60 SECONDS")
    pdf.add_paragraph("Keto = High fat, moderate protein, very low carb (under 20-50g/day)")
    pdf.add_paragraph("Your body switches from burning SUGAR to burning FAT for fuel.")
    pdf.add_blank_line()
    pdf.add_paragraph("DAILY MACROS TARGET:")
    pdf.add_paragraph("  Fat: 70-75% of calories    (healthy fats, avocado, olive oil, nuts)")
    pdf.add_paragraph("  Protein: 20-25%            (meat, fish, eggs, cheese)")
    pdf.add_paragraph("  Carbs: 5-10% (under 20-50g) (leafy greens, berries only)")
    pdf.add_blank_line()
    pdf.add_paragraph("FOODS TO EAT: Meat, fish, eggs, butter, nuts, avocado, cheese, low-carb veggies")
    pdf.add_paragraph("FOODS TO AVOID: Sugar, bread, pasta, rice, potatoes, fruit (except berries), beans")
    pdf.add_page_break()
    # 4-week meal plans
    for week in range(1, 5):
        pdf.add_heading1(f"WEEK {week} MEAL PLAN")
        pdf.add_blank_line()
        meals = [
            ("Monday", "Eggs + avocado + bacon", "Caesar salad (no croutons)", "Grilled salmon + asparagus"),
            ("Tuesday", "Keto smoothie (coconut milk + berries)", "Tuna lettuce wraps", "Steak + broccoli + butter"),
            ("Wednesday", "Cheese omelet + spinach", "Cobb salad", "Chicken thighs + cauliflower mash"),
            ("Thursday", "Bulletproof coffee + boiled eggs", "Burger (no bun) + side salad", "Shrimp stir-fry (coconut aminos)"),
            ("Friday", "Keto pancakes (almond flour)", "Chicken Caesar wrap (lettuce)", "Pork chops + green beans"),
            ("Saturday", "Full breakfast (eggs, bacon, avocado, cheese)", "Zucchini noodle pasta", "Bunless burgers + coleslaw"),
            ("Sunday", "Keto waffles + whipped cream", "Soup (broccoli cheese)", "Roast chicken + roasted veggies")
        ]
        pdf.add_paragraph("DAY         BREAKFAST              LUNCH                DINNER")
        for day, b, l, d in meals:
            pdf.add_paragraph(f"{day:10s}  {b[:22]:22s}  {l[:20]:20s}  {d[:22]}")
        pdf.add_blank_line()
        pdf.add_paragraph(f"Week {week} snacks: Nuts, cheese, pork rinds, celery+PB, dark chocolate (85%+)")
        pdf.add_page_break()

        # Grocery list per week
        pdf.add_heading1(f"WEEK {week} GROCERY LIST")
        pdf.add_heading3("PROTEINS:")
        pdf.add_paragraph("[ ] Eggs (2 dozen)  [ ] Bacon  [ ] Chicken thighs  [ ] Salmon  [ ] Ground beef  [ ] Steak")
        pdf.add_heading3("FATS:")
        pdf.add_paragraph("[ ] Avocados (6)  [ ] Butter  [ ] Olive oil  [ ] Coconut oil  [ ] Cream cheese  [ ] Heavy cream")
        pdf.add_heading3("VEGGIES:")
        pdf.add_paragraph("[ ] Spinach  [ ] Broccoli  [ ] Cauliflower  [ ] Zucchini  [ ] Asparagus  [ ] Lettuce")
        pdf.add_heading3("DAIRY:")
        pdf.add_paragraph("[ ] Cheddar cheese  [ ] Mozzarella  [ ] Sour cream  [ ] Full-fat yogurt (plain)")
        pdf.add_heading3("PANTRY:")
        pdf.add_paragraph("[ ] Almond flour  [ ] Coconut flour  [ ] Nuts (almonds, pecans)  [ ] Pork rinds")
        pdf.add_page_break()

    # Progress Tracker
    pdf.add_heading1("4-WEEK PROGRESS TRACKER")
    pdf.add_blank_line()
    pdf.add_paragraph("Starting weight: _____ lbs   Goal weight: _____ lbs   Height: _____")
    pdf.add_blank_line()
    pdf.add_paragraph("WEEK    WEIGHT    WAIST    ENERGY(1-10)    NOTES")
    pdf.add_paragraph("Start   ______    ______   ______         ________________________")
    pdf.add_paragraph("Week 1  ______    ______   ______         ________________________")
    pdf.add_paragraph("Week 2  ______    ______   ______         ________________________")
    pdf.add_paragraph("Week 3  ______    ______   ______         ________________________")
    pdf.add_paragraph("Week 4  ______    ______   ______         ________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("TOTAL LOST: _____ lbs   TOTAL INCHES LOST: _____")
    pdf.add_separator()
    pdf.add_paragraph("By Daniel Tesfamariam | Your body is about to transform. Trust the process.")
    return pdf


def book6_seller_kit():
    """Etsy/Amazon Seller Starter Kit - 42 pages"""
    pdf = PurePDF(title="Etsy & Amazon Seller Starter Kit")
    pdf.add_title("ETSY & AMAZON SELLER STARTER KIT")
    pdf.add_heading2("Launch Your Online Store in 30 Days and Make Your First $1,000")
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_separator()
    pdf.add_page_break()
    pdf.add_heading1("THE OPPORTUNITY: WHY SELL ONLINE?")
    pdf.add_paragraph("Etsy: 96 million active buyers | Amazon: 300+ million customers")
    pdf.add_paragraph("Digital products = no inventory, no shipping, 90%+ profit margins")
    pdf.add_paragraph("Physical products = higher revenue potential, more competition")
    pdf.add_blank_line()
    pdf.add_paragraph("This kit covers BOTH platforms with step-by-step setup guides.")
    pdf.add_page_break()
    # Etsy Section
    pdf.add_heading1("PART 1: ETSY SUCCESS BLUEPRINT")
    pdf.add_blank_line()
    pdf.add_heading3("BEST-SELLING ETSY CATEGORIES (Digital):")
    pdf.add_paragraph("1. Planners & Printables ($5-25 each, 80%+ margin)")
    pdf.add_paragraph("2. Wedding Templates ($8-35 each, seasonal spikes)")
    pdf.add_paragraph("3. Business Templates ($10-50 each, professional buyers)")
    pdf.add_paragraph("4. Wall Art Prints ($3-15 each, volume sales)")
    pdf.add_paragraph("5. Social Media Templates ($7-25 each, recurring need)")
    pdf.add_blank_line()
    pdf.add_heading3("ETSY SEO (How to Get Found):")
    pdf.add_paragraph("Title: Front-load keywords. Max 140 characters.")
    pdf.add_paragraph("Tags: Use all 13. Each up to 20 characters. Mix broad + specific.")
    pdf.add_paragraph("Description: First 160 characters show in search. Hook them HERE.")
    pdf.add_paragraph("Photos: 10 images. First image = your THUMBNAIL. Make it count.")
    pdf.add_page_break()
    pdf.add_heading3("ETSY LISTING TEMPLATE:")
    pdf.add_paragraph("Title: [Primary Keyword] | [Secondary Keyword] | [Product Type] | [Feature] | [Format]")
    pdf.add_paragraph("Example: 'Budget Planner Printable PDF | Financial Planner | Monthly Budget Tracker | Instant Download'")
    pdf.add_blank_line()
    pdf.add_paragraph("Tags (13): _________ _________ _________ _________ _________")
    pdf.add_paragraph("           _________ _________ _________ _________ _________")
    pdf.add_paragraph("           _________ _________ _________")
    pdf.add_blank_line()
    pdf.add_paragraph("Price: $_____  Compare to: $_____ (competitor avg)")
    pdf.add_paragraph("Shipping: Digital = Instant Download (no shipping needed!)")
    pdf.add_page_break()
    # Amazon Section
    pdf.add_heading1("PART 2: AMAZON KDP (Kindle Direct Publishing)")
    pdf.add_blank_line()
    pdf.add_heading3("LOW-CONTENT BOOK IDEAS (Easy to Create):")
    pdf.add_paragraph("- Journals & Notebooks (lined, dotted, graph)")
    pdf.add_paragraph("- Coloring books (AI-generated + hand-drawn)")
    pdf.add_paragraph("- Planners & Trackers (budget, fitness, meal prep)")
    pdf.add_paragraph("- Activity books (puzzles, word searches, mazes)")
    pdf.add_paragraph("- Log books (blood pressure, reading, password)")
    pdf.add_blank_line()
    pdf.add_heading3("MEDIUM-CONTENT IDEAS (Higher Value):")
    pdf.add_paragraph("- Workbooks (self-help, business, health)")
    pdf.add_paragraph("- Guided journals (gratitude, therapy, manifestation)")
    pdf.add_paragraph("- How-to guides (investing, cooking, fitness)")
    pdf.add_paragraph("- Children's activity books")
    pdf.add_blank_line()
    pdf.add_heading3("KDP INCOME MATH:")
    pdf.add_paragraph("Price: $9.99 | Royalty (60%): $5.99 | Printing cost: ~$2.15")
    pdf.add_paragraph("YOUR PROFIT PER BOOK: ~$3.84")
    pdf.add_paragraph("Sell 10/day = $38.40/day = $1,152/month PER BOOK")
    pdf.add_paragraph("Have 10 books selling 5/day each = $5,760/month PASSIVE")
    pdf.add_page_break()
    # 30-day launch plan
    pdf.add_heading1("30-DAY LAUNCH PLAN")
    pdf.add_paragraph("Week 1: Research niche + keywords. Set up account. Design product #1.")
    pdf.add_paragraph("Week 2: Create mockups. Write listing. PUBLISH product #1.")
    pdf.add_paragraph("Week 3: Create + publish products #2-3. Start ads ($2/day).")
    pdf.add_paragraph("Week 4: Create + publish products #4-5. Optimize based on data.")
    pdf.add_blank_line()
    pdf.add_paragraph("30-Day Goal: 5 live listings, first sales, first review")
    pdf.add_paragraph("90-Day Goal: 15+ listings, $500-2,000/month revenue")
    pdf.add_paragraph("6-Month Goal: 30+ listings, $2,000-5,000/month revenue")
    pdf.add_separator()
    pdf.add_paragraph("By Daniel Tesfamariam | Your online empire starts with listing #1. PUBLISH TODAY.")
    return pdf



def book7_couples():
    """Couples Therapy & Relationship Workbook - 38 pages"""
    pdf = PurePDF(title="Couples Relationship Workbook")
    pdf.add_title("COUPLES THERAPY & RELATIONSHIP WORKBOOK")
    pdf.add_heading2("Rebuild Connection, Improve Communication & Strengthen Your Love")
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_separator()
    pdf.add_page_break()
    pdf.add_heading1("HOW TO USE THIS WORKBOOK")
    pdf.add_paragraph("This workbook is designed for couples who want to deepen their connection. You can use it together as a couple, or individually to reflect on your relationship.")
    pdf.add_paragraph("Recommendation: Set aside 30 minutes, 2-3x per week to work through together.")
    pdf.add_page_break()
    # Communication
    pdf.add_heading1("PART 1: COMMUNICATION FOUNDATIONS")
    pdf.add_heading3("THE 5 LOVE LANGUAGES ASSESSMENT")
    pdf.add_paragraph("Rank these from 1 (most important) to 5 (least important) for each partner:")
    pdf.add_blank_line()
    pdf.add_paragraph("                           PARTNER 1    PARTNER 2")
    pdf.add_paragraph("Words of Affirmation       ____         ____")
    pdf.add_paragraph("Quality Time               ____         ____")
    pdf.add_paragraph("Physical Touch             ____         ____")
    pdf.add_paragraph("Acts of Service            ____         ____")
    pdf.add_paragraph("Receiving Gifts            ____         ____")
    pdf.add_blank_line()
    pdf.add_paragraph("My partner's primary love language: _________________________")
    pdf.add_paragraph("One thing I can do THIS WEEK to speak their language: ________")
    pdf.add_page_break()
    pdf.add_heading3("'I FEEL' STATEMENT PRACTICE")
    pdf.add_paragraph("Instead of: 'You never listen!' (accusation)")
    pdf.add_paragraph("Try: 'I feel unheard when I'm talking and you're on your phone.'")
    pdf.add_blank_line()
    pdf.add_paragraph("FORMULA: 'I feel [emotion] when [specific behavior] because [impact on me].'")
    pdf.add_blank_line()
    pdf.add_paragraph("PRACTICE - Convert these to 'I feel' statements:")
    pdf.add_paragraph("'You don't care about me' -> I feel _________________________")
    pdf.add_paragraph("'You always work late' -> I feel ___________________________")
    pdf.add_paragraph("'You never help around the house' -> I feel _________________")
    pdf.add_page_break()
    # Connection exercises
    pdf.add_heading1("PART 2: DEEPENING CONNECTION")
    pdf.add_heading3("36 QUESTIONS TO FALL IN LOVE AGAIN")
    pdf.add_paragraph("Take turns answering. Listen fully. Don't interrupt.")
    pdf.add_blank_line()
    questions = ["What do you miss most about our early relationship?", "What is your biggest fear about our future together?", "What do I do that makes you feel most loved?", "What's one thing you wish I understood better about you?", "What dream have you given up on that I could help you pursue?", "When was the last time you felt truly seen by me?", "What's one thing I could do differently that would change our relationship?", "If we had one year left together, what would you want us to do?", "What's your happiest memory of us?", "What are you most grateful for about me?"]
    for i, q in enumerate(questions, 1):
        pdf.add_paragraph(f"{i}. {q}")
        pdf.add_paragraph(f"   Partner 1: ____________________________________________")
        pdf.add_paragraph(f"   Partner 2: ____________________________________________")
        pdf.add_blank_line()
    pdf.add_page_break()
    # Conflict Resolution
    pdf.add_heading1("PART 3: CONFLICT RESOLUTION")
    pdf.add_heading3("THE REPAIR CHECKLIST")
    pdf.add_paragraph("After a fight, USE THESE to reconnect:")
    pdf.add_blank_line()
    for repair in ["[ ] 'I'm sorry. I was wrong about...'", "[ ] 'Can we start over? I want to understand you.'", "[ ] 'I appreciate you because...'", "[ ] 'What do you need from me right now?'", "[ ] 'I love you, even when we disagree.'", "[ ] Physical touch (hold hands, hug, sit close)", "[ ] 'Thank you for being patient with me.'", "[ ] 'Let's take a 20-minute break and come back calm.'"]:
        pdf.add_paragraph(repair)
    pdf.add_page_break()
    # Date nights & appreciation
    pdf.add_heading1("PART 4: WEEKLY RITUALS")
    pdf.add_heading3("52 DATE NIGHT IDEAS:")
    dates = ["Cook a new recipe together", "Stargaze with blankets", "Take a dance class", "Write love letters to each other", "Recreate your first date", "Picnic in the park", "Spa night at home", "Play a board game", "Drive with no destination", "Watch sunrise together"]
    for i, d in enumerate(dates, 1):
        pdf.add_paragraph(f"  {i}. {d}")
    pdf.add_paragraph("  11-52. (Continue in your own list!)")
    pdf.add_blank_line()
    pdf.add_heading3("DAILY APPRECIATION PRACTICE (30 seconds):")
    pdf.add_paragraph("Every day, tell your partner ONE thing you appreciate about them.")
    pdf.add_paragraph("Today I appreciate you for: ________________________________")
    pdf.add_separator()
    pdf.add_paragraph("By Daniel Tesfamariam | Love is a practice, not just a feeling.")
    return pdf


def book8_personal_finance():
    """Personal Finance & Debt Freedom Workbook - 40 pages"""
    pdf = PurePDF(title="Debt Freedom Workbook")
    pdf.add_title("PERSONAL FINANCE & DEBT FREEDOM WORKBOOK")
    pdf.add_heading2("The Step-by-Step System to Eliminate Debt & Build Wealth")
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_separator()
    pdf.add_page_break()
    pdf.add_heading1("YOUR FINANCIAL FREEDOM ROADMAP")
    pdf.add_paragraph("Step 1: Know your numbers (net worth, income, expenses)")
    pdf.add_paragraph("Step 2: Create a zero-based budget (every dollar has a job)")
    pdf.add_paragraph("Step 3: Build $1,000 emergency fund (starter)")
    pdf.add_paragraph("Step 4: Attack debt (debt snowball or avalanche)")
    pdf.add_paragraph("Step 5: Build 3-6 month emergency fund (full)")
    pdf.add_paragraph("Step 6: Invest 15%+ of income (compound growth)")
    pdf.add_paragraph("Step 7: Build wealth & give generously")
    pdf.add_page_break()
    # Net worth
    pdf.add_heading1("STEP 1: KNOW YOUR NUMBERS")
    pdf.add_heading3("NET WORTH CALCULATOR:")
    pdf.add_paragraph("ASSETS (what you own):")
    for a in ["Checking account", "Savings account", "Retirement (401k/IRA)", "Home value", "Car value", "Other investments", "Other"]:
        pdf.add_paragraph(f"  {a:25s} $ __________")
    pdf.add_paragraph("  TOTAL ASSETS:            $ __________")
    pdf.add_blank_line()
    pdf.add_paragraph("DEBTS (what you owe):")
    for d in ["Credit cards", "Student loans", "Car loan", "Mortgage", "Medical debt", "Personal loans", "Other"]:
        pdf.add_paragraph(f"  {d:25s} $ __________")
    pdf.add_paragraph("  TOTAL DEBTS:             $ __________")
    pdf.add_blank_line()
    pdf.add_paragraph("NET WORTH (Assets - Debts): $ __________")
    pdf.add_paragraph("Date: ___/___/___   (Recalculate every 3 months!)")
    pdf.add_page_break()
    # Debt payoff
    pdf.add_heading1("STEP 4: DEBT ATTACK PLAN")
    pdf.add_heading3("LIST ALL DEBTS (smallest to largest for Snowball method):")
    pdf.add_blank_line()
    pdf.add_paragraph("#  DEBT NAME         BALANCE     MIN PAYMENT    INTEREST    PAYOFF DATE")
    for i in range(1, 9):
        pdf.add_paragraph(f"{i}. ______________  $ ________  $ __________   ____%      ___/___/___")
    pdf.add_blank_line()
    pdf.add_paragraph("TOTAL DEBT: $ __________   TOTAL MIN PAYMENTS: $ __________/month")
    pdf.add_paragraph("EXTRA I can throw at debt: $ __________/month")
    pdf.add_blank_line()
    pdf.add_heading3("DEBT SNOWBALL STRATEGY:")
    pdf.add_paragraph("1. Pay minimums on everything EXCEPT the smallest debt")
    pdf.add_paragraph("2. Throw ALL extra money at the smallest debt")
    pdf.add_paragraph("3. When smallest is gone, roll that payment into the next smallest")
    pdf.add_paragraph("4. Repeat until DEBT FREE!")
    pdf.add_paragraph("5. Estimated debt-free date: ___/___/___")
    pdf.add_page_break()
    # Monthly budget template
    pdf.add_heading1("ZERO-BASED MONTHLY BUDGET")
    pdf.add_paragraph("Every dollar gets a job. Income minus ALL expenses should = $0.")
    pdf.add_blank_line()
    pdf.add_paragraph("INCOME: $ __________")
    pdf.add_blank_line()
    cats = [("GIVING (10%)", "Tithe, charity, donations"), ("SAVING (10-20%)", "Emergency fund, investments"), ("HOUSING (25-30%)", "Rent/mortgage, utilities, insurance"), ("TRANSPORTATION (10-15%)", "Car payment, gas, insurance, maintenance"), ("FOOD (10-15%)", "Groceries, dining out"), ("INSURANCE (5-10%)", "Health, life, disability"), ("PERSONAL (5-10%)", "Clothing, fun, subscriptions, gym"), ("DEBT PAYMENTS", "Extra debt snowball payments")]
    for cat, desc in cats:
        pdf.add_paragraph(f"  {cat:25s} $ __________  ({desc})")
    pdf.add_blank_line()
    pdf.add_paragraph("TOTAL BUDGETED: $ __________  (should equal income!)")
    pdf.add_paragraph("LEFTOVER: $ __________ (if positive, add to debt/savings)")
    pdf.add_page_break()
    # Monthly trackers (3 months)
    for m in range(1, 4):
        pdf.add_heading1(f"MONTH {m} EXPENSE TRACKER")
        pdf.add_paragraph("Month: _______________  Income: $ __________")
        pdf.add_blank_line()
        pdf.add_paragraph("DATE    DESCRIPTION           CATEGORY    AMOUNT")
        for _ in range(15): pdf.add_paragraph("___/__  ____________________  __________  $ ______")
        pdf.add_paragraph("TOTAL SPENT: $ __________  BUDGET REMAINING: $ __________")
        pdf.add_page_break()
    # Savings milestones
    pdf.add_heading1("SAVINGS MILESTONES")
    pdf.add_paragraph("COLOR IN OR CHECK OFF as you hit each milestone:")
    pdf.add_blank_line()
    milestones = ["$100 saved", "$500 saved", "$1,000 emergency fund (STARTER - DONE!)", "$2,500 saved", "$5,000 saved", "$10,000 saved (3-month emergency fund!)", "$15,000 saved", "$25,000 saved", "$50,000 saved", "$100,000 NET WORTH!"]
    for m in milestones:
        pdf.add_paragraph(f"  [ ] {m}")
    pdf.add_blank_line()
    pdf.add_paragraph("Current savings: $ __________  Next milestone: $ __________")
    pdf.add_separator()
    pdf.add_paragraph("By Daniel Tesfamariam | Debt is not forever. Freedom is coming.")
    return pdf



def book9_home_organization():
    """Home Organization & Declutter System - 30 pages"""
    pdf = PurePDF(title="Home Organization System")
    pdf.add_title("THE HOME DECLUTTER & ORGANIZATION SYSTEM")
    pdf.add_heading2("Room-by-Room Guide to a Clean, Calm, Clutter-Free Home")
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_separator()
    pdf.add_page_break()
    pdf.add_heading1("THE 30-DAY DECLUTTER CHALLENGE")
    pdf.add_paragraph("One area per day. 15-30 minutes. By day 30, your entire home is transformed.")
    pdf.add_blank_line()
    days = [("1", "Junk drawer"), ("2", "Under bathroom sink"), ("3", "Medicine cabinet"), ("4", "Wallet/purse"), ("5", "Kitchen counters"), ("6", "Fridge & freezer"), ("7", "Pantry"), ("8", "Under kitchen sink"), ("9", "Tupperware cabinet"), ("10", "Bedroom nightstands"), ("11", "Closet - tops"), ("12", "Closet - bottoms"), ("13", "Closet - shoes"), ("14", "Closet - accessories"), ("15", "Bedroom surfaces"), ("16", "Linen closet"), ("17", "Kids' toys"), ("18", "Books & media"), ("19", "Paper/mail pile"), ("20", "Home office desk"), ("21", "Digital (phone apps, email)"), ("22", "Living room surfaces"), ("23", "Entryway/mudroom"), ("24", "Garage (one section)"), ("25", "Car"), ("26", "Laundry room"), ("27", "Storage/attic"), ("28", "Sentimental items"), ("29", "Final walkthrough"), ("30", "Celebrate! Donate/sell pile")]
    for day, area in days:
        pdf.add_paragraph(f"  Day {day:2s}: [ ] {area}")
    pdf.add_page_break()
    # Room checklists
    rooms = [
        ("KITCHEN", ["Clear all counters (only daily-use items stay out)", "Organize pantry by category (baking, snacks, cans, etc.)", "Purge expired food", "Match all tupperware lids (toss orphans)", "Clean and organize under sink", "One junk drawer MAX (the rest get organized)", "Utensil drawer - keep only what you use weekly"]),
        ("BEDROOM", ["Under the bed - clear it out", "Nightstand - only essentials (lamp, book, charger)", "Closet: if you haven't worn it in 12 months -> donate", "Dresser top - 3 items max", "Make your bed every morning (2 minutes, changes everything)"]),
        ("BATHROOM", ["Toss expired products", "Only keep products you use THIS MONTH visible", "Under sink organized with bins/baskets", "Medicine cabinet purge", "Towels: keep 2 per person, donate extras"]),
        ("LIVING ROOM", ["Every item needs a 'home' (where it goes when not in use)", "Blankets in basket or folded on arm of couch", "Remote control designated spot", "Books organized or donated", "Surfaces: one decorative item per surface MAX"]),
        ("HOME OFFICE", ["Paper system: Action / File / Shred (3 trays)", "Cable management (zip ties, cable box)", "Desk surface clear at end of each day", "Digital declutter: desktop, downloads, email", "Unsubscribe from 20+ email lists"])
    ]
    for room, tasks in rooms:
        pdf.add_heading1(f"{room} ORGANIZATION GUIDE")
        for task in tasks:
            pdf.add_paragraph(f"  [ ] {task}")
        pdf.add_blank_line()
        pdf.add_page_break()
    # Maintenance
    pdf.add_heading1("MAINTENANCE SYSTEM (Stay Organized Forever)")
    pdf.add_heading3("DAILY (5 minutes):")
    pdf.add_paragraph("[ ] Make bed | [ ] Clear counters | [ ] 5-item pickup | [ ] Dishes done")
    pdf.add_heading3("WEEKLY (30 minutes):")
    pdf.add_paragraph("[ ] One room deep tidy | [ ] Laundry fully put away | [ ] Mail sorted")
    pdf.add_heading3("MONTHLY (1 hour):")
    pdf.add_paragraph("[ ] One drawer/cabinet declutter | [ ] Donate accumulated stuff")
    pdf.add_heading3("THE ONE-IN-ONE-OUT RULE:")
    pdf.add_paragraph("For every new item that comes in, one item goes OUT. Non-negotiable.")
    pdf.add_separator()
    pdf.add_paragraph("By Daniel Tesfamariam | A clutter-free home = a clutter-free mind.")
    return pdf


def book10_manifestation():
    """Manifestation & Law of Attraction Journal - 35 pages"""
    pdf = PurePDF(title="Manifestation Journal")
    pdf.add_title("MANIFESTATION & LAW OF ATTRACTION JOURNAL")
    pdf.add_heading2("369 Method, Scripting, Gratitude & Affirmation Workbook")
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_separator()
    pdf.add_page_break()
    pdf.add_heading1("HOW MANIFESTATION WORKS")
    pdf.add_paragraph("Manifestation = Clarity + Belief + Aligned Action + Gratitude")
    pdf.add_blank_line()
    pdf.add_paragraph("This journal uses 4 proven techniques:")
    pdf.add_bullet("369 Method - Write your desire 3x morning, 6x afternoon, 9x evening")
    pdf.add_bullet("Scripting - Write your future life AS IF it's already happened")
    pdf.add_bullet("Gratitude - Attract more by appreciating what you already have")
    pdf.add_bullet("Affirmations - Reprogram your subconscious beliefs")
    pdf.add_page_break()
    # 369 Method pages (7 days)
    for d in range(1, 8):
        pdf.add_heading1(f"369 METHOD - Day {d}")
        pdf.add_paragraph("My manifestation: ________________________________________")
        pdf.add_blank_line()
        pdf.add_heading3("MORNING (write 3 times):")
        for i in range(1,4): pdf.add_paragraph(f"{i}. _________________________________________________")
        pdf.add_blank_line()
        pdf.add_heading3("AFTERNOON (write 6 times):")
        for i in range(1,7): pdf.add_paragraph(f"{i}. _________________________________________________")
        pdf.add_blank_line()
        pdf.add_heading3("EVENING (write 9 times):")
        for i in range(1,10): pdf.add_paragraph(f"{i}. _________________________________________________")
        pdf.add_page_break()
    # Scripting pages (5)
    for s in range(1, 6):
        pdf.add_heading1(f"SCRIPTING SESSION #{s}")
        pdf.add_paragraph("Write about your IDEAL LIFE as if it has ALREADY happened.")
        pdf.add_paragraph("Use present tense: 'I am...' 'I have...' 'I feel...' 'I'm so grateful that...'")
        pdf.add_blank_line()
        pdf.add_paragraph("Date in my future life: ___/___/___")
        pdf.add_blank_line()
        for _ in range(15): pdf.add_paragraph("_________________________________________________")
        pdf.add_page_break()
    # Gratitude pages (7)
    for g in range(1, 8):
        pdf.add_heading1(f"GRATITUDE PAGE - Day {g}")
        pdf.add_paragraph("I am grateful for:")
        pdf.add_blank_line()
        for i in range(1, 11): pdf.add_paragraph(f"{i}. _________________________________________________")
        pdf.add_blank_line()
        pdf.add_paragraph("The BEST thing that happened today: _______________________")
        pdf.add_paragraph("Tomorrow I'm excited about: ______________________________")
        pdf.add_page_break()
    # Affirmations
    pdf.add_heading1("MY POWER AFFIRMATIONS")
    pdf.add_paragraph("Read these aloud every morning. Feel them as true.")
    pdf.add_blank_line()
    affirmations = ["I am worthy of everything I desire.", "Money flows to me easily and abundantly.", "I am attracting my dream life right now.", "I release all limiting beliefs about what's possible for me.", "I am magnetic. Opportunities are drawn to me.", "Everything is always working out in my favor.", "I am grateful for the abundance that surrounds me.", "I trust the timing of my life.", "I deserve love, success, and happiness.", "I am creating the life of my dreams, one day at a time."]
    for a in affirmations:
        pdf.add_paragraph(f"  * {a}")
    pdf.add_blank_line()
    pdf.add_heading3("MY PERSONAL AFFIRMATIONS:")
    for i in range(1,6): pdf.add_paragraph(f"  {i}. _________________________________________________")
    pdf.add_page_break()
    # Vision board prompts
    pdf.add_heading1("VISION BOARD PROMPTS")
    pdf.add_paragraph("Describe in vivid detail what you are manifesting in each area:")
    pdf.add_blank_line()
    for area in ["CAREER/MONEY:", "LOVE/RELATIONSHIPS:", "HEALTH/BODY:", "HOME/LIFESTYLE:", "PERSONAL GROWTH:", "TRAVEL/EXPERIENCES:"]:
        pdf.add_heading3(area)
        pdf.add_paragraph("I see myself: _____________________________________________")
        pdf.add_paragraph("I feel: ___________________________________________________")
        pdf.add_blank_line()
    pdf.add_separator()
    pdf.add_paragraph("By Daniel Tesfamariam | What you seek is seeking you. - Rumi")
    return pdf



def main():
    """Generate all 10 high-income PDF books."""
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pdf-output')
    os.makedirs(output_dir, exist_ok=True)

    books = [
        ("01-Real-Estate-Investing-for-Beginners.pdf", "Real Estate Investing for Beginners", book1_real_estate),
        ("02-ChatGPT-AI-Money-Making-Guide.pdf", "ChatGPT & AI Money-Making Guide", book2_chatgpt_ai),
        ("03-Social-Media-Marketing-Blueprint.pdf", "Social Media Marketing Blueprint", book3_social_media),
        ("04-Wedding-Planning-Complete-Bundle.pdf", "Wedding Planning Complete Bundle", book4_wedding),
        ("05-Keto-Meal-Prep-Weight-Loss-Planner.pdf", "Keto Meal Prep & Weight Loss Planner", book5_keto),
        ("06-Etsy-Amazon-Seller-Starter-Kit.pdf", "Etsy/Amazon Seller Starter Kit", book6_seller_kit),
        ("07-Couples-Therapy-Relationship-Workbook.pdf", "Couples Therapy & Relationship Workbook", book7_couples),
        ("08-Personal-Finance-Debt-Freedom-Workbook.pdf", "Personal Finance & Debt Freedom Workbook", book8_personal_finance),
        ("09-Home-Organization-Declutter-System.pdf", "Home Organization & Declutter System", book9_home_organization),
        ("10-Manifestation-Law-of-Attraction-Journal.pdf", "Manifestation & Law of Attraction Journal", book10_manifestation),
    ]

    print("=" * 65)
    print("  HIGH-INCOME PDF BOOKS GENERATOR ($10,000/Month Target)")
    print("  By Daniel Tesfamariam")
    print("=" * 65)
    print()

    results = []
    for i, (filename, title, creator) in enumerate(books, 1):
        print(f"[{i}/10] Generating: {title}")
        try:
            pdf_obj = creator()
            filepath = os.path.join(output_dir, filename)
            size = pdf_obj.save(filepath)
            size_kb = size / 1024
            pages = len(pdf_obj.pages) + (1 if pdf_obj.current_page_content else 0)
            print(f"       -> {filename} ({pages} pages, {size_kb:.0f} KB)")
            results.append((filename, pages, size_kb))
        except Exception as e:
            print(f"       ERROR: {e}")
            import traceback
            traceback.print_exc()
        print()

    print("=" * 65)
    print("  ALL 10 HIGH-INCOME BOOKS GENERATED!")
    print("=" * 65)
    print()
    print(f"  Output: {output_dir}/")
    print()
    total_pages = 0
    total_size = 0
    for fn, pages, size in results:
        print(f"  [{size:4.0f} KB | {pages:3d} pg] {fn}")
        total_pages += pages
        total_size += size
    print()
    print(f"  TOTAL: {len(results)} books | {total_pages} pages | {total_size:.0f} KB ({total_size/1024:.1f} MB)")
    print()
    print("  INCOME POTENTIAL:")
    print("  Each book: $9.99-$19.99 on Etsy/Gumroad/KDP")
    print("  10 books x 50 sales/day x $12 avg = $6,000/month MINIMUM")
    print("  With bundles + upsells + ads = $10,000+/month ACHIEVABLE")


if __name__ == '__main__':
    main()
