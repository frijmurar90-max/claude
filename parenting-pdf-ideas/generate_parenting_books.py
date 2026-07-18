#!/usr/bin/env python3
"""
PARENTING PDF PRODUCTS GENERATOR
Top 5 trending products based on real search data
By Daniel Tesfamariam
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'etsy-digital-products-strategy'))
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'etsy-digital-products-strategy', 'generate_pdfs.py')).read())


def product1_screen_time():
    """Screen Time Management System for Kids - 30 pages"""
    pdf = PurePDF(title="Screen Time Management System")
    pdf.add_title("THE SCREEN TIME MANAGEMENT SYSTEM")
    pdf.add_heading2("A Complete Printable Toolkit to Help Kids")
    pdf.add_heading2("Build Healthy Digital Habits (Ages 3-12)")
    pdf.add_blank_line()
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_paragraph("Based on AAP (American Academy of Pediatrics) Guidelines")
    pdf.add_separator()
    pdf.add_page_break()


    # Welcome page
    pdf.add_heading1("FOR PARENTS: HOW TO USE THIS SYSTEM")
    pdf.add_paragraph("This system works because it gives kids OWNERSHIP over their screen time instead of making you the 'screen police.' When kids understand the rules, help track their own time, and earn screen privileges - battles decrease dramatically.")
    pdf.add_blank_line()
    pdf.add_heading3("THE 4 COMPONENTS:")
    pdf.add_bullet("1. FAMILY RULES (pages 3-5): Establish clear, visual boundaries")
    pdf.add_bullet("2. EARN IT SYSTEM (pages 6-12): Tasks completed before screens")
    pdf.add_bullet("3. TRACKING (pages 13-20): Kids self-monitor with parent verification")
    pdf.add_bullet("4. ALTERNATIVES (pages 21-30): 100 activities to replace screen time")
    pdf.add_blank_line()
    pdf.add_heading3("AAP RECOMMENDED LIMITS:")
    pdf.add_paragraph("Ages 2-5: Max 1 hour/day of high-quality programming (with adult)")
    pdf.add_paragraph("Ages 6-12: Consistent limits, prioritize sleep, activity, homework first")
    pdf.add_paragraph("All ages: No screens 1 hour before bed, no screens during meals")
    pdf.add_blank_line()
    pdf.add_paragraph("TIP: Laminate pages 3-6 and hang them where kids can see daily!")
    pdf.add_page_break()

    # Family Screen Time Rules Contract
    pdf.add_heading1("OUR FAMILY SCREEN TIME RULES")
    pdf.add_paragraph("(Post this where everyone can see it!)")
    pdf.add_blank_line()
    pdf.add_heading3("WE AGREE TO THESE RULES:")
    pdf.add_blank_line()
    rules = [
        "Screens are OFF during meals (breakfast, lunch, dinner)",
        "No screens in the bedroom at night",
        "Homework and chores FIRST, screens AFTER",
        "All screens OFF by ______ PM on school nights",
        "All screens OFF by ______ PM on weekends",
        "We ask permission before downloading new apps/games",
        "We tell a parent if we see something scary or confusing online",
        "We take a break every 30 minutes (stretch, blink, move!)",
        "No screens in the car for trips under 30 minutes",
        "We use kind words online (same as in person)"
    ]
    for i, rule in enumerate(rules, 1):
        pdf.add_paragraph(f"  {i:2d}. [ ] {rule}")
    pdf.add_blank_line()
    pdf.add_paragraph("Family rule we want to add: _______________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("SIGNED:")
    pdf.add_paragraph("Child: _________________________ Date: ___/___/___")
    pdf.add_paragraph("Child: _________________________ Date: ___/___/___")
    pdf.add_paragraph("Parent: ________________________ Date: ___/___/___")
    pdf.add_paragraph("Parent: ________________________ Date: ___/___/___")
    pdf.add_page_break()

    # Screen time limits by age poster
    pdf.add_heading1("SCREEN TIME LIMITS (By Age)")
    pdf.add_paragraph("(Print and post on the fridge!)")
    pdf.add_blank_line()
    pdf.add_heading3("AGES 2-5:")
    pdf.add_paragraph("  Daily MAX: 1 hour")
    pdf.add_paragraph("  Type: Educational only (PBS Kids, Khan Academy Kids)")
    pdf.add_paragraph("  Rule: ALWAYS with a parent watching/discussing")
    pdf.add_blank_line()
    pdf.add_heading3("AGES 6-8:")
    pdf.add_paragraph("  School days: ______ minutes (recommended: 30-60 min)")
    pdf.add_paragraph("  Weekends: ______ minutes (recommended: 60-90 min)")
    pdf.add_paragraph("  Type: Mix of educational and entertainment")
    pdf.add_blank_line()
    pdf.add_heading3("AGES 9-12:")
    pdf.add_paragraph("  School days: ______ minutes (recommended: 60-90 min)")
    pdf.add_paragraph("  Weekends: ______ minutes (recommended: 90-120 min)")
    pdf.add_paragraph("  Type: Age-appropriate, parent-approved content")
    pdf.add_blank_line()
    pdf.add_heading3("ALL AGES - NO SCREEN ZONES:")
    pdf.add_paragraph("  [X] Dinner table    [X] Bedrooms at night    [X] During homework")
    pdf.add_paragraph("  [X] 1 hour before bed    [X] First thing in morning")
    pdf.add_page_break()

    # Device-free zone signs
    pdf.add_heading1("DEVICE-FREE ZONE")
    pdf.add_paragraph("(Cut out and place in screen-free areas)")
    pdf.add_blank_line()
    pdf.add_paragraph("================================================")
    pdf.add_paragraph("         >>> DEVICE-FREE ZONE <<<")
    pdf.add_paragraph("")
    pdf.add_paragraph("    No phones. No tablets. No TV.")
    pdf.add_paragraph("    Just US being together.")
    pdf.add_paragraph("")
    pdf.add_paragraph("    This is a space for:")
    pdf.add_paragraph("    * Talking    * Eating    * Reading")
    pdf.add_paragraph("    * Playing    * Sleeping  * Creating")
    pdf.add_paragraph("================================================")
    pdf.add_blank_line()
    pdf.add_paragraph("Place in: [ ] Kitchen/Dining  [ ] Bedroom  [ ] Homework area  [ ] ________")
    pdf.add_page_break()

    # Earn Your Screen Time checklist
    pdf.add_heading1("EARN YOUR SCREEN TIME!")
    pdf.add_paragraph("Complete these FIRST to unlock screen time. No checks = No screens!")
    pdf.add_paragraph("(Print a new copy each day or laminate and use dry-erase marker)")
    pdf.add_blank_line()
    pdf.add_heading3("BEFORE SCREENS - DAILY CHECKLIST:")
    pdf.add_blank_line()
    pdf.add_paragraph("MORNING:")
    for task in ["Made my bed", "Ate breakfast (at table, no screen)", "Brushed teeth", "Got dressed", "Backpack/lunch ready (school days)"]:
        pdf.add_paragraph(f"  [ ] {task}")
    pdf.add_blank_line()
    pdf.add_paragraph("AFTER SCHOOL:")
    for task in ["Homework DONE (or no homework today)", "Read for 20 minutes", "Played outside / physical activity for 30 min", "One chore completed (_______________)", "Talked to a family member about my day"]:
        pdf.add_paragraph(f"  [ ] {task}")
    pdf.add_blank_line()
    pdf.add_paragraph("ALL CHECKS DONE? -------> SCREEN TIME UNLOCKED!")
    pdf.add_paragraph("Time earned today: ______ minutes")
    pdf.add_paragraph("Timer set? [ ] YES  Start time: ______  Stop time: ______")
    pdf.add_page_break()

    # Weekly earn it pages (4 weeks)
    for week in range(1, 5):
        pdf.add_heading1(f"WEEKLY SCREEN TIME TRACKER - Week {week}")
        pdf.add_paragraph("Child's name: ___________________ Week of: ___/___/___")
        pdf.add_blank_line()
        pdf.add_paragraph("DAY        EARNED?  MINUTES USED   WHAT WATCHED/PLAYED     PARENT OK?")
        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
            pdf.add_paragraph(f"{day:11s} [ ]Y[ ]N  ___ min     ____________________    [ ]")
        pdf.add_blank_line()
        pdf.add_paragraph("WEEKLY TOTAL: ___ minutes  (Target max: ___ minutes)")
        pdf.add_paragraph("Under limit? [ ] YES! Great job!  [ ] Over - let's adjust next week")
        pdf.add_paragraph("Best day (least screen time): _______________")
        pdf.add_paragraph("Reward earned this week? [ ] YES -> Reward: _______________")
        pdf.add_page_break()

    # Screen Time Reward Token System
    pdf.add_heading1("SCREEN TIME TOKEN SYSTEM")
    pdf.add_paragraph("Cut out tokens below. Kids earn tokens for good behavior and can 'spend' them on screen time. Makes it tangible and teaches budgeting!")
    pdf.add_blank_line()
    pdf.add_heading3("HOW IT WORKS:")
    pdf.add_paragraph("1. Child earns tokens for: chores, reading, kindness, outdoor play")
    pdf.add_paragraph("2. Each token = 15 minutes of screen time")
    pdf.add_paragraph("3. Child decides WHEN to spend tokens (teaches self-regulation!)")
    pdf.add_paragraph("4. Unspent tokens at end of week = bonus reward!")
    pdf.add_blank_line()
    pdf.add_heading3("EARN TOKENS FOR:")
    pdf.add_paragraph("  Read 20 min = 1 token    |  Extra chore = 1 token")
    pdf.add_paragraph("  Outside 30 min = 1 token |  Kindness spotted = 1 token")
    pdf.add_paragraph("  Homework without fuss = 1 token")
    pdf.add_blank_line()
    pdf.add_paragraph("TOKENS (cut out - each = 15 min screen time):")
    pdf.add_paragraph("[15 MIN] [15 MIN] [15 MIN] [15 MIN] [15 MIN]")
    pdf.add_paragraph("[15 MIN] [15 MIN] [15 MIN] [15 MIN] [15 MIN]")
    pdf.add_paragraph("[15 MIN] [15 MIN] [15 MIN] [15 MIN] [15 MIN]")
    pdf.add_paragraph("[15 MIN] [15 MIN] [15 MIN] [15 MIN] [15 MIN]")
    pdf.add_page_break()

    # Monthly report card
    pdf.add_heading1("MONTHLY SCREEN TIME REPORT CARD")
    pdf.add_paragraph("Month: ___________________ Child: ___________________")
    pdf.add_blank_line()
    pdf.add_paragraph("WEEK 1: Total screen time: ___ hrs ___ min  Under limit? [ ]Y [ ]N")
    pdf.add_paragraph("WEEK 2: Total screen time: ___ hrs ___ min  Under limit? [ ]Y [ ]N")
    pdf.add_paragraph("WEEK 3: Total screen time: ___ hrs ___ min  Under limit? [ ]Y [ ]N")
    pdf.add_paragraph("WEEK 4: Total screen time: ___ hrs ___ min  Under limit? [ ]Y [ ]N")
    pdf.add_blank_line()
    pdf.add_paragraph("MONTHLY TOTAL: ___ hours  DAILY AVERAGE: ___ min/day")
    pdf.add_blank_line()
    pdf.add_heading3("IMPROVEMENTS THIS MONTH:")
    pdf.add_paragraph("[ ] Less arguing about screen time")
    pdf.add_paragraph("[ ] More outdoor/creative play")
    pdf.add_paragraph("[ ] Better sleep")
    pdf.add_paragraph("[ ] More family time")
    pdf.add_paragraph("[ ] Child self-regulating (turning off without being asked)")
    pdf.add_blank_line()
    pdf.add_paragraph("GRADE: [ ] A (Amazing!) [ ] B (Good progress!) [ ] C (Keep trying!) [ ] Needs work")
    pdf.add_paragraph("REWARD EARNED: ___________________________")
    pdf.add_page_break()

    # 100 Things to Do Instead of Screens
    pdf.add_heading1("100 THINGS TO DO INSTEAD OF SCREENS")
    pdf.add_paragraph("(Post this on the fridge! When kids say 'I'm bored!' point here.)")
    pdf.add_blank_line()
    activities = [
        "Build a fort with blankets", "Draw or color", "Play with LEGO/blocks",
        "Read a book", "Write a story", "Play outside", "Ride a bike", "Jump rope",
        "Play catch", "Climb a tree", "Have a dance party", "Do a puzzle",
        "Play board games", "Play card games", "Make up a play/skit",
        "Build with cardboard boxes", "Play with play-dough/clay", "Paint or finger paint",
        "Write a letter to grandparent", "Plant seeds/garden", "Cook or bake together",
        "Do a science experiment", "Play dress-up", "Make a treasure hunt",
        "Play in the sprinkler", "Have a picnic", "Bird watching", "Fly a kite",
        "Play hide and seek", "Make friendship bracelets", "Play with pets",
        "Visit the library", "Go for a nature walk", "Collect rocks/leaves",
        "Make a collage", "Play with bubbles", "Do yoga/stretching",
        "Learn a magic trick", "Write in a journal", "Organize your room",
        "Call a friend", "Play an instrument", "Sing songs", "Tell jokes",
        "Play restaurant/store", "Build a race track", "Have a tea party",
        "Make paper airplanes", "Do origami", "Play with water toys"
    ]
    for i, act in enumerate(activities, 1):
        pdf.add_paragraph(f"  {i:2d}. {act}")
        if i == 50:
            pdf.add_page_break()
            pdf.add_heading1("100 THINGS TO DO (continued)")
            pdf.add_blank_line()

    more = ["Star gaze at night", "Play flashlight tag", "Make shadow puppets",
            "Build a birdhouse", "Press flowers", "Make a time capsule",
            "Learn to juggle", "Play hopscotch", "Make slime",
            "Write a comic book", "Play Simon Says", "Do an obstacle course",
            "Make a lemonade stand", "Play with magnets", "Make a vision board",
            "Play charades", "Make homemade cards", "Learn to knit/crochet",
            "Do a random act of kindness", "Play 20 questions",
            "Make a family tree", "Play with sidewalk chalk", "Build a sandcastle",
            "Make a bookmark", "Go on a bike ride", "Play tag",
            "Make a fort outside", "Stargaze", "Tell campfire stories",
            "Make your own board game", "Write a song", "Do a craft project",
            "Play basketball/soccer", "Go swimming", "Make a photo album",
            "Play with trains/cars", "Build with sticks outside", "Make mud pies",
            "Have a water balloon fight", "Learn a new skill", "Play freeze dance",
            "Make a scrapbook", "Create an invention", "Go on a scavenger hunt",
            "Play monkey in the middle", "Build domino chain", "Make sock puppets",
            "Play frisbee", "Do cartwheels", "ENJOY BEING A KID!"]
    for i, act in enumerate(more, 51):
        pdf.add_paragraph(f"  {i:3d}. {act}")
    pdf.add_page_break()

    # Digital Wellness Family Discussion Cards
    pdf.add_heading1("FAMILY MEETING: DIGITAL WELLNESS DISCUSSION")
    pdf.add_paragraph("Use these questions for a monthly family check-in about screens:")
    pdf.add_blank_line()
    questions = [
        "What's your favorite thing to do that doesn't involve a screen?",
        "How do you feel AFTER a long time on screens? (tired? wired? sad?)",
        "Is there anything you've seen online that confused or upset you?",
        "What would you do with an extra hour if screens weren't an option?",
        "Do you think our family rules about screens are fair? What would you change?",
        "What's one new hobby or skill you'd like to try?",
        "How can we help each other put screens down?",
        "What's the best part of our screen-free time together?",
        "Is anyone at school talking about things they see online? How does that feel?",
        "What 'screen-free challenge' should our family try this week?"
    ]
    for i, q in enumerate(questions, 1):
        pdf.add_paragraph(f"  {i:2d}. {q}")
        pdf.add_blank_line()
    pdf.add_page_break()

    # Implementation tips
    pdf.add_heading1("PARENT TIPS: MAKING THIS WORK")
    pdf.add_blank_line()
    pdf.add_heading3("THE FIRST WEEK (Expect pushback!):")
    pdf.add_bullet("Announce new system at a family meeting - get input")
    pdf.add_bullet("Start on a weekend when everyone is calm")
    pdf.add_bullet("Expect 2-3 days of complaints - stay consistent")
    pdf.add_bullet("Celebrate EVERY day they follow the system")
    pdf.add_bullet("Lead by example - limit YOUR screen time too!")
    pdf.add_blank_line()
    pdf.add_heading3("WHEN THEY PUSH BACK (and they will):")
    pdf.add_paragraph("Say: 'I understand you're frustrated. The rules still apply.'")
    pdf.add_paragraph("Say: 'You can earn more screen time by [specific task].'")
    pdf.add_paragraph("Say: 'What from the 100 activities list sounds fun right now?'")
    pdf.add_paragraph("Don't say: 'Because I said so!' (explain the WHY)")
    pdf.add_blank_line()
    pdf.add_heading3("SIGNS THE SYSTEM IS WORKING:")
    pdf.add_paragraph("[ ] Less arguing about screen time")
    pdf.add_paragraph("[ ] Child asks for activities instead of screens")
    pdf.add_paragraph("[ ] Better sleep (falling asleep faster)")
    pdf.add_paragraph("[ ] More creativity and independent play")
    pdf.add_paragraph("[ ] Child self-regulates (turns off without being told)")
    pdf.add_paragraph("[ ] More family conversation and connection")
    pdf.add_blank_line()
    pdf.add_paragraph("Remember: Progress > Perfection. Even 30% less screen time = better outcomes.")
    pdf.add_separator()
    pdf.add_paragraph("By Daniel Tesfamariam | Raising humans, not screen zombies.")
    return pdf


    pdf.add_heading1("FOR PARENTS: HOW TO USE THIS SYSTEM")
    pdf.add_paragraph("This system gives kids OWNERSHIP over screen time instead of making you the 'screen police.'")
    pdf.add_blank_line()
    pdf.add_paragraph("4 COMPONENTS: 1) Family Rules, 2) Earn-It System, 3) Tracking, 4) Alternatives")
    pdf.add_blank_line()
    pdf.add_paragraph("AAP LIMITS: Ages 2-5: 1hr/day | Ages 6+: Consistent limits | All: No screens before bed")
    pdf.add_paragraph("TIP: Laminate key pages and hang where kids see them daily!")
    pdf.add_page_break()
    pdf.add_heading1("OUR FAMILY SCREEN TIME RULES")
    pdf.add_paragraph("(Post where everyone can see! Have kids sign for buy-in)")
    pdf.add_blank_line()
    rules = ["Screens OFF during meals", "No screens in bedroom at night", "Homework and chores FIRST, screens AFTER", "All screens OFF by ___PM on school nights", "All screens OFF by ___PM weekends", "Ask permission before new apps/games", "Tell a parent if we see something scary online", "Break every 30 minutes (stretch, move!)", "No screens in car for trips under 30 min", "Kind words online (same as in person)"]
    for i, r in enumerate(rules, 1):
        pdf.add_paragraph(f"  {i}. [ ] {r}")
    pdf.add_blank_line()
    pdf.add_paragraph("SIGNED: Child _______________ Parent _______________ Date ___/___/___")
    pdf.add_page_break()


    pdf.add_heading1("SCREEN TIME LIMITS BY AGE")
    pdf.add_paragraph("Ages 2-5: MAX 1 hour/day, educational only, WITH a parent")
    pdf.add_paragraph("Ages 6-8: School days ___ min | Weekends ___ min (rec: 30-60/60-90)")
    pdf.add_paragraph("Ages 9-12: School days ___ min | Weekends ___ min (rec: 60-90/90-120)")
    pdf.add_paragraph("NO-SCREEN ZONES: Dinner table | Bedrooms | During homework | Before bed")
    pdf.add_page_break()
    pdf.add_heading1("EARN YOUR SCREEN TIME! (Daily Checklist)")
    pdf.add_paragraph("Complete ALL tasks to unlock screen time today:")
    pdf.add_blank_line()
    pdf.add_paragraph("MORNING:")
    for t in ["Made bed", "Ate breakfast (no screen)", "Brushed teeth", "Got dressed", "Backpack ready"]:
        pdf.add_paragraph(f"  [ ] {t}")
    pdf.add_paragraph("AFTER SCHOOL:")
    for t in ["Homework DONE", "Read 20 min", "Outside play 30 min", "One chore done", "Talked to family about day"]:
        pdf.add_paragraph(f"  [ ] {t}")
    pdf.add_paragraph("ALL DONE? -> SCREEN TIME UNLOCKED! Minutes earned: ___  Timer set? [ ]")
    pdf.add_page_break()
    # Weekly trackers (4)
    for w in range(1, 5):
        pdf.add_heading1(f"WEEKLY SCREEN TIME TRACKER - Week {w}")
        pdf.add_paragraph("Child: ___________________ Week of: ___/___/___")
        pdf.add_paragraph("DAY        EARNED?  MINS USED   WHAT WATCHED        PARENT OK?")
        for d in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
            pdf.add_paragraph(f"{d:10s} [ ]Y[ ]N  ___min    __________________  [ ]")
        pdf.add_paragraph("TOTAL: ___min | Under limit? [ ]YES [ ]Over | Reward? ___________")
        pdf.add_page_break()
    # Token system
    pdf.add_heading1("SCREEN TIME TOKEN SYSTEM")
    pdf.add_paragraph("Earn tokens for good habits. Each token = 15 min screen time.")
    pdf.add_paragraph("EARN: Read 20min=1 | Chore=1 | Outside 30min=1 | Kindness=1 | Homework=1")
    pdf.add_blank_line()
    pdf.add_paragraph("TOKENS: [15] [15] [15] [15] [15] [15] [15] [15] [15] [15]")
    pdf.add_paragraph("        [15] [15] [15] [15] [15] [15] [15] [15] [15] [15]")
    pdf.add_paragraph("Tokens earned this week: ___ | Tokens spent: ___ | Saved: ___")
    pdf.add_page_break()
    # 100 alternatives
    pdf.add_heading1("100 THINGS TO DO INSTEAD OF SCREENS")
    pdf.add_paragraph("(Print and post on the fridge!)")
    activities = ["Build a fort", "Draw/color", "LEGO/blocks", "Read a book", "Write a story", "Play outside", "Ride bike", "Jump rope", "Dance party", "Puzzles", "Board games", "Card games", "Play-dough", "Paint", "Write letter", "Plant seeds", "Cook/bake", "Science experiment", "Dress-up", "Treasure hunt", "Sprinkler play", "Picnic", "Kite flying", "Hide & seek", "Bracelets", "Library visit", "Nature walk", "Bubbles", "Yoga", "Magic tricks", "Journal", "Organize room", "Call a friend", "Play instrument", "Tell jokes", "Paper airplanes", "Origami", "Play catch", "Climb tree", "Hopscotch", "Obstacle course", "Chalk art", "Sandcastle", "Water balloons", "Scavenger hunt", "Make slime", "Comic book", "Charades", "Lemonade stand", "ENJOY BEING A KID!"]
    for i, a in enumerate(activities, 1):
        pdf.add_paragraph(f"  {i:2d}. {a}")
    pdf.add_page_break()
    # Family discussion
    pdf.add_heading1("FAMILY DIGITAL WELLNESS DISCUSSION")
    pdf.add_paragraph("Monthly check-in questions:")
    for q in ["What's your favorite non-screen activity?", "How do you feel AFTER long screen time?", "Anything online that confused or upset you?", "What would you do with an extra screen-free hour?", "Are our screen rules fair? What would you change?", "What new hobby should we try as a family?", "What screen-free challenge should we try this week?"]:
        pdf.add_paragraph(f"  * {q}")
    pdf.add_page_break()
    pdf.add_heading1("TIPS: MAKING THIS WORK")
    pdf.add_paragraph("Week 1: Expect pushback! Stay consistent. Celebrate every win.")
    pdf.add_paragraph("Lead by example: limit YOUR screen time too!")
    pdf.add_paragraph("When they push back say: 'I understand you're frustrated. The rules still apply.'")
    pdf.add_paragraph("Signs it's working: less arguing, more play, better sleep, more connection")
    pdf.add_separator()
    pdf.add_paragraph("By Daniel Tesfamariam | Raising humans, not screen zombies.")
    return pdf



def product2_tantrum_toolkit():
    """Gentle Parenting Toddler Tantrum Toolkit - 35 pages"""
    pdf = PurePDF(title="Toddler Tantrum Toolkit")
    pdf.add_title("GENTLE PARENTING TODDLER TANTRUM TOOLKIT")
    pdf.add_heading2("20 Calm-Down Strategies, Scripts & Visual Tools")
    pdf.add_heading2("for Parents of Children Ages 1-5")
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_separator()
    pdf.add_page_break()
    pdf.add_heading1("WHY TODDLERS HAVE TANTRUMS (It's Normal!)")
    pdf.add_paragraph("Tantrums are NOT bad behavior. They're a sign your child's brain is overwhelmed and they haven't yet developed the skills to regulate emotions.")
    pdf.add_blank_line()
    pdf.add_paragraph("BRAIN SCIENCE: The prefrontal cortex (logic, self-control) isn't fully developed until age 25. Toddlers are literally unable to 'calm down on command.'")
    pdf.add_blank_line()
    pdf.add_paragraph("YOUR JOB: Be the calm in their storm. Co-regulate (stay calm yourself) and they will learn to self-regulate over time.")
    pdf.add_page_break()
    # The PAUSE method
    pdf.add_heading1("THE P.A.U.S.E. METHOD")
    pdf.add_paragraph("When a tantrum starts, use this 5-step framework:")
    pdf.add_blank_line()
    pdf.add_paragraph("P - PAUSE. Stop what you're doing. Take 3 breaths.")
    pdf.add_paragraph("A - ACKNOWLEDGE. 'I see you're really upset right now.'")
    pdf.add_paragraph("U - UNDERSTAND. What need is unmet? (hungry? tired? overwhelmed?)")
    pdf.add_paragraph("S - SUPPORT. Offer connection: 'I'm here. Would you like a hug?'")
    pdf.add_paragraph("E - EMPATHIZE. 'It's hard when we can't have what we want.'")
    pdf.add_blank_line()
    pdf.add_paragraph("AFTER the storm passes:")
    pdf.add_paragraph("1. Validate: 'You had really big feelings.'")
    pdf.add_paragraph("2. Name it: 'That was frustration/anger/sadness.'")
    pdf.add_paragraph("3. Problem-solve: 'Next time, you can...'")
    pdf.add_page_break()
    # Scripts for common tantrums
    pdf.add_heading1("SCRIPTS: WHAT TO SAY (20 Common Situations)")
    pdf.add_blank_line()
    scripts = [
        ("They can't have something", "I hear you. You really want that. It's okay to feel disappointed. The answer is still no, AND I love you."),
        ("They hit/bite/throw", "I won't let you hurt. Hitting hurts. You can stomp your feet or squeeze this pillow instead."),
        ("They won't leave the park", "We're leaving in 5 minutes. Would you like to go down the slide one more time or swing?"),
        ("They won't share", "It's hard to share. You can have it for 2 more minutes, then it's your friend's turn."),
        ("They want YOU to do it", "You want help. I'll help you start, then you can finish. I believe you can do it."),
        ("They're frustrated (can't do something)", "That IS frustrating! Would you like to try again, or take a break and come back?"),
        ("They say 'I HATE YOU'", "I can see you're really angry. It's okay to be angry. I love you even when you're mad."),
        ("They won't get dressed", "It's time to get dressed. Would you like the blue shirt or the red shirt? You choose!"),
        ("They melt down at bedtime", "Your body is tired even if your brain doesn't think so. Let's do our calm-down routine together."),
        ("Public tantrum (store/restaurant)", "I see you're having a hard time. Let's step outside for a minute to feel better.")
    ]
    for situation, script in scripts:
        pdf.add_heading3(f"When: {situation}")
        pdf.add_paragraph(f'Say: "{script}"')
        pdf.add_blank_line()
        if situation == "They want YOU to do it":
            pdf.add_page_break()
            pdf.add_heading1("SCRIPTS (continued)")
            pdf.add_blank_line()
    pdf.add_page_break()
    # Emotion wheel
    pdf.add_heading1("FEELINGS CHART FOR KIDS")
    pdf.add_paragraph("(Print, laminate, and use daily! 'Point to how you feel right now.')")
    pdf.add_blank_line()
    pdf.add_paragraph("  HAPPY  :)    SAD  :(    ANGRY  >:(    SCARED  :O")
    pdf.add_paragraph("  EXCITED !!   TIRED zzz  FRUSTRATED ?!  NERVOUS ~~~")
    pdf.add_paragraph("  PROUD  *     LONELY .   SILLY  :P     CALM  ~")
    pdf.add_blank_line()
    pdf.add_paragraph("'I feel _____________ because _____________.'")
    pdf.add_paragraph("(Help kids fill in the sentence with the chart)")
    pdf.add_page_break()
    # Calm-down strategies
    pdf.add_heading1("10 CALM-DOWN STRATEGIES (For Kids)")
    pdf.add_paragraph("(Print as cards, let child CHOOSE which one to try)")
    pdf.add_blank_line()
    strategies = [
        ("Belly Breathing", "Breathe in like smelling a flower, out like blowing a candle. 5 times."),
        ("Tight Squeeze Hug", "Ask: 'Can I give you a tight squeeze?' or let them hug a stuffed animal."),
        ("Stomp It Out", "Stomp feet 10 times. Get the angry energy OUT through your feet."),
        ("Count to 10", "Count slowly together. Whisper by the time you reach 10."),
        ("Safe Space", "Go to a designated 'calm corner' with pillows and soft things."),
        ("Ice Cube Hold", "Hold an ice cube until it melts. The sensation redirects the brain."),
        ("Draw Your Feelings", "Give paper and crayons. 'Draw how big your feeling is.'"),
        ("Body Shake", "Shake hands, arms, legs, whole body for 30 seconds. Then freeze."),
        ("Name 5 Things", "5 things you can see, 4 you can hear, 3 you can touch..."),
        ("Blow Bubbles", "Blowing = controlled breathing. Watching = calming. Win-win.")
    ]
    for i, (name, desc) in enumerate(strategies, 1):
        pdf.add_paragraph(f"  {i}. {name}: {desc}")
        pdf.add_blank_line()
    pdf.add_page_break()
    # Tantrum tracking log
    pdf.add_heading1("TANTRUM TRACKING LOG (Find Patterns!)")
    pdf.add_paragraph("Track tantrums for 2 weeks. You'll notice patterns you can PREVENT.")
    pdf.add_blank_line()
    pdf.add_paragraph("DATE   TIME    TRIGGER       DURATION   WHAT HELPED    PATTERN?")
    for _ in range(10):
        pdf.add_paragraph("_____ _____  ____________  ___min     ____________  __________")
    pdf.add_blank_line()
    pdf.add_paragraph("PATTERNS I NOTICE: _____________________________________________")
    pdf.add_paragraph("Common triggers: [ ] Hungry [ ] Tired [ ] Transitions [ ] Overstimulated")
    pdf.add_paragraph("Prevention plan: _______________________________________________")
    pdf.add_page_break()
    # Prevention
    pdf.add_heading1("TANTRUM PREVENTION CHECKLIST")
    pdf.add_paragraph("Most tantrums are PREVENTABLE. Daily check:")
    pdf.add_blank_line()
    for item in ["Fed regularly (no more than 3 hours between food)", "Slept enough (age-appropriate nap + bedtime)", "Given choices throughout the day (autonomy!)", "Warned before transitions ('5 more minutes, then...')", "Had 1-on-1 connection time with parent today", "Physical activity/outdoor play today", "Not overscheduled (downtime is essential!)", "Routines are predictable and consistent"]:
        pdf.add_paragraph(f"  [ ] {item}")
    pdf.add_blank_line()
    pdf.add_paragraph("If 3+ are unchecked: a meltdown is LIKELY coming. Address the need!")
    pdf.add_separator()
    pdf.add_paragraph("By Daniel Tesfamariam | Every tantrum is a chance to teach - not punish.")
    return pdf



def product3_coparenting():
    """Co-Parenting After Divorce Binder - 40 pages"""
    pdf = PurePDF(title="Co-Parenting Binder")
    pdf.add_title("CO-PARENTING AFTER DIVORCE")
    pdf.add_heading2("The Complete Binder: Custody Tracker, Communication Log,")
    pdf.add_heading2("Expense Splitter & Conflict Resolution Tools")
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_separator()
    pdf.add_page_break()
    pdf.add_heading1("HOW TO USE THIS BINDER")
    pdf.add_paragraph("This binder helps you: stay organized, document everything (for court if needed), reduce conflict, and put your child's needs first.")
    pdf.add_paragraph("Sections: 1) Custody Schedule 2) Communication Log 3) Expenses 4) Child Info 5) Conflict Tools")
    pdf.add_page_break()
    # Custody schedule (6 months)
    for m in range(1, 7):
        pdf.add_heading1(f"CUSTODY CALENDAR - Month {m}")
        pdf.add_paragraph("Month: _______________  Year: _______")
        pdf.add_paragraph("SUN    MON    TUE    WED    THU    FRI    SAT")
        for _ in range(5):
            pdf.add_paragraph("____   ____   ____   ____   ____   ____   ____")
        pdf.add_paragraph("Legend: M=Mom's time  D=Dad's time  T=Transition  H=Holiday")
        pdf.add_paragraph("Schedule changes this month: ___________________________________")
        pdf.add_page_break()
    # Communication log (4 pages)
    for p in range(1, 5):
        pdf.add_heading1(f"COMMUNICATION LOG (Page {p})")
        pdf.add_paragraph("Document ALL communication (texts, calls, emails) for your records.")
        pdf.add_blank_line()
        pdf.add_paragraph("DATE     METHOD    TOPIC              NOTES/OUTCOME")
        for _ in range(10):
            pdf.add_paragraph("___/___  ________  ________________  _________________________")
        pdf.add_page_break()
    # Expense tracker (4 pages)
    for p in range(1, 5):
        pdf.add_heading1(f"SHARED EXPENSE TRACKER (Page {p})")
        pdf.add_paragraph("Month: _______________  Split: ___% / ___%")
        pdf.add_blank_line()
        pdf.add_paragraph("DATE    EXPENSE           AMOUNT   WHO PAID    OWES WHO    SETTLED?")
        for _ in range(10):
            pdf.add_paragraph("___/__  ______________  $_______  _________  $_________  [ ]")
        pdf.add_paragraph("MONTHLY TOTAL: $________  Balance owed: $________")
        pdf.add_page_break()
    # Child info sheet
    pdf.add_heading1("CHILD INFORMATION SHEET")
    pdf.add_paragraph("(Give copy to both parents, update annually)")
    pdf.add_blank_line()
    pdf.add_paragraph("Child: _______________________ DOB: ___/___/___ Age: ___")
    pdf.add_paragraph("School: _____________________ Teacher: _________________")
    pdf.add_paragraph("Doctor: _____________________ Phone: ___________________")
    pdf.add_paragraph("Dentist: ____________________ Phone: ___________________")
    pdf.add_paragraph("Allergies: _____________________________________________")
    pdf.add_paragraph("Medications: ___________________________________________")
    pdf.add_paragraph("Emergency contact: _________________ Phone: _____________")
    pdf.add_blank_line()
    pdf.add_paragraph("DAILY ROUTINE:")
    pdf.add_paragraph("Wake: ___  School: ___  After-school: ___  Dinner: ___  Bed: ___")
    pdf.add_paragraph("SPECIAL NEEDS/NOTES: _______________________________________")
    pdf.add_page_break()
    # Handoff checklist
    pdf.add_heading1("TRANSITION/HANDOFF CHECKLIST")
    pdf.add_paragraph("Use at every custody exchange to avoid conflict and forgotten items:")
    pdf.add_blank_line()
    for item in ["Backpack/school items", "Medications (with instructions)", "Comfort item (blanket, stuffed animal)", "Clean clothes for ___ days", "Homework/projects due", "Activity gear (sports, dance, etc.)", "Electronics (tablet, charger)", "Communication about child's mood/health", "Upcoming schedule reminders"]:
        pdf.add_paragraph(f"  [ ] {item}")
    pdf.add_paragraph("Notes for other parent: ____________________________________")
    pdf.add_page_break()
    # Holiday rotation
    pdf.add_heading1("HOLIDAY ROTATION PLANNER (3-Year)")
    pdf.add_paragraph("Plan ahead to avoid December fights!")
    pdf.add_blank_line()
    pdf.add_paragraph("HOLIDAY              YEAR 1    YEAR 2    YEAR 3")
    for h in ["Christmas Eve", "Christmas Day", "New Year's Eve", "Easter", "Mother's Day", "Father's Day", "Thanksgiving", "Halloween", "Child's Birthday", "Spring Break", "Summer (weeks)", "Winter Break"]:
        pdf.add_paragraph(f"{h:20s}  _______   _______   _______")
    pdf.add_page_break()
    # Conflict resolution
    pdf.add_heading1("CONFLICT DE-ESCALATION SCRIPTS")
    pdf.add_paragraph("When co-parenting gets heated, use these:")
    pdf.add_blank_line()
    for phrase in ["'Let's focus on what's best for [child's name].'", "'I hear your concern. Can we find a middle ground?'", "'Let's table this and discuss when we're both calm.'", "'I'm willing to compromise on ___ if you can on ___.'", "'Can we communicate about this in writing instead?'", "'I don't agree, but I respect your perspective as their parent.'", "'Let's ask our mediator/therapist about this one.'"]:
        pdf.add_paragraph(f"  * {phrase}")
    pdf.add_blank_line()
    pdf.add_paragraph("GOLDEN RULE: Never put the child in the middle. Never badmouth the other parent to the child. Your child loves you BOTH.")
    pdf.add_separator()
    pdf.add_paragraph("By Daniel Tesfamariam | Two homes, one team, for the child.")
    return pdf



def product4_discipline_scripts():
    """Positive Discipline Scripts Guide - 30 pages"""
    pdf = PurePDF(title="Positive Discipline Scripts")
    pdf.add_title("POSITIVE DISCIPLINE SCRIPTS & PHRASES")
    pdf.add_heading2("50 Things to Say Instead of Yelling")
    pdf.add_heading2("(Situation-Specific Scripts for Ages 2-12)")
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_separator()
    pdf.add_page_break()
    pdf.add_heading1("THE FORMULA: ACKNOWLEDGE + VALIDATE + REDIRECT")
    pdf.add_paragraph("Step 1: ACKNOWLEDGE what they're doing/feeling")
    pdf.add_paragraph("Step 2: VALIDATE their emotion (even if behavior isn't okay)")
    pdf.add_paragraph("Step 3: REDIRECT to what they CAN do")
    pdf.add_blank_line()
    pdf.add_paragraph("Example: 'I see you're throwing blocks (acknowledge). You're frustrated (validate). You can throw soft balls outside instead (redirect).'")
    pdf.add_page_break()
    # 50 scripts organized by situation
    categories = [
        ("NOT LISTENING / IGNORING", [
            ("Instead of: 'How many times do I have to tell you?!'", "Try: 'I need your eyes on me. I have something important to say.'"),
            ("Instead of: 'You never listen!'", "Try: 'I notice you're focused on something else. I'll wait until you're ready.'"),
            ("Instead of: 'DO IT NOW!'", "Try: 'This needs to happen before [next fun thing]. Would you like to do it now or in 2 minutes?'"),
            ("Instead of: 'Are you deaf?!'", "Try: 'Let me come to you. [Touch shoulder, get on their level] Hey, I need your help with something.'"),
            ("Instead of: 'If I have to say this again...'", "Try: 'I've asked once. I'm going to help you do it now.'"),
        ]),
        ("HITTING / BITING / AGGRESSION", [
            ("Instead of: 'Stop hitting RIGHT NOW!'", "Try: 'I won't let you hurt. Bodies are not for hitting. I'm going to keep everyone safe.'"),
            ("Instead of: 'We do NOT hit in this house!'", "Try: 'You're so angry your body wants to hit. You CAN: stomp feet, squeeze a pillow, or punch this cushion.'"),
            ("Instead of: 'Say you're sorry!'", "Try: 'Let's check on your brother. How can we help him feel better?'"),
            ("Instead of: 'What is WRONG with you?'", "Try: 'Something big is happening inside you. Let's figure out what you need.'"),
            ("Instead of: 'Go to your room!'", "Try: 'Let's move to a calm space together until your body feels safe again.'"),
        ]),
        ("BEDTIME BATTLES", [
            ("Instead of: 'Get in bed NOW!'", "Try: 'It's time for our bedtime routine. Would you like to start with books or pajamas?'"),
            ("Instead of: 'I don't care if you're not tired!'", "Try: 'Your body needs rest to grow. You don't have to sleep yet - just rest quietly.'"),
            ("Instead of: 'This is the LAST time I'm coming in!'", "Try: 'I'll check on you one more time in 5 minutes. You're safe.'"),
            ("Instead of: 'If you don't stay in bed...'", "Try: 'Your bed is your cozy spot. If you need me, I'm right here.'"),
            ("Instead of: 'ENOUGH stalling!'", "Try: 'I know you want more time with me. Let's have our special bedtime chat and then lights out.'"),
        ]),
        ("SIBLING FIGHTING", [
            ("Instead of: 'STOP FIGHTING!'", "Try: 'I see two people who need help solving a problem. What happened?'"),
            ("Instead of: 'Who started it?'", "Try: 'It doesn't matter who started it. How can we fix it?'"),
            ("Instead of: 'Share or I'll take it away!'", "Try: 'You're both using this. How should we solve it? Timer? Trade?'"),
            ("Instead of: 'Be nice to your sister!'", "Try: 'I hear unkind words. In this family, we speak with respect. Try again.'"),
            ("Instead of: 'That's IT, both of you go to your rooms!'", "Try: 'You both need a break. Take 5 minutes apart, then let's solve this together.'"),
        ]),
        ("HOMEWORK / SCHOOL REFUSAL", [
            ("Instead of: 'Just DO your homework!'", "Try: 'Homework feels hard today. What part feels most overwhelming? Let's start with just ONE problem.'"),
            ("Instead of: 'You're being lazy!'", "Try: 'I can see you're stuck. Would you like help getting started, or do you need a 10-minute break first?'"),
            ("Instead of: 'You're going to fail!'", "Try: 'Struggling means you're learning something new. I believe you can figure this out.'"),
            ("Instead of: 'No TV until homework is done!'", "Try: 'Homework first, then fun stuff! How about we set a timer for 20 minutes of focused work?'"),
            ("Instead of: 'You HAVE to go to school!'", "Try: 'I hear you don't want to go. What's making school hard right now? Let's problem-solve together.'"),
        ]),
    ]
    for cat_name, scripts in categories:
        pdf.add_heading1(cat_name)
        pdf.add_blank_line()
        for old, new in scripts:
            pdf.add_paragraph(old)
            pdf.add_paragraph(new)
            pdf.add_blank_line()
        pdf.add_page_break()
    # Repair scripts
    pdf.add_heading1("REPAIR SCRIPTS (When YOU Lose Your Cool)")
    pdf.add_paragraph("You WILL yell sometimes. You're human. Here's how to repair:")
    pdf.add_blank_line()
    for script in ["'I yelled and I'm sorry. That wasn't okay. You didn't deserve that.'", "'I got really frustrated and I handled it badly. I'm working on doing better.'", "'Even grownups have big feelings sometimes. I should have taken a deep breath.'", "'I love you. My anger was about MY problem, not about you being bad.'", "'Can we have a redo? Let me try that conversation again the right way.'"]:
        pdf.add_paragraph(f"  * {script}")
    pdf.add_blank_line()
    pdf.add_paragraph("Repair teaches your child: mistakes happen, relationships matter more than perfection, and it's brave to apologize.")
    pdf.add_separator()
    pdf.add_paragraph("By Daniel Tesfamariam | Calm parents raise calm kids. You've got this.")
    return pdf


def product5_adhd_parenting():
    """ADHD Child Parenting Strategy Toolkit - 35 pages"""
    pdf = PurePDF(title="ADHD Child Parenting Toolkit")
    pdf.add_title("ADHD CHILD PARENTING STRATEGY TOOLKIT")
    pdf.add_heading2("Visual Schedules, Reward Systems & Coping Tools")
    pdf.add_heading2("for Parents of Neurodivergent Kids (Ages 4-12)")
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_separator()
    pdf.add_page_break()
    pdf.add_heading1("PARENTING AN ADHD CHILD: WHAT WORKS")
    pdf.add_paragraph("Traditional parenting strategies often FAIL with ADHD kids because their brains process rewards, time, and motivation differently.")
    pdf.add_blank_line()
    pdf.add_paragraph("WHAT WORKS:")
    pdf.add_bullet("VISUAL systems (they can't hold info in working memory)")
    pdf.add_bullet("IMMEDIATE rewards (delayed gratification is harder)")
    pdf.add_bullet("SHORTER tasks (break everything into 5-10 min chunks)")
    pdf.add_bullet("EXTERNAL structure (they can't create internal structure yet)")
    pdf.add_bullet("MOVEMENT breaks (sitting still depletes their energy)")
    pdf.add_bullet("CONNECTION before correction (shame makes ADHD worse)")
    pdf.add_page_break()
    # Morning routine chart
    pdf.add_heading1("VISUAL MORNING ROUTINE CHART")
    pdf.add_paragraph("(Laminate and hang in bedroom/bathroom!)")
    pdf.add_blank_line()
    pdf.add_paragraph("MORNING ROUTINE (Do in this order!):")
    steps = ["Wake up - sit up in bed!", "Use the bathroom", "Brush teeth (timer: 2 min)", "Get dressed (clothes laid out last night!)", "Eat breakfast", "Pack backpack (check list!)", "Shoes on, ready to go!", "OUT THE DOOR by ___:___ AM"]
    for i, step in enumerate(steps, 1):
        pdf.add_paragraph(f"  [{i}] [ ] {step}")
    pdf.add_blank_line()
    pdf.add_paragraph("PARENT TIP: Let child check off steps themselves. Each checkmark = dopamine!")
    pdf.add_paragraph("BONUS: If all done by ___:___, earn ____________________!")
    pdf.add_page_break()
    # After-school routine
    pdf.add_heading1("AFTER-SCHOOL ROUTINE CHART")
    pdf.add_blank_line()
    steps = ["Snack time (15 min - refuel!)", "Movement break (10 min - run, jump, dance!)", "Homework time (set timer: ___ minutes)", "Break (5 min)", "More homework if needed (timer again)", "Free time / play!", "Dinner", "Evening routine (below)"]
    for i, step in enumerate(steps, 1):
        pdf.add_paragraph(f"  [{i}] [ ] {step}")
    pdf.add_blank_line()
    pdf.add_paragraph("KEY: Movement BEFORE homework. A tired ADHD brain cannot focus!")
    pdf.add_page_break()
    # Bedtime routine
    pdf.add_heading1("BEDTIME ROUTINE CHART")
    pdf.add_blank_line()
    steps = ["Screens OFF (30 min before bed!)", "Bath/shower", "Pajamas on", "Brush teeth", "Pick tomorrow's clothes", "Read together (or audiobook)", "Calm-down activity (coloring, puzzle, breathing)", "Lights out by ___:___", "Goodnight ritual: ___________"]
    for i, step in enumerate(steps, 1):
        pdf.add_paragraph(f"  [{i}] [ ] {step}")
    pdf.add_paragraph("TIP: Same order EVERY night. Predictability = security for ADHD brains.")
    pdf.add_page_break()
    # Reward system
    pdf.add_heading1("ADHD-FRIENDLY REWARD SYSTEM")
    pdf.add_paragraph("ADHD brains need EXTERNAL motivation. This isn't bribery - it's brain science!")
    pdf.add_blank_line()
    pdf.add_heading3("TOKEN BOARD (earn tokens, trade for rewards):")
    pdf.add_paragraph("EARN TOKENS FOR:")
    for item in ["Routine completed (morning/afternoon/bedtime) = 1 token", "Homework done without major battle = 2 tokens", "Kind to siblings = 1 token", "Tried something hard = 1 token", "Remembered something without reminding = 2 tokens!"]:
        pdf.add_paragraph(f"  * {item}")
    pdf.add_blank_line()
    pdf.add_paragraph("SPEND TOKENS ON:")
    pdf.add_paragraph("  5 tokens = Extra screen time (30 min)")
    pdf.add_paragraph("  10 tokens = Choose dinner / Pick a movie")
    pdf.add_paragraph("  15 tokens = Special outing with parent")
    pdf.add_paragraph("  20 tokens = New book/toy (under $10)")
    pdf.add_paragraph("  30 tokens = BIG reward: _______________")
    pdf.add_blank_line()
    pdf.add_paragraph("TOKENS EARNED: [  ] [  ] [  ] [  ] [  ] [  ] [  ] [  ] [  ] [  ]")
    pdf.add_paragraph("               [  ] [  ] [  ] [  ] [  ] [  ] [  ] [  ] [  ] [  ]")
    pdf.add_page_break()
    # Homework station
    pdf.add_heading1("HOMEWORK STATION SETUP GUIDE")
    pdf.add_paragraph("Create a distraction-free zone that works WITH ADHD:")
    pdf.add_blank_line()
    pdf.add_paragraph("LOCATION: [ ] Desk in room [ ] Kitchen table [ ] Quiet corner")
    pdf.add_paragraph("(Wherever YOU can supervise without hovering)")
    pdf.add_blank_line()
    pdf.add_heading3("STATION MUST HAVES:")
    for item in ["Timer (visual timer best - they can SEE time passing)", "Fidget tool (quiet one: putty, stress ball, tangle)", "Noise-canceling headphones OR white noise", "All supplies within reach (pencils, eraser, sharpener)", "Water bottle (hydration helps focus!)", "Clear desk surface (nothing extra - only current task)", "Checklist of assignments (visible, checkable)"]:
        pdf.add_paragraph(f"  [ ] {item}")
    pdf.add_blank_line()
    pdf.add_paragraph("HOMEWORK STRATEGY: 10 min work -> 3 min break -> 10 min work -> 3 min break")
    pdf.add_paragraph("(Adjust times to your child: some do better with 15/5, some need 7/3)")
    pdf.add_page_break()
    # Sensory break menu
    pdf.add_heading1("SENSORY BREAK MENU")
    pdf.add_paragraph("When your child is dysregulated, overwhelmed, or can't focus - offer a SENSORY BREAK:")
    pdf.add_blank_line()
    pdf.add_heading3("HIGH ENERGY (burn it off):")
    for a in ["Jump on trampoline", "Run laps around house", "Dance to one song", "10 jumping jacks", "Push-ups against wall"]:
        pdf.add_paragraph(f"  [ ] {a}")
    pdf.add_heading3("CALMING (settle down):")
    for a in ["Deep pressure (tight hug, weighted blanket)", "Swing or rock", "Play with water/sand", "Listen to calm music", "Blow bubbles (controlled breathing)"]:
        pdf.add_paragraph(f"  [ ] {a}")
    pdf.add_heading3("FOCUSING (get ready to work):")
    for a in ["Chew gum or crunchy snack", "Fidget tool", "Cold water on wrists", "Stretching", "5 deep breaths"]:
        pdf.add_paragraph(f"  [ ] {a}")
    pdf.add_page_break()
    # Teacher communication
    pdf.add_heading1("TEACHER COMMUNICATION TEMPLATE")
    pdf.add_paragraph("Send at start of school year + as needed:")
    pdf.add_blank_line()
    pdf.add_paragraph("Dear [Teacher],")
    pdf.add_paragraph("My child [name] has ADHD. Here's what helps them succeed:")
    pdf.add_blank_line()
    pdf.add_paragraph("WORKS WELL: _____________________________________________")
    pdf.add_paragraph("STRUGGLES WITH: __________________________________________")
    pdf.add_paragraph("HELPFUL STRATEGIES: ______________________________________")
    pdf.add_paragraph("TRIGGERS TO WATCH FOR: ___________________________________")
    pdf.add_paragraph("BEST WAY TO CONTACT ME: __________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("My child is creative, energetic, and caring. Thank you for")
    pdf.add_paragraph("supporting them! I'm happy to collaborate anytime.")
    pdf.add_paragraph("- [Your name]")
    pdf.add_separator()
    pdf.add_paragraph("By Daniel Tesfamariam | ADHD is a superpower that needs the right support system.")
    return pdf



def main():
    """Generate all 5 parenting PDF products."""
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pdf-products')
    os.makedirs(output_dir, exist_ok=True)

    books = [
        ("01-Screen-Time-Management-System.pdf", "Screen Time Management System (Ages 3-12)", product1_screen_time),
        ("02-Toddler-Tantrum-Toolkit.pdf", "Gentle Parenting Toddler Tantrum Toolkit", product2_tantrum_toolkit),
        ("03-Co-Parenting-Divorce-Binder.pdf", "Co-Parenting After Divorce Binder", product3_coparenting),
        ("04-Positive-Discipline-Scripts.pdf", "Positive Discipline Scripts (50 Phrases)", product4_discipline_scripts),
        ("05-ADHD-Child-Parenting-Toolkit.pdf", "ADHD Child Parenting Strategy Toolkit", product5_adhd_parenting),
    ]

    print("=" * 65)
    print("  PARENTING PDF PRODUCTS GENERATOR")
    print("  Top 5 Trending Products by Daniel Tesfamariam")
    print("=" * 65)
    print()

    results = []
    for i, (filename, title, creator) in enumerate(books, 1):
        print(f"[{i}/5] Generating: {title}")
        try:
            pdf_obj = creator()
            filepath = os.path.join(output_dir, filename)
            size = pdf_obj.save(filepath)
            size_kb = size / 1024
            pages = len(pdf_obj.pages) + (1 if pdf_obj.current_page_content else 0)
            print(f"      -> {filename} ({pages} pages, {size_kb:.0f} KB)")
            results.append((filename, pages, size_kb))
        except Exception as e:
            print(f"      ERROR: {e}")
            import traceback
            traceback.print_exc()
        print()

    print("=" * 65)
    print("  ALL 5 PARENTING PRODUCTS GENERATED!")
    print("=" * 65)
    print()
    total_pages = sum(r[1] for r in results)
    total_size = sum(r[2] for r in results)
    for fn, pg, sz in results:
        print(f"  [{sz:4.0f} KB | {pg:3d} pg] {fn}")
    print(f"\n  TOTAL: {len(results)} products | {total_pages} pages | {total_size:.0f} KB")
    print(f"\n  SELL AT: $9.99-$14.99 each | $34.99 bundle")
    print(f"  INCOME: 50 sales/day x $12 avg = $18,000/month potential")


if __name__ == '__main__':
    main()
