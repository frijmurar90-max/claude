#!/usr/bin/env python3
"""
Generate all 10 ADHD Planner PDF Books
FocusFlow Prints by Daniel Tesfamariam
"""
import os
import sys

# Import PurePDF from existing generator
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'generate_pdfs.py')).read())


def create_book_1():
    """ADHD Budget Planner - 35 pages"""
    pdf = PurePDF(title="ADHD Budget Planner")
    pdf.add_title("ADHD BUDGET PLANNER")
    pdf.add_heading2("A Dopamine-Friendly Way to Manage Your Money")
    pdf.add_paragraph("By Daniel Tesfamariam | FocusFlow Prints")
    pdf.add_separator()
    pdf.add_paragraph("Designed for how your brain actually works.")
    pdf.add_paragraph("Not another system that makes you feel broken.")
    pdf.add_page_break()


    # Page 2 - Welcome
    pdf.add_heading1("HOW TO USE THIS PLANNER")
    pdf.add_paragraph("Hey there, beautiful brain.")
    pdf.add_paragraph("This planner was made for people who've tried every budgeting app, spreadsheet, and envelope system... and abandoned them all by Day 3.")
    pdf.add_blank_line()
    pdf.add_heading3("HERE ARE THE ONLY RULES:")
    pdf.add_bullet("Done beats perfect. A half-filled page is better than a blank one.")
    pdf.add_bullet("Use pencil. You'll change your mind. That's fine.")
    pdf.add_bullet("Only 5 spending categories. Seriously. Five. Not fifteen.")
    pdf.add_bullet("One line per day for tracking. That's it. One line.")
    pdf.add_bullet("Skip pages you don't need. There's no planner police.")
    pdf.add_bullet("Celebrate every tiny win. Paid a bill on time? CHAMPION.")
    pdf.add_blank_line()
    pdf.add_heading3("WHAT'S INSIDE:")
    pdf.add_bullet("Monthly Budget Overview ............ Pages 6-17")
    pdf.add_bullet("Weekly Spending Tracker ............ Pages 18-21")
    pdf.add_bullet("Bill Pay Command Center ............ Pages 22-23")
    pdf.add_bullet("Impulse Spending Tools ............. Pages 24-26")
    pdf.add_bullet("Savings & Debt Visual Trackers ..... Pages 27-30")
    pdf.add_bullet("Annual Overview & Reflection ....... Pages 31-35")
    pdf.add_page_break()

    # Page 3 - Money Snapshot
    pdf.add_heading1("MY MONEY SNAPSHOT")
    pdf.add_paragraph("Let's start with just THREE numbers. That's it. Three.")
    pdf.add_blank_line()
    pdf.add_heading3("MY MONTHLY INCOME (after taxes)")
    pdf.add_paragraph("$ ___________________________")
    pdf.add_paragraph("[ ] Steady paycheck  [ ] Variable/freelance  [ ] Multiple sources")
    pdf.add_blank_line()
    pdf.add_heading3("MY FIXED BILLS (total of all monthly bills)")
    pdf.add_paragraph("$ ___________________________")
    pdf.add_paragraph("(Rent + utilities + subscriptions + insurance + minimum debt payments)")
    pdf.add_blank_line()
    pdf.add_heading3("WHAT'S LEFT (Income minus Fixed Bills)")
    pdf.add_paragraph("$ ___________________________")
    pdf.add_paragraph("This is your 'choice money.' Let's make it work for you.")
    pdf.add_blank_line()
    pdf.add_paragraph("Not sure about the numbers? Guess. A rough guess is 1000% better than not starting.")
    pdf.add_page_break()


    # Page 4 - 5 Categories
    pdf.add_heading1("MY 5 SPENDING CATEGORIES")
    pdf.add_paragraph("Pick ONLY five. Fewer categories = less overwhelm = you'll actually track things.")
    pdf.add_blank_line()
    pdf.add_paragraph("1. _________________________________ (example: food & groceries)")
    pdf.add_paragraph("2. _________________________________ (example: transportation)")
    pdf.add_paragraph("3. _________________________________ (example: fun & entertainment)")
    pdf.add_paragraph("4. _________________________________ (example: personal & self-care)")
    pdf.add_paragraph("5. _________________________________ (example: everything else)")
    pdf.add_blank_line()
    pdf.add_heading3("CATEGORY IDEAS:")
    pdf.add_paragraph("Food/Groceries | Gas/Transport | Fun/Entertainment | Clothing")
    pdf.add_paragraph("Health/Medical | Pets | Gifts | Education | Fitness/Gym")
    pdf.add_paragraph("Personal Care | Coffee/Dining Out | Home Stuff | Subscriptions")
    pdf.add_page_break()

    # Page 5 - Financial Goals
    pdf.add_heading1("MY FINANCIAL GOALS")
    pdf.add_paragraph("Pick up to 3 things you're working toward. Big or small - all goals count.")
    pdf.add_blank_line()
    pdf.add_heading3("GOAL #1 (Short-term)")
    pdf.add_paragraph("Goal: _________________________________  Target: $ ________")
    pdf.add_paragraph("[  |  |  |  |  |  |  |  |  |  ] Color in as you save!")
    pdf.add_blank_line()
    pdf.add_heading3("GOAL #2 (Medium-term)")
    pdf.add_paragraph("Goal: _________________________________  Target: $ ________")
    pdf.add_paragraph("[  |  |  |  |  |  |  |  |  |  ] Color in as you save!")
    pdf.add_blank_line()
    pdf.add_heading3("GOAL #3 (Long-term dream!)")
    pdf.add_paragraph("Goal: _________________________________  Target: $ ________")
    pdf.add_paragraph("[  |  |  |  |  |  |  |  |  |  ] Color in as you save!")
    pdf.add_page_break()

    # Pages 6-17: Monthly Budget (12 months)
    quotes = [
        "Progress, not perfection.", "You showed up. That counts.",
        "Small steps still move you forward.", "Your best is enough.",
        "Money is a tool, not a measure of your worth.",
        "Every expert was once a beginner.", "You're doing better than you think.",
        "Consistency isn't about never missing - it's about always returning.",
        "Financial peace is possible for you.", "You deserve to feel calm about money.",
        "Almost there. Keep going.", "Look how far you've come."
    ]
    for i, quote in enumerate(quotes):
        pdf.add_heading1(f"MONTHLY BUDGET")
        pdf.add_paragraph(f'"{quote}"')
        pdf.add_blank_line()
        pdf.add_paragraph("MONTH: ___________________   YEAR: ________")
        pdf.add_blank_line()
        pdf.add_heading3("INCOME THIS MONTH")
        pdf.add_paragraph("Paycheck / Source 1:    $ __________")
        pdf.add_paragraph("Side income / Source 2: $ __________")
        pdf.add_paragraph("TOTAL INCOME:           $ __________")
        pdf.add_blank_line()
        pdf.add_heading3("FIXED BILLS (check off as paid!)")
        for bill in ["Rent/Mortgage", "Electricity/Gas", "Water", "Internet/Phone", "Insurance", "Subscriptions", "Debt payments", "_______________", "_______________"]:
            pdf.add_paragraph(f"[ ] {bill:20s}  $ __________")
        pdf.add_paragraph("TOTAL FIXED:            $ __________")
        pdf.add_blank_line()
        pdf.add_heading3("VARIABLE SPENDING (Your 5 Categories)")
        pdf.add_paragraph("Category          Budget      Actual      +/-")
        for j in range(1, 6):
            pdf.add_paragraph(f"{j}. ____________  $ ______  $ ______  $ ______")
        pdf.add_blank_line()
        pdf.add_paragraph("HOW DID I DO? [Over Budget -------- On Track -------- Surplus]")
        pdf.add_paragraph("One thing I'm proud of: ________________________________")
        pdf.add_page_break()


    # Pages 18-21: Weekly Spending Tracker (4 weeks)
    for w in range(1, 5):
        pdf.add_heading1(f"WEEKLY SPENDING TRACKER - Week {w}")
        pdf.add_paragraph("Week of: _____________ to _____________")
        pdf.add_paragraph("ONE LINE per day. What you spent on, how much, need or want.")
        pdf.add_blank_line()
        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
            pdf.add_paragraph(f"{day:12s} ________________________  $ ______  [ ]N [ ]W")
        pdf.add_blank_line()
        pdf.add_paragraph("WEEKLY TOTAL: $ ______")
        pdf.add_paragraph("'Wants' total: $ ______    'Needs' total: $ ______")
        pdf.add_blank_line()
        pdf.add_paragraph("VIBE CHECK: [ ] Great  [ ] Fine  [ ] Meh  [ ] Stressed  [ ] Frustrated")
        pdf.add_paragraph("One sentence about this week: _________________________________")
        pdf.add_page_break()

    # Pages 22-23: Bill Pay Command Center
    pdf.add_heading1("BILL PAY COMMAND CENTER")
    pdf.add_paragraph("Never miss a bill again. List them ALL here, then check them off.")
    pdf.add_blank_line()
    pdf.add_paragraph("BILL NAME          AMOUNT    DUE DATE    AUTO-PAY?   PAID")
    for _ in range(12):
        pdf.add_paragraph("_______________  $ ______  ___/month    [ ] Yes    [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]")
    pdf.add_paragraph("TOTAL MONTHLY BILLS: $ __________")
    pdf.add_page_break()

    pdf.add_heading1("BILL DUE DATE CALENDAR")
    pdf.add_paragraph("Write bill due dates on the calendar. See WHEN money leaves.")
    pdf.add_blank_line()
    pdf.add_paragraph("SUN    MON    TUE    WED    THU    FRI    SAT")
    for row in range(5):
        pdf.add_paragraph("____   ____   ____   ____   ____   ____   ____")
        pdf.add_blank_line()
    pdf.add_paragraph("COLOR CODE: Green=Auto-pay | Yellow=Manual pay | Red=Late fee risk")
    pdf.add_page_break()

    # Pages 24-26: Impulse Spending Tools
    pdf.add_heading1("THE 24-HOUR PAUSE")
    pdf.add_paragraph("You want to buy something. Let's just... pause for a second.")
    pdf.add_blank_line()
    pdf.add_paragraph("WHAT IS IT?  _______________________________________________")
    pdf.add_paragraph("HOW MUCH?    $ __________")
    pdf.add_paragraph("WHERE DID I SEE IT? [ ] Social media [ ] Email [ ] Store [ ] Ad")
    pdf.add_blank_line()
    pdf.add_heading3("THE PAUSE QUESTIONS:")
    pdf.add_paragraph("1. Do I need this, or do I want the FEELING of buying it?")
    pdf.add_paragraph("   [ ] Need it   [ ] Want the feeling   [ ] Not sure")
    pdf.add_paragraph("2. Will I remember this purchase in 2 weeks?")
    pdf.add_paragraph("   [ ] Yes       [ ] Probably not")
    pdf.add_paragraph("3. Can I afford this WITHOUT dipping into bill money?")
    pdf.add_paragraph("   [ ] Yes       [ ] No       [ ] Barely")
    pdf.add_paragraph("4. What triggered this urge?")
    pdf.add_paragraph("   Boredom | Stress | Sadness | Social media | Celebration | Habit")
    pdf.add_blank_line()
    pdf.add_paragraph("COME BACK TOMORROW:")
    pdf.add_paragraph("[ ] Still want it -> Buy it guilt-free!")
    pdf.add_paragraph("[ ] Forgot about it -> Saved money without trying!")
    pdf.add_paragraph("MONEY SAVED BY PAUSING: $ __________")
    pdf.add_page_break()


    pdf.add_heading1("IMPULSE SPENDING LOG")
    pdf.add_paragraph("No shame. Just awareness. Track impulses to find YOUR patterns.")
    pdf.add_blank_line()
    pdf.add_paragraph("DATE    ITEM                 COST      TRIGGER        REGRET?(1-5)")
    for _ in range(10):
        pdf.add_paragraph("____  __________________  $ ______  ____________   * * * * *")
    pdf.add_blank_line()
    pdf.add_paragraph("TOTAL IMPULSE SPENDING: $ __________")
    pdf.add_paragraph("My most common trigger: _________________________")
    pdf.add_paragraph("Time of day I'm most vulnerable: ________________")
    pdf.add_page_break()

    pdf.add_heading1("MY DOPAMINE MENU")
    pdf.add_paragraph("When you feel the urge to spend, grab a hit from this menu instead.")
    pdf.add_paragraph("Your brain wants dopamine - not stuff.")
    pdf.add_blank_line()
    pdf.add_heading3("FREE DOPAMINE:")
    for item in ["Take a walk outside", "Call a friend", "Take a hot shower/bath", "Dance to 3 songs", "Reorganize one drawer", "Watch a comfort show", "Stretch for 10 minutes", "Play with a pet", "Journal for 5 minutes", "Make a playlist"]:
        pdf.add_paragraph(f"[ ] {item}")
    pdf.add_blank_line()
    pdf.add_heading3("CHEAP DOPAMINE (under $5):")
    for item in ["Fancy coffee/tea", "New lip balm or candle", "Rent a movie", "Bake something", "Fresh flowers", "Face mask", "New stickers or pens"]:
        pdf.add_paragraph(f"[ ] {item}")
    pdf.add_blank_line()
    pdf.add_heading3("MY PERSONAL DOPAMINE HITS:")
    for i in range(1, 6):
        pdf.add_paragraph(f"{i}. ________________________________________")
    pdf.add_page_break()

    # Pages 27-30: Savings & Debt Trackers
    for goal_num in range(1, 4):
        colors = ["Short-term", "Medium-term", "Long-term (dream!)"]
        pdf.add_heading1(f"SAVINGS GOAL TRACKER #{goal_num}")
        pdf.add_paragraph(f"Type: {colors[goal_num-1]}")
        pdf.add_blank_line()
        pdf.add_paragraph("MY GOAL: _____________________________________________")
        pdf.add_paragraph("TARGET AMOUNT: $ ________________")
        pdf.add_paragraph("WHY THIS MATTERS: ____________________________________")
        pdf.add_paragraph("START DATE: ___/___/___   TARGET DATE: ___/___/___")
        pdf.add_blank_line()
        pdf.add_paragraph("PROGRESS THERMOMETER (color in as you save!):")
        pdf.add_paragraph("  |==========| 100%  GOAL REACHED!")
        pdf.add_paragraph("  |==========| 90%")
        pdf.add_paragraph("  |========  | 80%")
        pdf.add_paragraph("  |=======   | 70%")
        pdf.add_paragraph("  |======    | 60%")
        pdf.add_paragraph("  |=====     | 50%  HALFWAY!")
        pdf.add_paragraph("  |====      | 40%")
        pdf.add_paragraph("  |===       | 30%")
        pdf.add_paragraph("  |==        | 20%")
        pdf.add_paragraph("  |=         | 10%")
        pdf.add_paragraph("  |          | START")
        pdf.add_blank_line()
        pdf.add_paragraph("DEPOSITS: Date:____ $____ | Date:____ $____ | Date:____ $____")
        pdf.add_page_break()

    pdf.add_heading1("DEBT PAYOFF TRACKER")
    pdf.add_paragraph("I'M PAYING OFF: _______________________________________")
    pdf.add_paragraph("TOTAL OWED: $ ____________   MINIMUM PAYMENT: $ ___________")
    pdf.add_paragraph("MY PAYMENT: $ _________ per [ ] week [ ] bi-weekly [ ] month")
    pdf.add_blank_line()
    pdf.add_paragraph("Cross off each circle as you make a payment:")
    for row in range(6):
        pdf.add_paragraph("  O  O  O  O  O  O  O  O  O  O")
    pdf.add_blank_line()
    pdf.add_paragraph("MILESTONES:")
    pdf.add_paragraph("[ ] 25% paid off! Treat: ______________")
    pdf.add_paragraph("[ ] 50% HALFWAY!  Treat: ______________")
    pdf.add_paragraph("[ ] 75% Almost!   Treat: ______________")
    pdf.add_paragraph("[ ] 100% DEBT FREE!!! BIG Treat: ______________")
    pdf.add_page_break()


    # Pages 31-35: Annual Overview & Reflection
    pdf.add_heading1("ANNUAL OVERVIEW")
    pdf.add_paragraph("Fill in at the end of each month. Partial data is still useful data!")
    pdf.add_blank_line()
    pdf.add_paragraph("MONTH          INCOME       EXPENSES     LEFTOVER")
    for month in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]:
        pdf.add_paragraph(f"{month:12s}  $ ________  $ ________  $ ________")
    pdf.add_paragraph("YEARLY TOTAL  $ ________  $ ________  $ ________")
    pdf.add_page_break()

    pdf.add_heading1("MY MONEY WINS")
    pdf.add_paragraph("Every win counts. EVERY. SINGLE. ONE. Write them all here.")
    pdf.add_blank_line()
    for i in range(15):
        pdf.add_paragraph(f"* _________________________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph('"You are not behind. You are not broken. You are building something new."')
    pdf.add_page_break()

    pdf.add_heading1("WHAT I LEARNED ABOUT MY ADHD & MONEY")
    pdf.add_blank_line()
    pdf.add_heading3('1. "My ADHD shows up in my finances by..."')
    for _ in range(4): pdf.add_paragraph("_________________________________________________")
    pdf.add_blank_line()
    pdf.add_heading3('2. "Something that actually WORKED for me was..."')
    for _ in range(4): pdf.add_paragraph("_________________________________________________")
    pdf.add_blank_line()
    pdf.add_heading3('3. "Next time, I want to try..."')
    for _ in range(4): pdf.add_paragraph("_________________________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("My biggest spending trigger: ____________________________")
    pdf.add_paragraph("What helps me stay on track: ____________________________")
    pdf.add_page_break()

    pdf.add_heading1("SIMPLE NET WORTH SNAPSHOT")
    pdf.add_heading3("WHAT I OWN (Assets):")
    for item in ["Checking account(s)", "Savings account(s)", "Retirement (401k/IRA)", "Other investments", "Car value", "Other"]:
        pdf.add_paragraph(f"  {item:25s} $ __________")
    pdf.add_paragraph("  TOTAL ASSETS:               $ __________")
    pdf.add_blank_line()
    pdf.add_heading3("WHAT I OWE (Debts):")
    for item in ["Credit card(s)", "Student loans", "Car loan", "Personal loan", "Medical debt", "Other"]:
        pdf.add_paragraph(f"  {item:25s} $ __________")
    pdf.add_paragraph("  TOTAL DEBTS:                $ __________")
    pdf.add_blank_line()
    pdf.add_paragraph("NET WORTH = Assets - Debts = $ __________")
    pdf.add_paragraph("DATE: ___/___/___   Check again in 6 months!")
    pdf.add_page_break()

    pdf.add_heading1("LOOKING AHEAD - NEXT YEAR'S FOCUS")
    pdf.add_paragraph("MY 3 FINANCIAL INTENTIONS:")
    pdf.add_blank_line()
    for i in range(1, 4):
        pdf.add_paragraph(f"{i}. ___________________________________________________")
        pdf.add_paragraph(f"   Why this matters: _________________________________")
        pdf.add_blank_line()
    pdf.add_paragraph("ONE HABIT I WANT TO BUILD: ________________________________")
    pdf.add_paragraph("ONE THING I'M LETTING GO OF: ______________________________")
    pdf.add_blank_line()
    pdf.add_heading3("A LETTER TO FUTURE ME:")
    for _ in range(5): pdf.add_paragraph("_________________________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("You showed up. You tried. That's everything.")
    pdf.add_paragraph("See you next year, beautiful brain.")
    pdf.add_separator()
    pdf.add_paragraph("Made with love by FocusFlow Prints | Daniel Tesfamariam")

    return pdf



def create_book_2():
    """ADHD Daily Routine Planner - 40 pages"""
    pdf = PurePDF(title="ADHD Daily Routine Planner")
    pdf.add_title("ADHD DAILY ROUTINE PLANNER")
    pdf.add_heading2("Time-Blocking for Neurodivergent Brains")
    pdf.add_paragraph("By Daniel Tesfamariam | FocusFlow Prints")
    pdf.add_separator()
    pdf.add_paragraph("Structure that flows WITH your energy, not against it.")
    pdf.add_page_break()

    # Welcome
    pdf.add_heading1("HOW THIS PLANNER WORKS")
    pdf.add_paragraph("Traditional schedules expect you to be a robot. You're not a robot.")
    pdf.add_paragraph("This planner uses ENERGY-BASED time blocking:")
    pdf.add_bullet("Schedule hard tasks when your brain is ON")
    pdf.add_bullet("Protect low-energy times for easy wins")
    pdf.add_bullet("Build in buffer time (because ADHD time blindness is real)")
    pdf.add_bullet("Only 3 priorities per day (not 20)")
    pdf.add_bullet("Grace gaps between blocks for transitions")
    pdf.add_page_break()

    # Energy Map
    pdf.add_heading1("MY ENERGY MAP")
    pdf.add_paragraph("When is your brain ON vs. OFF? Fill in honestly.")
    pdf.add_blank_line()
    pdf.add_paragraph("TIME            ENERGY LEVEL           BEST FOR")
    for time in ["6-8 AM", "8-10 AM", "10-12 PM", "12-2 PM", "2-4 PM", "4-6 PM", "6-8 PM", "8-10 PM", "10 PM+"]:
        pdf.add_paragraph(f"{time:12s}  [ ]High [ ]Med [ ]Low    _______________")
    pdf.add_blank_line()
    pdf.add_paragraph("MY PEAK HOURS: _________ to _________")
    pdf.add_paragraph("MY CRASH HOURS: _________ to _________")
    pdf.add_page_break()

    # Routine Building Blocks
    pdf.add_heading1("MY ROUTINE BUILDING BLOCKS")
    pdf.add_paragraph("Choose ANCHOR activities for each part of day. These are your non-negotiables.")
    pdf.add_blank_line()
    pdf.add_heading3("MORNING ANCHORS (pick 2-3):")
    for item in ["[ ] Wake up time: ____", "[ ] Medication", "[ ] Water/coffee", "[ ] Movement/stretch", "[ ] Shower", "[ ] Breakfast", "[ ] Check calendar", "[ ] ________________"]:
        pdf.add_paragraph(f"  {item}")
    pdf.add_blank_line()
    pdf.add_heading3("EVENING ANCHORS (pick 2-3):")
    for item in ["[ ] Dinner time: ____", "[ ] Screen off time: ____", "[ ] Tomorrow's prep", "[ ] Wind-down ritual", "[ ] Bedtime: ____", "[ ] ________________"]:
        pdf.add_paragraph(f"  {item}")
    pdf.add_page_break()

    # 20 Daily Pages
    for d in range(1, 21):
        pdf.add_heading1(f"DAILY PLAN")
        pdf.add_paragraph(f"Date: ___/___/___   Day of week: __________")
        pdf.add_paragraph(f"Energy forecast: [ ] High  [ ] Medium  [ ] Low  [ ] Unpredictable")
        pdf.add_blank_line()
        pdf.add_heading3("TOP 3 PRIORITIES (if I do NOTHING else):")
        pdf.add_paragraph("1. ____________________________________________ [ ] Done!")
        pdf.add_paragraph("2. ____________________________________________ [ ] Done!")
        pdf.add_paragraph("3. ____________________________________________ [ ] Done!")
        pdf.add_blank_line()
        pdf.add_heading3("TIME BLOCKS:")
        for block in ["Morning (____-____)", "Mid-morning (____-____)", "Afternoon (____-____)", "Late afternoon (____-____)", "Evening (____-____)"]:
            pdf.add_paragraph(f"  {block}: ________________________________")
        pdf.add_blank_line()
        pdf.add_heading3("BRAIN DUMP (get it out of your head):")
        for _ in range(3): pdf.add_paragraph("  _________________________________________________")
        pdf.add_blank_line()
        pdf.add_paragraph("End of day: [ ] Proud  [ ] Okay  [ ] Rough  [ ] Tomorrow is new")
        pdf.add_page_break()

    # Weekly Reviews (4)
    for w in range(1, 5):
        pdf.add_heading1(f"WEEKLY REVIEW - Week {w}")
        pdf.add_paragraph("What WORKED this week? _________________________________")
        pdf.add_paragraph("What DIDN'T work? _____________________________________")
        pdf.add_paragraph("What will I ADJUST? ____________________________________")
        pdf.add_paragraph("Am I over-scheduling? [ ] Yes (cut back!) [ ] No")
        pdf.add_paragraph("Energy pattern I noticed: ______________________________")
        pdf.add_paragraph("Next week's focus: ____________________________________")
        pdf.add_page_break()

    # Brain Dump Pages (5)
    for b in range(1, 6):
        pdf.add_heading1("BRAIN DUMP")
        pdf.add_paragraph("Get it ALL out. Tasks, ideas, worries, random thoughts. Empty your head.")
        pdf.add_blank_line()
        for _ in range(20): pdf.add_paragraph("_________________________________________________")
        pdf.add_page_break()

    # Routine Reset
    pdf.add_heading1("ROUTINE RESET GUIDE")
    pdf.add_paragraph("You fell off your routine. That's not failure - that's ADHD.")
    pdf.add_paragraph("Here's how to restart without shame:")
    pdf.add_blank_line()
    pdf.add_bullet("Step 1: Notice (you're doing this now - good job!)")
    pdf.add_bullet("Step 2: No guilt. Seriously. Skip the shame spiral.")
    pdf.add_bullet("Step 3: Pick ONE anchor habit to restart tomorrow")
    pdf.add_bullet("Step 4: Do the bare minimum version for 3 days")
    pdf.add_bullet("Step 5: Add one more thing when ready")
    pdf.add_blank_line()
    pdf.add_paragraph("My restart anchor habit: _________________________________")
    pdf.add_paragraph("Bare minimum version: ___________________________________")
    pdf.add_paragraph("When I'll restart: Tomorrow / ___/___/___")
    pdf.add_separator()
    pdf.add_paragraph("Made with love by FocusFlow Prints | Daniel Tesfamariam")

    return pdf



def create_book_3():
    """ADHD Habit Tracker Bundle - 25 pages"""
    pdf = PurePDF(title="ADHD Habit Tracker Bundle")
    pdf.add_title("ADHD HABIT TRACKER BUNDLE")
    pdf.add_heading2("Build Habits That Actually Stick (for Once)")
    pdf.add_paragraph("By Daniel Tesfamariam | FocusFlow Prints")
    pdf.add_separator()
    pdf.add_page_break()

    pdf.add_heading1("HABIT BUILDING FOR ADHD BRAINS")
    pdf.add_paragraph("Why traditional habit tracking fails us:")
    pdf.add_bullet("We pick too many habits at once (max 3-4!)")
    pdf.add_bullet("All-or-nothing thinking ('I missed one day, it's over')")
    pdf.add_bullet("No external rewards built in (dopamine needs!)")
    pdf.add_bullet("Boring visual trackers that lose novelty")
    pdf.add_blank_line()
    pdf.add_paragraph("THIS tracker fixes all of that. Three different styles (because variety!) and built-in rewards.")
    pdf.add_page_break()

    pdf.add_heading1("MY HABIT MENU - Choose 3-4 MAX")
    pdf.add_paragraph("Circle or check the habits you want to build:")
    pdf.add_blank_line()
    pdf.add_heading3("HEALTH:")
    pdf.add_paragraph("[ ] Drink water [ ] Take meds [ ] Move 10 min [ ] Sleep by ___ [ ] Eat a vegetable")
    pdf.add_heading3("PRODUCTIVITY:")
    pdf.add_paragraph("[ ] Make bed [ ] Plan tomorrow [ ] Top 3 tasks [ ] Time block [ ] Brain dump")
    pdf.add_heading3("SELF-CARE:")
    pdf.add_paragraph("[ ] Shower/hygiene [ ] Go outside [ ] Journal [ ] No phone 1hr [ ] Gratitude")
    pdf.add_heading3("CUSTOM:")
    pdf.add_paragraph("[ ] ______________ [ ] ______________ [ ] ______________")
    pdf.add_blank_line()
    pdf.add_paragraph("MY 3-4 CHOSEN HABITS:")
    for i in range(1,5): pdf.add_paragraph(f"{i}. _________________________________")
    pdf.add_page_break()

    # Style A: Grid Tracker (4 pages)
    for month in range(1, 5):
        pdf.add_heading1(f"30-DAY GRID TRACKER (Month {month})")
        pdf.add_paragraph("Month: _______________  Start date: ___/___/___")
        pdf.add_blank_line()
        pdf.add_paragraph("HABIT                    1  2  3  4  5  6  7  8  9  10 11 12 13 14 15")
        for i in range(1, 5):
            pdf.add_paragraph(f"______________  [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]")
        pdf.add_blank_line()
        pdf.add_paragraph("HABIT                    16 17 18 19 20 21 22 23 24 25 26 27 28 29 30")
        for i in range(1, 5):
            pdf.add_paragraph(f"______________  [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]")
        pdf.add_blank_line()
        pdf.add_paragraph("Completion rate: ___/30 days = ___%")
        pdf.add_paragraph("'Minimum viable' still counts! (Did 5 min instead of 30? COUNTS!)")
        pdf.add_page_break()

    # Style B: Circle/Dot Tracker (4 pages)
    for month in range(1, 5):
        pdf.add_heading1(f"30-DAY DOT TRACKER (Month {month})")
        pdf.add_paragraph("Color in each dot when you complete the habit. Watch them fill up!")
        pdf.add_blank_line()
        pdf.add_paragraph(f"Habit: ___________________________")
        pdf.add_paragraph("O O O O O O O O O O  (Days 1-10)")
        pdf.add_paragraph("O O O O O O O O O O  (Days 11-20)")
        pdf.add_paragraph("O O O O O O O O O O  (Days 21-30)")
        pdf.add_blank_line()
        pdf.add_paragraph(f"Habit: ___________________________")
        pdf.add_paragraph("O O O O O O O O O O  (Days 1-10)")
        pdf.add_paragraph("O O O O O O O O O O  (Days 11-20)")
        pdf.add_paragraph("O O O O O O O O O O  (Days 21-30)")
        pdf.add_blank_line()
        pdf.add_paragraph(f"Habit: ___________________________")
        pdf.add_paragraph("O O O O O O O O O O  (Days 1-10)")
        pdf.add_paragraph("O O O O O O O O O O  (Days 11-20)")
        pdf.add_paragraph("O O O O O O O O O O  (Days 21-30)")
        pdf.add_page_break()

    # Weekly Mini-Habits (4 pages)
    for w in range(1, 5):
        pdf.add_heading1(f"WEEKLY MINI-HABIT CHECK (Week {w})")
        pdf.add_paragraph("Just 7 days. You can do ANYTHING for 7 days.")
        pdf.add_blank_line()
        pdf.add_paragraph("Habit:           Mon  Tue  Wed  Thu  Fri  Sat  Sun")
        for i in range(1, 5):
            pdf.add_paragraph(f"_____________  [ ]  [ ]  [ ]  [ ]  [ ]  [ ]  [ ]")
        pdf.add_blank_line()
        pdf.add_paragraph("Days completed: ___/7")
        pdf.add_paragraph("How I feel about this week: ____________________________")
        pdf.add_page_break()

    # Habit Stacking + Rewards + Restart
    pdf.add_heading1("HABIT STACKING TEMPLATE")
    pdf.add_paragraph("Attach new habits to existing ones. Your brain already does the first part!")
    pdf.add_blank_line()
    pdf.add_paragraph("After I _________________ (existing habit),")
    pdf.add_paragraph("I will _________________ (new habit).")
    pdf.add_blank_line()
    pdf.add_paragraph("After I _________________ (existing habit),")
    pdf.add_paragraph("I will _________________ (new habit).")
    pdf.add_blank_line()
    pdf.add_paragraph("After I _________________ (existing habit),")
    pdf.add_paragraph("I will _________________ (new habit).")
    pdf.add_page_break()

    pdf.add_heading1("MY REWARD SYSTEM")
    pdf.add_paragraph("ADHD brains need external rewards. Plan them in advance!")
    pdf.add_blank_line()
    pdf.add_paragraph("7 days streak:  Reward: _________________________________")
    pdf.add_paragraph("14 days streak: Reward: _________________________________")
    pdf.add_paragraph("21 days streak: Reward: _________________________________")
    pdf.add_paragraph("30 days streak: BIG Reward: _____________________________")
    pdf.add_page_break()

    pdf.add_heading1("RESTART WITHOUT SHAME")
    pdf.add_paragraph("You missed days. That's literally what ADHD does. Here's what to do:")
    pdf.add_blank_line()
    pdf.add_bullet("Step 1: Notice (done - you're here!)")
    pdf.add_bullet("Step 2: Skip the guilt. It's not helpful.")
    pdf.add_bullet("Step 3: Ask: Is this habit still right for me? [ ] Yes [ ] No -> swap it")
    pdf.add_bullet("Step 4: Restart with the MINIMUM version tomorrow")
    pdf.add_bullet("Step 5: 3 days minimum version, then build up")
    pdf.add_blank_line()
    pdf.add_paragraph("Number of times I've restarted: _____ (this number = resilience, not failure)")
    pdf.add_separator()
    pdf.add_paragraph("Made with love by FocusFlow Prints | Daniel Tesfamariam")
    return pdf



def create_book_4():
    """ADHD Meal Planner & Grocery List - 30 pages"""
    pdf = PurePDF(title="ADHD Meal Planner")
    pdf.add_title("ADHD MEAL PLANNER & GROCERY LIST")
    pdf.add_heading2("Eat Well Without the Executive Dysfunction Meltdown")
    pdf.add_paragraph("By Daniel Tesfamariam | FocusFlow Prints")
    pdf.add_separator()
    pdf.add_page_break()

    pdf.add_heading1("MEAL PLANNING WITH ADHD")
    pdf.add_paragraph("The problem isn't that you can't cook. It's that deciding WHAT to cook uses up all your executive function before you even start.")
    pdf.add_blank_line()
    pdf.add_paragraph("This planner removes decisions:")
    pdf.add_bullet("Pre-made 'go-to meals' list (decide once, use forever)")
    pdf.add_bullet("'I Can't Decide' options when your brain is fried")
    pdf.add_bullet("Grocery list organized by STORE SECTION (not recipe)")
    pdf.add_bullet("Emergency meals for 'I have no plan' nights")
    pdf.add_bullet("Zero guilt about ordering takeout sometimes")
    pdf.add_page_break()

    # Go-To Meals
    pdf.add_heading1("MY GO-TO MEALS LIST")
    pdf.add_paragraph("Fill this in ONCE. These are meals you already know how to make (or assemble).")
    pdf.add_blank_line()
    pdf.add_heading3("BREAKFASTS (pick 5 easy ones):")
    for i in range(1,6): pdf.add_paragraph(f"{i}. ________________________________________")
    pdf.add_blank_line()
    pdf.add_heading3("LUNCHES (pick 7):")
    for i in range(1,8): pdf.add_paragraph(f"{i}. ________________________________________")
    pdf.add_blank_line()
    pdf.add_heading3("DINNERS (pick 7):")
    for i in range(1,8): pdf.add_paragraph(f"{i}. ________________________________________")
    pdf.add_blank_line()
    pdf.add_heading3("SNACKS (pick 5):")
    for i in range(1,6): pdf.add_paragraph(f"{i}. ________________________________________")
    pdf.add_page_break()

    # Weekly Meal Planners (8 weeks)
    for w in range(1, 9):
        pdf.add_heading1(f"WEEKLY MEAL PLAN - Week {w}")
        pdf.add_paragraph("Just pick from your go-to list. Don't overthink it.")
        pdf.add_blank_line()
        pdf.add_paragraph("DAY         BREAKFAST       LUNCH           DINNER")
        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
            pdf.add_paragraph(f"{day:10s}  ____________  ____________  ____________")
        pdf.add_blank_line()
        pdf.add_paragraph("Prep needed: _________________________________________")
        pdf.add_paragraph("Takeout budget this week: $ _______")
        pdf.add_page_break()

    # Grocery Lists (4)
    for g in range(1, 5):
        pdf.add_heading1(f"GROCERY LIST (organized by section)")
        pdf.add_paragraph("Week of: _______________")
        pdf.add_blank_line()
        for section in ["PRODUCE:", "DAIRY/EGGS:", "MEAT/PROTEIN:", "BREAD/BAKERY:", "FROZEN:", "PANTRY/CANNED:", "SNACKS:", "DRINKS:", "OTHER:"]:
            pdf.add_heading3(section)
            pdf.add_paragraph("[ ] ____________ [ ] ____________ [ ] ____________")
        pdf.add_page_break()

    # Freezer Inventory + Pantry
    pdf.add_heading1("FREEZER INVENTORY")
    pdf.add_paragraph("What's in your freezer? Update when you add/use things.")
    pdf.add_blank_line()
    pdf.add_paragraph("ITEM                    DATE FROZEN     USE BY")
    for _ in range(12): pdf.add_paragraph("___________________  ___/___/___   ___/___/___")
    pdf.add_page_break()

    pdf.add_heading1("PANTRY STAPLES CHECKLIST")
    pdf.add_paragraph("Circle what you're LOW on. Take a photo of this page before shopping.")
    pdf.add_blank_line()
    for cat, items in [("GRAINS:", "Rice | Pasta | Bread | Oats | Tortillas | Cereal"),
                       ("CANNED:", "Beans | Tomatoes | Soup | Tuna | Coconut milk"),
                       ("OILS/SAUCES:", "Olive oil | Soy sauce | Hot sauce | Ketchup | Mayo"),
                       ("SPICES:", "Salt | Pepper | Garlic | Italian | Chili | Cinnamon"),
                       ("BAKING:", "Flour | Sugar | Baking soda | Vanilla | Honey"),
                       ("SNACKS:", "Nuts | Crackers | Popcorn | Chips | Dried fruit")]:
        pdf.add_heading3(cat)
        pdf.add_paragraph(items)
    pdf.add_page_break()

    # Emergency Meals
    pdf.add_heading1("EMERGENCY MEAL IDEAS")
    pdf.add_paragraph("It's 7pm. You have no plan. No energy. These require MINIMAL effort:")
    pdf.add_blank_line()
    pdf.add_heading3("5-MINUTE MEALS:")
    for m in ["Cereal (yes, for dinner. No judgment.)", "Toast + peanut butter + banana", "Quesadilla (tortilla + cheese + microwave)", "Yogurt + granola + fruit", "Ramen + frozen veggies + egg"]:
        pdf.add_bullet(m)
    pdf.add_blank_line()
    pdf.add_heading3("10-MINUTE MEALS:")
    for m in ["Scrambled eggs + toast", "Pasta + jar sauce", "Rice + canned beans + salsa", "Grilled cheese + canned soup", "Frozen pizza (no shame!)"]:
        pdf.add_bullet(m)
    pdf.add_blank_line()
    pdf.add_paragraph("REMEMBER: Fed is best. A 'bad' meal is better than no meal.")
    pdf.add_separator()
    pdf.add_paragraph("Made with love by FocusFlow Prints | Daniel Tesfamariam")
    return pdf



def create_book_5():
    """ADHD Cleaning Schedule - 20 pages"""
    pdf = PurePDF(title="ADHD Cleaning Schedule")
    pdf.add_title("ADHD CLEANING SCHEDULE & CHECKLIST")
    pdf.add_heading2("A 'Good Enough Clean' System for Real Life")
    pdf.add_paragraph("By Daniel Tesfamariam | FocusFlow Prints")
    pdf.add_separator()
    pdf.add_page_break()

    pdf.add_heading1("CLEANING WITH ADHD (NOT AGAINST IT)")
    pdf.add_paragraph("Your home doesn't need to be Instagram-perfect. It needs to be LIVEABLE.")
    pdf.add_blank_line()
    pdf.add_paragraph("This system works because:")
    pdf.add_bullet("One room per day (not the whole house)")
    pdf.add_bullet("'Bare minimum' daily list = 5 minutes MAX")
    pdf.add_bullet("Sprint timers make it a game (ADHD loves games)")
    pdf.add_bullet("Checklists give dopamine hits (check! check! check!)")
    pdf.add_bullet("'Before guests' panic guide for emergencies")
    pdf.add_page_break()

    # Daily Bare Minimum
    pdf.add_heading1("DAILY BARE MINIMUM (5 minutes)")
    pdf.add_paragraph("Do these 5 things. ONLY these 5. Then you're done for the day.")
    pdf.add_blank_line()
    pdf.add_paragraph("[ ] 1. Dishes in dishwasher (or at least in the sink)")
    pdf.add_paragraph("[ ] 2. Wipe one counter")
    pdf.add_paragraph("[ ] 3. One load of laundry (start OR fold OR put away)")
    pdf.add_paragraph("[ ] 4. Pick up 5 things off the floor")
    pdf.add_paragraph("[ ] 5. Take out trash if full")
    pdf.add_blank_line()
    pdf.add_paragraph("THAT'S IT. You cleaned today. Gold star.")
    pdf.add_page_break()

    # Room Checklists
    for room, tasks in [
        ("KITCHEN", ["Dishes done", "Counters wiped", "Stove/microwave wiped", "Sweep floor", "Take out trash", "Wipe table", "Clean sink", "Check fridge for old food"]),
        ("BATHROOM", ["Toilet cleaned", "Sink/mirror wiped", "Shower sprayed", "Floor swept/mopped", "Trash emptied", "Towels swapped", "Refill soap/TP"]),
        ("BEDROOM", ["Bed made", "Clothes put away", "Nightstand cleared", "Floor cleared", "Dust surfaces", "Change sheets (weekly)"]),
        ("LIVING ROOM", ["Couch cushions fixed", "Surfaces cleared", "Floor picked up", "Vacuum/sweep", "Blankets folded", "Remote controls found"]),
        ("OFFICE/DESK", ["Desk surface cleared", "Papers filed or trashed", "Trash emptied", "Cords organized", "Dust monitor/keyboard", "Tomorrow's setup ready"]),
        ("LAUNDRY", ["Wash load", "Dry load", "Fold & sort", "Put away", "Check hampers", "Stain treatment"])
    ]:
        pdf.add_heading1(f"{room} CHECKLIST")
        pdf.add_blank_line()
        for task in tasks:
            pdf.add_paragraph(f"[ ] {task}")
        pdf.add_blank_line()
        pdf.add_paragraph("Time it took: ___ minutes  (probably less than you thought!)")
        pdf.add_page_break()

    # Weekly Schedule
    pdf.add_heading1("WEEKLY CLEANING SCHEDULE")
    pdf.add_paragraph("One focus area per day. You're not cleaning EVERYTHING every day.")
    pdf.add_blank_line()
    for day, room in [("Monday", "Kitchen"), ("Tuesday", "Bathroom"), ("Wednesday", "Bedroom"), ("Thursday", "Living Room"), ("Friday", "Floors (whole house)"), ("Saturday", "Laundry catch-up"), ("Sunday", "REST (or light tidy)")]:
        pdf.add_paragraph(f"{day:12s} -> {room}")
    pdf.add_blank_line()
    pdf.add_paragraph("Didn't do today's room? Move it to tomorrow. No guilt spiral allowed.")
    pdf.add_page_break()

    # Sprint Timer Cards
    pdf.add_heading1("5-MINUTE CLEANING SPRINTS")
    pdf.add_paragraph("Set a timer. Race yourself. Stop when it beeps. DONE.")
    pdf.add_blank_line()
    pdf.add_paragraph("SPRINT CHALLENGES (pick one, set timer, GO!):")
    for sprint in ["Clear & wipe all counters", "Pick up everything on the floor in one room", "Sort one junk drawer", "Wipe all mirrors/glass", "Fold one basket of laundry", "Clear off the dining table", "Organize under the sink", "Wipe all door handles & light switches", "Clear your car's front seat", "Organize one shelf"]:
        pdf.add_paragraph(f"[ ] {sprint}")
    pdf.add_blank_line()
    pdf.add_paragraph("Sprints completed this week: ___/7  (even 1 is great!)")
    pdf.add_page_break()

    # Before Guests
    pdf.add_heading1("BEFORE GUESTS ARRIVE - PANIC CLEAN")
    pdf.add_paragraph("Someone's coming over. Here's what to hit based on your time:")
    pdf.add_blank_line()
    pdf.add_heading3("15 MINUTES:")
    pdf.add_bullet("Clear surfaces they'll see (stuff goes in a 'hide box')")
    pdf.add_bullet("Wipe bathroom sink + toilet")
    pdf.add_bullet("Light a candle (covers a multitude of sins)")
    pdf.add_blank_line()
    pdf.add_heading3("30 MINUTES:")
    pdf.add_bullet("All of the above PLUS:")
    pdf.add_bullet("Quick vacuum main areas")
    pdf.add_bullet("Kitchen counters clear")
    pdf.add_bullet("Close bedroom doors")
    pdf.add_blank_line()
    pdf.add_heading3("60 MINUTES:")
    pdf.add_bullet("All of the above PLUS:")
    pdf.add_bullet("Mop kitchen/bathroom")
    pdf.add_bullet("Full bathroom clean")
    pdf.add_bullet("Fluff pillows & fold blankets")
    pdf.add_separator()
    pdf.add_paragraph("Made with love by FocusFlow Prints | Daniel Tesfamariam")
    return pdf



def create_book_6():
    """ADHD Goal Setting Workbook - 28 pages"""
    pdf = PurePDF(title="ADHD Goal Setting Workbook")
    pdf.add_title("ADHD GOAL SETTING WORKBOOK")
    pdf.add_heading2("Dream Big, Plan Small, Actually Follow Through")
    pdf.add_paragraph("By Daniel Tesfamariam | FocusFlow Prints")
    pdf.add_separator()
    pdf.add_page_break()

    pdf.add_heading1("WHY GOALS FEEL IMPOSSIBLE WITH ADHD")
    pdf.add_paragraph("It's not willpower. It's executive function + dopamine.")
    pdf.add_blank_line()
    pdf.add_paragraph("ADHD goal-setting challenges:")
    pdf.add_bullet("We set too many goals (shiny new goal syndrome)")
    pdf.add_bullet("We skip from 'idea' to 'done' without planning the middle")
    pdf.add_bullet("We lose interest once novelty wears off")
    pdf.add_bullet("We feel shame about 'failed' goals and stop trying")
    pdf.add_blank_line()
    pdf.add_paragraph("THIS workbook fixes these with:")
    pdf.add_bullet("Only 3 goals at a time (max!)")
    pdf.add_bullet("90-day sprints (not annual goals)")
    pdf.add_bullet("Built-in 'is this still interesting?' checks")
    pdf.add_bullet("Permission to pivot (goal funeral included)")
    pdf.add_bullet("Micro-steps focus (what's the TINIEST first action?)")
    pdf.add_page_break()

    # Dream Dump
    pdf.add_heading1("DREAM DUMP")
    pdf.add_paragraph("Write EVERYTHING you want. Big, small, silly, serious. No filter.")
    pdf.add_blank_line()
    for _ in range(20): pdf.add_paragraph("* _________________________________________________")
    pdf.add_page_break()

    pdf.add_heading1("DREAM DUMP (continued)")
    for _ in range(20): pdf.add_paragraph("* _________________________________________________")
    pdf.add_page_break()

    # Vision Board Prompts
    pdf.add_heading1("VISION BOARD PROMPTS")
    pdf.add_paragraph("For each life area, write what 'success' looks like to YOU:")
    pdf.add_blank_line()
    for area in ["HEALTH & BODY:", "MONEY & CAREER:", "RELATIONSHIPS:", "PERSONAL GROWTH:", "FUN & JOY:", "HOME & ENVIRONMENT:"]:
        pdf.add_heading3(area)
        pdf.add_paragraph("In 90 days, I want: ____________________________________")
        pdf.add_paragraph("This matters because: __________________________________")
        pdf.add_blank_line()
    pdf.add_page_break()

    # Goal Selection
    pdf.add_heading1("PICK YOUR 3 GOALS (max!)")
    pdf.add_paragraph("From your dream dump + vision, choose ONLY 3 for this 90-day sprint:")
    pdf.add_blank_line()
    for i in range(1, 4):
        pdf.add_heading3(f"GOAL {i}:")
        pdf.add_paragraph(f"What: ________________________________________________")
        pdf.add_paragraph(f"Why (emotional reason): _______________________________")
        pdf.add_paragraph(f"How I'll know it's done: ______________________________")
        pdf.add_blank_line()
    pdf.add_paragraph("The rest of your dreams aren't gone - they're waiting for next sprint.")
    pdf.add_page_break()

    # Goal Breakdown (2 pages per goal = 6 pages)
    for g in range(1, 4):
        pdf.add_heading1(f"GOAL {g} BREAKDOWN")
        pdf.add_paragraph(f"Goal: ________________________________________________")
        pdf.add_blank_line()
        pdf.add_heading3("MILESTONES (break it into 3-4 chunks):")
        for m in range(1, 5):
            pdf.add_paragraph(f"Milestone {m}: _______________________ By: ___/___/___")
        pdf.add_blank_line()
        pdf.add_heading3("MICRO-STEPS FOR MILESTONE 1:")
        for s in range(1, 8):
            pdf.add_paragraph(f"[ ] Step {s}: ________________________________________")
        pdf.add_blank_line()
        pdf.add_paragraph("FIRST TINY ACTION (do today): _________________________")
        pdf.add_page_break()

    # 90-Day Sprint Planner (4 pages)
    for month in range(1, 5):
        pdf.add_heading1(f"90-DAY SPRINT - Month {month}")
        pdf.add_paragraph(f"Dates: ___/___/___ to ___/___/___")
        pdf.add_blank_line()
        pdf.add_paragraph("GOAL 1 focus this month: _____________________________")
        pdf.add_paragraph("GOAL 2 focus this month: _____________________________")
        pdf.add_paragraph("GOAL 3 focus this month: _____________________________")
        pdf.add_blank_line()
        pdf.add_heading3("WEEKLY ACTIONS:")
        for w in range(1, 5):
            pdf.add_paragraph(f"Week {w}: ____________________________________________")
        pdf.add_blank_line()
        pdf.add_paragraph("Am I still interested? [ ] Yes! [ ] Meh [ ] No -> see 'pivot' page")
        pdf.add_page_break()

    # Weekly Check-ins (6 pages)
    for w in range(1, 7):
        pdf.add_heading1(f"WEEKLY GOAL CHECK-IN (Week {w})")
        pdf.add_paragraph("Goal 1 progress: [ ] On track [ ] Behind [ ] Ahead [ ] Pivoting")
        pdf.add_paragraph("Goal 2 progress: [ ] On track [ ] Behind [ ] Ahead [ ] Pivoting")
        pdf.add_paragraph("Goal 3 progress: [ ] On track [ ] Behind [ ] Ahead [ ] Pivoting")
        pdf.add_blank_line()
        pdf.add_paragraph("What I accomplished: ___________________________________")
        pdf.add_paragraph("What blocked me: _______________________________________")
        pdf.add_paragraph("Next week's ONE focus: _________________________________")
        pdf.add_paragraph("Excitement level (1-10): ___ (below 3? time to pivot)")
        pdf.add_page_break()

    # Celebrate & Goal Funeral
    pdf.add_heading1("CELEBRATE YOUR WINS")
    pdf.add_paragraph("Every milestone deserves recognition. Write your wins:")
    pdf.add_blank_line()
    for _ in range(10): pdf.add_paragraph("* _________________________________________________")
    pdf.add_page_break()

    pdf.add_heading1("GOAL FUNERAL")
    pdf.add_paragraph("Some goals need to be released. That's not failure - it's wisdom.")
    pdf.add_blank_line()
    pdf.add_paragraph("Goal I'm releasing: ____________________________________")
    pdf.add_paragraph("Why it no longer serves me: _____________________________")
    pdf.add_paragraph("What I learned from pursuing it: ________________________")
    pdf.add_paragraph("What I'm replacing it with (or nothing): ________________")
    pdf.add_blank_line()
    pdf.add_paragraph("Permission slip: I give myself permission to let this go.")
    pdf.add_paragraph("Signed: __________________ Date: ___/___/___")
    pdf.add_separator()
    pdf.add_paragraph("Made with love by FocusFlow Prints | Daniel Tesfamariam")
    return pdf



def create_book_7():
    """ADHD Weekly Planner - 55 pages"""
    pdf = PurePDF(title="ADHD Weekly Planner")
    pdf.add_title("ADHD WEEKLY PLANNER (UNDATED)")
    pdf.add_heading2("52 Weeks of Gentle Structure")
    pdf.add_paragraph("By Daniel Tesfamariam | FocusFlow Prints")
    pdf.add_separator()
    pdf.add_page_break()
    pdf.add_heading1("HOW TO USE THIS PLANNER")
    pdf.add_paragraph("3 rules: (1) Top 3 daily, (2) Time block big tasks, (3) Brain dump the rest")
    pdf.add_bullet("ONE page per week - not complex 2-page spreads")
    pdf.add_bullet("Only 1 'must-do' per day + 2 'nice to do'")
    pdf.add_bullet("Undated = no guilt for skipped weeks")
    pdf.add_page_break()
    for w in range(1, 53):
        pdf.add_heading1(f"WEEK {w}")
        pdf.add_paragraph("Week of: ____________  Theme/Focus: ___________________")
        pdf.add_blank_line()
        for day in ["Mon", "Tue", "Wed", "Thu", "Fri"]:
            pdf.add_paragraph(f"{day}: MUST: _________________ Nice: ________ ________")
        pdf.add_paragraph("Sat: ___________________________________________________")
        pdf.add_paragraph("Sun: ___________________________________________________")
        pdf.add_blank_line()
        pdf.add_paragraph("Appointments: __________________________________________")
        pdf.add_paragraph("Brain dump: ____________________________________________")
        pdf.add_paragraph("Weekly wins: ___________________________________________")
        pdf.add_paragraph("Mood: [ ]Great [ ]Good [ ]Meh [ ]Hard [ ]Survival mode")
        pdf.add_page_break()
    pdf.add_paragraph("You made it through the year. Every week you showed up was a win.")
    pdf.add_separator()
    pdf.add_paragraph("Made with love by FocusFlow Prints | Daniel Tesfamariam")
    return pdf


def create_book_8():
    """ADHD Self-Care & Mental Health Journal - 35 pages"""
    pdf = PurePDF(title="ADHD Self-Care Journal")
    pdf.add_title("ADHD SELF-CARE & MENTAL HEALTH JOURNAL")
    pdf.add_heading2("Gentle Tools for Hard Days")
    pdf.add_paragraph("By Daniel Tesfamariam | FocusFlow Prints")
    pdf.add_separator()
    pdf.add_page_break()
    pdf.add_heading1("ADHD & MENTAL HEALTH")
    pdf.add_paragraph("ADHD doesn't travel alone. Anxiety, depression, and rejection sensitivity are common co-travelers. This journal is your companion - not a replacement for therapy, but a tool to use alongside it.")
    pdf.add_page_break()
    # Daily Check-ins (14)
    for d in range(1, 15):
        pdf.add_heading1(f"DAILY CHECK-IN (Day {d})")
        pdf.add_paragraph(f"Date: ___/___/___")
        pdf.add_paragraph("Mood:     [ ]Great [ ]Good [ ]Okay [ ]Low [ ]Crisis")
        pdf.add_paragraph("Energy:   [ ]High  [ ]Med  [ ]Low  [ ]Empty")
        pdf.add_paragraph("Meds taken? [ ]Yes [ ]No [ ]N/A")
        pdf.add_paragraph("Sleep:    ___ hours  Quality: [ ]Good [ ]Bad [ ]Broken")
        pdf.add_blank_line()
        pdf.add_paragraph("One thing I'm grateful for: ____________________________")
        pdf.add_paragraph("One worry I'm releasing: _______________________________")
        pdf.add_paragraph("How I'll care for myself today: ________________________")
        pdf.add_page_break()
    # Anxiety Brain Dump
    pdf.add_heading1("ANXIETY BRAIN DUMP")
    pdf.add_paragraph("Get it OUT of your head and onto paper. Don't organize - just dump.")
    for _ in range(18): pdf.add_paragraph("_________________________________________________")
    pdf.add_page_break()
    pdf.add_heading1("ANXIETY BRAIN DUMP (page 2)")
    for _ in range(20): pdf.add_paragraph("_________________________________________________")
    pdf.add_page_break()
    # RSD Log
    pdf.add_heading1("RSD (REJECTION SENSITIVITY) LOG")
    pdf.add_paragraph("Track triggers. Separate FACTS from FEELINGS.")
    pdf.add_blank_line()
    for _ in range(3):
        pdf.add_paragraph("Situation: _____________________________________________")
        pdf.add_paragraph("What I FELT: ___________________________________________")
        pdf.add_paragraph("What actually HAPPENED (facts only): ____________________")
        pdf.add_paragraph("Were my feelings proportional? [ ] Yes [ ] Maybe not")
        pdf.add_paragraph("What I'd tell a friend in this situation: _______________")
        pdf.add_blank_line()
    pdf.add_page_break()
    # Self-Care Menu
    pdf.add_heading1("SELF-CARE MENU (BY ENERGY LEVEL)")
    pdf.add_heading3("LOW ENERGY (bed/couch level):")
    for i in ["Listen to comfort music", "Watch a comfort show", "Hold a warm drink", "Text one person", "Breathe for 2 minutes"]:
        pdf.add_bullet(i)
    pdf.add_heading3("MEDIUM ENERGY:")
    for i in ["Short walk outside", "Shower or bath", "Cook a simple meal", "Call a friend", "Gentle stretching"]:
        pdf.add_bullet(i)
    pdf.add_heading3("HIGH ENERGY:")
    for i in ["Exercise/dance", "Deep clean one room", "Creative project", "Social outing", "Try something new"]:
        pdf.add_bullet(i)
    pdf.add_page_break()
    # Coping Strategy Cards
    pdf.add_heading1("COPING STRATEGIES")
    pdf.add_heading3("5-4-3-2-1 GROUNDING:")
    pdf.add_paragraph("5 things I see: ________________________________________")
    pdf.add_paragraph("4 things I touch: ______________________________________")
    pdf.add_paragraph("3 things I hear: _______________________________________")
    pdf.add_paragraph("2 things I smell: ______________________________________")
    pdf.add_paragraph("1 thing I taste: _______________________________________")
    pdf.add_blank_line()
    pdf.add_heading3("BOX BREATHING:")
    pdf.add_paragraph("Breathe in (4 sec) -> Hold (4 sec) -> Out (4 sec) -> Hold (4 sec)")
    pdf.add_paragraph("Repeat 4 times. You're safe. You're here.")
    pdf.add_page_break()
    # Medication Tracker + Therapy Notes
    pdf.add_heading1("MEDICATION & SYMPTOM TRACKER")
    pdf.add_paragraph("Bring this page to your doctor appointments!")
    pdf.add_blank_line()
    pdf.add_paragraph("DATE     MEDICATION    DOSE    EFFECTIVENESS(1-5)   SIDE EFFECTS")
    for _ in range(8): pdf.add_paragraph("____  ____________  ______  * * * * *          ___________")
    pdf.add_page_break()
    pdf.add_heading1("THERAPY SESSION NOTES")
    pdf.add_paragraph("PRE-SESSION: What do I want to talk about?")
    for _ in range(4): pdf.add_paragraph("_________________________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("POST-SESSION: Key takeaways:")
    for _ in range(4): pdf.add_paragraph("_________________________________________________")
    pdf.add_paragraph("Homework/practice: _____________________________________")
    pdf.add_page_break()
    # Crisis Resources
    pdf.add_heading1("CRISIS RESOURCES")
    pdf.add_paragraph("If you're in crisis, please reach out:")
    pdf.add_blank_line()
    pdf.add_paragraph("988 Suicide & Crisis Lifeline: Call or text 988")
    pdf.add_paragraph("Crisis Text Line: Text HOME to 741741")
    pdf.add_paragraph("NAMI Helpline: 1-800-950-6264")
    pdf.add_paragraph("My therapist: _______________________ Phone: ____________")
    pdf.add_paragraph("My emergency contact: ________________ Phone: ____________")
    pdf.add_blank_line()
    pdf.add_paragraph("You are not a burden. You deserve help. Reaching out is brave.")
    pdf.add_separator()
    pdf.add_paragraph("Made with love by FocusFlow Prints | Daniel Tesfamariam")
    return pdf



def create_book_9():
    """ADHD Student Planner - 40 pages"""
    pdf = PurePDF(title="ADHD Student Planner")
    pdf.add_title("ADHD STUDENT PLANNER")
    pdf.add_heading2("Survive & Thrive in College with ADHD")
    pdf.add_paragraph("By Daniel Tesfamariam | FocusFlow Prints")
    pdf.add_separator()
    pdf.add_page_break()
    pdf.add_heading1("STUDENT LIFE WITH ADHD")
    pdf.add_paragraph("College + ADHD = unique challenges. This planner addresses:")
    pdf.add_bullet("Prioritizing assignments (not just listing them)")
    pdf.add_bullet("Breaking big projects into micro-steps")
    pdf.add_bullet("Using deadline pressure productively (not panicking)")
    pdf.add_bullet("Preventing burnout with built-in self-care")
    pdf.add_page_break()
    # Semester Overview (2 pages)
    pdf.add_heading1("SEMESTER OVERVIEW")
    pdf.add_paragraph("Semester: [ ] Fall [ ] Spring [ ] Summer   Year: ________")
    pdf.add_blank_line()
    pdf.add_paragraph("CLASS              PROFESSOR         OFFICE HOURS     ROOM")
    for _ in range(6): pdf.add_paragraph("______________  ______________  ______________  ______")
    pdf.add_page_break()
    pdf.add_heading1("IMPORTANT DATES")
    pdf.add_paragraph("Write ALL deadlines here first, then transfer to weekly pages:")
    pdf.add_blank_line()
    pdf.add_paragraph("DATE         CLASS           WHAT'S DUE              WEIGHT(%)")
    for _ in range(15): pdf.add_paragraph("___/___/___  ____________  ____________________  ______%")
    pdf.add_page_break()
    # Assignment Tracker (4 pages)
    for p in range(1, 5):
        pdf.add_heading1(f"ASSIGNMENT TRACKER (Page {p})")
        pdf.add_paragraph("CLASS        ASSIGNMENT          DUE DATE    PRIORITY   STATUS")
        for _ in range(10): pdf.add_paragraph("__________  ________________  ___/___/___  [H][M][L]  [ ]Done")
        pdf.add_page_break()
    # Weekly Study Planners (12 weeks)
    for w in range(1, 13):
        pdf.add_heading1(f"WEEKLY PLAN - Week {w}")
        pdf.add_paragraph("Dates: ___/___ to ___/___")
        pdf.add_paragraph("DEADLINES THIS WEEK: ___________________________________")
        pdf.add_blank_line()
        for day in ["Mon", "Tue", "Wed", "Thu", "Fri"]:
            pdf.add_paragraph(f"{day}: Classes: _______ | Study: _______ | Due: _______")
        pdf.add_paragraph("Weekend study plan: ____________________________________")
        pdf.add_paragraph("Self-care planned: _____________________________________")
        pdf.add_page_break()
    # Exam Prep (4 pages)
    for e in range(1, 5):
        pdf.add_heading1(f"EXAM PREP COUNTDOWN #{e}")
        pdf.add_paragraph(f"Exam: _________________ Date: ___/___/___ Days until: ___")
        pdf.add_blank_line()
        pdf.add_paragraph("STUDY PLAN (work backwards from exam date):")
        pdf.add_paragraph("Day 7: Review chapter ___  [ ] Done")
        pdf.add_paragraph("Day 6: Review chapter ___  [ ] Done")
        pdf.add_paragraph("Day 5: Practice problems   [ ] Done")
        pdf.add_paragraph("Day 4: Review chapter ___  [ ] Done")
        pdf.add_paragraph("Day 3: Make flash cards    [ ] Done")
        pdf.add_paragraph("Day 2: Full practice test  [ ] Done")
        pdf.add_paragraph("Day 1: Light review ONLY   [ ] Done (no cramming!)")
        pdf.add_paragraph("Exam day: You're ready!")
        pdf.add_page_break()
    # Project Breakdown + Procrastination
    pdf.add_heading1("BIG PROJECT BREAKDOWN")
    pdf.add_paragraph("Project: ____________________________________________")
    pdf.add_paragraph("Class: _________________ Due: ___/___/___ Weight: ___%")
    pdf.add_blank_line()
    pdf.add_paragraph("MICRO-STEPS (do ONE per day):")
    for i in range(1, 11): pdf.add_paragraph(f"[ ] Step {i}: ______________________ Mini-deadline: ___/___")
    pdf.add_page_break()
    pdf.add_heading1("PROCRASTINATION BUSTER")
    pdf.add_paragraph("You're procrastinating. That's okay. Try these:")
    pdf.add_blank_line()
    pdf.add_bullet("'Just 5 minutes' rule - set timer, start, stop if you want")
    pdf.add_bullet("Body doubling - study with someone (even on video call)")
    pdf.add_bullet("Change location (library, cafe, different room)")
    pdf.add_bullet("Break it smaller (what's the TINIEST first step?)")
    pdf.add_bullet("Bribe yourself (finish 1 section = 10 min phone break)")
    pdf.add_bullet("'Future me will hate present me' visualization")
    pdf.add_blank_line()
    pdf.add_paragraph("What I'll try right now: ________________________________")
    pdf.add_separator()
    pdf.add_paragraph("Made with love by FocusFlow Prints | Daniel Tesfamariam")
    return pdf


def create_book_10():
    """ADHD Freelancer Business Planner - 45 pages"""
    pdf = PurePDF(title="ADHD Freelancer Planner")
    pdf.add_title("ADHD FREELANCER & SIDE HUSTLE PLANNER")
    pdf.add_heading2("Run Your Business Without Burning Out Your Brain")
    pdf.add_paragraph("By Daniel Tesfamariam | FocusFlow Prints")
    pdf.add_separator()
    pdf.add_page_break()
    pdf.add_heading1("FREELANCING WITH ADHD")
    pdf.add_paragraph("ADHD gives you SUPERPOWERS for freelancing (creativity, hyperfocus, adaptability) AND challenges (admin tasks, consistency, invoicing).")
    pdf.add_paragraph("This planner handles the boring parts so you can do the creative parts.")
    pdf.add_page_break()
    # Business Overview
    pdf.add_heading1("MY BUSINESS OVERVIEW")
    pdf.add_paragraph("Business name: _________________________________________")
    pdf.add_paragraph("What I do: _____________________________________________")
    pdf.add_paragraph("My ideal client: _______________________________________")
    pdf.add_paragraph("My rates: $______/hour OR $______/project")
    pdf.add_paragraph("Monthly income goal: $ _____________")
    pdf.add_paragraph("Services I offer:")
    for i in range(1, 5): pdf.add_paragraph(f"  {i}. _________________________ Price: $ _______")
    pdf.add_page_break()
    # Income Tracker (4 months)
    for m in range(1, 5):
        pdf.add_heading1(f"INCOME TRACKER - Month {m}")
        pdf.add_paragraph("Month: _______________")
        pdf.add_blank_line()
        pdf.add_paragraph("CLIENT          PROJECT              AMOUNT     PAID?")
        for _ in range(8): pdf.add_paragraph("____________  __________________  $ ________  [ ]Yes [ ]No")
        pdf.add_paragraph("TOTAL INCOME: $ ________   GOAL: $ ________")
        pdf.add_page_break()
    # Expense Tracker (4 months)
    for m in range(1, 5):
        pdf.add_heading1(f"EXPENSE TRACKER - Month {m}")
        pdf.add_paragraph("Month: _______________")
        pdf.add_blank_line()
        pdf.add_paragraph("DATE     EXPENSE              CATEGORY        AMOUNT")
        for _ in range(10): pdf.add_paragraph("___/___  ________________  ____________  $ ________")
        pdf.add_paragraph("TOTAL EXPENSES: $ ________")
        pdf.add_page_break()
    # Invoice Template (2 pages)
    pdf.add_heading1("INVOICE TEMPLATE")
    pdf.add_paragraph("INVOICE #: _________     DATE: ___/___/___")
    pdf.add_blank_line()
    pdf.add_paragraph("FROM: (Your business name)")
    pdf.add_paragraph("________________________________")
    pdf.add_paragraph("________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("TO: (Client)")
    pdf.add_paragraph("________________________________")
    pdf.add_paragraph("________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("DESCRIPTION                    QTY    RATE       AMOUNT")
    for _ in range(5): pdf.add_paragraph("__________________________  ___  $ ______  $ ________")
    pdf.add_blank_line()
    pdf.add_paragraph("                                         SUBTOTAL: $ ________")
    pdf.add_paragraph("                                         TAX:      $ ________")
    pdf.add_paragraph("                                         TOTAL:    $ ________")
    pdf.add_paragraph("DUE DATE: ___/___/___")
    pdf.add_paragraph("PAYMENT METHOD: ________________________________________")
    pdf.add_page_break()
    # Client Tracker (4 pages)
    for c in range(1, 5):
        pdf.add_heading1(f"CLIENT TRACKER (Page {c})")
        pdf.add_blank_line()
        for _ in range(2):
            pdf.add_paragraph("Client: ______________________ Email: ___________________")
            pdf.add_paragraph("Phone: ______________________ Rate: $ _______")
            pdf.add_paragraph("Project: ________________ Status: [ ]Active [ ]Complete [ ]Pending")
            pdf.add_paragraph("Notes: __________________________________________________")
            pdf.add_blank_line()
        pdf.add_page_break()
    # Project Planner (4 pages)
    for p in range(1, 5):
        pdf.add_heading1(f"PROJECT PLANNER #{p}")
        pdf.add_paragraph("Project: ___________________ Client: ___________________")
        pdf.add_paragraph("Deadline: ___/___/___ Fee: $ _______ Hours est: _______")
        pdf.add_blank_line()
        pdf.add_paragraph("TASKS:")
        for i in range(1, 8): pdf.add_paragraph(f"[ ] {i}. _______________________________ Due: ___/___")
        pdf.add_paragraph("Status: [ ] Not started [ ] In progress [ ] Review [ ] Done [ ] Invoiced")
        pdf.add_page_break()
    # Tax Prep + CEO Day + Quarterly Review
    pdf.add_heading1("TAX PREP CHECKLIST")
    pdf.add_paragraph("Q1 (Jan-Mar) estimated tax due: April 15 - $ _______")
    pdf.add_paragraph("Q2 (Apr-Jun) estimated tax due: June 15 - $ _______")
    pdf.add_paragraph("Q3 (Jul-Sep) estimated tax due: Sept 15 - $ _______")
    pdf.add_paragraph("Q4 (Oct-Dec) estimated tax due: Jan 15 - $ _______")
    pdf.add_blank_line()
    pdf.add_paragraph("DEDUCTIONS TO TRACK:")
    for d in ["Home office (% of rent/mortgage)", "Internet/phone (% for business)", "Software/subscriptions", "Equipment purchases", "Professional development", "Marketing/advertising", "Travel for work", "Meals with clients (50%)"]:
        pdf.add_bullet(d)
    pdf.add_page_break()
    pdf.add_heading1("'CEO DAY' MONTHLY PLANNER")
    pdf.add_paragraph("Pick ONE day per month for all boring admin. Batch it. Done.")
    pdf.add_blank_line()
    pdf.add_paragraph("My CEO Day this month: ___/___/___")
    pdf.add_blank_line()
    pdf.add_paragraph("CEO DAY CHECKLIST:")
    for task in ["[ ] Send all pending invoices", "[ ] Follow up on unpaid invoices", "[ ] Update income/expense tracking", "[ ] Review upcoming deadlines", "[ ] Respond to inquiries/emails", "[ ] Update portfolio/website", "[ ] Plan next month's marketing", "[ ] Set quarterly tax aside", "[ ] Check subscriptions (cancel unused)", "[ ] Celebrate wins!"]:
        pdf.add_paragraph(f"  {task}")
    pdf.add_page_break()
    for q in range(1, 5):
        pdf.add_heading1(f"QUARTERLY REVIEW - Q{q}")
        pdf.add_paragraph("Total revenue: $ _________  Total expenses: $ _________")
        pdf.add_paragraph("Profit: $ _________  Tax set aside: $ _________")
        pdf.add_paragraph("Number of clients: ___ Projects completed: ___")
        pdf.add_blank_line()
        pdf.add_paragraph("What went well: ________________________________________")
        pdf.add_paragraph("What was hard: _________________________________________")
        pdf.add_paragraph("Next quarter's focus: __________________________________")
        pdf.add_paragraph("Rate adjustment needed? [ ] Yes -> new rate: $ ___/hr")
        pdf.add_page_break()
    pdf.add_heading1("PRICING CALCULATOR")
    pdf.add_paragraph("What do you WANT to earn per year? $ ___________")
    pdf.add_paragraph("Divide by 50 weeks = $ _________/week")
    pdf.add_paragraph("Divide by hours you WANT to work/week (___hrs) = $ ____/hr")
    pdf.add_paragraph("Add 30% for taxes + expenses = $ ____/hr MINIMUM RATE")
    pdf.add_blank_line()
    pdf.add_paragraph("MY MINIMUM RATE: $ _______/hour")
    pdf.add_paragraph("You are allowed to charge this. You are worth this.")
    pdf.add_separator()
    pdf.add_paragraph("Made with love by FocusFlow Prints | Daniel Tesfamariam")
    return pdf



def main():
    """Generate all 10 PDF books."""
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'books-pdf-output')
    os.makedirs(output_dir, exist_ok=True)

    books = [
        ("01-ADHD-Budget-Planner.pdf", "ADHD Budget Planner", create_book_1),
        ("02-ADHD-Daily-Routine-Planner.pdf", "ADHD Daily Routine Planner", create_book_2),
        ("03-ADHD-Habit-Tracker-Bundle.pdf", "ADHD Habit Tracker Bundle", create_book_3),
        ("04-ADHD-Meal-Planner.pdf", "ADHD Meal Planner & Grocery List", create_book_4),
        ("05-ADHD-Cleaning-Schedule.pdf", "ADHD Cleaning Schedule", create_book_5),
        ("06-ADHD-Goal-Setting-Workbook.pdf", "ADHD Goal Setting Workbook", create_book_6),
        ("07-ADHD-Weekly-Planner.pdf", "ADHD Weekly Planner (Undated)", create_book_7),
        ("08-ADHD-Self-Care-Journal.pdf", "ADHD Self-Care & Mental Health Journal", create_book_8),
        ("09-ADHD-Student-Planner.pdf", "ADHD Student Planner", create_book_9),
        ("10-ADHD-Freelancer-Planner.pdf", "ADHD Freelancer Business Planner", create_book_10),
    ]

    print("=" * 60)
    print("  FocusFlow Prints - 10 ADHD Planner Books Generator")
    print("  By Daniel Tesfamariam")
    print("=" * 60)
    print()

    results = []
    for i, (filename, title, creator) in enumerate(books, 1):
        print(f"[{i}/10] Generating: {title}")
        try:
            pdf = creator()
            filepath = os.path.join(output_dir, filename)
            size = pdf.save(filepath)
            size_kb = size / 1024
            pages = len(pdf.pages) + (1 if pdf.current_page_content else 0)
            print(f"       -> {filename} ({pages} pages, {size_kb:.0f} KB)")
            results.append((filename, pages, size_kb))
        except Exception as e:
            print(f"       ERROR: {e}")
            import traceback
            traceback.print_exc()
        print()

    print("=" * 60)
    print("  ALL BOOKS GENERATED!")
    print("=" * 60)
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
    print(f"  TOTAL: {len(results)} books, {total_pages} pages, {total_size:.0f} KB ({total_size/1024:.1f} MB)")


if __name__ == '__main__':
    main()
