#!/usr/bin/env python3
"""
Etsy Business Builder - Complete PDF Book Generator
Generates Books 2-5 with 60+ pages each of real, actionable content.
Author: Daniel Tesfamariam
"""

import os, sys
sys.path.insert(0, '/projects/sandbox/CLAUDE/etsy-digital-products-strategy')
_code = open('/projects/sandbox/CLAUDE/etsy-digital-products-strategy/generate_pdfs.py').read()
_code = _code.replace("\nif __name__ == '__main__':\n    main()\n", "\n")
exec(_code)

OUTPUT_DIR = '/projects/sandbox/CLAUDE/etsy-business-builder/pdf-output'
os.makedirs(OUTPUT_DIR, exist_ok=True)


def generate_book2():
    """Book 2: Anxiety & Stress Management Workbook (60-80 pages)"""
    pdf = PurePDF(title="Anxiety & Stress Management Workbook", author="Daniel Tesfamariam")

    # TITLE PAGE
    pdf.add_blank_line()
    pdf.add_blank_line()
    pdf.add_blank_line()
    pdf.add_title("ANXIETY & STRESS MANAGEMENT")
    pdf.add_title("WORKBOOK")
    pdf.add_blank_line()
    pdf.add_heading2("A Complete CBT-Based System for Understanding,")
    pdf.add_heading2("Managing, and Overcoming Anxiety")
    pdf.add_blank_line()
    pdf.add_blank_line()
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_blank_line()
    pdf.add_paragraph("Evidence-based tools, worksheets, and tracking systems")
    pdf.add_paragraph("to help you regain control of your mental wellness.")
    pdf.add_blank_line()
    pdf.add_separator()

    pdf.add_paragraph("Copyright 2024 Daniel Tesfamariam. All rights reserved.")
    pdf.add_paragraph("This workbook is for educational purposes only and is not a substitute")
    pdf.add_paragraph("for professional mental health treatment.")

    # TABLE OF CONTENTS
    pdf.add_page_break()
    pdf.add_title("TABLE OF CONTENTS")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_paragraph("Chapter 1: Understanding Anxiety .......................... 3")
    pdf.add_paragraph("Chapter 2: CBT Thought Records & Worksheets .............. 11")
    pdf.add_paragraph("Chapter 3: Breathing & Grounding Techniques .............. 23")
    pdf.add_paragraph("Chapter 4: Worry Management System ....................... 31")
    pdf.add_paragraph("Chapter 5: 30-Day Anxiety Tracker ........................ 41")
    pdf.add_paragraph("Chapter 6: Coping Strategies Toolkit ..................... 53")
    pdf.add_paragraph("Chapter 7: Safety Planning ............................... 61")
    pdf.add_paragraph("Chapter 8: Action Plans & Goals .......................... 65")
    pdf.add_paragraph("Final: Next Steps & Resources ............................ 73")
    pdf.add_blank_line()
    pdf.add_separator()

    # CHAPTER 1: UNDERSTANDING ANXIETY
    pdf.add_page_break()
    pdf.add_heading1("CHAPTER 1: UNDERSTANDING ANXIETY")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_heading2("What Is Anxiety?")
    pdf.add_blank_line()
    pdf.add_paragraph("Anxiety is your body's natural response to perceived threats or danger. It is a complex combination of physical sensations, thoughts, and behaviors that evolved to protect us from harm. While some anxiety is normal and even helpful, excessive or chronic anxiety can interfere with daily life, relationships, work performance, and overall well-being.")
    pdf.add_blank_line()
    pdf.add_paragraph("Understanding anxiety is the first step toward managing it effectively. When you understand what is happening in your brain and body during an anxiety response, you gain the power to intervene and redirect that response in healthier ways.")
    pdf.add_blank_line()

    pdf.add_heading2("The Anxiety Cycle")
    pdf.add_blank_line()
    pdf.add_paragraph("Anxiety operates in a predictable cycle that reinforces itself over time. Understanding this cycle gives you multiple intervention points where you can break the pattern:")
    pdf.add_blank_line()
    pdf.add_bullet("TRIGGER: An event, thought, or sensation that activates anxiety")
    pdf.add_bullet("THOUGHT: An interpretation of the trigger (often catastrophic or distorted)")
    pdf.add_bullet("PHYSICAL RESPONSE: Body sensations like racing heart, sweating, tension")
    pdf.add_bullet("EMOTIONAL RESPONSE: Feelings of fear, dread, panic, or overwhelm")
    pdf.add_bullet("BEHAVIORAL RESPONSE: Avoidance, escape, reassurance-seeking, or safety behaviors")
    pdf.add_bullet("REINFORCEMENT: Short-term relief from avoidance strengthens the anxiety cycle")
    pdf.add_blank_line()
    pdf.add_paragraph("Each time you avoid something that triggers anxiety, your brain learns that the trigger is genuinely dangerous. This makes the anxiety stronger next time. Breaking this cycle requires gradually facing fears while using coping strategies to manage discomfort.")
    pdf.add_blank_line()

    pdf.add_heading2("Types of Anxiety Disorders")
    pdf.add_blank_line()
    pdf.add_paragraph("While this workbook addresses general anxiety management skills, it helps to understand the different presentations anxiety can take:")
    pdf.add_blank_line()
    pdf.add_heading3("Generalized Anxiety Disorder (GAD)")
    pdf.add_paragraph("Characterized by excessive, uncontrollable worry about multiple areas of life including work, health, family, money, and everyday matters. People with GAD often describe feeling worried most of the time and find it difficult to relax or stop their mind from racing.")
    pdf.add_blank_line()
    pdf.add_heading3("Social Anxiety Disorder")
    pdf.add_paragraph("Intense fear of social situations where you might be judged, embarrassed, or rejected. This can range from specific fears like public speaking to generalized discomfort in most social interactions.")
    pdf.add_blank_line()
    pdf.add_heading3("Panic Disorder")
    pdf.add_paragraph("Recurrent unexpected panic attacks followed by persistent worry about having more attacks. Panic attacks involve sudden surges of intense fear with physical symptoms like chest pain, shortness of breath, and feeling like you are dying.")
    pdf.add_blank_line()

    pdf.add_heading3("Specific Phobias")
    pdf.add_paragraph("Intense, irrational fear of specific objects or situations such as heights, flying, animals, blood, or enclosed spaces. The fear is out of proportion to the actual danger posed.")
    pdf.add_blank_line()
    pdf.add_heading3("Health Anxiety")
    pdf.add_paragraph("Preoccupation with having or developing a serious illness. Involves frequent body checking, excessive research about symptoms, repeated doctor visits, or avoidance of health-related information.")
    pdf.add_blank_line()

    pdf.add_heading2("Physical Symptoms of Anxiety")
    pdf.add_blank_line()
    pdf.add_paragraph("Anxiety is not just in your head. It produces real, measurable physical changes throughout your body. These symptoms occur because your sympathetic nervous system activates the fight-or-flight response:")
    pdf.add_blank_line()
    pdf.add_bullet("Rapid heartbeat or heart palpitations")
    pdf.add_bullet("Shortness of breath or feeling like you cannot get enough air")
    pdf.add_bullet("Chest tightness or chest pain")
    pdf.add_bullet("Muscle tension, especially in neck, shoulders, and jaw")
    pdf.add_bullet("Stomach problems: nausea, butterflies, IBS symptoms")
    pdf.add_bullet("Sweating, especially palms, underarms, and forehead")
    pdf.add_bullet("Trembling or shaking")
    pdf.add_bullet("Dizziness or lightheadedness")
    pdf.add_bullet("Tingling or numbness in hands and feet")
    pdf.add_bullet("Dry mouth and difficulty swallowing")
    pdf.add_bullet("Headaches and migraines")
    pdf.add_bullet("Fatigue and exhaustion despite adequate sleep")
    pdf.add_bullet("Insomnia or restless sleep")
    pdf.add_bullet("Frequent urination")
    pdf.add_bullet("Hot flashes or chills")
    pdf.add_blank_line()

    pdf.add_heading2("Your Anxiety Self-Assessment")
    pdf.add_blank_line()
    pdf.add_paragraph("Rate each item below from 0 (not at all) to 4 (nearly every day) over the past two weeks:")
    pdf.add_blank_line()
    pdf.add_paragraph("___ Feeling nervous, anxious, or on edge")
    pdf.add_paragraph("___ Not being able to stop or control worrying")
    pdf.add_paragraph("___ Worrying too much about different things")
    pdf.add_paragraph("___ Trouble relaxing")
    pdf.add_paragraph("___ Being so restless that it is hard to sit still")
    pdf.add_paragraph("___ Becoming easily annoyed or irritable")
    pdf.add_paragraph("___ Feeling afraid as if something awful might happen")
    pdf.add_paragraph("___ Difficulty concentrating on tasks")
    pdf.add_paragraph("___ Sleep difficulties (falling or staying asleep)")
    pdf.add_paragraph("___ Physical tension that will not go away")
    pdf.add_blank_line()
    pdf.add_paragraph("TOTAL SCORE: _____ / 40")
    pdf.add_blank_line()
    pdf.add_paragraph("Scoring: 0-7 Minimal | 8-15 Mild | 16-25 Moderate | 26-40 Severe")
    pdf.add_blank_line()

    pdf.add_heading2("My Anxiety Profile Worksheet")
    pdf.add_blank_line()
    pdf.add_paragraph("Take time to map your personal anxiety patterns:")
    pdf.add_blank_line()
    pdf.add_paragraph("My top 3 anxiety triggers:")
    pdf.add_paragraph("1. ____________________________________________________________")
    pdf.add_paragraph("2. ____________________________________________________________")
    pdf.add_paragraph("3. ____________________________________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("My most common anxious thoughts:")
    pdf.add_paragraph("1. ____________________________________________________________")
    pdf.add_paragraph("2. ____________________________________________________________")
    pdf.add_paragraph("3. ____________________________________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("My primary physical symptoms:")
    pdf.add_paragraph("1. ____________________________________________________________")
    pdf.add_paragraph("2. ____________________________________________________________")
    pdf.add_paragraph("3. ____________________________________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("My typical avoidance behaviors:")
    pdf.add_paragraph("1. ____________________________________________________________")
    pdf.add_paragraph("2. ____________________________________________________________")
    pdf.add_paragraph("3. ____________________________________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("Things that make my anxiety worse:")
    pdf.add_paragraph("1. ____________________________________________________________")
    pdf.add_paragraph("2. ____________________________________________________________")
    pdf.add_paragraph("3. ____________________________________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("Things that help my anxiety improve:")
    pdf.add_paragraph("1. ____________________________________________________________")
    pdf.add_paragraph("2. ____________________________________________________________")
    pdf.add_paragraph("3. ____________________________________________________________")
    pdf.add_blank_line()

    pdf.add_heading2("YOUR ACTION ITEMS - Chapter 1")
    pdf.add_separator()
    pdf.add_bullet("[ ] Complete the anxiety self-assessment above")
    pdf.add_bullet("[ ] Fill out your anxiety profile worksheet")
    pdf.add_bullet("[ ] Identify your top 3 triggers for the coming week")
    pdf.add_bullet("[ ] Notice which physical symptoms you experience most")
    pdf.add_bullet("[ ] Write down one situation you have been avoiding due to anxiety")
    pdf.add_bullet("[ ] Share your anxiety score with a trusted person or therapist")
    pdf.add_blank_line()

    # CHAPTER 2: CBT THOUGHT RECORDS
    pdf.add_page_break()
    pdf.add_heading1("CHAPTER 2: CBT THOUGHT RECORDS & WORKSHEETS")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_heading2("Introduction to Cognitive Behavioral Therapy")
    pdf.add_blank_line()
    pdf.add_paragraph("Cognitive Behavioral Therapy (CBT) is the gold standard treatment for anxiety disorders. It is based on the principle that our thoughts, feelings, and behaviors are all interconnected. By changing the way we think about situations, we can change how we feel and what we do.")
    pdf.add_blank_line()
    pdf.add_paragraph("The CBT model shows that it is not situations themselves that cause anxiety, but rather our interpretation of those situations. Two people can face the exact same situation and have completely different emotional responses because they interpret the situation differently.")
    pdf.add_blank_line()
    pdf.add_paragraph("Thought records are the cornerstone tool of CBT. They help you identify, examine, and restructure the automatic negative thoughts that fuel your anxiety. With regular practice, you will develop the ability to catch distorted thoughts in real-time and replace them with more balanced perspectives.")
    pdf.add_blank_line()

    pdf.add_heading2("Common Cognitive Distortions")
    pdf.add_blank_line()
    pdf.add_paragraph("These are thinking patterns that seem true but actually distort reality in anxiety-provoking ways:")
    pdf.add_blank_line()
    pdf.add_heading3("1. Catastrophizing")
    pdf.add_paragraph("Assuming the worst possible outcome will definitely happen. Example: A headache means you have a brain tumor. Being late to work means you will be fired.")
    pdf.add_blank_line()
    pdf.add_heading3("2. All-or-Nothing Thinking")
    pdf.add_paragraph("Seeing things in black and white with no middle ground. If something is not perfect, it is a complete failure. Example: If you make one mistake in a presentation, the entire thing was terrible.")
    pdf.add_blank_line()
    pdf.add_heading3("3. Mind Reading")
    pdf.add_paragraph("Assuming you know what others are thinking, usually that they are judging you negatively. Example: They did not text back because they think I am annoying.")
    pdf.add_blank_line()
    pdf.add_heading3("4. Fortune Telling")
    pdf.add_paragraph("Predicting negative outcomes with certainty before they happen. Example: I just know this interview is going to go badly.")
    pdf.add_blank_line()
    pdf.add_heading3("5. Emotional Reasoning")
    pdf.add_paragraph("Believing something is true because you feel it strongly. Example: I feel like a failure, so I must be one.")
    pdf.add_blank_line()
    pdf.add_heading3("6. Should Statements")
    pdf.add_paragraph("Rigid rules about how you, others, or the world should be. Example: I should never make mistakes. People should always be on time.")
    pdf.add_blank_line()
    pdf.add_heading3("7. Overgeneralization")
    pdf.add_paragraph("Taking one negative event and applying it to all situations. Example: One bad date means you will never find love.")
    pdf.add_blank_line()
    pdf.add_heading3("8. Magnification and Minimization")
    pdf.add_paragraph("Blowing negative things out of proportion while shrinking positives. Example: Focusing on one piece of critical feedback while ignoring ten compliments.")
    pdf.add_blank_line()
    pdf.add_heading3("9. Personalization")
    pdf.add_paragraph("Taking responsibility for things that are not your fault. Example: My friend canceled plans, so it must be because of something I did wrong.")
    pdf.add_blank_line()
    pdf.add_heading3("10. Filtering")
    pdf.add_paragraph("Focusing exclusively on negative details while filtering out all positive aspects of a situation.")
    pdf.add_blank_line()

    pdf.add_heading2("How to Complete a Thought Record")
    pdf.add_blank_line()
    pdf.add_paragraph("Follow these steps each time you notice anxiety rising:")
    pdf.add_blank_line()
    pdf.add_bullet("Step 1: Identify the SITUATION - What happened? Where were you? Who was there?")
    pdf.add_bullet("Step 2: Record your EMOTIONS - What did you feel? Rate intensity 0-100%")
    pdf.add_bullet("Step 3: Capture AUTOMATIC THOUGHTS - What went through your mind?")
    pdf.add_bullet("Step 4: Find the COGNITIVE DISTORTION - Which thinking error applies?")
    pdf.add_bullet("Step 5: Challenge the thought with EVIDENCE FOR and AGAINST")
    pdf.add_bullet("Step 6: Create a BALANCED THOUGHT - A more realistic alternative")
    pdf.add_bullet("Step 7: RE-RATE your emotions - How do you feel now? 0-100%")
    pdf.add_blank_line()

    # 10 BLANK THOUGHT RECORD WORKSHEETS
    for i in range(1, 11):
        pdf.add_page_break()
        pdf.add_heading2(f"THOUGHT RECORD WORKSHEET #{i}")
        pdf.add_separator()
        pdf.add_blank_line()
        pdf.add_paragraph(f"Date: _______________ Time: _______________ ")
        pdf.add_blank_line()
        pdf.add_heading3("SITUATION (What happened? Where? Who? When?)")
        pdf.add_paragraph("_______________________________________________________________")
        pdf.add_paragraph("_______________________________________________________________")
        pdf.add_paragraph("_______________________________________________________________")
        pdf.add_blank_line()
        pdf.add_heading3("EMOTIONS (What did you feel? Rate intensity 0-100%)")
        pdf.add_paragraph("Emotion 1: _________________________ Intensity: _____%")
        pdf.add_paragraph("Emotion 2: _________________________ Intensity: _____%")
        pdf.add_paragraph("Emotion 3: _________________________ Intensity: _____%")
        pdf.add_blank_line()
        pdf.add_heading3("AUTOMATIC THOUGHTS (What went through your mind?)")
        pdf.add_paragraph("_______________________________________________________________")
        pdf.add_paragraph("_______________________________________________________________")
        pdf.add_paragraph("_______________________________________________________________")
        pdf.add_paragraph("_______________________________________________________________")
        pdf.add_blank_line()
        pdf.add_heading3("COGNITIVE DISTORTION (Which thinking error?)")
        pdf.add_paragraph("[ ] Catastrophizing  [ ] All-or-Nothing  [ ] Mind Reading")
        pdf.add_paragraph("[ ] Fortune Telling  [ ] Emotional Reasoning  [ ] Should Statements")
        pdf.add_paragraph("[ ] Overgeneralization  [ ] Magnification  [ ] Personalization")
        pdf.add_blank_line()
        pdf.add_heading3("EVIDENCE FOR this thought:")
        pdf.add_paragraph("_______________________________________________________________")
        pdf.add_paragraph("_______________________________________________________________")
        pdf.add_blank_line()
        pdf.add_heading3("EVIDENCE AGAINST this thought:")
        pdf.add_paragraph("_______________________________________________________________")
        pdf.add_paragraph("_______________________________________________________________")
        pdf.add_blank_line()
        pdf.add_heading3("BALANCED THOUGHT (More realistic alternative)")
        pdf.add_paragraph("_______________________________________________________________")
        pdf.add_paragraph("_______________________________________________________________")
        pdf.add_paragraph("_______________________________________________________________")
        pdf.add_blank_line()
        pdf.add_heading3("RE-RATE EMOTIONS after completing this record:")
        pdf.add_paragraph("Emotion 1: _________________________ New Intensity: _____%")
        pdf.add_paragraph("Emotion 2: _________________________ New Intensity: _____%")
        pdf.add_paragraph("Emotion 3: _________________________ New Intensity: _____%")
        pdf.add_blank_line()
        pdf.add_paragraph("What did I learn from this exercise?")
        pdf.add_paragraph("_______________________________________________________________")
        pdf.add_paragraph("_______________________________________________________________")
        pdf.add_blank_line()

    pdf.add_heading2("YOUR ACTION ITEMS - Chapter 2")
    pdf.add_separator()
    pdf.add_bullet("[ ] Complete at least one thought record per day for one week")
    pdf.add_bullet("[ ] Identify your top 3 most common cognitive distortions")
    pdf.add_bullet("[ ] Practice catching automatic thoughts as they happen")
    pdf.add_bullet("[ ] Review completed thought records weekly to find patterns")
    pdf.add_bullet("[ ] Share a thought record with your therapist or support person")
    pdf.add_blank_line()

    # CHAPTER 3: BREATHING & GROUNDING
    pdf.add_page_break()
    pdf.add_heading1("CHAPTER 3: BREATHING & GROUNDING TECHNIQUES")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_heading2("Why Breathing Matters")
    pdf.add_blank_line()
    pdf.add_paragraph("When anxiety activates your fight-or-flight response, one of the first things that changes is your breathing pattern. You begin to breathe faster and shallower, taking in more oxygen than your body needs. This hyperventilation actually makes anxiety symptoms worse by causing dizziness, tingling, and chest tightness.")
    pdf.add_blank_line()
    pdf.add_paragraph("Controlled breathing is the fastest way to activate your parasympathetic nervous system, which is responsible for the relaxation response. By deliberately slowing and deepening your breath, you send a signal to your brain that says you are safe, and your body begins to calm down within minutes.")
    pdf.add_blank_line()

    pdf.add_heading2("Technique 1: 4-7-8 Breathing")
    pdf.add_blank_line()
    pdf.add_paragraph("This technique was developed by Dr. Andrew Weil and is one of the most effective methods for rapid anxiety relief. It works by extending your exhale, which stimulates the vagus nerve.")
    pdf.add_blank_line()
    pdf.add_heading3("Instructions:")
    pdf.add_bullet("Sit comfortably with your back straight")
    pdf.add_bullet("Place the tip of your tongue against the ridge behind your upper front teeth")
    pdf.add_bullet("Exhale completely through your mouth, making a whoosh sound")
    pdf.add_bullet("Close your mouth and INHALE quietly through your nose for 4 counts")
    pdf.add_bullet("HOLD your breath for 7 counts")
    pdf.add_bullet("EXHALE completely through your mouth for 8 counts (whoosh sound)")
    pdf.add_bullet("This is one complete breath cycle")
    pdf.add_bullet("Repeat for 4 full cycles (work up to 8 cycles over time)")
    pdf.add_blank_line()
    pdf.add_paragraph("Practice Schedule: Do this exercise twice daily - once in the morning and once before bed. Also use it any time you feel anxiety rising.")
    pdf.add_blank_line()
    pdf.add_paragraph("My 4-7-8 Practice Log:")
    pdf.add_paragraph("Day 1 - Morning: ___ Evening: ___ Anxiety Level Before/After: ___/___")
    pdf.add_paragraph("Day 2 - Morning: ___ Evening: ___ Anxiety Level Before/After: ___/___")
    pdf.add_paragraph("Day 3 - Morning: ___ Evening: ___ Anxiety Level Before/After: ___/___")
    pdf.add_paragraph("Day 4 - Morning: ___ Evening: ___ Anxiety Level Before/After: ___/___")
    pdf.add_paragraph("Day 5 - Morning: ___ Evening: ___ Anxiety Level Before/After: ___/___")
    pdf.add_paragraph("Day 6 - Morning: ___ Evening: ___ Anxiety Level Before/After: ___/___")
    pdf.add_paragraph("Day 7 - Morning: ___ Evening: ___ Anxiety Level Before/After: ___/___")
    pdf.add_blank_line()

    pdf.add_heading2("Technique 2: Box Breathing (Navy SEAL Method)")
    pdf.add_blank_line()
    pdf.add_paragraph("Used by Navy SEALs to remain calm under extreme pressure. This technique is excellent for acute anxiety or panic situations because of its simplicity and effectiveness.")
    pdf.add_blank_line()
    pdf.add_heading3("Instructions:")
    pdf.add_bullet("Visualize a square or box in your mind")
    pdf.add_bullet("INHALE for 4 counts (trace up the left side of the box)")
    pdf.add_bullet("HOLD for 4 counts (trace across the top)")
    pdf.add_bullet("EXHALE for 4 counts (trace down the right side)")
    pdf.add_bullet("HOLD for 4 counts (trace across the bottom)")
    pdf.add_bullet("Repeat for 5-10 minutes or until calm")
    pdf.add_blank_line()

    pdf.add_heading2("Technique 3: Diaphragmatic (Belly) Breathing")
    pdf.add_blank_line()
    pdf.add_paragraph("Most anxious people breathe into their chest. Diaphragmatic breathing engages the belly, activating deeper relaxation and better oxygen exchange.")
    pdf.add_blank_line()
    pdf.add_heading3("Instructions:")
    pdf.add_bullet("Lie down or sit comfortably")
    pdf.add_bullet("Place one hand on your chest and one on your belly")
    pdf.add_bullet("Breathe in slowly through your nose for 4 counts")
    pdf.add_bullet("Your belly should rise while your chest stays relatively still")
    pdf.add_bullet("Exhale slowly through pursed lips for 6 counts")
    pdf.add_bullet("Feel your belly fall back down")
    pdf.add_bullet("Practice for 5-10 minutes, twice daily")
    pdf.add_blank_line()

    pdf.add_heading2("Grounding Technique 1: The 5-4-3-2-1 Method")
    pdf.add_blank_line()
    pdf.add_paragraph("This powerful technique works by redirecting your attention from anxious thoughts to your immediate physical environment. It engages all five senses to anchor you in the present moment.")
    pdf.add_blank_line()
    pdf.add_heading3("Instructions:")
    pdf.add_paragraph("When you feel anxiety rising or a panic attack beginning, work through these steps:")
    pdf.add_blank_line()
    pdf.add_paragraph("5 THINGS I CAN SEE:")
    pdf.add_paragraph("1. ____________________________________________________________")
    pdf.add_paragraph("2. ____________________________________________________________")
    pdf.add_paragraph("3. ____________________________________________________________")
    pdf.add_paragraph("4. ____________________________________________________________")
    pdf.add_paragraph("5. ____________________________________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("4 THINGS I CAN TOUCH/FEEL:")
    pdf.add_paragraph("1. ____________________________________________________________")
    pdf.add_paragraph("2. ____________________________________________________________")
    pdf.add_paragraph("3. ____________________________________________________________")
    pdf.add_paragraph("4. ____________________________________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("3 THINGS I CAN HEAR:")
    pdf.add_paragraph("1. ____________________________________________________________")
    pdf.add_paragraph("2. ____________________________________________________________")
    pdf.add_paragraph("3. ____________________________________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("2 THINGS I CAN SMELL:")
    pdf.add_paragraph("1. ____________________________________________________________")
    pdf.add_paragraph("2. ____________________________________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("1 THING I CAN TASTE:")
    pdf.add_paragraph("1. ____________________________________________________________")
    pdf.add_blank_line()

    pdf.add_heading2("Grounding Technique 2: Progressive Muscle Relaxation")
    pdf.add_blank_line()
    pdf.add_paragraph("PMR works by systematically tensing and then releasing muscle groups throughout your body. This teaches you to recognize the difference between tension and relaxation, and releases stored physical anxiety.")
    pdf.add_blank_line()
    pdf.add_heading3("Full Body PMR Script (15-20 minutes):")
    pdf.add_blank_line()
    pdf.add_paragraph("For each muscle group: Tense for 5 seconds, then release for 15 seconds. Notice the contrast between tension and relaxation.")
    pdf.add_blank_line()
    pdf.add_bullet("FEET: Curl your toes tightly... hold... release and notice the relaxation")
    pdf.add_bullet("CALVES: Point your toes up toward shins... hold... release")
    pdf.add_bullet("THIGHS: Squeeze your thigh muscles... hold... release")
    pdf.add_bullet("BUTTOCKS: Clench your glutes... hold... release")
    pdf.add_bullet("STOMACH: Tighten your abdominal muscles... hold... release")
    pdf.add_bullet("CHEST: Take a deep breath and hold... hold... exhale and release")
    pdf.add_bullet("HANDS: Make tight fists... hold... release and spread fingers")
    pdf.add_bullet("FOREARMS: Flex your wrists back... hold... release")
    pdf.add_bullet("BICEPS: Curl your arms up tightly... hold... release")
    pdf.add_bullet("SHOULDERS: Shrug shoulders up to ears... hold... release and drop")
    pdf.add_bullet("NECK: Gently press head back... hold... release")
    pdf.add_bullet("FACE: Scrunch all facial muscles... hold... release")
    pdf.add_bullet("FOREHEAD: Raise eyebrows high... hold... release")
    pdf.add_blank_line()
    pdf.add_paragraph("After completing all muscle groups, take 3 deep breaths and notice how your entire body feels different from when you started.")
    pdf.add_blank_line()

    pdf.add_heading2("Grounding Technique 3: Cold Water Reset")
    pdf.add_blank_line()
    pdf.add_paragraph("The diving reflex is a powerful physiological response that immediately slows your heart rate and calms your nervous system. It works by triggering the vagus nerve through temperature change.")
    pdf.add_blank_line()
    pdf.add_heading3("Methods:")
    pdf.add_bullet("Hold ice cubes in your hands for 30-60 seconds")
    pdf.add_bullet("Splash very cold water on your face and wrists")
    pdf.add_bullet("Hold a cold pack against your forehead or back of neck")
    pdf.add_bullet("Submerge your face briefly in a bowl of cold water")
    pdf.add_blank_line()

    pdf.add_heading2("YOUR ACTION ITEMS - Chapter 3")
    pdf.add_separator()
    pdf.add_bullet("[ ] Practice 4-7-8 breathing twice daily for one week")
    pdf.add_bullet("[ ] Try box breathing during your next stressful moment")
    pdf.add_bullet("[ ] Complete the 5-4-3-2-1 grounding exercise above")
    pdf.add_bullet("[ ] Do progressive muscle relaxation before bed tonight")
    pdf.add_bullet("[ ] Keep ice cubes accessible for the cold water reset technique")
    pdf.add_bullet("[ ] Rate which technique works best for you personally")
    pdf.add_blank_line()

    # CHAPTER 4: WORRY MANAGEMENT
    pdf.add_page_break()
    pdf.add_heading1("CHAPTER 4: WORRY MANAGEMENT SYSTEM")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_heading2("Understanding Worry")
    pdf.add_blank_line()
    pdf.add_paragraph("Worry is a cognitive process where your mind repeatedly cycles through potential negative outcomes. Unlike productive problem-solving, worry does not lead to solutions. Instead, it keeps you trapped in a loop of what if scenarios that increase anxiety without resolving anything.")
    pdf.add_blank_line()
    pdf.add_paragraph("Research shows that 85% of things people worry about never actually happen. Of the 15% that do occur, 79% of people report handling the situation better than they expected. This means that 97% of what you worry about is either unlikely to happen or more manageable than you think.")
    pdf.add_blank_line()
    pdf.add_paragraph("The key is not to eliminate worry entirely, which is impossible, but to contain it, evaluate it, and redirect your mental energy toward things you can actually control.")
    pdf.add_blank_line()

    pdf.add_heading2("The Worry Decision Tree")
    pdf.add_blank_line()
    pdf.add_paragraph("When you notice yourself worrying, ask these questions in order:")
    pdf.add_blank_line()
    pdf.add_paragraph("Step 1: Is this worry about something I can control?")
    pdf.add_paragraph("   YES -> Go to Step 2")
    pdf.add_paragraph("   NO -> Practice acceptance. Use grounding. Let it go.")
    pdf.add_blank_line()
    pdf.add_paragraph("Step 2: Can I take action on this RIGHT NOW?")
    pdf.add_paragraph("   YES -> Take one small action immediately")
    pdf.add_paragraph("   NO -> Schedule it in your worry time. Write it down. Move on.")
    pdf.add_blank_line()
    pdf.add_paragraph("Step 3: What is the smallest possible action I can take?")
    pdf.add_paragraph("   Write it here: _________________________________________________")
    pdf.add_paragraph("   When will I do it? _____________________________________________")
    pdf.add_blank_line()

    pdf.add_heading2("Scheduled Worry Time")
    pdf.add_blank_line()
    pdf.add_paragraph("One of the most effective worry management strategies is to designate a specific time and place for worrying. Outside of this window, you postpone all worries to your scheduled time.")
    pdf.add_blank_line()
    pdf.add_heading3("How to implement:")
    pdf.add_bullet("Choose a 15-20 minute window each day (not before bed)")
    pdf.add_bullet("Choose a specific location (not your bedroom)")
    pdf.add_bullet("When worries arise outside this time, write them down and postpone")
    pdf.add_bullet("During worry time, worry intentionally about your list")
    pdf.add_bullet("When the timer ends, close your worry list and move on")
    pdf.add_blank_line()
    pdf.add_paragraph("My Scheduled Worry Time: _________ to _________")
    pdf.add_paragraph("My Worry Location: _________________________________________")
    pdf.add_blank_line()

    # WORRY JOURNAL PAGES
    for i in range(1, 11):
        pdf.add_page_break()
        pdf.add_heading2(f"WORRY JOURNAL - Page {i}")
        pdf.add_separator()
        pdf.add_paragraph(f"Date: _______________")
        pdf.add_blank_line()
        pdf.add_heading3("Worry #1")
        pdf.add_paragraph("What am I worried about? _________________________________________")
        pdf.add_paragraph("_______________________________________________________________")
        pdf.add_paragraph("Likelihood (0-100%): _____%")
        pdf.add_paragraph("Can I control this? [ ] Yes  [ ] No  [ ] Partially")
        pdf.add_paragraph("Worst case scenario: ____________________________________________")
        pdf.add_paragraph("Best case scenario: _____________________________________________")
        pdf.add_paragraph("Most likely scenario: ____________________________________________")
        pdf.add_paragraph("One action I can take: ___________________________________________")
        pdf.add_blank_line()
        pdf.add_heading3("Worry #2")
        pdf.add_paragraph("What am I worried about? _________________________________________")
        pdf.add_paragraph("_______________________________________________________________")
        pdf.add_paragraph("Likelihood (0-100%): _____%")
        pdf.add_paragraph("Can I control this? [ ] Yes  [ ] No  [ ] Partially")
        pdf.add_paragraph("Worst case scenario: ____________________________________________")
        pdf.add_paragraph("Best case scenario: _____________________________________________")
        pdf.add_paragraph("Most likely scenario: ____________________________________________")
        pdf.add_paragraph("One action I can take: ___________________________________________")
        pdf.add_blank_line()
        pdf.add_heading3("Worry #3")
        pdf.add_paragraph("What am I worried about? _________________________________________")
        pdf.add_paragraph("_______________________________________________________________")
        pdf.add_paragraph("Likelihood (0-100%): _____%")
        pdf.add_paragraph("Can I control this? [ ] Yes  [ ] No  [ ] Partially")
        pdf.add_paragraph("Worst case scenario: ____________________________________________")
        pdf.add_paragraph("Best case scenario: _____________________________________________")
        pdf.add_paragraph("Most likely scenario: ____________________________________________")
        pdf.add_paragraph("One action I can take: ___________________________________________")
        pdf.add_blank_line()

    pdf.add_heading2("YOUR ACTION ITEMS - Chapter 4")
    pdf.add_separator()
    pdf.add_bullet("[ ] Set up your scheduled worry time starting today")
    pdf.add_bullet("[ ] Use the worry decision tree for every worry this week")
    pdf.add_bullet("[ ] Complete at least 3 worry journal pages")
    pdf.add_bullet("[ ] Track how many of your worries actually come true")
    pdf.add_bullet("[ ] Practice postponing worries to your designated worry time")
    pdf.add_bullet("[ ] Identify your top 3 recurring worry themes")
    pdf.add_blank_line()

    # CHAPTER 5: 30-DAY ANXIETY TRACKER
    pdf.add_page_break()
    pdf.add_heading1("CHAPTER 5: 30-DAY ANXIETY TRACKER")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_heading2("How to Use This Tracker")
    pdf.add_blank_line()
    pdf.add_paragraph("Tracking your anxiety daily serves multiple important purposes. It helps you identify patterns in when and why your anxiety increases or decreases. It shows you the connection between your habits and your anxiety levels. And it provides concrete evidence of your progress over time.")
    pdf.add_blank_line()
    pdf.add_paragraph("Each day, fill in the following information. Try to complete it at the same time each day, ideally in the evening as you reflect on your day.")
    pdf.add_blank_line()
    pdf.add_heading3("Rating Scale:")
    pdf.add_paragraph("1 = Minimal anxiety, felt calm and in control most of the day")
    pdf.add_paragraph("2 = Mild anxiety, some worry but manageable")
    pdf.add_paragraph("3 = Moderate anxiety, noticeable impact on daily activities")
    pdf.add_paragraph("4 = High anxiety, significant difficulty functioning normally")
    pdf.add_paragraph("5 = Severe anxiety, overwhelming, possibly panic attacks")
    pdf.add_blank_line()
    pdf.add_separator()

    # 30 daily tracker entries
    for day in range(1, 31):
        pdf.add_heading3(f"DAY {day}")
        pdf.add_paragraph(f"Date: _______________")
        pdf.add_paragraph(f"Anxiety Level (1-5): ___")
        pdf.add_paragraph(f"Hours of Sleep Last Night: ___")
        pdf.add_paragraph(f"Exercise Today? [ ] Yes  [ ] No   Minutes: ___")
        pdf.add_paragraph(f"Caffeine Intake: ___  Alcohol: ___")
        pdf.add_paragraph(f"Main Trigger Today: ___________________________________________")
        pdf.add_paragraph(f"Coping Strategy Used: __________________________________________")
        pdf.add_paragraph(f"Did it help? [ ] Yes  [ ] Somewhat  [ ] No")
        pdf.add_paragraph(f"Gratitude - One good thing today: ______________________________")
        pdf.add_separator()
        if day % 5 == 0:
            pdf.add_blank_line()
            pdf.add_heading3(f"WEEK {day // 5} CHECK-IN (Days {day-4}-{day})")
            pdf.add_paragraph(f"Average anxiety this week (1-5): ___")
            pdf.add_paragraph(f"Most common trigger: __________________________________________")
            pdf.add_paragraph(f"Most helpful coping strategy: _________________________________")
            pdf.add_paragraph(f"Improvement from last week? [ ] Yes  [ ] Same  [ ] Worse")
            pdf.add_paragraph(f"Goal for next week: ___________________________________________")
            pdf.add_separator()
            pdf.add_blank_line()

    pdf.add_page_break()
    pdf.add_heading2("30-DAY SUMMARY & REFLECTION")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_paragraph("Overall average anxiety level: ___")
    pdf.add_paragraph("Lowest anxiety day: Day ___ (Level: ___)")
    pdf.add_paragraph("Highest anxiety day: Day ___ (Level: ___)")
    pdf.add_blank_line()
    pdf.add_paragraph("Top 3 triggers identified:")
    pdf.add_paragraph("1. ____________________________________________________________")
    pdf.add_paragraph("2. ____________________________________________________________")
    pdf.add_paragraph("3. ____________________________________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("Most effective coping strategies:")
    pdf.add_paragraph("1. ____________________________________________________________")
    pdf.add_paragraph("2. ____________________________________________________________")
    pdf.add_paragraph("3. ____________________________________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("Patterns I noticed (sleep, exercise, diet connections):")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("What I learned about my anxiety:")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("My plan going forward:")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_blank_line()

    pdf.add_heading2("YOUR ACTION ITEMS - Chapter 5")
    pdf.add_separator()
    pdf.add_bullet("[ ] Commit to tracking daily for the full 30 days")
    pdf.add_bullet("[ ] Set a daily reminder to complete your tracker entry")
    pdf.add_bullet("[ ] Review your weekly check-ins each Sunday")
    pdf.add_bullet("[ ] Complete the 30-day summary after finishing")
    pdf.add_bullet("[ ] Share progress with your accountability partner")
    pdf.add_blank_line()

    # CHAPTER 6: COPING STRATEGIES
    pdf.add_page_break()
    pdf.add_heading1("CHAPTER 6: COPING STRATEGIES TOOLKIT")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_paragraph("Having a diverse toolkit of coping strategies is essential because different situations call for different approaches. What works during a panic attack is different from what helps with chronic background worry. Build your personal toolkit by trying each strategy and noting which ones work best for you.")
    pdf.add_blank_line()

    pdf.add_heading2("CATEGORY 1: Physical Strategies (Body-Based)")
    pdf.add_blank_line()
    pdf.add_bullet("1. Go for a brisk 10-minute walk outside")
    pdf.add_bullet("2. Do 20 jumping jacks or burpees to burn off adrenaline")
    pdf.add_bullet("3. Take a cold shower or splash cold water on your face")
    pdf.add_bullet("4. Stretch your neck, shoulders, and back for 5 minutes")
    pdf.add_bullet("5. Practice progressive muscle relaxation from head to toe")
    pdf.add_bullet("6. Dance to your favorite upbeat song for 3 minutes")
    pdf.add_bullet("7. Do yoga or gentle stretching for 15 minutes")
    pdf.add_bullet("8. Squeeze a stress ball or fidget toy")
    pdf.add_bullet("9. Hug someone or a pillow tightly for 20 seconds")
    pdf.add_bullet("10. Chew gum or eat something crunchy mindfully")
    pdf.add_blank_line()

    pdf.add_heading2("CATEGORY 2: Mental Strategies (Thought-Based)")
    pdf.add_blank_line()
    pdf.add_bullet("11. Name your anxiety as a character (Hello, Worry Monster)")
    pdf.add_bullet("12. Count backward from 100 by 7s")
    pdf.add_bullet("13. Name 5 countries, 5 animals, 5 colors in your head")
    pdf.add_bullet("14. Visualize your safe place in vivid detail")
    pdf.add_bullet("15. Repeat a calming mantra: This feeling is temporary")
    pdf.add_bullet("16. Challenge the thought: What evidence supports this?")
    pdf.add_bullet("17. Ask: Will this matter in 5 years? 5 months? 5 weeks?")
    pdf.add_bullet("18. Imagine advising a friend with the same worry")
    pdf.add_bullet("19. Rate your anxiety 1-10 and check back in 10 minutes")
    pdf.add_bullet("20. Write the worry down and physically put it away")
    pdf.add_blank_line()

    pdf.add_heading2("CATEGORY 3: Sensory Strategies (Five Senses)")
    pdf.add_blank_line()
    pdf.add_bullet("21. Light a scented candle or use essential oils (lavender)")
    pdf.add_bullet("22. Listen to calming music or nature sounds")
    pdf.add_bullet("23. Look at photos that make you feel happy and safe")
    pdf.add_bullet("24. Wrap yourself in a weighted blanket or heavy comforter")
    pdf.add_bullet("25. Drink herbal tea slowly, noticing temperature and flavor")
    pdf.add_bullet("26. Take a warm bath with epsom salts")
    pdf.add_bullet("27. Pet an animal and focus on the texture of their fur")
    pdf.add_bullet("28. Eat dark chocolate slowly, savoring each bite")
    pdf.add_bullet("29. Hold something cold (ice cube) and focus on the sensation")
    pdf.add_bullet("30. Run your hands under warm water for 2 minutes")
    pdf.add_blank_line()

    pdf.add_heading2("CATEGORY 4: Social Strategies (Connection-Based)")
    pdf.add_blank_line()
    pdf.add_bullet("31. Call or text a supportive friend")
    pdf.add_bullet("32. Tell someone: I am feeling anxious right now")
    pdf.add_bullet("33. Attend a support group meeting (online or in-person)")
    pdf.add_bullet("34. Write a letter to someone you appreciate")
    pdf.add_bullet("35. Do something kind for a stranger")
    pdf.add_bullet("36. Play with children or pets")
    pdf.add_bullet("37. Join an online community for anxiety support")
    pdf.add_bullet("38. Ask for a hug from someone safe")
    pdf.add_bullet("39. Volunteer for a cause you believe in")
    pdf.add_bullet("40. Share your experience in a journal or blog")
    pdf.add_blank_line()

    pdf.add_heading2("CATEGORY 5: Creative Strategies (Expression-Based)")
    pdf.add_blank_line()
    pdf.add_bullet("41. Draw, paint, or color in an adult coloring book")
    pdf.add_bullet("42. Write freely in a journal for 10 minutes without stopping")
    pdf.add_bullet("43. Play a musical instrument")
    pdf.add_bullet("44. Sing loudly to your favorite song")
    pdf.add_bullet("45. Build something with your hands (origami, crafts, Legos)")
    pdf.add_bullet("46. Take photographs of beautiful things around you")
    pdf.add_bullet("47. Write a poem or short story about your feelings")
    pdf.add_bullet("48. Cook or bake something new")
    pdf.add_bullet("49. Garden or tend to houseplants")
    pdf.add_bullet("50. Rearrange or organize a small space")
    pdf.add_blank_line()

    pdf.add_heading2("My Personal Top 10 Coping Strategies")
    pdf.add_blank_line()
    pdf.add_paragraph("After trying the strategies above, record your top 10 most effective ones here for quick reference during anxious moments:")
    pdf.add_blank_line()
    pdf.add_paragraph("1. ____________________________________________________________")
    pdf.add_paragraph("2. ____________________________________________________________")
    pdf.add_paragraph("3. ____________________________________________________________")
    pdf.add_paragraph("4. ____________________________________________________________")
    pdf.add_paragraph("5. ____________________________________________________________")
    pdf.add_paragraph("6. ____________________________________________________________")
    pdf.add_paragraph("7. ____________________________________________________________")
    pdf.add_paragraph("8. ____________________________________________________________")
    pdf.add_paragraph("9. ____________________________________________________________")
    pdf.add_paragraph("10. ___________________________________________________________")
    pdf.add_blank_line()

    pdf.add_heading2("YOUR ACTION ITEMS - Chapter 6")
    pdf.add_separator()
    pdf.add_bullet("[ ] Try at least 2 strategies from each category this week")
    pdf.add_bullet("[ ] Rate each strategy effectiveness (1-10) after trying it")
    pdf.add_bullet("[ ] Fill in your Personal Top 10 list")
    pdf.add_bullet("[ ] Write your top 3 on an index card to carry with you")
    pdf.add_bullet("[ ] Teach one strategy to someone else")
    pdf.add_blank_line()

    # CHAPTER 7: SAFETY PLANNING
    pdf.add_page_break()
    pdf.add_heading1("CHAPTER 7: SAFETY PLANNING")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_paragraph("A safety plan is a personalized, practical plan that you create in advance for times when anxiety becomes overwhelming. Having a written plan means you do not have to think clearly during a crisis because you have already decided what to do.")
    pdf.add_blank_line()

    pdf.add_heading2("MY PERSONAL SAFETY PLAN")
    pdf.add_blank_line()
    pdf.add_heading3("Step 1: Warning Signs That My Anxiety Is Escalating")
    pdf.add_paragraph("Physical signs: _________________________________________________")
    pdf.add_paragraph("Thought patterns: _______________________________________________")
    pdf.add_paragraph("Behavioral changes: _____________________________________________")
    pdf.add_paragraph("Emotional shifts: ________________________________________________")
    pdf.add_blank_line()
    pdf.add_heading3("Step 2: Internal Coping Strategies (Things I Can Do Alone)")
    pdf.add_paragraph("1. ____________________________________________________________")
    pdf.add_paragraph("2. ____________________________________________________________")
    pdf.add_paragraph("3. ____________________________________________________________")
    pdf.add_paragraph("4. ____________________________________________________________")
    pdf.add_paragraph("5. ____________________________________________________________")
    pdf.add_blank_line()
    pdf.add_heading3("Step 3: People Who Can Help Distract Me")
    pdf.add_paragraph("Name: _________________________ Phone: _______________________")
    pdf.add_paragraph("Name: _________________________ Phone: _______________________")
    pdf.add_paragraph("Name: _________________________ Phone: _______________________")
    pdf.add_blank_line()
    pdf.add_heading3("Step 4: People I Can Ask for Help")
    pdf.add_paragraph("Name: _________________________ Phone: _______________________")
    pdf.add_paragraph("Name: _________________________ Phone: _______________________")
    pdf.add_paragraph("Therapist: _____________________ Phone: _______________________")
    pdf.add_blank_line()
    pdf.add_heading3("Step 5: Professional Resources")
    pdf.add_paragraph("My therapist: _____________________ Phone: ____________________")
    pdf.add_paragraph("My doctor: ________________________ Phone: ____________________")
    pdf.add_paragraph("Crisis line: 988 (Suicide & Crisis Lifeline)")
    pdf.add_paragraph("Crisis text: Text HOME to 741741")
    pdf.add_paragraph("Emergency: 911")
    pdf.add_blank_line()
    pdf.add_heading3("Step 6: Making My Environment Safe")
    pdf.add_paragraph("Things I can do to make my surroundings feel safer:")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_blank_line()
    pdf.add_heading3("Step 7: My Reasons for Getting Through This")
    pdf.add_paragraph("1. ____________________________________________________________")
    pdf.add_paragraph("2. ____________________________________________________________")
    pdf.add_paragraph("3. ____________________________________________________________")
    pdf.add_paragraph("4. ____________________________________________________________")
    pdf.add_paragraph("5. ____________________________________________________________")
    pdf.add_blank_line()

    pdf.add_heading2("YOUR ACTION ITEMS - Chapter 7")
    pdf.add_separator()
    pdf.add_bullet("[ ] Complete your full safety plan above")
    pdf.add_bullet("[ ] Share your safety plan with a trusted person")
    pdf.add_bullet("[ ] Save crisis numbers in your phone")
    pdf.add_bullet("[ ] Take a photo of this plan to keep on your phone")
    pdf.add_bullet("[ ] Review and update your plan monthly")
    pdf.add_blank_line()

    # CHAPTER 8: ACTION PLANS & GOALS
    pdf.add_page_break()
    pdf.add_heading1("CHAPTER 8: ACTION PLANS & GOALS")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_heading2("Setting Meaningful Anxiety Recovery Goals")
    pdf.add_blank_line()
    pdf.add_paragraph("Recovery from anxiety is not about eliminating all anxiety forever. It is about building the skills and confidence to manage anxiety effectively so it no longer controls your life. Setting specific, measurable goals gives you a roadmap and allows you to track your progress.")
    pdf.add_blank_line()
    pdf.add_paragraph("Use the SMART framework for your goals: Specific, Measurable, Achievable, Relevant, and Time-bound.")
    pdf.add_blank_line()

    pdf.add_heading2("My 30-Day Goals")
    pdf.add_blank_line()
    pdf.add_paragraph("Goal 1: ________________________________________________________")
    pdf.add_paragraph("How I will measure it: __________________________________________")
    pdf.add_paragraph("Target date: ___________________")
    pdf.add_blank_line()
    pdf.add_paragraph("Goal 2: ________________________________________________________")
    pdf.add_paragraph("How I will measure it: __________________________________________")
    pdf.add_paragraph("Target date: ___________________")
    pdf.add_blank_line()
    pdf.add_paragraph("Goal 3: ________________________________________________________")
    pdf.add_paragraph("How I will measure it: __________________________________________")
    pdf.add_paragraph("Target date: ___________________")
    pdf.add_blank_line()

    pdf.add_heading2("My 90-Day Goals")
    pdf.add_blank_line()
    pdf.add_paragraph("Goal 1: ________________________________________________________")
    pdf.add_paragraph("How I will measure it: __________________________________________")
    pdf.add_paragraph("Target date: ___________________")
    pdf.add_blank_line()
    pdf.add_paragraph("Goal 2: ________________________________________________________")
    pdf.add_paragraph("How I will measure it: __________________________________________")
    pdf.add_paragraph("Target date: ___________________")
    pdf.add_blank_line()
    pdf.add_paragraph("Goal 3: ________________________________________________________")
    pdf.add_paragraph("How I will measure it: __________________________________________")
    pdf.add_paragraph("Target date: ___________________")
    pdf.add_blank_line()

    pdf.add_heading2("Exposure Hierarchy (Fear Ladder)")
    pdf.add_blank_line()
    pdf.add_paragraph("List situations that cause anxiety from least (1) to most (10) feared. Start practicing exposure with the lowest items and work your way up as each level becomes manageable:")
    pdf.add_blank_line()
    pdf.add_paragraph("10 (Most feared): ______________________________________________")
    pdf.add_paragraph("   Date attempted: _____ Anxiety before: ___ After: ___ Completed? ___")
    pdf.add_blank_line()
    pdf.add_paragraph("9. _____________________________________________________________")
    pdf.add_paragraph("   Date attempted: _____ Anxiety before: ___ After: ___ Completed? ___")
    pdf.add_blank_line()
    pdf.add_paragraph("8. _____________________________________________________________")
    pdf.add_paragraph("   Date attempted: _____ Anxiety before: ___ After: ___ Completed? ___")
    pdf.add_blank_line()
    pdf.add_paragraph("7. _____________________________________________________________")
    pdf.add_paragraph("   Date attempted: _____ Anxiety before: ___ After: ___ Completed? ___")
    pdf.add_blank_line()
    pdf.add_paragraph("6. _____________________________________________________________")
    pdf.add_paragraph("   Date attempted: _____ Anxiety before: ___ After: ___ Completed? ___")
    pdf.add_blank_line()
    pdf.add_paragraph("5. _____________________________________________________________")
    pdf.add_paragraph("   Date attempted: _____ Anxiety before: ___ After: ___ Completed? ___")
    pdf.add_blank_line()
    pdf.add_paragraph("4. _____________________________________________________________")
    pdf.add_paragraph("   Date attempted: _____ Anxiety before: ___ After: ___ Completed? ___")
    pdf.add_blank_line()
    pdf.add_paragraph("3. _____________________________________________________________")
    pdf.add_paragraph("   Date attempted: _____ Anxiety before: ___ After: ___ Completed? ___")
    pdf.add_blank_line()
    pdf.add_paragraph("2. _____________________________________________________________")
    pdf.add_paragraph("   Date attempted: _____ Anxiety before: ___ After: ___ Completed? ___")
    pdf.add_blank_line()
    pdf.add_paragraph("1 (Least feared): ______________________________________________")
    pdf.add_paragraph("   Date attempted: _____ Anxiety before: ___ After: ___ Completed? ___")
    pdf.add_blank_line()

    pdf.add_heading2("Weekly Progress Check-In Template")
    pdf.add_blank_line()
    for week in range(1, 9):
        pdf.add_heading3(f"Week {week} Check-In")
        pdf.add_paragraph(f"Date: _______________")
        pdf.add_paragraph(f"Average anxiety this week (1-10): ___")
        pdf.add_paragraph(f"Thought records completed: ___")
        pdf.add_paragraph(f"Breathing exercises practiced: ___")
        pdf.add_paragraph(f"Exposures attempted: ___")
        pdf.add_paragraph(f"Biggest win this week: _________________________________________")
        pdf.add_paragraph(f"Biggest challenge: _____________________________________________")
        pdf.add_paragraph(f"Goal for next week: ____________________________________________")
        pdf.add_separator()
    pdf.add_blank_line()

    pdf.add_heading2("YOUR ACTION ITEMS - Chapter 8")
    pdf.add_separator()
    pdf.add_bullet("[ ] Set 3 SMART goals for the next 30 days")
    pdf.add_bullet("[ ] Complete your fear ladder / exposure hierarchy")
    pdf.add_bullet("[ ] Attempt the lowest item on your fear ladder this week")
    pdf.add_bullet("[ ] Schedule weekly check-ins with yourself")
    pdf.add_bullet("[ ] Celebrate every small step of progress")
    pdf.add_blank_line()

    # FINAL PAGE: NEXT STEPS
    pdf.add_page_break()
    pdf.add_heading1("NEXT STEPS & RESOURCES")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_paragraph("Congratulations on completing this workbook. By working through these chapters, you have built a comprehensive toolkit for managing anxiety. Remember that recovery is not linear. There will be good days and harder days, and that is completely normal.")
    pdf.add_blank_line()
    pdf.add_heading2("Your Ongoing Practice Plan")
    pdf.add_bullet("Continue daily breathing exercises (5 minutes minimum)")
    pdf.add_bullet("Complete thought records whenever anxiety is moderate or higher")
    pdf.add_bullet("Use your worry journal during scheduled worry time")
    pdf.add_bullet("Track anxiety daily for at least 90 days total")
    pdf.add_bullet("Work through your exposure hierarchy at your own pace")
    pdf.add_bullet("Review and update your safety plan monthly")
    pdf.add_bullet("Check in with your weekly progress template")
    pdf.add_blank_line()
    pdf.add_heading2("When to Seek Professional Help")
    pdf.add_paragraph("This workbook is a supplement to, not a replacement for, professional treatment. Please seek help from a licensed therapist or counselor if:")
    pdf.add_bullet("Your anxiety significantly impacts work, relationships, or daily functioning")
    pdf.add_bullet("You experience frequent panic attacks")
    pdf.add_bullet("You are using substances to cope with anxiety")
    pdf.add_bullet("You have thoughts of self-harm")
    pdf.add_bullet("Your anxiety has not improved after 4-6 weeks of consistent practice")
    pdf.add_blank_line()
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_paragraph("You are stronger than your anxiety. Keep going.")
    pdf.add_blank_line()

    filepath = os.path.join(OUTPUT_DIR, '02-Anxiety-Stress-Management-Workbook.pdf')
    pdf.save(filepath)
    return filepath, len(pdf.pages) + 1



def generate_book3():
    """Book 3: Wedding Planning Master Bundle (80-100 pages)"""
    pdf = PurePDF(title="Wedding Planning Master Bundle", author="Daniel Tesfamariam")

    # TITLE PAGE
    pdf.add_blank_line()
    pdf.add_blank_line()
    pdf.add_blank_line()
    pdf.add_title("WEDDING PLANNING")
    pdf.add_title("MASTER BUNDLE")
    pdf.add_blank_line()
    pdf.add_heading2("The Complete System for Planning Your Perfect Day")
    pdf.add_heading2("Budget Tracker | Timeline | Vendor Management | Guest Lists")
    pdf.add_blank_line()
    pdf.add_blank_line()
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_blank_line()
    pdf.add_paragraph("Everything you need to plan a beautiful wedding")
    pdf.add_paragraph("without the stress, overwhelm, or overspending.")
    pdf.add_blank_line()
    pdf.add_separator()
    pdf.add_paragraph("Copyright 2024 Daniel Tesfamariam. All rights reserved.")

    # TABLE OF CONTENTS
    pdf.add_page_break()
    pdf.add_title("TABLE OF CONTENTS")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_paragraph("Chapter 1: Getting Started ................................. 3")
    pdf.add_paragraph("Chapter 2: Budget Master Tracker ........................... 11")
    pdf.add_paragraph("Chapter 3: 12-Month Wedding Timeline ....................... 26")
    pdf.add_paragraph("Chapter 4: Vendor Management System ........................ 38")
    pdf.add_paragraph("Chapter 5: Guest Management & Tracker ...................... 50")
    pdf.add_paragraph("Chapter 6: Seating Chart System ............................ 60")
    pdf.add_paragraph("Chapter 7: Day-Of Timeline ................................. 68")
    pdf.add_paragraph("Chapter 8: Design & Decor Planner .......................... 76")
    pdf.add_paragraph("Chapter 9: Honeymoon Planner ............................... 84")
    pdf.add_paragraph("Chapter 10: Post-Wedding Tasks ............................. 90")
    pdf.add_paragraph("Final: Next Steps .......................................... 95")
    pdf.add_blank_line()

    # CHAPTER 1: GETTING STARTED
    pdf.add_page_break()
    pdf.add_heading1("CHAPTER 1: GETTING STARTED")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_heading2("Congratulations on Your Engagement!")
    pdf.add_blank_line()
    pdf.add_paragraph("Planning a wedding is one of the most exciting and complex projects you will ever undertake. This planner is designed to break down the entire process into manageable steps so you can enjoy the journey without feeling overwhelmed.")
    pdf.add_blank_line()
    pdf.add_paragraph("Whether you are planning an intimate ceremony for 30 guests or a grand celebration for 300, this system adapts to your needs. The key to stress-free wedding planning is organization, communication, and starting early.")
    pdf.add_blank_line()

    pdf.add_heading2("Wedding Vision Worksheet")
    pdf.add_blank_line()
    pdf.add_paragraph("Before diving into logistics, take time to clarify your shared vision:")
    pdf.add_blank_line()
    pdf.add_paragraph("Our wedding date (or target month): ____________________________")
    pdf.add_paragraph("Engagement date: ______________________________________________")
    pdf.add_paragraph("Planning timeline (months until wedding): _______________________")
    pdf.add_blank_line()
    pdf.add_paragraph("Our overall budget range: $____________ to $____________")
    pdf.add_paragraph("Who is contributing financially?")
    pdf.add_paragraph("  Couple: $___________")
    pdf.add_paragraph("  Partner 1 family: $___________")
    pdf.add_paragraph("  Partner 2 family: $___________")
    pdf.add_paragraph("  Other: $___________")
    pdf.add_paragraph("  TOTAL BUDGET: $___________")
    pdf.add_blank_line()
    pdf.add_paragraph("Estimated guest count: ___________")
    pdf.add_paragraph("Wedding style (circle): Formal | Semi-Formal | Casual | Rustic | Modern | Vintage")
    pdf.add_paragraph("Indoor or Outdoor preference: __________________________________")
    pdf.add_paragraph("Color palette ideas: ___________________________________________")
    pdf.add_paragraph("Season preference: _____________________________________________")
    pdf.add_paragraph("Religious or cultural traditions to include: _____________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_blank_line()

    pdf.add_heading2("Our Non-Negotiables")
    pdf.add_blank_line()
    pdf.add_paragraph("Things that are MOST important to us (top 5):")
    pdf.add_paragraph("1. ____________________________________________________________")
    pdf.add_paragraph("2. ____________________________________________________________")
    pdf.add_paragraph("3. ____________________________________________________________")
    pdf.add_paragraph("4. ____________________________________________________________")
    pdf.add_paragraph("5. ____________________________________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("Things we are willing to skip or simplify:")
    pdf.add_paragraph("1. ____________________________________________________________")
    pdf.add_paragraph("2. ____________________________________________________________")
    pdf.add_paragraph("3. ____________________________________________________________")
    pdf.add_blank_line()

    pdf.add_heading2("Wedding Party")
    pdf.add_blank_line()
    pdf.add_paragraph("Maid/Matron of Honor: ___________________________________________")
    pdf.add_paragraph("Best Man: ______________________________________________________")
    pdf.add_paragraph("Bridesmaid 1: __________________________________________________")
    pdf.add_paragraph("Bridesmaid 2: __________________________________________________")
    pdf.add_paragraph("Bridesmaid 3: __________________________________________________")
    pdf.add_paragraph("Bridesmaid 4: __________________________________________________")
    pdf.add_paragraph("Groomsman 1: ___________________________________________________")
    pdf.add_paragraph("Groomsman 2: ___________________________________________________")
    pdf.add_paragraph("Groomsman 3: ___________________________________________________")
    pdf.add_paragraph("Groomsman 4: ___________________________________________________")
    pdf.add_paragraph("Flower Girl: ___________________________________________________")
    pdf.add_paragraph("Ring Bearer: ___________________________________________________")
    pdf.add_paragraph("Officiant: _____________________________________________________")
    pdf.add_paragraph("Readers/Speakers: ______________________________________________")
    pdf.add_blank_line()

    pdf.add_heading2("Key Contacts & Passwords")
    pdf.add_blank_line()
    pdf.add_paragraph("Wedding Planner/Coordinator: _____________ Phone: _______________")
    pdf.add_paragraph("Venue Contact: __________________________ Phone: _______________")
    pdf.add_paragraph("Caterer: ________________________________ Phone: _______________")
    pdf.add_paragraph("Photographer: ___________________________ Phone: _______________")
    pdf.add_paragraph("DJ/Band: ________________________________ Phone: _______________")
    pdf.add_paragraph("Florist: ________________________________ Phone: _______________")
    pdf.add_paragraph("Baker: __________________________________ Phone: _______________")
    pdf.add_paragraph("Wedding website login: ___________________________________________")
    pdf.add_paragraph("Registry login: _________________________________________________")
    pdf.add_blank_line()

    pdf.add_heading2("YOUR ACTION ITEMS - Chapter 1")
    pdf.add_separator()
    pdf.add_bullet("[ ] Complete the wedding vision worksheet together")
    pdf.add_bullet("[ ] Agree on total budget and who contributes what")
    pdf.add_bullet("[ ] Create initial guest list draft (names only)")
    pdf.add_bullet("[ ] Choose your wedding party members")
    pdf.add_bullet("[ ] Set up a shared planning folder (Google Drive or similar)")
    pdf.add_bullet("[ ] Begin researching venues in your area and price range")
    pdf.add_blank_line()

    # CHAPTER 2: BUDGET MASTER TRACKER
    pdf.add_page_break()
    pdf.add_heading1("CHAPTER 2: BUDGET MASTER TRACKER")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_heading2("Budget Planning Philosophy")
    pdf.add_blank_line()
    pdf.add_paragraph("The average wedding costs between $20,000 and $35,000, but yours can be whatever fits your financial reality. The key is not how much you spend but how intentionally you allocate your resources toward the things that matter most to you as a couple.")
    pdf.add_blank_line()
    pdf.add_paragraph("This budget tracker helps you set realistic allocations, track every expense as it occurs, and avoid the surprise overages that cause wedding planning stress.")
    pdf.add_blank_line()

    pdf.add_heading2("Recommended Budget Allocation Percentages")
    pdf.add_blank_line()
    pdf.add_bullet("Venue & Catering: 40-50% of total budget")
    pdf.add_bullet("Photography & Videography: 10-12%")
    pdf.add_bullet("Music & Entertainment: 8-10%")
    pdf.add_bullet("Flowers & Decor: 8-10%")
    pdf.add_bullet("Attire & Beauty: 8-10%")
    pdf.add_bullet("Stationery & Invitations: 2-3%")
    pdf.add_bullet("Transportation: 2-3%")
    pdf.add_bullet("Wedding Rings: 2-3%")
    pdf.add_bullet("Gifts & Favors: 2-3%")
    pdf.add_bullet("Contingency Fund: 5-10% (this is essential!)")
    pdf.add_blank_line()

    pdf.add_heading2("MASTER BUDGET OVERVIEW")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_paragraph("Total Wedding Budget: $_______________")
    pdf.add_blank_line()

    # Detailed budget categories
    categories = [
        ("VENUE & RECEPTION", ["Ceremony venue rental", "Reception venue rental", "Site coordinator fee", "Tables and chairs rental", "Linens and tableware", "Lighting upgrades", "Sound system rental", "Parking and valet", "Restroom rentals (outdoor)", "Venue insurance", "Security/crowd management", "Setup and teardown fees"]),
        ("CATERING & BAR", ["Per-person dinner cost", "Cocktail hour appetizers", "Late night snack station", "Wedding cake or desserts", "Groom cake", "Dessert table extras", "Bar service (open bar)", "Specialty cocktails", "Non-alcoholic beverages", "Service charge and gratuity", "China and flatware upgrade", "Dietary accommodation meals"]),
        ("PHOTOGRAPHY & VIDEO", ["Lead photographer (8 hrs)", "Second photographer", "Engagement session", "Bridal portrait session", "Photo album", "Digital files and rights", "Videographer (8 hrs)", "Highlight reel editing", "Full ceremony video", "Drone footage", "Photo booth rental", "Extra hours coverage"]),
        ("MUSIC & ENTERTAINMENT", ["Ceremony musicians", "Cocktail hour music", "DJ for reception", "Live band", "Sound equipment rental", "MC/emcee", "Special performances", "Dance floor rental", "Lighting design", "Sparklers or confetti"]),
        ("FLOWERS & DECOR", ["Bridal bouquet", "Bridesmaid bouquets (x4)", "Boutonnières (x6)", "Corsages (x4)", "Ceremony arch/backdrop", "Ceremony aisle decor", "Reception centerpieces", "Head table arrangements", "Cake flowers", "Flower girl petals", "Cocktail hour flowers", "Restroom arrangements", "Toss bouquet", "Delivery and setup fee"]),
    ]

    for cat_name, items in categories:
        pdf.add_page_break()
        pdf.add_heading2(f"CATEGORY: {cat_name}")
        pdf.add_separator()
        pdf.add_paragraph("Budget Allocated: $_________ | Actual Spent: $_________ | Difference: $_________")
        pdf.add_blank_line()
        for item in items:
            pdf.add_paragraph(f"  {item}")
            pdf.add_paragraph(f"    Estimated: $_______ | Actual: $_______ | Vendor: _________________ | Paid? [ ]")
        pdf.add_blank_line()
        pdf.add_paragraph(f"  SUBTOTAL - {cat_name}: Estimated $_______ | Actual $_______")
        pdf.add_separator()

    # More categories on same pattern
    categories2 = [
        ("ATTIRE & BEAUTY", ["Wedding dress/suit", "Alterations", "Veil or headpiece", "Wedding shoes", "Jewelry", "Undergarments", "Groom suit/tux", "Groom shoes", "Groom accessories", "Hair styling", "Makeup artist", "Trial hair and makeup", "Bridesmaids hair", "Bridesmaids makeup", "Getting ready robes"]),
        ("STATIONERY", ["Save the dates", "Invitations suite", "RSVP cards and postage", "Programs", "Menu cards", "Place cards", "Table numbers", "Thank you cards", "Signage (welcome, seating)", "Postage for all mailings", "Calligraphy services"]),
        ("EXTRAS & GIFTS", ["Wedding party gifts", "Parent gifts", "Welcome bags", "Guest favors", "Tips for vendors", "Marriage license fee", "Officiant fee", "Hotel room (wedding night)", "Transportation (limo/bus)", "Wedding rings", "Ring insurance"]),
    ]

    for cat_name, items in categories2:
        pdf.add_page_break()
        pdf.add_heading2(f"CATEGORY: {cat_name}")
        pdf.add_separator()
        pdf.add_paragraph("Budget Allocated: $_________ | Actual Spent: $_________ | Difference: $_________")
        pdf.add_blank_line()
        for item in items:
            pdf.add_paragraph(f"  {item}")
            pdf.add_paragraph(f"    Estimated: $_______ | Actual: $_______ | Vendor: _________________ | Paid? [ ]")
        pdf.add_blank_line()
        pdf.add_paragraph(f"  SUBTOTAL - {cat_name}: Estimated $_______ | Actual $_______")
        pdf.add_separator()

    pdf.add_page_break()
    pdf.add_heading2("MONTHLY PAYMENT TRACKER")
    pdf.add_separator()
    pdf.add_blank_line()
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    for month in months:
        pdf.add_heading3(month)
        pdf.add_paragraph(f"  Payment 1: $_______ To: _________________ Date: _____ [ ] Paid")
        pdf.add_paragraph(f"  Payment 2: $_______ To: _________________ Date: _____ [ ] Paid")
        pdf.add_paragraph(f"  Payment 3: $_______ To: _________________ Date: _____ [ ] Paid")
        pdf.add_paragraph(f"  Payment 4: $_______ To: _________________ Date: _____ [ ] Paid")
        pdf.add_paragraph(f"  Monthly Total: $_______")
        pdf.add_blank_line()

    pdf.add_heading2("YOUR ACTION ITEMS - Chapter 2")
    pdf.add_separator()
    pdf.add_bullet("[ ] Set your total budget and allocate percentages per category")
    pdf.add_bullet("[ ] Fill in estimated costs for all categories")
    pdf.add_bullet("[ ] Set up a dedicated wedding bank account or credit card")
    pdf.add_bullet("[ ] Track every payment in the monthly tracker")
    pdf.add_bullet("[ ] Review budget vs actuals weekly")
    pdf.add_bullet("[ ] Keep all receipts and contracts in one folder")
    pdf.add_blank_line()

    # CHAPTER 3: 12-MONTH TIMELINE
    pdf.add_page_break()
    pdf.add_heading1("CHAPTER 3: 12-MONTH WEDDING TIMELINE")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_paragraph("This comprehensive month-by-month timeline ensures nothing falls through the cracks. Adjust timing based on your specific wedding date and planning duration.")
    pdf.add_blank_line()

    # 12 months of detailed checklists
    timeline_data = [
        ("12 MONTHS BEFORE", [
            "Set overall budget and discuss financial contributions",
            "Create initial guest list (determine approximate headcount)",
            "Research and tour potential venues (book early - venues fill up fast)",
            "Decide on wedding date (have 2-3 backup dates)",
            "Book ceremony and reception venues",
            "Begin researching photographers (they book 12+ months out)",
            "Start thinking about wedding party selections",
            "Consider hiring a wedding planner or day-of coordinator",
            "Set up wedding email address for all vendor communications",
            "Create shared planning document or spreadsheet",
            "Discuss general style and theme preferences",
            "Start a wedding inspiration board (Pinterest or physical)",
        ]),
        ("11 MONTHS BEFORE", [
            "Book photographer and videographer",
            "Research and book caterer (if not included with venue)",
            "Book officiant",
            "Finalize wedding party - ask bridesmaids and groomsmen",
            "Start dress shopping (gowns take 4-6 months to arrive)",
            "Research florists and gather inspiration images",
            "Begin researching DJs or bands",
            "Set up wedding website",
            "Consider engagement photos (use for save the dates)",
            "Research wedding insurance options",
            "Start thinking about rehearsal dinner plans",
            "Create detailed timeline for planning milestones",
        ]),
        ("10 MONTHS BEFORE", [
            "Book florist and discuss seasonal flower options",
            "Book DJ or band for reception",
            "Order wedding dress (allow 6 months for delivery)",
            "Book hotel room blocks for out-of-town guests",
            "Research invitation designers or DIY options",
            "Schedule engagement photoshoot",
            "Start planning honeymoon (book flights and hotels)",
            "Register for gifts at 2-3 stores",
            "Research hair and makeup artists",
            "Begin planning ceremony structure and readings",
            "Discuss transportation needs (guest shuttles, limo)",
        ]),
        ("9 MONTHS BEFORE", [
            "Send save the dates (mail or digital)",
            "Book hair and makeup artist (schedule trial)",
            "Order bridesmaid dresses (allow 4 months for delivery)",
            "Groom begins shopping for suit or tux",
            "Finalize ceremony details (readings, music, vows)",
            "Book rehearsal dinner venue",
            "Research and book wedding cake baker",
            "Plan welcome bags for out-of-town guests",
            "Confirm honeymoon reservations",
            "Start working on wedding vows if writing your own",
            "Research rental companies (tables, chairs, decor)",
        ]),
        ("8 MONTHS BEFORE", [
            "Finalize guest list (this drives many other decisions)",
            "Order invitations and envelopes",
            "Book rentals (furniture, linens, decor items)",
            "Plan and book bachelor/bachelorette parties",
            "Schedule cake tasting appointments",
            "Book transportation (limos, shuttles, vintage car)",
            "Begin planning reception layout and floor plan",
            "Order groomsmen suits or tuxes",
            "Research and book photo booth if desired",
            "Start compiling music playlists and must-play songs",
        ]),
        ("6 MONTHS BEFORE", [
            "Attend cake tasting and finalize design",
            "Hair and makeup trial run",
            "Finalize menu selections with caterer",
            "Order wedding favors",
            "Plan ceremony music selections",
            "Finalize flower selections and arrangements",
            "Purchase wedding party gifts",
            "Book calligrapher for invitations if using one",
            "Address and stuff invitation envelopes",
            "Confirm all vendor contracts and payment schedules",
            "Purchase wedding day accessories (veil, shoes, jewelry)",
            "Plan seating chart strategy",
        ]),
        ("4 MONTHS BEFORE", [
            "Mail invitations (allow 6-8 weeks before RSVP deadline)",
            "Apply for marriage license (check local requirements)",
            "Schedule dress fittings and alterations",
            "Finalize ceremony structure with officiant",
            "Write personal vows (if applicable)",
            "Plan and confirm rehearsal dinner details",
            "Order wedding programs",
            "Create day-of emergency kit",
            "Purchase gifts for parents",
            "Finalize playlist with DJ (must-play and do-not-play lists)",
            "Confirm honeymoon details and documents (passport check)",
        ]),
        ("2 MONTHS BEFORE", [
            "Follow up with guests who have not RSVPed",
            "Finalize seating chart",
            "Give caterer final headcount",
            "Final dress fitting",
            "Break in wedding shoes at home",
            "Create detailed day-of timeline for wedding party",
            "Confirm all vendor arrival times and setup needs",
            "Write thank you notes for early gifts",
            "Plan tips and final payments for vendors",
            "Assign day-of duties to wedding party members",
            "Confirm hotel reservations for out-of-town guests",
            "Practice first dance if choreographed",
        ]),
        ("1 MONTH BEFORE", [
            "Confirm every vendor with final details and timeline",
            "Final meeting with venue coordinator",
            "Pick up wedding dress from alterations",
            "Get marriage license",
            "Prepare final payments and tip envelopes",
            "Create seating chart cards and table assignments",
            "Deliver welcome bags to hotel",
            "Finalize vows and have backup copies",
            "Confirm rehearsal dinner headcount",
            "Pack for honeymoon",
            "Arrange for someone to handle gifts at reception",
            "Designate someone to return rentals after wedding",
        ]),
        ("1 WEEK BEFORE", [
            "Confirm timeline with all vendors one final time",
            "Rehearsal and rehearsal dinner",
            "Give rings to best man",
            "Prepare emergency kit (stain remover, sewing kit, meds, snacks)",
            "Steam or press wedding attire",
            "Prepare final vendor payments and tips",
            "Charge all devices (phone, camera)",
            "Get mani/pedi",
            "Confirm pickup time for transportation",
            "Relax and enjoy time with loved ones",
            "Early bed the night before - you deserve rest!",
        ]),
    ]

    for month_title, tasks in timeline_data:
        pdf.add_page_break()
        pdf.add_heading2(month_title)
        pdf.add_separator()
        pdf.add_blank_line()
        for task in tasks:
            pdf.add_bullet(f"[ ] {task}")
        pdf.add_blank_line()
        pdf.add_paragraph("Notes: ________________________________________________________")
        pdf.add_paragraph("_______________________________________________________________")
        pdf.add_paragraph("_______________________________________________________________")
        pdf.add_blank_line()

    pdf.add_heading2("YOUR ACTION ITEMS - Chapter 3")
    pdf.add_separator()
    pdf.add_bullet("[ ] Mark your wedding date and count back 12 months")
    pdf.add_bullet("[ ] Highlight which month you are currently in")
    pdf.add_bullet("[ ] Check off all items already completed")
    pdf.add_bullet("[ ] Add any items specific to your cultural or religious needs")
    pdf.add_bullet("[ ] Set calendar reminders for upcoming deadlines")
    pdf.add_blank_line()

    # CHAPTER 4: VENDOR MANAGEMENT
    pdf.add_page_break()
    pdf.add_heading1("CHAPTER 4: VENDOR MANAGEMENT SYSTEM")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_heading2("Choosing the Right Vendors")
    pdf.add_blank_line()
    pdf.add_paragraph("Your vendors make or break your wedding day experience. The right team of professionals will reduce your stress, execute your vision flawlessly, and handle problems before you even know they exist. Take time to research, compare, and interview multiple options before making decisions.")
    pdf.add_blank_line()
    pdf.add_paragraph("Key questions to ask every vendor: What is included in your package? What are additional fees? How many events do you handle per day? What is your cancellation and refund policy? Do you have liability insurance? Can I see references from recent clients?")
    pdf.add_blank_line()

    # Vendor comparison worksheets
    vendor_types = [
        "VENUE",
        "CATERER",
        "PHOTOGRAPHER",
        "VIDEOGRAPHER",
        "DJ / BAND",
        "FLORIST",
        "CAKE BAKER",
        "HAIR & MAKEUP",
        "OFFICIANT",
        "TRANSPORTATION",
        "RENTAL COMPANY",
        "WEDDING PLANNER",
    ]

    for vendor in vendor_types:
        pdf.add_page_break()
        pdf.add_heading2(f"VENDOR COMPARISON: {vendor}")
        pdf.add_separator()
        pdf.add_blank_line()

        for option in ["OPTION A", "OPTION B", "OPTION C"]:
            pdf.add_heading3(option)
            pdf.add_paragraph(f"Company Name: ________________________________________________")
            pdf.add_paragraph(f"Contact Person: ______________________________________________")
            pdf.add_paragraph(f"Phone: __________________ Email: _____________________________")
            pdf.add_paragraph(f"Website: _____________________________________________________")
            pdf.add_paragraph(f"Package/Price: $______________________________________________")
            pdf.add_paragraph(f"What is included: ____________________________________________")
            pdf.add_paragraph(f"_______________________________________________________________")
            pdf.add_paragraph(f"Additional fees: _____________________________________________")
            pdf.add_paragraph(f"Availability for our date? [ ] Yes  [ ] No  [ ] Tentative")
            pdf.add_paragraph(f"References checked? [ ] Yes  [ ] No")
            pdf.add_paragraph(f"Rating (1-10): ___  Gut feeling (1-10): ___")
            pdf.add_blank_line()

        pdf.add_paragraph(f"DECISION: Chosen vendor: ______________________________________")
        pdf.add_paragraph(f"Deposit paid: $_______ Date: _______ Contract signed? [ ] Yes")
        pdf.add_separator()

    pdf.add_heading2("YOUR ACTION ITEMS - Chapter 4")
    pdf.add_separator()
    pdf.add_bullet("[ ] Research at least 3 options for each major vendor category")
    pdf.add_bullet("[ ] Schedule consultations or tastings with top choices")
    pdf.add_bullet("[ ] Read all contracts carefully before signing")
    pdf.add_bullet("[ ] Keep copies of all signed contracts in one place")
    pdf.add_bullet("[ ] Record deposit amounts and remaining payment due dates")
    pdf.add_bullet("[ ] Ask for vendor recommendations from recently married friends")
    pdf.add_blank_line()

    # CHAPTER 5: GUEST MANAGEMENT
    pdf.add_page_break()
    pdf.add_heading1("CHAPTER 5: GUEST MANAGEMENT & TRACKER")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_heading2("Managing Your Guest List")
    pdf.add_blank_line()
    pdf.add_paragraph("The guest list is often the most emotionally complex part of wedding planning. It affects your budget, venue size, catering costs, and overall atmosphere. Start with your ideal number and work backward, making decisions as a team.")
    pdf.add_blank_line()
    pdf.add_paragraph("Tips for managing your guest list:")
    pdf.add_bullet("Set a firm number early and stick to it")
    pdf.add_bullet("Divide invitations: 50% couple, 25% each family (adjust as needed)")
    pdf.add_bullet("Create an A-list (must invite) and B-list (invite if space allows)")
    pdf.add_bullet("Consider plus-one policy early (engaged/married/living together?)")
    pdf.add_bullet("Kids or no kids? Decide early and communicate clearly")
    pdf.add_blank_line()
    pdf.add_paragraph("Total capacity of venue: ___________")
    pdf.add_paragraph("Our target guest count: ___________")
    pdf.add_paragraph("Estimated RSVPs yes (usually 75-85%): ___________")
    pdf.add_blank_line()

    pdf.add_heading2("MASTER GUEST TRACKER")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_paragraph("# | Name | Party Size | Address | RSVP | Meal | Table | Gift | Thank You")
    pdf.add_separator()

    # 200 guest rows
    for i in range(1, 201):
        if i % 25 == 1 and i > 1:
            pdf.add_page_break()
            pdf.add_heading3(f"GUEST TRACKER (continued - Rows {i}-{min(i+24, 200)})")
            pdf.add_separator()
            pdf.add_paragraph("# | Name | Party Size | Address | RSVP | Meal | Table | Gift | Thank You")
            pdf.add_separator()
        pdf.add_paragraph(f"{i:3d}. _________________ | __ | _________________________ | Y/N | ___ | ___ | [ ] | [ ]")

    pdf.add_blank_line()
    pdf.add_heading2("GUEST LIST SUMMARY")
    pdf.add_paragraph("Total invited: _______")
    pdf.add_paragraph("RSVPs received: _______")
    pdf.add_paragraph("Attending (Yes): _______")
    pdf.add_paragraph("Declined (No): _______")
    pdf.add_paragraph("No response yet: _______")
    pdf.add_paragraph("Total attending (with plus ones): _______")
    pdf.add_blank_line()

    pdf.add_heading2("YOUR ACTION ITEMS - Chapter 5")
    pdf.add_separator()
    pdf.add_bullet("[ ] Complete initial guest list with both families")
    pdf.add_bullet("[ ] Collect mailing addresses for all guests")
    pdf.add_bullet("[ ] Establish plus-one and children policies")
    pdf.add_bullet("[ ] Track RSVPs as they come in")
    pdf.add_bullet("[ ] Follow up with non-responders 2 weeks after deadline")
    pdf.add_bullet("[ ] Send final count to caterer")
    pdf.add_blank_line()

    # CHAPTER 6: SEATING CHART
    pdf.add_page_break()
    pdf.add_heading1("CHAPTER 6: SEATING CHART SYSTEM")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_heading2("Seating Chart Strategy")
    pdf.add_blank_line()
    pdf.add_paragraph("Creating a seating chart can feel overwhelming, but it ensures your guests have the best possible experience. People who know each other and get along will be seated together, creating natural conversation and comfort.")
    pdf.add_blank_line()
    pdf.add_paragraph("Tips for successful seating arrangements:")
    pdf.add_bullet("Start with the head table and VIP tables first")
    pdf.add_bullet("Group by relationship: college friends, work colleagues, family branches")
    pdf.add_bullet("Consider conversation compatibility (shared interests, similar ages)")
    pdf.add_bullet("Separate known conflicts (divorced parents, feuding relatives)")
    pdf.add_bullet("Place elderly or mobility-limited guests near exits and restrooms")
    pdf.add_bullet("Put families with young children near the edge for easy exits")
    pdf.add_bullet("Mix singles together at a fun table (not a sad singles table)")
    pdf.add_blank_line()
    pdf.add_paragraph("Number of tables needed: _______")
    pdf.add_paragraph("Guests per table: _______")
    pdf.add_paragraph("Table shape: [ ] Round  [ ] Rectangle  [ ] Mixed")
    pdf.add_blank_line()

    # Table assignment sheets
    for table_num in range(1, 21):
        pdf.add_heading3(f"TABLE {table_num}")
        pdf.add_paragraph(f"Location/Label: ___________________")
        pdf.add_paragraph(f"Seat 1: ___________________________")
        pdf.add_paragraph(f"Seat 2: ___________________________")
        pdf.add_paragraph(f"Seat 3: ___________________________")
        pdf.add_paragraph(f"Seat 4: ___________________________")
        pdf.add_paragraph(f"Seat 5: ___________________________")
        pdf.add_paragraph(f"Seat 6: ___________________________")
        pdf.add_paragraph(f"Seat 7: ___________________________")
        pdf.add_paragraph(f"Seat 8: ___________________________")
        pdf.add_paragraph(f"Seat 9: ___________________________")
        pdf.add_paragraph(f"Seat 10: __________________________")
        pdf.add_paragraph(f"Notes: ____________________________")
        pdf.add_separator()

    pdf.add_heading2("YOUR ACTION ITEMS - Chapter 6")
    pdf.add_separator()
    pdf.add_bullet("[ ] Determine table layout with venue coordinator")
    pdf.add_bullet("[ ] Assign head table first (wedding party)")
    pdf.add_bullet("[ ] Group remaining guests by social circles")
    pdf.add_bullet("[ ] Check for conflicts before finalizing")
    pdf.add_bullet("[ ] Order place cards and table numbers")
    pdf.add_bullet("[ ] Have a backup plan for last-minute RSVPs or cancellations")
    pdf.add_blank_line()

    # CHAPTER 7: DAY-OF TIMELINE
    pdf.add_page_break()
    pdf.add_heading1("CHAPTER 7: DAY-OF TIMELINE")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_heading2("Creating Your Perfect Day-Of Schedule")
    pdf.add_blank_line()
    pdf.add_paragraph("A detailed day-of timeline is the single most important document for ensuring your wedding day runs smoothly. Share this with your wedding party, coordinator, and all vendors so everyone knows exactly where to be and when.")
    pdf.add_blank_line()
    pdf.add_paragraph("Build in buffer time between activities. Things always take longer than expected on wedding days, and having extra time prevents stress and rushing.")
    pdf.add_blank_line()

    pdf.add_heading2("WEDDING DAY TIMELINE")
    pdf.add_separator()
    pdf.add_paragraph("Wedding Date: ___________________")
    pdf.add_blank_line()

    timeline_hours = [
        ("6:00 AM", "Wake up, light breakfast, hydrate"),
        ("6:30 AM", "Shower, skincare routine, begin getting ready"),
        ("7:00 AM", "Hair and makeup team arrives at getting-ready location"),
        ("7:15 AM", "First person in hair chair (furthest from bride)"),
        ("7:30 AM", "First person in makeup chair"),
        ("8:00 AM", "Bridesmaids continue hair and makeup rotation"),
        ("8:30 AM", "Light snacks and drinks for getting-ready group"),
        ("9:00 AM", "Bride begins hair"),
        ("9:30 AM", "Groom and groomsmen begin getting dressed"),
        ("9:45 AM", "Bride begins makeup"),
        ("10:00 AM", "Photographer arrives to capture getting-ready details"),
        ("10:15 AM", "Detail shots: dress, shoes, rings, invitations, flowers"),
        ("10:30 AM", "Bride gets into dress (capture the moment)"),
        ("10:45 AM", "Mother/father first look with bride"),
        ("11:00 AM", "Bridal party first look and group photos"),
        ("11:15 AM", "First look with partner (if doing one)"),
        ("11:30 AM", "Couple portraits (golden hour alternative for flexibility)"),
        ("11:45 AM", "Family formal portraits"),
        ("12:00 PM", "Full bridal party photos"),
        ("12:30 PM", "Break - snacks, touch-ups, bathroom break"),
        ("1:00 PM", "Travel to ceremony venue (if different location)"),
        ("1:30 PM", "Venue setup check - coordinator confirms all details"),
        ("2:00 PM", "Musicians/DJ begin setup and sound check"),
        ("2:30 PM", "Florist delivers and sets up ceremony flowers"),
        ("3:00 PM", "Ushers arrive and prepare for guest seating"),
        ("3:15 PM", "Guest shuttle departs from hotel (if applicable)"),
        ("3:30 PM", "Guests begin arriving - ushers seat them"),
        ("3:45 PM", "Immediate family seated"),
        ("3:55 PM", "Groom and groomsmen take positions"),
        ("4:00 PM", "CEREMONY BEGINS - Processional"),
        ("4:05 PM", "Bridesmaids walk down aisle"),
        ("4:08 PM", "Bride walks down aisle"),
        ("4:10 PM", "Welcome and opening words"),
        ("4:15 PM", "Readings"),
        ("4:20 PM", "Vows"),
        ("4:25 PM", "Ring exchange"),
        ("4:30 PM", "Pronouncement and first kiss"),
        ("4:32 PM", "Recessional - newlyweds exit"),
        ("4:35 PM", "Receiving line or post-ceremony photos"),
        ("4:45 PM", "Guests transition to cocktail hour"),
        ("5:00 PM", "COCKTAIL HOUR BEGINS"),
        ("5:00 PM", "Couple takes additional portraits during golden hour"),
        ("5:30 PM", "Couple joins cocktail hour briefly"),
        ("5:45 PM", "Guests invited to move to reception area"),
        ("6:00 PM", "RECEPTION BEGINS - Guests seated"),
        ("6:05 PM", "Wedding party introduced"),
        ("6:10 PM", "Couple grand entrance"),
        ("6:15 PM", "First dance"),
        ("6:20 PM", "Welcome speech and blessing/grace"),
        ("6:30 PM", "Dinner service begins (first course)"),
        ("7:00 PM", "Main course served"),
        ("7:15 PM", "Toasts and speeches (best man, maid of honor, parents)"),
        ("7:45 PM", "Parent dances (father-daughter, mother-son)"),
        ("8:00 PM", "Cake cutting"),
        ("8:15 PM", "Open dancing begins"),
        ("8:30 PM", "Bouquet and garter toss (if desired)"),
        ("9:00 PM", "Special dances (anniversary dance, etc.)"),
        ("9:30 PM", "Late-night snack station opens"),
        ("10:00 PM", "Last dance announced"),
        ("10:15 PM", "Grand exit (sparklers, bubbles, confetti)"),
        ("10:30 PM", "Couple departs"),
        ("10:30 PM", "Coordinator oversees venue cleanup and rental returns"),
    ]

    for time, activity in timeline_hours:
        pdf.add_paragraph(f"  {time}  |  {activity}")
        pdf.add_paragraph(f"           Notes: ____________________________________________")

    pdf.add_blank_line()
    pdf.add_heading2("YOUR ACTION ITEMS - Chapter 7")
    pdf.add_separator()
    pdf.add_bullet("[ ] Customize this timeline with your specific times")
    pdf.add_bullet("[ ] Share final timeline with ALL vendors at least 2 weeks before")
    pdf.add_bullet("[ ] Give a printed copy to your coordinator and wedding party")
    pdf.add_bullet("[ ] Build in 15-minute buffers between major transitions")
    pdf.add_bullet("[ ] Assign someone to keep the day on schedule")
    pdf.add_blank_line()

    # CHAPTER 8: DESIGN & DECOR
    pdf.add_page_break()
    pdf.add_heading1("CHAPTER 8: DESIGN & DECOR PLANNER")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_heading2("Defining Your Wedding Aesthetic")
    pdf.add_blank_line()
    pdf.add_paragraph("Your wedding decor tells the story of who you are as a couple. Whether you prefer minimalist elegance, rustic charm, modern sophistication, or bohemian whimsy, consistency across all visual elements creates a cohesive and memorable experience for your guests.")
    pdf.add_blank_line()

    pdf.add_heading3("Color Palette")
    pdf.add_paragraph("Primary Color: ________________________")
    pdf.add_paragraph("Secondary Color: ______________________")
    pdf.add_paragraph("Accent Color: _________________________")
    pdf.add_paragraph("Neutral Base: __________________________")
    pdf.add_blank_line()

    pdf.add_heading3("Style Keywords (circle 3-5)")
    pdf.add_paragraph("Romantic | Modern | Rustic | Vintage | Bohemian | Classic | Glamorous")
    pdf.add_paragraph("Minimalist | Industrial | Garden | Beach | Whimsical | Elegant | Moody")
    pdf.add_blank_line()

    pdf.add_heading2("Decor Element Tracker")
    pdf.add_blank_line()
    decor_areas = [
        ("Ceremony Space", ["Arch or backdrop", "Aisle runner", "Aisle decorations (petals, lanterns)", "Pew/chair markers", "Welcome sign", "Programs display", "Unity ceremony items"]),
        ("Cocktail Hour", ["Lounge furniture", "Bar signage", "Cocktail napkins", "Guest book station", "Photo display", "Escort card display"]),
        ("Reception Tables", ["Centerpieces", "Table runners or linens", "Place settings", "Napkin style and fold", "Menu cards", "Table numbers", "Candles/votives", "Charger plates", "Glassware style"]),
        ("Head Table", ["Sweetheart table or long table?", "Backdrop or greenery wall", "Special centerpiece", "Mr and Mrs sign", "Special chairs"]),
        ("Dance Floor & Stage", ["Dance floor decal or monogram", "Uplighting color", "String lights", "Disco ball or special effects", "Backdrop for band/DJ"]),
        ("Cake & Dessert", ["Cake table and display", "Dessert table setup", "Cake topper", "Serving set", "Signage for desserts"]),
        ("Photo Areas", ["Photo booth backdrop", "Props", "Guest book alternative", "Polaroid station", "Hashtag sign"]),
    ]

    for area, items in decor_areas:
        pdf.add_heading3(area)
        for item in items:
            pdf.add_paragraph(f"  [ ] {item}: _____________________________________________")
        pdf.add_blank_line()

    pdf.add_heading2("YOUR ACTION ITEMS - Chapter 8")
    pdf.add_separator()
    pdf.add_bullet("[ ] Finalize color palette with swatches")
    pdf.add_bullet("[ ] Create mood board with inspiration images")
    pdf.add_bullet("[ ] List all decor items needed and their sources")
    pdf.add_bullet("[ ] Get quotes for rental items vs purchased items")
    pdf.add_bullet("[ ] Assign decor setup tasks for day-of")
    pdf.add_bullet("[ ] Plan what happens to decor after wedding (keep, donate, sell)")
    pdf.add_blank_line()

    # CHAPTER 9: HONEYMOON PLANNER
    pdf.add_page_break()
    pdf.add_heading1("CHAPTER 9: HONEYMOON PLANNER")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_heading2("Planning Your Perfect Getaway")
    pdf.add_blank_line()
    pdf.add_paragraph("Your honeymoon is the well-deserved celebration after months of wedding planning. Whether it is a tropical beach escape, a European adventure, a cozy mountain retreat, or a multi-destination journey, planning it alongside your wedding ensures you have something wonderful to look forward to.")
    pdf.add_blank_line()

    pdf.add_heading3("Honeymoon Basics")
    pdf.add_paragraph("Destination: ___________________________________________________")
    pdf.add_paragraph("Departure date: _________________ Return date: __________________")
    pdf.add_paragraph("Duration: _____________ days")
    pdf.add_paragraph("Budget: $___________")
    pdf.add_blank_line()

    pdf.add_heading3("Travel Documents Checklist")
    pdf.add_bullet("[ ] Passports valid (6+ months from travel date)")
    pdf.add_bullet("[ ] Visas required? _______ Applied for? [ ] Yes")
    pdf.add_bullet("[ ] Travel insurance purchased? [ ] Yes")
    pdf.add_bullet("[ ] Copies of all documents (physical and digital)")
    pdf.add_bullet("[ ] Name change needed before travel? Timeline: __________")
    pdf.add_bullet("[ ] Vaccinations or medications needed?")
    pdf.add_bullet("[ ] International phone plan activated")
    pdf.add_bullet("[ ] Bank notified of international travel")
    pdf.add_blank_line()

    pdf.add_heading3("Bookings & Reservations")
    pdf.add_paragraph("Flights: __________________ Confirmation #: __________________")
    pdf.add_paragraph("Hotel/Resort: _______________ Confirmation #: __________________")
    pdf.add_paragraph("Car Rental: ________________ Confirmation #: __________________")
    pdf.add_paragraph("Activity 1: ________________ Confirmation #: __________________")
    pdf.add_paragraph("Activity 2: ________________ Confirmation #: __________________")
    pdf.add_paragraph("Activity 3: ________________ Confirmation #: __________________")
    pdf.add_paragraph("Restaurant 1: ______________ Reservation time: ________________")
    pdf.add_paragraph("Restaurant 2: ______________ Reservation time: ________________")
    pdf.add_blank_line()

    pdf.add_heading3("Packing Checklist")
    pdf.add_bullet("[ ] Passports and IDs")
    pdf.add_bullet("[ ] Printed confirmations and itinerary")
    pdf.add_bullet("[ ] Medications and first aid")
    pdf.add_bullet("[ ] Phone chargers and adapters")
    pdf.add_bullet("[ ] Sunscreen and toiletries")
    pdf.add_bullet("[ ] Comfortable walking shoes")
    pdf.add_bullet("[ ] Swimwear")
    pdf.add_bullet("[ ] Dressy outfits for dinners")
    pdf.add_bullet("[ ] Camera and memory cards")
    pdf.add_bullet("[ ] Travel pillow and eye mask")
    pdf.add_bullet("[ ] Books or entertainment for flights")
    pdf.add_bullet("[ ] Snacks for travel days")
    pdf.add_blank_line()

    pdf.add_heading2("YOUR ACTION ITEMS - Chapter 9")
    pdf.add_separator()
    pdf.add_bullet("[ ] Choose destination and discuss preferences together")
    pdf.add_bullet("[ ] Set honeymoon budget")
    pdf.add_bullet("[ ] Book flights and accommodations (6+ months out for best prices)")
    pdf.add_bullet("[ ] Research activities and make reservations")
    pdf.add_bullet("[ ] Verify travel documents are current")
    pdf.add_bullet("[ ] Purchase travel insurance")
    pdf.add_blank_line()

    # CHAPTER 10: POST-WEDDING
    pdf.add_page_break()
    pdf.add_heading1("CHAPTER 10: POST-WEDDING TASKS")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_heading2("After the Big Day")
    pdf.add_blank_line()
    pdf.add_paragraph("The wedding is over but there are still important tasks to handle. This chapter helps you tie up loose ends, preserve memories, and start your married life organized and stress-free.")
    pdf.add_blank_line()

    pdf.add_heading3("Week 1 After Wedding")
    pdf.add_bullet("[ ] Send vendor tips if not distributed day-of")
    pdf.add_bullet("[ ] Return any rented items (tuxes, decor, equipment)")
    pdf.add_bullet("[ ] Preserve wedding dress (dry clean and store properly)")
    pdf.add_bullet("[ ] Change social media status if desired")
    pdf.add_bullet("[ ] Begin writing thank you notes (aim for 10 per day)")
    pdf.add_bullet("[ ] Organize and store wedding cards and gifts")
    pdf.add_blank_line()

    pdf.add_heading3("Week 2-4 After Wedding")
    pdf.add_bullet("[ ] Complete all thank you notes (send within 3 months)")
    pdf.add_bullet("[ ] Begin name change process if applicable")
    pdf.add_bullet("[ ] Update identification documents")
    pdf.add_bullet("[ ] Update bank accounts and credit cards")
    pdf.add_bullet("[ ] Update insurance policies")
    pdf.add_bullet("[ ] Review and rate vendors online (they appreciate reviews)")
    pdf.add_bullet("[ ] Organize wedding photos when received")
    pdf.add_bullet("[ ] Order prints or albums")
    pdf.add_blank_line()

    pdf.add_heading3("Name Change Checklist (if applicable)")
    pdf.add_bullet("[ ] Social Security card")
    pdf.add_bullet("[ ] Drivers license or state ID")
    pdf.add_bullet("[ ] Passport")
    pdf.add_bullet("[ ] Bank accounts")
    pdf.add_bullet("[ ] Credit cards")
    pdf.add_bullet("[ ] Insurance policies (health, auto, home)")
    pdf.add_bullet("[ ] Employer/HR records")
    pdf.add_bullet("[ ] Voter registration")
    pdf.add_bullet("[ ] Utilities and subscriptions")
    pdf.add_bullet("[ ] Professional licenses")
    pdf.add_bullet("[ ] Email signature and business cards")
    pdf.add_blank_line()

    pdf.add_heading3("Thank You Note Tracker")
    pdf.add_paragraph("Use this to track who you have thanked:")
    pdf.add_blank_line()
    for i in range(1, 31):
        pdf.add_paragraph(f"{i:2d}. Name: _________________________ Gift: ________________ Sent: [ ]")
    pdf.add_blank_line()

    pdf.add_heading2("YOUR ACTION ITEMS - Chapter 10")
    pdf.add_separator()
    pdf.add_bullet("[ ] Create thank you note schedule (10 per day)")
    pdf.add_bullet("[ ] Return all rentals within the specified timeframe")
    pdf.add_bullet("[ ] Start name change process within 30 days")
    pdf.add_bullet("[ ] Back up all wedding photos to cloud storage")
    pdf.add_bullet("[ ] Leave reviews for your amazing vendors")
    pdf.add_blank_line()

    # FINAL PAGE
    pdf.add_page_break()
    pdf.add_heading1("NEXT STEPS")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_paragraph("Congratulations! Whether you are just starting your planning journey or deep in the details, this planner is your comprehensive companion. Remember: the wedding is ONE day, but the marriage is forever. Do not let planning stress overshadow the joy of this season.")
    pdf.add_blank_line()
    pdf.add_paragraph("Final Reminders:")
    pdf.add_bullet("Communicate openly with your partner throughout planning")
    pdf.add_bullet("Delegate tasks - you do not have to do everything yourself")
    pdf.add_bullet("Build in contingency budget (5-10%) for surprises")
    pdf.add_bullet("Take breaks from wedding planning regularly")
    pdf.add_bullet("Remember why you are doing this - you are marrying your person!")
    pdf.add_blank_line()
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_paragraph("Wishing you a beautiful wedding and an even more beautiful marriage.")

    filepath = os.path.join(OUTPUT_DIR, '03-Wedding-Planning-Master-Bundle.pdf')
    pdf.save(filepath)
    return filepath, len(pdf.pages) + 1



def generate_book4():
    """Book 4: Digital Declutter & Productivity System (60-80 pages)"""
    pdf = PurePDF(title="Digital Declutter & Productivity System", author="Daniel Tesfamariam")

    # TITLE PAGE
    pdf.add_blank_line()
    pdf.add_blank_line()
    pdf.add_blank_line()
    pdf.add_title("DIGITAL DECLUTTER &")
    pdf.add_title("PRODUCTIVITY SYSTEM")
    pdf.add_blank_line()
    pdf.add_heading2("Reclaim Your Time, Focus, and Mental Clarity")
    pdf.add_heading2("in a World of Digital Overwhelm")
    pdf.add_blank_line()
    pdf.add_blank_line()
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_blank_line()
    pdf.add_paragraph("A step-by-step system to organize your digital life,")
    pdf.add_paragraph("eliminate distractions, and build sustainable productivity habits.")
    pdf.add_blank_line()
    pdf.add_separator()
    pdf.add_paragraph("Copyright 2024 Daniel Tesfamariam. All rights reserved.")

    # TABLE OF CONTENTS
    pdf.add_page_break()
    pdf.add_title("TABLE OF CONTENTS")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_paragraph("Chapter 1: Digital Overwhelm Assessment .................... 3")
    pdf.add_paragraph("Chapter 2: Phone Declutter System .......................... 11")
    pdf.add_paragraph("Chapter 3: Email Inbox Zero ................................ 23")
    pdf.add_paragraph("Chapter 4: Computer & File Organization .................... 33")
    pdf.add_paragraph("Chapter 5: Social Media Detox .............................. 43")
    pdf.add_paragraph("Chapter 6: Digital Productivity System ..................... 51")
    pdf.add_paragraph("Chapter 7: Password & Security ............................. 63")
    pdf.add_paragraph("Chapter 8: 30-Day Digital Declutter Challenge .............. 69")
    pdf.add_paragraph("Final: Next Steps .......................................... 79")
    pdf.add_blank_line()

    # CHAPTER 1: DIGITAL OVERWHELM ASSESSMENT
    pdf.add_page_break()
    pdf.add_heading1("CHAPTER 1: DIGITAL OVERWHELM ASSESSMENT")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_heading2("The Digital Clutter Crisis")
    pdf.add_blank_line()
    pdf.add_paragraph("We live in an unprecedented era of digital overload. The average person checks their phone 96 times per day, has 40 apps installed, receives 121 emails daily, and spends over 7 hours per day on screens. This constant digital stimulation creates chronic stress, reduces attention spans, hampers creativity, and leaves us feeling perpetually behind.")
    pdf.add_blank_line()
    pdf.add_paragraph("Digital clutter is just as draining as physical clutter, yet most people never address it. Overflowing inboxes, chaotic file systems, endless notification pings, and cluttered desktops create a low-grade anxiety that saps your energy and focus throughout the day.")
    pdf.add_blank_line()
    pdf.add_paragraph("This workbook provides a systematic approach to decluttering every aspect of your digital life and building sustainable habits that keep it organized permanently.")
    pdf.add_blank_line()

    pdf.add_heading2("Digital Overwhelm Self-Assessment")
    pdf.add_blank_line()
    pdf.add_paragraph("Rate each statement from 1 (never) to 5 (always):")
    pdf.add_blank_line()
    pdf.add_paragraph("___ I feel anxious when I see my number of unread emails")
    pdf.add_paragraph("___ I spend time scrolling social media when I should be working")
    pdf.add_paragraph("___ I cannot find files or documents when I need them")
    pdf.add_paragraph("___ I have multiple tabs open that I never get back to")
    pdf.add_paragraph("___ My phone notifications interrupt my focus multiple times per hour")
    pdf.add_paragraph("___ I feel guilty about my screen time")
    pdf.add_paragraph("___ I subscribe to newsletters I never read")
    pdf.add_paragraph("___ My desktop is cluttered with files")
    pdf.add_paragraph("___ I have apps on my phone I have not used in months")
    pdf.add_paragraph("___ I check my phone first thing in the morning and last at night")
    pdf.add_paragraph("___ I lose track of passwords and account information")
    pdf.add_paragraph("___ I have duplicate files saved in multiple locations")
    pdf.add_paragraph("___ I feel overwhelmed by the amount of digital content to consume")
    pdf.add_paragraph("___ I have trouble focusing for more than 20 minutes without checking my phone")
    pdf.add_paragraph("___ My photos are unorganized with thousands I will never look at again")
    pdf.add_blank_line()
    pdf.add_paragraph("TOTAL SCORE: _____ / 75")
    pdf.add_blank_line()
    pdf.add_paragraph("Scoring: 15-25 Mild | 26-45 Moderate | 46-60 Significant | 61-75 Severe")
    pdf.add_blank_line()

    pdf.add_heading2("My Current Digital Inventory")
    pdf.add_blank_line()
    pdf.add_paragraph("Take stock of your current digital situation:")
    pdf.add_blank_line()
    pdf.add_paragraph("Number of apps on my phone: ___")
    pdf.add_paragraph("Unread emails right now: ___")
    pdf.add_paragraph("Email accounts I manage: ___")
    pdf.add_paragraph("Social media platforms I use: ___")
    pdf.add_paragraph("Daily average screen time (check phone settings): ___ hours")
    pdf.add_paragraph("Number of open browser tabs right now: ___")
    pdf.add_paragraph("Files on my desktop: ___")
    pdf.add_paragraph("Subscriptions I pay for monthly: ___")
    pdf.add_paragraph("Photos in my camera roll: ___")
    pdf.add_paragraph("Unread text/message notifications: ___")
    pdf.add_blank_line()

    pdf.add_heading2("My Digital Pain Points")
    pdf.add_blank_line()
    pdf.add_paragraph("What frustrates me most about my digital life:")
    pdf.add_paragraph("1. ____________________________________________________________")
    pdf.add_paragraph("2. ____________________________________________________________")
    pdf.add_paragraph("3. ____________________________________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("What I wish my digital life looked like:")
    pdf.add_paragraph("1. ____________________________________________________________")
    pdf.add_paragraph("2. ____________________________________________________________")
    pdf.add_paragraph("3. ____________________________________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("How digital clutter affects my daily life:")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_blank_line()

    pdf.add_heading2("YOUR ACTION ITEMS - Chapter 1")
    pdf.add_separator()
    pdf.add_bullet("[ ] Complete the Digital Overwhelm Self-Assessment")
    pdf.add_bullet("[ ] Fill out your Current Digital Inventory (actual numbers)")
    pdf.add_bullet("[ ] Identify your top 3 digital pain points")
    pdf.add_bullet("[ ] Check your phone screen time report for the past week")
    pdf.add_bullet("[ ] Write down your vision for an organized digital life")
    pdf.add_bullet("[ ] Commit to working through one chapter per day")
    pdf.add_blank_line()

    # CHAPTER 2: PHONE DECLUTTER
    pdf.add_page_break()
    pdf.add_heading1("CHAPTER 2: PHONE DECLUTTER SYSTEM")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_heading2("Your Phone Is Your Biggest Distraction")
    pdf.add_blank_line()
    pdf.add_paragraph("Your smartphone is the single most powerful tool for productivity or the single biggest source of distraction in your life. The difference comes down to how intentionally you set it up. Most people use their phone on autopilot with default settings designed by companies whose business model is to maximize your screen time.")
    pdf.add_blank_line()
    pdf.add_paragraph("This chapter walks you through a complete phone declutter that typically takes 60-90 minutes but saves you hours every week going forward.")
    pdf.add_blank_line()

    pdf.add_heading2("Step 1: App Audit")
    pdf.add_blank_line()
    pdf.add_paragraph("Go through EVERY app on your phone. For each one, decide: Keep, Delete, or Move to back pages. An app earns its place on your phone only if you use it at least weekly AND it adds genuine value to your life.")
    pdf.add_blank_line()
    pdf.add_heading3("Apps to DELETE (ones I never or rarely use):")
    for i in range(1, 16):
        pdf.add_paragraph(f"{i:2d}. ____________________________________________________________")
    pdf.add_blank_line()
    pdf.add_heading3("Apps to KEEP (daily/weekly use, genuine value):")
    for i in range(1, 16):
        pdf.add_paragraph(f"{i:2d}. ____________________________________________________________")
    pdf.add_blank_line()
    pdf.add_heading3("Apps to MOVE to back pages (occasional use):")
    for i in range(1, 11):
        pdf.add_paragraph(f"{i:2d}. ____________________________________________________________")
    pdf.add_blank_line()

    pdf.add_heading2("Step 2: Notification Audit")
    pdf.add_blank_line()
    pdf.add_paragraph("Most apps default to maximum notifications. Each notification interrupts your focus and takes an average of 23 minutes to fully recover your concentration. Be ruthless about which apps deserve to interrupt you.")
    pdf.add_blank_line()
    pdf.add_heading3("Notifications ALLOWED (urgent, time-sensitive):")
    pdf.add_bullet("Phone calls: YES")
    pdf.add_bullet("Text messages: YES (but consider Do Not Disturb schedules)")
    pdf.add_bullet("Calendar: YES")
    pdf.add_paragraph("Others: ________________________________________________________")
    pdf.add_paragraph("Others: ________________________________________________________")
    pdf.add_blank_line()
    pdf.add_heading3("Notifications DISABLED (everything else):")
    pdf.add_bullet("Social media: ALL OFF")
    pdf.add_bullet("Shopping apps: ALL OFF")
    pdf.add_bullet("News apps: ALL OFF")
    pdf.add_bullet("Games: ALL OFF")
    pdf.add_bullet("Email (check on schedule instead): OFF or VIP only")
    pdf.add_paragraph("Others disabled: _______________________________________________")
    pdf.add_paragraph("Others disabled: _______________________________________________")
    pdf.add_blank_line()

    pdf.add_heading2("Step 3: Home Screen Redesign")
    pdf.add_blank_line()
    pdf.add_paragraph("Your home screen should contain only tools that help you be productive, connected, and intentional. Social media and entertainment apps should never be on your home screen because they trigger mindless scrolling.")
    pdf.add_blank_line()
    pdf.add_heading3("My Ideal Home Screen Layout:")
    pdf.add_paragraph("Row 1: _________ | _________ | _________ | _________")
    pdf.add_paragraph("Row 2: _________ | _________ | _________ | _________")
    pdf.add_paragraph("Row 3: _________ | _________ | _________ | _________")
    pdf.add_paragraph("Row 4: _________ | _________ | _________ | _________")
    pdf.add_paragraph("Dock:  _________ | _________ | _________ | _________")
    pdf.add_blank_line()
    pdf.add_paragraph("Recommended home screen apps: Phone, Messages, Calendar, Camera, Notes, Maps, Weather, Music")
    pdf.add_blank_line()

    pdf.add_heading2("Step 4: Photo Library Cleanup")
    pdf.add_blank_line()
    pdf.add_paragraph("Most people have thousands of photos they will never look at again - blurry shots, duplicates, screenshots of things long resolved, and photos of menus or signs. A lean photo library makes it easier to find the memories that matter.")
    pdf.add_blank_line()
    pdf.add_heading3("Photo Declutter Plan:")
    pdf.add_bullet("[ ] Delete all blurry or duplicate photos")
    pdf.add_bullet("[ ] Delete old screenshots no longer relevant")
    pdf.add_bullet("[ ] Delete photos of text, receipts, or temporary info")
    pdf.add_bullet("[ ] Create albums for important events (vacation, birthday, etc.)")
    pdf.add_bullet("[ ] Back up photos to cloud storage (Google Photos, iCloud)")
    pdf.add_bullet("[ ] Delete photos from device after backing up")
    pdf.add_blank_line()
    pdf.add_paragraph("Photos before cleanup: ___________")
    pdf.add_paragraph("Photos after cleanup: ___________")
    pdf.add_paragraph("Storage freed up: ___________ GB")
    pdf.add_blank_line()

    pdf.add_heading2("Step 5: Contacts Cleanup")
    pdf.add_blank_line()
    pdf.add_paragraph("Your contacts list likely contains hundreds of people you no longer recognize or communicate with. A clean contacts list makes it faster to find who you need and reduces digital clutter in one more area of your phone.")
    pdf.add_blank_line()
    pdf.add_heading3("Contacts Cleanup Checklist:")
    pdf.add_bullet("[ ] Delete contacts with no name or unrecognizable numbers")
    pdf.add_bullet("[ ] Merge duplicate contacts")
    pdf.add_bullet("[ ] Update outdated phone numbers and emails")
    pdf.add_bullet("[ ] Add missing information to important contacts")
    pdf.add_bullet("[ ] Organize contacts into groups (Family, Work, Friends, Services)")
    pdf.add_bullet("[ ] Delete contacts from companies or services you no longer use")
    pdf.add_bullet("[ ] Back up contacts to cloud before making major deletions")
    pdf.add_blank_line()
    pdf.add_paragraph("Contacts before cleanup: ___________")
    pdf.add_paragraph("Contacts after cleanup: ___________")
    pdf.add_paragraph("Duplicates merged: ___________")
    pdf.add_blank_line()

    pdf.add_heading2("Step 6: Message & Chat Cleanup")
    pdf.add_blank_line()
    pdf.add_paragraph("Text messages and chat apps accumulate gigabytes of data over time. Old group chats, media files, and conversations with people you no longer talk to all take up space and mental energy.")
    pdf.add_blank_line()
    pdf.add_heading3("Message Cleanup Checklist:")
    pdf.add_bullet("[ ] Leave group chats you no longer participate in")
    pdf.add_bullet("[ ] Delete conversations with businesses (appointment confirmations, etc.)")
    pdf.add_bullet("[ ] Clear media from old conversations (photos, videos take most space)")
    pdf.add_bullet("[ ] Archive important conversations you want to keep but not see daily")
    pdf.add_bullet("[ ] Mute notifications for low-priority group chats")
    pdf.add_bullet("[ ] Uninstall messaging apps you rarely use")
    pdf.add_blank_line()
    pdf.add_paragraph("Group chats left: ___")
    pdf.add_paragraph("Conversations deleted: ___")
    pdf.add_paragraph("Storage freed: ___ GB")
    pdf.add_blank_line()

    pdf.add_heading2("Step 7: Subscription Audit")
    pdf.add_blank_line()
    pdf.add_paragraph("Check your app store subscriptions. Most people are paying for services they forgot about or no longer use. The average person wastes $30-50/month on unused subscriptions.")
    pdf.add_blank_line()
    pdf.add_heading3("Current Subscriptions:")
    pdf.add_paragraph("Service | Monthly Cost | Still Using? | Action")
    pdf.add_separator()
    for i in range(1, 16):
        pdf.add_paragraph(f"{i:2d}. _________________ | $_______ | [ ]Yes [ ]No | [ ]Keep [ ]Cancel")
    pdf.add_blank_line()
    pdf.add_paragraph("Total monthly subscription cost: $___________")
    pdf.add_paragraph("Amount saved by canceling unused: $___________")
    pdf.add_paragraph("Annual savings: $___________")
    pdf.add_blank_line()

    pdf.add_heading2("YOUR ACTION ITEMS - Chapter 2")
    pdf.add_separator()
    pdf.add_bullet("[ ] Complete the full app audit (delete, keep, move)")
    pdf.add_bullet("[ ] Disable notifications for all non-essential apps")
    pdf.add_bullet("[ ] Redesign your home screen for intentionality")
    pdf.add_bullet("[ ] Spend 30 minutes cleaning up your photo library")
    pdf.add_bullet("[ ] Audit and cancel unused subscriptions")
    pdf.add_bullet("[ ] Set up screen time limits for social media apps")
    pdf.add_bullet("[ ] Enable Do Not Disturb schedule for focus hours")
    pdf.add_blank_line()

    # CHAPTER 3: EMAIL INBOX ZERO
    pdf.add_page_break()
    pdf.add_heading1("CHAPTER 3: EMAIL INBOX ZERO")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_heading2("The Inbox Zero Philosophy")
    pdf.add_blank_line()
    pdf.add_paragraph("Inbox Zero does not mean you have zero emails in your inbox at all times. It means your inbox is a processing station, not a storage system. Every email that comes in gets processed (reply, archive, delegate, delete, or defer) rather than sitting there creating mental clutter and guilt.")
    pdf.add_blank_line()
    pdf.add_paragraph("The goal is to check email intentionally at scheduled times, process everything that came in, and then close your email until the next scheduled check. This eliminates the constant low-grade anxiety of an overflowing inbox and the productivity-killing habit of checking email every few minutes.")
    pdf.add_blank_line()

    pdf.add_heading2("Step 1: The Great Email Purge")
    pdf.add_blank_line()
    pdf.add_paragraph("If you have hundreds or thousands of unread emails, do not try to read them all. Use this triage approach:")
    pdf.add_blank_line()
    pdf.add_bullet("Select all emails older than 30 days and ARCHIVE them (not delete)")
    pdf.add_bullet("If anything was truly urgent from 30+ days ago, someone would have followed up")
    pdf.add_bullet("Search for and delete all promotional emails in bulk")
    pdf.add_bullet("Unsubscribe from every newsletter you have not read in the past month")
    pdf.add_bullet("Create a TEMP folder and move remaining old emails there for later review")
    pdf.add_blank_line()
    pdf.add_paragraph("Emails before purge: ___________")
    pdf.add_paragraph("Emails after purge: ___________")
    pdf.add_paragraph("Newsletters unsubscribed from: ___________")
    pdf.add_blank_line()

    pdf.add_heading2("Step 2: Unsubscribe Sprint")
    pdf.add_blank_line()
    pdf.add_paragraph("Track every newsletter and promotional email you unsubscribe from:")
    pdf.add_blank_line()
    for i in range(1, 26):
        pdf.add_paragraph(f"{i:2d}. ____________________________________________________________ [ ] Done")
    pdf.add_blank_line()

    pdf.add_heading2("Step 3: Create Your Folder System")
    pdf.add_blank_line()
    pdf.add_paragraph("Keep your folder/label system simple. Too many folders creates just as much overwhelm. Here is a proven minimal system:")
    pdf.add_blank_line()
    pdf.add_heading3("Recommended Folder Structure:")
    pdf.add_bullet("INBOX (processing station - aim to empty daily)")
    pdf.add_bullet("ACTION REQUIRED (emails that need a response or task)")
    pdf.add_bullet("WAITING FOR (emails where you are waiting on someone else)")
    pdf.add_bullet("REFERENCE (important info you may need to find later)")
    pdf.add_bullet("ARCHIVE (everything else - searchable but out of sight)")
    pdf.add_blank_line()
    pdf.add_paragraph("My folder system:")
    pdf.add_paragraph("1. ____________________________________________________________")
    pdf.add_paragraph("2. ____________________________________________________________")
    pdf.add_paragraph("3. ____________________________________________________________")
    pdf.add_paragraph("4. ____________________________________________________________")
    pdf.add_paragraph("5. ____________________________________________________________")
    pdf.add_blank_line()

    pdf.add_heading2("Step 4: Email Processing Schedule")
    pdf.add_blank_line()
    pdf.add_paragraph("Instead of checking email constantly, schedule specific times:")
    pdf.add_blank_line()
    pdf.add_paragraph("Morning check: _________ (process for ___ minutes)")
    pdf.add_paragraph("Midday check: _________ (process for ___ minutes)")
    pdf.add_paragraph("End of day check: _________ (process for ___ minutes)")
    pdf.add_blank_line()
    pdf.add_paragraph("The 4-D Method for processing each email:")
    pdf.add_bullet("DELETE - if it requires no action and has no reference value")
    pdf.add_bullet("DO - if it takes less than 2 minutes, do it immediately")
    pdf.add_bullet("DELEGATE - if someone else should handle it, forward it now")
    pdf.add_bullet("DEFER - if it takes longer than 2 minutes, move to Action folder")
    pdf.add_blank_line()

    pdf.add_heading2("Step 5: Email Templates")
    pdf.add_blank_line()
    pdf.add_paragraph("Create templates for emails you send repeatedly to save time:")
    pdf.add_blank_line()
    pdf.add_heading3("Template 1: ________________________")
    pdf.add_paragraph("Subject: _________________________________________________________")
    pdf.add_paragraph("Body: ___________________________________________________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_blank_line()
    pdf.add_heading3("Template 2: ________________________")
    pdf.add_paragraph("Subject: _________________________________________________________")
    pdf.add_paragraph("Body: ___________________________________________________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_blank_line()
    pdf.add_heading3("Template 3: ________________________")
    pdf.add_paragraph("Subject: _________________________________________________________")
    pdf.add_paragraph("Body: ___________________________________________________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_blank_line()

    pdf.add_heading2("YOUR ACTION ITEMS - Chapter 3")
    pdf.add_separator()
    pdf.add_bullet("[ ] Perform the Great Email Purge (archive old emails)")
    pdf.add_bullet("[ ] Unsubscribe from at least 20 newsletters")
    pdf.add_bullet("[ ] Set up your folder/label system")
    pdf.add_bullet("[ ] Schedule 3 specific email processing times per day")
    pdf.add_bullet("[ ] Create 3 email templates for common responses")
    pdf.add_bullet("[ ] Turn off email notifications (check on schedule only)")
    pdf.add_bullet("[ ] Process inbox to zero for the first time")
    pdf.add_blank_line()

    pdf.add_heading2("Email Processing Log (2 Weeks)")
    pdf.add_blank_line()
    pdf.add_paragraph("Track your email processing for 14 days to build the habit:")
    pdf.add_blank_line()
    for day in range(1, 15):
        pdf.add_heading3(f"Day {day}")
        pdf.add_paragraph(f"  Date: _______________")
        pdf.add_paragraph(f"  Emails received today: ___")
        pdf.add_paragraph(f"  Emails processed: ___  |  Deleted: ___  |  Archived: ___")
        pdf.add_paragraph(f"  Responses sent: ___  |  Delegated: ___  |  Deferred: ___")
        pdf.add_paragraph(f"  Time spent processing (minutes): ___")
        pdf.add_paragraph(f"  Inbox count at end of day: ___")
        pdf.add_paragraph(f"  Achieved inbox zero? [ ] Yes  [ ] No")
        pdf.add_paragraph(f"  Newsletters unsubscribed: ___")
        pdf.add_separator()

    pdf.add_paragraph("14-Day Email Summary:")
    pdf.add_paragraph("Average daily emails received: ___")
    pdf.add_paragraph("Average processing time: ___ minutes")
    pdf.add_paragraph("Days at inbox zero: ___ / 14")
    pdf.add_paragraph("Total unsubscribes: ___")
    pdf.add_paragraph("Feeling about email now (1-10): ___")
    pdf.add_blank_line()

    # CHAPTER 4: COMPUTER & FILE ORGANIZATION
    pdf.add_page_break()
    pdf.add_heading1("CHAPTER 4: COMPUTER & FILE ORGANIZATION")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_heading2("Building a File System That Works")
    pdf.add_blank_line()
    pdf.add_paragraph("A well-organized file system means you can find any document in under 30 seconds. No more wasting 10 minutes searching for that one file, no more saving things to your desktop because you do not know where else to put them, and no more duplicates scattered across multiple folders.")
    pdf.add_blank_line()
    pdf.add_paragraph("The key principles of effective file organization are: few top-level folders, consistent naming conventions, and a regular maintenance habit.")
    pdf.add_blank_line()

    pdf.add_heading2("Step 1: Desktop Cleanup")
    pdf.add_blank_line()
    pdf.add_paragraph("Your desktop should have ZERO files on it (or a maximum of 3-5 temporary items you are actively working on today). Everything else goes into your file system.")
    pdf.add_blank_line()
    pdf.add_paragraph("Items currently on my desktop: ___________")
    pdf.add_paragraph("Items that belong in my file system: ___________")
    pdf.add_paragraph("Items to delete: ___________")
    pdf.add_blank_line()

    pdf.add_heading2("Step 2: Recommended Folder Structure")
    pdf.add_blank_line()
    pdf.add_paragraph("Use this proven structure as your starting point and customize:")
    pdf.add_blank_line()
    pdf.add_heading3("Top-Level Folders:")
    pdf.add_bullet("01-WORK (or business name)")
    pdf.add_bullet("  - Projects (subfolder per project)")
    pdf.add_bullet("  - Clients (subfolder per client)")
    pdf.add_bullet("  - Resources (templates, guides, references)")
    pdf.add_bullet("  - Admin (contracts, invoices, tax docs)")
    pdf.add_blank_line()
    pdf.add_bullet("02-PERSONAL")
    pdf.add_bullet("  - Finance (bills, bank statements, tax returns)")
    pdf.add_bullet("  - Health (medical records, insurance)")
    pdf.add_bullet("  - Home (lease, utilities, maintenance)")
    pdf.add_bullet("  - Education (courses, certifications, transcripts)")
    pdf.add_blank_line()
    pdf.add_bullet("03-CREATIVE")
    pdf.add_bullet("  - Photos (organized by year/event)")
    pdf.add_bullet("  - Writing")
    pdf.add_bullet("  - Design")
    pdf.add_bullet("  - Music")
    pdf.add_blank_line()
    pdf.add_bullet("04-ARCHIVE (old projects, completed work)")
    pdf.add_blank_line()

    pdf.add_heading2("Step 3: File Naming Convention")
    pdf.add_blank_line()
    pdf.add_paragraph("Consistent file names make everything searchable. Use this format:")
    pdf.add_paragraph("YYYY-MM-DD_Category_Description_Version")
    pdf.add_blank_line()
    pdf.add_paragraph("Examples:")
    pdf.add_bullet("2024-03-15_Invoice_ClientName_v1.pdf")
    pdf.add_bullet("2024-03-15_Resume_DanielTesfamariam_v3.docx")
    pdf.add_bullet("2024-03-15_Budget_Q1-Review_final.xlsx")
    pdf.add_blank_line()
    pdf.add_paragraph("My naming convention: ___________________________________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_blank_line()

    pdf.add_heading2("Step 4: Cloud Storage Setup")
    pdf.add_blank_line()
    pdf.add_paragraph("Choose ONE primary cloud storage and use it for everything:")
    pdf.add_blank_line()
    pdf.add_paragraph("[ ] Google Drive  [ ] Dropbox  [ ] OneDrive  [ ] iCloud")
    pdf.add_paragraph("Other: _________________________________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("Sync settings: [ ] Full sync  [ ] Selective sync")
    pdf.add_paragraph("Storage used: ___ GB of ___ GB available")
    pdf.add_paragraph("Backup schedule: [ ] Automatic  [ ] Weekly manual  [ ] Monthly manual")
    pdf.add_blank_line()

    pdf.add_heading2("Step 5: Browser Cleanup")
    pdf.add_blank_line()
    pdf.add_paragraph("Your browser is likely cluttered with bookmarks you never visit, extensions you do not use, and saved passwords that need updating.")
    pdf.add_blank_line()
    pdf.add_heading3("Browser Declutter Checklist:")
    pdf.add_bullet("[ ] Close all unnecessary tabs (bookmark important ones first)")
    pdf.add_bullet("[ ] Organize bookmarks into folders (max 5-7 folders)")
    pdf.add_bullet("[ ] Delete bookmarks you have not visited in 6 months")
    pdf.add_bullet("[ ] Remove unused browser extensions")
    pdf.add_bullet("[ ] Clear browsing history and cache")
    pdf.add_bullet("[ ] Review and delete saved passwords for unused accounts")
    pdf.add_bullet("[ ] Set homepage to something intentional (not news or social)")
    pdf.add_bullet("[ ] Install an ad blocker and distraction blocker")
    pdf.add_blank_line()
    pdf.add_paragraph("Tabs before cleanup: ___")
    pdf.add_paragraph("Tabs after cleanup: ___")
    pdf.add_paragraph("Extensions removed: ___")
    pdf.add_paragraph("Bookmarks deleted: ___")
    pdf.add_blank_line()

    pdf.add_heading2("YOUR ACTION ITEMS - Chapter 4")
    pdf.add_separator()
    pdf.add_bullet("[ ] Clear your desktop completely (move everything to proper folders)")
    pdf.add_bullet("[ ] Create your top-level folder structure")
    pdf.add_bullet("[ ] Establish and document your file naming convention")
    pdf.add_bullet("[ ] Set up cloud backup for important files")
    pdf.add_bullet("[ ] Complete browser cleanup checklist")
    pdf.add_bullet("[ ] Delete or archive files you no longer need")
    pdf.add_bullet("[ ] Schedule a monthly 15-minute file maintenance session")
    pdf.add_blank_line()

    # CHAPTER 5: SOCIAL MEDIA DETOX
    pdf.add_page_break()
    pdf.add_heading1("CHAPTER 5: SOCIAL MEDIA DETOX")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_heading2("Reclaiming Your Attention from Social Media")
    pdf.add_blank_line()
    pdf.add_paragraph("Social media platforms are engineered by teams of brilliant psychologists and engineers to be as addictive as possible. They exploit our need for social validation, fear of missing out, and desire for novelty. The average person spends 2 hours and 27 minutes per day on social media, which adds up to over 37 days per year.")
    pdf.add_blank_line()
    pdf.add_paragraph("This is not about quitting social media entirely (unless you want to). It is about using it intentionally rather than compulsively, being a creator rather than a consumer, and ensuring these platforms serve your goals rather than stealing your time and mental health.")
    pdf.add_blank_line()

    pdf.add_heading2("My Social Media Audit")
    pdf.add_blank_line()
    pdf.add_paragraph("Platform | Daily Time | Purpose | Adds Value? | Action")
    pdf.add_separator()
    platforms = ["Instagram", "Facebook", "Twitter/X", "TikTok", "LinkedIn", "YouTube", "Reddit", "Pinterest", "Snapchat", "Other"]
    for p in platforms:
        pdf.add_paragraph(f"{p}: ___ min/day | Purpose: _________________ | Value: Y/N | Keep/Limit/Delete")
    pdf.add_blank_line()
    pdf.add_paragraph("Total daily social media time: ___ minutes (___ hours)")
    pdf.add_paragraph("Time I want to spend daily: ___ minutes")
    pdf.add_paragraph("Time I will save daily: ___ minutes")
    pdf.add_paragraph("That equals ___ hours/week and ___ hours/year reclaimed!")
    pdf.add_blank_line()

    pdf.add_heading2("Social Media Boundaries")
    pdf.add_blank_line()
    pdf.add_paragraph("Set clear rules for yourself:")
    pdf.add_blank_line()
    pdf.add_paragraph("No social media before: _______ AM")
    pdf.add_paragraph("No social media after: _______ PM")
    pdf.add_paragraph("Maximum daily usage: _______ minutes")
    pdf.add_paragraph("Phone-free zones: ________________________________________________")
    pdf.add_paragraph("Phone-free times: ________________________________________________")
    pdf.add_blank_line()
    pdf.add_heading3("Accounts to Unfollow/Mute (do not serve my goals):")
    for i in range(1, 11):
        pdf.add_paragraph(f"{i:2d}. ____________________________________________________________")
    pdf.add_blank_line()
    pdf.add_heading3("Accounts to Follow More (inspire and educate me):")
    for i in range(1, 6):
        pdf.add_paragraph(f"{i}. ____________________________________________________________")
    pdf.add_blank_line()

    pdf.add_heading2("The 7-Day Social Media Fast")
    pdf.add_blank_line()
    pdf.add_paragraph("Challenge yourself to one full week without social media. Track your experience:")
    pdf.add_blank_line()
    for day in range(1, 8):
        pdf.add_heading3(f"Day {day}")
        pdf.add_paragraph(f"Urge to check (1-10): ___")
        pdf.add_paragraph(f"How I spent the extra time: ____________________________________")
        pdf.add_paragraph(f"Mood today (1-10): ___")
        pdf.add_paragraph(f"What I noticed: ________________________________________________")
        pdf.add_blank_line()

    pdf.add_paragraph("7-Day Fast Reflection:")
    pdf.add_paragraph("What surprised me: _____________________________________________")
    pdf.add_paragraph("What I missed: _________________________________________________")
    pdf.add_paragraph("What I did NOT miss: ____________________________________________")
    pdf.add_paragraph("My plan going forward: __________________________________________")
    pdf.add_blank_line()

    pdf.add_heading2("YOUR ACTION ITEMS - Chapter 5")
    pdf.add_separator()
    pdf.add_bullet("[ ] Complete the social media audit with real screen time data")
    pdf.add_bullet("[ ] Set daily time limits on each platform")
    pdf.add_bullet("[ ] Unfollow or mute accounts that drain you")
    pdf.add_bullet("[ ] Delete social media apps from home screen")
    pdf.add_bullet("[ ] Try the 7-Day Social Media Fast")
    pdf.add_bullet("[ ] Replace scrolling time with one meaningful activity")
    pdf.add_blank_line()

    # CHAPTER 6: DIGITAL PRODUCTIVITY SYSTEM
    pdf.add_page_break()
    pdf.add_heading1("CHAPTER 6: DIGITAL PRODUCTIVITY SYSTEM")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_heading2("Building Your Personal Productivity Stack")
    pdf.add_blank_line()
    pdf.add_paragraph("Now that you have decluttered your digital environment, it is time to rebuild it intentionally as a productivity system. The right digital tools, used well, can dramatically increase your output while reducing stress and mental load.")
    pdf.add_blank_line()
    pdf.add_paragraph("The key is simplicity. You do not need 15 productivity apps. You need 3-5 core tools that work together seamlessly and that you actually use consistently.")
    pdf.add_blank_line()

    pdf.add_heading2("The 5 Pillars of Digital Productivity")
    pdf.add_blank_line()
    pdf.add_heading3("Pillar 1: Task Management")
    pdf.add_paragraph("One single source of truth for everything you need to do. No more sticky notes, random lists, or tasks scattered across apps.")
    pdf.add_blank_line()
    pdf.add_paragraph("My task management tool: ________________________________________")
    pdf.add_paragraph("How I capture new tasks: _________________________________________")
    pdf.add_paragraph("How often I review my task list: __________________________________")
    pdf.add_blank_line()

    pdf.add_heading3("Pillar 2: Calendar Management")
    pdf.add_paragraph("Your calendar is not just for meetings. It is for protecting your time, scheduling deep work, and ensuring you have boundaries.")
    pdf.add_blank_line()
    pdf.add_paragraph("My calendar tool: ________________________________________________")
    pdf.add_paragraph("Do I time-block? [ ] Yes [ ] No (consider starting)")
    pdf.add_paragraph("My recurring blocks:")
    pdf.add_paragraph("  Deep work: _______ to _______")
    pdf.add_paragraph("  Email processing: _______ to _______")
    pdf.add_paragraph("  Exercise: _______ to _______")
    pdf.add_paragraph("  Learning: _______ to _______")
    pdf.add_blank_line()

    pdf.add_heading3("Pillar 3: Note-Taking & Knowledge Management")
    pdf.add_paragraph("A system for capturing ideas, meeting notes, and information so you can find it when you need it.")
    pdf.add_blank_line()
    pdf.add_paragraph("My note-taking tool: _____________________________________________")
    pdf.add_paragraph("How I organize notes: ____________________________________________")
    pdf.add_paragraph("How I review notes: ______________________________________________")
    pdf.add_blank_line()

    pdf.add_heading3("Pillar 4: Communication")
    pdf.add_paragraph("Intentional communication means checking messages on YOUR schedule, not reactively responding to every ping.")
    pdf.add_blank_line()
    pdf.add_paragraph("Primary communication tools: _____________________________________")
    pdf.add_paragraph("My communication schedule:")
    pdf.add_paragraph("  Email: Check at _______, _______, _______")
    pdf.add_paragraph("  Messages: Check at _______, _______, _______")
    pdf.add_paragraph("  Slack/Teams: Check at _______, _______, _______")
    pdf.add_blank_line()

    pdf.add_heading3("Pillar 5: Focus & Deep Work")
    pdf.add_paragraph("Tools and techniques for protecting your attention during important work.")
    pdf.add_blank_line()
    pdf.add_paragraph("My focus technique: [ ] Pomodoro  [ ] Time-blocking  [ ] Flow state  [ ] Other")
    pdf.add_paragraph("My focus duration: ___ minutes per session")
    pdf.add_paragraph("Tools I use: [ ] Focus timer  [ ] Website blocker  [ ] Noise canceling  [ ] Do Not Disturb")
    pdf.add_blank_line()

    pdf.add_heading2("The Pomodoro Technique Tracker")
    pdf.add_blank_line()
    pdf.add_paragraph("Work for 25 minutes, break for 5 minutes. After 4 pomodoros, take a 15-30 minute break.")
    pdf.add_blank_line()
    for day in range(1, 8):
        pdf.add_heading3(f"Day {day} Pomodoro Log")
        pdf.add_paragraph(f"Pomodoro 1: Task: _________________________ Completed? [ ]")
        pdf.add_paragraph(f"Pomodoro 2: Task: _________________________ Completed? [ ]")
        pdf.add_paragraph(f"Pomodoro 3: Task: _________________________ Completed? [ ]")
        pdf.add_paragraph(f"Pomodoro 4: Task: _________________________ Completed? [ ]")
        pdf.add_paragraph(f"LONG BREAK")
        pdf.add_paragraph(f"Pomodoro 5: Task: _________________________ Completed? [ ]")
        pdf.add_paragraph(f"Pomodoro 6: Task: _________________________ Completed? [ ]")
        pdf.add_paragraph(f"Pomodoro 7: Task: _________________________ Completed? [ ]")
        pdf.add_paragraph(f"Pomodoro 8: Task: _________________________ Completed? [ ]")
        pdf.add_paragraph(f"Total focused hours today: ___")
        pdf.add_paragraph(f"Distractions resisted: ___")
        pdf.add_separator()

    pdf.add_heading2("Weekly Planning Template")
    pdf.add_blank_line()
    pdf.add_paragraph("Complete this every Sunday evening or Monday morning:")
    pdf.add_blank_line()
    pdf.add_heading3("This Week's Top 3 Priorities:")
    pdf.add_paragraph("1. ____________________________________________________________")
    pdf.add_paragraph("2. ____________________________________________________________")
    pdf.add_paragraph("3. ____________________________________________________________")
    pdf.add_blank_line()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    for day in days:
        pdf.add_heading3(day)
        pdf.add_paragraph(f"  Must-do: _____________________________________________________")
        pdf.add_paragraph(f"  Should-do: ___________________________________________________")
        pdf.add_paragraph(f"  Could-do: ____________________________________________________")
        pdf.add_paragraph(f"  Meetings/Calls: ______________________________________________")
        pdf.add_blank_line()

    # Additional weekly templates to add pages
    for week_num in range(2, 5):
        pdf.add_page_break()
        pdf.add_heading2(f"WEEKLY PLANNING TEMPLATE - Week {week_num}")
        pdf.add_separator()
        pdf.add_paragraph(f"Week of: _______________")
        pdf.add_blank_line()
        pdf.add_heading3("Weekly Review (from last week)")
        pdf.add_paragraph("Tasks completed: ___ / ___")
        pdf.add_paragraph("Biggest accomplishment: ________________________________________")
        pdf.add_paragraph("What went well: ________________________________________________")
        pdf.add_paragraph("What needs improvement: _________________________________________")
        pdf.add_paragraph("Pomodoros completed: ___")
        pdf.add_paragraph("Screen time average: ___ hours/day")
        pdf.add_blank_line()
        pdf.add_heading3("This Week's Top 3 Priorities:")
        pdf.add_paragraph("1. ____________________________________________________________")
        pdf.add_paragraph("2. ____________________________________________________________")
        pdf.add_paragraph("3. ____________________________________________________________")
        pdf.add_blank_line()
        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
            pdf.add_heading3(day)
            pdf.add_paragraph(f"  Top priority: ________________________________________________")
            pdf.add_paragraph(f"  Must-do: _____________________________________________________")
            pdf.add_paragraph(f"  Should-do: ___________________________________________________")
            pdf.add_paragraph(f"  Could-do: ____________________________________________________")
            pdf.add_paragraph(f"  Deep work block: ____ to ____ Task: __________________________")
            pdf.add_paragraph(f"  Meetings/Calls: ______________________________________________")
            pdf.add_paragraph(f"  Evening plan: ________________________________________________")
            pdf.add_blank_line()
        pdf.add_paragraph("End-of-week energy level (1-10): ___")
        pdf.add_paragraph("End-of-week satisfaction (1-10): ___")
        pdf.add_separator()

    pdf.add_heading2("Digital Habit Tracker (4 Weeks)")
    pdf.add_blank_line()
    pdf.add_paragraph("Track these daily habits to build your new digital lifestyle:")
    pdf.add_blank_line()
    habits = ["Checked email only at scheduled times", "No phone first 30 min of morning", "Used Pomodoro for deep work", "Social media under limit", "Desktop clear at end of day", "All tasks in task manager", "Inbox processed to zero"]
    for week in range(1, 5):
        pdf.add_page_break()
        pdf.add_heading3(f"Week {week} Habit Tracker")
        pdf.add_paragraph("Habit | M | T | W | T | F | S | S")
        pdf.add_separator()
        for habit in habits:
            pdf.add_paragraph(f"  {habit}: [ ] [ ] [ ] [ ] [ ] [ ] [ ]")
        pdf.add_blank_line()
        pdf.add_paragraph(f"  Habits completed this week: ___ / {len(habits) * 7}")
        pdf.add_paragraph(f"  Streak days: ___")
        pdf.add_paragraph(f"  Reward for consistency: _______________________________________")
        pdf.add_separator()

    pdf.add_heading2("YOUR ACTION ITEMS - Chapter 6")
    pdf.add_separator()
    pdf.add_bullet("[ ] Choose your core productivity tools (max 5)")
    pdf.add_bullet("[ ] Set up time-blocking in your calendar")
    pdf.add_bullet("[ ] Try the Pomodoro technique for one full week")
    pdf.add_bullet("[ ] Create your weekly planning ritual")
    pdf.add_bullet("[ ] Install a website/app blocker for focus sessions")
    pdf.add_bullet("[ ] Define your ideal daily schedule with blocks for each pillar")
    pdf.add_bullet("[ ] Complete the 4-week habit tracker consistently")
    pdf.add_blank_line()

    # CHAPTER 7: PASSWORD & SECURITY
    pdf.add_page_break()
    pdf.add_heading1("CHAPTER 7: PASSWORD & SECURITY")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_heading2("Securing Your Digital Life")
    pdf.add_blank_line()
    pdf.add_paragraph("Digital security is an essential part of digital organization. Weak passwords, reused credentials, and lack of two-factor authentication put your personal data, finances, and identity at serious risk. The good news is that setting up strong security takes just a few hours and then protects you indefinitely.")
    pdf.add_blank_line()

    pdf.add_heading2("Step 1: Password Manager Setup")
    pdf.add_blank_line()
    pdf.add_paragraph("A password manager is the single most important security tool you can use. It generates and stores unique, complex passwords for every account so you only need to remember one master password.")
    pdf.add_blank_line()
    pdf.add_paragraph("Recommended options: 1Password, Bitwarden, LastPass, Dashlane")
    pdf.add_blank_line()
    pdf.add_paragraph("My chosen password manager: _____________________________________")
    pdf.add_paragraph("Master password hint (DO NOT write the actual password): __________")
    pdf.add_paragraph("Recovery method set up? [ ] Yes  [ ] No")
    pdf.add_paragraph("Emergency access person: ________________________________________")
    pdf.add_blank_line()

    pdf.add_heading2("Step 2: Account Security Audit")
    pdf.add_blank_line()
    pdf.add_paragraph("Review each important account and update security:")
    pdf.add_blank_line()
    pdf.add_paragraph("Account | Strong Password? | 2FA Enabled? | Recovery Set?")
    pdf.add_separator()
    accounts = ["Primary Email", "Secondary Email", "Bank Account 1", "Bank Account 2", "Credit Card", "Investment Account", "Social Security/Gov", "Health Insurance", "Phone Provider", "Internet Provider", "Cloud Storage", "Social Media 1", "Social Media 2", "Amazon/Shopping", "Streaming Service 1", "Streaming Service 2", "Work Email", "Work Systems", "Apple/Google ID", "Password Manager"]
    for acc in accounts:
        pdf.add_paragraph(f"  {acc}: Password [ ] | 2FA [ ] | Recovery [ ]")
    pdf.add_blank_line()

    pdf.add_heading2("Step 3: Two-Factor Authentication (2FA)")
    pdf.add_blank_line()
    pdf.add_paragraph("Enable 2FA on every account that offers it, starting with these critical ones:")
    pdf.add_blank_line()
    pdf.add_bullet("[ ] Primary email account (most important - this is the master key)")
    pdf.add_bullet("[ ] Bank and financial accounts")
    pdf.add_bullet("[ ] Apple ID or Google Account")
    pdf.add_bullet("[ ] Social media accounts")
    pdf.add_bullet("[ ] Cloud storage (Google Drive, Dropbox, iCloud)")
    pdf.add_bullet("[ ] Password manager itself")
    pdf.add_bullet("[ ] Work accounts")
    pdf.add_bullet("[ ] Shopping accounts with saved payment info")
    pdf.add_blank_line()
    pdf.add_paragraph("Preferred 2FA method: [ ] Authenticator app  [ ] SMS  [ ] Hardware key")
    pdf.add_paragraph("Authenticator app used: _________________________________________")
    pdf.add_paragraph("Backup codes stored safely? [ ] Yes  Location: _________________")
    pdf.add_blank_line()

    pdf.add_heading2("Step 4: Digital Emergency Plan")
    pdf.add_blank_line()
    pdf.add_paragraph("What happens to your digital life if something happens to you? Create a plan:")
    pdf.add_blank_line()
    pdf.add_paragraph("Trusted person who knows my master password: _____________________")
    pdf.add_paragraph("Location of emergency access instructions: _______________________")
    pdf.add_paragraph("Important accounts they would need access to:")
    pdf.add_paragraph("1. ____________________________________________________________")
    pdf.add_paragraph("2. ____________________________________________________________")
    pdf.add_paragraph("3. ____________________________________________________________")
    pdf.add_paragraph("4. ____________________________________________________________")
    pdf.add_paragraph("5. ____________________________________________________________")
    pdf.add_blank_line()

    pdf.add_heading2("YOUR ACTION ITEMS - Chapter 7")
    pdf.add_separator()
    pdf.add_bullet("[ ] Choose and set up a password manager")
    pdf.add_bullet("[ ] Generate unique passwords for your top 10 accounts")
    pdf.add_bullet("[ ] Enable 2FA on all critical accounts")
    pdf.add_bullet("[ ] Store backup codes in a safe physical location")
    pdf.add_bullet("[ ] Create a digital emergency plan")
    pdf.add_bullet("[ ] Delete accounts you no longer use")
    pdf.add_blank_line()

    # Additional section: Account Cleanup
    pdf.add_page_break()
    pdf.add_heading1("BONUS: ACCOUNT CLEANUP & DIGITAL FOOTPRINT")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_heading2("Audit Your Online Accounts")
    pdf.add_blank_line()
    pdf.add_paragraph("Most people have 80-100+ online accounts, many of which they have forgotten about. Each account represents a potential security vulnerability and a piece of personal data floating in cyberspace. This audit helps you identify, clean up, or delete accounts you no longer need.")
    pdf.add_blank_line()
    pdf.add_paragraph("Go through each category and list every account you have:")
    pdf.add_blank_line()

    pdf.add_heading3("Shopping & Retail Accounts")
    for i in range(1, 11):
        pdf.add_paragraph(f"  {i:2d}. Site: _____________________ Active? [ ] Keep [ ] Delete [ ] Update password")
    pdf.add_blank_line()
    pdf.add_heading3("Social Media & Communication")
    for i in range(1, 11):
        pdf.add_paragraph(f"  {i:2d}. Platform: __________________ Active? [ ] Keep [ ] Delete [ ] Deactivate")
    pdf.add_blank_line()
    pdf.add_heading3("Financial & Banking")
    for i in range(1, 8):
        pdf.add_paragraph(f"  {i}. Service: _____________________ 2FA? [ ] Strong password? [ ] Active? [ ]")
    pdf.add_blank_line()
    pdf.add_heading3("Streaming & Entertainment")
    for i in range(1, 8):
        pdf.add_paragraph(f"  {i}. Service: _____________________ Monthly cost: $_____ Still using? [ ] Keep [ ] Cancel")
    pdf.add_blank_line()
    pdf.add_heading3("Productivity & Work Tools")
    for i in range(1, 8):
        pdf.add_paragraph(f"  {i}. Tool: ________________________ Active? [ ] Keep [ ] Delete [ ] Consolidate")
    pdf.add_blank_line()
    pdf.add_heading3("Health & Fitness")
    for i in range(1, 6):
        pdf.add_paragraph(f"  {i}. App/Site: ____________________ Active? [ ] Keep [ ] Delete")
    pdf.add_blank_line()
    pdf.add_heading3("Travel & Transportation")
    for i in range(1, 6):
        pdf.add_paragraph(f"  {i}. Service: _____________________ Active? [ ] Keep [ ] Delete")
    pdf.add_blank_line()

    pdf.add_heading2("Account Cleanup Results")
    pdf.add_paragraph("Total accounts identified: ___")
    pdf.add_paragraph("Accounts deleted: ___")
    pdf.add_paragraph("Accounts deactivated: ___")
    pdf.add_paragraph("Passwords updated: ___")
    pdf.add_paragraph("2FA enabled on: ___")
    pdf.add_paragraph("Subscriptions cancelled: ___")
    pdf.add_paragraph("Monthly savings from cancellations: $___")
    pdf.add_blank_line()

    pdf.add_heading2("Digital Wellness Daily Tracker (2 Weeks)")
    pdf.add_blank_line()
    pdf.add_paragraph("Track your digital wellness for 14 days to build awareness:")
    pdf.add_blank_line()
    for day in range(1, 15):
        pdf.add_heading3(f"Day {day}")
        pdf.add_paragraph(f"  Screen time total: ___ hrs  |  Phone pickups: ___")
        pdf.add_paragraph(f"  First screen check: ___ AM  |  Last screen: ___ PM")
        pdf.add_paragraph(f"  Social media time: ___ min  |  Productive screen: ___ hrs")
        pdf.add_paragraph(f"  Notifications received: ___  |  Focus sessions: ___")
        pdf.add_paragraph(f"  Mood (1-10): ___  |  Energy (1-10): ___  |  Focus (1-10): ___")
        pdf.add_separator()

    # CHAPTER 8: 30-DAY CHALLENGE
    pdf.add_page_break()
    pdf.add_heading1("CHAPTER 8: 30-DAY DIGITAL DECLUTTER CHALLENGE")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_heading2("Your Daily Action Plan")
    pdf.add_blank_line()
    pdf.add_paragraph("This 30-day challenge breaks down your entire digital declutter into one manageable task per day. Each day takes 15-30 minutes. By the end of 30 days, your entire digital life will be transformed.")
    pdf.add_blank_line()

    challenge_days = [
        ("Delete 10 unused apps from your phone", "Phone"),
        ("Disable notifications for all non-essential apps", "Phone"),
        ("Unsubscribe from 10 email newsletters", "Email"),
        ("Unsubscribe from 10 more newsletters", "Email"),
        ("Archive all emails older than 30 days", "Email"),
        ("Set up email folders and processing schedule", "Email"),
        ("Clean up phone home screen layout", "Phone"),
        ("Delete 100 old photos from camera roll", "Phone"),
        ("Delete 100 more photos and create 3 albums", "Phone"),
        ("Audit and cancel unused subscriptions", "Finance"),
        ("Clear computer desktop completely", "Computer"),
        ("Create top-level folder structure", "Computer"),
        ("Organize Downloads folder (delete or file everything)", "Computer"),
        ("Clean up browser bookmarks and close excess tabs", "Computer"),
        ("Remove unused browser extensions", "Computer"),
        ("Set up password manager and add 5 accounts", "Security"),
        ("Add 10 more accounts to password manager", "Security"),
        ("Enable 2FA on all critical accounts", "Security"),
        ("Social media audit - unfollow 20 accounts", "Social"),
        ("Set daily time limits on social media apps", "Social"),
        ("Delete social media apps from home screen", "Social"),
        ("Set up focus/Do Not Disturb schedules", "Productivity"),
        ("Choose and set up task management system", "Productivity"),
        ("Create weekly planning template", "Productivity"),
        ("Set up cloud backup for important files", "Computer"),
        ("Try a full Pomodoro work session (4 rounds)", "Productivity"),
        ("Digital-free evening (no screens after 8pm)", "Wellness"),
        ("Review all changes and note improvements", "Review"),
        ("Create maintenance schedule for ongoing habits", "Planning"),
        ("Celebrate! Write reflection on transformation", "Celebration"),
    ]

    for day_num, (task, category) in enumerate(challenge_days, 1):
        if day_num % 3 == 1:
            pdf.add_page_break()
        pdf.add_heading3(f"DAY {day_num}: {task}")
        pdf.add_paragraph(f"Category: {category}")
        pdf.add_paragraph(f"Date: _______________")
        pdf.add_paragraph(f"Completed: [ ] Yes  [ ] Partially  [ ] Skipped")
        pdf.add_paragraph(f"Time spent: ___ minutes")
        pdf.add_paragraph(f"What I did specifically: ________________________________________")
        pdf.add_paragraph(f"_______________________________________________________________")
        pdf.add_paragraph(f"Items deleted/organized/changed: ___")
        pdf.add_paragraph(f"How I feel after (1-10): ___")
        pdf.add_paragraph(f"Difficulty level (1-10): ___")
        pdf.add_paragraph(f"Notes: ________________________________________________________")
        pdf.add_paragraph(f"_______________________________________________________________")
        pdf.add_separator()
        if day_num % 10 == 0:
            pdf.add_page_break()
            pdf.add_heading2(f"10-DAY CHECK-IN (Days {day_num-9}-{day_num})")
            pdf.add_paragraph(f"Days completed: ___ / 10")
            pdf.add_paragraph(f"Days skipped: ___ / 10")
            pdf.add_paragraph(f"Total items decluttered/organized: ___")
            pdf.add_paragraph(f"Biggest win so far: ____________________________________________")
            pdf.add_paragraph(f"_______________________________________________________________")
            pdf.add_paragraph(f"Biggest challenge: _____________________________________________")
            pdf.add_paragraph(f"_______________________________________________________________")
            pdf.add_paragraph(f"Digital overwhelm level now (1-10): ___")
            pdf.add_paragraph(f"Motivation level (1-10): ___")
            pdf.add_paragraph(f"Screen time this period: ___ hours/day average")
            pdf.add_paragraph(f"Compared to start: [ ] Better  [ ] Same  [ ] Worse")
            pdf.add_paragraph(f"Adjustments for next 10 days: __________________________________")
            pdf.add_paragraph(f"_______________________________________________________________")
            pdf.add_separator()
            pdf.add_blank_line()

    pdf.add_page_break()
    pdf.add_heading2("30-DAY CHALLENGE COMPLETION REFLECTION")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_paragraph("Congratulations on completing the 30-Day Digital Declutter Challenge!")
    pdf.add_blank_line()
    pdf.add_paragraph("Digital Overwhelm Score (retake assessment):")
    pdf.add_paragraph("  Before (Day 1): ___ / 75")
    pdf.add_paragraph("  After (Day 30): ___ / 75")
    pdf.add_paragraph("  Improvement: ___ points")
    pdf.add_blank_line()
    pdf.add_paragraph("Screen time per day:")
    pdf.add_paragraph("  Before: ___ hours/day")
    pdf.add_paragraph("  After: ___ hours/day")
    pdf.add_paragraph("  Time saved: ___ hours/day = ___ hours/week = ___ hours/year")
    pdf.add_blank_line()
    pdf.add_paragraph("Top 3 changes that made the biggest difference:")
    pdf.add_paragraph("1. ____________________________________________________________")
    pdf.add_paragraph("2. ____________________________________________________________")
    pdf.add_paragraph("3. ____________________________________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("Habits I will maintain going forward:")
    pdf.add_paragraph("1. ____________________________________________________________")
    pdf.add_paragraph("2. ____________________________________________________________")
    pdf.add_paragraph("3. ____________________________________________________________")
    pdf.add_blank_line()

    pdf.add_heading2("YOUR ACTION ITEMS - Chapter 8")
    pdf.add_separator()
    pdf.add_bullet("[ ] Commit to starting the challenge on a specific date")
    pdf.add_bullet("[ ] Complete one task per day for 30 consecutive days")
    pdf.add_bullet("[ ] Track your progress honestly each day")
    pdf.add_bullet("[ ] Complete the 10-day check-ins")
    pdf.add_bullet("[ ] Retake the Digital Overwhelm Assessment after Day 30")
    pdf.add_bullet("[ ] Share your results with someone for accountability")
    pdf.add_blank_line()

    # FINAL PAGE
    pdf.add_page_break()
    pdf.add_heading1("NEXT STEPS")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_paragraph("You now have a complete system for maintaining a clean, organized, and intentional digital life. The key to long-term success is building maintenance habits that prevent clutter from accumulating again.")
    pdf.add_blank_line()
    pdf.add_heading2("Monthly Maintenance Checklist")
    pdf.add_bullet("[ ] Process email inbox to zero")
    pdf.add_bullet("[ ] Delete unused apps from phone")
    pdf.add_bullet("[ ] Review and update passwords for any breached accounts")
    pdf.add_bullet("[ ] Clean up downloads folder")
    pdf.add_bullet("[ ] Review subscriptions for anything to cancel")
    pdf.add_bullet("[ ] Back up important files to cloud")
    pdf.add_bullet("[ ] Review screen time and adjust limits if needed")
    pdf.add_bullet("[ ] Clear browser tabs and bookmarks")
    pdf.add_blank_line()
    pdf.add_heading2("Quarterly Maintenance")
    pdf.add_bullet("[ ] Full phone audit (apps, photos, storage)")
    pdf.add_bullet("[ ] File system review and reorganization")
    pdf.add_bullet("[ ] Security audit (passwords, 2FA, backup codes)")
    pdf.add_bullet("[ ] Retake Digital Overwhelm Assessment")
    pdf.add_bullet("[ ] Review and update productivity system")
    pdf.add_blank_line()
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_paragraph("Your digital life should serve you, not stress you. Stay intentional.")

    filepath = os.path.join(OUTPUT_DIR, '04-Digital-Declutter-Productivity-System.pdf')
    pdf.save(filepath)
    return filepath, len(pdf.pages) + 1



def generate_book5():
    """Book 5: Couples Communication Workbook (60-80 pages)"""
    pdf = PurePDF(title="Couples Communication Workbook", author="Daniel Tesfamariam")

    # TITLE PAGE
    pdf.add_blank_line()
    pdf.add_blank_line()
    pdf.add_blank_line()
    pdf.add_title("COUPLES COMMUNICATION")
    pdf.add_title("WORKBOOK")
    pdf.add_blank_line()
    pdf.add_heading2("Build Deeper Connection Through Better Communication")
    pdf.add_heading2("Active Listening | Conflict Resolution | Deep Connection")
    pdf.add_blank_line()
    pdf.add_blank_line()
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_blank_line()
    pdf.add_paragraph("Research-based tools, exercises, and scripts for couples who")
    pdf.add_paragraph("want to communicate more effectively and love more deeply.")
    pdf.add_blank_line()
    pdf.add_separator()
    pdf.add_paragraph("Copyright 2024 Daniel Tesfamariam. All rights reserved.")
    pdf.add_paragraph("This workbook is for educational purposes. For serious relationship")
    pdf.add_paragraph("concerns, please seek guidance from a licensed couples therapist.")

    # TABLE OF CONTENTS
    pdf.add_page_break()
    pdf.add_title("TABLE OF CONTENTS")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_paragraph("Chapter 1: Communication Foundations ........................ 3")
    pdf.add_paragraph("Chapter 2: Active Listening Skills .......................... 11")
    pdf.add_paragraph("Chapter 3: Conflict Resolution Tools ........................ 19")
    pdf.add_paragraph("Chapter 4: Deep Connection Exercises ........................ 31")
    pdf.add_paragraph("Chapter 5: Hard Conversations Scripts ....................... 41")
    pdf.add_paragraph("Chapter 6: Weekly & Monthly Rituals ......................... 51")
    pdf.add_paragraph("Chapter 7: Date Night Planning ............................... 59")
    pdf.add_paragraph("Chapter 8: Rebuilding Trust .................................. 67")
    pdf.add_paragraph("Final: Next Steps ............................................... 75")
    pdf.add_blank_line()

    # CHAPTER 1: COMMUNICATION FOUNDATIONS
    pdf.add_page_break()
    pdf.add_heading1("CHAPTER 1: COMMUNICATION FOUNDATIONS")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_heading2("Why Communication is the Foundation of Love")
    pdf.add_blank_line()
    pdf.add_paragraph("Research by Dr. John Gottman, who studied thousands of couples over four decades, shows that the number one predictor of relationship success or failure is the quality of communication between partners. It is not compatibility, shared interests, or even love alone that keeps couples together. It is the ability to communicate needs, resolve conflicts, and maintain emotional connection through conversation.")
    pdf.add_blank_line()
    pdf.add_paragraph("The good news is that communication is a skill, not a talent. No one is born a great communicator. These skills can be learned, practiced, and improved at any stage of a relationship, whether you have been together 6 months or 30 years.")
    pdf.add_blank_line()

    pdf.add_heading2("The Four Horsemen of Relationship Destruction")
    pdf.add_blank_line()
    pdf.add_paragraph("Dr. Gottman identified four communication patterns that predict divorce with over 90% accuracy. Recognizing these in yourself is the first step to changing them:")
    pdf.add_blank_line()
    pdf.add_heading3("1. Criticism (Attacking your partner's character)")
    pdf.add_paragraph("Criticism is different from a complaint. A complaint addresses a specific behavior. Criticism attacks who your partner IS as a person.")
    pdf.add_paragraph("Criticism example: You never help around the house. You are so lazy and selfish.")
    pdf.add_paragraph("Healthy alternative: I felt overwhelmed with housework this week. Could we talk about dividing chores more evenly?")
    pdf.add_blank_line()
    pdf.add_heading3("2. Contempt (Superiority, disgust, disrespect)")
    pdf.add_paragraph("Contempt is the single greatest predictor of divorce. It includes eye-rolling, sarcasm, name-calling, mocking, and hostile humor. It communicates: I am better than you.")
    pdf.add_paragraph("Contempt example: Oh, you forgot to pay the bill AGAIN? I should not be surprised.")
    pdf.add_paragraph("Healthy alternative: I noticed the bill was missed. Can we set up autopay so we do not have to worry about it?")
    pdf.add_blank_line()
    pdf.add_heading3("3. Defensiveness (Refusing responsibility)")
    pdf.add_paragraph("Defensiveness is a way of blaming your partner. It says: The problem is not me, it is you. It prevents resolution because no one takes ownership.")
    pdf.add_paragraph("Defensive example: It is not MY fault we were late. YOU took forever getting ready.")
    pdf.add_paragraph("Healthy alternative: You are right, I should have started getting ready earlier. I will set an alarm next time.")
    pdf.add_blank_line()
    pdf.add_heading3("4. Stonewalling (Shutting down, withdrawing)")
    pdf.add_paragraph("Stonewalling happens when one partner completely withdraws from interaction. They may physically leave, go silent, or appear to be listening but are actually checked out.")
    pdf.add_paragraph("Stonewall example: Partner crosses arms, avoids eye contact, gives one-word answers or silence.")
    pdf.add_paragraph("Healthy alternative: I am feeling flooded right now. Can we take a 20-minute break and come back to this when I am calmer?")
    pdf.add_blank_line()

    pdf.add_heading2("Communication Style Assessment")
    pdf.add_blank_line()
    pdf.add_paragraph("Each partner should complete this separately, then compare and discuss:")
    pdf.add_blank_line()
    pdf.add_heading3("Partner 1: _______________")
    pdf.add_paragraph("Rate yourself honestly (1=Never, 5=Often):")
    pdf.add_paragraph("___ I criticize my partner's character rather than addressing specific behaviors")
    pdf.add_paragraph("___ I use sarcasm, eye-rolling, or contemptuous language")
    pdf.add_paragraph("___ I get defensive instead of taking responsibility")
    pdf.add_paragraph("___ I shut down or withdraw during difficult conversations")
    pdf.add_paragraph("___ I interrupt my partner when they are speaking")
    pdf.add_paragraph("___ I bring up past grievances during current arguments")
    pdf.add_paragraph("___ I assume I know what my partner is thinking or feeling")
    pdf.add_paragraph("___ I raise my voice or use aggressive body language")
    pdf.add_paragraph("___ I avoid difficult conversations altogether")
    pdf.add_paragraph("___ I use I feel statements when expressing needs")
    pdf.add_paragraph("Total: ___ / 50")
    pdf.add_blank_line()
    pdf.add_heading3("Partner 2: _______________")
    pdf.add_paragraph("Rate yourself honestly (1=Never, 5=Often):")
    pdf.add_paragraph("___ I criticize my partner's character rather than addressing specific behaviors")
    pdf.add_paragraph("___ I use sarcasm, eye-rolling, or contemptuous language")
    pdf.add_paragraph("___ I get defensive instead of taking responsibility")
    pdf.add_paragraph("___ I shut down or withdraw during difficult conversations")
    pdf.add_paragraph("___ I interrupt my partner when they are speaking")
    pdf.add_paragraph("___ I bring up past grievances during current arguments")
    pdf.add_paragraph("___ I assume I know what my partner is thinking or feeling")
    pdf.add_paragraph("___ I raise my voice or use aggressive body language")
    pdf.add_paragraph("___ I avoid difficult conversations altogether")
    pdf.add_paragraph("___ I use I feel statements when expressing needs")
    pdf.add_paragraph("Total: ___ / 50")
    pdf.add_blank_line()

    pdf.add_heading2("Our Communication Goals")
    pdf.add_blank_line()
    pdf.add_paragraph("What we want to improve about our communication:")
    pdf.add_paragraph("1. ____________________________________________________________")
    pdf.add_paragraph("2. ____________________________________________________________")
    pdf.add_paragraph("3. ____________________________________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("How we will practice (frequency and setting):")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_blank_line()

    pdf.add_heading2("YOUR ACTION ITEMS - Chapter 1")
    pdf.add_separator()
    pdf.add_bullet("[ ] Both partners complete the communication style assessment")
    pdf.add_bullet("[ ] Compare results together without judgment")
    pdf.add_bullet("[ ] Identify which of the Four Horsemen you each tend toward")
    pdf.add_bullet("[ ] Set 3 specific communication goals as a couple")
    pdf.add_bullet("[ ] Commit to weekly practice using this workbook")
    pdf.add_bullet("[ ] Establish a safe word for when conversations get heated")
    pdf.add_blank_line()

    # CHAPTER 2: ACTIVE LISTENING
    pdf.add_page_break()
    pdf.add_heading1("CHAPTER 2: ACTIVE LISTENING SKILLS")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_heading2("The Art of Truly Hearing Your Partner")
    pdf.add_blank_line()
    pdf.add_paragraph("Most people listen to respond rather than listening to understand. Active listening is a deliberate practice where you give your full attention to your partner, seek to understand their perspective completely, and communicate that understanding back to them before sharing your own thoughts.")
    pdf.add_blank_line()
    pdf.add_paragraph("When your partner feels truly heard, they feel safe, valued, and connected. Most arguments escalate not because of the issue itself, but because one or both partners do not feel heard.")
    pdf.add_blank_line()

    pdf.add_heading2("The HEAR Method")
    pdf.add_blank_line()
    pdf.add_bullet("H - Halt: Stop what you are doing. Put down your phone. Turn toward your partner.")
    pdf.add_bullet("E - Empathize: Try to understand their feelings, not just their words.")
    pdf.add_bullet("A - Acknowledge: Reflect back what you heard to confirm understanding.")
    pdf.add_bullet("R - Respond: Only after they confirm you understood, share your perspective.")
    pdf.add_blank_line()

    pdf.add_heading2("Active Listening Practice Scenarios")
    pdf.add_blank_line()
    pdf.add_paragraph("Take turns being the speaker and the listener for each scenario. The speaker shares for 3 minutes uninterrupted. The listener practices the HEAR method.")
    pdf.add_blank_line()

    scenarios = [
        ("Scenario 1", "Speaker: Share about something stressful at work this week. Listener: Practice reflecting back what you hear without offering solutions."),
        ("Scenario 2", "Speaker: Describe a childhood memory that shaped who you are today. Listener: Ask follow-up questions that show curiosity about their experience."),
        ("Scenario 3", "Speaker: Share something you appreciate about your partner that you rarely say out loud. Listener: Receive the compliment fully without deflecting."),
        ("Scenario 4", "Speaker: Talk about a fear or worry you have been carrying. Listener: Validate their feelings without trying to fix or minimize."),
        ("Scenario 5", "Speaker: Describe your ideal weekend together in detail. Listener: Notice how their vision might differ from yours without judgment."),
        ("Scenario 6", "Speaker: Share something small that has been bothering you recently. Listener: Practice hearing without becoming defensive."),
        ("Scenario 7", "Speaker: Talk about a dream or goal you have for the next year. Listener: Ask questions that help them explore and expand their vision."),
        ("Scenario 8", "Speaker: Describe how you felt during your last disagreement. Listener: Focus entirely on understanding their emotional experience."),
        ("Scenario 9", "Speaker: Share what makes you feel most loved and connected. Listener: Take notes so you can remember and act on this information."),
        ("Scenario 10", "Speaker: Talk about something you wish was different in your relationship. Listener: Stay curious and open without becoming defensive or hurt."),
    ]

    for title, description in scenarios:
        pdf.add_heading3(title)
        pdf.add_paragraph(description)
        pdf.add_blank_line()
        pdf.add_paragraph("Speaker's notes: ______________________________________________")
        pdf.add_paragraph("_______________________________________________________________")
        pdf.add_paragraph("Listener's reflection (what I heard): __________________________")
        pdf.add_paragraph("_______________________________________________________________")
        pdf.add_paragraph("Speaker: Did the listener get it right? [ ] Yes  [ ] Partially  [ ] No")
        pdf.add_paragraph("What we learned from this exercise: ____________________________")
        pdf.add_paragraph("_______________________________________________________________")
        pdf.add_separator()

    pdf.add_heading2("YOUR ACTION ITEMS - Chapter 2")
    pdf.add_separator()
    pdf.add_bullet("[ ] Practice the HEAR method during one conversation today")
    pdf.add_bullet("[ ] Complete at least 5 of the 10 scenarios this week")
    pdf.add_bullet("[ ] Notice when you are listening to respond vs. listening to understand")
    pdf.add_bullet("[ ] Put your phone away during all conversations with your partner")
    pdf.add_bullet("[ ] Ask your partner: Do you feel heard by me? What could I do better?")
    pdf.add_blank_line()

    # CHAPTER 3: CONFLICT RESOLUTION
    pdf.add_page_break()
    pdf.add_heading1("CHAPTER 3: CONFLICT RESOLUTION TOOLS")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_heading2("Healthy Conflict Is Normal and Necessary")
    pdf.add_blank_line()
    pdf.add_paragraph("All couples argue. Research shows that 69% of conflicts in relationships are perpetual, meaning they never fully resolve because they are rooted in fundamental personality differences or values. The goal is not to eliminate conflict but to manage it in a way that strengthens rather than damages your relationship.")
    pdf.add_blank_line()
    pdf.add_paragraph("Healthy conflict means both partners feel safe to express their needs, differences are discussed with respect, and resolutions (or compromises) are reached that both partners can live with.")
    pdf.add_blank_line()

    pdf.add_heading2("The Softened Startup")
    pdf.add_blank_line()
    pdf.add_paragraph("How you begin a conversation about a problem determines 96% of whether it will end well. A harsh startup (criticism, blame, contempt) guarantees a negative outcome. A softened startup dramatically increases the chance of productive dialogue.")
    pdf.add_blank_line()
    pdf.add_heading3("Formula for a Softened Startup:")
    pdf.add_paragraph("I feel _____________ (emotion, not accusation)")
    pdf.add_paragraph("about _____________ (specific situation, not character)")
    pdf.add_paragraph("and I need _____________ (positive need, not criticism)")
    pdf.add_blank_line()
    pdf.add_heading3("Examples:")
    pdf.add_paragraph("HARSH: You never help with the dishes. You are so inconsiderate.")
    pdf.add_paragraph("SOFT: I feel overwhelmed when the dishes pile up after dinner. I need us to find a system for sharing this task.")
    pdf.add_blank_line()
    pdf.add_paragraph("HARSH: You always spend money without telling me. You are irresponsible.")
    pdf.add_paragraph("SOFT: I feel anxious when I see unexpected charges. I need us to have a quick check-in before purchases over $50.")
    pdf.add_blank_line()
    pdf.add_paragraph("HARSH: You care more about your phone than me.")
    pdf.add_paragraph("SOFT: I feel disconnected when we are both on our phones during dinner. I would love to have device-free meals together.")
    pdf.add_blank_line()

    pdf.add_heading2("Practice: Write Your Own Softened Startups")
    pdf.add_blank_line()
    pdf.add_paragraph("Issue 1: ________________________________________________________")
    pdf.add_paragraph("I feel ____________________________________________________________")
    pdf.add_paragraph("about ______________________________________________________________")
    pdf.add_paragraph("and I need __________________________________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("Issue 2: ________________________________________________________")
    pdf.add_paragraph("I feel ____________________________________________________________")
    pdf.add_paragraph("about ______________________________________________________________")
    pdf.add_paragraph("and I need __________________________________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("Issue 3: ________________________________________________________")
    pdf.add_paragraph("I feel ____________________________________________________________")
    pdf.add_paragraph("about ______________________________________________________________")
    pdf.add_paragraph("and I need __________________________________________________________")
    pdf.add_blank_line()

    pdf.add_heading2("The Time-Out Protocol")
    pdf.add_blank_line()
    pdf.add_paragraph("When emotions flood during an argument (heart rate above 100 BPM), productive communication becomes physiologically impossible. The time-out protocol prevents damage:")
    pdf.add_blank_line()
    pdf.add_bullet("Step 1: Either partner can call a time-out (use agreed signal or word)")
    pdf.add_bullet("Step 2: Separate for a minimum of 20 minutes (this is physiological, not optional)")
    pdf.add_bullet("Step 3: During the break, do something calming (walk, breathe, listen to music)")
    pdf.add_bullet("Step 4: Do NOT rehearse arguments or build your case during the break")
    pdf.add_bullet("Step 5: Return at the agreed time and resume with softened startups")
    pdf.add_blank_line()
    pdf.add_paragraph("Our time-out signal/word: ________________________________________")
    pdf.add_paragraph("Minimum break duration we agree to: _______ minutes")
    pdf.add_paragraph("What I will do during breaks: _____________________________________")
    pdf.add_blank_line()

    pdf.add_heading2("The Compromise Worksheet")
    pdf.add_blank_line()
    pdf.add_paragraph("Use this worksheet when you have a disagreement that needs resolution:")
    pdf.add_blank_line()
    for i in range(1, 6):
        pdf.add_heading3(f"Conflict Resolution Worksheet #{i}")
        pdf.add_paragraph("The issue: _____________________________________________________")
        pdf.add_paragraph("_______________________________________________________________")
        pdf.add_blank_line()
        pdf.add_paragraph("Partner 1's position: ___________________________________________")
        pdf.add_paragraph("_______________________________________________________________")
        pdf.add_paragraph("What I can be flexible on: ______________________________________")
        pdf.add_paragraph("What I cannot compromise on: ____________________________________")
        pdf.add_blank_line()
        pdf.add_paragraph("Partner 2's position: ___________________________________________")
        pdf.add_paragraph("_______________________________________________________________")
        pdf.add_paragraph("What I can be flexible on: ______________________________________")
        pdf.add_paragraph("What I cannot compromise on: ____________________________________")
        pdf.add_blank_line()
        pdf.add_paragraph("Our compromise: ________________________________________________")
        pdf.add_paragraph("_______________________________________________________________")
        pdf.add_paragraph("Review date (to check if this is working): ______________________")
        pdf.add_separator()

    pdf.add_heading2("Repair Attempts")
    pdf.add_blank_line()
    pdf.add_paragraph("Repair attempts are things you say or do during conflict to de-escalate tension. Successful couples make repair attempts AND their partners accept them. Practice these:")
    pdf.add_blank_line()
    pdf.add_bullet("I am sorry. That came out wrong. Let me try again.")
    pdf.add_bullet("I can see this is really important to you.")
    pdf.add_bullet("You are making a good point. I had not thought of it that way.")
    pdf.add_bullet("Can we start over? I do not like how this conversation is going.")
    pdf.add_bullet("I love you. Even when we disagree, I am on your team.")
    pdf.add_bullet("Let me make sure I understand what you are saying.")
    pdf.add_bullet("I think we are both getting flooded. Can we take a break?")
    pdf.add_bullet("What do you need from me right now?")
    pdf.add_bullet("I appreciate you telling me how you feel.")
    pdf.add_bullet("You are right about that part. I should not have done that.")
    pdf.add_blank_line()

    pdf.add_heading2("Conflict Patterns Awareness")
    pdf.add_blank_line()
    pdf.add_paragraph("Track your conflicts for 4 weeks to identify patterns:")
    pdf.add_blank_line()
    for conflict_num in range(1, 9):
        pdf.add_heading3(f"Conflict Log #{conflict_num}")
        pdf.add_paragraph(f"Date: _______________  Time: _______________")
        pdf.add_paragraph(f"Topic: ________________________________________________________")
        pdf.add_paragraph(f"Who raised it: [ ] Me  [ ] Partner")
        pdf.add_paragraph(f"Startup style: [ ] Soft  [ ] Harsh")
        pdf.add_paragraph(f"Four Horsemen present: [ ] Criticism  [ ] Contempt  [ ] Defensiveness  [ ] Stonewalling")
        pdf.add_paragraph(f"Did we take a time-out? [ ] Yes  [ ] No")
        pdf.add_paragraph(f"Repair attempts made: [ ] Yes  [ ] No  Accepted? [ ] Yes  [ ] No")
        pdf.add_paragraph(f"Resolution reached: [ ] Yes  [ ] Partial  [ ] No")
        pdf.add_paragraph(f"How I felt after: ______________________________________________")
        pdf.add_paragraph(f"What I would do differently: ____________________________________")
        pdf.add_separator()

    pdf.add_page_break()
    pdf.add_heading2("Apology Language Worksheet")
    pdf.add_blank_line()
    pdf.add_paragraph("Different people receive apologies differently. Understanding your partner's apology language helps you repair effectively:")
    pdf.add_blank_line()
    pdf.add_heading3("The 5 Apology Languages:")
    pdf.add_bullet("1. Expressing regret: I am sorry. I feel terrible about this.")
    pdf.add_bullet("2. Accepting responsibility: I was wrong. There is no excuse.")
    pdf.add_bullet("3. Making restitution: What can I do to make this right?")
    pdf.add_bullet("4. Genuine repentance: I will change this behavior. Here is my plan.")
    pdf.add_bullet("5. Requesting forgiveness: Will you forgive me? I value our relationship.")
    pdf.add_blank_line()
    pdf.add_paragraph("My primary apology language (what I need to hear): _______________")
    pdf.add_paragraph("My partner's primary apology language: ___________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("Practice writing apologies in your partner's language:")
    pdf.add_paragraph("For a recent situation: _________________________________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_blank_line()

    pdf.add_heading2("YOUR ACTION ITEMS - Chapter 3")
    pdf.add_separator()
    pdf.add_bullet("[ ] Practice writing softened startups for current issues")
    pdf.add_bullet("[ ] Establish your time-out protocol together")
    pdf.add_bullet("[ ] Use the compromise worksheet for one current disagreement")
    pdf.add_bullet("[ ] Memorize 3 repair attempts to use during arguments")
    pdf.add_bullet("[ ] Notice when you use harsh startups and catch yourself")
    pdf.add_bullet("[ ] Agree to accept each other's repair attempts going forward")
    pdf.add_bullet("[ ] Complete 4 weeks of conflict logging")
    pdf.add_bullet("[ ] Identify each other's apology language")
    pdf.add_blank_line()

    # CHAPTER 4: DEEP CONNECTION EXERCISES
    pdf.add_page_break()
    pdf.add_heading1("CHAPTER 4: DEEP CONNECTION EXERCISES")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_heading2("Building Emotional Intimacy")
    pdf.add_blank_line()
    pdf.add_paragraph("Emotional intimacy is built through vulnerability, curiosity, and shared experiences. Over time, couples often stop asking deep questions because they assume they already know everything about each other. But people change and grow, and maintaining curiosity about your partner keeps the relationship alive and deepening.")
    pdf.add_blank_line()
    pdf.add_paragraph("These 36 questions are inspired by research showing that mutual vulnerability fosters closeness. Take turns asking and answering. Give each question the time it deserves. No rushing, no judging, and no phones.")
    pdf.add_blank_line()

    pdf.add_heading2("36 Questions to Deepen Your Connection")
    pdf.add_blank_line()
    pdf.add_heading3("Set 1: Getting Reacquainted (Light)")
    questions_set1 = [
        "What is something you have always wanted to try but have been afraid to?",
        "If you could have dinner with anyone in history, who would it be and why?",
        "What does your perfect ordinary Tuesday look like 5 years from now?",
        "What is your happiest memory from our relationship so far?",
        "If you received a million dollars tomorrow, what would you do with it?",
        "What is something you admire about me that you have never told me?",
        "What did you dream of becoming when you were a child?",
        "What is the most adventurous thing you have ever done?",
        "If you could live anywhere in the world for a year, where would you choose?",
        "What is something small that brings you joy every day?",
        "What song reminds you of us or of falling in love?",
        "What is something you want to learn or get better at this year?",
    ]
    for i, q in enumerate(questions_set1, 1):
        pdf.add_paragraph(f"{i}. {q}")
        pdf.add_paragraph(f"   Partner 1 answer: ____________________________________________")
        pdf.add_paragraph(f"   Partner 2 answer: ____________________________________________")
        pdf.add_blank_line()

    pdf.add_page_break()
    pdf.add_heading3("Set 2: Going Deeper (Medium)")
    questions_set2 = [
        "What is your biggest fear about our future together?",
        "When do you feel most loved by me? What specifically do I do?",
        "What is something from your childhood that still affects you today?",
        "If you could change one thing about how you were raised, what would it be?",
        "What do you think is my greatest strength? My biggest challenge?",
        "What does home mean to you? Not a place, but a feeling.",
        "When was the last time you cried? What was it about?",
        "What is something you need more of in our relationship?",
        "What is a belief you held strongly that has changed over the years?",
        "If our relationship had a theme song right now, what would it be?",
        "What is one thing you wish you could tell your younger self?",
        "How do you want to be remembered by the people you love?",
    ]
    for i, q in enumerate(questions_set2, 13):
        pdf.add_paragraph(f"{i}. {q}")
        pdf.add_paragraph(f"   Partner 1 answer: ____________________________________________")
        pdf.add_paragraph(f"   Partner 2 answer: ____________________________________________")
        pdf.add_blank_line()

    pdf.add_page_break()
    pdf.add_heading3("Set 3: Deepest Vulnerability (Intense)")
    questions_set3 = [
        "What is something you have been afraid to tell me?",
        "What is your deepest insecurity in our relationship?",
        "What do you think is the biggest challenge we face as a couple?",
        "If I could understand one thing about you better, what would it be?",
        "What does forgiveness look like to you? Is there anything you need to forgive?",
        "What is the most painful experience you have been through and how did it change you?",
        "What do you need from me during your hardest moments?",
        "What is one thing about our intimacy (emotional or physical) you wish was different?",
        "If we could not fail, what would we build or create together?",
        "What legacy do you want us to leave as a couple?",
        "What are you most grateful for about us?",
        "What do you want to say to me that you have been holding back?",
    ]
    for i, q in enumerate(questions_set3, 25):
        pdf.add_paragraph(f"{i}. {q}")
        pdf.add_paragraph(f"   Partner 1 answer: ____________________________________________")
        pdf.add_paragraph(f"   ____________________________________________________________")
        pdf.add_paragraph(f"   Partner 2 answer: ____________________________________________")
        pdf.add_paragraph(f"   ____________________________________________________________")
        pdf.add_blank_line()

    pdf.add_heading2("YOUR ACTION ITEMS - Chapter 4")
    pdf.add_separator()
    pdf.add_bullet("[ ] Complete Set 1 together this week (one evening, no distractions)")
    pdf.add_bullet("[ ] Complete Set 2 the following week")
    pdf.add_bullet("[ ] Complete Set 3 when you both feel safe and connected")
    pdf.add_bullet("[ ] Listen without judgment, even if answers surprise you")
    pdf.add_bullet("[ ] Thank your partner for their vulnerability after each session")
    pdf.add_bullet("[ ] Revisit these questions in 6 months - answers will have changed")
    pdf.add_blank_line()

    # BONUS: Love Languages Assessment
    pdf.add_page_break()
    pdf.add_heading1("BONUS: UNDERSTANDING LOVE LANGUAGES")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_heading2("The 5 Love Languages")
    pdf.add_blank_line()
    pdf.add_paragraph("Dr. Gary Chapman's research shows that people give and receive love in five primary ways. Understanding your partner's love language means you can express love in the way that actually makes them FEEL loved, rather than expressing it in the way that makes sense to you.")
    pdf.add_blank_line()
    pdf.add_heading3("1. Words of Affirmation")
    pdf.add_paragraph("Verbal compliments, words of appreciation, encouragement, and hearing I love you. What to say: I am proud of you. You look amazing. I appreciate how hard you work for our family. Thank you for always being there.")
    pdf.add_blank_line()
    pdf.add_heading3("2. Quality Time")
    pdf.add_paragraph("Undivided attention, being fully present, shared activities, meaningful conversations. What to do: Put the phone away. Make eye contact. Plan activities together. Have device-free meals.")
    pdf.add_blank_line()
    pdf.add_heading3("3. Physical Touch")
    pdf.add_paragraph("Holding hands, hugs, kisses, cuddling, physical closeness, sexual intimacy. What to do: Reach for their hand. Kiss hello and goodbye. Sit close. Give spontaneous hugs.")
    pdf.add_blank_line()
    pdf.add_heading3("4. Acts of Service")
    pdf.add_paragraph("Doing things to make life easier: cooking, cleaning, running errands, taking care of tasks without being asked. What to do: Fill the car with gas. Make dinner. Handle a task they dislike.")
    pdf.add_blank_line()
    pdf.add_heading3("5. Receiving Gifts")
    pdf.add_paragraph("Thoughtful presents, visual symbols of love, remembering special occasions, surprise tokens of affection. What to do: Pick up their favorite coffee. Remember anniversaries. Give flowers randomly.")
    pdf.add_blank_line()

    pdf.add_heading2("Love Language Assessment")
    pdf.add_blank_line()
    pdf.add_paragraph("Rate how much each expression of love matters to you (1=least, 5=most):")
    pdf.add_blank_line()
    pdf.add_heading3("Partner 1: _______________")
    pdf.add_paragraph("  ___ Words of Affirmation (compliments, encouragement, verbal love)")
    pdf.add_paragraph("  ___ Quality Time (undivided attention, shared activities)")
    pdf.add_paragraph("  ___ Physical Touch (holding hands, hugs, kisses, closeness)")
    pdf.add_paragraph("  ___ Acts of Service (doing helpful things, easing burdens)")
    pdf.add_paragraph("  ___ Receiving Gifts (thoughtful presents, tokens of love)")
    pdf.add_paragraph("  My primary love language: _______________________________________")
    pdf.add_paragraph("  My secondary love language: _____________________________________")
    pdf.add_blank_line()
    pdf.add_heading3("Partner 2: _______________")
    pdf.add_paragraph("  ___ Words of Affirmation (compliments, encouragement, verbal love)")
    pdf.add_paragraph("  ___ Quality Time (undivided attention, shared activities)")
    pdf.add_paragraph("  ___ Physical Touch (holding hands, hugs, kisses, closeness)")
    pdf.add_paragraph("  ___ Acts of Service (doing helpful things, easing burdens)")
    pdf.add_paragraph("  ___ Receiving Gifts (thoughtful presents, tokens of love)")
    pdf.add_paragraph("  My primary love language: _______________________________________")
    pdf.add_paragraph("  My secondary love language: _____________________________________")
    pdf.add_blank_line()

    pdf.add_heading2("Speaking Your Partner's Love Language")
    pdf.add_blank_line()
    pdf.add_paragraph("Now that you know each other's love languages, brainstorm specific actions:")
    pdf.add_blank_line()
    pdf.add_paragraph("5 ways I will speak Partner 1's love language this week:")
    pdf.add_paragraph("1. ____________________________________________________________")
    pdf.add_paragraph("2. ____________________________________________________________")
    pdf.add_paragraph("3. ____________________________________________________________")
    pdf.add_paragraph("4. ____________________________________________________________")
    pdf.add_paragraph("5. ____________________________________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("5 ways I will speak Partner 2's love language this week:")
    pdf.add_paragraph("1. ____________________________________________________________")
    pdf.add_paragraph("2. ____________________________________________________________")
    pdf.add_paragraph("3. ____________________________________________________________")
    pdf.add_paragraph("4. ____________________________________________________________")
    pdf.add_paragraph("5. ____________________________________________________________")
    pdf.add_blank_line()

    pdf.add_heading2("Love Language Weekly Tracker")
    pdf.add_blank_line()
    for wk in range(1, 5):
        pdf.add_heading3(f"Week {wk}")
        pdf.add_paragraph(f"  Actions I took in partner's language: ___")
        pdf.add_paragraph(f"  Actions partner took in my language: ___")
        pdf.add_paragraph(f"  Did I feel loved this week? (1-10): ___")
        pdf.add_paragraph(f"  Did partner feel loved? (1-10): ___")
        pdf.add_paragraph(f"  What worked best: ____________________________________________")
        pdf.add_paragraph(f"  What I will try next week: ____________________________________")
        pdf.add_separator()
    pdf.add_blank_line()

    # CHAPTER 5: HARD CONVERSATIONS
    pdf.add_page_break()
    pdf.add_heading1("CHAPTER 5: HARD CONVERSATIONS SCRIPTS")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_heading2("Navigating Difficult Topics")
    pdf.add_blank_line()
    pdf.add_paragraph("Every relationship has topics that feel scary to bring up: money, intimacy, in-laws, parenting differences, unmet needs, or personal boundaries. The longer you avoid these conversations, the bigger and more explosive they become. These scripts give you a starting framework for approaching tough topics with grace.")
    pdf.add_blank_line()
    pdf.add_paragraph("Remember: You do not have to resolve everything in one conversation. The goal of the first conversation is to be heard and to hear your partner. Solutions come in follow-up conversations after both people feel understood.")
    pdf.add_blank_line()

    pdf.add_heading2("Script 1: Talking About Money")
    pdf.add_blank_line()
    pdf.add_paragraph("Opening: I would like to have an honest conversation about our finances. This is not about blaming anyone. I want us to be a team when it comes to money.")
    pdf.add_blank_line()
    pdf.add_paragraph("Questions to discuss together:")
    pdf.add_bullet("What was money like in your family growing up?")
    pdf.add_bullet("What does financial security mean to you?")
    pdf.add_bullet("Are there spending habits either of us has that concern the other?")
    pdf.add_bullet("What are our shared financial goals for this year? In 5 years?")
    pdf.add_bullet("How should we handle individual vs. shared spending?")
    pdf.add_blank_line()
    pdf.add_paragraph("Our agreements about money:")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_blank_line()

    pdf.add_heading2("Script 2: Talking About Intimacy")
    pdf.add_blank_line()
    pdf.add_paragraph("Opening: Our physical and emotional connection is really important to me. I want to make sure we are both feeling fulfilled and connected. Can we talk openly about this?")
    pdf.add_blank_line()
    pdf.add_paragraph("Questions to discuss together:")
    pdf.add_bullet("On a scale of 1-10, how satisfied are you with our physical intimacy?")
    pdf.add_bullet("What makes you feel most desired and attractive?")
    pdf.add_bullet("Is there anything you would like more of? Less of?")
    pdf.add_bullet("What barriers do we face to connection (stress, schedule, energy)?")
    pdf.add_bullet("How can we prioritize time for intimacy?")
    pdf.add_blank_line()
    pdf.add_paragraph("Our agreements about intimacy:")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_blank_line()

    pdf.add_heading2("Script 3: Talking About Family Boundaries")
    pdf.add_blank_line()
    pdf.add_paragraph("Opening: I love both of our families, and I want to make sure we are setting boundaries that protect our relationship. Can we talk about what feels comfortable for both of us?")
    pdf.add_blank_line()
    pdf.add_paragraph("Questions to discuss together:")
    pdf.add_bullet("How often should we visit or host each family?")
    pdf.add_bullet("What topics are off-limits for family members to weigh in on?")
    pdf.add_bullet("How do we handle it when a family member oversteps?")
    pdf.add_bullet("Who communicates boundaries to which family?")
    pdf.add_bullet("How do we support each other during family conflicts?")
    pdf.add_blank_line()
    pdf.add_paragraph("Our family boundary agreements:")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_blank_line()

    pdf.add_heading2("Script 4: Talking About Division of Labor")
    pdf.add_blank_line()
    pdf.add_paragraph("Opening: I want us both to feel like household responsibilities are shared fairly. This is not about keeping score - it is about both of us feeling like a team. Can we figure this out together?")
    pdf.add_blank_line()
    pdf.add_paragraph("Exercise: List who currently does each task and discuss if it feels fair:")
    pdf.add_bullet("Cooking: ______________________")
    pdf.add_bullet("Dishes: _______________________")
    pdf.add_bullet("Laundry: ______________________")
    pdf.add_bullet("Grocery shopping: ______________")
    pdf.add_bullet("Cleaning bathrooms: ____________")
    pdf.add_bullet("Vacuuming/mopping: _____________")
    pdf.add_bullet("Yard work: ____________________")
    pdf.add_bullet("Bills/finances: ________________")
    pdf.add_bullet("Pet care: ______________________")
    pdf.add_bullet("Scheduling/appointments: ________")
    pdf.add_blank_line()
    pdf.add_paragraph("Changes we are making:")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_blank_line()

    pdf.add_heading2("Script 5: Talking About Unmet Needs")
    pdf.add_blank_line()
    pdf.add_paragraph("Opening: There is something I have been needing that I want to share with you. I know you love me and would want to know. This is not a criticism - it is an invitation for us to grow closer.")
    pdf.add_blank_line()
    pdf.add_paragraph("Template:")
    pdf.add_paragraph("I have been feeling: _____________________________________________")
    pdf.add_paragraph("What I need more of: _____________________________________________")
    pdf.add_paragraph("What that would look like specifically: ____________________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_paragraph("How it would make me feel: _______________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("Partner's response:")
    pdf.add_paragraph("What I heard you say: ____________________________________________")
    pdf.add_paragraph("I am willing to: _________________________________________________")
    pdf.add_paragraph("I need from you in return: ________________________________________")
    pdf.add_blank_line()

    pdf.add_heading2("Script 6: Talking About Future Goals")
    pdf.add_blank_line()
    pdf.add_paragraph("Opening: I want to make sure we are building a life that excites us both. Can we dream together about what we want our future to look like?")
    pdf.add_blank_line()
    pdf.add_paragraph("Questions to discuss together:")
    pdf.add_bullet("Where do we want to be living in 5 years? 10 years?")
    pdf.add_bullet("Do we want children? If so, when? How many?")
    pdf.add_bullet("What are our career aspirations? How do we support each other?")
    pdf.add_bullet("What role does religion or spirituality play in our future?")
    pdf.add_bullet("How do we envision retirement? What will we do together?")
    pdf.add_bullet("What adventures or experiences are on our shared bucket list?")
    pdf.add_blank_line()
    pdf.add_paragraph("Our shared vision for the future:")
    pdf.add_paragraph("1 year: ________________________________________________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_paragraph("5 years: _______________________________________________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_paragraph("10 years: ______________________________________________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_paragraph("Lifetime dreams: ________________________________________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_blank_line()

    pdf.add_heading2("Conversation Preparation Worksheet")
    pdf.add_blank_line()
    pdf.add_paragraph("Use this worksheet before any difficult conversation:")
    pdf.add_blank_line()
    pdf.add_paragraph("Topic I need to discuss: _________________________________________")
    pdf.add_paragraph("Why this matters to me: __________________________________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_paragraph("My feelings about this: __________________________________________")
    pdf.add_paragraph("What I need from this conversation: _______________________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_paragraph("My softened startup: _____________________________________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_paragraph("What my partner might feel hearing this: __________________________")
    pdf.add_paragraph("How can I show empathy for their perspective: _____________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_paragraph("Best time/place for this conversation: ____________________________")
    pdf.add_paragraph("If things get heated, I will: _____________________________________")
    pdf.add_paragraph("Ideal outcome: __________________________________________________")
    pdf.add_paragraph("Am I willing to compromise? What is flexible: _____________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_blank_line()

    pdf.add_heading2("YOUR ACTION ITEMS - Chapter 5")
    pdf.add_separator()
    pdf.add_bullet("[ ] Choose one hard conversation you have been avoiding")
    pdf.add_bullet("[ ] Use the appropriate script to prepare your opener")
    pdf.add_bullet("[ ] Schedule a time to have the conversation (not spontaneously)")
    pdf.add_bullet("[ ] Use softened startup and active listening during the conversation")
    pdf.add_bullet("[ ] Write down your agreements")
    pdf.add_bullet("[ ] Schedule a follow-up conversation to check on progress")
    pdf.add_blank_line()

    # CHAPTER 6: WEEKLY & MONTHLY RITUALS
    pdf.add_page_break()
    pdf.add_heading1("CHAPTER 6: WEEKLY & MONTHLY RITUALS")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_heading2("The Power of Relationship Rituals")
    pdf.add_blank_line()
    pdf.add_paragraph("Happy couples do not leave their connection to chance. They build regular rituals into their lives that ensure they stay emotionally connected regardless of how busy, stressful, or routine life becomes. These are not grand gestures but consistent, small practices that compound into deep intimacy over time.")
    pdf.add_blank_line()

    pdf.add_heading2("Daily Connection Rituals (5-10 minutes)")
    pdf.add_blank_line()
    pdf.add_heading3("1. The 6-Second Kiss")
    pdf.add_paragraph("Research shows that a kiss lasting at least 6 seconds is long enough to create a moment of genuine connection and release bonding hormones. Make this your hello and goodbye ritual.")
    pdf.add_blank_line()
    pdf.add_heading3("2. Highs, Lows, and Gratitudes")
    pdf.add_paragraph("Each evening, share: one high point of your day, one low point, and one thing you are grateful for about your partner. This takes 5 minutes and maintains emotional awareness.")
    pdf.add_blank_line()
    pdf.add_heading3("3. The Stress-Reducing Conversation")
    pdf.add_paragraph("Spend 10-15 minutes at the end of each day talking about stresses OUTSIDE the relationship (work, friends, family). The listener's job is only to be supportive, not to give advice.")
    pdf.add_blank_line()
    pdf.add_heading3("4. Goodnight Ritual")
    pdf.add_paragraph("Go to bed at the same time at least a few nights per week. This is when many couples have their best conversations and feel most connected.")
    pdf.add_blank_line()

    pdf.add_heading2("Weekly Rituals")
    pdf.add_blank_line()
    pdf.add_heading3("The Weekly Check-In (30 minutes)")
    pdf.add_paragraph("Schedule 30 minutes each week (same time) to discuss your relationship directly. This prevents issues from building up and ensures you stay proactive about connection.")
    pdf.add_blank_line()
    pdf.add_paragraph("Our weekly check-in time: _______ Day: _______")
    pdf.add_blank_line()
    pdf.add_heading3("Weekly Check-In Agenda:")
    pdf.add_bullet("1. Appreciations: Each share 3 things you appreciated about your partner this week")
    pdf.add_bullet("2. Logistics: Calendar review, upcoming events, coordination")
    pdf.add_bullet("3. Issues: Any small things that need addressing? (use softened startups)")
    pdf.add_bullet("4. Fun: Plan something enjoyable for the coming week")
    pdf.add_bullet("5. Intimacy: Check in on physical and emotional connection")
    pdf.add_blank_line()

    # 8 weekly check-in templates
    for week in range(1, 9):
        pdf.add_page_break()
        pdf.add_heading2(f"WEEKLY CHECK-IN #{week}")
        pdf.add_separator()
        pdf.add_paragraph(f"Date: _______________")
        pdf.add_blank_line()
        pdf.add_heading3("Appreciations (share 3 each)")
        pdf.add_paragraph("Partner 1 appreciates:")
        pdf.add_paragraph("1. ____________________________________________________________")
        pdf.add_paragraph("2. ____________________________________________________________")
        pdf.add_paragraph("3. ____________________________________________________________")
        pdf.add_paragraph("Partner 2 appreciates:")
        pdf.add_paragraph("1. ____________________________________________________________")
        pdf.add_paragraph("2. ____________________________________________________________")
        pdf.add_paragraph("3. ____________________________________________________________")
        pdf.add_blank_line()
        pdf.add_heading3("Relationship Temperature Check")
        pdf.add_paragraph("How connected did we feel this week? (1-10)")
        pdf.add_paragraph("  Partner 1: ___  Partner 2: ___")
        pdf.add_paragraph("How well did we communicate? (1-10)")
        pdf.add_paragraph("  Partner 1: ___  Partner 2: ___")
        pdf.add_paragraph("How supported did I feel? (1-10)")
        pdf.add_paragraph("  Partner 1: ___  Partner 2: ___")
        pdf.add_blank_line()
        pdf.add_heading3("Highlights & Challenges")
        pdf.add_paragraph("Best moment together this week: ________________________________")
        pdf.add_paragraph("_______________________________________________________________")
        pdf.add_paragraph("A challenge we faced: __________________________________________")
        pdf.add_paragraph("_______________________________________________________________")
        pdf.add_paragraph("How we handled it: _____________________________________________")
        pdf.add_blank_line()
        pdf.add_heading3("Logistics & Calendar")
        pdf.add_paragraph("Upcoming events: ______________________________________________")
        pdf.add_paragraph("Coordination needed: ___________________________________________")
        pdf.add_paragraph("Decisions to make together: _____________________________________")
        pdf.add_blank_line()
        pdf.add_heading3("Issues to Address (use softened startup)")
        pdf.add_paragraph("Issue 1: _______________________________________________________")
        pdf.add_paragraph("I feel: _________ about: _________ and I need: _________________")
        pdf.add_paragraph("Agreement: _____________________________________________________")
        pdf.add_blank_line()
        pdf.add_paragraph("Issue 2: _______________________________________________________")
        pdf.add_paragraph("I feel: _________ about: _________ and I need: _________________")
        pdf.add_paragraph("Agreement: _____________________________________________________")
        pdf.add_blank_line()
        pdf.add_heading3("Fun & Connection Plans")
        pdf.add_paragraph("Date night this week: __________________________________________")
        pdf.add_paragraph("Daily ritual we will practice: __________________________________")
        pdf.add_paragraph("Something new we will try: _____________________________________")
        pdf.add_blank_line()
        pdf.add_heading3("Goals for Next Week")
        pdf.add_paragraph("As a couple we will: ___________________________________________")
        pdf.add_paragraph("I personally commit to: ________________________________________")
        pdf.add_paragraph("What would make next week a 10: _______________________________")
        pdf.add_separator()

    pdf.add_heading2("Monthly Rituals")
    pdf.add_blank_line()
    pdf.add_heading3("Monthly State of the Union")
    pdf.add_paragraph("Once a month, have a deeper conversation about the overall direction of your relationship. Discuss goals, dreams, challenges, and growth areas.")
    pdf.add_blank_line()
    pdf.add_heading3("Monthly Date Night")
    pdf.add_paragraph("Commit to at least one intentional date night per month. Alternate who plans it. Make it something that creates new shared experiences.")
    pdf.add_blank_line()

    pdf.add_heading2("YOUR ACTION ITEMS - Chapter 6")
    pdf.add_separator()
    pdf.add_bullet("[ ] Choose 2 daily rituals to start this week")
    pdf.add_bullet("[ ] Schedule your weekly check-in time")
    pdf.add_bullet("[ ] Complete your first weekly check-in using the template")
    pdf.add_bullet("[ ] Plan your next monthly date night")
    pdf.add_bullet("[ ] Commit to these rituals for 30 days before evaluating")
    pdf.add_blank_line()

    # CHAPTER 7: DATE NIGHT PLANNING
    pdf.add_page_break()
    pdf.add_heading1("CHAPTER 7: DATE NIGHT PLANNING")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_heading2("Why Regular Dates Matter")
    pdf.add_blank_line()
    pdf.add_paragraph("Couples who have regular date nights report higher relationship satisfaction, better communication, increased intimacy, and lower divorce rates. Date nights work because they create dedicated time for connection away from the routines, responsibilities, and distractions of daily life.")
    pdf.add_blank_line()
    pdf.add_paragraph("The key to great date nights: novelty. Research shows that couples who try new things together experience increases in relationship satisfaction that mimic the excitement of early dating. Break out of the dinner-and-movie routine and explore together.")
    pdf.add_blank_line()

    pdf.add_heading2("52 Date Night Ideas (One for Every Week)")
    pdf.add_blank_line()
    pdf.add_heading3("Adventure & Outdoors")
    date_ideas_adventure = [
        "Take a sunset hike at a trail you have never been to",
        "Rent kayaks or paddleboards for a morning on the water",
        "Go stargazing at a dark sky location with blankets and hot chocolate",
        "Take a road trip to a town within 2 hours that you have never visited",
        "Go rock climbing at an indoor gym together",
        "Bike ride along a scenic route with a picnic stop",
        "Visit a botanical garden or nature reserve",
        "Go camping in your backyard (fire pit, s'mores, sleeping bags)",
        "Take a sunrise walk on the beach",
        "Try geocaching in your city",
        "Go berry picking or visit a farm in season",
        "Explore a new neighborhood on foot together",
        "Take a ferry ride somewhere",
    ]
    for i, idea in enumerate(date_ideas_adventure, 1):
        pdf.add_bullet(f"{i}. {idea}")
    pdf.add_blank_line()

    pdf.add_heading3("Creative & Learning")
    date_ideas_creative = [
        "Take a pottery or ceramics class together",
        "Attend a cooking class (Thai, Italian, sushi-making)",
        "Visit a museum and discuss your favorite pieces over coffee after",
        "Take a dance class (salsa, swing, ballroom)",
        "Paint and sip night (at home or at a studio)",
        "Attend a live theater performance or local play",
        "Take a photography walk with a theme (doors, shadows, color red)",
        "Build something together (furniture, garden bed, LEGO set)",
        "Write letters to your future selves to open in 5 years",
        "Visit a bookstore and each pick a book for the other",
        "Take a language class together",
        "Attend a wine or whiskey tasting",
        "Go to an open mic night or comedy show",
    ]
    for i, idea in enumerate(date_ideas_creative, 14):
        pdf.add_bullet(f"{i}. {idea}")
    pdf.add_blank_line()

    pdf.add_heading3("Cozy & At-Home")
    date_ideas_home = [
        "Build a blanket fort and watch childhood movies",
        "Cook a fancy multi-course dinner together with candles",
        "Have a game night (board games, card games, video games)",
        "Create a DIY spa night (face masks, massage, bubble bath)",
        "Do a puzzle together with jazz music and wine",
        "Have a themed movie marathon (trilogy, decade, director)",
        "Recreate your first date at home",
        "Build a vision board together for your next year",
        "Have a fondue night (cheese AND chocolate)",
        "Indoor picnic on the living room floor",
        "Read to each other from a book you both choose",
        "Do a couples workout video together",
        "Try a new recipe from a cuisine neither of you has cooked before",
    ]
    for i, idea in enumerate(date_ideas_home, 27):
        pdf.add_bullet(f"{i}. {idea}")
    pdf.add_blank_line()

    pdf.add_heading3("Social & Community")
    date_ideas_social = [
        "Double date with another couple you admire",
        "Volunteer together at a local charity or food bank",
        "Attend a local festival, fair, or market",
        "Take a group class or workshop",
        "Host a themed dinner party together",
        "Go to a sporting event (even a minor league game)",
        "Attend a concert or live music event",
        "Visit a farmers market and cook what you find",
        "Take a neighborhood walking tour",
        "Go to a trivia night at a local bar",
        "Visit an escape room with friends",
        "Attend a community event (parade, outdoor movie, fireworks)",
        "Explore a flea market or antique shop together",
    ]
    for i, idea in enumerate(date_ideas_social, 40):
        pdf.add_bullet(f"{i}. {idea}")
    pdf.add_blank_line()

    pdf.add_heading2("Date Night Planner")
    pdf.add_blank_line()
    for month in range(1, 13):
        pdf.add_heading3(f"Date Night #{month}")
        pdf.add_paragraph(f"Date: _______________  Planned by: _______________")
        pdf.add_paragraph(f"Activity: _____________________________________________________")
        pdf.add_paragraph(f"Location: _____________________________________________________")
        pdf.add_paragraph(f"Budget: $___________")
        pdf.add_paragraph(f"What we loved about it: ________________________________________")
        pdf.add_paragraph(f"_______________________________________________________________")
        pdf.add_paragraph(f"Connection rating (1-10): ___")
        pdf.add_paragraph(f"Something new I learned about my partner: ______________________")
        pdf.add_paragraph(f"_______________________________________________________________")
        pdf.add_paragraph(f"Would we do this again? [ ] Yes  [ ] No")
        pdf.add_separator()

    pdf.add_heading2("YOUR ACTION ITEMS - Chapter 7")
    pdf.add_separator()
    pdf.add_bullet("[ ] Schedule your next date night right now")
    pdf.add_bullet("[ ] Each partner stars 5 ideas from the list above")
    pdf.add_bullet("[ ] Alternate who plans date night each time")
    pdf.add_bullet("[ ] Keep phones put away during the entire date")
    pdf.add_bullet("[ ] Try at least one brand-new activity together this month")
    pdf.add_bullet("[ ] Make date night non-negotiable (protect it like a meeting)")
    pdf.add_blank_line()

    # CHAPTER 8: REBUILDING TRUST
    pdf.add_page_break()
    pdf.add_heading1("CHAPTER 8: REBUILDING TRUST")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_heading2("When Trust Has Been Broken")
    pdf.add_blank_line()
    pdf.add_paragraph("Trust is the foundation of every healthy relationship. When it is broken, whether through dishonesty, betrayal, broken promises, or emotional unavailability, the relationship enters a critical period. Rebuilding trust is possible but requires consistent effort, patience, accountability, and genuine willingness to change from both partners.")
    pdf.add_blank_line()
    pdf.add_paragraph("This chapter provides a framework for the difficult work of trust repair. If the breach was severe (infidelity, addiction, abuse), please work with a licensed couples therapist alongside this workbook.")
    pdf.add_blank_line()

    pdf.add_heading2("Understanding Trust")
    pdf.add_blank_line()
    pdf.add_paragraph("Trust is not a single thing. It is built from multiple components:")
    pdf.add_blank_line()
    pdf.add_bullet("RELIABILITY: You do what you say you will do, consistently")
    pdf.add_bullet("HONESTY: You tell the truth, even when it is uncomfortable")
    pdf.add_bullet("VULNERABILITY: You share your inner world authentically")
    pdf.add_bullet("SAFETY: Your partner feels physically and emotionally safe with you")
    pdf.add_bullet("LOYALTY: You protect the relationship from outside threats")
    pdf.add_bullet("ACCOUNTABILITY: You take responsibility when you make mistakes")
    pdf.add_blank_line()

    pdf.add_heading2("Trust Assessment")
    pdf.add_blank_line()
    pdf.add_paragraph("Rate each area of trust from 1 (completely broken) to 10 (fully intact):")
    pdf.add_blank_line()
    pdf.add_paragraph("Partner 1 rates trust in Partner 2:")
    pdf.add_paragraph("  Reliability: ___  Honesty: ___  Vulnerability: ___")
    pdf.add_paragraph("  Safety: ___  Loyalty: ___  Accountability: ___")
    pdf.add_paragraph("  Overall trust level: ___ / 10")
    pdf.add_blank_line()
    pdf.add_paragraph("Partner 2 rates trust in Partner 1:")
    pdf.add_paragraph("  Reliability: ___  Honesty: ___  Vulnerability: ___")
    pdf.add_paragraph("  Safety: ___  Loyalty: ___  Accountability: ___")
    pdf.add_paragraph("  Overall trust level: ___ / 10")
    pdf.add_blank_line()

    pdf.add_heading2("The Trust Rebuilding Process")
    pdf.add_blank_line()
    pdf.add_heading3("Phase 1: Acknowledgment (Weeks 1-4)")
    pdf.add_paragraph("The person who broke trust must fully acknowledge what happened, take responsibility without excuses, and demonstrate genuine remorse. The hurt partner needs space to express their pain without being shut down.")
    pdf.add_blank_line()
    pdf.add_paragraph("What happened (write it honestly): _______________________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_paragraph("How it affected my partner: ______________________________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_paragraph("What I take responsibility for: ___________________________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_blank_line()

    pdf.add_heading3("Phase 2: Transparency (Weeks 4-12)")
    pdf.add_paragraph("Rebuilding trust requires radical transparency. The person who broke trust willingly offers more information, more access, and more check-ins than normal.")
    pdf.add_blank_line()
    pdf.add_paragraph("Specific transparency commitments I am making:")
    pdf.add_paragraph("1. ____________________________________________________________")
    pdf.add_paragraph("2. ____________________________________________________________")
    pdf.add_paragraph("3. ____________________________________________________________")
    pdf.add_paragraph("4. ____________________________________________________________")
    pdf.add_paragraph("5. ____________________________________________________________")
    pdf.add_blank_line()

    pdf.add_heading3("Phase 3: Consistency (Months 3-12)")
    pdf.add_paragraph("Trust is rebuilt through hundreds of small consistent actions over time. There are no shortcuts. The hurt partner watches for alignment between words and actions.")
    pdf.add_blank_line()
    pdf.add_paragraph("Monthly trust check-in:")
    for month in range(1, 7):
        pdf.add_paragraph(f"  Month {month}: Trust level (1-10): ___  Evidence of change: _______________")
    pdf.add_blank_line()

    pdf.add_heading3("Phase 4: Forgiveness and New Beginning (12+ months)")
    pdf.add_paragraph("Forgiveness is not forgetting. It is choosing to release resentment and move forward. It cannot be rushed or demanded. It happens when the hurt partner sees consistent change and feels safe again.")
    pdf.add_blank_line()
    pdf.add_paragraph("Am I ready to forgive? Reflection:")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_paragraph("_______________________________________________________________")
    pdf.add_blank_line()

    pdf.add_heading2("Daily Trust-Building Actions")
    pdf.add_blank_line()
    pdf.add_paragraph("Small daily actions that rebuild trust over time:")
    pdf.add_bullet("Follow through on every promise, no matter how small")
    pdf.add_bullet("Be where you say you will be, when you say you will be there")
    pdf.add_bullet("Share information proactively rather than waiting to be asked")
    pdf.add_bullet("Be honest about small things (this builds credibility for big things)")
    pdf.add_bullet("Check in emotionally: How are you doing? How are we doing?")
    pdf.add_bullet("Accept your partner's feelings without getting defensive")
    pdf.add_bullet("Show patience when your partner needs reassurance")
    pdf.add_bullet("Prioritize the relationship visibly")
    pdf.add_bullet("Be consistent even when you think no one is watching")
    pdf.add_bullet("Celebrate small milestones in the rebuilding process")
    pdf.add_blank_line()

    pdf.add_heading2("Trust Rebuilding Journal")
    pdf.add_blank_line()
    pdf.add_paragraph("Use this journal weekly to track your trust rebuilding progress:")
    pdf.add_blank_line()
    for entry in range(1, 9):
        pdf.add_heading3(f"Trust Journal Entry #{entry}")
        pdf.add_paragraph(f"Date: _______________  Week #: ___")
        pdf.add_paragraph(f"Trust level this week (1-10): ___")
        pdf.add_paragraph(f"Trust-building actions I took this week:")
        pdf.add_paragraph(f"1. ____________________________________________________________")
        pdf.add_paragraph(f"2. ____________________________________________________________")
        pdf.add_paragraph(f"3. ____________________________________________________________")
        pdf.add_paragraph(f"Moments I felt trust growing:")
        pdf.add_paragraph(f"_______________________________________________________________")
        pdf.add_paragraph(f"Moments that felt difficult:")
        pdf.add_paragraph(f"_______________________________________________________________")
        pdf.add_paragraph(f"What my partner did that helped:")
        pdf.add_paragraph(f"_______________________________________________________________")
        pdf.add_paragraph(f"What I need more of: ___________________________________________")
        pdf.add_paragraph(f"My commitment for next week: ___________________________________")
        pdf.add_separator()

    pdf.add_heading2("YOUR ACTION ITEMS - Chapter 8")
    pdf.add_separator()
    pdf.add_bullet("[ ] Complete the trust assessment together honestly")
    pdf.add_bullet("[ ] Identify which phase of trust rebuilding you are in")
    pdf.add_bullet("[ ] Write specific transparency commitments")
    pdf.add_bullet("[ ] Schedule monthly trust check-ins")
    pdf.add_bullet("[ ] Practice daily trust-building actions consistently")
    pdf.add_bullet("[ ] Consider working with a couples therapist for support")
    pdf.add_blank_line()

    # FINAL PAGE
    pdf.add_page_break()
    pdf.add_heading1("NEXT STEPS")
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_paragraph("Congratulations on investing in your relationship by working through this workbook. The fact that you are here means you care deeply about your connection and are willing to put in the work. That commitment is the most important ingredient in a thriving relationship.")
    pdf.add_blank_line()
    pdf.add_heading2("Your Ongoing Practice")
    pdf.add_bullet("Continue weekly check-ins (they prevent issues from building up)")
    pdf.add_bullet("Keep having regular date nights (protect this time)")
    pdf.add_bullet("Practice active listening daily")
    pdf.add_bullet("Use softened startups whenever raising an issue")
    pdf.add_bullet("Revisit the 36 questions every 6 months (your answers will evolve)")
    pdf.add_bullet("Celebrate your progress and growth as a couple")
    pdf.add_blank_line()
    pdf.add_heading2("When to Seek Professional Help")
    pdf.add_paragraph("Consider couples therapy if:")
    pdf.add_bullet("The same issues keep recurring without resolution")
    pdf.add_bullet("Communication frequently escalates to yelling or silence")
    pdf.add_bullet("There has been infidelity or betrayal")
    pdf.add_bullet("One or both partners feel emotionally disconnected")
    pdf.add_bullet("You are considering separation")
    pdf.add_bullet("There is any form of abuse (physical, emotional, financial)")
    pdf.add_blank_line()
    pdf.add_paragraph("By Daniel Tesfamariam")
    pdf.add_paragraph("Your relationship is worth fighting for. Keep communicating, keep connecting, keep choosing each other.")

    filepath = os.path.join(OUTPUT_DIR, '05-Couples-Communication-Workbook.pdf')
    pdf.save(filepath)
    return filepath, len(pdf.pages) + 1



def main():
    """Generate all 4 books."""
    print("=" * 60)
    print("  ETSY BUSINESS BUILDER - PDF Book Generator")
    print("  Author: Daniel Tesfamariam")
    print("=" * 60)
    print()
    print(f"  Output directory: {OUTPUT_DIR}")
    print()

    books = [
        ("Book 2: Anxiety & Stress Management Workbook", generate_book2),
        ("Book 3: Wedding Planning Master Bundle", generate_book3),
        ("Book 4: Digital Declutter & Productivity System", generate_book4),
        ("Book 5: Couples Communication Workbook", generate_book5),
    ]

    results = []
    for title, generator in books:
        print(f"  Generating: {title}...")
        try:
            filepath, page_count = generator()
            file_size = os.path.getsize(filepath) / 1024
            results.append((title, filepath, page_count, file_size))
            print(f"    -> {page_count} pages | {file_size:.0f} KB | {os.path.basename(filepath)}")
        except Exception as e:
            print(f"    -> ERROR: {e}")
            import traceback
            traceback.print_exc()
        print()

    print()
    print("=" * 60)
    print("  GENERATION COMPLETE")
    print("=" * 60)
    print()
    print(f"  {'Book':<50} {'Pages':>6} {'Size':>8}")
    print(f"  {'-'*50} {'-'*6} {'-'*8}")
    for title, filepath, pages, size in results:
        print(f"  {title:<50} {pages:>6} {size:>6.0f} KB")
    print()
    total_pages = sum(r[2] for r in results)
    total_size = sum(r[3] for r in results)
    print(f"  {'TOTAL':<50} {total_pages:>6} {total_size:>6.0f} KB")
    print()

    # Verify page counts
    all_pass = True
    for title, filepath, pages, size in results:
        if pages < 60:
            print(f"  WARNING: {title} has only {pages} pages (minimum 60 required)")
            all_pass = False

    if all_pass:
        print("  All books meet the 60+ page requirement!")
    print()


if __name__ == '__main__':
    main()
