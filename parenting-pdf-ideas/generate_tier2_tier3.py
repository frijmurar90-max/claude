#!/usr/bin/env python3
"""
PARENTING PDF BOOKS - TIER 2 & TIER 3 (Books 6-20)
Generate remaining 15 parenting products
By Daniel Tesfamariam
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'etsy-digital-products-strategy'))
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'etsy-digital-products-strategy', 'generate_pdfs.py')).read())

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pdf-products')
os.makedirs(OUTPUT_DIR, exist_ok=True)


def book6_adhd_parenting():
    """ADHD Child Parenting Strategy Guide"""
    pdf = PurePDF(title="ADHD Child Parenting Guide")
    pdf.add_title("ADHD CHILD PARENTING STRATEGY GUIDE")
    pdf.add_heading2("Visual Schedules, Reward Systems & Coping Tools (Ages 4-12)")
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_separator()
    pdf.add_page_break()

    pdf.add_heading1("WHY TRADITIONAL PARENTING FAILS ADHD KIDS")
    pdf.add_paragraph("ADHD brains process rewards, time, and motivation differently.")
    pdf.add_bullet("VISUAL systems (can't hold info in working memory)")
    pdf.add_bullet("IMMEDIATE rewards (delayed gratification is harder)")
    pdf.add_bullet("SHORTER tasks (break everything into 5-10 min chunks)")
    pdf.add_bullet("MOVEMENT breaks (sitting still depletes energy)")
    pdf.add_bullet("CONNECTION before correction (shame makes ADHD worse)")
    pdf.add_page_break()

    pdf.add_heading1("MORNING ROUTINE VISUAL CHART")
    pdf.add_paragraph("(Laminate and hang in bedroom/bathroom!)")
    for i, step in enumerate([
        "Wake up", "Bathroom", "Brush teeth (2 min timer)",
        "Get dressed (clothes laid out night before)", "Eat breakfast",
        "Pack backpack", "Shoes on", "OUT THE DOOR by ___:___"
    ], 1):
        pdf.add_paragraph(f"  [{i}] [ ] {step}")
    pdf.add_paragraph("TIP: Child checks off steps themselves!")
    pdf.add_page_break()

    pdf.add_heading1("AFTER-SCHOOL ROUTINE")
    for i, step in enumerate([
        "Snack (15 min)", "Movement break (10 min - run/jump/dance)",
        "Homework (timer: ___ min)", "Break (5 min)",
        "Free time / play", "Dinner", "Evening routine"
    ], 1):
        pdf.add_paragraph(f"  [{i}] [ ] {step}")
    pdf.add_paragraph("KEY: Movement BEFORE homework!")
    pdf.add_page_break()


    pdf.add_heading1("BEDTIME ROUTINE")
    for i, step in enumerate([
        "Screens OFF (30 min before bed)", "Bath/shower", "Pajamas",
        "Brush teeth", "Pick tomorrow's clothes", "Read/audiobook",
        "Calm activity", "Lights out ___:___"
    ], 1):
        pdf.add_paragraph(f"  [{i}] [ ] {step}")
    pdf.add_page_break()

    pdf.add_heading1("ADHD-FRIENDLY REWARD SYSTEM")
    pdf.add_heading3("EARN TOKENS:")
    pdf.add_bullet("Routine completed without reminders = 2 tokens")
    pdf.add_bullet("Homework done with timer = 2 tokens")
    pdf.add_bullet("Kind to siblings = 1 token")
    pdf.add_bullet("Remembered task without reminding = 2 tokens")
    pdf.add_bullet("Tried something hard = 1 token")
    pdf.add_heading3("SPEND TOKENS:")
    pdf.add_bullet("5 tokens = Extra screen time (30 min)")
    pdf.add_bullet("10 tokens = Choose dinner menu")
    pdf.add_bullet("15 tokens = Special outing with parent")
    pdf.add_bullet("20 tokens = Small toy or book")
    pdf.add_bullet("30 tokens = BIG reward (you choose!)")
    pdf.add_paragraph("TOKEN TRACKER:")
    pdf.add_paragraph("[  ][  ][  ][  ][  ][  ][  ][  ][  ][  ]")
    pdf.add_paragraph("[  ][  ][  ][  ][  ][  ][  ][  ][  ][  ]")
    pdf.add_paragraph("[  ][  ][  ][  ][  ][  ][  ][  ][  ][  ]")
    pdf.add_page_break()

    pdf.add_heading1("HOMEWORK STATION SETUP")
    pdf.add_bullet("Visual timer (Time Timer or sand timer)")
    pdf.add_bullet("Fidget tool (tangle, putty, or stress ball)")
    pdf.add_bullet("Noise-canceling headphones or white noise")
    pdf.add_bullet("All supplies within arm's reach")
    pdf.add_bullet("Water bottle filled")
    pdf.add_bullet("Clear desk - nothing extra")
    pdf.add_bullet("Assignment checklist visible")
    pdf.add_paragraph("STRATEGY: 10 min work -> 3 min break -> repeat")
    pdf.add_page_break()

    pdf.add_heading1("SENSORY BREAK MENU")
    pdf.add_heading3("HIGH ENERGY:")
    pdf.add_bullet("Jump on trampoline")
    pdf.add_bullet("Run laps outside")
    pdf.add_bullet("Dance to one song")
    pdf.add_bullet("Jumping jacks (20)")
    pdf.add_bullet("Wall push-ups (10)")
    pdf.add_heading3("CALMING:")
    pdf.add_bullet("Tight hug or weighted blanket")
    pdf.add_bullet("Swing for 5 minutes")
    pdf.add_bullet("Water play at sink")
    pdf.add_bullet("Listen to calm music")
    pdf.add_bullet("Blow bubbles (slow breathing)")
    pdf.add_heading3("FOCUSING:")
    pdf.add_bullet("Chew gum")
    pdf.add_bullet("Use fidget tool")
    pdf.add_bullet("Cold water on wrists")
    pdf.add_bullet("Full body stretch")
    pdf.add_bullet("5 deep belly breaths")
    pdf.add_page_break()


    pdf.add_heading1("IEP/504 PLAN PREPARATION WORKSHEET")
    pdf.add_paragraph("Child's name: _____________________________ Grade: ______")
    pdf.add_paragraph("Diagnosis: _____________________________ Date: ___/___/___")
    pdf.add_paragraph("Child's strengths: ___________________________________________")
    pdf.add_paragraph("Areas of challenge: __________________________________________")
    pdf.add_heading3("Accommodations to request:")
    for a in [
        "Extended time on tests", "Preferential seating (near teacher)",
        "Movement breaks every 20 min", "Chunked assignments",
        "Visual schedules provided", "Fidget tools allowed in class",
        "Reduced homework load", "Check-in system with teacher",
        "Copy of notes provided", "Separate testing environment"
    ]:
        pdf.add_paragraph(f"  [ ] {a}")
    pdf.add_page_break()

    pdf.add_heading1("TEACHER COMMUNICATION TEMPLATE")
    pdf.add_paragraph("Dear [Teacher],")
    pdf.add_paragraph("My child [name] has ADHD. Here is what helps them succeed:")
    pdf.add_blank_line()
    pdf.add_paragraph("WORKS WELL: ______________________________________________")
    pdf.add_paragraph("STRUGGLES WITH: ___________________________________________")
    pdf.add_paragraph("TRIGGERS: _________________________________________________")
    pdf.add_paragraph("CALMING STRATEGIES: _______________________________________")
    pdf.add_paragraph("BEST CONTACT METHOD: _____________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("I'd love to schedule a brief meeting to discuss strategies.")
    pdf.add_paragraph("Thank you, [Your name]")
    pdf.add_separator()
    pdf.add_paragraph("By Daniel Tesfamariam | ADHD is a superpower with the right support.")
    return pdf


def book7_teen_communication():
    """Teen & Tween Communication Workbook"""
    pdf = PurePDF(title="Teen Communication Workbook")
    pdf.add_title("TEEN & TWEEN COMMUNICATION WORKBOOK")
    pdf.add_heading2("50 Conversation Starters, Scripts for Hard Topics & Trust-Building Tools")
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_separator()
    pdf.add_page_break()

    pdf.add_heading1("THE TEEN BRAIN: WHY COMMUNICATION BREAKS DOWN")
    pdf.add_paragraph("Teens are not trying to be difficult. Their prefrontal cortex is literally rewiring.")
    pdf.add_paragraph("They need: autonomy, respect, privacy, AND your guidance.")
    pdf.add_paragraph("Rule #1: LISTEN more than you lecture. Ask more than you tell.")
    pdf.add_paragraph("Rule #2: Side-by-side (car, cooking) works better than face-to-face.")
    pdf.add_paragraph("Rule #3: Timing matters. Not when they're hungry, tired, or in front of friends.")
    pdf.add_page_break()


    pdf.add_heading1("50 NON-INVASIVE CONVERSATION STARTERS")
    pdf.add_paragraph("(Use during car rides, walks, or cooking - NOT face-to-face interrogation)")
    starters = [
        "What was the best part of your day?",
        "What stressed you out this week?",
        "If you could change one thing about school?",
        "What are your friends into that you don't understand?",
        "Who do you sit with at lunch?",
        "Is there anyone at school you're worried about?",
        "What do you wish I understood about being a teen?",
        "If you could have any superpower, what and why?",
        "What surprised you recently?",
        "Anything you've been wanting to tell me?",
        "What do you want life to look like in 5 years?",
        "What's hardest about being your age?",
        "Who do you admire and why?",
        "What would you do with $1000?",
        "Any topic you wish we discussed more openly?",
        "Which rule of ours do you think is unfair?",
        "Kindest thing someone did for you recently?",
        "What makes a good friend?",
        "Anything happening online that worries you?",
        "Do you need more space or more togetherness from me?",
        "How would you describe our relationship to friends?",
        "What's your biggest fear right now?",
        "Is there peer pressure to do things you're uncomfortable with?",
        "What would make home feel safer?",
        "What are you most proud of about yourself?",
    ]
    for i, s in enumerate(starters, 1):
        pdf.add_paragraph(f"  {i:2d}. {s}")
    pdf.add_page_break()

    pdf.add_heading1("SCRIPTS FOR HARD CONVERSATIONS")
    topics = [
        ("SOCIAL MEDIA & ONLINE SAFETY",
         "I'm not trying to spy. I want to understand your world. Can you show me what you like about [platform]? What worries me is..."),
        ("DRUGS & ALCOHOL",
         "I know you'll be around this stuff. I'd rather talk honestly than pretend it doesn't exist. What have you seen?"),
        ("SEX & RELATIONSHIPS",
         "This might feel awkward for both of us. I want you to have accurate info and know you can always come to me."),
        ("MENTAL HEALTH",
         "I've noticed you seem [tired/withdrawn/stressed]. I'm not judging. How are you really doing?"),
        ("BULLYING",
         "Has anyone made you feel small or scared? You won't get in trouble. I'm on your team."),
        ("THEIR MISTAKES",
         "Everyone messes up. I'm more interested in what you learned than in punishing you. Tell me what happened."),
    ]
    for topic, script in topics:
        pdf.add_heading3(topic)
        pdf.add_paragraph(f'"{script}"')
        pdf.add_blank_line()
    pdf.add_page_break()


    pdf.add_heading1("PHONE & SOCIAL MEDIA CONTRACT")
    pdf.add_paragraph("This phone belongs to [parent] and is loaned to [teen] under these terms:")
    pdf.add_blank_line()
    for rule in [
        "Phone charges in kitchen at night (not bedroom)",
        "Parent may check phone with notice (not secretly)",
        "No sharing personal info/location with strangers",
        "No downloading apps without discussion",
        "Respond to parent messages within 30 minutes",
        "No phone during family meals or homework",
        "Report any bullying, threats, or uncomfortable contact",
        "Phone privilege reviewed monthly",
        "Consequences for breaking contract: ___________________",
    ]:
        pdf.add_paragraph(f"  [ ] {rule}")
    pdf.add_blank_line()
    pdf.add_paragraph("Signed: Teen _________________ Parent _________________ Date ___/___/___")
    pdf.add_page_break()

    pdf.add_heading1("TRUST-BUILDING CHALLENGES")
    for i, activity in enumerate([
        "Have a no-phone dinner and really talk",
        "Let them teach YOU something they're good at",
        "Share an embarrassing story from YOUR teen years",
        "Give them a decision to make (and respect it)",
        "Write each other a letter about what you appreciate",
        "Do their hobby together (even if you're terrible)",
        "Stay up 30 min later for a real conversation",
        "Apologize for something specific you got wrong",
    ], 1):
        pdf.add_paragraph(f"  {i}. {activity}")
    pdf.add_page_break()

    pdf.add_heading1("WARNING SIGNS: WHEN TO GET PROFESSIONAL HELP")
    pdf.add_paragraph("Trust your gut. If something feels wrong, ACT.")
    pdf.add_heading3("MENTAL HEALTH RED FLAGS:")
    pdf.add_bullet("Withdrawal from friends/family lasting 2+ weeks")
    pdf.add_bullet("Major sleep changes (too much or too little)")
    pdf.add_bullet("Giving away possessions")
    pdf.add_bullet("Talking about being a burden or not wanting to be here")
    pdf.add_bullet("Self-harm signs (cuts, burns, scratches)")
    pdf.add_heading3("SUBSTANCE USE:")
    pdf.add_bullet("Sudden friend group change")
    pdf.add_bullet("Secretive behavior / missing money")
    pdf.add_bullet("Red eyes, slurred speech, new smells")
    pdf.add_blank_line()
    pdf.add_paragraph("CRISIS: 988 Suicide & Crisis Lifeline (call or text 988)")
    pdf.add_separator()
    pdf.add_paragraph("By Daniel Tesfamariam | The teen who pushes you away needs you most.")
    return pdf


def book8_montessori_home():
    """Montessori Home Activities Guide"""
    pdf = PurePDF(title="Montessori Home Activities Guide")
    pdf.add_title("MONTESSORI HOME ACTIVITIES GUIDE")
    pdf.add_heading2("100 Activities by Age Using Household Items")
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_separator()
    pdf.add_page_break()


    pdf.add_heading1("MONTESSORI PRINCIPLES FOR HOME")
    pdf.add_bullet("Follow the child - observe their interests")
    pdf.add_bullet("Prepare the environment - child-sized, accessible")
    pdf.add_bullet("Freedom within limits - choices, not chaos")
    pdf.add_bullet("Hands-on learning - concrete before abstract")
    pdf.add_bullet("Independence - 'Help me do it myself'")
    pdf.add_bullet("Real work - practical life skills are learning")
    pdf.add_page_break()

    pdf.add_heading1("AGES 0-12 MONTHS: SENSORY EXPLORATION")
    activities_baby = [
        "Treasure basket with safe household objects (wooden spoon, fabric, brush)",
        "Black and white contrast cards (newborn to 3 months)",
        "Tracking a slow-moving object with eyes",
        "Tummy time with a mirror",
        "Grasping rattles and fabric squares",
        "Exploring different textures (smooth, rough, soft, bumpy)",
        "Listening to different sounds (bells, crinkle paper, music)",
        "Pulling tissues from a box (great motor practice!)",
        "Stacking and knocking down soft blocks",
        "Water play in shallow container with supervision",
    ]
    for i, a in enumerate(activities_baby, 1):
        pdf.add_paragraph(f"  {i:2d}. {a}")
    pdf.add_page_break()

    pdf.add_heading1("AGES 1-2 YEARS: PRACTICAL LIFE")
    activities_toddler = [
        "Transferring beans between bowls with spoon",
        "Pouring water between small pitchers",
        "Opening and closing containers (jars, boxes)",
        "Putting balls into a container and dumping",
        "Simple puzzles (knob puzzles, 2-3 pieces)",
        "Wiping table with small sponge",
        "Matching socks from laundry",
        "Peeling a banana or orange",
        "Sweeping with child-sized broom",
        "Putting shoes in shoe rack",
        "Watering a plant with small watering can",
        "Sorting objects by color into bowls",
        "Threading large beads on thick string",
        "Washing vegetables in water",
        "Carrying breakable items carefully (builds focus)",
    ]
    for i, a in enumerate(activities_toddler, 1):
        pdf.add_paragraph(f"  {i:2d}. {a}")
    pdf.add_page_break()

    pdf.add_heading1("AGES 2-3 YEARS: INDEPENDENCE SKILLS")
    activities_2 = [
        "Dressing self (elastic pants, velcro shoes)",
        "Pouring own water from small pitcher",
        "Spreading butter/cream cheese on bread",
        "Cutting soft food with butter knife",
        "Washing hands independently (step stool at sink)",
        "Folding small washcloths",
        "Setting table (placemat with outlines)",
        "Caring for a pet (filling water bowl)",
        "Sorting silverware from dishwasher",
        "Planting seeds in soil",
        "Cutting with scissors (playdough or paper strips)",
        "Lacing cards or threading pasta",
        "Matching shapes and colors",
        "Building with blocks (copying simple patterns)",
        "Washing dishes in soapy water",
    ]
    for i, a in enumerate(activities_2, 1):
        pdf.add_paragraph(f"  {i:2d}. {a}")
    pdf.add_page_break()


    pdf.add_heading1("AGES 3-4 YEARS: CONCENTRATION & ORDER")
    activities_3 = [
        "Pouring from pitcher to multiple cups (tea party)",
        "Buttoning and zipping jackets",
        "Cutting food for snack with supervision",
        "Sweeping floor with dustpan",
        "Polishing shoes or silver items",
        "Sewing with large blunt needle on burlap",
        "Washing windows with spray bottle and cloth",
        "Arranging flowers in a vase",
        "Making simple recipes (no-bake cookies, salad)",
        "Sorting objects by multiple attributes (size AND color)",
        "Building complex block towers",
        "Tracing shapes and letters in sand/salt tray",
        "Caring for plants (watering, removing dead leaves)",
        "Folding own laundry",
        "Making bed independently",
    ]
    for i, a in enumerate(activities_3, 1):
        pdf.add_paragraph(f"  {i:2d}. {a}")
    pdf.add_page_break()

    pdf.add_heading1("AGES 4-6 YEARS: ACADEMIC READINESS")
    activities_4 = [
        "Sandpaper letters - tracing with fingers",
        "Moveable alphabet - building words",
        "Counting with real objects (beans, buttons)",
        "Addition with physical items",
        "Reading simple 3-letter words",
        "Writing in a journal (drawing + labeling)",
        "Geography - continent puzzle map",
        "Science experiments (sink/float, magnet testing)",
        "Cooking with measuring cups (math in action)",
        "Creating a nature journal",
        "Time telling with analog clock",
        "Money recognition and counting coins",
        "Simple chapter books (read aloud together)",
        "Board games requiring strategy",
        "Writing letters to family members",
    ]
    for i, a in enumerate(activities_4, 1):
        pdf.add_paragraph(f"  {i:2d}. {a}")
    pdf.add_page_break()

    pdf.add_heading1("SETTING UP YOUR MONTESSORI HOME")
    pdf.add_heading3("Kitchen:")
    pdf.add_bullet("Low shelf with child's dishes and cups")
    pdf.add_bullet("Step stool at counter")
    pdf.add_bullet("Water pitcher they can reach")
    pdf.add_bullet("Healthy snacks at their level")
    pdf.add_heading3("Bedroom:")
    pdf.add_bullet("Floor bed or low bed (independence)")
    pdf.add_bullet("Clothes in low drawers they can reach")
    pdf.add_bullet("Mirror at their height")
    pdf.add_bullet("Limited toys, rotated weekly")
    pdf.add_heading3("Bathroom:")
    pdf.add_bullet("Step stool at sink and toilet")
    pdf.add_bullet("Towel hook at child height")
    pdf.add_bullet("Toothbrush and soap accessible")
    pdf.add_heading3("Living areas:")
    pdf.add_bullet("Low bookshelves (books face out)")
    pdf.add_bullet("Art supplies accessible")
    pdf.add_bullet("Child-sized table and chair")
    pdf.add_bullet("Nature table for seasonal collections")
    pdf.add_separator()
    pdf.add_paragraph("By Daniel Tesfamariam | The child who can do for themselves, will.")
    return pdf


def book9_potty_training():
    """Potty Training Complete System"""
    pdf = PurePDF(title="Potty Training Complete System")
    pdf.add_title("POTTY TRAINING COMPLETE SYSTEM")
    pdf.add_heading2("3-Day Method, Reward Charts & Progress Tracking")
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_separator()
    pdf.add_page_break()


    pdf.add_heading1("READINESS SIGNS CHECKLIST")
    pdf.add_paragraph("Your child may be ready if they show 5+ of these signs:")
    for sign in [
        "Stays dry for 2+ hours at a time",
        "Shows interest in the toilet/others using it",
        "Can pull pants up and down",
        "Tells you when diaper is wet or dirty",
        "Hides to poop (shows awareness)",
        "Can follow simple 2-step instructions",
        "Shows desire for independence",
        "Has regular bowel movements",
        "Dislikes feeling wet/dirty",
        "Can sit still for 2-3 minutes",
    ]:
        pdf.add_paragraph(f"  [ ] {sign}")
    pdf.add_paragraph(f"Signs checked: ___/10  Ready? [ ] YES  [ ] WAIT 2-4 WEEKS")
    pdf.add_page_break()

    pdf.add_heading1("PREPARATION (1 Week Before)")
    pdf.add_heading3("Shopping List:")
    pdf.add_bullet("Potty chair OR toilet seat insert")
    pdf.add_bullet("Step stool for regular toilet")
    pdf.add_bullet("10-15 pairs of underwear (let child choose!)")
    pdf.add_bullet("Easy-on/off pants (elastic waist, no buttons)")
    pdf.add_bullet("Reward stickers or small treats")
    pdf.add_bullet("Waterproof mattress cover")
    pdf.add_bullet("Extra cleaning supplies")
    pdf.add_bullet("Books about potty training (for child)")
    pdf.add_heading3("Environment Setup:")
    pdf.add_bullet("Place potty in bathroom (or living area initially)")
    pdf.add_bullet("Put step stool at toilet and sink")
    pdf.add_bullet("Stock bathroom with books/toys for sitting")
    pdf.add_bullet("Clear your schedule for 3 full days")
    pdf.add_page_break()

    pdf.add_heading1("THE 3-DAY METHOD")
    pdf.add_heading2("DAY 1: Introduction")
    pdf.add_paragraph("Morning: Say goodbye to diapers together (throw away/donate)")
    pdf.add_paragraph("Put child in underwear only (no pants easier at first)")
    pdf.add_paragraph("Every 15-20 minutes: 'Let's try sitting on the potty!'")
    pdf.add_paragraph("Watch for signs: squirming, holding, hiding, stopping play")
    pdf.add_paragraph("CELEBRATE every success - even just sitting!")
    pdf.add_paragraph("Accidents WILL happen. Stay calm: 'Oops! Pee goes in the potty.'")
    pdf.add_paragraph("Fluid loading: extra water/juice = more practice opportunities")
    pdf.add_blank_line()
    pdf.add_heading2("DAY 2: Building Awareness")
    pdf.add_paragraph("Extend time between reminders to 30 minutes")
    pdf.add_paragraph("Ask: 'Are your underwear dry? Let's keep them dry!'")
    pdf.add_paragraph("Child may start self-initiating today")
    pdf.add_paragraph("Fewer accidents expected but still normal")
    pdf.add_paragraph("Short outing (30 min max) with potty reminder before leaving")
    pdf.add_blank_line()
    pdf.add_heading2("DAY 3: Independence")
    pdf.add_paragraph("Let child take the lead - remind less often")
    pdf.add_paragraph("Longer outing with portable potty or planned bathroom stops")
    pdf.add_paragraph("Practice pants up and down independently")
    pdf.add_paragraph("Handwashing routine established")
    pdf.add_page_break()


    pdf.add_heading1("REWARD CHART")
    pdf.add_paragraph("Place a sticker for each success!")
    pdf.add_paragraph("DAY 1:  [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]")
    pdf.add_paragraph("DAY 2:  [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]")
    pdf.add_paragraph("DAY 3:  [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]")
    pdf.add_paragraph("DAY 4:  [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]")
    pdf.add_paragraph("DAY 5:  [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]")
    pdf.add_paragraph("DAY 6:  [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]")
    pdf.add_paragraph("DAY 7:  [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]")
    pdf.add_blank_line()
    pdf.add_paragraph("MILESTONE REWARDS:")
    pdf.add_paragraph("  5 stickers = ___________________________")
    pdf.add_paragraph("  10 stickers = __________________________")
    pdf.add_paragraph("  20 stickers = __________________________")
    pdf.add_paragraph("  Full week dry = ________________________")
    pdf.add_page_break()

    pdf.add_heading1("WEEKLY PROGRESS TRACKER")
    pdf.add_paragraph("Week of: ___/___/___ to ___/___/___")
    pdf.add_blank_line()
    for day in ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]:
        pdf.add_paragraph(f"  {day}: Successes: ___ Accidents: ___ Initiated: [ ] Dry nap: [ ]")
    pdf.add_blank_line()
    pdf.add_paragraph("Notes: ___________________________________________________")
    pdf.add_page_break()

    pdf.add_heading1("TROUBLESHOOTING COMMON ISSUES")
    pdf.add_heading3("Refuses to sit on potty:")
    pdf.add_bullet("Don't force! Let them sit with clothes on first")
    pdf.add_bullet("Try during a preferred activity (tablet, book)")
    pdf.add_bullet("Make it fun - sing songs, blow bubbles while sitting")
    pdf.add_heading3("Pees fine but won't poop on potty:")
    pdf.add_bullet("This is VERY common - poop takes longer to master")
    pdf.add_bullet("Offer a diaper for poop if needed (then gradually transition)")
    pdf.add_bullet("Ensure feet are supported (stool) for proper positioning")
    pdf.add_heading3("Regression after weeks of success:")
    pdf.add_bullet("Check for: new sibling, move, stress, illness")
    pdf.add_bullet("Go back to more frequent reminders temporarily")
    pdf.add_bullet("NEVER shame or punish - it makes it worse")
    pdf.add_heading3("Nighttime dryness:")
    pdf.add_bullet("Separate from daytime - can take months to years longer")
    pdf.add_bullet("Use waterproof mattress cover and pull-ups at night")
    pdf.add_bullet("Limit fluids 1 hour before bed")
    pdf.add_bullet("Not developmental until age 5-6 for many children")
    pdf.add_separator()
    pdf.add_paragraph("By Daniel Tesfamariam | Patience is the #1 potty training tool.")
    return pdf


def book10_anxiety_emotions():
    """Anxiety & Big Emotions Workbook for Kids"""
    pdf = PurePDF(title="Anxiety & Big Emotions Workbook")
    pdf.add_title("ANXIETY & BIG EMOTIONS WORKBOOK FOR KIDS")
    pdf.add_heading2("Worry Monster, Breathing Techniques & Coping Strategies")
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_separator()
    pdf.add_page_break()


    pdf.add_heading1("UNDERSTANDING BIG EMOTIONS")
    pdf.add_paragraph("All feelings are okay. All behaviors are NOT okay.")
    pdf.add_paragraph("It's okay to feel angry. It's NOT okay to hit.")
    pdf.add_paragraph("It's okay to feel scared. It's NOT okay to scream at others.")
    pdf.add_paragraph("It's okay to feel sad. It's NOT okay to break things.")
    pdf.add_blank_line()
    pdf.add_heading3("THE FEELINGS THERMOMETER:")
    pdf.add_paragraph("  5 = EXPLODING (out of control, can't think)")
    pdf.add_paragraph("  4 = VERY HOT (about to lose it)")
    pdf.add_paragraph("  3 = WARM (getting frustrated/worried)")
    pdf.add_paragraph("  2 = COOL (a little uncomfortable)")
    pdf.add_paragraph("  1 = CALM (feeling good, in control)")
    pdf.add_paragraph("Right now I'm at: ___ My goal is to get to: ___")
    pdf.add_page_break()

    pdf.add_heading1("MEET YOUR WORRY MONSTER")
    pdf.add_paragraph("Everyone has a Worry Monster in their brain. It's trying to keep you SAFE,")
    pdf.add_paragraph("but sometimes it gets TOO loud about things that aren't actually dangerous.")
    pdf.add_blank_line()
    pdf.add_paragraph("My Worry Monster's name: _________________________")
    pdf.add_paragraph("What it looks like: _______________________________")
    pdf.add_paragraph("What it usually says to me: _______________________")
    pdf.add_paragraph("__________________________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("TALKING BACK TO YOUR WORRY MONSTER:")
    pdf.add_paragraph('  Worry says: "Something bad will happen!"')
    pdf.add_paragraph('  I say: "Maybe, maybe not. I can handle it."')
    pdf.add_paragraph('  Worry says: "Everyone is looking at you!"')
    pdf.add_paragraph('  I say: "Most people are thinking about themselves."')
    pdf.add_paragraph('  Worry says: "You can\'t do it!"')
    pdf.add_paragraph('  I say: "I\'ve done hard things before. I can try."')
    pdf.add_page_break()

    pdf.add_heading1("5 BREATHING TECHNIQUES FOR KIDS")
    pdf.add_heading3("1. BALLOON BREATH:")
    pdf.add_paragraph("Breathe in through nose (inflate your belly like a balloon)")
    pdf.add_paragraph("Breathe out through mouth slowly (deflate the balloon)")
    pdf.add_paragraph("Repeat 5 times")
    pdf.add_heading3("2. SQUARE BREATHING:")
    pdf.add_paragraph("Breathe in for 4 counts | Hold for 4 counts")
    pdf.add_paragraph("Breathe out for 4 counts | Hold for 4 counts")
    pdf.add_paragraph("Trace a square in the air while you do it")
    pdf.add_heading3("3. FLOWER & CANDLE:")
    pdf.add_paragraph("Smell the flower (breathe in through nose)")
    pdf.add_paragraph("Blow out the candle (breathe out through mouth)")
    pdf.add_heading3("4. 5-4-3-2-1 GROUNDING:")
    pdf.add_paragraph("5 things you SEE | 4 things you TOUCH")
    pdf.add_paragraph("3 things you HEAR | 2 things you SMELL | 1 thing you TASTE")
    pdf.add_heading3("5. STARFISH BREATH:")
    pdf.add_paragraph("Spread fingers like a starfish. Trace up each finger (breathe in)")
    pdf.add_paragraph("Trace down each finger (breathe out). 5 breaths total!")
    pdf.add_page_break()


    pdf.add_heading1("MY COPING TOOLBOX")
    pdf.add_paragraph("When I feel BIG emotions, I can try:")
    pdf.add_heading3("BODY tools:")
    pdf.add_bullet("Jump 10 times")
    pdf.add_bullet("Squeeze a stress ball")
    pdf.add_bullet("Run in place")
    pdf.add_bullet("Push against a wall (10 seconds)")
    pdf.add_bullet("Drink cold water")
    pdf.add_heading3("MIND tools:")
    pdf.add_bullet("Count backwards from 10")
    pdf.add_bullet("Name 5 animals")
    pdf.add_bullet("Think of my favorite place")
    pdf.add_bullet("Remember: this feeling will pass")
    pdf.add_bullet("Talk to my worry monster")
    pdf.add_heading3("COMFORT tools:")
    pdf.add_bullet("Hug my stuffed animal")
    pdf.add_bullet("Go to my calm corner")
    pdf.add_bullet("Listen to my calm playlist")
    pdf.add_bullet("Draw how I feel")
    pdf.add_bullet("Ask for a hug")
    pdf.add_page_break()

    pdf.add_heading1("CALM CORNER SETUP GUIDE")
    pdf.add_paragraph("Every child needs a safe place to go when emotions get big:")
    pdf.add_heading3("What to include:")
    pdf.add_bullet("Soft pillows or beanbag")
    pdf.add_bullet("Noise-canceling headphones")
    pdf.add_bullet("Feelings chart (posted on wall)")
    pdf.add_bullet("Breathing tool (pinwheel, bubbles)")
    pdf.add_bullet("Fidget tools (putty, tangle)")
    pdf.add_bullet("Weighted stuffed animal")
    pdf.add_bullet("Journal or drawing pad")
    pdf.add_bullet("Calm-down jar (glitter + water)")
    pdf.add_heading3("Rules for the calm corner:")
    pdf.add_bullet("This is NOT a punishment")
    pdf.add_bullet("You can go here anytime you need it")
    pdf.add_bullet("Stay as long as you need")
    pdf.add_bullet("Come out when you feel at level 1-2")
    pdf.add_page_break()

    pdf.add_heading1("DAILY FEELINGS CHECK-IN")
    pdf.add_paragraph("Circle how you feel today:")
    pdf.add_paragraph("HAPPY  SAD  ANGRY  SCARED  EXCITED  FRUSTRATED  CALM  LONELY")
    pdf.add_blank_line()
    pdf.add_paragraph("My feeling level (1-5): ___")
    pdf.add_paragraph("What happened: ___________________________________________")
    pdf.add_paragraph("What I did to cope: ______________________________________")
    pdf.add_paragraph("Did it help? [ ] YES  [ ] A LITTLE  [ ] NO")
    pdf.add_paragraph("Tomorrow I want to feel: __________________________________")
    pdf.add_page_break()

    pdf.add_heading1("WORRY JAR EXERCISE")
    pdf.add_paragraph("Write each worry on a slip of paper. Put it in your Worry Jar.")
    pdf.add_paragraph("Once a week, open the jar with a parent and sort:")
    pdf.add_blank_line()
    pdf.add_paragraph("WORRY: ___________________________________________________")
    pdf.add_paragraph("Did it come true?  [ ] YES  [ ] NO")
    pdf.add_paragraph("Can I control it?   [ ] YES  [ ] NO")
    pdf.add_paragraph("Action I can take:  _______________________________________")
    pdf.add_paragraph("Let it go?          [ ] YES (tear it up!)")
    pdf.add_blank_line()
    pdf.add_paragraph("WORRY: ___________________________________________________")
    pdf.add_paragraph("Did it come true?  [ ] YES  [ ] NO")
    pdf.add_paragraph("Can I control it?   [ ] YES  [ ] NO")
    pdf.add_paragraph("Action I can take:  _______________________________________")
    pdf.add_paragraph("Let it go?          [ ] YES (tear it up!)")
    pdf.add_separator()
    pdf.add_paragraph("By Daniel Tesfamariam | Feelings are visitors. Let them come and go.")
    return pdf


def book11_baby_sleep():
    """Baby Sleep Training Guide"""
    pdf = PurePDF(title="Baby Sleep Training Guide")
    pdf.add_title("BABY SLEEP TRAINING GUIDE")
    pdf.add_heading2("Methods, Wake Windows, Nap Transitions & Schedules")
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_separator()
    pdf.add_page_break()


    pdf.add_heading1("WAKE WINDOWS BY AGE")
    pdf.add_paragraph("A wake window is how long baby can stay awake before needing sleep:")
    pdf.add_blank_line()
    pdf.add_paragraph("  Newborn (0-4 wks):   45-60 minutes")
    pdf.add_paragraph("  1-2 months:          60-90 minutes")
    pdf.add_paragraph("  3-4 months:          75-120 minutes")
    pdf.add_paragraph("  5-7 months:          2-3 hours")
    pdf.add_paragraph("  8-10 months:         2.5-3.5 hours")
    pdf.add_paragraph("  11-14 months:        3-4 hours")
    pdf.add_paragraph("  15-18 months:        4-5.5 hours")
    pdf.add_paragraph("  2-3 years:           5-6 hours")
    pdf.add_blank_line()
    pdf.add_paragraph("TIP: Watch for sleepy cues - yawning, eye rubbing, fussiness")
    pdf.add_page_break()

    pdf.add_heading1("SLEEP TRAINING METHODS COMPARISON")
    pdf.add_heading2("1. FERBER METHOD (Graduated Extinction)")
    pdf.add_paragraph("How it works: Put baby down awake, check at increasing intervals")
    pdf.add_paragraph("Day 1: Check at 3, 5, 10, 10, 10 min...")
    pdf.add_paragraph("Day 2: Check at 5, 10, 12, 12, 12 min...")
    pdf.add_paragraph("Day 3: Check at 10, 12, 15, 15, 15 min...")
    pdf.add_paragraph("During checks: Brief verbal comfort, no picking up. 30 seconds max.")
    pdf.add_paragraph("Best for: 5+ months, parents who want structure, works in 3-7 days")
    pdf.add_blank_line()
    pdf.add_heading2("2. GENTLE/CHAIR METHOD")
    pdf.add_paragraph("How it works: Sit in chair next to crib, gradually move farther away")
    pdf.add_paragraph("Days 1-3: Chair right next to crib, pat/shush")
    pdf.add_paragraph("Days 4-6: Chair halfway across room")
    pdf.add_paragraph("Days 7-9: Chair by the door")
    pdf.add_paragraph("Days 10-12: Chair outside door (in hallway)")
    pdf.add_paragraph("Best for: Anxious babies, parents who can't hear crying, takes 2-3 weeks")
    pdf.add_blank_line()
    pdf.add_heading2("3. PICK UP/PUT DOWN")
    pdf.add_paragraph("How it works: Pick up when crying, put down when calm. Repeat.")
    pdf.add_paragraph("Best for: Under 6 months, parents who want very gentle approach")
    pdf.add_paragraph("Takes longest: 2-4 weeks typically")
    pdf.add_page_break()

    pdf.add_heading1("BEDTIME ROUTINE (MUST BE CONSISTENT)")
    pdf.add_paragraph("Same order, same time, every single night. 20-30 minutes total:")
    pdf.add_blank_line()
    pdf.add_paragraph("  Time: ___:___ Start routine")
    pdf.add_paragraph("  [ ] Bath (not necessary every night)")
    pdf.add_paragraph("  [ ] Pajamas and diaper")
    pdf.add_paragraph("  [ ] Feed (keep baby awake!)")
    pdf.add_paragraph("  [ ] Book (1-2 short books)")
    pdf.add_paragraph("  [ ] Song or white noise on")
    pdf.add_paragraph("  [ ] Phrase: 'I love you. Time to sleep.'")
    pdf.add_paragraph("  [ ] Place in crib DROWSY BUT AWAKE")
    pdf.add_paragraph("  Time: ___:___ Baby in crib")
    pdf.add_blank_line()
    pdf.add_paragraph("KEY: Baby must go INTO crib awake so they learn to fall asleep there!")
    pdf.add_page_break()


    pdf.add_heading1("NAP TRANSITIONS GUIDE")
    pdf.add_heading3("4 to 3 naps (around 4-5 months):")
    pdf.add_bullet("Drop the late afternoon catnap")
    pdf.add_bullet("Move bedtime earlier temporarily")
    pdf.add_heading3("3 to 2 naps (around 7-9 months):")
    pdf.add_bullet("Drop the third nap when it interferes with bedtime")
    pdf.add_bullet("Stretch wake windows gradually (15 min per day)")
    pdf.add_heading3("2 to 1 nap (around 13-18 months):")
    pdf.add_bullet("THIS IS THE HARDEST TRANSITION")
    pdf.add_bullet("Signs of readiness: fighting one nap consistently for 2+ weeks")
    pdf.add_bullet("Move single nap to 12:00-12:30pm")
    pdf.add_bullet("Early bedtime for 2-4 weeks during transition")
    pdf.add_heading3("1 to 0 naps (around 3-4 years):")
    pdf.add_bullet("Replace nap with quiet time (books, puzzles in room)")
    pdf.add_bullet("Move bedtime 30-60 min earlier")
    pdf.add_page_break()

    pdf.add_heading1("SLEEP LOG")
    pdf.add_paragraph("Date: ___/___/___")
    pdf.add_paragraph("Nap 1: ___:___ to ___:___ (length: ___ min)")
    pdf.add_paragraph("Nap 2: ___:___ to ___:___ (length: ___ min)")
    pdf.add_paragraph("Nap 3: ___:___ to ___:___ (length: ___ min)")
    pdf.add_paragraph("Bedtime routine started: ___:___")
    pdf.add_paragraph("In crib: ___:___  Fell asleep: ___:___")
    pdf.add_paragraph("Night wakings: ___:___ | ___:___ | ___:___ | ___:___")
    pdf.add_paragraph("Morning wake: ___:___")
    pdf.add_paragraph("Total night sleep: ___ hrs  Total day sleep: ___ hrs")
    pdf.add_paragraph("Notes: _______________________________________________")
    pdf.add_page_break()

    pdf.add_heading1("TROUBLESHOOTING SLEEP ISSUES")
    pdf.add_heading3("Taking 30+ min to fall asleep:")
    pdf.add_bullet("Bedtime may be too early - push later by 15 min")
    pdf.add_bullet("Not enough physical activity during the day")
    pdf.add_heading3("Waking at 5am:")
    pdf.add_bullet("Room may not be dark enough (blackout curtains!)")
    pdf.add_bullet("Last nap may be too late or too long")
    pdf.add_bullet("Bedtime may be too late (overtired = early waking)")
    pdf.add_heading3("Waking every 1-2 hours:")
    pdf.add_bullet("May need to learn independent sleep skills")
    pdf.add_bullet("Check: hungry? teething? sick? too hot/cold?")
    pdf.add_heading3("Fighting naps:")
    pdf.add_bullet("Wake window may be too short or too long")
    pdf.add_bullet("Try a mini-routine before nap (book + song)")
    pdf.add_bullet("Nap environment: dark, cool, white noise")
    pdf.add_separator()
    pdf.add_paragraph("By Daniel Tesfamariam | Good sleep is a skill. You can teach it with love.")
    return pdf


def book12_sibling_rivalry():
    """Sibling Rivalry Resolution Toolkit"""
    pdf = PurePDF(title="Sibling Rivalry Resolution Toolkit")
    pdf.add_title("SIBLING RIVALRY RESOLUTION TOOLKIT")
    pdf.add_heading2("Conflict Scripts, Bonding Activities & Peace Corner Setup")
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_separator()
    pdf.add_page_break()


    pdf.add_heading1("WHY SIBLINGS FIGHT")
    pdf.add_paragraph("Sibling conflict is NORMAL and even healthy when managed well.")
    pdf.add_bullet("Competition for parent attention (the #1 driver)")
    pdf.add_bullet("Developmental differences (older vs younger abilities)")
    pdf.add_bullet("Temperament clashes (introvert vs extrovert)")
    pdf.add_bullet("Boredom and proximity")
    pdf.add_bullet("Feeling unfairly treated")
    pdf.add_paragraph("Your goal is NOT to eliminate conflict but to teach conflict resolution.")
    pdf.add_page_break()

    pdf.add_heading1("CONFLICT RESOLUTION SCRIPTS FOR PARENTS")
    pdf.add_heading3("When they're fighting over a toy:")
    pdf.add_paragraph('"I see two kids who both want the same toy. What can we do?"')
    pdf.add_paragraph("Options: Timer (5 min each) | Trade for something else | Play together")
    pdf.add_blank_line()
    pdf.add_heading3("When one hits/hurts the other:")
    pdf.add_paragraph('"Stop. Hitting is not okay. [To victim]: Are you okay? [To hitter]:"')
    pdf.add_paragraph('"I can see you were angry. Hitting hurts. What could you do instead?"')
    pdf.add_blank_line()
    pdf.add_heading3("When they tattle:")
    pdf.add_paragraph('"Is someone hurt or in danger? No? Then can you try solving it first?"')
    pdf.add_paragraph('"Tell your brother how you feel using I-statements."')
    pdf.add_blank_line()
    pdf.add_heading3("When they say 'It's not fair!':")
    pdf.add_paragraph('"Fair doesn\'t mean everyone gets the same. It means everyone gets what they NEED."')
    pdf.add_paragraph('"What do YOU need right now?"')
    pdf.add_blank_line()
    pdf.add_heading3("When the older child is mean to the younger:")
    pdf.add_paragraph('"I know it can be hard having a little sibling. They look up to you so much."')
    pdf.add_paragraph('"Would you like some time alone? Or some just-you-and-me time?"')
    pdf.add_page_break()

    pdf.add_heading1("THE PEACE CORNER (Conflict Resolution Station)")
    pdf.add_paragraph("Set up a designated space where siblings go to resolve conflicts:")
    pdf.add_heading3("What to include:")
    pdf.add_bullet("Peace agreement poster (rules posted)")
    pdf.add_bullet("Timer (for taking turns talking)")
    pdf.add_bullet("Feelings faces chart")
    pdf.add_bullet("Problem-solving wheel (spin for solutions)")
    pdf.add_bullet("'I feel...' sentence starter cards")
    pdf.add_heading3("Peace Corner Rules:")
    pdf.add_paragraph("  1. One person talks at a time (hold the talking stick)")
    pdf.add_paragraph("  2. Use 'I feel...' not 'You always...'")
    pdf.add_paragraph("  3. Listen without interrupting")
    pdf.add_paragraph("  4. Brainstorm solutions together")
    pdf.add_paragraph("  5. Agree on one solution to try")
    pdf.add_paragraph("  6. Shake hands or high-five")
    pdf.add_page_break()

    pdf.add_heading1("SIBLING BONDING ACTIVITIES (Do Together)")
    pdf.add_heading3("Cooperative (not competitive) activities:")
    for i, activity in enumerate([
        "Build a blanket fort together",
        "Cook or bake something as a team",
        "Create a sibling secret handshake",
        "Make a time capsule together",
        "Collaborate on an art project",
        "Put on a show for parents",
        "Build something with blocks/LEGO together",
        "Start a 'sibling business' (lemonade stand)",
        "Read to each other before bed",
        "Work on a puzzle together",
        "Plan a surprise for a parent together",
        "Create a comic strip starring both of them",
    ], 1):
        pdf.add_paragraph(f"  {i:2d}. {activity}")
    pdf.add_page_break()

    pdf.add_heading1("PREVENTING FIGHTS: DAILY STRATEGIES")
    pdf.add_bullet("Give each child 10 minutes of individual attention daily")
    pdf.add_bullet("Notice and praise when they get along (not just when they fight)")
    pdf.add_bullet("Avoid comparing ('Your sister never does that!')")
    pdf.add_bullet("Give specific roles ('You're the mixer, you're the pourer')")
    pdf.add_bullet("Separate when overstimulated (before the meltdown)")
    pdf.add_bullet("Let them solve minor conflicts themselves (don't always referee)")
    pdf.add_bullet("Family meetings to address recurring issues")
    pdf.add_page_break()

    pdf.add_heading1("ONE-ON-ONE TIME TRACKER")
    pdf.add_paragraph("Each child needs regular individual time with each parent:")
    pdf.add_blank_line()
    pdf.add_paragraph("Child: _________________ This week's special time:")
    pdf.add_paragraph("  MON: ___ min  Activity: ___________________________")
    pdf.add_paragraph("  TUE: ___ min  Activity: ___________________________")
    pdf.add_paragraph("  WED: ___ min  Activity: ___________________________")
    pdf.add_paragraph("  THU: ___ min  Activity: ___________________________")
    pdf.add_paragraph("  FRI: ___ min  Activity: ___________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("Child: _________________ This week's special time:")
    pdf.add_paragraph("  MON: ___ min  Activity: ___________________________")
    pdf.add_paragraph("  TUE: ___ min  Activity: ___________________________")
    pdf.add_paragraph("  WED: ___ min  Activity: ___________________________")
    pdf.add_paragraph("  THU: ___ min  Activity: ___________________________")
    pdf.add_paragraph("  FRI: ___ min  Activity: ___________________________")
    pdf.add_separator()
    pdf.add_paragraph("By Daniel Tesfamariam | Siblings are practicing for all future relationships.")
    return pdf


def book13_back_to_school():
    """Back-to-School Organization Bundle"""
    pdf = PurePDF(title="Back-to-School Organization Bundle")
    pdf.add_title("BACK-TO-SCHOOL ORGANIZATION BUNDLE")
    pdf.add_heading2("Morning Routines, Homework Systems & Lunch Planning")
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_separator()
    pdf.add_page_break()


    pdf.add_heading1("MORNING ROUTINE CHECKLIST")
    pdf.add_paragraph("Target: Out the door by ___:___  Wake up at ___:___")
    pdf.add_blank_line()
    for step in [
        "Wake up (alarm goes off)",
        "Make bed",
        "Get dressed (clothes chosen night before)",
        "Brush teeth & wash face",
        "Eat breakfast",
        "Check backpack (homework, lunch, water bottle)",
        "Shoes on, jacket ready",
        "Out the door!",
    ]:
        pdf.add_paragraph(f"  [ ] {step}  Time: ___:___")
    pdf.add_blank_line()
    pdf.add_paragraph("RULE: No screens until fully ready!")
    pdf.add_page_break()

    pdf.add_heading1("EVENING PREP (Night Before)")
    pdf.add_paragraph("Do this EVERY night to make mornings easy:")
    for step in [
        "Check school folder / empty backpack",
        "Homework completed and packed",
        "Choose tomorrow's outfit (including underwear & socks)",
        "Pack lunch (or have lunch money ready)",
        "Fill water bottle (refrigerate)",
        "Pack any extras (library book, PE clothes, permission slip)",
        "Charge devices if needed for school",
        "Set alarm",
        "Lights out by ___:___",
    ]:
        pdf.add_paragraph(f"  [ ] {step}")
    pdf.add_page_break()

    pdf.add_heading1("HOMEWORK SYSTEM")
    pdf.add_heading3("The Homework Station:")
    pdf.add_bullet("Designated quiet spot (same place every day)")
    pdf.add_bullet("All supplies stocked (pencils, eraser, ruler, scissors, glue)")
    pdf.add_bullet("Timer visible")
    pdf.add_bullet("No phone/tablet during homework")
    pdf.add_heading3("The Homework Routine:")
    pdf.add_paragraph("  1. Snack first (10 min)")
    pdf.add_paragraph("  2. Play/movement break (15-20 min)")
    pdf.add_paragraph("  3. Review assignments (write list)")
    pdf.add_paragraph("  4. Start with hardest subject")
    pdf.add_paragraph("  5. Work in 20-min blocks with 5-min breaks")
    pdf.add_paragraph("  6. Parent check when done")
    pdf.add_paragraph("  7. Pack in backpack IMMEDIATELY")
    pdf.add_page_break()

    pdf.add_heading1("WEEKLY HOMEWORK TRACKER")
    pdf.add_paragraph("Week of: ___/___/___")
    pdf.add_blank_line()
    for day in ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]:
        pdf.add_heading3(f"{day}:")
        pdf.add_paragraph("  Subject: _____________ Assignment: _____________ [ ] Done [ ] Packed")
        pdf.add_paragraph("  Subject: _____________ Assignment: _____________ [ ] Done [ ] Packed")
    pdf.add_page_break()

    pdf.add_heading1("LUNCH PLANNING SYSTEM")
    pdf.add_heading3("FORMULA: Protein + Grain + Fruit + Veggie + Treat")
    pdf.add_blank_line()
    pdf.add_paragraph("PROTEINS: Turkey, cheese, hummus, hard-boiled egg, yogurt, PB")
    pdf.add_paragraph("GRAINS: Bread, crackers, tortilla, pretzels, granola bar")
    pdf.add_paragraph("FRUITS: Apple, grapes, berries, banana, mandarin, dried fruit")
    pdf.add_paragraph("VEGGIES: Carrots, cucumber, bell pepper, cherry tomatoes, celery")
    pdf.add_paragraph("TREATS: Cookies, fruit snacks, chocolate, trail mix")
    pdf.add_blank_line()
    pdf.add_heading3("THIS WEEK'S LUNCHES:")
    for day in ["MON", "TUE", "WED", "THU", "FRI"]:
        pdf.add_paragraph(f"  {day}: P:_______ G:_______ F:_______ V:_______ T:_______")
    pdf.add_page_break()

    pdf.add_heading1("AFTER-SCHOOL SCHEDULE")
    pdf.add_paragraph("Child: _________________")
    pdf.add_blank_line()
    for day in ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]:
        pdf.add_paragraph(f"  {day}:")
        pdf.add_paragraph("    Activity: _________________ Time: ___:___ to ___:___")
        pdf.add_paragraph("    Transport: _________________ Contact: _______________")
    pdf.add_page_break()

    pdf.add_heading1("SCHOOL YEAR CALENDAR AT-A-GLANCE")
    pdf.add_paragraph("Fill in key dates at the start of the year:")
    pdf.add_blank_line()
    pdf.add_paragraph("First day of school: ___/___/___")
    pdf.add_paragraph("Last day of school: ___/___/___")
    pdf.add_paragraph("Parent-teacher conferences: ___/___/___ and ___/___/___")
    pdf.add_paragraph("School breaks: ____________________________________________")
    pdf.add_paragraph("Early dismissal days: _____________________________________")
    pdf.add_paragraph("Picture day: ___/___/___")
    pdf.add_paragraph("Field trips: ______________________________________________")
    pdf.add_paragraph("Sports/activity dates: ____________________________________")
    pdf.add_paragraph("Teacher contact: __________________________________________")
    pdf.add_separator()
    pdf.add_paragraph("By Daniel Tesfamariam | Organization is a skill - teach it early.")
    return pdf


def book14_single_mom():
    """Single Mom Survival Guide"""
    pdf = PurePDF(title="Single Mom Survival Guide")
    pdf.add_title("SINGLE MOM SURVIVAL GUIDE")
    pdf.add_heading2("Budget, Time Management, Self-Care & Support Network")
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_separator()
    pdf.add_page_break()


    pdf.add_heading1("YOU ARE DOING AN INCREDIBLE JOB")
    pdf.add_paragraph("Being a single mom means doing the work of two people. You're not failing.")
    pdf.add_paragraph("You don't need to be perfect. You need to be consistent, present, and kind")
    pdf.add_paragraph("to yourself. This guide is your permission to ask for help and say no.")
    pdf.add_page_break()

    pdf.add_heading1("SINGLE MOM BUDGET WORKSHEET")
    pdf.add_heading3("MONTHLY INCOME:")
    pdf.add_paragraph("  Job/salary: $__________")
    pdf.add_paragraph("  Child support: $__________")
    pdf.add_paragraph("  Government assistance: $__________")
    pdf.add_paragraph("  Side income: $__________")
    pdf.add_paragraph("  Other: $__________")
    pdf.add_paragraph("  TOTAL INCOME: $__________")
    pdf.add_blank_line()
    pdf.add_heading3("FIXED EXPENSES:")
    pdf.add_paragraph("  Rent/mortgage: $__________")
    pdf.add_paragraph("  Utilities: $__________")
    pdf.add_paragraph("  Phone/internet: $__________")
    pdf.add_paragraph("  Car payment: $__________")
    pdf.add_paragraph("  Insurance (health/car/life): $__________")
    pdf.add_paragraph("  Childcare/daycare: $__________")
    pdf.add_paragraph("  Debt payments: $__________")
    pdf.add_paragraph("  TOTAL FIXED: $__________")
    pdf.add_blank_line()
    pdf.add_heading3("VARIABLE EXPENSES:")
    pdf.add_paragraph("  Groceries: $__________")
    pdf.add_paragraph("  Gas/transport: $__________")
    pdf.add_paragraph("  Kids activities: $__________")
    pdf.add_paragraph("  Household items: $__________")
    pdf.add_paragraph("  Clothing: $__________")
    pdf.add_paragraph("  Entertainment: $__________")
    pdf.add_paragraph("  TOTAL VARIABLE: $__________")
    pdf.add_blank_line()
    pdf.add_paragraph("  REMAINING (Income - Fixed - Variable): $__________")
    pdf.add_page_break()

    pdf.add_heading1("TIME MANAGEMENT: WEEKLY PLANNER")
    pdf.add_paragraph("You cannot do everything. Prioritize ruthlessly.")
    pdf.add_heading3("THE 3 DAILY NON-NEGOTIABLES:")
    pdf.add_paragraph("  1. Kids are fed, safe, and loved")
    pdf.add_paragraph("  2. One thing that moves life forward (bills, laundry, etc)")
    pdf.add_paragraph("  3. 15 minutes of self-care (non-negotiable!)")
    pdf.add_blank_line()
    pdf.add_heading3("WEEKLY TIME BLOCKS:")
    for day in ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]:
        pdf.add_paragraph(f"  {day}: Morning: _________ After work: _________ Evening: _________")
    pdf.add_page_break()

    pdf.add_heading1("MEAL PREP FOR BUSY SINGLE MOMS")
    pdf.add_paragraph("SUNDAY PREP (2 hours saves 5+ hours during the week):")
    pdf.add_bullet("Cook 2 proteins (chicken + ground beef or beans)")
    pdf.add_bullet("Prep 2-3 vegetables (chop, roast, or steam)")
    pdf.add_bullet("Cook 2 grains (rice + pasta or quinoa)")
    pdf.add_bullet("Prep 5 snack packs (for kids' lunches)")
    pdf.add_bullet("Hard boil eggs (quick protein all week)")
    pdf.add_blank_line()
    pdf.add_heading3("5 QUICK DINNERS (Under 20 min):")
    pdf.add_paragraph("  1. Tacos (precooked meat + toppings)")
    pdf.add_paragraph("  2. Pasta + jar sauce + pre-chopped veggies")
    pdf.add_paragraph("  3. Rice bowls (pre-cooked rice + protein + sauce)")
    pdf.add_paragraph("  4. Quesadillas + fruit")
    pdf.add_paragraph("  5. Breakfast for dinner (eggs, toast, fruit)")
    pdf.add_page_break()


    pdf.add_heading1("SELF-CARE (NOT OPTIONAL)")
    pdf.add_paragraph("You cannot pour from an empty cup. Schedule these like appointments:")
    pdf.add_heading3("DAILY (15 min - pick one):")
    pdf.add_bullet("Hot coffee/tea in silence before kids wake")
    pdf.add_bullet("5-minute journaling")
    pdf.add_bullet("Walk around the block")
    pdf.add_bullet("Stretching or yoga video")
    pdf.add_bullet("Call a friend")
    pdf.add_heading3("WEEKLY (1-2 hours):")
    pdf.add_bullet("Exercise class or home workout")
    pdf.add_bullet("Hobby time (reading, crafting, cooking)")
    pdf.add_bullet("Friend date (in person or phone)")
    pdf.add_bullet("Bath/skincare/pampering")
    pdf.add_heading3("MONTHLY (half or full day):")
    pdf.add_bullet("Solo outing (movie, shopping, nature)")
    pdf.add_bullet("Appointment for yourself (doctor, hair, therapy)")
    pdf.add_blank_line()
    pdf.add_paragraph("My self-care non-negotiable: _________________________________")
    pdf.add_paragraph("Person who can watch kids for my self-care: ___________________")
    pdf.add_page_break()

    pdf.add_heading1("SUPPORT NETWORK MAP")
    pdf.add_paragraph("You need a TEAM. Fill in your people:")
    pdf.add_blank_line()
    pdf.add_paragraph("Emergency childcare (drop everything): _______________________")
    pdf.add_paragraph("Regular childcare backup: ___________________________________")
    pdf.add_paragraph("Emotional support (can call crying at 2am): __________________")
    pdf.add_paragraph("Practical help (rides, errands, repairs): ____________________")
    pdf.add_paragraph("Co-parent/ex (if applicable): _______________________________")
    pdf.add_paragraph("Financial advice/help: ______________________________________")
    pdf.add_paragraph("Mom friend who 'gets it': ___________________________________")
    pdf.add_paragraph("Professional support (therapist/counselor): __________________")
    pdf.add_paragraph("Pediatrician: ______________________________________________")
    pdf.add_paragraph("School contact: _____________________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("RESOURCES:")
    pdf.add_bullet("211.org - local assistance programs")
    pdf.add_bullet("Local food banks and clothing closets")
    pdf.add_bullet("Single mom support groups (online and local)")
    pdf.add_bullet("SNAP, WIC, Medicaid (if eligible)")
    pdf.add_separator()
    pdf.add_paragraph("By Daniel Tesfamariam | Asking for help is strength, not weakness.")
    return pdf


def book15_emotional_intelligence():
    """Emotional Intelligence Activities for Kids"""
    pdf = PurePDF(title="Emotional Intelligence Activities")
    pdf.add_title("EMOTIONAL INTELLIGENCE ACTIVITIES FOR KIDS")
    pdf.add_heading2("Empathy, Social Skills & Gratitude Practices")
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_separator()
    pdf.add_page_break()

    pdf.add_heading1("WHAT IS EMOTIONAL INTELLIGENCE?")
    pdf.add_paragraph("EQ (Emotional Quotient) matters MORE than IQ for life success.")
    pdf.add_paragraph("5 components of EQ:")
    pdf.add_bullet("Self-awareness: Knowing what I feel")
    pdf.add_bullet("Self-regulation: Managing my reactions")
    pdf.add_bullet("Motivation: Pushing through hard things")
    pdf.add_bullet("Empathy: Understanding how others feel")
    pdf.add_bullet("Social skills: Getting along with people")
    pdf.add_paragraph("The good news: EQ can be TAUGHT and practiced like any skill!")
    pdf.add_page_break()


    pdf.add_heading1("SELF-AWARENESS ACTIVITIES")
    pdf.add_heading3("1. Feelings Check-In (Daily)")
    pdf.add_paragraph("Right now I feel: _____________ because _________________________")
    pdf.add_paragraph("My body feels: _________________________________________________")
    pdf.add_paragraph("What I need: ___________________________________________________")
    pdf.add_blank_line()
    pdf.add_heading3("2. Emotions Charades")
    pdf.add_paragraph("Take turns acting out emotions. Others guess the feeling.")
    pdf.add_paragraph("Emotions: happy, sad, angry, scared, surprised, disgusted,")
    pdf.add_paragraph("nervous, excited, embarrassed, proud, jealous, grateful")
    pdf.add_blank_line()
    pdf.add_heading3("3. Body Map")
    pdf.add_paragraph("Where do you feel emotions in your body?")
    pdf.add_paragraph("Anger = _________ (hot face? tight fists? fast heart?)")
    pdf.add_paragraph("Sadness = _______ (heavy chest? stinging eyes? tired body?)")
    pdf.add_paragraph("Anxiety = _______ (butterflies? sweaty palms? racing thoughts?)")
    pdf.add_paragraph("Joy = ___________ (light body? big smile? warm chest?)")
    pdf.add_page_break()

    pdf.add_heading1("EMPATHY BUILDERS")
    pdf.add_heading3("1. Perspective Flip")
    pdf.add_paragraph("When reading a book or watching a show, pause and ask:")
    pdf.add_paragraph("'How do you think [character] feels? Why? What would YOU feel?'")
    pdf.add_blank_line()
    pdf.add_heading3("2. Kindness Jar")
    pdf.add_paragraph("Each family member writes acts of kindness they notice on slips.")
    pdf.add_paragraph("Read them together weekly. Who can fill the jar?")
    pdf.add_blank_line()
    pdf.add_heading3("3. Walk in Their Shoes")
    pdf.add_paragraph("When a conflict happens, ask:")
    pdf.add_paragraph("'Can you tell me what [person] might be thinking and feeling?'")
    pdf.add_paragraph("'What might be going on in their life that we don't see?'")
    pdf.add_blank_line()
    pdf.add_heading3("4. Community Helper Project")
    pdf.add_paragraph("Choose one monthly: food bank, elderly visit, neighbor help,")
    pdf.add_paragraph("donation drive, thank-you cards for helpers (mail carrier, teacher)")
    pdf.add_page_break()

    pdf.add_heading1("SOCIAL SKILLS PRACTICE")
    pdf.add_heading3("Conversation Skills:")
    pdf.add_paragraph("STARTING: 'Hi! I'm [name]. What are you playing?'")
    pdf.add_paragraph("JOINING: 'Can I play too? What role can I have?'")
    pdf.add_paragraph("LISTENING: Eye contact + nodding + asking questions")
    pdf.add_paragraph("DISAGREEING: 'I see it differently. What if we try...'")
    pdf.add_paragraph("APOLOGIZING: 'I'm sorry I [specific action]. Are you okay?'")
    pdf.add_blank_line()
    pdf.add_heading3("Friendship Skills Checklist:")
    pdf.add_paragraph("  [ ] I take turns in conversations")
    pdf.add_paragraph("  [ ] I notice when someone looks sad or left out")
    pdf.add_paragraph("  [ ] I can disagree without being mean")
    pdf.add_paragraph("  [ ] I celebrate my friends' successes")
    pdf.add_paragraph("  [ ] I apologize when I make a mistake")
    pdf.add_paragraph("  [ ] I include others in my games")
    pdf.add_paragraph("  [ ] I keep secrets that friends share with me")
    pdf.add_paragraph("  [ ] I ask before borrowing things")
    pdf.add_page_break()

    pdf.add_heading1("GRATITUDE PRACTICES")
    pdf.add_heading3("1. Gratitude Journal (Nightly)")
    pdf.add_paragraph("3 things I'm grateful for today:")
    pdf.add_paragraph("  1. _________________________________________________________")
    pdf.add_paragraph("  2. _________________________________________________________")
    pdf.add_paragraph("  3. _________________________________________________________")
    pdf.add_paragraph("Someone I'm grateful for: ____________ Why: __________________")
    pdf.add_blank_line()
    pdf.add_heading3("2. Thank-You Note Writing")
    pdf.add_paragraph("Once a week, write a thank-you note to someone specific.")
    pdf.add_paragraph("Dear: _________________")
    pdf.add_paragraph("Thank you for: ______________________________________________")
    pdf.add_paragraph("It made me feel: ____________________________________________")
    pdf.add_blank_line()
    pdf.add_heading3("3. Rose, Thorn, Bud (Dinner Table Game)")
    pdf.add_paragraph("Rose = best part of today: __________________________________")
    pdf.add_paragraph("Thorn = hardest part: _______________________________________")
    pdf.add_paragraph("Bud = something to look forward to: _________________________")
    pdf.add_separator()
    pdf.add_paragraph("By Daniel Tesfamariam | EQ is the skill that makes all other skills work.")
    return pdf


def book16_family_meeting():
    """Family Meeting Toolkit"""
    pdf = PurePDF(title="Family Meeting Toolkit")
    pdf.add_title("FAMILY MEETING TOOLKIT")
    pdf.add_heading2("Agenda Templates, Discussion Cards & Decision-Making Tools")
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_separator()
    pdf.add_page_break()


    pdf.add_heading1("WHY FAMILY MEETINGS WORK")
    pdf.add_paragraph("Regular family meetings teach kids: democracy, problem-solving,")
    pdf.add_paragraph("communication, and that their voice matters.")
    pdf.add_bullet("Reduces daily nagging (decisions made together stick)")
    pdf.add_bullet("Kids feel heard and respected")
    pdf.add_bullet("Problems get solved before they explode")
    pdf.add_bullet("Builds teamwork and family identity")
    pdf.add_bullet("Teaches real-world meeting and negotiation skills")
    pdf.add_page_break()

    pdf.add_heading1("FAMILY MEETING GROUND RULES")
    pdf.add_paragraph("Post these where everyone can see:")
    pdf.add_paragraph("  1. Everyone gets a turn to talk")
    pdf.add_paragraph("  2. Listen without interrupting")
    pdf.add_paragraph("  3. No blaming or name-calling")
    pdf.add_paragraph("  4. Focus on solutions, not problems")
    pdf.add_paragraph("  5. Decisions need agreement (not just parent vote)")
    pdf.add_paragraph("  6. Meeting lasts 15-30 minutes max")
    pdf.add_paragraph("  7. End with something fun (game, treat, activity)")
    pdf.add_page_break()

    pdf.add_heading1("WEEKLY MEETING AGENDA TEMPLATE")
    pdf.add_paragraph("Date: ___/___/___  Time: ___:___  Facilitator: _____________")
    pdf.add_blank_line()
    pdf.add_paragraph("1. OPENING (2 min)")
    pdf.add_paragraph("   Appreciation round - each person compliments another family member")
    pdf.add_blank_line()
    pdf.add_paragraph("2. REVIEW LAST WEEK (3 min)")
    pdf.add_paragraph("   Did we follow through on decisions?  [ ] Yes  [ ] Partially  [ ] No")
    pdf.add_paragraph("   What worked? _______________________________________________")
    pdf.add_paragraph("   What didn't? _______________________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("3. NEW BUSINESS (10-15 min)")
    pdf.add_paragraph("   Issue 1: ___________________________________________________")
    pdf.add_paragraph("   Solutions brainstormed: _____________________________________")
    pdf.add_paragraph("   Decision: __________________________________________________")
    pdf.add_paragraph("   Who will do what by when? ___________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("   Issue 2: ___________________________________________________")
    pdf.add_paragraph("   Solutions brainstormed: _____________________________________")
    pdf.add_paragraph("   Decision: __________________________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("4. CALENDAR CHECK (3 min)")
    pdf.add_paragraph("   Upcoming events: ___________________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("5. FUN ACTIVITY (5+ min)")
    pdf.add_paragraph("   This week: _________________________________________________")
    pdf.add_page_break()

    pdf.add_heading1("DISCUSSION CARDS (Cut Out & Use)")
    pdf.add_paragraph("Pull one card each meeting for bonus discussion:")
    cards = [
        "What's one rule that needs changing? Why?",
        "What's the best thing about our family?",
        "Is anyone feeling overwhelmed this week?",
        "What chore system is working/not working?",
        "What should we do for fun this weekend?",
        "Is anyone having trouble with a friend?",
        "What meal should we cook together this week?",
        "What's something we could do for our community?",
        "Is screen time working fairly for everyone?",
        "What are we looking forward to this month?",
        "Does anyone need help with something?",
        "How can we be kinder to each other this week?",
    ]
    for i, card in enumerate(cards, 1):
        pdf.add_paragraph(f"  {i:2d}. {card}")
    pdf.add_page_break()

    pdf.add_heading1("FAMILY DECISION-MAKING TOOLS")
    pdf.add_heading3("Method 1: Thumbs Vote")
    pdf.add_paragraph("Thumbs up = love it | Sideways = okay with it | Down = can't live with it")
    pdf.add_paragraph("Need: No thumbs down to proceed")
    pdf.add_blank_line()
    pdf.add_heading3("Method 2: Pros and Cons List")
    pdf.add_paragraph("Option: ___________________________")
    pdf.add_paragraph("PROS: _________ | _________ | _________ | _________")
    pdf.add_paragraph("CONS: _________ | _________ | _________ | _________")
    pdf.add_blank_line()
    pdf.add_heading3("Method 3: Trial Period")
    pdf.add_paragraph("We'll try [decision] for ___ week(s) and review at next meeting.")
    pdf.add_blank_line()
    pdf.add_heading3("Method 4: Rotate Choice")
    pdf.add_paragraph("This week [name] chooses. Next week [name] chooses.")
    pdf.add_page_break()

    pdf.add_heading1("FAMILY MEETING TRACKER")
    pdf.add_paragraph("Keep a record of decisions made:")
    pdf.add_blank_line()
    for i in range(1, 9):
        pdf.add_paragraph(f"  Meeting #{i}  Date: ___/___/___")
        pdf.add_paragraph(f"  Decision: ________________________________________________")
        pdf.add_paragraph(f"  Follow-up: [ ] Done [ ] In progress [ ] Needs discussion")
        pdf.add_blank_line()
    pdf.add_separator()
    pdf.add_paragraph("By Daniel Tesfamariam | Families that talk together, stay together.")
    return pdf


def book17_chore_allowance():
    """Chore Chart & Allowance System"""
    pdf = PurePDF(title="Chore Chart & Allowance System")
    pdf.add_title("CHORE CHART & ALLOWANCE SYSTEM")
    pdf.add_heading2("Age-Specific Chores, Reward Menu & Money Management for Kids")
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_separator()
    pdf.add_page_break()


    pdf.add_heading1("AGE-APPROPRIATE CHORES")
    pdf.add_heading3("Ages 2-3:")
    pdf.add_bullet("Put toys in bin")
    pdf.add_bullet("Put dirty clothes in hamper")
    pdf.add_bullet("Wipe up spills with help")
    pdf.add_bullet("Help feed pets")
    pdf.add_bullet("Put books on shelf")
    pdf.add_heading3("Ages 4-5:")
    pdf.add_bullet("Make bed (imperfectly is fine!)")
    pdf.add_bullet("Set table")
    pdf.add_bullet("Clear own plate")
    pdf.add_bullet("Get dressed independently")
    pdf.add_bullet("Water plants")
    pdf.add_bullet("Sort laundry by color")
    pdf.add_heading3("Ages 6-8:")
    pdf.add_bullet("Fold and put away laundry")
    pdf.add_bullet("Sweep floors")
    pdf.add_bullet("Take out trash/recycling")
    pdf.add_bullet("Load/unload dishwasher")
    pdf.add_bullet("Feed and water pets independently")
    pdf.add_bullet("Pack own lunch")
    pdf.add_bullet("Keep room clean")
    pdf.add_heading3("Ages 9-12:")
    pdf.add_bullet("Vacuum and mop")
    pdf.add_bullet("Clean bathroom")
    pdf.add_bullet("Cook simple meals")
    pdf.add_bullet("Mow lawn / yard work")
    pdf.add_bullet("Do own laundry start to finish")
    pdf.add_bullet("Babysit younger siblings (short time)")
    pdf.add_bullet("Organize pantry/closets")
    pdf.add_page_break()

    pdf.add_heading1("WEEKLY CHORE CHART")
    pdf.add_paragraph("Child: _________________ Week of: ___/___/___")
    pdf.add_blank_line()
    pdf.add_paragraph("CHORE                    M   T   W   Th  F   Sa  Su")
    pdf.add_paragraph("________________________ [ ] [ ] [ ] [ ] [ ] [ ] [ ]")
    pdf.add_paragraph("________________________ [ ] [ ] [ ] [ ] [ ] [ ] [ ]")
    pdf.add_paragraph("________________________ [ ] [ ] [ ] [ ] [ ] [ ] [ ]")
    pdf.add_paragraph("________________________ [ ] [ ] [ ] [ ] [ ] [ ] [ ]")
    pdf.add_paragraph("________________________ [ ] [ ] [ ] [ ] [ ] [ ] [ ]")
    pdf.add_paragraph("________________________ [ ] [ ] [ ] [ ] [ ] [ ] [ ]")
    pdf.add_blank_line()
    pdf.add_paragraph("Completed ___/___  Earned: $_____")
    pdf.add_page_break()

    pdf.add_heading1("ALLOWANCE SYSTEM OPTIONS")
    pdf.add_heading3("Option A: Base + Commission")
    pdf.add_paragraph("Base allowance (for being a family member): $____ /week")
    pdf.add_paragraph("Extra chores for extra pay:")
    pdf.add_paragraph("  Wash car: $___  |  Deep clean room: $___  |  Yard work: $___")
    pdf.add_blank_line()
    pdf.add_heading3("Option B: Points System")
    pdf.add_paragraph("Each chore = points. Points convert to money at week's end.")
    pdf.add_paragraph("Easy chore = 1 pt | Medium = 2 pts | Hard = 3 pts")
    pdf.add_paragraph("1 point = $____ (set amount)")
    pdf.add_blank_line()
    pdf.add_heading3("Option C: Flat Allowance (not tied to chores)")
    pdf.add_paragraph("Amount: $____ per week (age x $0.50-1.00 is common)")
    pdf.add_paragraph("Chores are expected because you're part of the family.")
    pdf.add_paragraph("Allowance is for learning money management.")
    pdf.add_page_break()

    pdf.add_heading1("MONEY MANAGEMENT: SPEND, SAVE, GIVE")
    pdf.add_paragraph("Teach kids to split ALL money they receive:")
    pdf.add_blank_line()
    pdf.add_paragraph("  SPEND jar (50%): For small wants this week")
    pdf.add_paragraph("  SAVE jar (30%): For bigger goals")
    pdf.add_paragraph("  GIVE jar (20%): For charity or gifts")
    pdf.add_blank_line()
    pdf.add_heading3("SAVINGS GOAL TRACKER:")
    pdf.add_paragraph("I'm saving for: ________________________________")
    pdf.add_paragraph("Total cost: $___________")
    pdf.add_paragraph("Amount saved so far: $___________")
    pdf.add_paragraph("Amount still needed: $___________")
    pdf.add_paragraph("Weeks until goal (at $___/week): ___________")
    pdf.add_blank_line()
    pdf.add_paragraph("PROGRESS: [  ][  ][  ][  ][  ][  ][  ][  ][  ][  ] = GOAL!")
    pdf.add_page_break()

    pdf.add_heading1("REWARD MENU (Non-Money Rewards)")
    pdf.add_paragraph("For younger kids or as bonus motivation:")
    pdf.add_heading3("5 STARS:")
    pdf.add_bullet("Extra 15 min screen time")
    pdf.add_bullet("Choose a snack at the store")
    pdf.add_bullet("Stay up 15 min later")
    pdf.add_heading3("10 STARS:")
    pdf.add_bullet("Choose dinner menu")
    pdf.add_bullet("Have a friend over")
    pdf.add_bullet("Special dessert")
    pdf.add_heading3("20 STARS:")
    pdf.add_bullet("Family movie night (they pick)")
    pdf.add_bullet("Skip one chore for a week")
    pdf.add_bullet("Choose a family outing")
    pdf.add_heading3("50 STARS:")
    pdf.add_bullet("New toy/game (under $20)")
    pdf.add_bullet("Special one-on-one outing with parent")
    pdf.add_bullet("Sleepover party")
    pdf.add_separator()
    pdf.add_paragraph("By Daniel Tesfamariam | Chores teach responsibility. Money teaches choices.")
    return pdf


def book18_picky_eater():
    """Picky Eater Solution Guide"""
    pdf = PurePDF(title="Picky Eater Solution Guide")
    pdf.add_title("PICKY EATER SOLUTION GUIDE")
    pdf.add_heading2("Food Exposure Log, Recipes & Mealtime Rules That Work")
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_separator()
    pdf.add_page_break()


    pdf.add_heading1("WHY KIDS ARE PICKY (It's Normal!)")
    pdf.add_paragraph("Picky eating peaks between ages 2-6. It's developmental, not defiance.")
    pdf.add_bullet("Neophobia (fear of new) is a survival instinct")
    pdf.add_bullet("Kids may need 15-20 exposures before accepting a new food")
    pdf.add_bullet("Pressure and force ALWAYS backfire")
    pdf.add_bullet("Division of responsibility: Parent decides WHAT and WHEN. Child decides IF and HOW MUCH.")
    pdf.add_page_break()

    pdf.add_heading1("MEALTIME RULES (Post at the Table)")
    pdf.add_paragraph("  1. You don't have to eat it. You DO have to sit with the family.")
    pdf.add_paragraph("  2. No 'yuck' or 'gross' - you can say 'no thank you'")
    pdf.add_paragraph("  3. New foods go on the 'explorer plate' (no pressure)")
    pdf.add_paragraph("  4. One safe food always served (bread, rice, fruit)")
    pdf.add_paragraph("  5. Meals last 20-30 minutes, then kitchen closes")
    pdf.add_paragraph("  6. No short-order cooking (one meal for everyone)")
    pdf.add_paragraph("  7. No screens at the table")
    pdf.add_paragraph("  8. Snacks are 2 hours before meals (not right before)")
    pdf.add_page_break()

    pdf.add_heading1("FOOD EXPOSURE LOG")
    pdf.add_paragraph("Track each food exposure. Remember: seeing, smelling, and touching COUNT!")
    pdf.add_paragraph("Goal: 15-20 exposures of each new food")
    pdf.add_blank_line()
    pdf.add_paragraph("FOOD: ___________________________")
    pdf.add_paragraph("Exposure 1: Date ___/___ Reaction: [ ]Refused [ ]Touched [ ]Smelled [ ]Licked [ ]Tasted [ ]Ate!")
    pdf.add_paragraph("Exposure 2: Date ___/___ Reaction: [ ]Refused [ ]Touched [ ]Smelled [ ]Licked [ ]Tasted [ ]Ate!")
    pdf.add_paragraph("Exposure 3: Date ___/___ Reaction: [ ]Refused [ ]Touched [ ]Smelled [ ]Licked [ ]Tasted [ ]Ate!")
    pdf.add_paragraph("Exposure 4: Date ___/___ Reaction: [ ]Refused [ ]Touched [ ]Smelled [ ]Licked [ ]Tasted [ ]Ate!")
    pdf.add_paragraph("Exposure 5: Date ___/___ Reaction: [ ]Refused [ ]Touched [ ]Smelled [ ]Licked [ ]Tasted [ ]Ate!")
    pdf.add_blank_line()
    pdf.add_paragraph("FOOD: ___________________________")
    pdf.add_paragraph("Exposure 1: Date ___/___ Reaction: [ ]Refused [ ]Touched [ ]Smelled [ ]Licked [ ]Tasted [ ]Ate!")
    pdf.add_paragraph("Exposure 2: Date ___/___ Reaction: [ ]Refused [ ]Touched [ ]Smelled [ ]Licked [ ]Tasted [ ]Ate!")
    pdf.add_paragraph("Exposure 3: Date ___/___ Reaction: [ ]Refused [ ]Touched [ ]Smelled [ ]Licked [ ]Tasted [ ]Ate!")
    pdf.add_paragraph("Exposure 4: Date ___/___ Reaction: [ ]Refused [ ]Touched [ ]Smelled [ ]Licked [ ]Tasted [ ]Ate!")
    pdf.add_paragraph("Exposure 5: Date ___/___ Reaction: [ ]Refused [ ]Touched [ ]Smelled [ ]Licked [ ]Tasted [ ]Ate!")
    pdf.add_page_break()

    pdf.add_heading1("SNEAK-IT-IN RECIPES")
    pdf.add_paragraph("(Use ALONGSIDE open exposure, not as a replacement for it)")
    pdf.add_blank_line()
    pdf.add_heading3("1. Hidden Veggie Pasta Sauce")
    pdf.add_paragraph("Blend: 1 can tomatoes + 1 carrot + 1 zucchini + handful spinach")
    pdf.add_paragraph("Cook: Simmer 20 min. Kids won't see or taste the veggies!")
    pdf.add_blank_line()
    pdf.add_heading3("2. Smoothie Popsicles")
    pdf.add_paragraph("Blend: banana + berries + yogurt + handful spinach (turns it green-purple)")
    pdf.add_paragraph("Pour into molds. Kids eat veggies as a 'treat'!")
    pdf.add_blank_line()
    pdf.add_heading3("3. Zucchini Muffins")
    pdf.add_paragraph("Your favorite muffin recipe + 1 cup shredded zucchini. They dissolve!")
    pdf.add_blank_line()
    pdf.add_heading3("4. Cauliflower Mac & Cheese")
    pdf.add_paragraph("Steam cauliflower, blend into cheese sauce. Same taste, added nutrition.")
    pdf.add_blank_line()
    pdf.add_heading3("5. Veggie Quesadillas")
    pdf.add_paragraph("Finely diced peppers + beans + cheese in tortilla. Melted cheese hides veggies!")
    pdf.add_page_break()


    pdf.add_heading1("FOOD EXPLORATION ACTIVITIES")
    pdf.add_paragraph("Making food FUN reduces fear. Try these with no eating pressure:")
    pdf.add_bullet("Food art: make faces/pictures with fruit and veggies")
    pdf.add_bullet("Grow it: plant herbs or tomatoes together")
    pdf.add_bullet("Shop it: let child choose ONE new food to try")
    pdf.add_bullet("Cook it: kids who help cook are more likely to eat")
    pdf.add_bullet("Science it: 'What happens when we cook broccoli?'")
    pdf.add_bullet("Rate it: blind taste tests with ratings (fun, not pressure)")
    pdf.add_bullet("Build it: kebabs, wraps, pizza where THEY assemble")
    pdf.add_bullet("Story it: read books about food and trying new things")
    pdf.add_page_break()

    pdf.add_heading1("ACCEPTED FOODS INVENTORY")
    pdf.add_paragraph("List ALL foods your child currently accepts:")
    pdf.add_heading3("Proteins:")
    pdf.add_paragraph("______________________________________________________________")
    pdf.add_heading3("Grains/Starches:")
    pdf.add_paragraph("______________________________________________________________")
    pdf.add_heading3("Fruits:")
    pdf.add_paragraph("______________________________________________________________")
    pdf.add_heading3("Vegetables:")
    pdf.add_paragraph("______________________________________________________________")
    pdf.add_heading3("Dairy:")
    pdf.add_paragraph("______________________________________________________________")
    pdf.add_heading3("Snacks/Other:")
    pdf.add_paragraph("______________________________________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("Count: ___ foods accepted. Goal: Add 1-2 new foods per month.")
    pdf.add_paragraph("WHEN TO SEEK HELP: Fewer than 20 accepted foods, weight loss,")
    pdf.add_paragraph("gagging/vomiting with textures = see a feeding therapist.")
    pdf.add_separator()
    pdf.add_paragraph("By Daniel Tesfamariam | Patience is the secret ingredient.")
    return pdf


def book19_grief():
    """Parenting Through Grief"""
    pdf = PurePDF(title="Parenting Through Grief")
    pdf.add_title("PARENTING THROUGH GRIEF")
    pdf.add_heading2("Helping Kids Cope with Loss, Memory Book & Conversation Scripts")
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_separator()
    pdf.add_page_break()

    pdf.add_heading1("HOW CHILDREN GRIEVE (By Age)")
    pdf.add_heading3("Under 3 years:")
    pdf.add_bullet("Don't understand death but sense absence and parent's grief")
    pdf.add_bullet("May regress (sleep, feeding, clinging)")
    pdf.add_bullet("Need: routine, physical comfort, simple honest words")
    pdf.add_heading3("Ages 3-5:")
    pdf.add_bullet("Think death is temporary/reversible (like sleep)")
    pdf.add_bullet("Magical thinking ('Did I cause this?')")
    pdf.add_bullet("May ask the same questions repeatedly")
    pdf.add_bullet("Need: concrete explanations, reassurance, play-based processing")
    pdf.add_heading3("Ages 6-9:")
    pdf.add_bullet("Understand death is permanent but may not grasp it happening to them")
    pdf.add_bullet("May worry about other people dying")
    pdf.add_bullet("Can seem fine then suddenly collapse in grief")
    pdf.add_bullet("Need: factual info, permission to feel, continued normalcy")
    pdf.add_heading3("Ages 10-12:")
    pdf.add_bullet("Understand death fully")
    pdf.add_bullet("May hide emotions to 'protect' parents")
    pdf.add_bullet("Risk of anger, acting out, withdrawal")
    pdf.add_bullet("Need: honest conversations, peer support, counseling access")
    pdf.add_heading3("Teens:")
    pdf.add_bullet("Grieve like adults but with fewer coping tools")
    pdf.add_bullet("May turn to peers instead of parents")
    pdf.add_bullet("Risk of substance use, reckless behavior")
    pdf.add_bullet("Need: space AND availability, professional support offered")
    pdf.add_page_break()


    pdf.add_heading1("WHAT TO SAY (AND NOT SAY)")
    pdf.add_heading3("SAY:")
    pdf.add_bullet('"[Person] died. Their body stopped working and cannot be fixed."')
    pdf.add_bullet('"It is okay to cry. It is okay to feel angry. All feelings are allowed."')
    pdf.add_bullet('"This is not your fault. Nothing you did caused this."')
    pdf.add_bullet('"I am sad too. We can be sad together."')
    pdf.add_bullet('"I don\'t know why this happened. I wish I did."')
    pdf.add_bullet('"We will always remember [person]. They will always be part of our family."')
    pdf.add_blank_line()
    pdf.add_heading3("DO NOT SAY:")
    pdf.add_bullet('"They went to sleep" (causes fear of sleeping)')
    pdf.add_bullet('"God needed another angel" (causes anger at God)')
    pdf.add_bullet('"They went on a long trip" (causes confusion/abandonment)')
    pdf.add_bullet('"You need to be strong for mommy" (suppresses grief)')
    pdf.add_bullet('"At least they\'re not in pain" (minimizes the child\'s pain)')
    pdf.add_bullet('"Don\'t cry, they wouldn\'t want you to be sad" (shames emotions)')
    pdf.add_page_break()

    pdf.add_heading1("CONVERSATION SCRIPTS FOR SPECIFIC LOSSES")
    pdf.add_heading3("Death of a grandparent:")
    pdf.add_paragraph('"Grandma/Grandpa\'s body was very old and tired. It stopped working."')
    pdf.add_paragraph('"They loved you so much. Let\'s talk about your favorite memories."')
    pdf.add_blank_line()
    pdf.add_heading3("Death of a parent:")
    pdf.add_paragraph('"Mommy/Daddy died. This means their body stopped working forever."')
    pdf.add_paragraph('"You will always be safe. I am here. [Other person] is here."')
    pdf.add_paragraph('"It is okay to feel anything. There is no wrong way to feel."')
    pdf.add_blank_line()
    pdf.add_heading3("Death of a pet:")
    pdf.add_paragraph('"[Pet name]\'s body stopped working. They are not in pain."')
    pdf.add_paragraph('"It is okay to miss them a lot. They were an important part of our family."')
    pdf.add_blank_line()
    pdf.add_heading3("Death of a peer/classmate:")
    pdf.add_paragraph('"Something very sad happened. [Name] died. This was not normal."')
    pdf.add_paragraph('"You are safe. Would you like to talk about how you feel?"')
    pdf.add_page_break()

    pdf.add_heading1("MEMORY BOOK PAGES")
    pdf.add_paragraph("Create a memory book together. Here are pages to fill:")
    pdf.add_blank_line()
    pdf.add_paragraph("Person I'm remembering: _______________________________________")
    pdf.add_paragraph("My relationship to them: ______________________________________")
    pdf.add_paragraph("My favorite memory with them: _________________________________")
    pdf.add_paragraph("______________________________________________________________")
    pdf.add_paragraph("Something funny they used to do: _______________________________")
    pdf.add_paragraph("A smell/sound/food that reminds me of them: ____________________")
    pdf.add_paragraph("Something they taught me: _____________________________________")
    pdf.add_paragraph("What I wish I could tell them: ________________________________")
    pdf.add_paragraph("How I feel today about them being gone: ________________________")
    pdf.add_paragraph("Something that makes me smile when I think of them: ____________")
    pdf.add_page_break()

    pdf.add_heading1("GRIEF SUPPORT STRATEGIES")
    pdf.add_heading3("Creating rituals:")
    pdf.add_bullet("Light a candle on special days")
    pdf.add_bullet("Visit a meaningful place together")
    pdf.add_bullet("Make their favorite recipe on their birthday")
    pdf.add_bullet("Write a letter to them (balloon release or burning)")
    pdf.add_bullet("Plant a memorial tree or garden")
    pdf.add_heading3("Daily support:")
    pdf.add_bullet("Keep routines as normal as possible")
    pdf.add_bullet("Let them see you grieve (models healthy processing)")
    pdf.add_bullet("Give permission for ALL feelings (including laughter and joy)")
    pdf.add_bullet("Check in regularly but don't force conversation")
    pdf.add_bullet("Expect grief waves at unpredictable times")
    pdf.add_heading3("When to get professional help:")
    pdf.add_bullet("Prolonged sleep or appetite changes (2+ weeks)")
    pdf.add_bullet("Talking about wanting to die or be with the person")
    pdf.add_bullet("Inability to function at school/home")
    pdf.add_bullet("Persistent nightmares or new fears")
    pdf.add_bullet("Self-harm or substance use")
    pdf.add_blank_line()
    pdf.add_paragraph("Grief counselor: ______________________________________________")
    pdf.add_paragraph("Children's grief support group: _______________________________")
    pdf.add_separator()
    pdf.add_paragraph("By Daniel Tesfamariam | Grief is love with nowhere to go. Let it flow.")
    return pdf


def book20_autism_parenting():
    """Autism Spectrum Parenting Toolkit"""
    pdf = PurePDF(title="Autism Spectrum Parenting Toolkit")
    pdf.add_title("AUTISM SPECTRUM PARENTING TOOLKIT")
    pdf.add_heading2("Visual Schedules, Social Stories, Sensory Diet & IEP Prep")
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_separator()
    pdf.add_page_break()


    pdf.add_heading1("UNDERSTANDING YOUR AUTISTIC CHILD")
    pdf.add_paragraph("Autism is a neurological DIFFERENCE, not a deficiency.")
    pdf.add_paragraph("Your child experiences the world more intensely - sounds louder,")
    pdf.add_paragraph("lights brighter, textures sharper, social rules more confusing.")
    pdf.add_blank_line()
    pdf.add_paragraph("KEY PRINCIPLES:")
    pdf.add_bullet("Presume competence - they understand more than they can express")
    pdf.add_bullet("Behavior IS communication - look for the unmet need")
    pdf.add_bullet("Accommodate first, then teach - reduce barriers before adding demands")
    pdf.add_bullet("Special interests are STRENGTHS - use them to teach other skills")
    pdf.add_bullet("Meltdowns are NOT tantrums - they are nervous system overload")
    pdf.add_page_break()

    pdf.add_heading1("VISUAL SCHEDULE TEMPLATES")
    pdf.add_paragraph("Visual schedules reduce anxiety by making the day predictable.")
    pdf.add_blank_line()
    pdf.add_heading3("MORNING:")
    for i, step in enumerate([
        "Wake up", "Toilet", "Get dressed (see outfit card)",
        "Eat breakfast (see menu card)", "Brush teeth",
        "Get backpack", "Go to school/car"
    ], 1):
        pdf.add_paragraph(f"  {i}. [ ] {step}")
    pdf.add_blank_line()
    pdf.add_heading3("AFTER SCHOOL:")
    for i, step in enumerate([
        "Arrive home", "Snack", "Calm time (30 min)",
        "Homework/therapy", "Free time/special interest",
        "Dinner", "Bath", "Bedtime routine"
    ], 1):
        pdf.add_paragraph(f"  {i}. [ ] {step}")
    pdf.add_paragraph("TIP: Use pictures/icons for non-readers. Velcro strips let child")
    pdf.add_paragraph("move items from 'to do' to 'done' for satisfaction.")
    pdf.add_page_break()

    pdf.add_heading1("SOCIAL STORIES TEMPLATE")
    pdf.add_paragraph("Social stories explain situations in a clear, literal way:")
    pdf.add_blank_line()
    pdf.add_heading3("Template structure:")
    pdf.add_paragraph("1. SITUATION: Where/when does this happen?")
    pdf.add_paragraph("2. PERSPECTIVE: How do others feel/think in this situation?")
    pdf.add_paragraph("3. DIRECTIVE: What can I do?")
    pdf.add_paragraph("4. AFFIRMATIVE: I will try my best. That's okay.")
    pdf.add_blank_line()
    pdf.add_heading3("Example: Going to the Doctor")
    pdf.add_paragraph("Sometimes I need to go to the doctor. (Situation)")
    pdf.add_paragraph("The doctor wants to help me stay healthy. (Perspective)")
    pdf.add_paragraph("I can bring my headphones and a comfort item. (Directive)")
    pdf.add_paragraph("It might feel uncomfortable but it will be over soon. (Affirmative)")
    pdf.add_blank_line()
    pdf.add_heading3("Write your own:")
    pdf.add_paragraph("Situation: ___________________________________________________")
    pdf.add_paragraph("Perspective: _________________________________________________")
    pdf.add_paragraph("Directive: ___________________________________________________")
    pdf.add_paragraph("Affirmative: _________________________________________________")
    pdf.add_page_break()

    pdf.add_heading1("SENSORY DIET PLANNER")
    pdf.add_paragraph("A sensory diet provides regular sensory input throughout the day")
    pdf.add_paragraph("to keep your child regulated. Work with an OT to customize.")
    pdf.add_blank_line()
    pdf.add_heading3("CALMING (when overstimulated):")
    pdf.add_bullet("Deep pressure (weighted blanket, tight hugs, compression vest)")
    pdf.add_bullet("Dim lights / reduce noise")
    pdf.add_bullet("Slow rhythmic movement (rocking, swinging)")
    pdf.add_bullet("Chewing (chewy tube, crunchy snacks)")
    pdf.add_bullet("Warm bath or shower")
    pdf.add_heading3("ALERTING (when under-responsive):")
    pdf.add_bullet("Cold water or ice")
    pdf.add_bullet("Fast movement (jumping, spinning, running)")
    pdf.add_bullet("Bright lights or music")
    pdf.add_bullet("Sour or spicy flavors")
    pdf.add_bullet("Vibration (vibrating toothbrush, massager)")
    pdf.add_heading3("ORGANIZING (for focus):")
    pdf.add_bullet("Heavy work (carrying books, pushing cart, digging)")
    pdf.add_bullet("Oral motor (drinking through straw, blowing bubbles)")
    pdf.add_bullet("Fidget tools (putty, tangle, stress ball)")
    pdf.add_bullet("Proprioceptive input (wall push-ups, bear walks)")
    pdf.add_page_break()


    pdf.add_heading1("SENSORY PROFILE WORKSHEET")
    pdf.add_paragraph("Document your child's sensory preferences:")
    pdf.add_blank_line()
    pdf.add_paragraph("SOUND:")
    pdf.add_paragraph("  Bothered by: ________________________________________________")
    pdf.add_paragraph("  Seeks/enjoys: _______________________________________________")
    pdf.add_paragraph("  Accommodations: _____________________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("TOUCH:")
    pdf.add_paragraph("  Bothered by: ________________________________________________")
    pdf.add_paragraph("  Seeks/enjoys: _______________________________________________")
    pdf.add_paragraph("  Accommodations: _____________________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("SIGHT:")
    pdf.add_paragraph("  Bothered by: ________________________________________________")
    pdf.add_paragraph("  Seeks/enjoys: _______________________________________________")
    pdf.add_paragraph("  Accommodations: _____________________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("TASTE/SMELL:")
    pdf.add_paragraph("  Bothered by: ________________________________________________")
    pdf.add_paragraph("  Seeks/enjoys: _______________________________________________")
    pdf.add_paragraph("  Accommodations: _____________________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("MOVEMENT:")
    pdf.add_paragraph("  Bothered by: ________________________________________________")
    pdf.add_paragraph("  Seeks/enjoys: _______________________________________________")
    pdf.add_paragraph("  Accommodations: _____________________________________________")
    pdf.add_page_break()

    pdf.add_heading1("IEP PREPARATION GUIDE")
    pdf.add_paragraph("Know your rights. Come prepared. Bring this to meetings.")
    pdf.add_blank_line()
    pdf.add_paragraph("Child's name: _________________ Grade: _____ Date: ___/___/___")
    pdf.add_paragraph("Diagnosis: _________________ Date of diagnosis: ___/___/___")
    pdf.add_blank_line()
    pdf.add_heading3("STRENGTHS (lead with these!):")
    pdf.add_paragraph("  1. ________________________________________________________")
    pdf.add_paragraph("  2. ________________________________________________________")
    pdf.add_paragraph("  3. ________________________________________________________")
    pdf.add_blank_line()
    pdf.add_heading3("AREAS OF NEED:")
    pdf.add_paragraph("  Academic: __________________________________________________")
    pdf.add_paragraph("  Social: ____________________________________________________")
    pdf.add_paragraph("  Communication: _____________________________________________")
    pdf.add_paragraph("  Behavioral: ________________________________________________")
    pdf.add_paragraph("  Sensory: ___________________________________________________")
    pdf.add_blank_line()
    pdf.add_heading3("ACCOMMODATIONS REQUESTING:")
    for acc in [
        "Visual schedule in classroom",
        "Sensory breaks (frequency: ___________)",
        "Noise-canceling headphones allowed",
        "Advance notice of schedule changes",
        "Social skills instruction",
        "Speech/language therapy",
        "Occupational therapy",
        "Aide/paraprofessional support",
        "Modified homework expectations",
        "Testing in quiet separate room",
        "Extended time on assignments",
        "Communication device/AAC access",
    ]:
        pdf.add_paragraph(f"  [ ] {acc}")
    pdf.add_page_break()

    pdf.add_heading1("MELTDOWN vs TANTRUM (Know the Difference)")
    pdf.add_heading3("TANTRUM (goal-directed):")
    pdf.add_bullet("Child wants something specific")
    pdf.add_bullet("Watches for your reaction")
    pdf.add_bullet("Stops when they get what they want (or realize they won't)")
    pdf.add_bullet("Can be redirected")
    pdf.add_heading3("MELTDOWN (nervous system overload):")
    pdf.add_bullet("Caused by sensory/emotional overwhelm")
    pdf.add_bullet("NOT within the child's control")
    pdf.add_bullet("Cannot be reasoned with during it")
    pdf.add_bullet("Needs safety and time to pass")
    pdf.add_blank_line()
    pdf.add_heading3("DURING A MELTDOWN:")
    pdf.add_paragraph("  1. Ensure safety (move dangerous objects, create space)")
    pdf.add_paragraph("  2. Reduce sensory input (lights down, people back, quiet voice)")
    pdf.add_paragraph("  3. Don't talk too much (processing is overloaded)")
    pdf.add_paragraph("  4. Offer comfort items (blanket, headphones, chewy)")
    pdf.add_paragraph("  5. Wait. Be calm. Be present. It WILL pass.")
    pdf.add_paragraph("  6. After: reconnect, don't lecture. 'That was hard. I'm here.'")
    pdf.add_page_break()

    pdf.add_heading1("COMMUNICATION SUPPORT")
    pdf.add_heading3("If your child is verbal but struggles:")
    pdf.add_bullet("Give processing time (wait 10+ seconds after asking)")
    pdf.add_bullet("Use visual supports alongside verbal instructions")
    pdf.add_bullet("One instruction at a time (not multi-step)")
    pdf.add_bullet("Be literal (avoid sarcasm, idioms, implied meaning)")
    pdf.add_heading3("If your child is non-speaking or limited verbal:")
    pdf.add_bullet("AAC (communication device) is NOT a last resort - offer early")
    pdf.add_bullet("Honor ALL forms of communication (gesture, picture, behavior)")
    pdf.add_bullet("Don't withhold AAC to 'encourage' speech")
    pdf.add_bullet("Model AAC use yourself")
    pdf.add_blank_line()
    pdf.add_paragraph("Communication tools we use: ___________________________________")
    pdf.add_paragraph("SLP (speech therapist): _______________________________________")
    pdf.add_paragraph("OT (occupational therapist): __________________________________")
    pdf.add_separator()
    pdf.add_paragraph("By Daniel Tesfamariam | Different, not less. Always presume competence.")
    return pdf



def main():
    """Generate all 15 Tier 2 & 3 parenting books (Books 6-20)."""
    print("=" * 60)
    print("  PARENTING PDF BOOKS - Tier 2 & 3 Generator")
    print("  Books 6-20 | By Daniel Tesfamariam")
    print("=" * 60)
    print()

    books = [
        (book6_adhd_parenting, "06-ADHD-Child-Parenting-Guide.pdf"),
        (book7_teen_communication, "07-Teen-Tween-Communication-Workbook.pdf"),
        (book8_montessori_home, "08-Montessori-Home-Activities-Guide.pdf"),
        (book9_potty_training, "09-Potty-Training-Complete-System.pdf"),
        (book10_anxiety_emotions, "10-Anxiety-Big-Emotions-Workbook.pdf"),
        (book11_baby_sleep, "11-Baby-Sleep-Training-Guide.pdf"),
        (book12_sibling_rivalry, "12-Sibling-Rivalry-Resolution-Toolkit.pdf"),
        (book13_back_to_school, "13-Back-to-School-Organization-Bundle.pdf"),
        (book14_single_mom, "14-Single-Mom-Survival-Guide.pdf"),
        (book15_emotional_intelligence, "15-Emotional-Intelligence-Activities.pdf"),
        (book16_family_meeting, "16-Family-Meeting-Toolkit.pdf"),
        (book17_chore_allowance, "17-Chore-Chart-Allowance-System.pdf"),
        (book18_picky_eater, "18-Picky-Eater-Solution-Guide.pdf"),
        (book19_grief, "19-Parenting-Through-Grief.pdf"),
        (book20_autism_parenting, "20-Autism-Parenting-Toolkit.pdf"),
    ]

    results = []
    for i, (book_func, filename) in enumerate(books, 1):
        print(f"[{i:2d}/15] Generating: {filename}")
        try:
            pdf = book_func()
            filepath = os.path.join(OUTPUT_DIR, filename)
            size = pdf.save(filepath)
            size_kb = size / 1024
            print(f"        -> Saved ({size_kb:.1f} KB)")
            results.append((filename, size_kb))
        except Exception as e:
            print(f"        -> ERROR: {e}")
            import traceback
            traceback.print_exc()

    print()
    print("=" * 60)
    print("  GENERATION COMPLETE")
    print("=" * 60)
    print(f"  Books generated: {len(results)}/15")
    print(f"  Output: {OUTPUT_DIR}/")
    print()
    for fname, size in results:
        print(f"    [{size:5.1f} KB] {fname}")
    total = sum(s for _, s in results)
    print(f"\n  Total: {total:.0f} KB ({total/1024:.1f} MB)")
    print()


if __name__ == "__main__":
    main()
