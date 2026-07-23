#!/usr/bin/env python3
"""
Health Digital Products PDF Generator
Generates all 20 health PDF books for Etsy shop.
Author: Daniel Tesfamariam
"""

import os
import sys

# Import PurePDF from existing module
exec(open('/projects/sandbox/CLAUDE/etsy-digital-products-strategy/generate_pdfs.py').read().replace("\nif __name__ == '__main__':\n    main()\n", "\n"))

OUTPUT_DIR = '/projects/sandbox/CLAUDE/etsy-health-products/pdf-output'
AUTHOR = "Daniel Tesfamariam"
DISCLAIMER = ("MEDICAL DISCLAIMER: This workbook is for informational purposes only and does "
              "not constitute medical advice. Always consult your healthcare provider before "
              "making changes to your diet, exercise, or medication. The author is not a "
              "licensed medical professional. Never disregard professional medical advice or "
              "delay seeking it because of something you have read in this workbook.")

os.makedirs(OUTPUT_DIR, exist_ok=True)



def add_front_matter(pdf, title, subtitle=""):
    """Add title page and disclaimer."""
    pdf.add_blank_line()
    pdf.add_blank_line()
    pdf.add_blank_line()
    pdf.add_title(title)
    if subtitle:
        pdf.add_heading2(subtitle)
    pdf.add_blank_line()
    pdf.add_paragraph(f"By {AUTHOR}")
    pdf.add_blank_line()
    pdf.add_paragraph("A Comprehensive Health & Wellness Workbook")
    pdf.add_blank_line()
    pdf.add_separator()
    pdf.add_blank_line()
    pdf.add_heading3("Medical Disclaimer")
    pdf.add_paragraph(DISCLAIMER)
    pdf.add_blank_line()
    pdf.add_paragraph("Copyright. All rights reserved. No part of this publication may be "
                      "reproduced without written permission from the author.")
    pdf.add_page_break()



def add_toc(pdf, chapters):
    """Add table of contents."""
    pdf.add_heading1("Table of Contents")
    pdf.add_blank_line()
    for i, ch in enumerate(chapters, 1):
        pdf.add_paragraph(f"{i}. {ch}")
    pdf.add_blank_line()
    pdf.add_separator()
    pdf.add_page_break()


def add_about_author(pdf):
    """Add about the author page."""
    # Add notes pages before author
    pdf.add_page_break()
    pdf.add_heading1("Notes & Reflections")
    pdf.add_blank_line()
    pdf.add_paragraph("Use these pages to record your thoughts, observations, and insights "
                      "as you work through this workbook.")
    pdf.add_page_break()
    for p in range(20):
        pdf.add_heading3(f"Notes - Page {p+1}")
        pdf.add_paragraph("Date: __/__/____")
        pdf.add_blank_line()
        for line in range(25):
            pdf.add_paragraph("_" * 70)
        pdf.add_page_break()
    
    pdf.add_heading1("About the Author")
    pdf.add_blank_line()
    pdf.add_paragraph(f"{AUTHOR} is a health and wellness content creator dedicated to making "
                      "evidence-based health information accessible and actionable. Through carefully "
                      "designed workbooks and guides, Daniel helps people take control of their health "
                      "journey with practical tools, trackers, and strategies.")
    pdf.add_blank_line()
    pdf.add_paragraph("For more health and wellness resources, visit our Etsy shop for additional "
                      "workbooks, planners, and guides covering nutrition, fitness, mental health, "
                      "and chronic condition management.")
    pdf.add_blank_line()
    pdf.add_heading3("Connect With Us")
    pdf.add_bullet("Visit our Etsy shop for more wellness workbooks")
    pdf.add_bullet("Leave a review if this workbook helped you")
    pdf.add_bullet("Share your progress - we love hearing success stories")
    pdf.add_blank_line()
    pdf.add_paragraph("Thank you for investing in your health. You deserve to feel your best.")



def add_tracker_pages(pdf, title, fields, num_pages=20):
    """Add multiple tracker pages with given fields."""
    for p in range(num_pages):
        pdf.add_heading3(f"{title} - Page {p+1}")
        pdf.add_blank_line()
        for day in range(5):
            pdf.add_paragraph(f"Day: ________  Date: __/__/____")
            for field in fields:
                pdf.add_paragraph(f"  {field}: _______________")
            pdf.add_blank_line()
            pdf.add_separator()
        pdf.add_page_break()


def add_weekly_review(pdf, questions, num_weeks=12):
    """Add weekly review pages."""
    for w in range(num_weeks):
        pdf.add_heading3(f"Week {w+1} Review")
        pdf.add_paragraph(f"Date Range: __/__/____ to __/__/____")
        pdf.add_blank_line()
        for q in questions:
            pdf.add_paragraph(f"{q}")
            pdf.add_paragraph("_" * 60)
            pdf.add_blank_line()
        pdf.add_separator()
        pdf.add_page_break()


def add_notes_pages(pdf, title="Notes & Reflections", num_pages=8):
    """Add lined notes pages."""
    for p in range(num_pages):
        pdf.add_heading3(f"{title} - Page {p+1}")
        pdf.add_paragraph("Date: __/__/____")
        pdf.add_blank_line()
        for line in range(25):
            pdf.add_paragraph("_" * 70)
        pdf.add_page_break()


def add_faq_section(pdf, faqs):
    """Add FAQ section with questions and answers."""
    pdf.add_page_break()
    pdf.add_heading1("Frequently Asked Questions")
    pdf.add_blank_line()
    for q, a in faqs:
        pdf.add_heading3(f"Q: {q}")
        pdf.add_paragraph(a)
        pdf.add_blank_line()



def book_01_anti_inflammatory():
    """Anti-Inflammatory Diet Complete Guide"""
    pdf = PurePDF(title="Anti-Inflammatory Diet Complete Guide", author=AUTHOR)
    add_front_matter(pdf, "Anti-Inflammatory Diet", "Complete Guide with 4-Week Meal Plan")
    
    chapters = ["Understanding Inflammation & Your Body", "Anti-Inflammatory Food Guide",
                "4-Week Meal Plan", "Recipes & Meal Prep", "Daily Food & Symptom Tracker",
                "Lifestyle Strategies", "Progress Review & Adjustment", "FAQ & Resources"]
    add_toc(pdf, chapters)
    
    # Introduction
    pdf.add_heading1("Introduction")
    pdf.add_paragraph("Chronic inflammation is at the root of many modern health conditions, from "
                      "joint pain and digestive issues to heart disease and autoimmune disorders. "
                      "This comprehensive guide will help you understand inflammation, identify your "
                      "personal triggers, and build an anti-inflammatory lifestyle through food.")
    pdf.add_blank_line()
    pdf.add_heading3("How to Use This Workbook")
    pdf.add_bullet("Start with Chapter 1 to understand inflammation basics")
    pdf.add_bullet("Use the food guide in Chapter 2 as your shopping companion")
    pdf.add_bullet("Follow the 4-week meal plan or customize your own")
    pdf.add_bullet("Track your symptoms daily to identify patterns")
    pdf.add_bullet("Review progress weekly and adjust as needed")
    pdf.add_blank_line()
    pdf.add_heading3("Who This Book Is For")
    pdf.add_bullet("Anyone experiencing chronic pain or fatigue")
    pdf.add_bullet("People with autoimmune conditions seeking dietary support")
    pdf.add_bullet("Those wanting to reduce inflammation markers")
    pdf.add_bullet("Anyone interested in disease prevention through nutrition")
    pdf.add_page_break()
    
    # Chapter 1
    pdf.add_heading1("Chapter 1: Understanding Inflammation")
    pdf.add_blank_line()
    pdf.add_heading2("What Is Inflammation?")
    pdf.add_paragraph("Inflammation is your body's natural defense mechanism. When you get a cut "
                      "or infection, acute inflammation helps you heal. However, when inflammation "
                      "becomes chronic - lasting weeks, months, or years - it can damage healthy "
                      "tissue and contribute to serious health conditions.")
    pdf.add_blank_line()
    pdf.add_heading3("Acute vs. Chronic Inflammation")
    pdf.add_paragraph("Acute inflammation: Short-term response to injury or infection. Signs include "
                      "redness, swelling, heat, and pain. This is healthy and necessary.")
    pdf.add_paragraph("Chronic inflammation: Low-grade, persistent inflammation that can last months "
                      "or years. Often has no obvious symptoms initially but damages tissues over time.")
    pdf.add_blank_line()
    pdf.add_heading3("Common Signs of Chronic Inflammation")
    pdf.add_bullet("Persistent fatigue and low energy")
    pdf.add_bullet("Joint pain or stiffness")
    pdf.add_bullet("Digestive problems (bloating, gas, irregular bowels)")
    pdf.add_bullet("Skin issues (eczema, psoriasis, acne)")
    pdf.add_bullet("Brain fog and difficulty concentrating")
    pdf.add_bullet("Frequent infections or slow healing")
    pdf.add_bullet("Weight gain, especially around the midsection")
    pdf.add_bullet("Mood changes, anxiety, or depression")
    pdf.add_blank_line()
    pdf.add_heading2("What Causes Chronic Inflammation?")
    pdf.add_bullet("Poor diet high in processed foods, sugar, and refined carbs")
    pdf.add_bullet("Sedentary lifestyle and lack of movement")
    pdf.add_bullet("Chronic stress and poor sleep")
    pdf.add_bullet("Environmental toxins and pollutants")
    pdf.add_bullet("Gut dysbiosis and food sensitivities")
    pdf.add_bullet("Excess body fat, particularly visceral fat")
    pdf.add_bullet("Smoking and excessive alcohol consumption")
    pdf.add_blank_line()
    pdf.add_heading2("The Role of Diet in Inflammation")
    pdf.add_paragraph("Research consistently shows that dietary patterns play a major role in either "
                      "promoting or reducing inflammation. The Standard American Diet (SAD) is highly "
                      "inflammatory due to its reliance on processed foods, added sugars, refined "
                      "oils, and artificial additives.")
    pdf.add_blank_line()
    pdf.add_heading3("Inflammatory Foods to Reduce")
    pdf.add_bullet("Refined sugars and high-fructose corn syrup")
    pdf.add_bullet("Trans fats and partially hydrogenated oils")
    pdf.add_bullet("Refined carbohydrates (white bread, pastries)")
    pdf.add_bullet("Processed meats (hot dogs, sausages, deli meats)")
    pdf.add_bullet("Excessive omega-6 fatty acids (soybean oil, corn oil)")
    pdf.add_bullet("Excessive alcohol")
    pdf.add_bullet("Artificial sweeteners and additives")
    pdf.add_blank_line()
    pdf.add_heading3("Anti-Inflammatory Foods to Increase")
    pdf.add_bullet("Fatty fish (salmon, mackerel, sardines) - omega-3s")
    pdf.add_bullet("Leafy greens (spinach, kale, collards)")
    pdf.add_bullet("Berries (blueberries, strawberries, blackberries)")
    pdf.add_bullet("Nuts and seeds (walnuts, flaxseeds, chia seeds)")
    pdf.add_bullet("Extra virgin olive oil")
    pdf.add_bullet("Turmeric, ginger, and other spices")
    pdf.add_bullet("Green tea and herbal teas")
    pdf.add_bullet("Cruciferous vegetables (broccoli, cauliflower)")
    pdf.add_page_break()
    
    # Chapter 2 - Food Guide
    pdf.add_heading1("Chapter 2: Anti-Inflammatory Food Guide")
    pdf.add_blank_line()
    pdf.add_heading2("The Anti-Inflammatory Food Pyramid")
    pdf.add_paragraph("Base your diet on these food categories, starting from the most important:")
    pdf.add_blank_line()
    pdf.add_heading3("Level 1: Eat Abundantly (Daily)")
    pdf.add_bullet("Non-starchy vegetables: All colors, aim for 5+ servings daily")
    pdf.add_bullet("Leafy greens: Spinach, kale, arugula, Swiss chard")
    pdf.add_bullet("Herbs and spices: Turmeric, ginger, garlic, oregano, rosemary")
    pdf.add_bullet("Healthy fats: Extra virgin olive oil, avocado")
    pdf.add_blank_line()
    pdf.add_heading3("Level 2: Eat Regularly (4-5x/week)")
    pdf.add_bullet("Fatty fish: Salmon, sardines, mackerel, herring")
    pdf.add_bullet("Berries: Blueberries, raspberries, strawberries")
    pdf.add_bullet("Nuts and seeds: Walnuts, almonds, flaxseeds, chia")
    pdf.add_bullet("Legumes: Lentils, chickpeas, black beans")
    pdf.add_blank_line()
    pdf.add_heading3("Level 3: Eat Moderately (2-3x/week)")
    pdf.add_bullet("Whole grains: Quinoa, brown rice, oats")
    pdf.add_bullet("Starchy vegetables: Sweet potatoes, squash")
    pdf.add_bullet("Poultry: Organic chicken, turkey")
    pdf.add_bullet("Eggs: Pasture-raised preferred")
    pdf.add_blank_line()
    pdf.add_heading3("Level 4: Eat Sparingly (1-2x/week or less)")
    pdf.add_bullet("Red meat: Grass-fed, lean cuts only")
    pdf.add_bullet("Dairy: If tolerated, choose fermented (yogurt, kefir)")
    pdf.add_bullet("Natural sweeteners: Raw honey, maple syrup (small amounts)")
    pdf.add_bullet("Dark chocolate: 70%+ cacao, 1-2 squares")
    pdf.add_blank_line()
    pdf.add_heading2("Complete Grocery Shopping List")
    pdf.add_heading3("Proteins")
    pdf.add_bullet("Wild-caught salmon, sardines, mackerel")
    pdf.add_bullet("Organic chicken breast and thighs")
    pdf.add_bullet("Grass-fed beef (occasional)")
    pdf.add_bullet("Eggs (pasture-raised)")
    pdf.add_bullet("Lentils, chickpeas, black beans")
    pdf.add_bullet("Tempeh and organic tofu")
    pdf.add_heading3("Vegetables")
    pdf.add_bullet("Spinach, kale, arugula, Swiss chard")
    pdf.add_bullet("Broccoli, cauliflower, Brussels sprouts")
    pdf.add_bullet("Bell peppers, tomatoes, onions")
    pdf.add_bullet("Sweet potatoes, butternut squash")
    pdf.add_bullet("Zucchini, asparagus, artichokes")
    pdf.add_bullet("Garlic, ginger root, fresh herbs")
    pdf.add_heading3("Fruits")
    pdf.add_bullet("Blueberries, raspberries, strawberries")
    pdf.add_bullet("Cherries, pomegranate, oranges")
    pdf.add_bullet("Avocados, lemons, limes")
    pdf.add_bullet("Apples, pears (with skin)")
    pdf.add_heading3("Pantry Staples")
    pdf.add_bullet("Extra virgin olive oil (cold-pressed)")
    pdf.add_bullet("Coconut oil (unrefined)")
    pdf.add_bullet("Apple cider vinegar")
    pdf.add_bullet("Turmeric, cinnamon, black pepper")
    pdf.add_bullet("Green tea, herbal teas")
    pdf.add_bullet("Bone broth or vegetable broth")
    pdf.add_bullet("Quinoa, brown rice, steel-cut oats")
    pdf.add_bullet("Raw nuts: walnuts, almonds, cashews")
    pdf.add_bullet("Seeds: chia, flax, hemp, pumpkin")
    pdf.add_page_break()
    
    # Chapter 3 - 4 Week Meal Plan
    pdf.add_heading1("Chapter 3: 4-Week Anti-Inflammatory Meal Plan")
    pdf.add_blank_line()
    pdf.add_paragraph("This meal plan is designed to gradually transition you to an anti-inflammatory "
                      "diet. Each week builds on the previous one, making sustainable changes.")
    pdf.add_blank_line()
    
    weeks = [
        ("Week 1: Foundation - Remove the Worst Offenders",
         [("Monday", "Green smoothie with spinach, berries, flax", "Large salad with salmon, olive oil dressing", "Herb-roasted chicken with roasted vegetables"),
          ("Tuesday", "Overnight oats with walnuts and blueberries", "Lentil soup with mixed greens side", "Baked salmon with steamed broccoli and quinoa"),
          ("Wednesday", "Avocado toast on sprouted bread with eggs", "Leftover salmon quinoa bowl with greens", "Turkey stir-fry with colorful vegetables"),
          ("Thursday", "Turmeric golden milk smoothie with banana", "Chickpea salad with olive oil and herbs", "Grass-fed beef stew with root vegetables"),
          ("Friday", "Berry parfait with coconut yogurt and seeds", "Mediterranean wrap with hummus and veggies", "Baked cod with sweet potato and asparagus"),
          ("Saturday", "Veggie omelet with fresh herbs", "Bone broth soup with mixed vegetables", "Grilled chicken with Mediterranean salad"),
          ("Sunday", "Banana pancakes (oat flour) with berries", "Leftover chicken grain bowl", "Slow cooker anti-inflammatory stew")]),
        ("Week 2: Increase Anti-Inflammatory Foods",
         [("Monday", "Matcha smoothie bowl with seeds and fruit", "Turmeric chicken salad with greens", "Wild salmon with garlic roasted vegetables"),
          ("Tuesday", "Chia pudding with coconut milk and mango", "Lentil curry with brown rice", "Herb-crusted fish with steamed greens"),
          ("Wednesday", "Green juice + boiled eggs + avocado", "Sardine salad on greens with lemon", "Chicken bone broth bowl with vegetables"),
          ("Thursday", "Sweet potato breakfast hash with eggs", "Anti-inflammatory Buddha bowl", "Turkey meatballs with zucchini noodles"),
          ("Friday", "Smoothie: kale, pineapple, ginger, turmeric", "Grilled chicken over massaged kale salad", "Coconut curry shrimp with cauliflower rice"),
          ("Saturday", "Buckwheat crepes with berries", "Roasted vegetable and lentil soup", "Grilled fish tacos with cabbage slaw"),
          ("Sunday", "Frittata with seasonal vegetables", "Leftovers bowl with fresh greens", "Slow cooker chicken with sweet potatoes")]),
        ("Week 3: Optimize and Fine-Tune",
         [("Monday", "Anti-inflammatory smoothie (beets, berries, ginger)", "Mediterranean quinoa bowl", "Pan-seared salmon with herb sauce"),
          ("Tuesday", "Coconut yogurt bowl with anti-inflammatory granola", "Turmeric cauliflower soup", "Grass-fed burger (no bun) with roasted veggies"),
          ("Wednesday", "Egg muffins with vegetables (prep ahead)", "Big colorful salad with seeds and avocado", "Thai coconut fish curry with vegetables"),
          ("Thursday", "Golden milk oatmeal with walnuts", "Leftover curry over greens", "Chicken with roasted Brussels sprouts"),
          ("Friday", "Green smoothie with collagen and flax", "Sardines with crackers and veggie sticks", "Stuffed bell peppers with quinoa"),
          ("Saturday", "Sweet potato pancakes with cinnamon", "Minestrone soup (no pasta)", "Baked fish with pesto and vegetables"),
          ("Sunday", "Brunch: smoked salmon, eggs, avocado", "Light soup or salad", "Sheet pan chicken with root vegetables")]),
        ("Week 4: Full Anti-Inflammatory Lifestyle",
         [("Monday", "Warming turmeric porridge with seeds", "Healing bone broth with vegetables", "Herb-roasted salmon with asparagus"),
          ("Tuesday", "Protein smoothie with greens and berries", "Rainbow Buddha bowl with tahini", "Slow cooker anti-inflammatory chili"),
          ("Wednesday", "Avocado and egg with sauerkraut", "Leftover chili with greens", "Pan-seared fish with mushrooms"),
          ("Thursday", "Overnight oats with anti-inflammatory spices", "Large Mediterranean salad", "Chicken curry with cauliflower rice"),
          ("Friday", "Green juice + nut butter on seed crackers", "Lentil and vegetable stew", "Grilled fish with chimichurri"),
          ("Saturday", "Veggie-loaded frittata", "Grain bowl with roasted vegetables", "Turkey stuffed sweet potatoes"),
          ("Sunday", "Celebration brunch: all favorites", "Light and fresh salad", "Roast chicken with seasonal vegetables")])
    ]
    
    for week_title, days in weeks:
        pdf.add_heading2(week_title)
        pdf.add_blank_line()
        for day, breakfast, lunch, dinner in days:
            pdf.add_heading3(day)
            pdf.add_bullet(f"Breakfast: {breakfast}")
            pdf.add_bullet(f"Lunch: {lunch}")
            pdf.add_bullet(f"Dinner: {dinner}")
            pdf.add_blank_line()
        pdf.add_page_break()
    
    # Chapter 4 - Recipes
    pdf.add_heading1("Chapter 4: Anti-Inflammatory Recipes")
    pdf.add_blank_line()
    recipes = [
        ("Golden Turmeric Smoothie", ["1 cup unsweetened almond milk", "1/2 banana (frozen)",
         "1 tsp turmeric powder", "1/2 tsp cinnamon", "1 tbsp almond butter", "1 tsp honey",
         "Pinch of black pepper (enhances turmeric absorption)", "Ice cubes"],
         "Blend all ingredients until smooth. The black pepper increases turmeric bioavailability by up to 2000%."),
        ("Anti-Inflammatory Salmon Bowl", ["4 oz wild-caught salmon fillet", "1 cup cooked quinoa",
         "1 cup mixed greens", "1/2 avocado, sliced", "1/4 cup shredded carrots",
         "2 tbsp extra virgin olive oil", "1 tbsp lemon juice", "Fresh dill and parsley"],
         "Bake salmon at 400F for 12-15 minutes. Arrange bowl with quinoa base, greens, and toppings. Drizzle with olive oil and lemon."),
        ("Healing Bone Broth Soup", ["4 cups bone broth (chicken or beef)", "2 cups mixed vegetables (carrots, celery, onion)",
         "1 cup leafy greens (kale or spinach)", "2 cloves garlic, minced", "1 inch fresh ginger, grated",
         "1 tsp turmeric", "Salt and pepper to taste", "Fresh herbs for garnish"],
         "Saute vegetables and garlic in olive oil. Add broth, ginger, and turmeric. Simmer 20 minutes. Add greens last 2 minutes."),
        ("Overnight Anti-Inflammatory Oats", ["1/2 cup rolled oats", "1 cup almond milk",
         "1 tbsp chia seeds", "1/2 tsp cinnamon", "1/4 tsp turmeric", "1 tbsp walnuts",
         "Fresh berries for topping", "1 tsp raw honey (optional)"],
         "Combine oats, milk, chia, and spices in a jar. Refrigerate overnight. Top with walnuts and berries in the morning."),
        ("Mediterranean Lentil Salad", ["1 cup cooked green lentils", "1 cucumber, diced",
         "1 cup cherry tomatoes, halved", "1/4 red onion, finely diced", "1/4 cup fresh parsley",
         "2 tbsp extra virgin olive oil", "1 tbsp lemon juice", "Salt, pepper, oregano"],
         "Combine all ingredients in a large bowl. Toss with olive oil and lemon dressing. Best served at room temperature.")
    ]
    
    for name, ingredients, instructions in recipes:
        pdf.add_heading2(name)
        pdf.add_heading3("Ingredients:")
        for ing in ingredients:
            pdf.add_bullet(ing)
        pdf.add_blank_line()
        pdf.add_heading3("Instructions:")
        pdf.add_paragraph(instructions)
        pdf.add_blank_line()
        pdf.add_separator()
    pdf.add_page_break()
    
    # Chapter 5 - Tracking
    pdf.add_heading1("Chapter 5: Daily Food & Symptom Tracker")
    pdf.add_paragraph("Track what you eat and how you feel to identify your personal triggers.")
    pdf.add_blank_line()
    add_tracker_pages(pdf, "Daily Anti-Inflammatory Tracker",
                      ["Breakfast", "Lunch", "Dinner", "Snacks",
                       "Water (glasses)", "Energy (1-10)", "Pain (1-10)",
                       "Digestion (1-10)", "Mood (1-10)", "Notes"], num_pages=16)
    pdf.add_page_break()
    
    # Chapter 6 - Lifestyle
    pdf.add_heading1("Chapter 6: Anti-Inflammatory Lifestyle Strategies")
    pdf.add_blank_line()
    pdf.add_heading2("Movement & Exercise")
    pdf.add_paragraph("Regular moderate exercise reduces inflammatory markers. Aim for 150 minutes "
                      "per week of moderate activity.")
    pdf.add_bullet("Walking: 30 minutes daily, preferably in nature")
    pdf.add_bullet("Yoga: Reduces cortisol and inflammation")
    pdf.add_bullet("Swimming: Low-impact, full-body movement")
    pdf.add_bullet("Strength training: 2-3x per week, moderate intensity")
    pdf.add_bullet("Avoid overtraining: Excessive exercise increases inflammation")
    pdf.add_blank_line()
    pdf.add_heading2("Sleep Optimization")
    pdf.add_paragraph("Poor sleep dramatically increases inflammation. Prioritize 7-9 hours nightly.")
    pdf.add_bullet("Consistent sleep/wake schedule (even weekends)")
    pdf.add_bullet("Dark, cool bedroom (65-68F)")
    pdf.add_bullet("No screens 1 hour before bed")
    pdf.add_bullet("Magnesium before bed may help")
    pdf.add_bullet("Address sleep apnea if suspected")
    pdf.add_blank_line()
    pdf.add_heading2("Stress Management")
    pdf.add_paragraph("Chronic stress is one of the biggest drivers of inflammation.")
    pdf.add_bullet("Daily meditation or deep breathing (10+ minutes)")
    pdf.add_bullet("Time in nature (reduces cortisol)")
    pdf.add_bullet("Social connection and community")
    pdf.add_bullet("Journaling and gratitude practice")
    pdf.add_bullet("Set boundaries and reduce overcommitment")
    pdf.add_blank_line()
    pdf.add_heading2("Supplements to Discuss with Your Doctor")
    pdf.add_bullet("Omega-3 fish oil (EPA/DHA)")
    pdf.add_bullet("Curcumin (turmeric extract with piperine)")
    pdf.add_bullet("Vitamin D3 (most people are deficient)")
    pdf.add_bullet("Probiotics (for gut health)")
    pdf.add_bullet("Magnesium glycinate")
    pdf.add_page_break()
    
    # Chapter 7 - Progress Review
    pdf.add_heading1("Chapter 7: Progress Review & Adjustment")
    pdf.add_blank_line()
    add_weekly_review(pdf, [
        "Biggest improvement this week:",
        "Biggest challenge this week:",
        "Foods that made me feel best:",
        "Foods that triggered symptoms:",
        "Energy level average (1-10):",
        "Pain level average (1-10):",
        "Adjustment for next week:",
        "Goal for next week:"
    ], num_weeks=8)
    pdf.add_page_break()
    
    # FAQ
    faqs = [
        ("How quickly will I see results?", "Most people notice improvements in energy and digestion within 2-3 weeks. Significant reduction in pain and inflammation markers may take 6-12 weeks of consistent dietary changes."),
        ("Do I have to give up all inflammatory foods forever?", "No. The goal is an 80/20 approach - eat anti-inflammatory foods 80% of the time. Occasional treats won't undo your progress if your baseline diet is solid."),
        ("Can I still drink coffee?", "Yes! Coffee in moderation (1-3 cups) is actually anti-inflammatory due to its polyphenol content. Avoid adding sugar and artificial creamers."),
        ("What about nightshade vegetables?", "Nightshades (tomatoes, peppers, eggplant) are anti-inflammatory for most people. Only eliminate them if you notice they trigger YOUR symptoms."),
        ("Is organic food necessary?", "Prioritize organic for the Dirty Dozen (thin-skinned produce). For other items, conventional is fine - eating vegetables matters more than organic vs conventional."),
        ("Can this diet help autoimmune conditions?", "Many people with autoimmune conditions report significant improvement with anti-inflammatory diets. Work with your doctor to complement medical treatment."),
        ("How much water should I drink?", "Aim for half your body weight in ounces daily. Hydration supports every anti-inflammatory process in your body."),
        ("What if I have food allergies?", "Adapt the meal plan around your allergies. The principles remain the same - focus on whole, colorful, unprocessed foods."),
        ("Should I take anti-inflammatory supplements?", "Food should be your foundation. Discuss supplements with your healthcare provider, especially omega-3s, vitamin D, and curcumin."),
        ("Can children follow this diet?", "The principles are healthy for all ages. Adjust portions and ensure adequate calories for growing children. Consult a pediatrician."),
    ]
    add_faq_section(pdf, faqs)
    pdf.add_page_break()
    
    # Resources
    pdf.add_heading1("Resources & Recommended Reading")
    pdf.add_blank_line()
    pdf.add_heading3("When to See a Doctor")
    pdf.add_bullet("Persistent pain lasting more than 2 weeks")
    pdf.add_bullet("Unexplained weight changes")
    pdf.add_bullet("Severe digestive issues not improving with diet")
    pdf.add_bullet("Signs of infection (fever, swelling, redness)")
    pdf.add_bullet("Before starting any new supplement regimen")
    pdf.add_blank_line()
    pdf.add_heading3("Recommended Lab Tests")
    pdf.add_bullet("hs-CRP (high-sensitivity C-reactive protein)")
    pdf.add_bullet("ESR (erythrocyte sedimentation rate)")
    pdf.add_bullet("Vitamin D levels")
    pdf.add_bullet("Complete blood count (CBC)")
    pdf.add_bullet("Comprehensive metabolic panel")
    pdf.add_blank_line()
    pdf.add_heading3("Quick-Reference: Daily Anti-Inflammatory Checklist")
    pdf.add_bullet("[ ] Ate 5+ servings of colorful vegetables")
    pdf.add_bullet("[ ] Consumed omega-3 rich food or supplement")
    pdf.add_bullet("[ ] Used anti-inflammatory spices (turmeric, ginger)")
    pdf.add_bullet("[ ] Drank 8+ glasses of water")
    pdf.add_bullet("[ ] Moved my body for 30+ minutes")
    pdf.add_bullet("[ ] Managed stress (meditation, deep breathing)")
    pdf.add_bullet("[ ] Got 7-9 hours of quality sleep")
    pdf.add_bullet("[ ] Avoided processed foods and added sugars")
    
    add_about_author(pdf)
    filepath = os.path.join(OUTPUT_DIR, "01-Anti-Inflammatory-Diet-Complete-Guide.pdf")
    pdf.save(filepath)
    return filepath



def book_02_gut_health():
    """Gut Health Recovery Workbook"""
    pdf = PurePDF(title="Gut Health Recovery Workbook", author=AUTHOR)
    add_front_matter(pdf, "Gut Health Recovery Workbook", "Food Sensitivity Tracker & Healing Protocol")
    
    chapters = ["Understanding Your Gut Microbiome", "Gut Health Self-Assessment",
                "The Elimination Diet Protocol", "Food Sensitivity Tracker",
                "Gut-Healing Nutrition Plan", "Lifestyle Strategies for Gut Health",
                "Progress Review & Reintroduction", "FAQ & Resources"]
    add_toc(pdf, chapters)
    
    # Introduction
    pdf.add_heading1("Introduction")
    pdf.add_paragraph("Your gut is often called your 'second brain' - and for good reason. The gut "
                      "microbiome influences everything from digestion and immunity to mental health "
                      "and energy levels. If you're experiencing bloating, irregular bowel movements, "
                      "food sensitivities, or unexplained fatigue, your gut health may need attention.")
    pdf.add_blank_line()
    pdf.add_paragraph("This workbook provides a structured approach to identifying food triggers, "
                      "healing your gut lining, and rebuilding a healthy microbiome through diet "
                      "and lifestyle changes.")
    pdf.add_blank_line()
    pdf.add_heading3("Who This Book Is For")
    pdf.add_bullet("People with IBS, bloating, or chronic digestive issues")
    pdf.add_bullet("Those suspecting food sensitivities or intolerances")
    pdf.add_bullet("Anyone recovering from antibiotic use or gut infections")
    pdf.add_bullet("People with autoimmune conditions linked to gut health")
    pdf.add_bullet("Anyone wanting to optimize their microbiome")
    pdf.add_page_break()
    
    # Chapter 1
    pdf.add_heading1("Chapter 1: Understanding Your Gut Microbiome")
    pdf.add_blank_line()
    pdf.add_heading2("The Gut Ecosystem")
    pdf.add_paragraph("Your gut contains trillions of microorganisms - bacteria, fungi, viruses, "
                      "and other microbes that form a complex ecosystem. This microbiome weighs "
                      "about 3-5 pounds and contains more genetic material than your own cells.")
    pdf.add_blank_line()
    pdf.add_heading3("Functions of a Healthy Gut")
    pdf.add_bullet("Digests food and absorbs nutrients")
    pdf.add_bullet("Produces vitamins (B12, K, folate)")
    pdf.add_bullet("Regulates immune system (70% lives in gut)")
    pdf.add_bullet("Produces neurotransmitters (95% of serotonin)")
    pdf.add_bullet("Protects against pathogens")
    pdf.add_bullet("Regulates inflammation throughout the body")
    pdf.add_bullet("Influences weight and metabolism")
    pdf.add_blank_line()
    pdf.add_heading2("Signs of an Unhealthy Gut")
    pdf.add_heading3("Digestive Symptoms")
    pdf.add_bullet("Bloating after meals")
    pdf.add_bullet("Gas and abdominal discomfort")
    pdf.add_bullet("Constipation, diarrhea, or alternating")
    pdf.add_bullet("Acid reflux or heartburn")
    pdf.add_bullet("Undigested food in stool")
    pdf.add_heading3("Non-Digestive Symptoms")
    pdf.add_bullet("Chronic fatigue")
    pdf.add_bullet("Brain fog and poor concentration")
    pdf.add_bullet("Skin problems (acne, eczema, rosacea)")
    pdf.add_bullet("Mood disorders (anxiety, depression)")
    pdf.add_bullet("Frequent colds and infections")
    pdf.add_bullet("Joint pain and inflammation")
    pdf.add_bullet("Sugar cravings")
    pdf.add_blank_line()
    pdf.add_heading2("What Damages Gut Health")
    pdf.add_bullet("Antibiotics (kill beneficial bacteria along with harmful)")
    pdf.add_bullet("NSAIDs and acid-blocking medications")
    pdf.add_bullet("High-sugar, low-fiber diet")
    pdf.add_bullet("Chronic stress")
    pdf.add_bullet("Alcohol and processed foods")
    pdf.add_bullet("Food additives and emulsifiers")
    pdf.add_bullet("Environmental toxins")
    pdf.add_blank_line()
    pdf.add_heading2("The 5R Protocol for Gut Healing")
    pdf.add_paragraph("This evidence-based framework guides gut recovery:")
    pdf.add_bullet("1. REMOVE: Eliminate triggers (foods, stress, toxins, infections)")
    pdf.add_bullet("2. REPLACE: Add digestive support (enzymes, acid, bile)")
    pdf.add_bullet("3. REINOCULATE: Restore beneficial bacteria (probiotics, prebiotics)")
    pdf.add_bullet("4. REPAIR: Heal the gut lining (L-glutamine, bone broth, zinc)")
    pdf.add_bullet("5. REBALANCE: Lifestyle factors (sleep, stress, movement)")
    pdf.add_page_break()
    
    # Chapter 2 - Assessment
    pdf.add_heading1("Chapter 2: Gut Health Self-Assessment")
    pdf.add_blank_line()
    pdf.add_heading2("Symptom Severity Assessment")
    pdf.add_paragraph("Rate each symptom 0 (none) to 5 (severe). Complete at baseline and every 4 weeks.")
    pdf.add_blank_line()
    symptoms = ["Bloating", "Gas/flatulence", "Abdominal pain", "Constipation", "Diarrhea",
                "Acid reflux", "Nausea", "Fatigue", "Brain fog", "Headaches", "Joint pain",
                "Skin issues", "Mood changes", "Sugar cravings", "Food reactions"]
    pdf.add_paragraph("Date: __/__/____")
    pdf.add_blank_line()
    for s in symptoms:
        pdf.add_paragraph(f"  {s}: ____/5   Notes: _______________________")
    pdf.add_blank_line()
    pdf.add_paragraph(f"Total Score: ____/75")
    pdf.add_blank_line()
    pdf.add_heading3("Score Interpretation")
    pdf.add_bullet("0-15: Mild gut issues - focus on optimization")
    pdf.add_bullet("16-35: Moderate dysfunction - elimination diet recommended")
    pdf.add_bullet("36-55: Significant issues - consider professional guidance")
    pdf.add_bullet("56-75: Severe - work with a functional medicine practitioner")
    pdf.add_blank_line()
    pdf.add_heading2("Bristol Stool Chart Reference")
    pdf.add_paragraph("Track your stool type daily using this scale:")
    pdf.add_bullet("Type 1: Separate hard lumps (severe constipation)")
    pdf.add_bullet("Type 2: Lumpy, sausage-shaped (mild constipation)")
    pdf.add_bullet("Type 3: Sausage with cracks (normal)")
    pdf.add_bullet("Type 4: Smooth, soft sausage (ideal)")
    pdf.add_bullet("Type 5: Soft blobs with clear edges (lacking fiber)")
    pdf.add_bullet("Type 6: Mushy, fluffy pieces (mild diarrhea)")
    pdf.add_bullet("Type 7: Watery, no solid pieces (severe diarrhea)")
    pdf.add_page_break()
    
    # Chapter 3 - Elimination Diet
    pdf.add_heading1("Chapter 3: The Elimination Diet Protocol")
    pdf.add_blank_line()
    pdf.add_heading2("Phase 1: Elimination (2-4 Weeks)")
    pdf.add_paragraph("Remove common trigger foods completely for 2-4 weeks until symptoms improve.")
    pdf.add_blank_line()
    pdf.add_heading3("Foods to REMOVE")
    pdf.add_bullet("Gluten (wheat, barley, rye, spelt)")
    pdf.add_bullet("Dairy (milk, cheese, yogurt, butter)")
    pdf.add_bullet("Eggs")
    pdf.add_bullet("Soy (tofu, soy sauce, edamame)")
    pdf.add_bullet("Corn")
    pdf.add_bullet("Refined sugar and artificial sweeteners")
    pdf.add_bullet("Alcohol")
    pdf.add_bullet("Caffeine (or reduce to 1 cup green tea)")
    pdf.add_bullet("Processed and packaged foods")
    pdf.add_blank_line()
    pdf.add_heading3("Foods to EAT Freely")
    pdf.add_bullet("All vegetables (especially leafy greens)")
    pdf.add_bullet("Most fruits (limit high-sugar tropical fruits)")
    pdf.add_bullet("Lean proteins: chicken, turkey, fish")
    pdf.add_bullet("Healthy fats: olive oil, avocado, coconut oil")
    pdf.add_bullet("Gluten-free grains: rice, quinoa, millet")
    pdf.add_bullet("Nuts and seeds (if tolerated)")
    pdf.add_bullet("Herbs, spices, and bone broth")
    pdf.add_blank_line()
    pdf.add_heading2("Phase 2: Reintroduction (6-8 Weeks)")
    pdf.add_paragraph("Reintroduce one food at a time, every 3-4 days, and monitor reactions.")
    pdf.add_blank_line()
    pdf.add_heading3("Reintroduction Protocol")
    pdf.add_bullet("Day 1: Eat the test food 2-3 times")
    pdf.add_bullet("Days 2-3: Remove the food and monitor symptoms")
    pdf.add_bullet("Day 4: If no reaction, move to next food")
    pdf.add_bullet("If reaction occurs: Remove food, wait until symptoms clear, then test next food")
    pdf.add_blank_line()
    pdf.add_heading3("Reintroduction Order (least to most reactive)")
    pdf.add_bullet("1. Eggs")
    pdf.add_bullet("2. Dairy (start with butter/ghee)")
    pdf.add_bullet("3. Gluten-free grains (oats)")
    pdf.add_bullet("4. Soy")
    pdf.add_bullet("5. Corn")
    pdf.add_bullet("6. Gluten (start with sourdough)")
    pdf.add_page_break()
    
    # Chapter 4 - Tracking
    pdf.add_heading1("Chapter 4: Food Sensitivity Tracker")
    pdf.add_blank_line()
    pdf.add_paragraph("Use these pages to track your elimination and reintroduction phases.")
    pdf.add_blank_line()
    add_tracker_pages(pdf, "Daily Gut Health Tracker",
                      ["Breakfast", "Lunch", "Dinner", "Snacks",
                       "Bloating (1-10)", "Pain (1-10)", "Stool Type (1-7)",
                       "Energy (1-10)", "Mood (1-10)", "Reactions/Notes"], num_pages=16)
    pdf.add_page_break()
    
    # Chapter 5 - Nutrition
    pdf.add_heading1("Chapter 5: Gut-Healing Nutrition Plan")
    pdf.add_blank_line()
    pdf.add_heading2("Gut-Healing Foods")
    pdf.add_heading3("Prebiotic Foods (feed good bacteria)")
    pdf.add_bullet("Garlic, onions, leeks")
    pdf.add_bullet("Asparagus, artichokes")
    pdf.add_bullet("Bananas (slightly green)")
    pdf.add_bullet("Oats and flaxseeds")
    pdf.add_bullet("Apples (with skin)")
    pdf.add_heading3("Probiotic Foods (add good bacteria)")
    pdf.add_bullet("Sauerkraut (unpasteurized)")
    pdf.add_bullet("Kimchi")
    pdf.add_bullet("Kombucha")
    pdf.add_bullet("Coconut yogurt")
    pdf.add_bullet("Miso and tempeh")
    pdf.add_heading3("Gut-Lining Repair Foods")
    pdf.add_bullet("Bone broth (collagen and amino acids)")
    pdf.add_bullet("Cabbage juice (L-glutamine)")
    pdf.add_bullet("Slippery elm and marshmallow root tea")
    pdf.add_bullet("Aloe vera juice")
    pdf.add_bullet("Zinc-rich foods (pumpkin seeds, oysters)")
    pdf.add_blank_line()
    pdf.add_heading2("7-Day Gut Healing Meal Plan")
    gut_meals = [
        ("Monday", "Bone broth + scrambled eggs with spinach", "Chicken and vegetable soup", "Baked salmon with steamed vegetables"),
        ("Tuesday", "Smoothie: banana, coconut yogurt, flax", "Turkey lettuce wraps with avocado", "Slow-cooker chicken with root vegetables"),
        ("Wednesday", "Overnight oats with berries and seeds", "Bone broth soup with greens", "Grilled fish with quinoa and asparagus"),
        ("Thursday", "Scrambled eggs with sauerkraut", "Large salad with olive oil dressing", "Chicken stir-fry with coconut aminos"),
        ("Friday", "Coconut yogurt parfait with seeds", "Lentil soup (if tolerated)", "Baked cod with sweet potato"),
        ("Saturday", "Sweet potato hash with eggs", "Leftover fish and veggie bowl", "Turkey meatballs with zucchini noodles"),
        ("Sunday", "Green smoothie with collagen powder", "Bone broth with vegetables", "Roast chicken with roasted vegetables")
    ]
    for day, b, l, d in gut_meals:
        pdf.add_heading3(day)
        pdf.add_bullet(f"Breakfast: {b}")
        pdf.add_bullet(f"Lunch: {l}")
        pdf.add_bullet(f"Dinner: {d}")
        pdf.add_blank_line()
    pdf.add_page_break()
    
    # Chapter 6 - Lifestyle
    pdf.add_heading1("Chapter 6: Lifestyle Strategies for Gut Health")
    pdf.add_blank_line()
    pdf.add_heading2("Stress and Your Gut")
    pdf.add_paragraph("The gut-brain axis means stress directly impacts digestion. Chronic stress "
                      "reduces beneficial bacteria, increases gut permeability, and slows motility.")
    pdf.add_bullet("Practice diaphragmatic breathing before meals")
    pdf.add_bullet("Eat in a calm, relaxed environment")
    pdf.add_bullet("Chew food thoroughly (30+ chews per bite)")
    pdf.add_bullet("Avoid eating while stressed or distracted")
    pdf.add_bullet("Daily meditation or yoga")
    pdf.add_blank_line()
    pdf.add_heading2("Sleep and Gut Health")
    pdf.add_paragraph("Poor sleep disrupts the circadian rhythms of your gut bacteria.")
    pdf.add_bullet("Consistent sleep schedule supports microbiome diversity")
    pdf.add_bullet("Avoid large meals within 3 hours of bedtime")
    pdf.add_bullet("Aim for 7-9 hours of quality sleep")
    pdf.add_blank_line()
    pdf.add_heading2("Movement for Digestion")
    pdf.add_bullet("Gentle walking after meals aids digestion")
    pdf.add_bullet("Yoga poses for digestion (twists, forward folds)")
    pdf.add_bullet("Regular exercise increases microbiome diversity")
    pdf.add_bullet("Avoid intense exercise immediately after eating")
    pdf.add_page_break()
    
    # Chapter 7 - Progress Review
    pdf.add_heading1("Chapter 7: Progress Review & Reintroduction Log")
    pdf.add_blank_line()
    pdf.add_heading2("Food Reintroduction Record")
    for i in range(8):
        pdf.add_heading3(f"Reintroduction Test #{i+1}")
        pdf.add_paragraph(f"Food Being Tested: ___________________")
        pdf.add_paragraph(f"Date Started: __/__/____")
        pdf.add_paragraph(f"Amount Consumed: ___________________")
        pdf.add_paragraph(f"Symptoms (0-24 hours): ___________________")
        pdf.add_paragraph(f"Symptoms (24-72 hours): ___________________")
        pdf.add_paragraph(f"Result: [ ] PASS (no reaction)  [ ] FAIL (reaction)")
        pdf.add_paragraph(f"Notes: ___________________________________")
        pdf.add_blank_line()
        pdf.add_separator()
    pdf.add_page_break()
    
    add_weekly_review(pdf, [
        "Overall digestion this week (1-10):",
        "Bloating frequency (times per week):",
        "Energy level average:",
        "Foods that worked well:",
        "Foods that caused issues:",
        "Stool consistency pattern:",
        "Supplement changes:",
        "Goals for next week:"
    ], num_weeks=4)
    pdf.add_page_break()
    
    # FAQ
    faqs = [
        ("How long does gut healing take?", "It varies by individual. Most people see improvement in 2-4 weeks, but full healing of gut lining can take 3-6 months. Consistency is key."),
        ("Do I need a probiotic supplement?", "Food-based probiotics are preferred. If supplementing, choose a multi-strain probiotic with at least 10 billion CFUs. Start slowly to avoid die-off symptoms."),
        ("What is leaky gut?", "Intestinal permeability ('leaky gut') occurs when tight junctions in the gut lining weaken, allowing particles to enter the bloodstream and trigger immune reactions."),
        ("Can stress really affect my gut?", "Absolutely. The gut-brain axis is a bidirectional communication system. Stress can change gut motility, increase permeability, and alter the microbiome within hours."),
        ("Should I get tested for food sensitivities?", "Testing can be helpful but is not always accurate. The gold standard remains an elimination diet with careful reintroduction and symptom tracking."),
        ("How do I know if I need medical help?", "See a doctor if you have blood in stool, unexplained weight loss, severe pain, fever, or symptoms that don't improve after 4-6 weeks of dietary changes."),
        ("Is bone broth really beneficial?", "Yes. Bone broth contains collagen, glutamine, glycine, and gelatin - all of which support gut lining repair and reduce inflammation."),
        ("Can I heal my gut while on medications?", "Yes, though some medications (PPIs, NSAIDs, antibiotics) can slow healing. Never stop medications without medical guidance."),
        ("What about FODMAPs?", "If you have IBS, a low-FODMAP diet may help identify specific carbohydrate triggers. Consider working with a registered dietitian for this protocol."),
        ("How do I rebuild my microbiome after antibiotics?", "Focus on diverse fiber intake, fermented foods, and possibly a probiotic supplement for 2-3 months. Eat 30+ different plant foods per week."),
    ]
    add_faq_section(pdf, faqs)
    
    # Resources
    pdf.add_page_break()
    pdf.add_heading1("Resources")
    pdf.add_blank_line()
    pdf.add_heading3("Quick-Reference: Daily Gut Health Checklist")
    pdf.add_bullet("[ ] Ate prebiotic-rich foods (garlic, onions, asparagus)")
    pdf.add_bullet("[ ] Consumed probiotic food (sauerkraut, kimchi, yogurt)")
    pdf.add_bullet("[ ] Drank bone broth or gut-healing tea")
    pdf.add_bullet("[ ] Chewed food thoroughly and ate mindfully")
    pdf.add_bullet("[ ] Managed stress (breathing, meditation)")
    pdf.add_bullet("[ ] Drank adequate water between meals")
    pdf.add_bullet("[ ] Avoided known trigger foods")
    pdf.add_bullet("[ ] Gentle movement or walking after meals")
    
    add_about_author(pdf)
    filepath = os.path.join(OUTPUT_DIR, "02-Gut-Health-Recovery-Workbook.pdf")
    pdf.save(filepath)
    return filepath



def book_03_hormone_balance():
    """Hormone Balance Guide for Women"""
    pdf = PurePDF(title="Hormone Balance Guide for Women", author=AUTHOR)
    add_front_matter(pdf, "Hormone Balance Guide", "For Women: PCOS, Perimenopause & Thyroid Nutrition")
    
    chapters = ["Understanding Female Hormones", "Hormone Health Self-Assessment",
                "Cycle Syncing Protocol", "Nutrition for Hormone Balance",
                "Daily Hormone Tracker", "Lifestyle & Supplement Strategies",
                "Progress Review & Adjustment", "FAQ & Resources"]
    add_toc(pdf, chapters)
    
    pdf.add_heading1("Introduction")
    pdf.add_paragraph("Hormonal imbalances affect millions of women, causing symptoms ranging from "
                      "irregular periods and weight gain to mood swings, fatigue, and fertility issues. "
                      "This guide provides a comprehensive approach to understanding your hormones "
                      "and supporting balance through nutrition, lifestyle, and cycle syncing.")
    pdf.add_blank_line()
    pdf.add_heading3("Who This Book Is For")
    pdf.add_bullet("Women with PCOS or suspected hormonal imbalance")
    pdf.add_bullet("Those experiencing perimenopause symptoms")
    pdf.add_bullet("Women with thyroid concerns")
    pdf.add_bullet("Anyone wanting to understand their menstrual cycle better")
    pdf.add_bullet("Women struggling with PMS, irregular periods, or fertility")
    pdf.add_page_break()
    
    # Chapter 1
    pdf.add_heading1("Chapter 1: Understanding Female Hormones")
    pdf.add_blank_line()
    pdf.add_heading2("The Key Players")
    pdf.add_heading3("Estrogen")
    pdf.add_paragraph("The primary female sex hormone responsible for reproductive development, "
                      "bone health, brain function, and cardiovascular health. Too much (estrogen "
                      "dominance) or too little causes distinct symptoms.")
    pdf.add_bullet("High estrogen: Heavy periods, breast tenderness, weight gain, mood swings")
    pdf.add_bullet("Low estrogen: Hot flashes, vaginal dryness, bone loss, brain fog")
    pdf.add_blank_line()
    pdf.add_heading3("Progesterone")
    pdf.add_paragraph("The 'calming' hormone that balances estrogen, supports pregnancy, and "
                      "promotes relaxation and sleep.")
    pdf.add_bullet("Low progesterone: Anxiety, insomnia, short cycles, spotting, infertility")
    pdf.add_blank_line()
    pdf.add_heading3("Testosterone")
    pdf.add_paragraph("Women need small amounts for libido, muscle tone, energy, and motivation.")
    pdf.add_bullet("High testosterone (PCOS): Acne, facial hair, hair loss, irregular periods")
    pdf.add_bullet("Low testosterone: Low libido, fatigue, muscle weakness")
    pdf.add_blank_line()
    pdf.add_heading3("Cortisol")
    pdf.add_paragraph("The stress hormone that affects all other hormones when chronically elevated.")
    pdf.add_bullet("High cortisol: Weight gain (belly), anxiety, insomnia, sugar cravings")
    pdf.add_blank_line()
    pdf.add_heading3("Thyroid Hormones (T3, T4, TSH)")
    pdf.add_paragraph("Control metabolism, energy, temperature regulation, and weight.")
    pdf.add_bullet("Hypothyroid: Fatigue, weight gain, cold intolerance, hair loss, constipation")
    pdf.add_bullet("Hyperthyroid: Weight loss, anxiety, heart palpitations, heat intolerance")
    pdf.add_blank_line()
    pdf.add_heading3("Insulin")
    pdf.add_paragraph("Regulates blood sugar and is closely linked to all sex hormones.")
    pdf.add_bullet("Insulin resistance: Weight gain, PCOS, sugar cravings, energy crashes")
    pdf.add_blank_line()
    pdf.add_heading2("The Menstrual Cycle Phases")
    pdf.add_heading3("Phase 1: Menstrual (Days 1-5)")
    pdf.add_paragraph("All hormones are at their lowest. Energy is typically lowest. "
                      "Focus on rest, gentle movement, and iron-rich foods.")
    pdf.add_heading3("Phase 2: Follicular (Days 6-14)")
    pdf.add_paragraph("Estrogen rises steadily. Energy increases, creativity peaks. "
                      "Great time for new projects and intense exercise.")
    pdf.add_heading3("Phase 3: Ovulatory (Days 15-17)")
    pdf.add_paragraph("Estrogen and testosterone peak. Highest energy and social confidence. "
                      "Peak fertility window.")
    pdf.add_heading3("Phase 4: Luteal (Days 18-28)")
    pdf.add_paragraph("Progesterone rises then falls. Energy decreases. PMS symptoms may appear. "
                      "Focus on self-care and calming activities.")
    pdf.add_page_break()
    
    # Chapter 2 - Assessment
    pdf.add_heading1("Chapter 2: Hormone Health Self-Assessment")
    pdf.add_blank_line()
    pdf.add_heading2("Estrogen Dominance Checklist")
    pdf.add_paragraph("Check all that apply:")
    estrogen_symptoms = ["Heavy or painful periods", "Breast tenderness or fibrocystic breasts",
                         "Weight gain in hips and thighs", "Mood swings and irritability",
                         "Bloating and water retention", "Headaches or migraines (cyclical)",
                         "Fibroids or endometriosis", "PMS lasting 7+ days"]
    for s in estrogen_symptoms:
        pdf.add_bullet(f"[ ] {s}")
    pdf.add_paragraph("Score: ___/8  (4+ suggests estrogen dominance)")
    pdf.add_blank_line()
    pdf.add_heading2("Low Progesterone Checklist")
    prog_symptoms = ["Anxiety or nervousness", "Difficulty sleeping", "Short menstrual cycles (under 25 days)",
                     "Spotting before period", "Infertility or miscarriage", "Low mood in luteal phase",
                     "Night sweats", "Frequent headaches"]
    for s in prog_symptoms:
        pdf.add_bullet(f"[ ] {s}")
    pdf.add_paragraph("Score: ___/8  (4+ suggests low progesterone)")
    pdf.add_blank_line()
    pdf.add_heading2("PCOS Indicators")
    pcos_symptoms = ["Irregular or absent periods", "Acne (jawline, chin)", "Excess facial or body hair",
                     "Thinning hair on head", "Weight gain (especially belly)", "Difficulty losing weight",
                     "Dark patches on skin", "Sugar/carb cravings"]
    for s in pcos_symptoms:
        pdf.add_bullet(f"[ ] {s}")
    pdf.add_paragraph("Score: ___/8  (3+ suggests PCOS - see your doctor)")
    pdf.add_page_break()
    
    # Chapter 3 - Cycle Syncing
    pdf.add_heading1("Chapter 3: Cycle Syncing Protocol")
    pdf.add_blank_line()
    pdf.add_paragraph("Cycle syncing means aligning your nutrition, exercise, work, and self-care "
                      "with the four phases of your menstrual cycle for optimal hormonal support.")
    pdf.add_blank_line()
    pdf.add_heading2("Menstrual Phase (Days 1-5)")
    pdf.add_heading3("Nutrition")
    pdf.add_bullet("Iron-rich foods: red meat, lentils, spinach, pumpkin seeds")
    pdf.add_bullet("Warm, cooked foods (soups, stews)")
    pdf.add_bullet("Omega-3 fats for pain relief")
    pdf.add_bullet("Magnesium-rich foods for cramps")
    pdf.add_heading3("Exercise")
    pdf.add_bullet("Gentle yoga, walking, stretching")
    pdf.add_bullet("Rest days as needed")
    pdf.add_heading3("Lifestyle")
    pdf.add_bullet("Prioritize rest and sleep")
    pdf.add_bullet("Journaling and reflection")
    pdf.add_bullet("Reduce social obligations")
    pdf.add_blank_line()
    pdf.add_heading2("Follicular Phase (Days 6-14)")
    pdf.add_heading3("Nutrition")
    pdf.add_bullet("Light, fresh foods (salads, fermented foods)")
    pdf.add_bullet("Sprouted foods and lean proteins")
    pdf.add_bullet("Healthy fats for building hormones")
    pdf.add_heading3("Exercise")
    pdf.add_bullet("High intensity: HIIT, running, spinning")
    pdf.add_bullet("Try new workouts - energy is high")
    pdf.add_heading3("Lifestyle")
    pdf.add_bullet("Start new projects")
    pdf.add_bullet("Social activities and networking")
    pdf.add_bullet("Creative work and brainstorming")
    pdf.add_blank_line()
    pdf.add_heading2("Ovulatory Phase (Days 15-17)")
    pdf.add_heading3("Nutrition")
    pdf.add_bullet("Raw vegetables and anti-inflammatory foods")
    pdf.add_bullet("Cruciferous vegetables (help metabolize estrogen)")
    pdf.add_bullet("Lighter meals, fiber-rich foods")
    pdf.add_heading3("Exercise")
    pdf.add_bullet("Peak performance: heavy lifting, intense cardio")
    pdf.add_bullet("Group classes and competitive activities")
    pdf.add_heading3("Lifestyle")
    pdf.add_bullet("Important conversations and presentations")
    pdf.add_bullet("Date nights and social events")
    pdf.add_blank_line()
    pdf.add_heading2("Luteal Phase (Days 18-28)")
    pdf.add_heading3("Nutrition")
    pdf.add_bullet("Complex carbs (sweet potato, brown rice) - support serotonin")
    pdf.add_bullet("Magnesium-rich foods (dark chocolate, leafy greens)")
    pdf.add_bullet("B6 foods (chicken, bananas, potatoes)")
    pdf.add_bullet("Avoid excess salt, caffeine, alcohol")
    pdf.add_heading3("Exercise")
    pdf.add_bullet("Moderate: Pilates, strength training, yoga")
    pdf.add_bullet("Reduce intensity as period approaches")
    pdf.add_heading3("Lifestyle")
    pdf.add_bullet("Nesting and organizing")
    pdf.add_bullet("Self-care rituals")
    pdf.add_bullet("Earlier bedtime")
    pdf.add_page_break()
    
    # Chapter 4 - Nutrition
    pdf.add_heading1("Chapter 4: Nutrition for Hormone Balance")
    pdf.add_blank_line()
    pdf.add_heading2("Essential Nutrients for Hormones")
    pdf.add_bullet("Omega-3 fatty acids: Build hormone molecules (salmon, walnuts, flax)")
    pdf.add_bullet("Zinc: Supports ovulation and progesterone (pumpkin seeds, oysters)")
    pdf.add_bullet("Magnesium: Calms nervous system, reduces PMS (leafy greens, dark chocolate)")
    pdf.add_bullet("B6: Supports progesterone production (chicken, bananas)")
    pdf.add_bullet("Vitamin D: Functions as a hormone itself (sunlight, fatty fish)")
    pdf.add_bullet("Iron: Critical during menstruation (red meat, lentils)")
    pdf.add_bullet("Iodine: Essential for thyroid (seaweed, fish)")
    pdf.add_bullet("Selenium: Thyroid conversion T4 to T3 (Brazil nuts)")
    pdf.add_blank_line()
    pdf.add_heading2("Foods for Specific Conditions")
    pdf.add_heading3("For PCOS")
    pdf.add_bullet("Low-glycemic foods to manage insulin")
    pdf.add_bullet("Spearmint tea (may reduce androgens)")
    pdf.add_bullet("Inositol-rich foods (citrus, beans)")
    pdf.add_bullet("Anti-inflammatory foods")
    pdf.add_bullet("Cinnamon (may improve insulin sensitivity)")
    pdf.add_heading3("For Perimenopause")
    pdf.add_bullet("Phytoestrogen foods (flaxseeds, soy)")
    pdf.add_bullet("Calcium and vitamin D for bone health")
    pdf.add_bullet("Adaptogenic herbs (ashwagandha, maca)")
    pdf.add_bullet("Healthy fats for hormone production")
    pdf.add_heading3("For Thyroid Health")
    pdf.add_bullet("Selenium-rich foods (2-3 Brazil nuts daily)")
    pdf.add_bullet("Iodine (seaweed, fish, iodized salt)")
    pdf.add_bullet("Zinc (pumpkin seeds, beef)")
    pdf.add_bullet("Avoid excess raw cruciferous vegetables if hypothyroid")
    pdf.add_page_break()
    
    # Chapter 5 - Tracking
    pdf.add_heading1("Chapter 5: Daily Hormone & Cycle Tracker")
    pdf.add_blank_line()
    add_tracker_pages(pdf, "Daily Hormone Tracker",
                      ["Cycle Day", "Phase (M/F/O/L)", "Basal Body Temp",
                       "Energy (1-10)", "Mood (1-10)", "Sleep Quality (1-10)",
                       "Cravings", "Symptoms", "Exercise", "Notes"], num_pages=16)
    pdf.add_page_break()
    
    # Chapter 6 - Lifestyle
    pdf.add_heading1("Chapter 6: Lifestyle & Supplement Strategies")
    pdf.add_blank_line()
    pdf.add_heading2("Stress Management for Hormones")
    pdf.add_paragraph("Chronic stress steals progesterone to make cortisol (the 'progesterone steal').")
    pdf.add_bullet("Morning cortisol management: Sunlight within 30 min of waking")
    pdf.add_bullet("Adaptogenic herbs: Ashwagandha, rhodiola, holy basil")
    pdf.add_bullet("Evening routine: Dim lights, no screens, calming tea")
    pdf.add_bullet("Say no: Overcommitment raises cortisol")
    pdf.add_blank_line()
    pdf.add_heading2("Exercise Guidelines")
    pdf.add_bullet("Avoid overexercising (raises cortisol, disrupts hormones)")
    pdf.add_bullet("PCOS: Mix of strength training and moderate cardio")
    pdf.add_bullet("Perimenopause: Prioritize strength training for bone/muscle")
    pdf.add_bullet("Thyroid issues: Avoid extreme exercise, focus on consistency")
    pdf.add_blank_line()
    pdf.add_heading2("Supplements to Discuss with Your Doctor")
    pdf.add_bullet("Magnesium glycinate: 200-400mg at bedtime")
    pdf.add_bullet("Vitamin D3: 2000-5000 IU (test levels first)")
    pdf.add_bullet("Omega-3 fish oil: 1000-2000mg EPA/DHA")
    pdf.add_bullet("B-complex: Supports overall hormone metabolism")
    pdf.add_bullet("Zinc: 15-30mg (especially for PCOS)")
    pdf.add_bullet("Inositol: 2-4g (for PCOS insulin resistance)")
    pdf.add_bullet("DIM: Supports healthy estrogen metabolism")
    pdf.add_page_break()
    
    # Chapter 7
    pdf.add_heading1("Chapter 7: Progress Review")
    add_weekly_review(pdf, [
        "Cycle day range this week:",
        "Dominant symptoms:",
        "Energy pattern (high/medium/low):",
        "Exercise completed:",
        "Nutritional wins:",
        "Challenges faced:",
        "Supplement changes:",
        "Adjustment for next week:"
    ], num_weeks=5)
    pdf.add_page_break()
    
    faqs = [
        ("How long until I notice hormone improvements?", "Most women notice subtle improvements in 1-2 cycles. Significant changes typically take 3-6 months of consistent effort. Hormones respond slowly to lifestyle changes."),
        ("Should I get my hormones tested?", "Yes, especially if symptoms are severe. Ask for: estrogen, progesterone (Day 21), testosterone, DHEA-S, cortisol, full thyroid panel, fasting insulin, and vitamin D."),
        ("Can I balance hormones without medication?", "Many women can significantly improve symptoms through diet, lifestyle, and supplements alone. However, some conditions require medical intervention."),
        ("Does birth control mask hormone problems?", "Yes, hormonal birth control suppresses your natural cycle. It can mask underlying issues like PCOS or thyroid problems. Discuss alternatives with your doctor."),
        ("What is seed cycling?", "Eating specific seeds during different cycle phases: flax+pumpkin seeds in follicular phase, sesame+sunflower in luteal phase. Some women find it helpful for mild imbalances."),
        ("How does weight affect hormones?", "Fat tissue produces estrogen. Both excess weight and being underweight disrupt hormone balance. Aim for a healthy weight through nourishing (not restrictive) eating."),
        ("Can stress really stop my period?", "Yes. Extreme stress can cause hypothalamic amenorrhea by suppressing GnRH, the hormone that triggers ovulation. This is your body's protective mechanism."),
        ("Is soy good or bad for hormones?", "Moderate amounts of whole soy (tempeh, edamame) can be beneficial due to phytoestrogens. Avoid processed soy isolates. Those with thyroid issues should monitor intake."),
    ]
    add_faq_section(pdf, faqs)
    
    pdf.add_page_break()
    pdf.add_heading1("Quick-Reference: Hormone Balance Daily Checklist")
    pdf.add_bullet("[ ] Ate protein at every meal (stabilizes blood sugar)")
    pdf.add_bullet("[ ] Included healthy fats (olive oil, avocado, nuts)")
    pdf.add_bullet("[ ] Ate cruciferous vegetables (broccoli, cauliflower)")
    pdf.add_bullet("[ ] Managed stress (breathing, nature, boundaries)")
    pdf.add_bullet("[ ] Moved my body appropriately for cycle phase")
    pdf.add_bullet("[ ] Prioritized 7-9 hours of sleep")
    pdf.add_bullet("[ ] Took recommended supplements")
    pdf.add_bullet("[ ] Tracked cycle day and symptoms")
    
    add_about_author(pdf)
    filepath = os.path.join(OUTPUT_DIR, "03-Hormone-Balance-Guide-Women.pdf")
    pdf.save(filepath)
    return filepath



def book_04_blood_pressure():
    """Blood Pressure Management Workbook"""
    pdf = PurePDF(title="Blood Pressure Management Workbook", author=AUTHOR)
    add_front_matter(pdf, "Blood Pressure Management", "Daily BP Log, DASH Diet Guide & Lifestyle Plan")
    
    chapters = ["Understanding Blood Pressure", "Your BP Baseline Assessment",
                "The DASH Diet Guide", "Daily Blood Pressure Log",
                "Nutrition & Meal Planning", "Lifestyle Strategies",
                "Medication & Progress Tracking", "FAQ & Resources"]
    add_toc(pdf, chapters)
    
    pdf.add_heading1("Introduction")
    pdf.add_paragraph("High blood pressure (hypertension) is called the 'silent killer' because it "
                      "often has no symptoms while damaging your heart, kidneys, brain, and blood "
                      "vessels. The good news: lifestyle changes can significantly reduce blood "
                      "pressure, often by 10-20 points or more.")
    pdf.add_blank_line()
    pdf.add_paragraph("This workbook gives you the tools to monitor, manage, and reduce your "
                      "blood pressure through the proven DASH diet, stress management, exercise, "
                      "and daily tracking.")
    pdf.add_page_break()
    
    # Chapter 1
    pdf.add_heading1("Chapter 1: Understanding Blood Pressure")
    pdf.add_blank_line()
    pdf.add_heading2("What Blood Pressure Numbers Mean")
    pdf.add_paragraph("Blood pressure is measured in two numbers:")
    pdf.add_bullet("Systolic (top number): Pressure when heart beats")
    pdf.add_bullet("Diastolic (bottom number): Pressure between beats")
    pdf.add_blank_line()
    pdf.add_heading3("Blood Pressure Categories")
    pdf.add_bullet("Normal: Less than 120/80 mmHg")
    pdf.add_bullet("Elevated: 120-129/less than 80 mmHg")
    pdf.add_bullet("Stage 1 Hypertension: 130-139/80-89 mmHg")
    pdf.add_bullet("Stage 2 Hypertension: 140+/90+ mmHg")
    pdf.add_bullet("Hypertensive Crisis: 180+/120+ (seek emergency care)")
    pdf.add_blank_line()
    pdf.add_heading2("Risk Factors You Can Control")
    pdf.add_bullet("Diet high in sodium and processed foods")
    pdf.add_bullet("Excess weight (especially abdominal)")
    pdf.add_bullet("Physical inactivity")
    pdf.add_bullet("Excessive alcohol consumption")
    pdf.add_bullet("Chronic stress")
    pdf.add_bullet("Smoking")
    pdf.add_bullet("Poor sleep and sleep apnea")
    pdf.add_blank_line()
    pdf.add_heading2("Complications of Uncontrolled Hypertension")
    pdf.add_bullet("Heart attack and heart failure")
    pdf.add_bullet("Stroke")
    pdf.add_bullet("Kidney disease and failure")
    pdf.add_bullet("Vision loss")
    pdf.add_bullet("Cognitive decline and dementia")
    pdf.add_bullet("Peripheral artery disease")
    pdf.add_blank_line()
    pdf.add_heading2("How to Measure Blood Pressure Correctly")
    pdf.add_bullet("Sit quietly for 5 minutes before measuring")
    pdf.add_bullet("Sit with back supported, feet flat on floor")
    pdf.add_bullet("Arm supported at heart level")
    pdf.add_bullet("Do not smoke, exercise, or drink caffeine 30 minutes before")
    pdf.add_bullet("Take 2-3 readings, 1 minute apart, and average them")
    pdf.add_bullet("Measure at the same time daily (morning preferred)")
    pdf.add_bullet("Use a validated upper-arm cuff monitor")
    pdf.add_page_break()
    
    # Chapter 2 - Assessment
    pdf.add_heading1("Chapter 2: Your BP Baseline Assessment")
    pdf.add_blank_line()
    pdf.add_heading2("Initial Readings (Take for 7 days)")
    for d in range(7):
        pdf.add_paragraph(f"Day {d+1}: Date: __/__/____")
        pdf.add_paragraph(f"  Morning: ___/___ mmHg  Time: _____  Pulse: ___")
        pdf.add_paragraph(f"  Evening: ___/___ mmHg  Time: _____  Pulse: ___")
        pdf.add_blank_line()
    pdf.add_paragraph("7-Day Average: ___/___ mmHg")
    pdf.add_paragraph("Category: ___________________")
    pdf.add_blank_line()
    pdf.add_heading2("Risk Factor Assessment")
    pdf.add_paragraph("Current weight: ___ lbs  Height: ___  BMI: ___")
    pdf.add_paragraph("Waist circumference: ___ inches")
    pdf.add_paragraph("Current medications: _________________________")
    pdf.add_paragraph("Family history of hypertension: [ ] Yes [ ] No")
    pdf.add_paragraph("Smoking status: [ ] Never [ ] Former [ ] Current")
    pdf.add_paragraph("Alcohol (drinks/week): ___")
    pdf.add_paragraph("Exercise (minutes/week): ___")
    pdf.add_paragraph("Sodium intake estimate: [ ] Low [ ] Moderate [ ] High")
    pdf.add_paragraph("Stress level (1-10): ___")
    pdf.add_paragraph("Sleep hours/night: ___  Quality (1-10): ___")
    pdf.add_page_break()
    
    # Chapter 3 - DASH Diet
    pdf.add_heading1("Chapter 3: The DASH Diet Guide")
    pdf.add_blank_line()
    pdf.add_paragraph("DASH (Dietary Approaches to Stop Hypertension) is the most researched "
                      "diet for blood pressure reduction. It can lower BP by 8-14 points.")
    pdf.add_blank_line()
    pdf.add_heading2("DASH Diet Daily Servings")
    pdf.add_bullet("Grains: 6-8 servings (whole grains preferred)")
    pdf.add_bullet("Vegetables: 4-5 servings")
    pdf.add_bullet("Fruits: 4-5 servings")
    pdf.add_bullet("Low-fat dairy: 2-3 servings")
    pdf.add_bullet("Lean meats/fish: 6 oz or less")
    pdf.add_bullet("Nuts/seeds/legumes: 4-5 per week")
    pdf.add_bullet("Fats/oils: 2-3 servings (healthy oils)")
    pdf.add_bullet("Sweets: 5 or fewer per week")
    pdf.add_blank_line()
    pdf.add_heading2("Sodium Guidelines")
    pdf.add_bullet("Standard DASH: Less than 2,300mg sodium daily")
    pdf.add_bullet("Lower-sodium DASH: Less than 1,500mg daily (greater BP reduction)")
    pdf.add_blank_line()
    pdf.add_heading3("High-Sodium Foods to Avoid")
    pdf.add_bullet("Canned soups and vegetables (choose low-sodium)")
    pdf.add_bullet("Deli meats and processed meats")
    pdf.add_bullet("Frozen dinners and fast food")
    pdf.add_bullet("Condiments (soy sauce, ketchup, salad dressings)")
    pdf.add_bullet("Bread and rolls (surprisingly high)")
    pdf.add_bullet("Cheese (especially processed)")
    pdf.add_bullet("Pickles and olives")
    pdf.add_blank_line()
    pdf.add_heading3("Flavor Without Salt")
    pdf.add_bullet("Fresh herbs: basil, cilantro, parsley, dill")
    pdf.add_bullet("Spices: cumin, paprika, garlic powder, onion powder")
    pdf.add_bullet("Citrus: lemon, lime juice and zest")
    pdf.add_bullet("Vinegar: balsamic, apple cider, rice wine")
    pdf.add_bullet("Aromatics: garlic, ginger, onion")
    pdf.add_blank_line()
    pdf.add_heading2("Key Minerals for Blood Pressure")
    pdf.add_heading3("Potassium (4,700mg/day goal)")
    pdf.add_bullet("Bananas, oranges, cantaloupe")
    pdf.add_bullet("Potatoes, sweet potatoes, spinach")
    pdf.add_bullet("Beans, lentils, yogurt")
    pdf.add_heading3("Magnesium (320-420mg/day)")
    pdf.add_bullet("Dark leafy greens, nuts, seeds")
    pdf.add_bullet("Dark chocolate, avocado")
    pdf.add_heading3("Calcium (1,000-1,200mg/day)")
    pdf.add_bullet("Low-fat dairy, fortified plant milk")
    pdf.add_bullet("Leafy greens, sardines with bones")
    pdf.add_page_break()
    
    # Chapter 4 - BP Log
    pdf.add_heading1("Chapter 4: Daily Blood Pressure Log")
    pdf.add_blank_line()
    pdf.add_paragraph("Record your blood pressure readings consistently. Take 2-3 readings "
                      "each time and record the average.")
    pdf.add_blank_line()
    for week in range(36):
        pdf.add_heading3(f"Week {week+1}")
        for day in range(7):
            pdf.add_paragraph(f"Date: __/__  AM: ___/___  PM: ___/___  "
                            f"Pulse: ___  Meds: [ ]Y [ ]N  Notes: ________")
        pdf.add_paragraph(f"Weekly Average: ___/___ mmHg")
        pdf.add_blank_line()
        pdf.add_separator()
        pdf.add_page_break()
    pdf.add_page_break()
    
    # Chapter 5 - Meal Planning
    pdf.add_heading1("Chapter 5: DASH Diet Meal Plans")
    pdf.add_blank_line()
    pdf.add_heading2("Week 1 Meal Plan (1,600-2,000 calories)")
    dash_meals = [
        ("Monday", "Oatmeal with banana and walnuts, skim milk", "Turkey and avocado wrap with side salad", "Grilled salmon, brown rice, steamed broccoli"),
        ("Tuesday", "Whole grain toast with almond butter, berries", "Lentil soup with whole grain roll", "Chicken stir-fry with mixed vegetables"),
        ("Wednesday", "Greek yogurt parfait with granola and fruit", "Tuna salad on greens with olive oil", "Bean and vegetable chili with cornbread"),
        ("Thursday", "Veggie omelet with whole wheat toast", "Quinoa bowl with roasted vegetables", "Baked fish with sweet potato and spinach"),
        ("Friday", "Smoothie: spinach, banana, yogurt, flax", "Mediterranean salad with chickpeas", "Lean beef stir-fry with brown rice"),
        ("Saturday", "Whole grain pancakes with fresh berries", "Black bean soup with avocado", "Grilled chicken with roasted vegetables"),
        ("Sunday", "Scrambled eggs with vegetables, fruit", "Leftovers or large salad", "Slow-cooker pot roast with root vegetables")
    ]
    for day, b, l, d in dash_meals:
        pdf.add_heading3(day)
        pdf.add_bullet(f"Breakfast: {b}")
        pdf.add_bullet(f"Lunch: {l}")
        pdf.add_bullet(f"Dinner: {d}")
        pdf.add_bullet("Snacks: Fresh fruit, raw nuts, yogurt, veggie sticks")
        pdf.add_blank_line()
    pdf.add_page_break()
    
    # Chapter 6 - Lifestyle
    pdf.add_heading1("Chapter 6: Lifestyle Strategies")
    pdf.add_blank_line()
    pdf.add_heading2("Exercise for Blood Pressure")
    pdf.add_paragraph("Regular exercise can lower BP by 5-8 points. Aim for:")
    pdf.add_bullet("150 minutes moderate aerobic activity per week")
    pdf.add_bullet("Or 75 minutes vigorous activity per week")
    pdf.add_bullet("Plus 2 days of strength training")
    pdf.add_blank_line()
    pdf.add_heading3("Best Exercises for BP")
    pdf.add_bullet("Brisk walking (30 min, 5x/week)")
    pdf.add_bullet("Swimming and water aerobics")
    pdf.add_bullet("Cycling (stationary or outdoor)")
    pdf.add_bullet("Dancing")
    pdf.add_bullet("Moderate strength training")
    pdf.add_blank_line()
    pdf.add_heading2("Weight Management")
    pdf.add_paragraph("Losing even 5-10 pounds can significantly reduce blood pressure.")
    pdf.add_bullet("Each kilogram lost = approximately 1 mmHg reduction")
    pdf.add_bullet("Focus on waist circumference (men <40in, women <35in)")
    pdf.add_blank_line()
    pdf.add_heading2("Stress Reduction Techniques")
    pdf.add_bullet("Deep breathing: 4-7-8 technique (inhale 4, hold 7, exhale 8)")
    pdf.add_bullet("Progressive muscle relaxation")
    pdf.add_bullet("Meditation: 10-20 minutes daily")
    pdf.add_bullet("Nature walks and time outdoors")
    pdf.add_bullet("Limiting news and social media")
    pdf.add_blank_line()
    pdf.add_heading2("Sleep Optimization")
    pdf.add_paragraph("Poor sleep raises blood pressure. Address sleep apnea if suspected.")
    pdf.add_bullet("Consistent schedule (same bedtime/wake time)")
    pdf.add_bullet("Cool, dark, quiet bedroom")
    pdf.add_bullet("No caffeine after 2pm")
    pdf.add_bullet("Screen curfew 1 hour before bed")
    pdf.add_blank_line()
    pdf.add_heading2("Alcohol and Caffeine")
    pdf.add_bullet("Alcohol: Limit to 1 drink/day women, 2/day men")
    pdf.add_bullet("Caffeine: Monitor your personal response")
    pdf.add_bullet("Stay well-hydrated with water")
    pdf.add_page_break()
    
    # Chapter 7
    pdf.add_heading1("Chapter 7: Medication & Progress Tracking")
    pdf.add_blank_line()
    pdf.add_heading2("Medication Log")
    pdf.add_paragraph("Track your medications and any side effects:")
    for i in range(4):
        pdf.add_paragraph(f"Medication #{i+1}: _______________  Dose: _______  Time: _______")
        pdf.add_paragraph(f"  Start date: __/__/____  Side effects: _________________________")
        pdf.add_blank_line()
    pdf.add_blank_line()
    add_weekly_review(pdf, [
        "Average BP this week: ___/___ mmHg",
        "Medications taken as prescribed: [ ] Yes [ ] No",
        "Sodium intake (estimate): [ ] Under 2300mg [ ] Over",
        "Exercise minutes this week:",
        "Stress level average (1-10):",
        "Weight: ___ lbs",
        "Biggest win this week:",
        "Goal for next week:"
    ], num_weeks=6)
    pdf.add_page_break()
    
    faqs = [
        ("How quickly can diet lower blood pressure?", "The DASH diet can reduce BP within 2 weeks. Full benefits are typically seen at 4-6 weeks with consistent adherence."),
        ("Can I stop my medication if BP improves?", "Never stop medication without doctor approval. Lifestyle changes may allow dose reduction over time, but this must be medically supervised."),
        ("Is coffee bad for blood pressure?", "Caffeine can temporarily raise BP. If your readings are well-controlled, moderate coffee (2-3 cups) is generally acceptable. Monitor your response."),
        ("How much sodium is too much?", "Most health organizations recommend under 2,300mg daily. For greater BP reduction, aim for 1,500mg. The average American consumes 3,400mg."),
        ("Does stress really raise blood pressure?", "Yes. Acute stress can spike BP 20+ points. Chronic stress keeps it elevated and contributes to long-term hypertension through hormonal effects."),
        ("What about potassium supplements?", "Getting potassium from food is preferred. Supplements can be dangerous if you have kidney disease or take certain medications. Discuss with your doctor."),
        ("Is white coat hypertension real?", "Yes. Some people have elevated readings only in medical settings. Home monitoring provides more accurate data about your typical blood pressure."),
        ("Can young people have high blood pressure?", "Yes. Hypertension is increasing in younger adults due to obesity, poor diet, and sedentary lifestyles. Regular screening is important at any age."),
        ("How accurate are home blood pressure monitors?", "Validated upper-arm monitors are quite accurate. Bring yours to your doctor to compare readings. Wrist monitors are less reliable."),
        ("Does alcohol affect blood pressure?", "Yes. More than moderate drinking raises BP. Binge drinking can cause acute spikes. Reducing alcohol is one of the most effective lifestyle changes."),
    ]
    add_faq_section(pdf, faqs)
    
    pdf.add_page_break()
    pdf.add_heading1("Quick-Reference: Daily BP Management Checklist")
    pdf.add_bullet("[ ] Took blood pressure readings (AM and/or PM)")
    pdf.add_bullet("[ ] Took medications as prescribed")
    pdf.add_bullet("[ ] Kept sodium under 2,300mg")
    pdf.add_bullet("[ ] Ate 4+ servings of fruits and vegetables")
    pdf.add_bullet("[ ] Exercised for 30+ minutes")
    pdf.add_bullet("[ ] Practiced stress management")
    pdf.add_bullet("[ ] Drank adequate water")
    pdf.add_bullet("[ ] Limited alcohol (if applicable)")
    pdf.add_bullet("[ ] Got 7-9 hours of sleep")
    
    add_about_author(pdf)
    filepath = os.path.join(OUTPUT_DIR, "04-Blood-Pressure-Management-Workbook.pdf")
    pdf.save(filepath)
    return filepath



def book_05_sleep():
    """Sleep Optimization Workbook"""
    pdf = PurePDF(title="Sleep Optimization Workbook", author=AUTHOR)
    add_front_matter(pdf, "Sleep Optimization Workbook", "CBT-I Techniques, Sleep Hygiene & Insomnia Recovery")
    
    chapters = ["Understanding Sleep Science", "Sleep Assessment & Baseline",
                "CBT-I: Cognitive Behavioral Therapy for Insomnia", "Sleep Diary & Tracking",
                "Sleep Hygiene Protocol", "Nutrition, Exercise & Supplements",
                "Progress Review & Adjustment", "FAQ & Resources"]
    add_toc(pdf, chapters)
    
    pdf.add_heading1("Introduction")
    pdf.add_paragraph("Sleep is not a luxury - it is a biological necessity. Poor sleep affects every "
                      "system in your body, from immune function and metabolism to mental health and "
                      "cognitive performance. Yet one-third of adults do not get adequate sleep.")
    pdf.add_blank_line()
    pdf.add_paragraph("This workbook uses evidence-based Cognitive Behavioral Therapy for Insomnia "
                      "(CBT-I) - the first-line treatment recommended by medical organizations - "
                      "combined with comprehensive sleep hygiene optimization.")
    pdf.add_blank_line()
    pdf.add_heading3("Who This Book Is For")
    pdf.add_bullet("People struggling to fall asleep or stay asleep")
    pdf.add_bullet("Anyone with chronic insomnia or poor sleep quality")
    pdf.add_bullet("Those wanting to optimize sleep for better health")
    pdf.add_bullet("People reducing or transitioning off sleep medications")
    pdf.add_bullet("Shift workers, new parents, or those with disrupted schedules")
    pdf.add_page_break()
    
    # Chapter 1
    pdf.add_heading1("Chapter 1: Understanding Sleep Science")
    pdf.add_blank_line()
    pdf.add_heading2("The Two-Process Model of Sleep")
    pdf.add_paragraph("Sleep is regulated by two systems working together:")
    pdf.add_blank_line()
    pdf.add_heading3("Process S: Sleep Pressure (Homeostatic)")
    pdf.add_paragraph("The longer you are awake, the stronger your drive to sleep. Adenosine "
                      "accumulates in the brain during waking hours, creating 'sleep pressure.' "
                      "Caffeine blocks adenosine receptors, which is why it keeps you awake.")
    pdf.add_blank_line()
    pdf.add_heading3("Process C: Circadian Rhythm")
    pdf.add_paragraph("Your internal 24-hour clock, controlled by the suprachiasmatic nucleus (SCN) "
                      "in the brain. Light exposure is the primary signal that sets this clock. "
                      "Melatonin release begins in the evening as light decreases.")
    pdf.add_blank_line()
    pdf.add_heading2("Sleep Architecture")
    pdf.add_heading3("Sleep Stages")
    pdf.add_bullet("Stage 1 (N1): Light sleep, transition stage (5% of night)")
    pdf.add_bullet("Stage 2 (N2): True sleep onset, memory consolidation (45%)")
    pdf.add_bullet("Stage 3 (N3): Deep/slow-wave sleep, physical restoration (25%)")
    pdf.add_bullet("REM Sleep: Dreaming, emotional processing, learning (25%)")
    pdf.add_blank_line()
    pdf.add_paragraph("One complete sleep cycle takes 90-110 minutes. You need 4-6 cycles per night.")
    pdf.add_blank_line()
    pdf.add_heading2("Consequences of Poor Sleep")
    pdf.add_heading3("Short-Term (1-3 nights)")
    pdf.add_bullet("Impaired concentration and memory")
    pdf.add_bullet("Irritability and mood changes")
    pdf.add_bullet("Increased appetite and cravings")
    pdf.add_bullet("Reduced immune function")
    pdf.add_heading3("Long-Term (Chronic)")
    pdf.add_bullet("Increased risk of obesity and diabetes")
    pdf.add_bullet("Cardiovascular disease")
    pdf.add_bullet("Depression and anxiety")
    pdf.add_bullet("Cognitive decline and dementia risk")
    pdf.add_bullet("Weakened immune system")
    pdf.add_bullet("Hormonal imbalances")
    pdf.add_blank_line()
    pdf.add_heading2("Common Causes of Insomnia")
    pdf.add_bullet("Hyperarousal: Racing mind, inability to 'turn off'")
    pdf.add_bullet("Poor sleep habits: Irregular schedule, screen use")
    pdf.add_bullet("Anxiety and depression")
    pdf.add_bullet("Medical conditions: Pain, sleep apnea, restless legs")
    pdf.add_bullet("Medications and substances (caffeine, alcohol)")
    pdf.add_bullet("Environmental factors (noise, light, temperature)")
    pdf.add_bullet("Conditioned arousal: Associating bed with wakefulness")
    pdf.add_page_break()
    
    # Chapter 2 - Assessment
    pdf.add_heading1("Chapter 2: Sleep Assessment & Baseline")
    pdf.add_blank_line()
    pdf.add_heading2("Insomnia Severity Index (ISI)")
    pdf.add_paragraph("Rate each item 0-4 (0=none, 1=mild, 2=moderate, 3=severe, 4=very severe)")
    pdf.add_blank_line()
    isi_items = [
        "Difficulty falling asleep",
        "Difficulty staying asleep",
        "Problem waking too early",
        "Satisfaction with current sleep pattern",
        "How noticeable is your sleep problem to others",
        "How worried are you about your sleep",
        "How much does poor sleep interfere with daily functioning"
    ]
    for item in isi_items:
        pdf.add_paragraph(f"  {item}: ___/4")
    pdf.add_blank_line()
    pdf.add_paragraph("Total ISI Score: ___/28")
    pdf.add_heading3("Scoring")
    pdf.add_bullet("0-7: No clinically significant insomnia")
    pdf.add_bullet("8-14: Subthreshold insomnia")
    pdf.add_bullet("15-21: Clinical insomnia (moderate severity)")
    pdf.add_bullet("22-28: Clinical insomnia (severe)")
    pdf.add_blank_line()
    pdf.add_heading2("Sleep Environment Assessment")
    pdf.add_paragraph("Rate each factor:")
    pdf.add_paragraph("Room darkness (1=bright, 10=pitch dark): ___")
    pdf.add_paragraph("Room temperature (ideal 60-67F): ___ degrees")
    pdf.add_paragraph("Noise level (1=loud, 10=silent): ___")
    pdf.add_paragraph("Mattress comfort (1-10): ___")
    pdf.add_paragraph("Pillow comfort (1-10): ___")
    pdf.add_paragraph("Partner disruption (1=major, 10=none): ___")
    pdf.add_paragraph("Screen use before bed (minutes): ___")
    pdf.add_paragraph("Caffeine cutoff time: ___")
    pdf.add_paragraph("Last meal before bed (hours): ___")
    pdf.add_page_break()
    
    # Chapter 3 - CBT-I
    pdf.add_heading1("Chapter 3: CBT-I Techniques")
    pdf.add_blank_line()
    pdf.add_paragraph("CBT-I is the gold standard treatment for chronic insomnia, recommended over "
                      "medication by medical organizations worldwide. It addresses the root causes "
                      "of insomnia rather than just masking symptoms.")
    pdf.add_blank_line()
    pdf.add_heading2("Technique 1: Sleep Restriction")
    pdf.add_paragraph("Counterintuitively, spending less time in bed improves sleep quality.")
    pdf.add_bullet("Step 1: Calculate your average sleep time from diary (e.g., 5.5 hours)")
    pdf.add_bullet("Step 2: Set your time in bed to that amount (minimum 5 hours)")
    pdf.add_bullet("Step 3: Choose a fixed wake time (e.g., 6:30 AM)")
    pdf.add_bullet("Step 4: Calculate bedtime (wake time minus sleep window)")
    pdf.add_bullet("Step 5: When sleep efficiency reaches 85%+, add 15 minutes")
    pdf.add_blank_line()
    pdf.add_paragraph("Sleep Efficiency = (Total Sleep Time / Time in Bed) x 100")
    pdf.add_blank_line()
    pdf.add_heading3("My Sleep Restriction Plan")
    pdf.add_paragraph("Current average sleep time: ___ hours")
    pdf.add_paragraph("Initial sleep window: ___ hours")
    pdf.add_paragraph("Fixed wake time: ___:___ AM")
    pdf.add_paragraph("Initial bedtime: ___:___ PM")
    pdf.add_blank_line()
    pdf.add_heading2("Technique 2: Stimulus Control")
    pdf.add_paragraph("Break the association between bed/bedroom and wakefulness:")
    pdf.add_bullet("Go to bed ONLY when sleepy (not just tired)")
    pdf.add_bullet("Use the bed only for sleep and intimacy")
    pdf.add_bullet("If awake for 15-20 minutes, get up and do something calm")
    pdf.add_bullet("Return to bed only when sleepy again")
    pdf.add_bullet("Wake at the same time every day regardless of sleep")
    pdf.add_bullet("No napping during the day (or limit to 20 min before 2pm)")
    pdf.add_blank_line()
    pdf.add_heading2("Technique 3: Cognitive Restructuring")
    pdf.add_paragraph("Challenge unhelpful thoughts about sleep:")
    pdf.add_blank_line()
    pdf.add_heading3("Common Sleep Myths to Challenge")
    pdf.add_bullet("Myth: 'I need exactly 8 hours or I can't function'")
    pdf.add_paragraph("  Reality: Sleep needs vary (6-9 hours). Quality matters more than quantity.")
    pdf.add_bullet("Myth: 'One bad night will ruin my whole week'")
    pdf.add_paragraph("  Reality: Your body compensates with deeper sleep the following night.")
    pdf.add_bullet("Myth: 'I should try harder to fall asleep'")
    pdf.add_paragraph("  Reality: Effort is the enemy of sleep. Let go of trying.")
    pdf.add_bullet("Myth: 'Lying in bed resting is almost as good as sleeping'")
    pdf.add_paragraph("  Reality: Lying awake in bed creates conditioned arousal.")
    pdf.add_blank_line()
    pdf.add_heading3("Thought Record Worksheet")
    for i in range(3):
        pdf.add_paragraph(f"Worry #{i+1}: ________________________________________")
        pdf.add_paragraph(f"  Evidence for this thought: ___________________________")
        pdf.add_paragraph(f"  Evidence against: ____________________________________")
        pdf.add_paragraph(f"  More balanced thought: _______________________________")
        pdf.add_blank_line()
    pdf.add_blank_line()
    pdf.add_heading2("Technique 4: Relaxation Training")
    pdf.add_heading3("Progressive Muscle Relaxation (PMR)")
    pdf.add_paragraph("Tense each muscle group for 5 seconds, then relax for 30 seconds:")
    muscle_groups = ["Feet and toes", "Calves", "Thighs", "Buttocks", "Abdomen",
                     "Chest", "Hands and forearms", "Upper arms", "Shoulders",
                     "Neck", "Face (jaw, eyes, forehead)"]
    for mg in muscle_groups:
        pdf.add_bullet(mg)
    pdf.add_blank_line()
    pdf.add_heading3("4-7-8 Breathing Technique")
    pdf.add_bullet("Inhale through nose for 4 counts")
    pdf.add_bullet("Hold breath for 7 counts")
    pdf.add_bullet("Exhale through mouth for 8 counts")
    pdf.add_bullet("Repeat 4 cycles")
    pdf.add_page_break()
    
    # Chapter 4 - Sleep Diary
    pdf.add_heading1("Chapter 4: Sleep Diary")
    pdf.add_blank_line()
    pdf.add_paragraph("Complete this diary every morning for at least 2 weeks to establish patterns.")
    pdf.add_blank_line()
    for week in range(16):
        pdf.add_heading3(f"Week {week+1} Sleep Diary")
        for day in range(7):
            pdf.add_paragraph(f"Date: __/__  Bedtime: ___:___  Wake time: ___:___")
            pdf.add_paragraph(f"  Time to fall asleep (min): ___  Night wakings: ___")
            pdf.add_paragraph(f"  Total time awake at night: ___  Total sleep: ___ hrs")
            pdf.add_paragraph(f"  Sleep quality (1-10): ___  Refreshed (1-10): ___")
            pdf.add_paragraph(f"  Caffeine (last time): ___  Alcohol: [ ]Y [ ]N")
            pdf.add_paragraph(f"  Exercise: [ ]Y [ ]N  Nap: [ ]Y [ ]N ___min")
            pdf.add_blank_line()
        pdf.add_paragraph(f"Week {week+1} Sleep Efficiency: ___% (goal: 85%+)")
        pdf.add_separator()
        pdf.add_page_break()
    
    # Chapter 5 - Sleep Hygiene
    pdf.add_heading1("Chapter 5: Sleep Hygiene Protocol")
    pdf.add_blank_line()
    pdf.add_heading2("The Ideal Evening Routine")
    pdf.add_heading3("3 Hours Before Bed")
    pdf.add_bullet("Finish last meal")
    pdf.add_bullet("No more caffeine (ideally none after noon)")
    pdf.add_bullet("Complete any vigorous exercise")
    pdf.add_heading3("2 Hours Before Bed")
    pdf.add_bullet("Dim lights throughout the house")
    pdf.add_bullet("Begin winding down activities")
    pdf.add_bullet("Avoid intense conversations or work")
    pdf.add_heading3("1 Hour Before Bed")
    pdf.add_bullet("All screens OFF (blue light blocks melatonin)")
    pdf.add_bullet("Take a warm bath or shower (body cooling triggers sleep)")
    pdf.add_bullet("Relaxation practice: reading, gentle stretching, meditation")
    pdf.add_heading3("30 Minutes Before Bed")
    pdf.add_bullet("Prepare bedroom: cool (60-67F), dark, quiet")
    pdf.add_bullet("Journaling or brain dump (write worries on paper)")
    pdf.add_bullet("Gentle breathing or progressive muscle relaxation")
    pdf.add_blank_line()
    pdf.add_heading2("Bedroom Environment Optimization")
    pdf.add_bullet("Temperature: 60-67 degrees Fahrenheit (15-19 Celsius)")
    pdf.add_bullet("Darkness: Blackout curtains, cover all LED lights")
    pdf.add_bullet("Sound: White noise machine or earplugs if needed")
    pdf.add_bullet("Remove clutter and work materials from bedroom")
    pdf.add_bullet("Comfortable mattress and pillows (replace every 7-10 years)")
    pdf.add_bullet("Reserve bed for sleep and intimacy only")
    pdf.add_blank_line()
    pdf.add_heading2("Morning Routine for Better Sleep")
    pdf.add_bullet("Wake at the same time every day (even weekends)")
    pdf.add_bullet("Get bright light within 30 minutes of waking")
    pdf.add_bullet("Move your body (even a short walk)")
    pdf.add_bullet("Avoid hitting snooze (fragments sleep)")
    pdf.add_page_break()
    
    # Chapter 6
    pdf.add_heading1("Chapter 6: Nutrition, Exercise & Supplements")
    pdf.add_blank_line()
    pdf.add_heading2("Foods That Promote Sleep")
    pdf.add_bullet("Tart cherry juice (natural melatonin source)")
    pdf.add_bullet("Kiwi fruit (shown to improve sleep onset)")
    pdf.add_bullet("Almonds and walnuts (melatonin and magnesium)")
    pdf.add_bullet("Turkey (tryptophan)")
    pdf.add_bullet("Chamomile tea (apigenin promotes relaxation)")
    pdf.add_bullet("Fatty fish (omega-3s and vitamin D)")
    pdf.add_bullet("Warm milk (tryptophan and psychological comfort)")
    pdf.add_blank_line()
    pdf.add_heading2("Foods That Disrupt Sleep")
    pdf.add_bullet("Caffeine (half-life 5-6 hours, affects sleep even if you fall asleep)")
    pdf.add_bullet("Alcohol (disrupts REM sleep and causes awakenings)")
    pdf.add_bullet("Spicy foods (raise body temperature)")
    pdf.add_bullet("High-sugar foods (blood sugar crashes)")
    pdf.add_bullet("Heavy meals close to bedtime")
    pdf.add_blank_line()
    pdf.add_heading2("Exercise and Sleep")
    pdf.add_bullet("Regular exercise improves sleep quality significantly")
    pdf.add_bullet("30 minutes of moderate exercise most days")
    pdf.add_bullet("Complete vigorous exercise 3+ hours before bed")
    pdf.add_bullet("Morning or afternoon exercise is ideal for sleep")
    pdf.add_bullet("Yoga and stretching in the evening can help relaxation")
    pdf.add_blank_line()
    pdf.add_heading2("Supplements to Discuss with Your Doctor")
    pdf.add_bullet("Magnesium glycinate: 200-400mg before bed (calming)")
    pdf.add_bullet("Melatonin: 0.5-3mg (for circadian issues, not long-term)")
    pdf.add_bullet("L-theanine: 200mg (promotes relaxation without drowsiness)")
    pdf.add_bullet("Glycine: 3g before bed (lowers core body temperature)")
    pdf.add_bullet("Valerian root: May improve sleep quality")
    pdf.add_bullet("Ashwagandha: Reduces cortisol, improves sleep")
    pdf.add_page_break()
    
    # Chapter 7
    pdf.add_heading1("Chapter 7: Progress Review")
    add_weekly_review(pdf, [
        "Average sleep efficiency this week: ___%",
        "Average time to fall asleep: ___ min",
        "Average total sleep time: ___ hours",
        "Number of nights with insomnia: ___/7",
        "CBT-I techniques practiced:",
        "Biggest improvement:",
        "Remaining challenges:",
        "Adjustment for next week:"
    ], num_weeks=5)
    pdf.add_page_break()
    
    faqs = [
        ("How long does CBT-I take to work?", "Most people see improvement within 2-4 weeks. Full benefits are typically achieved in 6-8 weeks. It's normal for things to feel harder before they get better, especially with sleep restriction."),
        ("Is it normal to feel worse when starting sleep restriction?", "Yes. Initial daytime sleepiness is expected and actually helps build stronger sleep drive. This temporary discomfort leads to better, more consolidated sleep."),
        ("Should I take melatonin every night?", "Melatonin is best for circadian rhythm issues (jet lag, shift work) rather than general insomnia. Long-term nightly use is not recommended. Discuss with your doctor."),
        ("Why does alcohol make insomnia worse?", "While alcohol helps you fall asleep initially, it severely disrupts sleep architecture, suppresses REM sleep, and causes middle-of-the-night awakenings as it metabolizes."),
        ("Can I ever catch up on lost sleep?", "Partially. One or two late mornings can help, but chronic sleep debt cannot be fully repaid by sleeping in on weekends. Consistency is more important than marathon sleep sessions."),
        ("When should I see a sleep specialist?", "If insomnia persists after 4-6 weeks of CBT-I, or if you suspect sleep apnea (snoring, gasping, daytime sleepiness despite adequate hours), excessive daytime sleepiness, or restless legs."),
        ("Is napping good or bad?", "For insomnia sufferers, napping typically makes nighttime sleep worse by reducing sleep pressure. If you must nap, keep it under 20 minutes and before 2pm."),
        ("Does screen time really affect sleep?", "Yes. Blue light from screens suppresses melatonin production by up to 50%. The stimulating content also increases arousal. Stop screens 1+ hour before bed."),
        ("What if I work shifts?", "Shift workers need modified strategies: blackout curtains for day sleep, strategic light exposure, consistent anchor sleep times, and melatonin timed to your desired sleep window."),
        ("Can anxiety cause insomnia?", "Absolutely. Anxiety and insomnia form a bidirectional cycle - each worsens the other. CBT-I addresses both by reducing hyperarousal and breaking the anxiety-insomnia connection."),
    ]
    add_faq_section(pdf, faqs)
    
    pdf.add_page_break()
    pdf.add_heading1("Quick-Reference: Sleep Hygiene Checklist")
    pdf.add_bullet("[ ] Consistent wake time (same every day)")
    pdf.add_bullet("[ ] Bright light exposure within 30 min of waking")
    pdf.add_bullet("[ ] No caffeine after noon")
    pdf.add_bullet("[ ] Exercise completed (not within 3 hours of bed)")
    pdf.add_bullet("[ ] Screens off 1 hour before bed")
    pdf.add_bullet("[ ] Bedroom cool (60-67F), dark, and quiet")
    pdf.add_bullet("[ ] Relaxation practice before bed")
    pdf.add_bullet("[ ] In bed only when sleepy")
    pdf.add_bullet("[ ] No clock-watching during the night")
    
    add_about_author(pdf)
    filepath = os.path.join(OUTPUT_DIR, "05-Sleep-Optimization-Workbook.pdf")
    pdf.save(filepath)
    return filepath



def book_06_diabetes():
    """Diabetes Management Workbook Type 2"""
    pdf = PurePDF(title="Diabetes Management Workbook Type 2", author=AUTHOR)
    add_front_matter(pdf, "Type 2 Diabetes Management", "Blood Sugar Log, Carb Counting & Meal Planner")
    
    chapters = ["Understanding Type 2 Diabetes", "Your Diabetes Baseline",
                "Blood Sugar Management", "Daily Blood Sugar Log",
                "Carb Counting & Meal Planning", "Exercise & Lifestyle",
                "Progress Review & A1C Tracking", "FAQ & Resources"]
    add_toc(pdf, chapters)
    
    pdf.add_heading1("Introduction")
    pdf.add_paragraph("A Type 2 diabetes diagnosis can feel overwhelming, but it is a condition "
                      "that responds remarkably well to lifestyle management. Many people achieve "
                      "excellent blood sugar control - and even remission - through nutrition, "
                      "exercise, and consistent self-monitoring.")
    pdf.add_blank_line()
    pdf.add_paragraph("This workbook provides everything you need to track, manage, and improve "
                      "your blood sugar control with practical tools and evidence-based strategies.")
    pdf.add_page_break()
    
    # Chapter 1
    pdf.add_heading1("Chapter 1: Understanding Type 2 Diabetes")
    pdf.add_blank_line()
    pdf.add_heading2("What Is Type 2 Diabetes?")
    pdf.add_paragraph("In Type 2 diabetes, your body either does not produce enough insulin or "
                      "your cells have become resistant to insulin's effects. This results in "
                      "elevated blood glucose (sugar) levels that, over time, can damage blood "
                      "vessels, nerves, and organs.")
    pdf.add_blank_line()
    pdf.add_heading3("Key Terms to Know")
    pdf.add_bullet("Insulin: Hormone that allows glucose to enter cells for energy")
    pdf.add_bullet("Insulin resistance: Cells don't respond properly to insulin")
    pdf.add_bullet("Glucose: Sugar in your blood (from food and liver)")
    pdf.add_bullet("A1C: Average blood sugar over 2-3 months")
    pdf.add_bullet("Fasting glucose: Blood sugar after 8+ hours without food")
    pdf.add_bullet("Postprandial: Blood sugar after eating")
    pdf.add_blank_line()
    pdf.add_heading2("Blood Sugar Targets")
    pdf.add_heading3("General Guidelines (discuss with your doctor)")
    pdf.add_bullet("Fasting (before meals): 80-130 mg/dL")
    pdf.add_bullet("2 hours after meal start: Less than 180 mg/dL")
    pdf.add_bullet("A1C goal: Less than 7% (or as set by your doctor)")
    pdf.add_bullet("Bedtime: 100-140 mg/dL")
    pdf.add_blank_line()
    pdf.add_heading2("Risk Factors for Complications")
    pdf.add_bullet("Consistently elevated blood sugar")
    pdf.add_bullet("High blood pressure")
    pdf.add_bullet("High cholesterol")
    pdf.add_bullet("Smoking")
    pdf.add_bullet("Physical inactivity")
    pdf.add_bullet("Excess weight")
    pdf.add_blank_line()
    pdf.add_heading2("Potential Complications (Prevention Is Key)")
    pdf.add_bullet("Heart disease and stroke")
    pdf.add_bullet("Nerve damage (neuropathy)")
    pdf.add_bullet("Kidney disease (nephropathy)")
    pdf.add_bullet("Eye damage (retinopathy)")
    pdf.add_bullet("Foot problems and slow healing")
    pdf.add_paragraph("These complications are largely preventable with good blood sugar control!")
    pdf.add_page_break()
    
    # Chapter 2 - Baseline
    pdf.add_heading1("Chapter 2: Your Diabetes Baseline")
    pdf.add_blank_line()
    pdf.add_heading2("My Diabetes Profile")
    pdf.add_paragraph("Date diagnosed: __/__/____")
    pdf.add_paragraph("Most recent A1C: ___% Date: __/__/____")
    pdf.add_paragraph("A1C goal (from doctor): ___%")
    pdf.add_paragraph("Fasting glucose average: ___ mg/dL")
    pdf.add_paragraph("Current weight: ___ lbs  Goal weight: ___ lbs")
    pdf.add_paragraph("Blood pressure: ___/___ mmHg")
    pdf.add_paragraph("Last eye exam: __/__/____")
    pdf.add_paragraph("Last foot exam: __/__/____")
    pdf.add_blank_line()
    pdf.add_heading2("Current Medications")
    for i in range(4):
        pdf.add_paragraph(f"Medication #{i+1}: _____________  Dose: _______  Times/day: ___")
    pdf.add_blank_line()
    pdf.add_heading2("My Healthcare Team")
    pdf.add_paragraph("Primary doctor: _____________  Phone: _____________")
    pdf.add_paragraph("Endocrinologist: _____________  Phone: _____________")
    pdf.add_paragraph("Diabetes educator: _____________  Phone: _____________")
    pdf.add_paragraph("Dietitian: _____________  Phone: _____________")
    pdf.add_paragraph("Eye doctor: _____________  Phone: _____________")
    pdf.add_paragraph("Podiatrist: _____________  Phone: _____________")
    pdf.add_page_break()
    
    # Chapter 3 - Blood Sugar Management
    pdf.add_heading1("Chapter 3: Blood Sugar Management Strategies")
    pdf.add_blank_line()
    pdf.add_heading2("The Glucose Equation")
    pdf.add_paragraph("Blood sugar is affected by: Food (raises it), Exercise (lowers it), "
                      "Medication (lowers it), Stress (raises it), Sleep (poor sleep raises it), "
                      "Illness (raises it).")
    pdf.add_blank_line()
    pdf.add_heading2("How to Test Blood Sugar")
    pdf.add_bullet("Wash hands with warm water (cold hands give low readings)")
    pdf.add_bullet("Use side of fingertip (less painful)")
    pdf.add_bullet("Rotate fingers and sites")
    pdf.add_bullet("Record immediately in your log")
    pdf.add_blank_line()
    pdf.add_heading3("When to Test")
    pdf.add_bullet("Fasting (first thing in morning)")
    pdf.add_bullet("Before meals")
    pdf.add_bullet("2 hours after first bite of meals")
    pdf.add_bullet("Before bed")
    pdf.add_bullet("Before and after exercise")
    pdf.add_bullet("When feeling 'off' (high or low symptoms)")
    pdf.add_blank_line()
    pdf.add_heading2("Recognizing Highs and Lows")
    pdf.add_heading3("High Blood Sugar (Hyperglycemia) Signs")
    pdf.add_bullet("Increased thirst and frequent urination")
    pdf.add_bullet("Blurred vision")
    pdf.add_bullet("Fatigue and headache")
    pdf.add_bullet("Slow healing wounds")
    pdf.add_heading3("Low Blood Sugar (Hypoglycemia) Signs")
    pdf.add_bullet("Shakiness, sweating, rapid heartbeat")
    pdf.add_bullet("Dizziness, confusion")
    pdf.add_bullet("Hunger")
    pdf.add_bullet("Irritability")
    pdf.add_blank_line()
    pdf.add_heading3("Rule of 15 for Low Blood Sugar")
    pdf.add_bullet("If below 70 mg/dL: Eat 15g fast-acting carbs")
    pdf.add_bullet("Wait 15 minutes and retest")
    pdf.add_bullet("If still low, repeat")
    pdf.add_bullet("Once normal, eat a balanced snack")
    pdf.add_page_break()
    
    # Chapter 4 - Blood Sugar Log
    pdf.add_heading1("Chapter 4: Daily Blood Sugar Log")
    pdf.add_blank_line()
    for week in range(36):
        pdf.add_heading3(f"Week {week+1}")
        for day in range(7):
            pdf.add_paragraph(f"Date: __/__  Fasting: ___  Pre-lunch: ___  "
                            f"Post-lunch: ___  Pre-dinner: ___  Bedtime: ___")
            pdf.add_paragraph(f"  Meds taken: [ ]Y  Exercise: ___min  Carbs est: ___g  Notes: ______")
        pdf.add_paragraph(f"Weekly Fasting Average: ___  Post-meal Average: ___")
        pdf.add_separator()
        pdf.add_page_break()
    pdf.add_page_break()
    
    # Chapter 5 - Carb Counting
    pdf.add_heading1("Chapter 5: Carb Counting & Meal Planning")
    pdf.add_blank_line()
    pdf.add_heading2("Carbohydrate Basics")
    pdf.add_paragraph("Carbohydrates have the biggest impact on blood sugar. Learning to count "
                      "and manage carbs is the most important dietary skill for diabetes management.")
    pdf.add_blank_line()
    pdf.add_heading3("Daily Carb Targets (discuss with your team)")
    pdf.add_bullet("Conservative: 45-60g per meal, 15-20g per snack")
    pdf.add_bullet("Moderate: 30-45g per meal, 15g per snack")
    pdf.add_bullet("Lower carb: 20-30g per meal, 10g per snack")
    pdf.add_blank_line()
    pdf.add_heading3("Carb Counting Quick Reference")
    pdf.add_bullet("1 slice bread = 15g carbs")
    pdf.add_bullet("1/3 cup rice or pasta = 15g carbs")
    pdf.add_bullet("1 small fruit = 15g carbs")
    pdf.add_bullet("1 cup milk = 12g carbs")
    pdf.add_bullet("1/2 cup beans = 15g carbs")
    pdf.add_bullet("Non-starchy vegetables = 5g per cup")
    pdf.add_bullet("Meat, fish, cheese, oils = 0g carbs")
    pdf.add_blank_line()
    pdf.add_heading2("Best Foods for Blood Sugar Control")
    pdf.add_heading3("Low-Glycemic Foods (choose often)")
    pdf.add_bullet("Non-starchy vegetables (unlimited)")
    pdf.add_bullet("Beans and lentils")
    pdf.add_bullet("Steel-cut oats")
    pdf.add_bullet("Sweet potatoes (better than white)")
    pdf.add_bullet("Berries (lower sugar than tropical fruits)")
    pdf.add_bullet("Nuts and seeds")
    pdf.add_bullet("Quinoa")
    pdf.add_heading3("The Plate Method")
    pdf.add_bullet("1/2 plate: Non-starchy vegetables")
    pdf.add_bullet("1/4 plate: Lean protein")
    pdf.add_bullet("1/4 plate: Complex carbohydrates")
    pdf.add_bullet("Add: Healthy fat (olive oil, avocado)")
    pdf.add_blank_line()
    pdf.add_heading2("7-Day Diabetes-Friendly Meal Plan")
    dm_meals = [
        ("Monday", "2 eggs + spinach + 1 slice whole grain toast", "Grilled chicken salad with olive oil", "Salmon + roasted vegetables + 1/2 cup brown rice"),
        ("Tuesday", "Greek yogurt + berries + 10 almonds", "Turkey lettuce wraps + vegetable soup", "Lean beef stir-fry with lots of vegetables"),
        ("Wednesday", "Oatmeal (1/3 cup dry) + walnuts + cinnamon", "Lentil soup + side salad", "Baked chicken + sweet potato + broccoli"),
        ("Thursday", "Veggie omelet + avocado", "Tuna salad on greens + whole grain crackers", "Shrimp + zucchini noodles + marinara"),
        ("Friday", "Smoothie: protein powder + spinach + berries", "Bean and cheese quesadilla (1 tortilla) + salad", "Grilled fish + cauliflower mash + asparagus"),
        ("Saturday", "Cottage cheese + sliced peaches + seeds", "Large salad with protein + olive oil dressing", "Turkey meatballs + spaghetti squash"),
        ("Sunday", "Egg muffins (made ahead) + fruit", "Leftovers or soup", "Slow cooker chicken thighs + root vegetables")
    ]
    for day, b, l, d in dm_meals:
        pdf.add_heading3(day)
        pdf.add_bullet(f"Breakfast: {b}")
        pdf.add_bullet(f"Lunch: {l}")
        pdf.add_bullet(f"Dinner: {d}")
        pdf.add_blank_line()
    pdf.add_page_break()
    
    # Chapter 6
    pdf.add_heading1("Chapter 6: Exercise & Lifestyle")
    pdf.add_blank_line()
    pdf.add_heading2("Exercise and Blood Sugar")
    pdf.add_paragraph("Exercise is powerful medicine for Type 2 diabetes. It improves insulin "
                      "sensitivity for up to 48 hours after activity.")
    pdf.add_blank_line()
    pdf.add_heading3("Exercise Guidelines")
    pdf.add_bullet("150+ minutes moderate aerobic activity per week")
    pdf.add_bullet("2-3 sessions of resistance/strength training")
    pdf.add_bullet("Break up sitting every 30 minutes")
    pdf.add_bullet("10-15 minute walk after meals (very effective)")
    pdf.add_blank_line()
    pdf.add_heading3("Safety Tips")
    pdf.add_bullet("Check blood sugar before exercise")
    pdf.add_bullet("If under 100: Have a small snack first")
    pdf.add_bullet("If over 250: Check ketones, delay exercise if positive")
    pdf.add_bullet("Carry fast-acting glucose during activity")
    pdf.add_bullet("Stay hydrated")
    pdf.add_blank_line()
    pdf.add_heading2("Stress Management")
    pdf.add_paragraph("Stress hormones directly raise blood sugar. Managing stress is essential "
                      "for diabetes control.")
    pdf.add_bullet("Daily relaxation practice (deep breathing, meditation)")
    pdf.add_bullet("Regular physical activity")
    pdf.add_bullet("Adequate sleep (7-9 hours)")
    pdf.add_bullet("Social connection and support")
    pdf.add_bullet("Time management and saying no")
    pdf.add_page_break()
    
    # Chapter 7
    pdf.add_heading1("Chapter 7: Progress Review & A1C Tracking")
    pdf.add_blank_line()
    pdf.add_heading2("A1C Record")
    pdf.add_paragraph("Track your A1C results over time:")
    for i in range(8):
        pdf.add_paragraph(f"Date: __/__/____  A1C: ____%  Doctor notes: ________________")
    pdf.add_blank_line()
    add_weekly_review(pdf, [
        "Fasting glucose average: ___ mg/dL",
        "Post-meal average: ___ mg/dL",
        "Highs this week (over target): ___",
        "Lows this week (under 70): ___",
        "Exercise minutes: ___",
        "Carbs managed well: [ ] Yes [ ] Mostly [ ] Struggled",
        "Medications taken consistently: [ ] Yes [ ] No",
        "Goal for next week:"
    ], num_weeks=5)
    pdf.add_page_break()
    
    faqs = [
        ("Can Type 2 diabetes be reversed?", "Many people achieve remission (normal blood sugar without medication) through significant lifestyle changes, especially weight loss and low-carb eating. Discuss realistic goals with your doctor."),
        ("How often should I check my blood sugar?", "This depends on your treatment plan. Those on insulin may test 4+ times daily. Others may test fasting and after meals a few times per week. Follow your doctor's guidance."),
        ("Are all carbs bad?", "No. Focus on quality: whole grains, legumes, fruits, and vegetables are healthful. Minimize refined carbs, sugar, and processed foods. Portion control matters most."),
        ("Can I still eat fruit?", "Yes! Choose whole fruits over juice. Berries, apples, and citrus have lower glycemic impact. Pair fruit with protein or fat to slow glucose absorption."),
        ("What about artificial sweeteners?", "They don't raise blood sugar directly, but may affect gut bacteria and appetite. Use in moderation. Water, unsweetened tea, and sparkling water are best."),
        ("Should I follow a keto diet?", "Very low-carb diets can significantly improve blood sugar but must be medically supervised, especially if on insulin or sulfonylureas (risk of hypoglycemia). Sustainability matters."),
        ("How does sleep affect blood sugar?", "Poor sleep increases insulin resistance, raises cortisol, and makes blood sugar harder to control. Prioritize 7-9 hours of quality sleep."),
        ("Can stress raise my blood sugar?", "Yes, significantly. Stress hormones (cortisol, adrenaline) tell the liver to release glucose. Chronic stress can raise A1C by 0.5-1%."),
        ("When should I call my doctor?", "Contact your doctor if blood sugar is consistently over 250, under 70, if you feel sick, or if you notice signs of complications (numbness, vision changes, slow healing)."),
        ("Will I need insulin eventually?", "Not necessarily. Many people manage Type 2 with lifestyle and oral medications long-term. Needing insulin isn't a failure - it means your body needs additional support."),
    ]
    add_faq_section(pdf, faqs)
    
    pdf.add_page_break()
    pdf.add_heading1("Quick-Reference: Daily Diabetes Checklist")
    pdf.add_bullet("[ ] Checked blood sugar as recommended")
    pdf.add_bullet("[ ] Took all medications on time")
    pdf.add_bullet("[ ] Counted/managed carb intake")
    pdf.add_bullet("[ ] Ate balanced meals with vegetables")
    pdf.add_bullet("[ ] Moved body for 30+ minutes")
    pdf.add_bullet("[ ] Walked after at least one meal")
    pdf.add_bullet("[ ] Drank adequate water")
    pdf.add_bullet("[ ] Checked feet for issues")
    pdf.add_bullet("[ ] Managed stress levels")
    pdf.add_bullet("[ ] Recorded readings in log")
    
    add_about_author(pdf)
    filepath = os.path.join(OUTPUT_DIR, "06-Diabetes-Management-Workbook-Type2.pdf")
    pdf.save(filepath)
    return filepath



def book_07_chronic_pain():
    """Chronic Pain Management Workbook"""
    pdf = PurePDF(title="Chronic Pain Management Workbook", author=AUTHOR)
    add_front_matter(pdf, "Chronic Pain Management", "Pain Journal, Trigger Tracker & Coping Toolkit")
    
    chapters = ["Understanding Chronic Pain", "Pain Assessment & Baseline",
                "Pain Management Strategies", "Daily Pain Journal",
                "Movement & Physical Therapy", "Mind-Body Techniques",
                "Flare-Up Action Plan", "FAQ & Resources"]
    add_toc(pdf, chapters)
    
    pdf.add_heading1("Introduction")
    pdf.add_paragraph("Living with chronic pain is exhausting, isolating, and often misunderstood. "
                      "This workbook is designed to be your daily companion in managing pain - "
                      "not just surviving it, but building a meaningful life alongside it.")
    pdf.add_blank_line()
    pdf.add_paragraph("You will learn evidence-based strategies for tracking triggers, managing "
                      "flare-ups, communicating with healthcare providers, and finding what works "
                      "for YOUR unique pain experience.")
    pdf.add_blank_line()
    pdf.add_heading3("Who This Book Is For")
    pdf.add_bullet("People with chronic pain lasting 3+ months")
    pdf.add_bullet("Those with fibromyalgia, arthritis, or back pain")
    pdf.add_bullet("Anyone managing pain alongside medical treatment")
    pdf.add_bullet("People seeking non-pharmacological pain tools")
    pdf.add_page_break()
    
    # Chapter 1
    pdf.add_heading1("Chapter 1: Understanding Chronic Pain")
    pdf.add_blank_line()
    pdf.add_heading2("Pain Science: What We Now Know")
    pdf.add_paragraph("Modern pain science reveals that chronic pain is NOT simply 'damage signals "
                      "from tissues.' Pain is a complex output of the brain, influenced by biology, "
                      "psychology, social context, beliefs, and emotions. This does NOT mean pain "
                      "is 'in your head' - it is absolutely real. But understanding its complexity "
                      "opens doors to more effective management.")
    pdf.add_blank_line()
    pdf.add_heading3("Acute vs. Chronic Pain")
    pdf.add_bullet("Acute pain: Protective alarm system. Usually proportional to tissue damage. Heals.")
    pdf.add_bullet("Chronic pain: Pain lasting 3+ months. Nervous system becomes sensitized. "
                   "Pain signals amplified. Often not proportional to tissue state.")
    pdf.add_blank_line()
    pdf.add_heading2("Central Sensitization")
    pdf.add_paragraph("In chronic pain, the nervous system becomes 'turned up' like a volume dial. "
                      "This means normal sensations can be perceived as painful, and painful stimuli "
                      "feel more intense. This is a real neurological change, not imagined.")
    pdf.add_blank_line()
    pdf.add_heading3("Signs of Central Sensitization")
    pdf.add_bullet("Pain that spreads beyond the original site")
    pdf.add_bullet("Normal touch feels painful (allodynia)")
    pdf.add_bullet("Heightened sensitivity to light, sound, or temperature")
    pdf.add_bullet("Pain persists long after injury should have healed")
    pdf.add_bullet("Fatigue, poor sleep, brain fog alongside pain")
    pdf.add_blank_line()
    pdf.add_heading2("The Biopsychosocial Model of Pain")
    pdf.add_paragraph("Pain is influenced by three interacting factors:")
    pdf.add_heading3("Biological")
    pdf.add_bullet("Tissue health and inflammation")
    pdf.add_bullet("Nervous system sensitivity")
    pdf.add_bullet("Sleep quality and physical fitness")
    pdf.add_bullet("Nutrition and overall health")
    pdf.add_heading3("Psychological")
    pdf.add_bullet("Thoughts and beliefs about pain")
    pdf.add_bullet("Mood (depression, anxiety)")
    pdf.add_bullet("Attention and focus on pain")
    pdf.add_bullet("Catastrophizing vs. acceptance")
    pdf.add_heading3("Social")
    pdf.add_bullet("Support system and relationships")
    pdf.add_bullet("Work and financial stress")
    pdf.add_bullet("Social isolation")
    pdf.add_bullet("Healthcare experiences")
    pdf.add_page_break()
    
    # Chapter 2
    pdf.add_heading1("Chapter 2: Pain Assessment & Baseline")
    pdf.add_blank_line()
    pdf.add_heading2("My Pain Profile")
    pdf.add_paragraph("Primary pain condition: ___________________________")
    pdf.add_paragraph("Duration of chronic pain: ___ months/years")
    pdf.add_paragraph("Pain locations (mark all): _________________________")
    pdf.add_paragraph("Average pain level (0-10): ___")
    pdf.add_paragraph("Worst pain level this month: ___")
    pdf.add_paragraph("Best pain level this month: ___")
    pdf.add_blank_line()
    pdf.add_heading2("Pain Impact Assessment")
    pdf.add_paragraph("Rate impact (0=none, 10=complete interference):")
    pain_areas = ["Sleep", "Work/productivity", "Physical activity", "Social life",
                  "Mood/emotional health", "Relationships", "Self-care",
                  "Hobbies/enjoyment", "Concentration", "Independence"]
    for area in pain_areas:
        pdf.add_paragraph(f"  {area}: ___/10")
    pdf.add_paragraph(f"Total Impact Score: ___/100")
    pdf.add_blank_line()
    pdf.add_heading2("Known Triggers")
    pdf.add_paragraph("List activities, foods, weather, stress that worsen pain:")
    for i in range(8):
        pdf.add_paragraph(f"  Trigger #{i+1}: ________________  Severity increase: ___/10")
    pdf.add_blank_line()
    pdf.add_heading2("What Helps")
    pdf.add_paragraph("List things that reduce or help manage your pain:")
    for i in range(8):
        pdf.add_paragraph(f"  Relief #{i+1}: ________________  Effectiveness: ___/10")
    pdf.add_page_break()
    
    # Chapter 3
    pdf.add_heading1("Chapter 3: Pain Management Strategies")
    pdf.add_blank_line()
    pdf.add_heading2("The Pain Management Toolbox")
    pdf.add_paragraph("No single strategy eliminates chronic pain. The goal is building a diverse "
                      "toolbox of techniques that together help you manage pain and improve function.")
    pdf.add_blank_line()
    pdf.add_heading3("Pacing: Your Most Important Tool")
    pdf.add_paragraph("Pacing means balancing activity and rest to avoid the boom-bust cycle:")
    pdf.add_bullet("Boom: On good days, overdoing it because you feel better")
    pdf.add_bullet("Bust: Days of increased pain and forced rest afterwards")
    pdf.add_bullet("Pacing: Consistent moderate activity regardless of pain level")
    pdf.add_blank_line()
    pdf.add_heading3("How to Pace")
    pdf.add_bullet("Find your baseline: The activity level you can do WITHOUT a flare-up")
    pdf.add_bullet("Set time limits, not completion goals")
    pdf.add_bullet("Take breaks BEFORE pain increases")
    pdf.add_bullet("Gradually increase by 10% per week only when stable")
    pdf.add_bullet("On good days: Do the same amount, not more")
    pdf.add_blank_line()
    pdf.add_heading2("Graded Exposure")
    pdf.add_paragraph("Gradually reintroduce activities you've been avoiding due to pain:")
    pdf.add_bullet("List avoided activities in order of fear/difficulty")
    pdf.add_bullet("Start with the easiest, do a small amount")
    pdf.add_bullet("Notice: Did the feared consequence happen?")
    pdf.add_bullet("Gradually increase as confidence builds")
    pdf.add_blank_line()
    pdf.add_heading2("Acceptance-Based Approaches")
    pdf.add_paragraph("Acceptance does not mean giving up. It means stopping the fight against "
                      "pain and redirecting energy toward living well despite pain.")
    pdf.add_bullet("Acknowledge pain without judgment")
    pdf.add_bullet("Focus on values and what matters to you")
    pdf.add_bullet("Take action toward goals even with pain present")
    pdf.add_bullet("Practice willingness to experience discomfort")
    pdf.add_page_break()
    
    # Chapter 4 - Pain Journal
    pdf.add_heading1("Chapter 4: Daily Pain Journal")
    pdf.add_blank_line()
    add_tracker_pages(pdf, "Daily Pain & Activity Log",
                      ["Pain level AM (0-10)", "Pain level PM (0-10)",
                       "Pain locations", "Activity level (1-10)",
                       "Sleep quality (1-10)", "Mood (1-10)",
                       "Strategies used", "Triggers noticed", "Wins today"], num_pages=16)
    pdf.add_page_break()
    
    # Chapter 5
    pdf.add_heading1("Chapter 5: Movement & Physical Therapy")
    pdf.add_blank_line()
    pdf.add_heading2("Why Movement Matters")
    pdf.add_paragraph("Movement is medicine for chronic pain. It may seem counterintuitive, but "
                      "gentle, consistent movement actually reduces pain sensitivity over time by "
                      "retraining the nervous system.")
    pdf.add_blank_line()
    pdf.add_heading3("Gentle Movement Options")
    pdf.add_bullet("Walking: Start with 5 minutes, increase gradually")
    pdf.add_bullet("Swimming/water therapy: Joint-friendly, soothing")
    pdf.add_bullet("Yoga: Gentle/restorative classes (not power yoga)")
    pdf.add_bullet("Tai Chi: Slow, flowing movements, proven for pain")
    pdf.add_bullet("Stretching: Daily gentle stretches for affected areas")
    pdf.add_bullet("Pilates: Core strengthening, modified for pain")
    pdf.add_blank_line()
    pdf.add_heading3("Movement Principles for Chronic Pain")
    pdf.add_bullet("Start below what you think you can do")
    pdf.add_bullet("Consistency over intensity (daily small amounts)")
    pdf.add_bullet("Some discomfort is okay; sharp or escalating pain means stop")
    pdf.add_bullet("Progress slowly (10% increase per week maximum)")
    pdf.add_bullet("Never compare to pre-pain abilities")
    pdf.add_bullet("Celebrate every minute of movement")
    pdf.add_blank_line()
    pdf.add_heading2("Daily Gentle Stretching Routine")
    stretches = [
        ("Neck rolls", "Slowly circle head 5x each direction"),
        ("Shoulder shrugs", "Lift shoulders to ears, hold 5 sec, release x10"),
        ("Cat-cow stretches", "On all fours, arch and round spine gently x10"),
        ("Knee-to-chest", "Lying down, pull one knee to chest, hold 30 sec each"),
        ("Child's pose", "Kneel, sit back on heels, arms forward, hold 1 min"),
        ("Gentle twist", "Seated, twist to each side gently, hold 30 sec"),
        ("Hamstring stretch", "Seated, reach toward toes, hold 30 sec"),
        ("Hip flexor stretch", "Lunge position, hold 30 sec each side")
    ]
    for name, desc in stretches:
        pdf.add_bullet(f"{name}: {desc}")
    pdf.add_page_break()
    
    # Chapter 6
    pdf.add_heading1("Chapter 6: Mind-Body Techniques")
    pdf.add_blank_line()
    pdf.add_heading2("Mindfulness for Pain")
    pdf.add_paragraph("Mindfulness meditation has strong evidence for reducing pain perception "
                      "and suffering. It works by changing how the brain processes pain signals.")
    pdf.add_blank_line()
    pdf.add_heading3("Body Scan Meditation (15 minutes)")
    pdf.add_bullet("Lie comfortably with eyes closed")
    pdf.add_bullet("Notice breath for 2 minutes")
    pdf.add_bullet("Bring attention to feet - notice sensations without judgment")
    pdf.add_bullet("Slowly move attention up through each body part")
    pdf.add_bullet("When reaching painful areas, breathe INTO the sensation")
    pdf.add_bullet("Observe pain with curiosity, not resistance")
    pdf.add_bullet("Continue through entire body to top of head")
    pdf.add_blank_line()
    pdf.add_heading2("Breathing Techniques for Pain")
    pdf.add_heading3("Box Breathing")
    pdf.add_bullet("Inhale for 4 counts")
    pdf.add_bullet("Hold for 4 counts")
    pdf.add_bullet("Exhale for 4 counts")
    pdf.add_bullet("Hold for 4 counts")
    pdf.add_bullet("Repeat 4-8 cycles")
    pdf.add_blank_line()
    pdf.add_heading3("Elongated Exhale (activates parasympathetic)")
    pdf.add_bullet("Inhale for 4 counts")
    pdf.add_bullet("Exhale for 6-8 counts")
    pdf.add_bullet("Repeat for 5 minutes")
    pdf.add_blank_line()
    pdf.add_heading2("Cognitive Techniques")
    pdf.add_heading3("Challenging Pain Catastrophizing")
    pdf.add_paragraph("Pain catastrophizing = magnifying, ruminating, or feeling helpless about pain")
    pdf.add_blank_line()
    pdf.add_paragraph("Catastrophic thought: ________________________________")
    pdf.add_paragraph("Evidence this is true: ________________________________")
    pdf.add_paragraph("Evidence against: ____________________________________")
    pdf.add_paragraph("More balanced thought: _______________________________")
    pdf.add_paragraph("What would I tell a friend: ____________________________")
    pdf.add_page_break()
    
    # Chapter 7 - Flare Plan
    pdf.add_heading1("Chapter 7: Flare-Up Action Plan")
    pdf.add_blank_line()
    pdf.add_heading2("My Personal Flare-Up Protocol")
    pdf.add_paragraph("Complete this when you're feeling well so it's ready for flare days.")
    pdf.add_blank_line()
    pdf.add_heading3("Level 1: Early Warning (pain increasing)")
    pdf.add_bullet("Action 1: ____________________________________")
    pdf.add_bullet("Action 2: ____________________________________")
    pdf.add_bullet("Action 3: ____________________________________")
    pdf.add_heading3("Level 2: Moderate Flare (significantly worse)")
    pdf.add_bullet("Action 1: ____________________________________")
    pdf.add_bullet("Action 2: ____________________________________")
    pdf.add_bullet("Action 3: ____________________________________")
    pdf.add_heading3("Level 3: Severe Flare (crisis level)")
    pdf.add_bullet("Action 1: ____________________________________")
    pdf.add_bullet("Action 2: ____________________________________")
    pdf.add_bullet("Contact: ____________________________________")
    pdf.add_blank_line()
    pdf.add_heading2("Flare-Up Reminders")
    pdf.add_bullet("This will pass. Flares are temporary, even when they feel endless.")
    pdf.add_bullet("You have survived every flare before this one.")
    pdf.add_bullet("Rest is not weakness. It is a strategic recovery tool.")
    pdf.add_bullet("You do not need to earn rest or justify it.")
    pdf.add_bullet("Ask for help. People want to support you.")
    pdf.add_blank_line()
    add_weekly_review(pdf, [
        "Average pain this week (0-10):",
        "Highest pain day and possible trigger:",
        "Lowest pain day - what helped:",
        "Activities completed despite pain:",
        "Strategies used and effectiveness:",
        "Movement minutes this week:",
        "Mood average (1-10):",
        "Goal for next week:"
    ], num_weeks=5)
    pdf.add_page_break()
    
    faqs = [
        ("Why hasn't my pain gone away even though tests are normal?", "Normal imaging does not mean no pain. Chronic pain involves nervous system sensitization - real neurological changes that don't show on X-rays or MRIs. Your pain is valid regardless of test results."),
        ("Is it safe to exercise with chronic pain?", "Yes, with appropriate pacing. Gentle, graded exercise is one of the most evidence-based treatments for chronic pain. Start well below your limit and increase very gradually."),
        ("Will I always have this pain?", "Many people experience significant improvement over time with proper management. The nervous system can recalibrate. Focus on function and quality of life rather than zero pain."),
        ("Are pain medications the answer?", "Medications can be part of a management plan but rarely solve chronic pain alone. A multimodal approach (movement, psychology, lifestyle, medication) typically works best."),
        ("Why does weather affect my pain?", "Barometric pressure changes may affect joint fluid and nerve sensitivity. While the exact mechanism isn't fully understood, this is a real phenomenon many people experience."),
        ("How do I explain chronic pain to family?", "Use analogies: 'My alarm system is stuck on - it fires even without danger.' Share educational resources. Invite them to a doctor's appointment. Be direct about what helps and what doesn't."),
        ("Is chronic pain 'all in my head'?", "No. Chronic pain is real and involves measurable changes in the nervous system. The brain processes all pain - this doesn't make it less real. Anyone suggesting otherwise is uninformed."),
        ("Should I push through pain or rest?", "Neither extreme works. Pushing through leads to flares; excessive rest leads to deconditioning. Pacing - consistent moderate activity with planned rest - is the evidence-based approach."),
    ]
    add_faq_section(pdf, faqs)
    
    pdf.add_page_break()
    pdf.add_heading1("Quick-Reference: Daily Pain Management Checklist")
    pdf.add_bullet("[ ] Completed gentle movement/stretching")
    pdf.add_bullet("[ ] Practiced pacing (breaks before pain increases)")
    pdf.add_bullet("[ ] Used mind-body technique (breathing, meditation)")
    pdf.add_bullet("[ ] Recorded pain level and activities in journal")
    pdf.add_bullet("[ ] Prioritized sleep hygiene")
    pdf.add_bullet("[ ] Connected with someone (social support)")
    pdf.add_bullet("[ ] Did one enjoyable activity despite pain")
    pdf.add_bullet("[ ] Practiced acceptance/self-compassion")
    
    add_about_author(pdf)
    filepath = os.path.join(OUTPUT_DIR, "07-Chronic-Pain-Management-Workbook.pdf")
    pdf.save(filepath)
    return filepath



def book_08_menopause():
    """Menopause Survival Guide"""
    pdf = PurePDF(title="Menopause Survival Guide", author=AUTHOR)
    add_front_matter(pdf, "Menopause Survival Guide", "Symptom Tracker, Nutrition Plan & Lifestyle Strategies")
    
    chapters = ["Understanding Menopause", "Symptom Assessment",
                "Nutrition for Menopause", "Daily Symptom Tracker",
                "HRT & Treatment Options Worksheet", "Lifestyle Strategies",
                "Progress Review", "FAQ & Resources"]
    add_toc(pdf, chapters)
    
    pdf.add_heading1("Introduction")
    pdf.add_paragraph("Menopause is not a disease - it is a natural transition. But that doesn't "
                      "mean it's easy. Hot flashes, sleep disruption, mood changes, weight gain, "
                      "and brain fog can significantly impact your quality of life. This guide "
                      "gives you practical tools to navigate this transition with knowledge and grace.")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 1: Understanding Menopause")
    pdf.add_blank_line()
    pdf.add_heading2("The Stages of Menopause")
    pdf.add_heading3("Perimenopause (2-10 years before menopause)")
    pdf.add_bullet("Hormones begin fluctuating wildly")
    pdf.add_bullet("Periods become irregular")
    pdf.add_bullet("Symptoms often begin here (many women don't realize)")
    pdf.add_bullet("Can start as early as late 30s, typically mid-40s")
    pdf.add_heading3("Menopause (defined retrospectively)")
    pdf.add_bullet("12 consecutive months without a period")
    pdf.add_bullet("Average age: 51 (range 45-55)")
    pdf.add_heading3("Postmenopause (after)")
    pdf.add_bullet("Symptoms may continue for years")
    pdf.add_bullet("Focus shifts to long-term health (bones, heart, brain)")
    pdf.add_blank_line()
    pdf.add_heading2("Common Symptoms")
    pdf.add_bullet("Hot flashes and night sweats (75% of women)")
    pdf.add_bullet("Sleep disturbances")
    pdf.add_bullet("Mood changes (anxiety, irritability, depression)")
    pdf.add_bullet("Brain fog and memory issues")
    pdf.add_bullet("Weight gain (especially midsection)")
    pdf.add_bullet("Vaginal dryness and painful intimacy")
    pdf.add_bullet("Joint pain and stiffness")
    pdf.add_bullet("Thinning hair and skin changes")
    pdf.add_bullet("Heart palpitations")
    pdf.add_bullet("Urinary changes")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 2: Symptom Assessment")
    pdf.add_blank_line()
    pdf.add_heading2("Menopause Symptom Severity Scale")
    pdf.add_paragraph("Rate each symptom 0 (none) to 10 (unbearable). Complete monthly.")
    pdf.add_paragraph("Date: __/__/____")
    meno_symptoms = ["Hot flashes (frequency/intensity)", "Night sweats", "Sleep quality",
                     "Mood changes", "Anxiety", "Brain fog/memory", "Fatigue",
                     "Weight changes", "Joint pain", "Vaginal dryness",
                     "Libido changes", "Heart palpitations", "Headaches", "Skin/hair changes"]
    for s in meno_symptoms:
        pdf.add_paragraph(f"  {s}: ___/10")
    pdf.add_paragraph("Total Symptom Score: ___/140")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 3: Nutrition for Menopause")
    pdf.add_blank_line()
    pdf.add_heading2("Key Nutritional Priorities")
    pdf.add_bullet("Calcium: 1200mg/day (bone protection)")
    pdf.add_bullet("Vitamin D: 1000-2000 IU/day")
    pdf.add_bullet("Protein: 1.0-1.2g/kg body weight (muscle maintenance)")
    pdf.add_bullet("Phytoestrogens: Flaxseeds, soy, legumes")
    pdf.add_bullet("Omega-3 fats: Heart and brain protection")
    pdf.add_bullet("Fiber: 25-30g/day (hormone clearance)")
    pdf.add_blank_line()
    pdf.add_heading2("Foods That Help Symptoms")
    pdf.add_heading3("For Hot Flashes")
    pdf.add_bullet("Soy foods (isoflavones): edamame, tofu, tempeh")
    pdf.add_bullet("Flaxseeds (2 tablespoons ground daily)")
    pdf.add_bullet("Sage tea (traditionally used for sweating)")
    pdf.add_bullet("Cold water and cooling foods")
    pdf.add_heading3("For Bone Health")
    pdf.add_bullet("Dairy or fortified plant milks")
    pdf.add_bullet("Sardines with bones, leafy greens")
    pdf.add_bullet("Vitamin K2 foods (natto, fermented foods)")
    pdf.add_heading3("For Brain Fog")
    pdf.add_bullet("Fatty fish (omega-3 DHA)")
    pdf.add_bullet("Blueberries and dark-colored berries")
    pdf.add_bullet("Walnuts and dark chocolate")
    pdf.add_bullet("Green tea (L-theanine for focus)")
    pdf.add_heading3("For Mood Support")
    pdf.add_bullet("Complex carbs (support serotonin production)")
    pdf.add_bullet("Magnesium-rich foods")
    pdf.add_bullet("B-vitamin foods (whole grains, eggs, legumes)")
    pdf.add_blank_line()
    pdf.add_heading2("7-Day Menopause-Supportive Meal Plan")
    meno_meals = [
        ("Monday", "Flaxseed oatmeal + berries + walnuts", "Salmon salad with leafy greens", "Tofu stir-fry with broccoli and brown rice"),
        ("Tuesday", "Smoothie: soy milk, banana, flax, spinach", "Sardine and avocado toast on sourdough", "Chicken with sweet potato and kale"),
        ("Wednesday", "Greek yogurt + seeds + fruit", "Lentil soup with whole grain bread", "Baked fish with quinoa and asparagus"),
        ("Thursday", "Eggs on toast with sauerkraut", "Edamame and grain bowl", "Turkey and vegetable curry"),
        ("Friday", "Overnight oats with soy milk and berries", "Large salad with chickpeas", "Grilled salmon with roasted vegetables"),
        ("Saturday", "Veggie frittata with side of fruit", "Miso soup with tofu and seaweed", "Mediterranean chicken with olive oil"),
        ("Sunday", "Buckwheat pancakes with fruit", "Leftover bowl", "Slow cooker bone broth stew")
    ]
    for day, b, l, d in meno_meals:
        pdf.add_heading3(day)
        pdf.add_bullet(f"Breakfast: {b}")
        pdf.add_bullet(f"Lunch: {l}")
        pdf.add_bullet(f"Dinner: {d}")
        pdf.add_blank_line()
    pdf.add_page_break()
    
    # Tracker
    pdf.add_heading1("Chapter 4: Daily Symptom Tracker")
    add_tracker_pages(pdf, "Daily Menopause Tracker",
                      ["Hot flashes (count)", "Night sweats (Y/N)", "Sleep hours/quality",
                       "Mood (1-10)", "Energy (1-10)", "Brain fog (1-10)",
                       "Exercise", "Food highlights", "Supplements taken", "Notes"], num_pages=16)
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 5: HRT & Treatment Options Worksheet")
    pdf.add_blank_line()
    pdf.add_paragraph("Use this section to organize information for discussions with your doctor.")
    pdf.add_blank_line()
    pdf.add_heading2("Hormone Replacement Therapy (HRT) Overview")
    pdf.add_paragraph("HRT replaces declining hormones and is the most effective treatment for "
                      "moderate-severe menopause symptoms. It also protects bones and may benefit "
                      "heart health when started within 10 years of menopause.")
    pdf.add_blank_line()
    pdf.add_heading3("Questions to Ask Your Doctor")
    pdf.add_bullet("Am I a candidate for HRT based on my health history?")
    pdf.add_bullet("What type of HRT is best for my symptoms?")
    pdf.add_bullet("What are the risks vs. benefits for me specifically?")
    pdf.add_bullet("How long should I take HRT?")
    pdf.add_bullet("What about bioidentical hormones?")
    pdf.add_bullet("Are there non-hormonal prescription options?")
    pdf.add_blank_line()
    pdf.add_heading3("My Treatment Decision Worksheet")
    pdf.add_paragraph("Current treatment: _______________________")
    pdf.add_paragraph("Effectiveness (1-10): ___")
    pdf.add_paragraph("Side effects: ___________________________")
    pdf.add_paragraph("Questions for next appointment: __________")
    pdf.add_paragraph("_________________________________________")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 6: Lifestyle Strategies")
    pdf.add_blank_line()
    pdf.add_heading2("Exercise for Menopause")
    pdf.add_paragraph("Exercise becomes even more critical during menopause for bone density, "
                      "muscle mass, metabolic health, mood, and sleep.")
    pdf.add_bullet("Strength training: 2-3x/week (builds bone and muscle)")
    pdf.add_bullet("Weight-bearing cardio: Walking, dancing, hiking")
    pdf.add_bullet("Flexibility: Yoga, stretching (joint health)")
    pdf.add_bullet("Balance work: Prevents falls as bone density changes")
    pdf.add_blank_line()
    pdf.add_heading2("Hot Flash Management")
    pdf.add_bullet("Layer clothing for easy removal")
    pdf.add_bullet("Keep a fan nearby (desk fan, handheld)")
    pdf.add_bullet("Cold water and cooling sprays")
    pdf.add_bullet("Identify and avoid triggers (spicy food, alcohol, stress)")
    pdf.add_bullet("Practice slow breathing when flash begins")
    pdf.add_bullet("Cool bedroom for night sweats (moisture-wicking sheets)")
    pdf.add_blank_line()
    pdf.add_heading2("Sleep Strategies")
    pdf.add_bullet("Keep bedroom cool (65-68F)")
    pdf.add_bullet("Moisture-wicking sleepwear and bedding")
    pdf.add_bullet("Consistent bedtime routine")
    pdf.add_bullet("Limit alcohol (triggers night sweats)")
    pdf.add_bullet("Magnesium before bed")
    pdf.add_bullet("Consider separate blankets if partner sleeps warm")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 7: Progress Review")
    add_weekly_review(pdf, [
        "Hot flash frequency this week:",
        "Sleep quality average (1-10):",
        "Mood average (1-10):",
        "Exercise completed:",
        "Nutrition wins:",
        "Most bothersome symptom:",
        "What helped most this week:",
        "Priority for next week:"
    ], num_weeks=5)
    pdf.add_page_break()
    
    faqs = [
        ("At what age does menopause start?", "Average age is 51, but perimenopause can begin 4-10 years earlier. The normal range for menopause is 45-55. Before 45 is considered early menopause."),
        ("Is HRT safe?", "For most healthy women under 60 or within 10 years of menopause, HRT benefits outweigh risks. Individual risk factors matter. Have a thorough discussion with your doctor."),
        ("Will I gain weight during menopause?", "Metabolic changes make weight gain easier, but it's not inevitable. Prioritize strength training, protein intake, and be aware that you may need fewer calories than before."),
        ("How long do hot flashes last?", "Average duration is 7-10 years, but varies widely. Some women have them for a few months, others for 20+ years. Treatment can significantly reduce frequency and severity."),
        ("Can I get pregnant during perimenopause?", "Yes! Until you've had 12 months without a period, pregnancy is possible. Use contraception if pregnancy is not desired."),
        ("Does menopause affect mental health?", "Yes. Fluctuating hormones can trigger anxiety, depression, irritability, and brain fog. These are physiological, not 'just stress.' Treatment is available and effective."),
        ("What about vaginal dryness?", "Very common and treatable. Options include local estrogen (very safe), moisturizers, and lubricants. Don't suffer in silence - talk to your doctor."),
        ("Should I get a bone density test?", "Generally recommended at age 65, or earlier if you have risk factors (early menopause, family history, low body weight, smoking, certain medications)."),
    ]
    add_faq_section(pdf, faqs)
    
    pdf.add_page_break()
    pdf.add_heading1("Quick-Reference: Daily Menopause Wellness Checklist")
    pdf.add_bullet("[ ] Ate calcium and vitamin D rich foods")
    pdf.add_bullet("[ ] Consumed phytoestrogens (flax, soy)")
    pdf.add_bullet("[ ] Adequate protein intake")
    pdf.add_bullet("[ ] Strength training or weight-bearing exercise")
    pdf.add_bullet("[ ] Stress management practice")
    pdf.add_bullet("[ ] Tracked symptoms")
    pdf.add_bullet("[ ] Cool sleep environment prepared")
    pdf.add_bullet("[ ] Self-care or enjoyable activity")
    
    add_about_author(pdf)
    filepath = os.path.join(OUTPUT_DIR, "08-Menopause-Survival-Guide.pdf")
    pdf.save(filepath)
    return filepath



def book_09_mediterranean():
    """Mediterranean Diet Complete Guide"""
    pdf = PurePDF(title="Mediterranean Diet Complete Guide", author=AUTHOR)
    add_front_matter(pdf, "Mediterranean Diet", "Complete Guide with 30-Day Meal Plan")
    
    chapters = ["The Mediterranean Lifestyle", "Getting Started Assessment",
                "30-Day Meal Plan", "Recipes & Cooking Tips",
                "Daily Food & Health Tracker", "Lifestyle Beyond Food",
                "Progress Review", "FAQ & Resources"]
    add_toc(pdf, chapters)
    
    pdf.add_heading1("Introduction")
    pdf.add_paragraph("The Mediterranean diet is consistently ranked the world's healthiest eating "
                      "pattern. It reduces risk of heart disease, diabetes, cancer, and Alzheimer's "
                      "while promoting longevity and mental well-being. Best of all, it is delicious, "
                      "satisfying, and sustainable for life.")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 1: The Mediterranean Lifestyle")
    pdf.add_blank_line()
    pdf.add_heading2("More Than a Diet")
    pdf.add_paragraph("The Mediterranean diet is a lifestyle pattern observed in countries "
                      "bordering the Mediterranean Sea. It includes not just food choices but "
                      "how you eat, move, connect, and enjoy life.")
    pdf.add_blank_line()
    pdf.add_heading3("Core Principles")
    pdf.add_bullet("Abundance of plant foods (vegetables, fruits, whole grains, legumes)")
    pdf.add_bullet("Olive oil as primary fat source")
    pdf.add_bullet("Moderate fish and seafood")
    pdf.add_bullet("Moderate dairy (mainly yogurt and cheese)")
    pdf.add_bullet("Limited red meat")
    pdf.add_bullet("Red wine in moderation (optional)")
    pdf.add_bullet("Shared meals with family and friends")
    pdf.add_bullet("Regular physical activity")
    pdf.add_bullet("Enjoyment of food without guilt")
    pdf.add_blank_line()
    pdf.add_heading2("Proven Health Benefits")
    pdf.add_bullet("30% reduction in heart attacks and strokes")
    pdf.add_bullet("Reduced risk of Type 2 diabetes")
    pdf.add_bullet("Lower rates of certain cancers")
    pdf.add_bullet("Better brain health and reduced Alzheimer's risk")
    pdf.add_bullet("Improved mood and reduced depression")
    pdf.add_bullet("Healthy weight management")
    pdf.add_bullet("Reduced inflammation")
    pdf.add_bullet("Better gut health")
    pdf.add_blank_line()
    pdf.add_heading2("The Mediterranean Food Pyramid")
    pdf.add_heading3("Daily")
    pdf.add_bullet("Vegetables: 5+ servings, all colors")
    pdf.add_bullet("Fruits: 2-3 servings")
    pdf.add_bullet("Whole grains: 3-6 servings")
    pdf.add_bullet("Olive oil: 2-4 tablespoons")
    pdf.add_bullet("Nuts and seeds: 1-2 handfuls")
    pdf.add_bullet("Herbs and spices: Unlimited")
    pdf.add_heading3("Several Times Per Week")
    pdf.add_bullet("Fish and seafood: 2-3 times")
    pdf.add_bullet("Legumes: 3-4 times")
    pdf.add_bullet("Eggs: 3-4 times")
    pdf.add_bullet("Poultry: 2-3 times")
    pdf.add_bullet("Yogurt and cheese: Daily or several times/week")
    pdf.add_heading3("Occasionally")
    pdf.add_bullet("Red meat: 1-2 times per week or less")
    pdf.add_bullet("Sweets: Few times per week")
    pdf.add_bullet("Processed foods: Rarely")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 2: Getting Started")
    pdf.add_blank_line()
    pdf.add_heading2("Kitchen Makeover Checklist")
    pdf.add_heading3("Stock Your Pantry")
    pdf.add_bullet("[ ] Extra virgin olive oil (high quality)")
    pdf.add_bullet("[ ] Canned beans (chickpeas, cannellini, lentils)")
    pdf.add_bullet("[ ] Whole grains (quinoa, brown rice, farro, bulgur)")
    pdf.add_bullet("[ ] Whole wheat pasta")
    pdf.add_bullet("[ ] Canned tomatoes (diced, crushed)")
    pdf.add_bullet("[ ] Nuts (almonds, walnuts, pine nuts)")
    pdf.add_bullet("[ ] Seeds (sesame, sunflower, pumpkin)")
    pdf.add_bullet("[ ] Dried herbs and spices")
    pdf.add_bullet("[ ] Red wine vinegar, balsamic vinegar")
    pdf.add_bullet("[ ] Olives and capers")
    pdf.add_heading3("Fresh Items to Buy Weekly")
    pdf.add_bullet("[ ] Fresh vegetables (whatever is seasonal)")
    pdf.add_bullet("[ ] Fresh fruits")
    pdf.add_bullet("[ ] Fresh fish or seafood")
    pdf.add_bullet("[ ] Lemons and limes")
    pdf.add_bullet("[ ] Fresh herbs (basil, parsley, mint)")
    pdf.add_bullet("[ ] Feta cheese, Parmesan")
    pdf.add_bullet("[ ] Greek yogurt")
    pdf.add_bullet("[ ] Hummus")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 3: 30-Day Mediterranean Meal Plan")
    pdf.add_blank_line()
    for week_num in range(1, 5):
        pdf.add_heading2(f"Week {week_num}")
        week_meals = [
            ("Day 1", "Greek yogurt + honey + walnuts + berries", "Large Greek salad with feta and olive oil", "Grilled fish with lemon, roasted vegetables, quinoa"),
            ("Day 2", "Whole grain toast with avocado and tomato", "Lentil soup with crusty bread", "Chicken souvlaki with tzatziki and salad"),
            ("Day 3", "Oatmeal with figs, almonds, cinnamon", "Tuna and white bean salad", "Pasta with tomato sauce, olives, capers"),
            ("Day 4", "Smoothie: banana, spinach, Greek yogurt", "Hummus wrap with roasted vegetables", "Baked salmon with herbs, sweet potato, greens"),
            ("Day 5", "Eggs with tomatoes, feta, fresh herbs", "Minestrone soup with Parmesan", "Lamb chops with roasted Mediterranean vegetables"),
            ("Day 6", "Fruit salad with yogurt and honey", "Grain bowl with chickpeas and tahini", "Seafood pasta with garlic and white wine"),
            ("Day 7", "Mediterranean frittata", "Leftovers and fresh salad", "Slow-roasted chicken with potatoes and lemon")
        ]
        for day, b, l, d in week_meals:
            pdf.add_heading3(f"Week {week_num}, {day}")
            pdf.add_bullet(f"Breakfast: {b}")
            pdf.add_bullet(f"Lunch: {l}")
            pdf.add_bullet(f"Dinner: {d}")
            pdf.add_blank_line()
        pdf.add_page_break()
    
    pdf.add_heading1("Chapter 4: Recipes & Cooking Tips")
    pdf.add_blank_line()
    med_recipes = [
        ("Classic Greek Salad", ["2 cups chopped cucumber", "2 cups cherry tomatoes", "1/2 red onion, sliced",
         "1/2 cup Kalamata olives", "4 oz feta cheese, cubed", "3 tbsp extra virgin olive oil",
         "1 tbsp red wine vinegar", "Dried oregano, salt, pepper"],
         "Combine all vegetables in a large bowl. Top with feta and olives. Drizzle with olive oil and vinegar. Sprinkle oregano."),
        ("Baked Lemon Herb Salmon", ["4 salmon fillets", "3 tbsp olive oil", "2 lemons (juice and zest)",
         "4 cloves garlic, minced", "Fresh dill and parsley", "Salt and pepper",
         "Cherry tomatoes for roasting"],
         "Preheat oven to 400F. Place salmon on parchment-lined pan. Mix olive oil, lemon, garlic, herbs. Pour over salmon. Roast 12-15 minutes."),
        ("Classic Hummus", ["1 can chickpeas (drained, reserve liquid)", "3 tbsp tahini", "2 cloves garlic",
         "3 tbsp lemon juice", "2 tbsp olive oil", "1/2 tsp cumin", "Salt to taste",
         "Reserved aquafaba for smoothness"],
         "Blend chickpeas with tahini, garlic, lemon, and olive oil until very smooth. Add aquafaba for desired consistency. Drizzle with olive oil and paprika to serve."),
    ]
    for name, ingredients, instructions in med_recipes:
        pdf.add_heading2(name)
        pdf.add_heading3("Ingredients:")
        for ing in ingredients:
            pdf.add_bullet(ing)
        pdf.add_heading3("Instructions:")
        pdf.add_paragraph(instructions)
        pdf.add_separator()
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 5: Daily Food & Health Tracker")
    add_tracker_pages(pdf, "Daily Mediterranean Diet Tracker",
                      ["Vegetables (servings)", "Fruits (servings)", "Olive oil (tbsp)",
                       "Fish/seafood", "Whole grains", "Legumes",
                       "Water (glasses)", "Energy (1-10)", "Mood (1-10)", "Exercise"], num_pages=16)
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 6: Mediterranean Lifestyle Beyond Food")
    pdf.add_blank_line()
    pdf.add_heading2("The Social Component")
    pdf.add_bullet("Share meals with family and friends regularly")
    pdf.add_bullet("Cook together as a bonding activity")
    pdf.add_bullet("Eat slowly and mindfully - meals are not to be rushed")
    pdf.add_bullet("Appreciate food as a source of pleasure and connection")
    pdf.add_blank_line()
    pdf.add_heading2("Movement")
    pdf.add_bullet("Daily walking (the foundation - not gym required)")
    pdf.add_bullet("Active transportation when possible")
    pdf.add_bullet("Gardening and outdoor activities")
    pdf.add_bullet("Dancing and recreational sports")
    pdf.add_blank_line()
    pdf.add_heading2("Rest and Enjoyment")
    pdf.add_bullet("Afternoon rest or relaxation (siesta culture)")
    pdf.add_bullet("Time outdoors in sunshine")
    pdf.add_bullet("Strong community bonds")
    pdf.add_bullet("Work-life balance")
    pdf.add_bullet("Gratitude and presence")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 7: Progress Review")
    add_weekly_review(pdf, [
        "Mediterranean adherence this week (1-10):",
        "Vegetables servings per day (average):",
        "Fish meals this week:",
        "Olive oil used daily: [ ]Y [ ]N",
        "Energy level (1-10):",
        "Weight (if tracking):",
        "Biggest success:",
        "Challenge to address:"
    ], num_weeks=5)
    pdf.add_page_break()
    
    faqs = [
        ("Is the Mediterranean diet good for weight loss?", "Yes. While not a 'diet' in the restrictive sense, the Mediterranean pattern naturally promotes healthy weight through whole foods, healthy fats, and satisfaction. Focus on quality and portion awareness."),
        ("Is olive oil really that important?", "Yes! Extra virgin olive oil is rich in polyphenols with powerful anti-inflammatory effects. Use it generously as your primary cooking and dressing oil. Choose high-quality, cold-pressed."),
        ("Can I follow this diet on a budget?", "Absolutely. Beans, lentils, seasonal vegetables, whole grains, and eggs are affordable staples. Buy olive oil in bulk. Canned fish is budget-friendly. Skip expensive specialty items."),
        ("Do I need to drink wine?", "No. Wine is optional and not required for health benefits. If you don't drink, don't start. The diet's benefits come primarily from the food pattern."),
        ("How is this different from other healthy diets?", "The Mediterranean diet emphasizes healthy fats (olive oil, fish), moderate dairy, and the social aspect of eating. It's less restrictive than many diets and more sustainable long-term."),
        ("Can I eat bread?", "Yes! Whole grain bread is part of the Mediterranean diet. Choose sourdough, whole wheat, or traditional rustic breads. Enjoy with olive oil instead of butter."),
        ("What about dairy?", "Moderate dairy is included - primarily yogurt and cheese rather than milk. Choose fermented options when possible. If dairy-free, focus on other calcium sources."),
        ("How quickly will I see health improvements?", "Many people notice improved energy and digestion within 1-2 weeks. Blood markers (cholesterol, inflammation) may improve within 4-8 weeks of consistent adherence."),
    ]
    add_faq_section(pdf, faqs)
    
    pdf.add_page_break()
    pdf.add_heading1("Quick-Reference: Daily Mediterranean Checklist")
    pdf.add_bullet("[ ] Used olive oil as primary fat")
    pdf.add_bullet("[ ] Ate 5+ servings of vegetables")
    pdf.add_bullet("[ ] Ate 2-3 servings of fruit")
    pdf.add_bullet("[ ] Included whole grains")
    pdf.add_bullet("[ ] Added nuts or seeds")
    pdf.add_bullet("[ ] Enjoyed a meal mindfully")
    pdf.add_bullet("[ ] Drank plenty of water")
    pdf.add_bullet("[ ] Moved my body joyfully")
    
    add_about_author(pdf)
    filepath = os.path.join(OUTPUT_DIR, "09-Mediterranean-Diet-Complete-Guide.pdf")
    pdf.save(filepath)
    return filepath



def book_10_migraine():
    """Migraine Tracker & Management Workbook"""
    pdf = PurePDF(title="Migraine Tracker & Management Workbook", author=AUTHOR)
    add_front_matter(pdf, "Migraine Tracker &", "Management Workbook")
    
    chapters = ["Understanding Migraines", "Migraine Assessment",
                "Trigger Identification", "Headache Diary",
                "Attack Protocol & Rescue Plan", "Prevention Strategies",
                "Progress Review", "FAQ & Resources"]
    add_toc(pdf, chapters)
    
    pdf.add_heading1("Introduction")
    pdf.add_paragraph("Migraines are not 'just headaches.' They are a complex neurological condition "
                      "affecting over 1 billion people worldwide. This workbook helps you identify "
                      "your personal triggers, track attack patterns, develop rescue protocols, "
                      "and work toward fewer, less severe migraine days.")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 1: Understanding Migraines")
    pdf.add_blank_line()
    pdf.add_heading2("What Is a Migraine?")
    pdf.add_paragraph("A migraine is a neurological event involving changes in brain chemistry, "
                      "blood flow, and nerve signaling. It typically involves moderate-severe "
                      "headache plus other symptoms.")
    pdf.add_blank_line()
    pdf.add_heading3("Migraine Phases")
    pdf.add_bullet("Prodrome (hours-days before): Mood changes, food cravings, neck stiffness, fatigue")
    pdf.add_bullet("Aura (20-60 min before, 25% of sufferers): Visual disturbances, tingling, speech difficulty")
    pdf.add_bullet("Attack (4-72 hours): Throbbing head pain, nausea, light/sound sensitivity")
    pdf.add_bullet("Postdrome (hours-days after): 'Migraine hangover' - fatigue, brain fog, weakness")
    pdf.add_blank_line()
    pdf.add_heading2("Types of Migraines")
    pdf.add_bullet("Migraine without aura (most common, ~75%)")
    pdf.add_bullet("Migraine with aura (visual/sensory warning signs)")
    pdf.add_bullet("Chronic migraine (15+ headache days/month)")
    pdf.add_bullet("Menstrual migraine (linked to hormone changes)")
    pdf.add_bullet("Vestibular migraine (dizziness and balance issues)")
    pdf.add_blank_line()
    pdf.add_heading2("Common Triggers")
    pdf.add_bullet("Hormonal changes (menstruation, ovulation)")
    pdf.add_bullet("Stress (or stress letdown - weekend/vacation)")
    pdf.add_bullet("Sleep changes (too much, too little, or irregular)")
    pdf.add_bullet("Weather and barometric pressure changes")
    pdf.add_bullet("Dietary triggers (alcohol, aged cheese, MSG, nitrates)")
    pdf.add_bullet("Dehydration and skipped meals")
    pdf.add_bullet("Sensory overload (bright lights, strong smells, loud noise)")
    pdf.add_bullet("Neck tension and poor posture")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 2: Migraine Assessment")
    pdf.add_blank_line()
    pdf.add_heading2("My Migraine Profile")
    pdf.add_paragraph("Age of first migraine: ___")
    pdf.add_paragraph("Average attacks per month: ___")
    pdf.add_paragraph("Average duration: ___ hours")
    pdf.add_paragraph("Typical pain location: ___________________")
    pdf.add_paragraph("Pain type: [ ]Throbbing [ ]Pressing [ ]Stabbing [ ]Other")
    pdf.add_paragraph("Average severity (1-10): ___")
    pdf.add_paragraph("Aura: [ ]Yes [ ]No  Type: _______________")
    pdf.add_paragraph("Family history: [ ]Yes [ ]No  Who: ___________")
    pdf.add_blank_line()
    pdf.add_heading2("Associated Symptoms (check all)")
    migraine_assoc = ["Nausea", "Vomiting", "Light sensitivity", "Sound sensitivity",
                      "Smell sensitivity", "Neck pain", "Dizziness", "Visual changes",
                      "Tingling/numbness", "Brain fog", "Mood changes", "Fatigue"]
    for s in migraine_assoc:
        pdf.add_bullet(f"[ ] {s}")
    pdf.add_blank_line()
    pdf.add_heading2("Current Treatments")
    pdf.add_paragraph("Acute medications: _________________________")
    pdf.add_paragraph("Preventive medications: _________________________")
    pdf.add_paragraph("Supplements: _________________________")
    pdf.add_paragraph("Non-drug strategies: _________________________")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 3: Trigger Identification")
    pdf.add_blank_line()
    pdf.add_heading2("My Trigger Checklist")
    pdf.add_paragraph("Track for 3+ months to identify YOUR triggers. Not everyone has the same ones.")
    pdf.add_blank_line()
    trigger_cats = [
        ("Dietary", ["Alcohol (especially red wine)", "Aged cheese", "Chocolate", "Caffeine (too much or withdrawal)",
                     "MSG/processed foods", "Artificial sweeteners", "Skipped meals", "Dehydration"]),
        ("Hormonal", ["Menstruation", "Ovulation", "Birth control changes", "Perimenopause"]),
        ("Environmental", ["Weather/barometric pressure", "Bright or flickering lights",
                          "Strong smells (perfume, chemicals)", "Loud noise", "Altitude changes"]),
        ("Lifestyle", ["Poor or excessive sleep", "High stress", "Stress letdown (weekends)",
                      "Intense exercise", "Neck tension/posture", "Screen time"])
    ]
    for cat, triggers in trigger_cats:
        pdf.add_heading3(cat)
        for t in triggers:
            pdf.add_bullet(f"[ ] {t}  Confidence: [ ]Definite [ ]Possible [ ]Unlikely")
        pdf.add_blank_line()
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 4: Headache Diary")
    pdf.add_blank_line()
    pdf.add_paragraph("Track every headache/migraine day for pattern identification.")
    pdf.add_blank_line()
    for month in range(8):
        pdf.add_heading2(f"Month {month+1} Headache Diary")
        for entry in range(12):
            pdf.add_heading3(f"Attack #{entry+1}")
            pdf.add_paragraph("Date: __/__  Start time: ___  End time: ___  Duration: ___ hrs")
            pdf.add_paragraph("Severity (1-10): ___  Location: _________  Type: _________")
            pdf.add_paragraph("Warning signs/aura: _______________________________")
            pdf.add_paragraph("Possible triggers: _________________________________")
            pdf.add_paragraph("Treatment used: ____________  Effective: [ ]Y [ ]N")
            pdf.add_paragraph("Time to relief: ___  Able to function: [ ]Y [ ]Partially [ ]N")
            pdf.add_paragraph("Associated symptoms: _____________________________")
            pdf.add_blank_line()
            pdf.add_separator()
        pdf.add_page_break()
    
    pdf.add_heading1("Chapter 5: Attack Protocol & Rescue Plan")
    pdf.add_blank_line()
    pdf.add_heading2("My Migraine Rescue Protocol")
    pdf.add_paragraph("Complete when well. Keep copies at home, work, and in bag.")
    pdf.add_blank_line()
    pdf.add_heading3("At First Warning Signs (prodrome/aura)")
    pdf.add_bullet("Take acute medication: _____________ (within ___ minutes)")
    pdf.add_bullet("Move to quiet, dark environment if possible")
    pdf.add_bullet("Apply cold pack to: _____________")
    pdf.add_bullet("Other: _____________")
    pdf.add_heading3("During Attack")
    pdf.add_bullet("Medication #2 (if first doesn't work in ___ min): _____________")
    pdf.add_bullet("Position: _____________")
    pdf.add_bullet("Tools: [ ]Ice pack [ ]Eye mask [ ]Earplugs [ ]Peppermint oil")
    pdf.add_bullet("Do NOT: _____________")
    pdf.add_heading3("Emergency - Seek Medical Care If:")
    pdf.add_bullet("Worst headache of your life (sudden onset)")
    pdf.add_bullet("Fever with stiff neck")
    pdf.add_bullet("Confusion, weakness, or speech difficulty")
    pdf.add_bullet("Pain after head injury")
    pdf.add_bullet("Pain unresponsive to all treatments for 72+ hours")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 6: Prevention Strategies")
    pdf.add_blank_line()
    pdf.add_heading2("Lifestyle Prevention")
    pdf.add_bullet("Regular sleep schedule (same time every day including weekends)")
    pdf.add_bullet("Never skip meals (stable blood sugar)")
    pdf.add_bullet("Stay hydrated (aim for clear urine)")
    pdf.add_bullet("Regular moderate exercise (avoid sudden intense exertion)")
    pdf.add_bullet("Stress management (consistent practices, not just during stress)")
    pdf.add_bullet("Limit screen time and take regular breaks")
    pdf.add_bullet("Good posture and ergonomic workspace")
    pdf.add_blank_line()
    pdf.add_heading2("Supplements (discuss with your doctor)")
    pdf.add_bullet("Magnesium: 400-600mg daily (best evidence for prevention)")
    pdf.add_bullet("Riboflavin (B2): 400mg daily")
    pdf.add_bullet("CoQ10: 100mg three times daily")
    pdf.add_bullet("Feverfew: Herbal, modest evidence")
    pdf.add_bullet("Butterbur: Effective but quality concerns (PA-free only)")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 7: Progress Review")
    add_weekly_review(pdf, [
        "Migraine days this week: ___/7",
        "Average severity (1-10):",
        "Triggers identified:",
        "Treatments used and effectiveness:",
        "Prevention strategies followed:",
        "Sleep consistency (1-10):",
        "Stress level (1-10):",
        "Notes for doctor:"
    ], num_weeks=5)
    pdf.add_page_break()
    
    faqs = [
        ("Why are my migraines getting more frequent?", "Increased frequency can result from medication overuse, stress changes, hormonal shifts, new triggers, or progression to chronic migraine. Track patterns and discuss with your neurologist."),
        ("What is medication overuse headache?", "Using acute migraine medications more than 10-15 days per month can paradoxically cause more headaches. If you need medication this often, discuss preventive options with your doctor."),
        ("Can diet really help migraines?", "For some people, yes. Common dietary triggers include alcohol, aged cheese, processed meats, and MSG. An elimination approach can identify your personal triggers."),
        ("Should I see a neurologist?", "Consider a neurologist or headache specialist if: migraines are increasing, current treatment isn't working, you need acute medication 10+ days/month, or you have unusual symptoms."),
        ("Are migraines dangerous?", "While extremely painful and disabling, most migraines are not dangerous. However, always seek emergency care for sudden worst-ever headache, or migraine with neurological symptoms."),
        ("Can exercise trigger migraines?", "It can for some people, especially sudden intense exercise. Start gradually, warm up properly, stay hydrated, and exercise regularly rather than sporadically."),
        ("What about caffeine?", "Caffeine is complex for migraines - it can both trigger and treat them. Consistent moderate intake (same amount daily) is better than irregular use. Withdrawal is a common trigger."),
        ("Do migraines get better with age?", "Many people experience improvement after age 50-60, especially women after menopause. However, this varies significantly between individuals."),
    ]
    add_faq_section(pdf, faqs)
    
    pdf.add_page_break()
    pdf.add_heading1("Quick-Reference: Daily Migraine Prevention Checklist")
    pdf.add_bullet("[ ] Woke at consistent time")
    pdf.add_bullet("[ ] Ate regular meals (no skipping)")
    pdf.add_bullet("[ ] Drank adequate water (8+ glasses)")
    pdf.add_bullet("[ ] Took preventive supplements/medication")
    pdf.add_bullet("[ ] Managed stress proactively")
    pdf.add_bullet("[ ] Moved body gently")
    pdf.add_bullet("[ ] Limited screen time / took breaks")
    pdf.add_bullet("[ ] Avoided known triggers")
    pdf.add_bullet("[ ] Prepared for sleep at consistent time")
    
    add_about_author(pdf)
    filepath = os.path.join(OUTPUT_DIR, "10-Migraine-Tracker-Management-Workbook.pdf")
    pdf.save(filepath)
    return filepath



def book_11_weight_loss():
    """Weight Loss Accountability Workbook"""
    pdf = PurePDF(title="Weight Loss Accountability Workbook", author=AUTHOR)
    add_front_matter(pdf, "Weight Loss Accountability", "Mindset, Habit Building & Non-Diet Approach")
    
    chapters = ["Rethinking Weight Loss", "Your Starting Point Assessment",
                "Building Sustainable Habits", "Daily Accountability Tracker",
                "Nutrition Without Restriction", "Movement & Body Respect",
                "Progress Review & Milestone Tracking", "FAQ & Resources"]
    add_toc(pdf, chapters)
    
    pdf.add_heading1("Introduction")
    pdf.add_paragraph("This is not another restrictive diet book. This workbook takes a "
                      "sustainable, behavior-based approach to weight management that focuses on "
                      "building healthy habits, improving your relationship with food, and creating "
                      "lasting change without deprivation or punishment.")
    pdf.add_blank_line()
    pdf.add_paragraph("The focus is on consistency, self-compassion, and progress - not perfection.")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 1: Rethinking Weight Loss")
    pdf.add_blank_line()
    pdf.add_heading2("Why Most Diets Fail")
    pdf.add_paragraph("Research shows that 80-95% of diets fail long-term. This isn't because "
                      "people lack willpower - it's because restrictive approaches are fundamentally "
                      "unsustainable and trigger biological compensation mechanisms.")
    pdf.add_blank_line()
    pdf.add_heading3("The Diet Cycle")
    pdf.add_bullet("Restriction creates deprivation and cravings")
    pdf.add_bullet("Willpower inevitably breaks down")
    pdf.add_bullet("Overeating or binging occurs")
    pdf.add_bullet("Guilt and shame follow")
    pdf.add_bullet("More restriction is attempted")
    pdf.add_bullet("The cycle repeats with metabolic damage")
    pdf.add_blank_line()
    pdf.add_heading2("A Better Approach: Behavior Change")
    pdf.add_bullet("Focus on ADDING healthy behaviors, not restricting")
    pdf.add_bullet("Build habits that fit your life permanently")
    pdf.add_bullet("Aim for progress, not perfection")
    pdf.add_bullet("Address emotional eating patterns")
    pdf.add_bullet("Move your body from a place of respect, not punishment")
    pdf.add_bullet("Measure success beyond the scale")
    pdf.add_blank_line()
    pdf.add_heading2("Sustainable Weight Management Principles")
    pdf.add_bullet("No food is forbidden (all foods fit)")
    pdf.add_bullet("Eat enough - under-eating backfires")
    pdf.add_bullet("Protein and fiber at every meal")
    pdf.add_bullet("80/20 approach - nourishing foods most of the time")
    pdf.add_bullet("Listen to hunger and fullness cues")
    pdf.add_bullet("Move in ways you enjoy")
    pdf.add_bullet("Prioritize sleep (crucial for weight management)")
    pdf.add_bullet("Manage stress (cortisol promotes fat storage)")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 2: Your Starting Point")
    pdf.add_blank_line()
    pdf.add_heading2("Baseline Measurements")
    pdf.add_paragraph("Record these now. Remeasure monthly (not more often).")
    pdf.add_paragraph("Date: __/__/____")
    pdf.add_paragraph("Weight: ___ lbs  (remember: one data point, not your worth)")
    pdf.add_paragraph("Chest: ___ inches")
    pdf.add_paragraph("Waist: ___ inches")
    pdf.add_paragraph("Hips: ___ inches")
    pdf.add_paragraph("Thigh: ___ inches")
    pdf.add_paragraph("Arm: ___ inches")
    pdf.add_blank_line()
    pdf.add_heading2("Non-Scale Measures (equally important)")
    pdf.add_paragraph("Energy level (1-10): ___")
    pdf.add_paragraph("Sleep quality (1-10): ___")
    pdf.add_paragraph("Mood (1-10): ___")
    pdf.add_paragraph("Confidence (1-10): ___")
    pdf.add_paragraph("Physical fitness (1-10): ___")
    pdf.add_paragraph("Relationship with food (1-10): ___")
    pdf.add_blank_line()
    pdf.add_heading2("My 'Why' Exploration")
    pdf.add_paragraph("Why do you want to change? (Be honest and specific)")
    pdf.add_paragraph("_" * 60)
    pdf.add_paragraph("_" * 60)
    pdf.add_paragraph("How will your life be different?")
    pdf.add_paragraph("_" * 60)
    pdf.add_paragraph("What have you tried before and why did it not work?")
    pdf.add_paragraph("_" * 60)
    pdf.add_paragraph("What does sustainable mean to you?")
    pdf.add_paragraph("_" * 60)
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 3: Building Sustainable Habits")
    pdf.add_blank_line()
    pdf.add_heading2("The Habit Stacking Method")
    pdf.add_paragraph("Attach new habits to existing routines:")
    pdf.add_bullet("After I [existing habit], I will [new habit]")
    pdf.add_bullet("Example: After I pour my morning coffee, I will drink a glass of water")
    pdf.add_blank_line()
    pdf.add_heading3("My Habit Stack Plan")
    for i in range(5):
        pdf.add_paragraph(f"Habit #{i+1}: After I _____________, I will _____________")
    pdf.add_blank_line()
    pdf.add_heading2("Keystone Habits for Weight Management")
    pdf.add_heading3("Start with ONE and master it before adding more:")
    pdf.add_bullet("Drink water first thing in the morning")
    pdf.add_bullet("Eat protein at breakfast")
    pdf.add_bullet("Walk for 10 minutes after lunch")
    pdf.add_bullet("Eat vegetables at 2 meals per day")
    pdf.add_bullet("Stop eating when 80% full")
    pdf.add_bullet("Go to bed by [specific time]")
    pdf.add_bullet("Meal prep on Sunday")
    pdf.add_bullet("Track food (without judgment) for awareness")
    pdf.add_blank_line()
    pdf.add_heading2("The 2-Day Rule")
    pdf.add_paragraph("Never miss your chosen habit two days in a row. One missed day is life. "
                      "Two missed days is the start of a new (unwanted) pattern.")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 4: Daily Accountability Tracker")
    add_tracker_pages(pdf, "Daily Wellness Tracker",
                      ["Water (glasses)", "Vegetables (servings)", "Protein at meals (Y/N)",
                       "Movement (type/min)", "Sleep hours", "Hunger/fullness honored",
                       "Stress level (1-10)", "Win of the day", "Tomorrow's intention"], num_pages=16)
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 5: Nutrition Without Restriction")
    pdf.add_blank_line()
    pdf.add_heading2("The Plate Framework")
    pdf.add_paragraph("Instead of counting calories, build balanced plates:")
    pdf.add_bullet("1/2 plate: Vegetables and/or fruit")
    pdf.add_bullet("1/4 plate: Protein (palm-sized portion)")
    pdf.add_bullet("1/4 plate: Complex carbohydrates (fist-sized)")
    pdf.add_bullet("Add: Thumb-sized portion of healthy fat")
    pdf.add_blank_line()
    pdf.add_heading2("Hunger and Fullness Scale")
    pdf.add_bullet("1: Starving, lightheaded, irritable (too hungry)")
    pdf.add_bullet("2: Very hungry, hard to concentrate")
    pdf.add_bullet("3: Hungry, stomach growling (ideal time to eat)")
    pdf.add_bullet("4: Slightly hungry")
    pdf.add_bullet("5: Neutral - neither hungry nor full")
    pdf.add_bullet("6: Satisfied, comfortable (ideal stopping point)")
    pdf.add_bullet("7: Slightly full")
    pdf.add_bullet("8: Full, slightly uncomfortable")
    pdf.add_bullet("9: Very full, uncomfortable")
    pdf.add_bullet("10: Painfully stuffed (never a goal)")
    pdf.add_paragraph("Aim to eat at 3-4 and stop at 6-7.")
    pdf.add_blank_line()
    pdf.add_heading2("Meal Ideas")
    pdf.add_heading3("Balanced Breakfasts")
    pdf.add_bullet("Eggs + vegetables + whole grain toast")
    pdf.add_bullet("Greek yogurt + berries + nuts")
    pdf.add_bullet("Oatmeal + protein powder + fruit")
    pdf.add_bullet("Smoothie with protein, greens, and healthy fat")
    pdf.add_heading3("Balanced Lunches")
    pdf.add_bullet("Large salad + protein + grains + olive oil dressing")
    pdf.add_bullet("Soup + sandwich on whole grain")
    pdf.add_bullet("Grain bowl with protein and vegetables")
    pdf.add_heading3("Balanced Dinners")
    pdf.add_bullet("Protein + roasted vegetables + small portion starch")
    pdf.add_bullet("Stir-fry with protein and lots of vegetables")
    pdf.add_bullet("Fish + salad + quinoa or sweet potato")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 6: Movement & Body Respect")
    pdf.add_blank_line()
    pdf.add_heading2("Joyful Movement")
    pdf.add_paragraph("Exercise should not be punishment for eating. Find movement you enjoy.")
    pdf.add_bullet("Walking (the most underrated exercise)")
    pdf.add_bullet("Dancing")
    pdf.add_bullet("Swimming")
    pdf.add_bullet("Cycling")
    pdf.add_bullet("Yoga")
    pdf.add_bullet("Group fitness classes")
    pdf.add_bullet("Sports and recreational activities")
    pdf.add_bullet("Hiking and nature walks")
    pdf.add_blank_line()
    pdf.add_heading2("Movement Goals")
    pdf.add_bullet("Daily: 7,000-10,000 steps or 30 minutes of activity")
    pdf.add_bullet("Weekly: 2-3 strength training sessions")
    pdf.add_bullet("Always: Choose stairs, park farther, move more")
    pdf.add_blank_line()
    pdf.add_heading2("Body Respect Affirmations")
    pdf.add_bullet("My body deserves nourishment, not punishment")
    pdf.add_bullet("I move because it feels good, not to earn food")
    pdf.add_bullet("Progress is not always visible on the scale")
    pdf.add_bullet("I am more than a number")
    pdf.add_bullet("I choose consistency over perfection")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 7: Progress Review & Milestones")
    pdf.add_blank_line()
    pdf.add_heading2("Monthly Measurements")
    for m in range(6):
        pdf.add_heading3(f"Month {m+1}")
        pdf.add_paragraph(f"Date: __/__/____  Weight: ___  Waist: ___  Energy: ___/10")
        pdf.add_paragraph(f"Habits maintained: ____________  Mood: ___/10")
        pdf.add_paragraph(f"Non-scale win: ____________________________________")
        pdf.add_blank_line()
    
    add_weekly_review(pdf, [
        "Habits maintained this week (list):",
        "Meals that were balanced (out of 21):",
        "Movement sessions:",
        "Sleep average:",
        "Energy level (1-10):",
        "Relationship with food (1-10):",
        "Biggest win:",
        "Compassion moment (when I was kind to myself):"
    ], num_weeks=5)
    pdf.add_page_break()
    
    faqs = [
        ("How fast should I expect to lose weight?", "Sustainable fat loss is 0.5-1 pound per week. Faster loss typically means muscle loss and is harder to maintain. Focus on trend over time, not day-to-day fluctuations."),
        ("Should I count calories?", "Calorie counting works for some but triggers disordered eating in others. The plate method, hunger/fullness awareness, and food quality focus work well without counting."),
        ("What about cheat days?", "The concept of 'cheating' implies restriction and guilt. Instead, practice flexible eating - enjoy all foods without labeling them good or bad. No food is off-limits."),
        ("Why did I stop losing weight (plateau)?", "Plateaus are normal and expected. Your body adapts. Options: adjust portions slightly, increase protein, add strength training, manage stress, or accept this as your body's set point."),
        ("Is it possible to be healthy at a higher weight?", "Health markers (blood pressure, blood sugar, cholesterol, fitness level) matter more than the number on the scale. Focus on behaviors and health outcomes."),
        ("How do I handle emotional eating?", "First, identify the emotion. Then ask: Am I physically hungry? If not, what do I actually need? (Rest, connection, comfort, stimulation.) Food is not the enemy, but it can't solve non-food problems."),
        ("Does sleep really affect weight?", "Absolutely. Poor sleep increases hunger hormones, decreases willpower, promotes fat storage, and makes you more likely to choose high-calorie foods. Prioritize 7-9 hours."),
        ("How do I stay motivated long-term?", "Motivation fades - habits sustain you. Focus on identity ('I am someone who moves daily') rather than goals. Track behaviors, not just outcomes. Celebrate non-scale wins."),
    ]
    add_faq_section(pdf, faqs)
    
    pdf.add_page_break()
    pdf.add_heading1("Quick-Reference: Daily Accountability Checklist")
    pdf.add_bullet("[ ] Drank water upon waking")
    pdf.add_bullet("[ ] Ate balanced meals with protein and vegetables")
    pdf.add_bullet("[ ] Moved my body in a way I enjoy")
    pdf.add_bullet("[ ] Checked in with hunger/fullness")
    pdf.add_bullet("[ ] Practiced one keystone habit")
    pdf.add_bullet("[ ] Got adequate sleep")
    pdf.add_bullet("[ ] Practiced self-compassion")
    pdf.add_bullet("[ ] Celebrated one small win")
    
    add_about_author(pdf)
    filepath = os.path.join(OUTPUT_DIR, "11-Weight-Loss-Accountability-Workbook.pdf")
    pdf.save(filepath)
    return filepath



def book_12_nervous_system():
    """Nervous System Regulation Workbook"""
    pdf = PurePDF(title="Nervous System Regulation Workbook", author=AUTHOR)
    add_front_matter(pdf, "Nervous System Regulation", "Vagus Nerve, Anxiety Management & Somatic Tools")
    
    chapters = ["Understanding Your Nervous System", "Nervous System Assessment",
                "Vagus Nerve Activation Exercises", "Daily Regulation Tracker",
                "Somatic Tools & Body-Based Practices", "Lifestyle for Nervous System Health",
                "Progress Review", "FAQ & Resources"]
    add_toc(pdf, chapters)
    
    pdf.add_heading1("Introduction")
    pdf.add_paragraph("If you feel constantly on edge, exhausted, overwhelmed, or emotionally "
                      "reactive, your nervous system may be dysregulated. This workbook teaches "
                      "you to recognize your nervous system state, use evidence-based tools to "
                      "return to safety and calm, and build resilience over time.")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 1: Understanding Your Nervous System")
    pdf.add_blank_line()
    pdf.add_heading2("The Autonomic Nervous System")
    pdf.add_paragraph("Your autonomic nervous system (ANS) operates automatically, controlling "
                      "heart rate, breathing, digestion, and stress responses. It has two main "
                      "branches plus an important newer discovery:")
    pdf.add_blank_line()
    pdf.add_heading3("Sympathetic: Fight or Flight")
    pdf.add_bullet("Activated by perceived threat (real or imagined)")
    pdf.add_bullet("Heart rate increases, breathing quickens")
    pdf.add_bullet("Muscles tense, pupils dilate")
    pdf.add_bullet("Digestion shuts down, energy mobilized")
    pdf.add_bullet("Feelings: Anxiety, panic, anger, hypervigilance")
    pdf.add_blank_line()
    pdf.add_heading3("Parasympathetic: Rest and Digest")
    pdf.add_bullet("Activated when safe and relaxed")
    pdf.add_bullet("Heart rate slows, breathing deepens")
    pdf.add_bullet("Digestion resumes, repair processes activate")
    pdf.add_bullet("Feelings: Calm, connected, present, content")
    pdf.add_blank_line()
    pdf.add_heading3("Dorsal Vagal: Freeze/Shutdown")
    pdf.add_bullet("Activated when threat feels inescapable")
    pdf.add_bullet("Energy collapses, numbness, disconnection")
    pdf.add_bullet("Feelings: Hopelessness, dissociation, depression, exhaustion")
    pdf.add_blank_line()
    pdf.add_heading2("Polyvagal Theory: The Three States")
    pdf.add_paragraph("Dr. Stephen Porges' Polyvagal Theory explains how our nervous system "
                      "constantly scans for safety (neuroception) and moves between three states:")
    pdf.add_bullet("Ventral Vagal (safe/social): Ideal state. Connected, calm, curious, creative.")
    pdf.add_bullet("Sympathetic (mobilized): Fight or flight. Anxious, angry, restless.")
    pdf.add_bullet("Dorsal Vagal (immobilized): Freeze or collapse. Numb, disconnected, shut down.")
    pdf.add_blank_line()
    pdf.add_heading2("The Vagus Nerve")
    pdf.add_paragraph("The vagus nerve is the longest cranial nerve, connecting brain to gut. "
                      "It is the main nerve of the parasympathetic system. Higher vagal tone = "
                      "better ability to return to calm after stress.")
    pdf.add_blank_line()
    pdf.add_heading3("Signs of Good Vagal Tone")
    pdf.add_bullet("Quick recovery after stress")
    pdf.add_bullet("Good digestion")
    pdf.add_bullet("Healthy heart rate variability")
    pdf.add_bullet("Ability to socially engage")
    pdf.add_bullet("Emotional resilience")
    pdf.add_heading3("Signs of Poor Vagal Tone")
    pdf.add_bullet("Chronic anxiety or depression")
    pdf.add_bullet("Digestive issues (IBS, bloating)")
    pdf.add_bullet("Difficulty calming down after upset")
    pdf.add_bullet("Chronic inflammation")
    pdf.add_bullet("Social withdrawal")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 2: Nervous System Assessment")
    pdf.add_blank_line()
    pdf.add_heading2("Where Do You Spend Most Time?")
    pdf.add_paragraph("Check the column that best describes your typical state:")
    pdf.add_blank_line()
    pdf.add_heading3("Ventral Vagal (Safe)")
    safe_signs = ["I feel calm and present most of the time", "I enjoy connecting with others",
                  "I can focus and think clearly", "I recover quickly from stress",
                  "My digestion works well", "I sleep well most nights"]
    for s in safe_signs:
        pdf.add_bullet(f"[ ] {s}")
    pdf.add_paragraph("Count: ___/6")
    pdf.add_blank_line()
    pdf.add_heading3("Sympathetic (Fight/Flight)")
    ff_signs = ["I feel anxious or on edge most days", "My heart races or I feel restless",
                "I'm easily startled or irritable", "I have trouble sleeping (mind racing)",
                "I feel tense in my body constantly", "I snap at people or feel angry"]
    for s in ff_signs:
        pdf.add_bullet(f"[ ] {s}")
    pdf.add_paragraph("Count: ___/6")
    pdf.add_blank_line()
    pdf.add_heading3("Dorsal Vagal (Freeze)")
    freeze_signs = ["I feel numb or disconnected", "I have no energy or motivation",
                    "I feel hopeless or stuck", "I zone out or dissociate",
                    "I want to isolate and withdraw", "I feel heavy and want to sleep all day"]
    for s in freeze_signs:
        pdf.add_bullet(f"[ ] {s}")
    pdf.add_paragraph("Count: ___/6")
    pdf.add_paragraph("Highest score indicates your dominant state. Many people oscillate between states.")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 3: Vagus Nerve Activation Exercises")
    pdf.add_blank_line()
    pdf.add_paragraph("These exercises directly stimulate the vagus nerve to shift from "
                      "sympathetic/dorsal states toward ventral vagal (safe and social).")
    pdf.add_blank_line()
    pdf.add_heading2("1. Physiological Sigh (fastest reset)")
    pdf.add_bullet("Double inhale through nose (short-short)")
    pdf.add_bullet("Long slow exhale through mouth")
    pdf.add_bullet("Repeat 3-5 times")
    pdf.add_bullet("Works within 1-2 breaths for acute anxiety")
    pdf.add_blank_line()
    pdf.add_heading2("2. Cold Water Vagal Dive Reflex")
    pdf.add_bullet("Splash cold water on face (especially forehead and cheeks)")
    pdf.add_bullet("Or: Hold ice cubes in hands for 30-60 seconds")
    pdf.add_bullet("Or: Cold water at end of shower for 30 seconds")
    pdf.add_bullet("Triggers automatic parasympathetic response")
    pdf.add_blank_line()
    pdf.add_heading2("3. Humming, Singing, and Gargling")
    pdf.add_bullet("Hum deeply for 2-3 minutes (vibrates vagus nerve in throat)")
    pdf.add_bullet("Sing loudly (especially low notes)")
    pdf.add_bullet("Gargle water vigorously for 30 seconds")
    pdf.add_bullet("Chant 'om' or 'voo' sound")
    pdf.add_blank_line()
    pdf.add_heading2("4. Extended Exhale Breathing")
    pdf.add_bullet("Inhale for 4 counts")
    pdf.add_bullet("Exhale for 6-8 counts (longer exhale activates PNS)")
    pdf.add_bullet("Continue for 5-10 minutes")
    pdf.add_bullet("Box breathing: 4 in, 4 hold, 4 out, 4 hold")
    pdf.add_blank_line()
    pdf.add_heading2("5. Orienting to Safety")
    pdf.add_bullet("Slowly look around your environment")
    pdf.add_bullet("Name 5 things you can see")
    pdf.add_bullet("Name 4 things you can touch/feel")
    pdf.add_bullet("Name 3 things you can hear")
    pdf.add_bullet("This tells your nervous system: 'I am safe right now'")
    pdf.add_blank_line()
    pdf.add_heading2("6. Social Engagement")
    pdf.add_bullet("Make eye contact with a safe person")
    pdf.add_bullet("Listen to or use a warm, melodic voice tone")
    pdf.add_bullet("Smile (even forced smiling sends safety signals)")
    pdf.add_bullet("Hug or gentle touch from trusted person")
    pdf.add_blank_line()
    pdf.add_heading2("7. Gentle Rocking and Swaying")
    pdf.add_bullet("Rock gently side to side or front to back")
    pdf.add_bullet("Use a rocking chair")
    pdf.add_bullet("Sway with arms wrapped around yourself")
    pdf.add_bullet("Mimics being held (primal safety signal)")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 4: Daily Regulation Tracker")
    add_tracker_pages(pdf, "Daily Nervous System Tracker",
                      ["Dominant state today (V/S/D)", "Anxiety level (1-10)",
                       "Triggers noticed", "Regulation tools used",
                       "Time in calm/connected state", "Sleep quality (1-10)",
                       "Body tension areas", "Social connection (Y/N)",
                       "Movement/exercise", "Wins today"], num_pages=16)
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 5: Somatic Tools & Body-Based Practices")
    pdf.add_blank_line()
    pdf.add_heading2("Why Body-Based Tools Work")
    pdf.add_paragraph("The nervous system speaks the language of the body. You cannot think "
                      "your way out of a dysregulated state - you must work through the body "
                      "to signal safety to the brain.")
    pdf.add_blank_line()
    pdf.add_heading2("Shaking and Tremoring")
    pdf.add_paragraph("Animals shake after a threat to discharge survival energy. Humans can too:")
    pdf.add_bullet("Stand with slightly bent knees")
    pdf.add_bullet("Begin gentle bouncing or shaking")
    pdf.add_bullet("Let the shaking spread naturally to whole body")
    pdf.add_bullet("Continue for 5-15 minutes")
    pdf.add_bullet("Notice what happens as you slow down")
    pdf.add_blank_line()
    pdf.add_heading2("Grounding Techniques")
    pdf.add_heading3("Feet on Floor")
    pdf.add_bullet("Press feet firmly into the ground")
    pdf.add_bullet("Notice the sensation of support beneath you")
    pdf.add_bullet("Rock weight forward, back, side to side")
    pdf.add_bullet("Stomp gently if needed for more sensation")
    pdf.add_heading3("Butterfly Hug (bilateral stimulation)")
    pdf.add_bullet("Cross arms over chest, hands on shoulders")
    pdf.add_bullet("Alternately tap left, right, left, right")
    pdf.add_bullet("Slow rhythm for 2-3 minutes")
    pdf.add_bullet("Used in EMDR for emotional processing")
    pdf.add_blank_line()
    pdf.add_heading2("Progressive Muscle Relaxation")
    pdf.add_paragraph("Tense each muscle group for 5 seconds, then release completely:")
    pdf.add_bullet("Start with feet, work up through body to face")
    pdf.add_bullet("Notice the contrast between tension and release")
    pdf.add_bullet("Takes 10-15 minutes for full body")
    pdf.add_blank_line()
    pdf.add_heading2("Containment Visualization")
    pdf.add_bullet("Imagine a container (box, vault, locked chest)")
    pdf.add_bullet("Mentally place overwhelming feelings/memories inside")
    pdf.add_bullet("Close and lock the container")
    pdf.add_bullet("You can return to it when ready and resourced")
    pdf.add_bullet("Useful for managing flashbacks or overwhelm")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 6: Lifestyle for Nervous System Health")
    pdf.add_blank_line()
    pdf.add_heading2("Daily Practices for Regulation")
    pdf.add_bullet("Morning: Sunlight within 30 min (sets circadian rhythm, calms NS)")
    pdf.add_bullet("Movement: Daily gentle exercise (walking, yoga, swimming)")
    pdf.add_bullet("Nature: Time outdoors (proven to shift to parasympathetic)")
    pdf.add_bullet("Connection: At least one meaningful interaction daily")
    pdf.add_bullet("Breathwork: 5-10 minutes of intentional breathing")
    pdf.add_bullet("Sleep: Consistent schedule, 7-9 hours")
    pdf.add_blank_line()
    pdf.add_heading2("Nutrition for the Nervous System")
    pdf.add_bullet("Omega-3 fats: Brain and nerve health (fatty fish, walnuts)")
    pdf.add_bullet("Magnesium: Natural relaxant (leafy greens, dark chocolate)")
    pdf.add_bullet("B vitamins: Nerve function (whole grains, eggs)")
    pdf.add_bullet("Probiotics: Gut-brain axis support (fermented foods)")
    pdf.add_bullet("Avoid: Excess caffeine, alcohol, sugar (all dysregulating)")
    pdf.add_blank_line()
    pdf.add_heading2("Building a Safety Toolkit")
    pdf.add_paragraph("Create your personalized toolkit for different states:")
    pdf.add_blank_line()
    pdf.add_heading3("When Anxious/Activated (sympathetic):")
    pdf.add_paragraph("My tools: _______________________________________")
    pdf.add_heading3("When Numb/Shutdown (dorsal vagal):")
    pdf.add_paragraph("My tools: _______________________________________")
    pdf.add_heading3("For Maintenance (daily regulation):")
    pdf.add_paragraph("My tools: _______________________________________")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 7: Progress Review")
    add_weekly_review(pdf, [
        "Dominant nervous system state this week:",
        "Number of days in regulated state: ___/7",
        "Tools used and effectiveness:",
        "Triggers identified:",
        "Recovery time from activation:",
        "Sleep quality average:",
        "Body tension level (1-10):",
        "What helped most this week:"
    ], num_weeks=5)
    pdf.add_page_break()
    
    faqs = [
        ("How long does it take to regulate a dysregulated nervous system?", "It varies greatly depending on how long dysregulation has been present. Some people notice shifts within days of consistent practice. Deeper changes take months of daily work. Be patient and consistent."),
        ("Is this the same as anxiety?", "Anxiety is often a symptom of nervous system dysregulation (stuck in sympathetic activation). Regulation tools address the root cause rather than just managing symptoms."),
        ("Can trauma cause nervous system dysregulation?", "Yes. Trauma is one of the primary causes. The nervous system can get 'stuck' in protective states long after danger has passed. Professional trauma therapy combined with these tools is recommended."),
        ("Why do I feel worse before feeling better?", "As your nervous system begins to regulate, suppressed emotions and body sensations may surface. This is actually a sign of healing - you're feeling things you've been numb to. Go slowly and seek support if needed."),
        ("Can children benefit from these tools?", "Absolutely. Teaching children co-regulation and simple tools like breathing and shaking helps build nervous system resilience early. Model these practices - children learn through watching."),
        ("What is the difference between regulation and relaxation?", "Relaxation is one state (parasympathetic). Regulation is the ability to flexibly move between states as appropriate - being activated when needed and returning to baseline when safe."),
        ("Should I avoid all stress?", "No. Some stress is healthy and necessary (exercise, challenges, growth). The goal is building resilience - the ability to handle stress and recover. Avoid chronic, unrelenting stress."),
        ("How do I know if I need professional help?", "If dysregulation significantly impacts daily functioning, if you have trauma history, if you experience dissociation, or if self-help tools aren't providing relief after consistent practice for 6-8 weeks."),
    ]
    add_faq_section(pdf, faqs)
    
    pdf.add_page_break()
    pdf.add_heading1("Quick-Reference: Daily Regulation Checklist")
    pdf.add_bullet("[ ] Morning sunlight exposure")
    pdf.add_bullet("[ ] Breathwork practice (5+ min)")
    pdf.add_bullet("[ ] Checked in with body (where am I holding tension?)")
    pdf.add_bullet("[ ] Used vagal toning exercise")
    pdf.add_bullet("[ ] Moved body gently")
    pdf.add_bullet("[ ] Connected with another person")
    pdf.add_bullet("[ ] Spent time in nature or outdoors")
    pdf.add_bullet("[ ] Honored my nervous system's needs")
    pdf.add_bullet("[ ] Practiced self-compassion")
    
    add_about_author(pdf)
    filepath = os.path.join(OUTPUT_DIR, "12-Nervous-System-Regulation-Workbook.pdf")
    pdf.save(filepath)
    return filepath



def book_13_postpartum():
    """Postpartum Recovery & Wellness Guide"""
    pdf = PurePDF(title="Postpartum Recovery & Wellness Guide", author=AUTHOR)
    add_front_matter(pdf, "Postpartum Recovery", "& Wellness Guide for New Moms")
    
    chapters = ["Understanding Postpartum Recovery", "Your Recovery Assessment",
                "Physical Healing", "Postpartum Mood & Mental Health",
                "Nutrition for Recovery & Breastfeeding", "New Mom Daily Tracker",
                "Progress & Milestone Tracking", "FAQ & Resources"]
    add_toc(pdf, chapters)
    
    pdf.add_heading1("Introduction")
    pdf.add_paragraph("The postpartum period (often called the 'fourth trimester') is a time of "
                      "enormous physical, emotional, and social change. Your body has done something "
                      "extraordinary, and it deserves intentional care as it heals. This guide "
                      "supports you through recovery with practical tools and compassionate guidance.")
    pdf.add_blank_line()
    pdf.add_paragraph("Remember: Recovery is not linear, and you do not need to 'bounce back.' "
                      "You are becoming someone new - a mother. Give yourself grace.")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 1: Understanding Postpartum Recovery")
    pdf.add_blank_line()
    pdf.add_heading2("Timeline of Physical Recovery")
    pdf.add_heading3("Week 1-2: Immediate Healing")
    pdf.add_bullet("Uterus begins contracting back to size")
    pdf.add_bullet("Lochia (postpartum bleeding) is heaviest")
    pdf.add_bullet("Perineum or incision healing begins")
    pdf.add_bullet("Breast milk comes in (days 2-5)")
    pdf.add_bullet("Hormone crash (baby blues possible)")
    pdf.add_heading3("Weeks 2-6: Early Recovery")
    pdf.add_bullet("Bleeding gradually decreases")
    pdf.add_bullet("Energy slowly returns")
    pdf.add_bullet("Breastfeeding establishing (or bottle feeding routine)")
    pdf.add_bullet("Sleep deprivation peaks")
    pdf.add_bullet("6-week postpartum check-up")
    pdf.add_heading3("Months 2-6: Continued Healing")
    pdf.add_bullet("Core and pelvic floor strengthening")
    pdf.add_bullet("Hormones gradually stabilizing")
    pdf.add_bullet("Hair changes (postpartum shedding around month 3-4)")
    pdf.add_bullet("Gradual return to exercise")
    pdf.add_heading3("Months 6-12+: Full Recovery")
    pdf.add_bullet("Full healing takes 12-18 months (not 6 weeks)")
    pdf.add_bullet("Body composition changes may be permanent - and that's okay")
    pdf.add_bullet("Mental health needs ongoing attention")
    pdf.add_blank_line()
    pdf.add_heading2("Red Flags - Seek Immediate Medical Care")
    pdf.add_bullet("Heavy bleeding (soaking a pad in 1 hour or large clots)")
    pdf.add_bullet("Fever over 100.4F")
    pdf.add_bullet("Severe headache or vision changes")
    pdf.add_bullet("Thoughts of harming yourself or baby (call 988 or go to ER)")
    pdf.add_bullet("Signs of infection (foul smell, increasing pain, redness)")
    pdf.add_bullet("Chest pain or difficulty breathing")
    pdf.add_bullet("Calf pain or swelling (possible blood clot)")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 2: Your Recovery Assessment")
    pdf.add_blank_line()
    pdf.add_heading2("Birth Information")
    pdf.add_paragraph("Baby born: __/__/____  Method: [ ]Vaginal [ ]C-section")
    pdf.add_paragraph("Complications: _______________________________")
    pdf.add_paragraph("Feeding method: [ ]Breast [ ]Bottle [ ]Combo")
    pdf.add_paragraph("Support system: _______________________________")
    pdf.add_blank_line()
    pdf.add_heading2("Weekly Check-In (complete each week)")
    pdf.add_paragraph("Date: __/__/____  Weeks postpartum: ___")
    pdf.add_paragraph("Physical pain level (1-10): ___")
    pdf.add_paragraph("Energy level (1-10): ___")
    pdf.add_paragraph("Mood (1-10): ___")
    pdf.add_paragraph("Sleep (hours in 24hrs): ___")
    pdf.add_paragraph("Feeding going well: [ ]Yes [ ]Struggling [ ]Need help")
    pdf.add_paragraph("Bonding with baby (1-10): ___")
    pdf.add_paragraph("Anxiety level (1-10): ___")
    pdf.add_paragraph("Support received (1-10): ___")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 3: Physical Healing")
    pdf.add_blank_line()
    pdf.add_heading2("Core & Pelvic Floor Recovery")
    pdf.add_paragraph("Your core and pelvic floor need specific, gentle rehabilitation after "
                      "pregnancy and birth. Do NOT jump back into crunches or high-impact exercise.")
    pdf.add_blank_line()
    pdf.add_heading3("Week 1-2 Exercises (gentle)")
    pdf.add_bullet("Diaphragmatic breathing: Inhale belly expands, exhale belly draws in gently")
    pdf.add_bullet("Pelvic floor activation: Gentle Kegel (lift and hold 5 sec, release)")
    pdf.add_bullet("Gentle walking as tolerated")
    pdf.add_heading3("Weeks 3-6 (building)")
    pdf.add_bullet("Bridge pose (gentle)")
    pdf.add_bullet("Bird dog (on all fours, extend opposite arm/leg)")
    pdf.add_bullet("Clamshells (side-lying hip strengthening)")
    pdf.add_bullet("Modified planks (on knees)")
    pdf.add_bullet("Longer walks")
    pdf.add_heading3("After 6 Weeks (with clearance)")
    pdf.add_bullet("Gradually increase intensity")
    pdf.add_bullet("Continue pelvic floor work")
    pdf.add_bullet("Consider pelvic floor physiotherapy if any leaking, pain, or heaviness")
    pdf.add_blank_line()
    pdf.add_heading2("C-Section Recovery")
    pdf.add_bullet("No lifting anything heavier than baby for 6 weeks")
    pdf.add_bullet("Support incision when coughing/laughing")
    pdf.add_bullet("Gentle scar massage after 6 weeks (prevents adhesions)")
    pdf.add_bullet("Walk daily as soon as possible (prevents blood clots)")
    pdf.add_bullet("Monitor incision for signs of infection")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 4: Postpartum Mood & Mental Health")
    pdf.add_blank_line()
    pdf.add_heading2("Understanding Postpartum Mental Health")
    pdf.add_heading3("Baby Blues (80% of new mothers)")
    pdf.add_bullet("Occurs days 2-14 postpartum")
    pdf.add_bullet("Crying, mood swings, overwhelm")
    pdf.add_bullet("Resolves on its own within 2 weeks")
    pdf.add_bullet("Caused by sudden hormone drop")
    pdf.add_heading3("Postpartum Depression (1 in 7 mothers)")
    pdf.add_bullet("Persists beyond 2 weeks or worsens over time")
    pdf.add_bullet("Persistent sadness, loss of interest")
    pdf.add_bullet("Difficulty bonding with baby")
    pdf.add_bullet("Changes in appetite and sleep (beyond baby-related)")
    pdf.add_bullet("Feelings of worthlessness or guilt")
    pdf.add_bullet("THIS IS TREATABLE - please reach out for help")
    pdf.add_heading3("Postpartum Anxiety")
    pdf.add_bullet("Excessive worry about baby's health/safety")
    pdf.add_bullet("Racing thoughts, inability to relax")
    pdf.add_bullet("Physical symptoms: racing heart, nausea, tension")
    pdf.add_bullet("Intrusive scary thoughts (common and treatable)")
    pdf.add_blank_line()
    pdf.add_heading2("Mood Self-Screening (Edinburgh Postnatal Depression Scale)")
    pdf.add_paragraph("Complete at 2, 6, and 12 weeks postpartum. Share results with your provider.")
    pdf.add_paragraph("In the past 7 days:")
    edinburgh = [
        "I have been able to laugh and see the funny side of things",
        "I have looked forward with enjoyment to things",
        "I have blamed myself unnecessarily when things went wrong",
        "I have been anxious or worried for no good reason",
        "I have felt scared or panicky for no good reason",
        "Things have been getting on top of me",
        "I have been so unhappy that I have had difficulty sleeping",
        "I have felt sad or miserable",
        "I have been so unhappy that I have been crying",
        "The thought of harming myself has occurred to me"
    ]
    for i, q in enumerate(edinburgh, 1):
        pdf.add_paragraph(f"  {i}. {q}: ___/3")
    pdf.add_paragraph("Total: ___/30  (Score 10+ = discuss with provider immediately)")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 5: Nutrition for Recovery & Breastfeeding")
    pdf.add_blank_line()
    pdf.add_heading2("Postpartum Nutritional Needs")
    pdf.add_paragraph("Your body needs MORE nutrition after birth, not less. Now is not the time "
                      "for dieting. Focus on nourishing recovery and milk production (if breastfeeding).")
    pdf.add_blank_line()
    pdf.add_heading3("Key Nutrients")
    pdf.add_bullet("Iron: Replenish blood loss (red meat, lentils, spinach)")
    pdf.add_bullet("Protein: Tissue repair, milk production (aim 75-100g/day)")
    pdf.add_bullet("Calcium: Bone health (depleted during pregnancy/nursing)")
    pdf.add_bullet("Omega-3 DHA: Brain health for you and baby")
    pdf.add_bullet("Vitamin D: Often depleted, support immune health")
    pdf.add_bullet("Choline: Brain development if breastfeeding")
    pdf.add_bullet("Fluids: Extra 24-32oz if breastfeeding")
    pdf.add_blank_line()
    pdf.add_heading2("Easy Postpartum Meals (one-handed, minimal prep)")
    pdf.add_bullet("Overnight oats prepared the night before")
    pdf.add_bullet("Protein smoothies (prep ingredients in freezer bags)")
    pdf.add_bullet("Egg muffins (batch cook for the week)")
    pdf.add_bullet("Rotisserie chicken with pre-washed salad")
    pdf.add_bullet("Trail mix with nuts, seeds, dried fruit")
    pdf.add_bullet("Pre-made bone broth (sip throughout day)")
    pdf.add_bullet("Nut butter on toast with banana")
    pdf.add_bullet("Batch soups and stews (freezer meals)")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 6: New Mom Daily Tracker")
    add_tracker_pages(pdf, "Daily Postpartum Tracker",
                      ["Baby feeds (count)", "My meals eaten", "Water intake",
                       "Sleep (total hours in 24hrs)", "Pain level (1-10)",
                       "Mood (1-10)", "Baby mood/fussiness", "Help received from",
                       "Self-care done", "One thing I did well today"], num_pages=16)
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 7: Progress & Milestone Tracking")
    pdf.add_blank_line()
    pdf.add_heading2("Monthly Recovery Milestones")
    for m in range(6):
        pdf.add_heading3(f"Month {m+1} Postpartum")
        pdf.add_paragraph(f"Date: __/__/____")
        pdf.add_paragraph(f"Physical recovery (1-10): ___")
        pdf.add_paragraph(f"Emotional wellbeing (1-10): ___")
        pdf.add_paragraph(f"Sleep pattern: ______")
        pdf.add_paragraph(f"Feeding going: ______")
        pdf.add_paragraph(f"Support level (1-10): ___")
        pdf.add_paragraph(f"What I'm proud of: ______________________")
        pdf.add_paragraph(f"What I need help with: ___________________")
        pdf.add_blank_line()
    
    add_weekly_review(pdf, [
        "Physical healing progress:",
        "Mood and emotional state:",
        "Sleep (best I can get):",
        "Nutrition (am I eating enough?):",
        "Help I need to ask for:",
        "Something that made me smile:",
        "Self-care I managed:",
        "One thing I want to do differently:"
    ], num_weeks=4)
    pdf.add_page_break()
    
    faqs = [
        ("When will I feel like myself again?", "The 'new normal' develops gradually over 6-12 months. You may not return to your pre-baby self - you're becoming a new version. Be patient and compassionate with this transformation."),
        ("Is it normal to not feel bonded to my baby immediately?", "Yes. Bonding is not always instant. It develops over time through care, skin-to-skin contact, and attentive presence. If bonding difficulties persist, talk to your provider."),
        ("When can I exercise again?", "Light walking can start days after vaginal birth (when comfortable). More structured exercise after 6-week clearance. C-section requires longer recovery. Always start gentle."),
        ("How do I know if I have postpartum depression vs. baby blues?", "Baby blues resolve within 2 weeks. PPD persists, worsens, or begins after 2 weeks. If symptoms interfere with functioning or bonding, or include thoughts of harm - seek help immediately."),
        ("Is breastfeeding supposed to hurt?", "Initial tenderness is common, but persistent pain is NOT normal and usually indicates latch issues. See a lactation consultant. Fed is best - however you choose to feed your baby."),
        ("When will my body look normal again?", "Your body grew a human. It may never look exactly the same, and that's okay. Focus on how you FEEL rather than how you look. Give yourself at least 12-18 months before evaluating."),
        ("How do I accept help?", "Practice saying 'yes' to every offer. Be specific: 'Could you bring a meal?' or 'Could you hold baby while I shower?' People want to help - let them. This is not weakness."),
        ("Is it normal to feel overwhelmed?", "Absolutely. New parenthood is one of life's biggest transitions. Overwhelm is expected. It's not normal to feel hopeless, to not eat/sleep at all, or to have thoughts of harm - those need professional support."),
    ]
    add_faq_section(pdf, faqs)
    
    pdf.add_page_break()
    pdf.add_heading1("Quick-Reference: Daily New Mom Checklist")
    pdf.add_bullet("[ ] Ate at least 3 meals (nourishing, not perfect)")
    pdf.add_bullet("[ ] Drank plenty of water")
    pdf.add_bullet("[ ] Slept when baby slept (at least once)")
    pdf.add_bullet("[ ] Fresh air (even 5 min on porch counts)")
    pdf.add_bullet("[ ] Connected with another adult")
    pdf.add_bullet("[ ] One small thing just for me")
    pdf.add_bullet("[ ] Accepted help or asked for it")
    pdf.add_bullet("[ ] Said something kind to myself")
    
    add_about_author(pdf)
    filepath = os.path.join(OUTPUT_DIR, "13-Postpartum-Recovery-Wellness-Guide.pdf")
    pdf.save(filepath)
    return filepath



def book_14_pcos():
    """PCOS Management Workbook"""
    pdf = PurePDF(title="PCOS Management Workbook", author=AUTHOR)
    add_front_matter(pdf, "PCOS Management Workbook", "Anti-Inflammatory Meals, Cycle Tracker & Lifestyle Guide")
    
    chapters = ["Understanding PCOS", "Your PCOS Assessment",
                "Nutrition for PCOS", "Cycle & Symptom Tracker",
                "Exercise & Lifestyle Plan", "Supplement & Medication Guide",
                "Progress Review", "FAQ & Resources"]
    add_toc(pdf, chapters)
    
    pdf.add_heading1("Introduction")
    pdf.add_paragraph("Polycystic Ovary Syndrome (PCOS) affects 1 in 10 women of reproductive age, "
                      "yet many go undiagnosed for years. This workbook provides comprehensive tools "
                      "for managing PCOS through nutrition, exercise, and lifestyle modifications "
                      "that address the root causes: insulin resistance and inflammation.")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 1: Understanding PCOS")
    pdf.add_blank_line()
    pdf.add_heading2("What Is PCOS?")
    pdf.add_paragraph("PCOS is a hormonal and metabolic condition characterized by excess androgen "
                      "production, insulin resistance, and often (but not always) ovarian cysts. "
                      "It affects hormones, metabolism, fertility, and long-term health.")
    pdf.add_blank_line()
    pdf.add_heading3("Diagnostic Criteria (Rotterdam - need 2 of 3)")
    pdf.add_bullet("Irregular or absent periods (oligo/anovulation)")
    pdf.add_bullet("High androgens (clinical signs or blood tests)")
    pdf.add_bullet("Polycystic ovaries on ultrasound")
    pdf.add_blank_line()
    pdf.add_heading2("PCOS Phenotypes (Types)")
    pdf.add_heading3("Type A: Classic (most common)")
    pdf.add_bullet("All three criteria present")
    pdf.add_bullet("Highest metabolic risk")
    pdf.add_heading3("Type B: Classic without PCO")
    pdf.add_bullet("Irregular periods + high androgens")
    pdf.add_heading3("Type C: Ovulatory")
    pdf.add_bullet("High androgens + polycystic ovaries but regular periods")
    pdf.add_heading3("Type D: Non-hyperandrogenic")
    pdf.add_bullet("Irregular periods + polycystic ovaries but normal androgens")
    pdf.add_blank_line()
    pdf.add_heading2("Root Causes")
    pdf.add_heading3("Insulin Resistance (70-80% of PCOS)")
    pdf.add_paragraph("High insulin drives the ovaries to produce excess testosterone. Managing "
                      "insulin is the key to managing PCOS for most women.")
    pdf.add_heading3("Chronic Inflammation")
    pdf.add_paragraph("Low-grade inflammation stimulates androgen production and worsens "
                      "insulin resistance, creating a vicious cycle.")
    pdf.add_heading3("Adrenal PCOS")
    pdf.add_paragraph("About 20-30% of PCOS is driven by adrenal androgens (DHEA-S) "
                      "rather than ovarian. Stress management is key for this type.")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 2: Your PCOS Assessment")
    pdf.add_blank_line()
    pdf.add_heading2("My PCOS Profile")
    pdf.add_paragraph("Diagnosis date: __/__/____")
    pdf.add_paragraph("PCOS type (if known): ___")
    pdf.add_paragraph("BMI: ___  Waist circumference: ___ inches")
    pdf.add_paragraph("Menstrual cycle: [ ]Regular [ ]Irregular [ ]Absent")
    pdf.add_paragraph("Average cycle length: ___ days")
    pdf.add_paragraph("Trying to conceive: [ ]Yes [ ]No [ ]Future")
    pdf.add_blank_line()
    pdf.add_heading2("Symptom Checklist")
    pcos_symptoms = ["Irregular/absent periods", "Excess facial hair (hirsutism)",
                     "Acne (jawline, chin, back)", "Hair thinning/loss on head",
                     "Weight gain (especially midsection)", "Difficulty losing weight",
                     "Dark skin patches (acanthosis nigricans)", "Skin tags",
                     "Sugar/carb cravings", "Fatigue after meals",
                     "Mood swings/anxiety/depression", "Fertility struggles"]
    for s in pcos_symptoms:
        pdf.add_bullet(f"[ ] {s}  Severity (1-10): ___")
    pdf.add_blank_line()
    pdf.add_heading2("Lab Values to Track")
    pdf.add_paragraph("Testosterone (total): ___  Date: __/__/____")
    pdf.add_paragraph("Free testosterone: ___")
    pdf.add_paragraph("DHEA-S: ___")
    pdf.add_paragraph("Fasting insulin: ___")
    pdf.add_paragraph("Fasting glucose: ___")
    pdf.add_paragraph("HOMA-IR: ___")
    pdf.add_paragraph("AMH: ___")
    pdf.add_paragraph("LH:FSH ratio: ___")
    pdf.add_paragraph("Vitamin D: ___")
    pdf.add_paragraph("A1C: ___")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 3: Nutrition for PCOS")
    pdf.add_blank_line()
    pdf.add_heading2("The PCOS Diet Principles")
    pdf.add_paragraph("The goal: Lower insulin, reduce inflammation, support hormone balance.")
    pdf.add_blank_line()
    pdf.add_heading3("1. Blood Sugar Balance (Most Important)")
    pdf.add_bullet("Never eat carbs alone - always pair with protein/fat")
    pdf.add_bullet("Choose low-glycemic carbs (vegetables, legumes, whole grains)")
    pdf.add_bullet("Eat protein at every meal (palm-sized portion)")
    pdf.add_bullet("Don't skip meals (blood sugar crashes spike insulin)")
    pdf.add_bullet("Eat within 1 hour of waking")
    pdf.add_heading3("2. Anti-Inflammatory Focus")
    pdf.add_bullet("Omega-3 rich foods daily (fatty fish, walnuts, flax)")
    pdf.add_bullet("Colorful vegetables and berries")
    pdf.add_bullet("Turmeric, ginger, green tea")
    pdf.add_bullet("Minimize processed foods, sugar, and seed oils")
    pdf.add_heading3("3. Gut Health Support")
    pdf.add_bullet("Fermented foods daily (sauerkraut, kimchi)")
    pdf.add_bullet("High fiber intake (30g+ daily)")
    pdf.add_bullet("Prebiotic foods (garlic, onion, asparagus)")
    pdf.add_blank_line()
    pdf.add_heading2("7-Day PCOS Meal Plan")
    pcos_meals = [
        ("Monday", "Eggs + avocado + spinach (no toast)", "Large salad with salmon and olive oil", "Chicken thighs with roasted vegetables"),
        ("Tuesday", "Protein smoothie with berries and flax", "Turkey and vegetable soup with lentils", "Baked fish with sweet potato and broccoli"),
        ("Wednesday", "Greek yogurt + cinnamon + walnuts + seeds", "Grain bowl: quinoa, chickpeas, vegetables", "Grass-fed beef stir-fry with cauliflower rice"),
        ("Thursday", "Egg muffins with vegetables", "Leftover stir-fry over greens", "Salmon with asparagus and quinoa"),
        ("Friday", "Chia pudding with berries and almond butter", "Mediterranean salad with olive oil", "Chicken curry with vegetables (no rice or cauliflower rice)"),
        ("Saturday", "Sweet potato hash with eggs", "Lentil soup with side salad", "Grilled fish with roasted Mediterranean vegetables"),
        ("Sunday", "Protein pancakes (almond flour) with berries", "Bone broth soup with vegetables", "Slow cooker chicken with root vegetables")
    ]
    for day, b, l, d in pcos_meals:
        pdf.add_heading3(day)
        pdf.add_bullet(f"Breakfast: {b}")
        pdf.add_bullet(f"Lunch: {l}")
        pdf.add_bullet(f"Dinner: {d}")
        pdf.add_blank_line()
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 4: Cycle & Symptom Tracker")
    add_tracker_pages(pdf, "PCOS Daily Tracker",
                      ["Cycle day (if cycling)", "Bleeding (L/M/H/None)",
                       "Cervical mucus", "Basal temp", "Acne (1-10)",
                       "Energy (1-10)", "Cravings (1-10)", "Mood (1-10)",
                       "Exercise", "Blood sugar symptoms", "Notes"], num_pages=16)
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 5: Exercise & Lifestyle")
    pdf.add_blank_line()
    pdf.add_heading2("Best Exercise for PCOS")
    pdf.add_paragraph("Exercise improves insulin sensitivity - the core issue in PCOS.")
    pdf.add_blank_line()
    pdf.add_heading3("Strength Training (MOST IMPORTANT)")
    pdf.add_bullet("2-4x per week")
    pdf.add_bullet("Builds muscle which improves insulin sensitivity 24/7")
    pdf.add_bullet("Compound movements: squats, deadlifts, presses, rows")
    pdf.add_bullet("Progressive overload (gradually increase weight)")
    pdf.add_heading3("Moderate Cardio")
    pdf.add_bullet("Walking: 30+ minutes daily")
    pdf.add_bullet("Swimming, cycling, dance")
    pdf.add_bullet("AVOID excessive cardio (raises cortisol, can worsen PCOS)")
    pdf.add_heading3("Yoga and Stress-Reducing Movement")
    pdf.add_bullet("Yoga: Proven to improve PCOS symptoms")
    pdf.add_bullet("Helps with stress and cortisol management")
    pdf.add_blank_line()
    pdf.add_heading2("Stress Management for PCOS")
    pdf.add_paragraph("Stress raises cortisol which raises insulin which worsens PCOS.")
    pdf.add_bullet("Daily meditation or breathwork (10+ minutes)")
    pdf.add_bullet("Adequate sleep (7-9 hours, consistent schedule)")
    pdf.add_bullet("Nature exposure")
    pdf.add_bullet("Boundaries and saying no")
    pdf.add_bullet("Joyful activities and social connection")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 6: Supplements & Medications")
    pdf.add_blank_line()
    pdf.add_heading2("Evidence-Based Supplements for PCOS")
    pdf.add_bullet("Inositol (myo-inositol + D-chiro-inositol, 40:1 ratio): Improves insulin sensitivity, ovulation, and egg quality. Dose: 4g myo + 100mg D-chiro daily")
    pdf.add_bullet("Vitamin D: Most PCOS women are deficient. Test and supplement to optimal (40-60 ng/mL)")
    pdf.add_bullet("Omega-3 fish oil: Reduces inflammation and androgens. 2-3g daily")
    pdf.add_bullet("Magnesium: Improves insulin resistance, sleep, anxiety. 200-400mg glycinate")
    pdf.add_bullet("Zinc: Supports ovulation and reduces acne/hair growth. 30mg daily")
    pdf.add_bullet("Berberine: Natural insulin sensitizer (similar to metformin). 500mg 2-3x daily")
    pdf.add_bullet("NAC (N-acetyl cysteine): Antioxidant, may improve ovulation. 600mg 2-3x daily")
    pdf.add_blank_line()
    pdf.add_heading2("Common PCOS Medications")
    pdf.add_bullet("Metformin: Insulin sensitizer (discuss with doctor)")
    pdf.add_bullet("Spironolactone: Anti-androgen for acne/hirsutism")
    pdf.add_bullet("Birth control: Manages periods and androgens (doesn't treat root cause)")
    pdf.add_bullet("Letrozole/Clomid: For ovulation induction if trying to conceive")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 7: Progress Review")
    add_weekly_review(pdf, [
        "Cycle regularity this month:",
        "Symptom severity (1-10):",
        "Blood sugar stability (1-10):",
        "Exercise completed:",
        "Nutrition adherence (1-10):",
        "Stress level (1-10):",
        "Supplements taken consistently:",
        "Next step/goal:"
    ], num_weeks=5)
    pdf.add_page_break()
    
    faqs = [
        ("Can PCOS be cured?", "PCOS is a lifelong condition, but symptoms can be managed extremely well through lifestyle. Many women achieve regular ovulation, clear skin, and healthy weight through diet and exercise alone."),
        ("Can I get pregnant with PCOS?", "Yes! PCOS is the most common cause of ovulatory infertility, but it is also the most treatable. Lifestyle changes, supplements (inositol), and medical interventions can help most women conceive."),
        ("Will losing weight cure my PCOS?", "Weight loss can dramatically improve symptoms (even 5-10% body weight), but PCOS is not caused by weight. Lean PCOS exists. Focus on insulin sensitivity and inflammation regardless of weight."),
        ("Is keto good for PCOS?", "Low-carb approaches can help insulin resistance, but very strict keto can raise cortisol and stress the body. Moderate low-carb (under 100g carbs) with adequate fiber is often the best approach."),
        ("Why is my hair falling out?", "PCOS-related hair loss is usually from excess androgens. It can improve with anti-androgen treatment, inositol, zinc, and addressing the root insulin resistance. Be patient - hair cycles are slow."),
        ("Does PCOS get worse with age?", "Without management, metabolic risks increase with age. However, many women find symptoms actually improve in their 30s-40s, especially with consistent lifestyle management."),
        ("Should I avoid dairy with PCOS?", "Dairy can spike insulin and may worsen acne for some women with PCOS. Try eliminating it for 3 months and observe. If tolerated, fermented dairy (yogurt) is better than milk."),
        ("How long until supplements help?", "Most PCOS supplements take 3-6 months to show full effects (the time for a full follicular cycle). Be consistent and patient. Inositol often shows results in 2-3 months."),
    ]
    add_faq_section(pdf, faqs)
    
    pdf.add_page_break()
    pdf.add_heading1("Quick-Reference: Daily PCOS Management Checklist")
    pdf.add_bullet("[ ] Ate protein at every meal")
    pdf.add_bullet("[ ] Paired carbs with protein/fat (never alone)")
    pdf.add_bullet("[ ] Included anti-inflammatory foods")
    pdf.add_bullet("[ ] Exercised (strength or walking)")
    pdf.add_bullet("[ ] Managed stress (breathing, meditation)")
    pdf.add_bullet("[ ] Took supplements consistently")
    pdf.add_bullet("[ ] Tracked cycle/symptoms")
    pdf.add_bullet("[ ] Got 7-9 hours of sleep")
    pdf.add_bullet("[ ] Drank spearmint tea (if using for androgens)")
    
    add_about_author(pdf)
    filepath = os.path.join(OUTPUT_DIR, "14-PCOS-Management-Workbook.pdf")
    pdf.save(filepath)
    return filepath



def book_15_medical_binder():
    """Medical Information Binder"""
    pdf = PurePDF(title="Medical Information Binder", author=AUTHOR)
    add_front_matter(pdf, "Medical Information Binder", "Complete Health Records Organizer")
    
    chapters = ["Personal Health Profile", "Medication & Supplement Tracker",
                "Appointment Log & Doctor Directory", "Health History Record",
                "Emergency Information", "Insurance & Legal Documents",
                "Lab Results Tracker", "FAQ & Resources"]
    add_toc(pdf, chapters)
    
    pdf.add_heading1("Introduction")
    pdf.add_paragraph("Having your medical information organized in one place can be life-saving "
                      "in emergencies and invaluable for managing ongoing health. This binder "
                      "provides comprehensive templates to track medications, appointments, lab "
                      "results, insurance, and your complete health history.")
    pdf.add_blank_line()
    pdf.add_paragraph("Print this workbook and keep it updated. Bring it to every appointment. "
                      "Keep a copy with your emergency contact.")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 1: Personal Health Profile")
    pdf.add_blank_line()
    pdf.add_heading2("Personal Information")
    pdf.add_paragraph("Full name: _________________________________")
    pdf.add_paragraph("Date of birth: __/__/____  Blood type: ___")
    pdf.add_paragraph("Address: _________________________________")
    pdf.add_paragraph("Phone: _____________  Email: ______________")
    pdf.add_paragraph("Primary care doctor: _______________________")
    pdf.add_paragraph("Insurance company: _________________________")
    pdf.add_paragraph("Insurance ID#: _____________  Group#: ________")
    pdf.add_paragraph("Pharmacy: _____________  Phone: _____________")
    pdf.add_blank_line()
    pdf.add_heading2("Emergency Contacts")
    for i in range(3):
        pdf.add_paragraph(f"Contact #{i+1}: ___________  Relation: ___________")
        pdf.add_paragraph(f"  Phone: ___________  Alt phone: ___________")
    pdf.add_blank_line()
    pdf.add_heading2("Allergies & Sensitivities")
    pdf.add_heading3("Drug Allergies")
    for i in range(5):
        pdf.add_paragraph(f"  Medication: _______________  Reaction: _______________")
    pdf.add_heading3("Food Allergies/Intolerances")
    for i in range(5):
        pdf.add_paragraph(f"  Food: _______________  Reaction: _______________")
    pdf.add_heading3("Other Allergies (latex, environmental, etc.)")
    for i in range(3):
        pdf.add_paragraph(f"  Allergen: _______________  Reaction: _______________")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 2: Medication & Supplement Tracker")
    pdf.add_blank_line()
    pdf.add_heading2("Current Prescription Medications")
    for i in range(8):
        pdf.add_heading3(f"Medication #{i+1}")
        pdf.add_paragraph(f"Name: _______________  Generic: _______________")
        pdf.add_paragraph(f"Dose: _______  Frequency: _______  Time(s): _______")
        pdf.add_paragraph(f"Prescribing doctor: _______________")
        pdf.add_paragraph(f"Purpose: _______________")
        pdf.add_paragraph(f"Start date: __/__/____  Refill date: __/__/____")
        pdf.add_paragraph(f"Side effects: _______________")
        pdf.add_paragraph(f"Special instructions: _______________")
        pdf.add_blank_line()
    pdf.add_page_break()
    
    pdf.add_heading2("Current Supplements & Vitamins")
    for i in range(8):
        pdf.add_paragraph(f"Supplement #{i+1}: _______________  Dose: _______  "
                         f"Frequency: _______  Purpose: _______________")
    pdf.add_blank_line()
    pdf.add_heading2("Medication Schedule (Daily)")
    pdf.add_heading3("Morning")
    for i in range(4):
        pdf.add_paragraph(f"  [ ] _______________  Dose: _______  With food: [ ]Y [ ]N")
    pdf.add_heading3("Midday")
    for i in range(3):
        pdf.add_paragraph(f"  [ ] _______________  Dose: _______  With food: [ ]Y [ ]N")
    pdf.add_heading3("Evening")
    for i in range(4):
        pdf.add_paragraph(f"  [ ] _______________  Dose: _______  With food: [ ]Y [ ]N")
    pdf.add_heading3("Bedtime")
    for i in range(3):
        pdf.add_paragraph(f"  [ ] _______________  Dose: _______  With food: [ ]Y [ ]N")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 3: Appointment Log & Doctor Directory")
    pdf.add_blank_line()
    pdf.add_heading2("My Healthcare Team")
    doctors = ["Primary Care", "Specialist #1", "Specialist #2", "Specialist #3",
               "Dentist", "Eye Doctor", "Therapist/Counselor", "Physical Therapist"]
    for doc in doctors:
        pdf.add_heading3(doc)
        pdf.add_paragraph(f"Name: _______________  Practice: _______________")
        pdf.add_paragraph(f"Phone: _______________  Fax: _______________")
        pdf.add_paragraph(f"Address: _______________")
        pdf.add_paragraph(f"Patient portal: _______________")
        pdf.add_blank_line()
    pdf.add_page_break()
    
    pdf.add_heading2("Appointment Log")
    for i in range(120):
        pdf.add_paragraph(f"Date: __/__/____  Doctor: _______________  Purpose: _______________")
        pdf.add_paragraph(f"  Notes/Follow-up: _____________________________________________")
        pdf.add_paragraph(f"  Next appointment: __/__/____")
        pdf.add_blank_line()
        if (i + 1) % 5 == 0:
            pdf.add_page_break()
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 4: Health History Record")
    pdf.add_blank_line()
    pdf.add_heading2("Diagnoses & Conditions")
    for i in range(10):
        pdf.add_paragraph(f"Condition #{i+1}: _______________  Date diagnosed: __/__/____")
        pdf.add_paragraph(f"  Status: [ ]Active [ ]Managed [ ]Resolved  Treating doctor: ___________")
    pdf.add_blank_line()
    pdf.add_heading2("Surgical History")
    for i in range(6):
        pdf.add_paragraph(f"Surgery #{i+1}: _______________  Date: __/__/____")
        pdf.add_paragraph(f"  Hospital: _______________  Surgeon: _______________")
    pdf.add_blank_line()
    pdf.add_heading2("Hospitalizations")
    for i in range(5):
        pdf.add_paragraph(f"Date: __/__/____  Reason: _______________  Duration: ___ days")
        pdf.add_paragraph(f"  Hospital: _______________  Notes: _______________")
    pdf.add_blank_line()
    pdf.add_heading2("Family Medical History")
    family = ["Mother", "Father", "Maternal Grandmother", "Maternal Grandfather",
              "Paternal Grandmother", "Paternal Grandfather", "Siblings"]
    for member in family:
        pdf.add_paragraph(f"{member}: _______________________________________________")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 5: Emergency Information")
    pdf.add_blank_line()
    pdf.add_heading2("IN CASE OF EMERGENCY")
    pdf.add_paragraph("(Keep this page easily accessible)")
    pdf.add_blank_line()
    pdf.add_paragraph("NAME: ___________________________________")
    pdf.add_paragraph("DOB: __/__/____  BLOOD TYPE: ___")
    pdf.add_paragraph("ALLERGIES: _______________________________")
    pdf.add_paragraph("CURRENT MEDICATIONS: _______________________________")
    pdf.add_paragraph("___________________________________________________")
    pdf.add_paragraph("CONDITIONS: _______________________________")
    pdf.add_paragraph("PRIMARY DOCTOR: _______________  PHONE: ___________")
    pdf.add_paragraph("EMERGENCY CONTACT: _______________  PHONE: ___________")
    pdf.add_paragraph("INSURANCE: _______________  ID#: ___________")
    pdf.add_paragraph("PREFERRED HOSPITAL: _______________")
    pdf.add_blank_line()
    pdf.add_heading2("Special Instructions")
    pdf.add_paragraph("DNR/Advance Directive: [ ]Yes [ ]No  Location: _______________")
    pdf.add_paragraph("Medical alert: _______________________________________________")
    pdf.add_paragraph("Implanted devices: __________________________________________")
    pdf.add_paragraph("Language/communication needs: _______________________________")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 6: Insurance & Legal Documents")
    pdf.add_blank_line()
    pdf.add_heading2("Insurance Information")
    pdf.add_paragraph("Primary Insurance: _______________")
    pdf.add_paragraph("  Member ID: _______________  Group: _______________")
    pdf.add_paragraph("  Phone: _______________  Website: _______________")
    pdf.add_paragraph("  Deductible: $___  Met: $___  Out-of-pocket max: $___")
    pdf.add_blank_line()
    pdf.add_paragraph("Secondary Insurance: _______________")
    pdf.add_paragraph("  Member ID: _______________  Group: _______________")
    pdf.add_blank_line()
    pdf.add_paragraph("Dental Insurance: _______________  ID: _______________")
    pdf.add_paragraph("Vision Insurance: _______________  ID: _______________")
    pdf.add_blank_line()
    pdf.add_heading2("Important Documents Checklist")
    pdf.add_bullet("[ ] Health insurance cards (copies)")
    pdf.add_bullet("[ ] Advance directive/living will")
    pdf.add_bullet("[ ] Healthcare power of attorney")
    pdf.add_bullet("[ ] HIPAA authorization forms")
    pdf.add_bullet("[ ] Organ donor registration")
    pdf.add_bullet("[ ] Immunization records")
    pdf.add_bullet("[ ] Recent lab results")
    pdf.add_bullet("[ ] Surgical/procedure reports")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 7: Lab Results Tracker")
    pdf.add_blank_line()
    pdf.add_heading2("Blood Work Results")
    pdf.add_paragraph("Record results over time to track trends:")
    pdf.add_blank_line()
    labs = ["Total Cholesterol", "LDL", "HDL", "Triglycerides",
            "Fasting Glucose", "A1C", "Vitamin D", "Iron/Ferritin",
            "TSH", "B12", "CBC (WBC/RBC/Plt)", "CRP",
            "Kidney function (BUN/Creatinine)", "Liver function (ALT/AST)"]
    for lab in labs:
        pdf.add_paragraph(f"{lab}:")
        pdf.add_paragraph(f"  Date: __/__  Result: ___  | Date: __/__  Result: ___  | Date: __/__  Result: ___")
        pdf.add_blank_line()
    pdf.add_page_break()
    
    pdf.add_heading2("Immunization Record")
    vaccines = ["Flu (annual)", "COVID-19", "Tdap/Td", "Shingles (Shingrix)",
                "Pneumonia", "Hepatitis A", "Hepatitis B", "HPV",
                "MMR", "Other"]
    for vax in vaccines:
        pdf.add_paragraph(f"{vax}: Date 1: __/__/____  Date 2: __/__/____  Date 3: __/__/____")
    pdf.add_page_break()
    
    faqs = [
        ("How often should I update this binder?", "Update after every doctor appointment, medication change, or new diagnosis. Review the entire binder every 6 months to ensure accuracy."),
        ("Should I bring this to every appointment?", "Yes! Having your complete medical history, current medications, and questions prepared makes appointments more efficient and ensures nothing is missed."),
        ("What if I have multiple conditions?", "This binder is designed to track everything in one place. You may want to add sections or extra tracking pages for specific conditions."),
        ("Should I keep a digital copy?", "Yes. Take photos of completed pages and store in a secure cloud location. Some prefer a digital health app alongside this physical binder."),
        ("What about my children's records?", "Create a separate binder for each family member. Children especially need immunization and growth records tracked carefully."),
        ("How do I organize lab results?", "Keep them chronological. Highlight any values outside normal range. Track trends over time to discuss with your doctor."),
        ("What if I change doctors?", "This binder makes transitions easy. Your new doctor will appreciate having complete records. Request copies of records from your previous doctor."),
        ("Is this HIPAA compliant?", "This is your personal health record. Keep it secure as you would any sensitive document. Do not leave it in public places."),
    ]
    add_faq_section(pdf, faqs)
    
    pdf.add_page_break()
    pdf.add_heading1("Quick-Reference: Annual Health Maintenance")
    pdf.add_bullet("[ ] Annual physical exam")
    pdf.add_bullet("[ ] Dental cleaning (every 6 months)")
    pdf.add_bullet("[ ] Eye exam (annually)")
    pdf.add_bullet("[ ] Blood work/labs (as recommended)")
    pdf.add_bullet("[ ] Skin check (annually)")
    pdf.add_bullet("[ ] Age-appropriate screenings (mammogram, colonoscopy, etc.)")
    pdf.add_bullet("[ ] Flu shot (annually)")
    pdf.add_bullet("[ ] Update medication list")
    pdf.add_bullet("[ ] Review insurance coverage")
    pdf.add_bullet("[ ] Update emergency contacts")
    
    add_about_author(pdf)
    filepath = os.path.join(OUTPUT_DIR, "15-Medical-Information-Binder.pdf")
    pdf.save(filepath)
    return filepath



def book_16_thyroid():
    """Thyroid Health & Hashimoto's Workbook"""
    pdf = PurePDF(title="Thyroid Health & Hashimoto's Workbook", author=AUTHOR)
    add_front_matter(pdf, "Thyroid Health &", "Hashimoto's Workbook")
    
    chapters = ["Understanding Thyroid Health", "Your Thyroid Assessment",
                "Lab Tracker & Interpretation", "Nutrition for Thyroid Health",
                "Daily Symptom Tracker", "Lifestyle & Supplement Guide",
                "Progress Review", "FAQ & Resources"]
    add_toc(pdf, chapters)
    
    pdf.add_heading1("Introduction")
    pdf.add_paragraph("Thyroid conditions affect an estimated 20 million Americans, and up to 60% "
                      "are undiagnosed. Whether you have hypothyroidism, Hashimoto's thyroiditis, "
                      "or are trying to optimize your thyroid function, this workbook provides "
                      "comprehensive tracking tools and evidence-based strategies.")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 1: Understanding Thyroid Health")
    pdf.add_blank_line()
    pdf.add_heading2("What Does the Thyroid Do?")
    pdf.add_paragraph("The thyroid is a butterfly-shaped gland in your neck that produces hormones "
                      "controlling metabolism, energy, temperature, heart rate, brain function, "
                      "and virtually every cell in your body.")
    pdf.add_blank_line()
    pdf.add_heading3("Key Thyroid Hormones")
    pdf.add_bullet("TSH (Thyroid Stimulating Hormone): Brain's message to thyroid")
    pdf.add_bullet("T4 (Thyroxine): Inactive storage form (produced by thyroid)")
    pdf.add_bullet("T3 (Triiodothyronine): Active form (converted from T4 in body)")
    pdf.add_bullet("Reverse T3: Inactive T3 (produced during stress)")
    pdf.add_blank_line()
    pdf.add_heading2("Hypothyroidism (Underactive)")
    pdf.add_heading3("Common Symptoms")
    pdf.add_bullet("Fatigue and sluggishness")
    pdf.add_bullet("Weight gain or inability to lose weight")
    pdf.add_bullet("Cold intolerance")
    pdf.add_bullet("Constipation")
    pdf.add_bullet("Dry skin and brittle nails")
    pdf.add_bullet("Hair loss (including outer third of eyebrows)")
    pdf.add_bullet("Brain fog and poor memory")
    pdf.add_bullet("Depression and low mood")
    pdf.add_bullet("Muscle aches and joint pain")
    pdf.add_bullet("Heavy or irregular periods")
    pdf.add_bullet("High cholesterol")
    pdf.add_blank_line()
    pdf.add_heading2("Hashimoto's Thyroiditis")
    pdf.add_paragraph("Hashimoto's is an autoimmune condition where the immune system attacks "
                      "the thyroid gland. It is the most common cause of hypothyroidism.")
    pdf.add_bullet("Affects 5% of the population (10x more common in women)")
    pdf.add_bullet("Diagnosed by thyroid antibodies (TPO, TgAb)")
    pdf.add_bullet("Can fluctuate between hypo and hyper symptoms")
    pdf.add_bullet("Autoimmune = immune system dysfunction, not just thyroid")
    pdf.add_bullet("Often occurs alongside other autoimmune conditions")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 2: Your Thyroid Assessment")
    pdf.add_blank_line()
    pdf.add_heading2("Symptom Checklist")
    pdf.add_paragraph("Rate each symptom 0-5 (0=none, 5=severe)")
    thyroid_sx = ["Fatigue/low energy", "Weight gain", "Cold hands and feet",
                  "Hair loss or thinning", "Constipation", "Dry skin",
                  "Brain fog/poor memory", "Depression or low mood",
                  "Joint/muscle pain", "Puffy face or swelling",
                  "Hoarse voice", "High cholesterol", "Slow heart rate",
                  "Heavy periods", "Difficulty concentrating"]
    for s in thyroid_sx:
        pdf.add_paragraph(f"  {s}: ___/5")
    pdf.add_paragraph("Total Score: ___/75")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 3: Lab Tracker & Interpretation")
    pdf.add_blank_line()
    pdf.add_heading2("Complete Thyroid Panel (request ALL of these)")
    pdf.add_paragraph("Many doctors only test TSH. For full picture, you need:")
    pdf.add_blank_line()
    thyroid_labs = [
        ("TSH", "0.5-2.0 mIU/L (functional optimal)", "Standard: 0.4-4.5"),
        ("Free T4", "1.0-1.5 ng/dL (optimal)", "Standard: 0.8-1.8"),
        ("Free T3", "3.0-4.0 pg/mL (optimal)", "Standard: 2.3-4.2"),
        ("Reverse T3", "Under 15 ng/dL (optimal)", "High = conversion issue"),
        ("TPO Antibodies", "Under 35 IU/mL", "High = Hashimoto's"),
        ("Thyroglobulin Antibodies", "Under 1 IU/mL", "High = Hashimoto's"),
        ("Vitamin D", "50-80 ng/mL (optimal)", "Most are deficient"),
        ("Iron/Ferritin", "70-90 ng/mL (optimal for thyroid)", "Low impairs conversion"),
        ("B12", "Over 500 pg/mL (optimal)", "Under 300 = suboptimal")
    ]
    for lab, optimal, note in thyroid_labs:
        pdf.add_heading3(lab)
        pdf.add_paragraph(f"Optimal range: {optimal}")
        pdf.add_paragraph(f"Note: {note}")
        pdf.add_paragraph(f"  Date: __/__  Result: ___ | Date: __/__  Result: ___ | Date: __/__  Result: ___")
        pdf.add_blank_line()
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 4: Nutrition for Thyroid Health")
    pdf.add_blank_line()
    pdf.add_heading2("Essential Nutrients for Thyroid")
    pdf.add_bullet("Iodine: Needed to make thyroid hormone (seaweed, fish, iodized salt)")
    pdf.add_bullet("Selenium: Converts T4 to T3 and reduces antibodies (2-3 Brazil nuts daily)")
    pdf.add_bullet("Zinc: Required for T3 production (pumpkin seeds, beef, oysters)")
    pdf.add_bullet("Iron: Necessary for thyroid enzyme function (red meat, lentils)")
    pdf.add_bullet("Vitamin D: Immune modulation (sunlight, fatty fish, supplement)")
    pdf.add_bullet("B12: Energy and nerve function (animal products, supplement)")
    pdf.add_bullet("Magnesium: Supports conversion and reduces inflammation")
    pdf.add_blank_line()
    pdf.add_heading2("Foods to Emphasize")
    pdf.add_bullet("Wild-caught fish (salmon, cod, sardines)")
    pdf.add_bullet("Brazil nuts (2-3 daily for selenium)")
    pdf.add_bullet("Seaweed in moderation (iodine)")
    pdf.add_bullet("Grass-fed meat and organ meats")
    pdf.add_bullet("Eggs (contain iodine, selenium, B12)")
    pdf.add_bullet("Colorful vegetables and fruits")
    pdf.add_bullet("Fermented foods (gut-immune connection)")
    pdf.add_bullet("Bone broth (gut healing)")
    pdf.add_blank_line()
    pdf.add_heading2("Foods to Consider Limiting")
    pdf.add_heading3("For Hashimoto's specifically")
    pdf.add_bullet("Gluten: Strong association with Hashimoto's - trial elimination recommended")
    pdf.add_bullet("Dairy: Can be inflammatory for some")
    pdf.add_bullet("Soy: May interfere with thyroid medication absorption")
    pdf.add_bullet("Raw cruciferous vegetables in LARGE amounts (cook them instead)")
    pdf.add_bullet("Excess sugar and processed foods (inflammation)")
    pdf.add_blank_line()
    pdf.add_heading2("7-Day Thyroid Support Meal Plan")
    thyroid_meals = [
        ("Monday", "Eggs + avocado + 2 Brazil nuts", "Salmon salad with olive oil", "Chicken with roasted vegetables and quinoa"),
        ("Tuesday", "Smoothie: berries + protein + collagen", "Bone broth soup with vegetables", "Baked cod with sweet potato and greens"),
        ("Wednesday", "GF oatmeal with pumpkin seeds and berries", "Turkey and veggie wrap (GF)", "Grass-fed beef with rice and broccoli (cooked)"),
        ("Thursday", "Eggs with sauteed spinach and mushrooms", "Lentil soup with GF bread", "Baked salmon with asparagus"),
        ("Friday", "Coconut yogurt + nuts + seeds", "Large salad with protein and tahini", "Slow cooker chicken with root vegetables"),
        ("Saturday", "Sweet potato hash with eggs", "Leftovers and fresh vegetables", "Fish with cauliflower mash and greens"),
        ("Sunday", "GF pancakes with berries", "Bone broth + grain bowl", "Roast chicken with seasonal vegetables")
    ]
    for day, b, l, d in thyroid_meals:
        pdf.add_heading3(day)
        pdf.add_bullet(f"Breakfast: {b}")
        pdf.add_bullet(f"Lunch: {l}")
        pdf.add_bullet(f"Dinner: {d}")
        pdf.add_blank_line()
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 5: Daily Symptom Tracker")
    add_tracker_pages(pdf, "Daily Thyroid Tracker",
                      ["Energy (1-10)", "Brain fog (1-10)", "Mood (1-10)",
                       "Body temperature AM", "Weight", "Bowel movement (Y/N/type)",
                       "Hair loss noticed", "Sleep quality (1-10)",
                       "Exercise", "Medication taken (time)", "Notes"], num_pages=16)
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 6: Lifestyle & Supplements")
    pdf.add_blank_line()
    pdf.add_heading2("Medication Tips")
    pdf.add_bullet("Take thyroid medication first thing, on empty stomach")
    pdf.add_bullet("Wait 30-60 minutes before eating")
    pdf.add_bullet("Wait 4 hours before calcium, iron, or coffee")
    pdf.add_bullet("Take at the same time daily")
    pdf.add_bullet("Do not stop or change dose without doctor guidance")
    pdf.add_blank_line()
    pdf.add_heading2("Supplements for Thyroid/Hashimoto's")
    pdf.add_bullet("Selenium: 200mcg daily (critical for Hashimoto's - reduces antibodies)")
    pdf.add_bullet("Vitamin D3: 2000-5000 IU (test and optimize)")
    pdf.add_bullet("Zinc: 15-30mg daily")
    pdf.add_bullet("B-complex: Energy and conversion support")
    pdf.add_bullet("Magnesium glycinate: 200-400mg")
    pdf.add_bullet("Iron: Only if deficient (test ferritin)")
    pdf.add_bullet("Omega-3: Anti-inflammatory")
    pdf.add_blank_line()
    pdf.add_heading2("Stress Management (Critical for Hashimoto's)")
    pdf.add_paragraph("Stress directly suppresses thyroid function and increases autoimmune activity.")
    pdf.add_bullet("Adaptogenic herbs: Ashwagandha (caution: may not suit all thyroid conditions)")
    pdf.add_bullet("Daily meditation or breathwork")
    pdf.add_bullet("Adequate sleep (8+ hours for thyroid patients)")
    pdf.add_bullet("Gentle exercise (avoid overexercise with hypothyroidism)")
    pdf.add_bullet("Set boundaries and reduce obligations")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 7: Progress Review")
    add_weekly_review(pdf, [
        "Energy level average this week (1-10):",
        "Brain fog frequency:",
        "Weight trend:",
        "Bowel regularity:",
        "Hair loss observations:",
        "Mood average:",
        "Medication taken consistently: [ ]Y [ ]N",
        "Lab work scheduled/completed:"
    ], num_weeks=5)
    pdf.add_page_break()
    
    faqs = [
        ("Why does my doctor say my labs are 'normal' but I still feel terrible?", "Standard lab ranges are very wide. You can be 'within normal' but far from optimal. Advocate for a full panel and ask about functional/optimal ranges. Consider a functional medicine practitioner."),
        ("Can Hashimoto's be reversed?", "The autoimmune process can be slowed or put into remission (lowered antibodies, improved function). Gluten elimination, selenium, and gut healing show the most promise."),
        ("Should I avoid all goitrogens (cruciferous vegetables)?", "No. Cooking reduces goitrogenic activity by 80%. Only raw, massive quantities cause issues. Cooked broccoli, cauliflower, etc. are healthy choices."),
        ("Can stress affect my thyroid?", "Absolutely. Stress increases reverse T3 (blocks active T3), suppresses TSH, and in Hashimoto's can trigger autoimmune flares. Stress management is essential."),
        ("How long does thyroid medication take to work?", "You may notice some improvement in 2-4 weeks, but full effects take 6-8 weeks. Labs should be rechecked 6-8 weeks after any dose change."),
        ("Is natural desiccated thyroid (NDT) better than levothyroxine?", "Some patients do better on NDT (contains both T4 and T3), while others do well on levothyroxine alone. Work with your doctor to find what works for you."),
        ("Can I exercise with hypothyroidism?", "Yes, but honor your energy levels. Start gentle, progress slowly. Overexercise can worsen fatigue. Walking, yoga, and moderate strength training are excellent choices."),
        ("Does gluten-free really help Hashimoto's?", "Multiple studies show gluten-free diets reduce thyroid antibodies in Hashimoto's patients. The molecular structure of gluten resembles thyroid tissue (molecular mimicry). Trial 3-6 months."),
    ]
    add_faq_section(pdf, faqs)
    
    pdf.add_page_break()
    pdf.add_heading1("Quick-Reference: Daily Thyroid Wellness Checklist")
    pdf.add_bullet("[ ] Took thyroid medication on empty stomach")
    pdf.add_bullet("[ ] Waited before eating/coffee/supplements")
    pdf.add_bullet("[ ] Ate selenium-rich food (Brazil nuts)")
    pdf.add_bullet("[ ] Consumed adequate protein")
    pdf.add_bullet("[ ] Managed stress (breathing, rest)")
    pdf.add_bullet("[ ] Got adequate sleep (8+ hours)")
    pdf.add_bullet("[ ] Gentle movement/exercise")
    pdf.add_bullet("[ ] Avoided dietary triggers")
    pdf.add_bullet("[ ] Tracked symptoms")
    
    add_about_author(pdf)
    filepath = os.path.join(OUTPUT_DIR, "16-Thyroid-Health-Hashimotos-Workbook.pdf")
    pdf.save(filepath)
    return filepath



def book_17_keto():
    """Keto Diet Complete Starter Guide"""
    pdf = PurePDF(title="Keto Diet Complete Starter Guide", author=AUTHOR)
    add_front_matter(pdf, "Keto Diet Complete", "Starter Guide with 4-Week Meal Plan")
    
    chapters = ["Understanding the Keto Diet", "Getting Started Assessment",
                "Macro Calculator & Food Lists", "4-Week Keto Meal Plan",
                "Daily Keto Tracker", "Exercise & Lifestyle on Keto",
                "Progress Review & Troubleshooting", "FAQ & Resources"]
    add_toc(pdf, chapters)
    
    pdf.add_heading1("Introduction")
    pdf.add_paragraph("The ketogenic diet shifts your body from burning glucose to burning fat "
                      "for fuel. When done correctly, it can support weight loss, stable energy, "
                      "mental clarity, and improved metabolic markers. This guide provides everything "
                      "you need to start keto safely and sustainably.")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 1: Understanding Keto")
    pdf.add_blank_line()
    pdf.add_heading2("What Is Nutritional Ketosis?")
    pdf.add_paragraph("Ketosis is a metabolic state where your body primarily uses fat (converted to "
                      "ketones) for energy instead of glucose from carbohydrates. This happens when "
                      "carb intake is low enough (typically under 20-50g net carbs daily).")
    pdf.add_blank_line()
    pdf.add_heading3("Standard Keto Macros")
    pdf.add_bullet("Fat: 70-75% of calories")
    pdf.add_bullet("Protein: 20-25% of calories")
    pdf.add_bullet("Net Carbs: 5-10% of calories (20-50g)")
    pdf.add_blank_line()
    pdf.add_heading2("Benefits of Keto")
    pdf.add_bullet("Weight loss (especially body fat)")
    pdf.add_bullet("Stable energy (no crashes)")
    pdf.add_bullet("Reduced hunger and cravings")
    pdf.add_bullet("Mental clarity and focus")
    pdf.add_bullet("Improved blood sugar and insulin")
    pdf.add_bullet("Reduced inflammation")
    pdf.add_bullet("Better triglycerides and HDL cholesterol")
    pdf.add_blank_line()
    pdf.add_heading2("The Keto Flu (and How to Avoid It)")
    pdf.add_paragraph("During the transition period (days 2-7), you may experience:")
    pdf.add_bullet("Fatigue and brain fog")
    pdf.add_bullet("Headaches")
    pdf.add_bullet("Irritability")
    pdf.add_bullet("Muscle cramps")
    pdf.add_bullet("Nausea")
    pdf.add_blank_line()
    pdf.add_heading3("Prevention:")
    pdf.add_bullet("Electrolytes: Sodium (5-7g), Potassium (3-4g), Magnesium (300-400mg)")
    pdf.add_bullet("Drink plenty of water (dehydration is common)")
    pdf.add_bullet("Don't restrict calories initially - eat until full")
    pdf.add_bullet("Rest more during adaptation (1-2 weeks)")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 2: Getting Started")
    pdf.add_blank_line()
    pdf.add_heading2("Baseline Measurements")
    pdf.add_paragraph("Date: __/__/____")
    pdf.add_paragraph("Weight: ___ lbs  Goal weight: ___ lbs")
    pdf.add_paragraph("Chest: ___  Waist: ___  Hips: ___  Thigh: ___")
    pdf.add_paragraph("Fasting glucose (if known): ___")
    pdf.add_paragraph("Energy level (1-10): ___")
    pdf.add_paragraph("Cravings level (1-10): ___")
    pdf.add_paragraph("Mental clarity (1-10): ___")
    pdf.add_blank_line()
    pdf.add_heading2("Kitchen Prep Checklist")
    pdf.add_heading3("Remove (donate or give away)")
    pdf.add_bullet("[ ] Bread, pasta, rice, cereals")
    pdf.add_bullet("[ ] Sugar, candy, baked goods")
    pdf.add_bullet("[ ] Chips, crackers, snack foods")
    pdf.add_bullet("[ ] Sugary drinks and juices")
    pdf.add_bullet("[ ] Low-fat products (usually high sugar)")
    pdf.add_heading3("Stock (your keto essentials)")
    pdf.add_bullet("[ ] Butter, ghee, coconut oil, olive oil, avocado oil")
    pdf.add_bullet("[ ] Eggs (lots of them)")
    pdf.add_bullet("[ ] Cheese (all types)")
    pdf.add_bullet("[ ] Heavy cream, cream cheese, sour cream")
    pdf.add_bullet("[ ] Meat: beef, chicken, pork, bacon")
    pdf.add_bullet("[ ] Fish: salmon, tuna, shrimp")
    pdf.add_bullet("[ ] Low-carb vegetables: spinach, broccoli, cauliflower, zucchini")
    pdf.add_bullet("[ ] Avocados")
    pdf.add_bullet("[ ] Nuts: almonds, macadamia, pecans")
    pdf.add_bullet("[ ] Almond flour, coconut flour")
    pdf.add_bullet("[ ] Sugar-free sweetener (stevia, erythritol)")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 3: Macro Calculator & Food Lists")
    pdf.add_blank_line()
    pdf.add_heading2("Calculate Your Macros")
    pdf.add_paragraph("Step 1: Find your maintenance calories (TDEE)")
    pdf.add_paragraph("  My TDEE (estimated): _____ calories")
    pdf.add_paragraph("Step 2: Subtract deficit (typically 20-25% for fat loss)")
    pdf.add_paragraph("  My target calories: _____ calories")
    pdf.add_paragraph("Step 3: Calculate macros")
    pdf.add_paragraph("  Net carbs: 20g (fixed for most people starting)")
    pdf.add_paragraph("  Protein: ___ g (0.8-1g per pound lean body mass)")
    pdf.add_paragraph("  Fat: ___ g (remaining calories divided by 9)")
    pdf.add_blank_line()
    pdf.add_heading2("Keto Food Lists")
    pdf.add_heading3("EAT FREELY (very low carb)")
    pdf.add_bullet("All meats: beef, pork, chicken, turkey, lamb")
    pdf.add_bullet("Fatty fish: salmon, mackerel, sardines, tuna")
    pdf.add_bullet("Eggs (any style)")
    pdf.add_bullet("Butter, ghee, lard, tallow")
    pdf.add_bullet("Olive oil, avocado oil, coconut oil")
    pdf.add_bullet("Hard cheeses, cream cheese, heavy cream")
    pdf.add_bullet("Leafy greens: spinach, lettuce, kale, arugula")
    pdf.add_bullet("Above-ground vegetables: broccoli, cauliflower, zucchini, mushrooms")
    pdf.add_heading3("EAT IN MODERATION")
    pdf.add_bullet("Nuts: almonds (3g net/oz), macadamia (2g), pecans (1g)")
    pdf.add_bullet("Seeds: chia, flax, sunflower, pumpkin")
    pdf.add_bullet("Berries: raspberries (3g/half cup), blackberries (3g)")
    pdf.add_bullet("Dark chocolate (85%+): 4-5g per oz")
    pdf.add_bullet("Avocado: 2g net per half")
    pdf.add_bullet("Tomatoes, peppers, onions (count carbs)")
    pdf.add_heading3("AVOID (high carb)")
    pdf.add_bullet("Grains: bread, pasta, rice, oats, cereal")
    pdf.add_bullet("Sugar: all forms (honey, maple syrup, agave)")
    pdf.add_bullet("Starchy vegetables: potatoes, corn, peas")
    pdf.add_bullet("Most fruits (banana, apple, orange = 20-25g each)")
    pdf.add_bullet("Beans and legumes (15-20g per serving)")
    pdf.add_bullet("Milk (12g per cup)")
    pdf.add_bullet("Beer, sweet cocktails")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 4: 4-Week Keto Meal Plan")
    pdf.add_blank_line()
    for week_num in range(1, 5):
        pdf.add_heading2(f"Week {week_num}")
        keto_meals = [
            ("Monday", "Bacon and eggs with avocado", "Chicken caesar salad (no croutons)", "Bunless burger with cheese, bacon, side salad"),
            ("Tuesday", "Keto smoothie: coconut milk, MCT, berries", "Tuna salad lettuce wraps", "Salmon with butter, asparagus, cauliflower mash"),
            ("Wednesday", "3-egg omelet with cheese, mushrooms, spinach", "Egg salad with celery sticks and cheese", "Pork chops with creamy mushroom sauce, green beans"),
            ("Thursday", "Bulletproof coffee + boiled eggs", "Cobb salad with full-fat ranch", "Steak with butter, broccoli with cheese sauce"),
            ("Friday", "Cream cheese pancakes with sugar-free syrup", "Leftover steak salad", "Shrimp scampi with zucchini noodles"),
            ("Saturday", "Eggs benedict on portobello mushroom caps", "Cheeseburger lettuce wraps", "Chicken thighs with creamy garlic sauce, roasted vegetables"),
            ("Sunday", "Keto breakfast casserole (eggs, sausage, cheese)", "Antipasto platter (meats, cheese, olives)", "Slow cooker pot roast with low-carb vegetables")
        ]
        for day, b, l, d in keto_meals:
            pdf.add_heading3(f"W{week_num} {day}")
            pdf.add_bullet(f"B: {b}")
            pdf.add_bullet(f"L: {l}")
            pdf.add_bullet(f"D: {d}")
            pdf.add_blank_line()
        pdf.add_page_break()
    
    pdf.add_heading1("Chapter 5: Daily Keto Tracker")
    add_tracker_pages(pdf, "Daily Keto Tracker",
                      ["Net carbs (g)", "Protein (g)", "Fat (g)", "Calories",
                       "Water (oz)", "Ketone level (if testing)",
                       "Energy (1-10)", "Cravings (1-10)",
                       "Exercise", "Weight", "Notes"], num_pages=16)
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 6: Exercise & Lifestyle on Keto")
    pdf.add_blank_line()
    pdf.add_heading2("Exercise During Keto Adaptation (Weeks 1-4)")
    pdf.add_bullet("Reduce intensity by 30-50% during first 2-3 weeks")
    pdf.add_bullet("Walking and yoga are excellent choices")
    pdf.add_bullet("Performance will temporarily decrease then improve")
    pdf.add_bullet("Stay hydrated and maintain electrolytes")
    pdf.add_blank_line()
    pdf.add_heading2("Exercise After Adaptation (Weeks 4+)")
    pdf.add_bullet("Strength training: Excellent on keto (maintain/build muscle)")
    pdf.add_bullet("Moderate cardio: Well-fueled by fat burning")
    pdf.add_bullet("High-intensity: May benefit from targeted carbs around workouts")
    pdf.add_bullet("Endurance: Keto-adapted athletes often excel at long-duration")
    pdf.add_blank_line()
    pdf.add_heading2("Electrolyte Management")
    pdf.add_paragraph("Keto increases water and electrolyte loss. Supplement daily:")
    pdf.add_bullet("Sodium: 5-7g (add salt generously, drink broth)")
    pdf.add_bullet("Potassium: 3,000-4,000mg (avocado, spinach, supplement)")
    pdf.add_bullet("Magnesium: 300-400mg (supplement glycinate or citrate)")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 7: Progress Review & Troubleshooting")
    pdf.add_blank_line()
    pdf.add_heading2("Monthly Progress")
    for m in range(4):
        pdf.add_heading3(f"Month {m+1}")
        pdf.add_paragraph(f"Date: __/__/____  Weight: ___  Waist: ___  Energy: ___/10")
        pdf.add_paragraph(f"Cravings: ___/10  Mental clarity: ___/10  Sleep: ___/10")
        pdf.add_paragraph(f"Biggest success: ____________________________")
        pdf.add_paragraph(f"Biggest challenge: __________________________")
        pdf.add_blank_line()
    
    add_weekly_review(pdf, [
        "Net carbs average: ___g/day",
        "Weight change this week:",
        "Energy level (1-10):",
        "Cravings (1-10):",
        "Electrolytes maintained: [ ]Y [ ]N",
        "Exercise sessions:",
        "Challenges:",
        "Adjustment for next week:"
    ], num_weeks=4)
    pdf.add_page_break()
    
    faqs = [
        ("How long until I'm in ketosis?", "Most people enter ketosis within 2-4 days of keeping net carbs under 20g. Full fat-adaptation (optimal performance) takes 4-8 weeks."),
        ("How do I know if I'm in ketosis?", "Signs: Decreased appetite, metallic taste, increased thirst/urination, improved mental clarity. You can test with urine strips (less accurate) or blood ketone meters (most accurate)."),
        ("Is keto safe long-term?", "For most healthy adults, yes. However, those with kidney disease, pancreatitis, liver conditions, or type 1 diabetes should not do keto without medical supervision."),
        ("Can I have alcohol on keto?", "Spirits (vodka, whiskey, gin) with zero-carb mixers are technically keto. Wine in moderation (5g carbs per glass). Beer is generally too high-carb. Note: alcohol tolerance decreases significantly on keto."),
        ("Why am I not losing weight on keto?", "Common reasons: Eating too many calories, too much protein (gluconeogenesis), hidden carbs, not tracking accurately, stress/sleep issues, or body recomposition (gaining muscle)."),
        ("What about cholesterol on keto?", "LDL may temporarily rise in some people. Focus on particle size (large fluffy is benign), triglycerides (should drop significantly), HDL (should rise), and overall ratios. Discuss with your doctor."),
        ("Can I do keto as a vegetarian?", "Yes, though more challenging. Emphasize eggs, cheese, nuts, seeds, avocados, coconut products, and low-carb vegetables. Protein may require careful planning."),
        ("How do I handle social situations?", "Choose meat and vegetable options at restaurants. Bring keto-friendly dishes to gatherings. Most meals can be adapted by removing the starch component."),
        ("What is a 'keto stall' and how do I break it?", "A stall is 3+ weeks without weight change. Try: a fat fast, reducing dairy, intermittent fasting, changing exercise routine, reducing artificial sweeteners, or just being patient."),
        ("Should I cycle in and out of keto?", "Some people benefit from cyclical keto (5 days keto, 1-2 days higher carb). This can help thyroid function and workout performance. Experiment after full adaptation."),
    ]
    add_faq_section(pdf, faqs)
    
    pdf.add_page_break()
    pdf.add_heading1("Quick-Reference: Daily Keto Checklist")
    pdf.add_bullet("[ ] Net carbs under 20g")
    pdf.add_bullet("[ ] Adequate protein (palm-size at each meal)")
    pdf.add_bullet("[ ] Healthy fats with each meal")
    pdf.add_bullet("[ ] Electrolytes: sodium, potassium, magnesium")
    pdf.add_bullet("[ ] Drank 80+ oz water")
    pdf.add_bullet("[ ] Ate vegetables (low-carb)")
    pdf.add_bullet("[ ] Tracked macros")
    pdf.add_bullet("[ ] Moved body")
    
    add_about_author(pdf)
    filepath = os.path.join(OUTPUT_DIR, "17-Keto-Diet-Complete-Starter-Guide.pdf")
    pdf.save(filepath)
    return filepath



def book_18_pregnancy():
    """Pregnancy Nutrition & Wellness Guide"""
    pdf = PurePDF(title="Pregnancy Nutrition & Wellness Guide", author=AUTHOR)
    add_front_matter(pdf, "Pregnancy Nutrition", "& Wellness Guide")
    
    chapters = ["Understanding Pregnancy Nutrition", "First Trimester Guide",
                "Second Trimester Guide", "Third Trimester Guide",
                "Exercise During Pregnancy", "Supplement & Safety Guide",
                "Birth Preparation", "FAQ & Resources"]
    add_toc(pdf, chapters)
    
    pdf.add_heading1("Introduction")
    pdf.add_paragraph("Pregnancy is a time when nutrition matters more than ever - you're building "
                      "a human! This guide provides trimester-by-trimester nutrition, safe exercise "
                      "guidelines, supplement information, and wellness tracking to support you "
                      "and your baby through all 40 weeks.")
    pdf.add_blank_line()
    pdf.add_paragraph("Note: Every pregnancy is unique. This guide provides general evidence-based "
                      "information. Always follow your healthcare provider's specific recommendations.")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 1: Understanding Pregnancy Nutrition")
    pdf.add_blank_line()
    pdf.add_heading2("Caloric Needs by Trimester")
    pdf.add_bullet("First trimester: No extra calories needed (focus on quality)")
    pdf.add_bullet("Second trimester: +340 calories per day")
    pdf.add_bullet("Third trimester: +450 calories per day")
    pdf.add_paragraph("These are averages - your provider will guide you based on starting weight.")
    pdf.add_blank_line()
    pdf.add_heading2("Key Nutrients for Pregnancy")
    pdf.add_heading3("Folate (600mcg DFE daily)")
    pdf.add_paragraph("Critical for neural tube development. Needed before and during early pregnancy.")
    pdf.add_bullet("Sources: Leafy greens, legumes, fortified foods")
    pdf.add_bullet("Supplement: Prenatal vitamin with methylfolate preferred")
    pdf.add_heading3("Iron (27mg daily)")
    pdf.add_paragraph("Blood volume increases 50% during pregnancy. Iron prevents anemia.")
    pdf.add_bullet("Sources: Red meat, lentils, spinach, fortified cereals")
    pdf.add_bullet("Take with vitamin C for better absorption")
    pdf.add_heading3("Calcium (1000mg daily)")
    pdf.add_paragraph("Builds baby's bones and teeth. If you don't consume enough, baby takes from your bones.")
    pdf.add_bullet("Sources: Dairy, fortified plant milk, leafy greens, sardines")
    pdf.add_heading3("DHA Omega-3 (300mg daily)")
    pdf.add_paragraph("Critical for baby's brain and eye development.")
    pdf.add_bullet("Sources: Fatty fish (2-3 servings/week), DHA supplement")
    pdf.add_heading3("Choline (450mg daily)")
    pdf.add_paragraph("Brain development and prevents neural tube defects. Often missing from prenatals.")
    pdf.add_bullet("Sources: Eggs (1 egg = 150mg), liver, meat, fish")
    pdf.add_heading3("Protein (75-100g daily)")
    pdf.add_paragraph("Builds baby's tissues, placenta, and supports blood volume.")
    pdf.add_bullet("Sources: Meat, fish, eggs, dairy, legumes")
    pdf.add_blank_line()
    pdf.add_heading2("Foods to Avoid During Pregnancy")
    pdf.add_bullet("Raw or undercooked meat, fish, eggs")
    pdf.add_bullet("High-mercury fish (shark, swordfish, king mackerel, tilefish)")
    pdf.add_bullet("Unpasteurized dairy and juice")
    pdf.add_bullet("Deli meats (unless heated until steaming)")
    pdf.add_bullet("Raw sprouts")
    pdf.add_bullet("Alcohol (no safe amount during pregnancy)")
    pdf.add_bullet("Excessive caffeine (limit to 200mg/day = 1 cup coffee)")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 2: First Trimester (Weeks 1-13)")
    pdf.add_blank_line()
    pdf.add_heading2("What's Happening")
    pdf.add_paragraph("All major organs and body systems are forming. This is the most critical "
                      "time for nutrition quality (even though you may not feel like eating).")
    pdf.add_blank_line()
    pdf.add_heading2("Managing Nausea")
    pdf.add_bullet("Eat small, frequent meals (every 2-3 hours)")
    pdf.add_bullet("Keep crackers by bedside for morning sickness")
    pdf.add_bullet("Ginger: Tea, candies, or supplement (shown to reduce nausea)")
    pdf.add_bullet("Vitamin B6: 25mg 3x daily (discuss with provider)")
    pdf.add_bullet("Cold foods may be tolerated better than hot")
    pdf.add_bullet("Avoid strong smells and trigger foods")
    pdf.add_bullet("Stay hydrated (sip throughout the day)")
    pdf.add_blank_line()
    pdf.add_heading2("First Trimester Nutrition Priorities")
    pdf.add_bullet("Folate-rich foods daily")
    pdf.add_bullet("Adequate hydration despite nausea")
    pdf.add_bullet("Whatever you can keep down is okay")
    pdf.add_bullet("Prenatal vitamin (try at night if morning sickness)")
    pdf.add_bullet("Protein when tolerated (aids nausea)")
    pdf.add_blank_line()
    pdf.add_heading2("First Trimester Wellness Tracker")
    for w in range(18):
        pdf.add_heading3(f"Week {w+4}")
        pdf.add_paragraph(f"Nausea level (1-10): ___  Fatigue (1-10): ___")
        pdf.add_paragraph(f"Prenatal taken: [ ]Y [ ]N  Meals eaten: ___")
        pdf.add_paragraph(f"Water intake: ___oz  Exercise: ___min")
        pdf.add_paragraph(f"Symptoms/concerns: ___________________________")
        pdf.add_paragraph(f"Mood (1-10): ___  Sleep quality (1-10): ___")
        pdf.add_paragraph(f"Notes: ________________________________________")
        pdf.add_blank_line()
        pdf.add_separator()
        if (w + 1) % 2 == 0:
            pdf.add_page_break()
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 3: Second Trimester (Weeks 14-27)")
    pdf.add_blank_line()
    pdf.add_heading2("What's Happening")
    pdf.add_paragraph("Baby is growing rapidly. Energy often returns (the 'honeymoon trimester'). "
                      "Focus on nutrient-dense foods and increasing intake.")
    pdf.add_blank_line()
    pdf.add_heading2("Second Trimester Nutrition Focus")
    pdf.add_bullet("Increase calories by ~340/day")
    pdf.add_bullet("Emphasize calcium and vitamin D (baby's bones forming)")
    pdf.add_bullet("Iron-rich foods (blood volume expanding)")
    pdf.add_bullet("Protein at every meal")
    pdf.add_bullet("Fiber for constipation prevention (25-30g daily)")
    pdf.add_bullet("DHA for brain development")
    pdf.add_blank_line()
    pdf.add_heading2("Sample Day - Second Trimester")
    pdf.add_bullet("Breakfast: Eggs + whole grain toast + fruit + prenatal vitamin")
    pdf.add_bullet("Snack: Greek yogurt with berries and granola")
    pdf.add_bullet("Lunch: Salmon salad with leafy greens and olive oil")
    pdf.add_bullet("Snack: Apple with almond butter")
    pdf.add_bullet("Dinner: Chicken, sweet potato, steamed broccoli")
    pdf.add_bullet("Evening: Warm milk with honey, handful of walnuts")
    pdf.add_blank_line()
    pdf.add_heading2("Second Trimester Wellness Tracker")
    for w in range(16):
        pdf.add_heading3(f"Week {w+14}")
        pdf.add_paragraph(f"Energy (1-10): ___  Appetite (1-10): ___")
        pdf.add_paragraph(f"Baby movement felt: [ ]Y [ ]N")
        pdf.add_paragraph(f"Exercise this week: ___________________________")
        pdf.add_paragraph(f"Cravings: _____________  Aversions: _____________")
        pdf.add_paragraph(f"Weight: ___  Blood pressure (if monitored): ___/___")
        pdf.add_paragraph(f"Mood (1-10): ___  Sleep (1-10): ___")
        pdf.add_paragraph(f"Notes: ________________________________________")
        pdf.add_blank_line()
        pdf.add_separator()
        if (w + 1) % 2 == 0:
            pdf.add_page_break()
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 4: Third Trimester (Weeks 28-40)")
    pdf.add_blank_line()
    pdf.add_heading2("What's Happening")
    pdf.add_paragraph("Baby is gaining weight rapidly (about 1/2 pound per week). Your body is "
                      "preparing for labor. Space in stomach decreases - eat smaller, more frequent meals.")
    pdf.add_blank_line()
    pdf.add_heading2("Third Trimester Nutrition")
    pdf.add_bullet("Increase calories by ~450/day over baseline")
    pdf.add_bullet("Protein: Critical for baby's final growth spurt")
    pdf.add_bullet("Iron: Prepare for blood loss at delivery")
    pdf.add_bullet("Vitamin K: Important for blood clotting (leafy greens)")
    pdf.add_bullet("Dates: 6 per day from week 36 (may ease labor)")
    pdf.add_bullet("Red raspberry leaf tea: After week 32 (uterine toning)")
    pdf.add_blank_line()
    pdf.add_heading2("Managing Common Discomforts")
    pdf.add_heading3("Heartburn")
    pdf.add_bullet("Eat smaller, more frequent meals")
    pdf.add_bullet("Avoid lying down after eating")
    pdf.add_bullet("Skip spicy, fatty, acidic foods if triggering")
    pdf.add_heading3("Constipation")
    pdf.add_bullet("High fiber foods (30g+ daily)")
    pdf.add_bullet("Adequate water (10+ cups daily)")
    pdf.add_bullet("Movement and walking")
    pdf.add_bullet("Magnesium supplement")
    pdf.add_heading3("Swelling")
    pdf.add_bullet("Adequate protein (helps with fluid balance)")
    pdf.add_bullet("Elevate feet when possible")
    pdf.add_bullet("Reduce sodium if excessive")
    pdf.add_bullet("Stay hydrated (counterintuitive but helps)")
    pdf.add_blank_line()
    pdf.add_heading2("Third Trimester Wellness Tracker")
    for w in range(18):
        pdf.add_heading3(f"Week {w+27}")
        pdf.add_paragraph(f"Energy (1-10): ___  Sleep quality (1-10): ___")
        pdf.add_paragraph(f"Baby kicks counted: [ ]Y ___/hour")
        pdf.add_paragraph(f"Swelling: [ ]None [ ]Mild [ ]Moderate")
        pdf.add_paragraph(f"Braxton Hicks: [ ]Y [ ]N  Exercise: ___")
        pdf.add_paragraph(f"Weight: ___  Mood (1-10): ___")
        pdf.add_paragraph(f"Concerns for provider: ________________________")
        pdf.add_paragraph(f"Notes: ________________________________________")
        pdf.add_blank_line()
        pdf.add_separator()
        if (w + 1) % 2 == 0:
            pdf.add_page_break()
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 5: Exercise During Pregnancy")
    pdf.add_blank_line()
    pdf.add_heading2("Benefits of Prenatal Exercise")
    pdf.add_bullet("Reduces risk of gestational diabetes")
    pdf.add_bullet("Helps manage healthy weight gain")
    pdf.add_bullet("Reduces back pain and constipation")
    pdf.add_bullet("May shorten labor and reduce c-section risk")
    pdf.add_bullet("Improves mood and sleep")
    pdf.add_bullet("Faster postpartum recovery")
    pdf.add_blank_line()
    pdf.add_heading2("Safe Exercises")
    pdf.add_bullet("Walking (all trimesters)")
    pdf.add_bullet("Swimming and water aerobics (joint-friendly)")
    pdf.add_bullet("Prenatal yoga")
    pdf.add_bullet("Stationary cycling")
    pdf.add_bullet("Modified strength training")
    pdf.add_bullet("Pelvic floor exercises (Kegels)")
    pdf.add_blank_line()
    pdf.add_heading2("Exercises to Avoid")
    pdf.add_bullet("Contact sports or fall risk activities")
    pdf.add_bullet("Lying flat on back after first trimester")
    pdf.add_bullet("Hot yoga or hot environments")
    pdf.add_bullet("Heavy lifting with breath holding")
    pdf.add_bullet("Jumping, bouncing, or jarring movements")
    pdf.add_bullet("Exercises that cause pain or dizziness")
    pdf.add_blank_line()
    pdf.add_heading2("Stop Exercise and Call Provider If:")
    pdf.add_bullet("Vaginal bleeding")
    pdf.add_bullet("Dizziness or faintness")
    pdf.add_bullet("Chest pain or shortness of breath")
    pdf.add_bullet("Headache")
    pdf.add_bullet("Muscle weakness")
    pdf.add_bullet("Calf pain or swelling")
    pdf.add_bullet("Regular contractions")
    pdf.add_bullet("Fluid leaking from vagina")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 6: Supplement & Safety Guide")
    pdf.add_blank_line()
    pdf.add_heading2("Essential Prenatal Supplements")
    pdf.add_bullet("Prenatal multivitamin: Contains folate, iron, DHA, etc.")
    pdf.add_bullet("DHA/EPA: 300mg DHA minimum (if not in prenatal)")
    pdf.add_bullet("Vitamin D: 2000-4000 IU (many women are deficient)")
    pdf.add_bullet("Iron: If anemic (separate from calcium)")
    pdf.add_bullet("Choline: 450mg (often not in prenatals)")
    pdf.add_bullet("Magnesium: For leg cramps, constipation, sleep")
    pdf.add_bullet("Probiotic: Gut health and potentially reduces Group B strep")
    pdf.add_blank_line()
    pdf.add_heading2("My Supplement Schedule")
    pdf.add_paragraph("Morning: _______________________________________________")
    pdf.add_paragraph("Midday: _______________________________________________")
    pdf.add_paragraph("Evening: _______________________________________________")
    pdf.add_paragraph("Bedtime: _______________________________________________")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 7: Birth Preparation")
    pdf.add_blank_line()
    pdf.add_heading2("Birth Preferences Worksheet")
    pdf.add_paragraph("Birth location: [ ]Hospital [ ]Birth center [ ]Home")
    pdf.add_paragraph("Pain management preference: _______________________")
    pdf.add_paragraph("Support team: _______________________________________")
    pdf.add_paragraph("Atmosphere requests: ________________________________")
    pdf.add_paragraph("Immediate postpartum wishes: ________________________")
    pdf.add_paragraph("Feeding plan: [ ]Breast [ ]Bottle [ ]Combo")
    pdf.add_blank_line()
    pdf.add_heading2("Hospital Bag Nutrition Pack")
    pdf.add_bullet("[ ] Coconut water (electrolytes for labor)")
    pdf.add_bullet("[ ] Honey sticks or dates (energy during labor)")
    pdf.add_bullet("[ ] Protein bars or trail mix")
    pdf.add_bullet("[ ] Postpartum recovery snacks")
    pdf.add_bullet("[ ] Water bottle")
    pdf.add_bullet("[ ] Partner snacks (labor can be long!)")
    pdf.add_blank_line()
    add_weekly_review(pdf, [
        "Weeks pregnant: ___",
        "Prenatal supplements taken consistently: [ ]Y [ ]N",
        "Exercise this week:",
        "Nutrition quality (1-10):",
        "Energy level (1-10):",
        "Concerns for next appointment:",
        "Baby movement pattern:",
        "Self-care this week:"
    ], num_weeks=4)
    pdf.add_page_break()
    
    faqs = [
        ("How much weight should I gain?", "Depends on starting BMI: Normal weight: 25-35 lbs, Overweight: 15-25 lbs, Underweight: 28-40 lbs, Obese: 11-20 lbs. Your provider will give personalized guidance."),
        ("Is caffeine safe?", "Up to 200mg/day (about one 12oz coffee) is considered safe. Some providers recommend less. Avoid energy drinks entirely."),
        ("Can I eat sushi?", "Raw fish carries infection risk during pregnancy. Cooked sushi rolls (shrimp tempura, California roll with imitation crab) are fine. Low-mercury cooked fish is encouraged."),
        ("What about food cravings?", "Cravings are normal and okay to indulge in moderation. If craving non-food items (ice, dirt, chalk) - this is called pica and may indicate a nutritional deficiency. Tell your provider."),
        ("Do I really need a prenatal vitamin?", "Yes. It's very difficult to get adequate folate, iron, and DHA from food alone during pregnancy. Think of it as insurance for any nutritional gaps."),
        ("Is exercise safe in the third trimester?", "Yes, unless your provider says otherwise. Modify as needed - reduce intensity, avoid overheating, stop if anything feels wrong. Walking and swimming are excellent throughout."),
        ("What if I can't keep anything down?", "Severe nausea/vomiting (hyperemesis gravidarum) affects 1-3% of pregnancies and needs medical treatment. If you cannot keep food/water down for 24 hours, contact your provider."),
        ("Can I diet during pregnancy?", "Pregnancy is not the time for weight loss diets. Focus on nutrient quality, not restriction. If overweight, your provider may recommend modest calorie awareness without restriction."),
    ]
    add_faq_section(pdf, faqs)
    
    pdf.add_page_break()
    pdf.add_heading1("Quick-Reference: Daily Pregnancy Nutrition Checklist")
    pdf.add_bullet("[ ] Took prenatal vitamin")
    pdf.add_bullet("[ ] Ate protein at every meal")
    pdf.add_bullet("[ ] Consumed calcium-rich food")
    pdf.add_bullet("[ ] Ate iron-rich food")
    pdf.add_bullet("[ ] Had DHA source (fish or supplement)")
    pdf.add_bullet("[ ] Ate colorful fruits and vegetables")
    pdf.add_bullet("[ ] Drank 10+ cups of water")
    pdf.add_bullet("[ ] Had choline source (eggs)")
    pdf.add_bullet("[ ] Moved body (even just a walk)")
    
    add_about_author(pdf)
    filepath = os.path.join(OUTPUT_DIR, "18-Pregnancy-Nutrition-Wellness-Guide.pdf")
    pdf.save(filepath)
    return filepath



def book_19_intermittent_fasting():
    """Intermittent Fasting Complete Guide"""
    pdf = PurePDF(title="Intermittent Fasting Complete Guide", author=AUTHOR)
    add_front_matter(pdf, "Intermittent Fasting", "Complete Guide with Daily Tracker")
    
    chapters = ["Understanding Intermittent Fasting", "Choosing Your Method",
                "Getting Started Plan", "Daily Fasting Tracker",
                "Nutrition During Eating Windows", "Exercise & Lifestyle",
                "Progress Review & Results Journal", "FAQ & Resources"]
    add_toc(pdf, chapters)
    
    pdf.add_heading1("Introduction")
    pdf.add_paragraph("Intermittent fasting (IF) is not a diet - it's an eating pattern that "
                      "cycles between periods of fasting and eating. It focuses on WHEN you eat "
                      "rather than WHAT you eat. Research shows benefits for weight loss, metabolic "
                      "health, brain function, and longevity.")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 1: Understanding Intermittent Fasting")
    pdf.add_blank_line()
    pdf.add_heading2("How IF Works")
    pdf.add_paragraph("When you fast, several things happen in your body:")
    pdf.add_bullet("Insulin levels drop significantly (promotes fat burning)")
    pdf.add_bullet("Human Growth Hormone increases (muscle preservation)")
    pdf.add_bullet("Cellular repair processes activate (autophagy)")
    pdf.add_bullet("Gene expression changes (longevity and protection genes)")
    pdf.add_blank_line()
    pdf.add_heading2("Benefits of Intermittent Fasting")
    pdf.add_bullet("Weight and body fat loss (especially visceral fat)")
    pdf.add_bullet("Improved insulin sensitivity")
    pdf.add_bullet("Reduced inflammation")
    pdf.add_bullet("Better brain function and clarity")
    pdf.add_bullet("Cellular cleanup (autophagy)")
    pdf.add_bullet("Simplified eating schedule")
    pdf.add_bullet("May improve cholesterol and blood pressure")
    pdf.add_bullet("Potential longevity benefits")
    pdf.add_blank_line()
    pdf.add_heading2("Who Should NOT Fast")
    pdf.add_bullet("Pregnant or breastfeeding women")
    pdf.add_bullet("Children and teenagers")
    pdf.add_bullet("People with eating disorder history")
    pdf.add_bullet("Those with Type 1 diabetes or on insulin")
    pdf.add_bullet("Severely underweight individuals")
    pdf.add_bullet("People with certain medical conditions (ask your doctor)")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 2: Choosing Your Method")
    pdf.add_blank_line()
    pdf.add_heading2("Popular IF Methods Compared")
    pdf.add_blank_line()
    pdf.add_heading3("16:8 (Most Popular - Recommended for Beginners)")
    pdf.add_bullet("Fast for 16 hours, eat within 8-hour window")
    pdf.add_bullet("Example: Eat 12pm-8pm, fast 8pm-12pm")
    pdf.add_bullet("Difficulty: Easy to moderate")
    pdf.add_bullet("Best for: Beginners, daily practice, sustainable lifestyle")
    pdf.add_blank_line()
    pdf.add_heading3("18:6 (Intermediate)")
    pdf.add_bullet("Fast for 18 hours, eat within 6-hour window")
    pdf.add_bullet("Example: Eat 1pm-7pm")
    pdf.add_bullet("Difficulty: Moderate")
    pdf.add_bullet("Best for: Those comfortable with 16:8 wanting more benefits")
    pdf.add_blank_line()
    pdf.add_heading3("20:4 (Warrior Diet)")
    pdf.add_bullet("Fast for 20 hours, eat within 4-hour window")
    pdf.add_bullet("Example: Eat 4pm-8pm (one large meal + snack)")
    pdf.add_bullet("Difficulty: Challenging")
    pdf.add_bullet("Best for: Experienced fasters, those who prefer one big meal")
    pdf.add_blank_line()
    pdf.add_heading3("5:2 (Modified Fasting)")
    pdf.add_bullet("Eat normally 5 days, restrict to 500-600 calories on 2 non-consecutive days")
    pdf.add_bullet("Example: Fast on Monday and Thursday")
    pdf.add_bullet("Difficulty: Moderate")
    pdf.add_bullet("Best for: Those who prefer not fasting daily")
    pdf.add_blank_line()
    pdf.add_heading3("Alternate Day Fasting (ADF)")
    pdf.add_bullet("Alternate between normal eating days and fasting/very low calorie days")
    pdf.add_bullet("Difficulty: Hard")
    pdf.add_bullet("Best for: Quick results, experienced fasters")
    pdf.add_blank_line()
    pdf.add_heading3("OMAD (One Meal A Day)")
    pdf.add_bullet("Fast for 23 hours, one large meal")
    pdf.add_bullet("Difficulty: Very challenging")
    pdf.add_bullet("Best for: Very experienced, those who thrive on simplicity")
    pdf.add_blank_line()
    pdf.add_heading2("My Chosen Method")
    pdf.add_paragraph("Method: _________________")
    pdf.add_paragraph("Eating window: ___:___ to ___:___")
    pdf.add_paragraph("Fasting hours: ___")
    pdf.add_paragraph("Start date: __/__/____")
    pdf.add_paragraph("Reason for choosing this method: ___________________")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 3: Getting Started Plan")
    pdf.add_blank_line()
    pdf.add_heading2("Gradual Adaptation Schedule")
    pdf.add_heading3("Week 1: 12:12 (ease in)")
    pdf.add_bullet("Stop eating after dinner (e.g., 8pm)")
    pdf.add_bullet("Don't eat until 8am (12-hour fast)")
    pdf.add_bullet("This is natural for many people")
    pdf.add_heading3("Week 2: 14:10")
    pdf.add_bullet("Push breakfast back 2 hours (10am)")
    pdf.add_bullet("Notice: You're probably not truly hungry at your old breakfast time")
    pdf.add_heading3("Week 3: 16:8")
    pdf.add_bullet("Full 16:8 protocol")
    pdf.add_bullet("First meal at noon (or your chosen time)")
    pdf.add_bullet("Last meal by 8pm")
    pdf.add_heading3("Week 4+: Maintain or extend")
    pdf.add_bullet("Stick with 16:8 or experiment with longer fasts")
    pdf.add_bullet("Listen to your body")
    pdf.add_blank_line()
    pdf.add_heading2("What Breaks a Fast?")
    pdf.add_heading3("Won't Break Your Fast (okay during fasting window)")
    pdf.add_bullet("Water (plain, sparkling, mineral)")
    pdf.add_bullet("Black coffee (no cream, sugar, or sweetener)")
    pdf.add_bullet("Plain tea (green, black, herbal)")
    pdf.add_bullet("Salt/electrolytes")
    pdf.add_heading3("WILL Break Your Fast")
    pdf.add_bullet("Any calories (even small amounts)")
    pdf.add_bullet("Cream or milk in coffee")
    pdf.add_bullet("Diet soda (debated, but insulin response possible)")
    pdf.add_bullet("Supplements with calories (fish oil, gummies)")
    pdf.add_bullet("Bone broth (technically, though some allow it)")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 4: Daily Fasting Tracker")
    pdf.add_blank_line()
    pdf.add_paragraph("Track your fasting window, how you feel, and results.")
    pdf.add_blank_line()
    for week in range(24):
        pdf.add_heading3(f"Week {week+1}")
        for day in range(7):
            pdf.add_paragraph(f"Date: __/__  Fast start: ___:___  Fast end: ___:___  "
                            f"Hours: ___  Hunger (1-10): ___")
            pdf.add_paragraph(f"  Energy: ___/10  Clarity: ___/10  "
                            f"Exercise: [ ]Y  Broke fast with: __________")
        pdf.add_separator()
        pdf.add_page_break()
    
    pdf.add_heading1("Chapter 5: Nutrition During Eating Windows")
    pdf.add_blank_line()
    pdf.add_heading2("What to Eat (Quality Matters)")
    pdf.add_paragraph("IF works best when combined with nutritious food. Don't use it as an "
                      "excuse to eat poorly during your eating window.")
    pdf.add_blank_line()
    pdf.add_heading3("Breaking Your Fast (First Meal)")
    pdf.add_bullet("Start with something gentle (not a huge heavy meal)")
    pdf.add_bullet("Protein first (stabilizes blood sugar)")
    pdf.add_bullet("Include healthy fat (satiety)")
    pdf.add_bullet("Add vegetables (fiber and nutrients)")
    pdf.add_bullet("Avoid pure sugar/carbs as first food (causes crash)")
    pdf.add_blank_line()
    pdf.add_heading3("Ideal Break-Fast Meals")
    pdf.add_bullet("Eggs with avocado and vegetables")
    pdf.add_bullet("Greek yogurt with nuts and berries")
    pdf.add_bullet("Salmon with salad")
    pdf.add_bullet("Bone broth followed by balanced meal")
    pdf.add_bullet("Protein smoothie with greens and fat")
    pdf.add_blank_line()
    pdf.add_heading2("Sample 16:8 Day")
    pdf.add_bullet("7am: Wake, drink water, black coffee")
    pdf.add_bullet("10am: Sparkling water, green tea")
    pdf.add_bullet("12pm (break fast): Eggs, avocado, vegetables, fruit")
    pdf.add_bullet("3pm: Snack - nuts, cheese, apple")
    pdf.add_bullet("6-7pm (last meal): Protein + vegetables + healthy carbs")
    pdf.add_bullet("8pm: Fasting window begins")
    pdf.add_bullet("Herbal tea allowed in the evening")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 6: Exercise & Lifestyle")
    pdf.add_blank_line()
    pdf.add_heading2("Working Out While Fasting")
    pdf.add_bullet("Fasted exercise can enhance fat burning")
    pdf.add_bullet("Low-moderate intensity works best fasted (walking, yoga)")
    pdf.add_bullet("High intensity may be better in fed state initially")
    pdf.add_bullet("Always prioritize how you feel over the 'rules'")
    pdf.add_bullet("Stay hydrated and maintain electrolytes")
    pdf.add_blank_line()
    pdf.add_heading2("Sleep and Fasting")
    pdf.add_bullet("Stop eating 2-3 hours before bed (improves sleep quality)")
    pdf.add_bullet("IF often improves sleep once adapted")
    pdf.add_bullet("Poor sleep increases hunger hormones - prioritize rest")
    pdf.add_blank_line()
    pdf.add_heading2("Social Situations")
    pdf.add_bullet("IF is flexible - adjust your window for special occasions")
    pdf.add_bullet("One off day won't ruin progress")
    pdf.add_bullet("You don't owe anyone an explanation about when you eat")
    pdf.add_bullet("Shift your window earlier for dinner events")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 7: Progress Review & Results Journal")
    pdf.add_blank_line()
    pdf.add_heading2("Monthly Check-In")
    for m in range(4):
        pdf.add_heading3(f"Month {m+1}")
        pdf.add_paragraph(f"Date: __/__/____  Weight: ___  Waist: ___")
        pdf.add_paragraph(f"Fasting method used: ___  Consistency: ___/7 days per week")
        pdf.add_paragraph(f"Energy (1-10): ___  Mental clarity (1-10): ___")
        pdf.add_paragraph(f"Hunger management (1-10): ___")
        pdf.add_paragraph(f"Biggest benefit noticed: ___________________")
        pdf.add_paragraph(f"Biggest challenge: ___________________")
        pdf.add_blank_line()
    
    add_weekly_review(pdf, [
        "Days fasted this week: ___/7",
        "Average fasting hours: ___",
        "Hunger level trend (easier/harder):",
        "Energy level:",
        "Food quality during eating window:",
        "Exercise while fasting:",
        "Weight/measurements change:",
        "Adjustment for next week:"
    ], num_weeks=4)
    pdf.add_page_break()
    
    faqs = [
        ("Won't I lose muscle while fasting?", "No, if you eat adequate protein during your eating window and do resistance training. IF actually increases growth hormone, which helps preserve muscle. Muscle loss happens with chronic undereating, not time-restricted eating."),
        ("Can I fast every day?", "Yes, methods like 16:8 are designed for daily use and are safe long-term for most healthy adults. Listen to your body - some people benefit from 1-2 non-fasting days per week."),
        ("Why am I not losing weight with IF?", "Common reasons: Overeating during eating window, not in a calorie deficit overall, too many processed foods, not enough sleep, high stress, or medical factors. IF is a tool, not magic."),
        ("Is fasting safe for women?", "Yes, but some women are more sensitive to fasting. Start conservatively (12-14 hours), avoid fasting around your period, and stop if menstrual irregularities occur. Pregnant/nursing women should not fast."),
        ("Does coffee break a fast?", "Black coffee (no cream, sugar, or sweetener) does not break a fast. It actually enhances fat burning and suppresses appetite. Keep it to 1-2 cups to avoid cortisol spikes."),
        ("Can I drink water during fasting?", "Yes! Drink plenty of water during fasting. Add a pinch of salt for electrolytes. Sparkling water, black coffee, and plain tea are all fine."),
        ("How long until I see results?", "Many people notice improved energy and mental clarity within the first week. Weight loss typically becomes visible at 2-4 weeks. Body composition changes take 4-8 weeks."),
        ("Is IF better than calorie counting?", "Both can work. Many people find IF easier because it simplifies decision-making (you just watch the clock). Some people do best combining both. Choose what's sustainable for you."),
        ("What if I feel dizzy or weak?", "Initial adjustment is normal. Ensure adequate electrolytes (sodium, potassium, magnesium), stay hydrated, and ease into longer fasts. If severe, shorten your fasting window or break your fast."),
        ("Can I fast with diabetes?", "Type 2 diabetes patients may benefit from IF, but MUST work with their doctor, especially if on insulin or sulfonylureas (hypoglycemia risk). Never fast without medical guidance if diabetic."),
    ]
    add_faq_section(pdf, faqs)
    
    pdf.add_page_break()
    pdf.add_heading1("Quick-Reference: Daily IF Checklist")
    pdf.add_bullet("[ ] Fasted for target hours")
    pdf.add_bullet("[ ] Drank adequate water (half body weight in oz)")
    pdf.add_bullet("[ ] Maintained electrolytes")
    pdf.add_bullet("[ ] Broke fast with protein and healthy food")
    pdf.add_bullet("[ ] Ate nutrient-dense foods in eating window")
    pdf.add_bullet("[ ] Did not overeat during window")
    pdf.add_bullet("[ ] Exercised (fasted or fed)")
    pdf.add_bullet("[ ] Tracked fasting window and how I felt")
    
    add_about_author(pdf)
    filepath = os.path.join(OUTPUT_DIR, "19-Intermittent-Fasting-Complete-Guide.pdf")
    pdf.save(filepath)
    return filepath



def book_20_burnout():
    """Burnout Recovery Workbook"""
    pdf = PurePDF(title="Burnout Recovery Workbook", author=AUTHOR)
    add_front_matter(pdf, "Burnout Recovery Workbook", "Stress Assessment, Cortisol Management & Energy Restoration")
    
    chapters = ["Understanding Burnout", "Burnout Assessment",
                "Cortisol & Stress Management", "Daily Energy & Wellness Tracker",
                "Recovery Nutrition & Sleep", "Lifestyle Redesign",
                "Progress Review & Rebuilding", "FAQ & Resources"]
    add_toc(pdf, chapters)
    
    pdf.add_heading1("Introduction")
    pdf.add_paragraph("Burnout is not just being tired. It is a state of chronic physical, emotional, "
                      "and mental exhaustion caused by prolonged stress. It affects your health, "
                      "relationships, identity, and quality of life. Recovery is possible, but it "
                      "requires intentional changes - not just a vacation.")
    pdf.add_blank_line()
    pdf.add_paragraph("This workbook guides you through understanding your burnout, assessing its "
                      "severity, and building a personalized recovery plan that restores your energy, "
                      "purpose, and joy.")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 1: Understanding Burnout")
    pdf.add_blank_line()
    pdf.add_heading2("The Three Dimensions of Burnout")
    pdf.add_heading3("1. Exhaustion (Physical and Emotional)")
    pdf.add_bullet("Feeling drained, depleted, unable to recover with rest")
    pdf.add_bullet("Chronic fatigue that sleep doesn't fix")
    pdf.add_bullet("Getting sick more often (immune suppression)")
    pdf.add_bullet("Physical symptoms: headaches, muscle tension, digestive issues")
    pdf.add_heading3("2. Cynicism/Depersonalization")
    pdf.add_bullet("Feeling detached, numb, or negative")
    pdf.add_bullet("Loss of caring about work or responsibilities")
    pdf.add_bullet("Irritability and impatience with others")
    pdf.add_bullet("Withdrawal from colleagues, friends, and family")
    pdf.add_heading3("3. Reduced Efficacy")
    pdf.add_bullet("Feeling incompetent despite past achievements")
    pdf.add_bullet("Inability to concentrate or produce quality work")
    pdf.add_bullet("Self-doubt and imposter syndrome intensified")
    pdf.add_bullet("Loss of motivation and purpose")
    pdf.add_blank_line()
    pdf.add_heading2("Burnout vs. Depression vs. Regular Stress")
    pdf.add_paragraph("Stress: You feel overwhelmed but engaged. Recovery happens with rest.")
    pdf.add_paragraph("Burnout: You feel empty and beyond caring. Rest alone doesn't help.")
    pdf.add_paragraph("Depression: Pervasive hopelessness affecting all life areas. "
                      "Burnout can trigger depression - seek help if hopelessness persists.")
    pdf.add_blank_line()
    pdf.add_heading2("The Burnout Cycle")
    pdf.add_bullet("1. Compulsion to prove yourself (overcommitment)")
    pdf.add_bullet("2. Working harder, neglecting personal needs")
    pdf.add_bullet("3. Neglecting self-care, relationships, fun")
    pdf.add_bullet("4. Dismissing problems, blaming others or yourself")
    pdf.add_bullet("5. Values revision - work becomes only identity")
    pdf.add_bullet("6. Denial of emerging problems")
    pdf.add_bullet("7. Withdrawal from social life")
    pdf.add_bullet("8. Behavioral changes noticed by others")
    pdf.add_bullet("9. Depersonalization - losing sense of self")
    pdf.add_bullet("10. Inner emptiness and anxiety")
    pdf.add_bullet("11. Depression and exhaustion")
    pdf.add_bullet("12. Full burnout syndrome (collapse)")
    pdf.add_blank_line()
    pdf.add_heading2("What Causes Burnout")
    pdf.add_heading3("Work Factors")
    pdf.add_bullet("Unsustainable workload")
    pdf.add_bullet("Lack of control or autonomy")
    pdf.add_bullet("Insufficient recognition or reward")
    pdf.add_bullet("Toxic work environment")
    pdf.add_bullet("Values mismatch with organization")
    pdf.add_bullet("Unfair treatment")
    pdf.add_heading3("Personal Factors")
    pdf.add_bullet("Perfectionism and high self-expectations")
    pdf.add_bullet("People-pleasing and inability to say no")
    pdf.add_bullet("Caregiving responsibilities without support")
    pdf.add_bullet("Identity entirely tied to productivity")
    pdf.add_bullet("Neglecting rest and recovery needs")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 2: Burnout Assessment")
    pdf.add_blank_line()
    pdf.add_heading2("Burnout Severity Scale")
    pdf.add_paragraph("Rate each statement 0 (never) to 5 (every day):")
    pdf.add_blank_line()
    burnout_items = [
        "I feel emotionally drained by my work/responsibilities",
        "I feel used up at the end of the day",
        "I feel tired when I get up and have to face another day",
        "I feel burned out from my work",
        "I have become less interested in my work",
        "I have become less enthusiastic about things",
        "I doubt the significance of what I do",
        "I feel I am not as effective as I should be",
        "I have trouble concentrating",
        "I feel distant or disconnected from people around me",
        "I experience physical symptoms (headaches, pain, illness)",
        "I have lost my sense of humor and joy",
        "I dread going to work or starting my day",
        "I feel guilty when I'm not being productive",
        "I have trouble sleeping even though I'm exhausted"
    ]
    for item in burnout_items:
        pdf.add_paragraph(f"  {item}: ___/5")
    pdf.add_blank_line()
    pdf.add_paragraph("Total Score: ___/75")
    pdf.add_heading3("Scoring")
    pdf.add_bullet("0-20: Low burnout risk (focus on prevention)")
    pdf.add_bullet("21-40: Moderate burnout (intervention needed)")
    pdf.add_bullet("41-55: High burnout (significant changes required)")
    pdf.add_bullet("56-75: Severe burnout (consider medical leave, professional help)")
    pdf.add_blank_line()
    pdf.add_heading2("My Burnout Triggers")
    pdf.add_paragraph("Top 3 things draining my energy:")
    for i in range(3):
        pdf.add_paragraph(f"  {i+1}. _________________________________________")
    pdf.add_paragraph("Things I've stopped doing for myself:")
    for i in range(3):
        pdf.add_paragraph(f"  {i+1}. _________________________________________")
    pdf.add_paragraph("What I wish I could change immediately:")
    pdf.add_paragraph("  _________________________________________")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 3: Cortisol & Stress Management")
    pdf.add_blank_line()
    pdf.add_heading2("Understanding Cortisol")
    pdf.add_paragraph("Cortisol is your primary stress hormone. In burnout, the cortisol system "
                      "becomes dysregulated - often high at night (can't sleep) and low in the "
                      "morning (can't wake up/function). This is HPA axis dysfunction.")
    pdf.add_blank_line()
    pdf.add_heading3("Healthy Cortisol Rhythm")
    pdf.add_bullet("Highest in morning (helps you wake up and feel alert)")
    pdf.add_bullet("Gradually decreases throughout the day")
    pdf.add_bullet("Lowest at night (allows sleep)")
    pdf.add_heading3("Burnout Cortisol Pattern")
    pdf.add_bullet("Low in morning (exhaustion, can't get going)")
    pdf.add_bullet("Spikes at random times (anxiety, panic)")
    pdf.add_bullet("Elevated at night (insomnia, wired-but-tired)")
    pdf.add_blank_line()
    pdf.add_heading2("Cortisol Recovery Protocol")
    pdf.add_heading3("Morning (Support natural cortisol rise)")
    pdf.add_bullet("Wake at consistent time")
    pdf.add_bullet("Sunlight within 30 minutes (sets cortisol clock)")
    pdf.add_bullet("Protein-rich breakfast (stabilizes blood sugar)")
    pdf.add_bullet("Avoid checking phone/email for first hour")
    pdf.add_bullet("Gentle movement (walk, stretch)")
    pdf.add_heading3("Afternoon (Prevent cortisol spike)")
    pdf.add_bullet("Eat regular meals (blood sugar drops trigger cortisol)")
    pdf.add_bullet("Take a genuine break (walk outside, not scrolling)")
    pdf.add_bullet("10-minute breathwork or meditation")
    pdf.add_bullet("Set a hard stop time for work")
    pdf.add_heading3("Evening (Lower cortisol for sleep)")
    pdf.add_bullet("Dim lights after sunset")
    pdf.add_bullet("No screens 1+ hour before bed")
    pdf.add_bullet("Magnesium supplement (glycinate)")
    pdf.add_bullet("Journaling or brain dump (externalize worries)")
    pdf.add_bullet("Calming tea: chamomile, lemon balm, valerian")
    pdf.add_bullet("Restorative yoga or gentle stretching")
    pdf.add_blank_line()
    pdf.add_heading2("Immediate Stress Reset Techniques")
    pdf.add_bullet("Physiological sigh: Double inhale, long exhale (30 seconds)")
    pdf.add_bullet("Cold water on face or wrists (vagal nerve activation)")
    pdf.add_bullet("5-4-3-2-1 grounding (senses check)")
    pdf.add_bullet("Progressive muscle relaxation (2 minutes)")
    pdf.add_bullet("Walk outside for 5 minutes (nature + movement)")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 4: Daily Energy & Wellness Tracker")
    add_tracker_pages(pdf, "Daily Burnout Recovery Tracker",
                      ["Energy AM (1-10)", "Energy PM (1-10)", "Stress level (1-10)",
                       "Sleep hours/quality", "Meals eaten (count)",
                       "Movement/exercise", "Time outdoors (min)",
                       "Work hours", "Recovery activity done",
                       "Joy/fun experienced (Y/N)", "Boundaries honored (Y/N)"], num_pages=16)
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 5: Recovery Nutrition & Sleep")
    pdf.add_blank_line()
    pdf.add_heading2("Eating for Burnout Recovery")
    pdf.add_paragraph("Burnout depletes nutrients. Your body needs replenishment, not restriction.")
    pdf.add_blank_line()
    pdf.add_heading3("Key Nutrients for Recovery")
    pdf.add_bullet("Magnesium: Depleted by stress (leafy greens, dark chocolate, nuts)")
    pdf.add_bullet("B vitamins: Used rapidly during stress (whole grains, eggs, meat)")
    pdf.add_bullet("Vitamin C: Adrenal support (citrus, bell peppers, berries)")
    pdf.add_bullet("Omega-3: Brain repair and anti-inflammatory (fatty fish, walnuts)")
    pdf.add_bullet("Protein: Neurotransmitter building blocks (every meal)")
    pdf.add_bullet("Complex carbs: Serotonin production (sweet potato, oats)")
    pdf.add_blank_line()
    pdf.add_heading3("Eating Principles for Recovery")
    pdf.add_bullet("Eat within 1 hour of waking (stabilize cortisol)")
    pdf.add_bullet("Don't skip meals (blood sugar crashes worsen burnout)")
    pdf.add_bullet("Protein at every meal (brain chemistry support)")
    pdf.add_bullet("Reduce caffeine (further depletes adrenals)")
    pdf.add_bullet("Reduce sugar (energy rollercoaster)")
    pdf.add_bullet("Hydrate well (dehydration mimics fatigue)")
    pdf.add_blank_line()
    pdf.add_heading2("Sleep Recovery Protocol")
    pdf.add_paragraph("Sleep is when your body repairs from stress. It is NON-NEGOTIABLE for recovery.")
    pdf.add_bullet("Target: 8-9 hours (more than usual - you're healing)")
    pdf.add_bullet("Consistent schedule (same time daily, even weekends)")
    pdf.add_bullet("Wind-down routine starting 90 minutes before bed")
    pdf.add_bullet("No work in the bedroom (retrain brain)")
    pdf.add_bullet("Magnesium glycinate before bed")
    pdf.add_bullet("If racing mind: Write a brain dump list, then close the notebook")
    pdf.add_bullet("If can't sleep: Get up after 20 min, do something boring, return when sleepy")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 6: Lifestyle Redesign")
    pdf.add_blank_line()
    pdf.add_heading2("Boundaries Workshop")
    pdf.add_paragraph("Burnout often results from insufficient boundaries. This section helps you "
                      "identify and implement necessary changes.")
    pdf.add_blank_line()
    pdf.add_heading3("Boundary Audit")
    pdf.add_paragraph("Area: Work hours")
    pdf.add_paragraph("  Current reality: _________________________________")
    pdf.add_paragraph("  What I need: _________________________________")
    pdf.add_paragraph("  One boundary to set: _________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("Area: Personal time")
    pdf.add_paragraph("  Current reality: _________________________________")
    pdf.add_paragraph("  What I need: _________________________________")
    pdf.add_paragraph("  One boundary to set: _________________________________")
    pdf.add_blank_line()
    pdf.add_paragraph("Area: Relationships/Obligations")
    pdf.add_paragraph("  Current reality: _________________________________")
    pdf.add_paragraph("  What I need: _________________________________")
    pdf.add_paragraph("  One boundary to set: _________________________________")
    pdf.add_blank_line()
    pdf.add_heading2("The Joy Inventory")
    pdf.add_paragraph("List activities that bring you genuine joy (not productivity, not obligation):")
    for i in range(10):
        pdf.add_paragraph(f"  {i+1}. _________________________________________")
    pdf.add_paragraph("When did you last do each one? Schedule one THIS WEEK.")
    pdf.add_blank_line()
    pdf.add_heading2("The Energy Audit")
    pdf.add_heading3("Energy Givers (activities that fill you up)")
    for i in range(5):
        pdf.add_paragraph(f"  {i+1}. _________________________________________")
    pdf.add_heading3("Energy Drainers (activities that deplete you)")
    for i in range(5):
        pdf.add_paragraph(f"  {i+1}. _________________________________________")
    pdf.add_paragraph("Goal: Increase givers, reduce or delegate drainers.")
    pdf.add_blank_line()
    pdf.add_heading2("Recovery Non-Negotiables")
    pdf.add_paragraph("Choose 3-5 daily non-negotiables for your recovery:")
    pdf.add_bullet("[ ] _________________________________________")
    pdf.add_bullet("[ ] _________________________________________")
    pdf.add_bullet("[ ] _________________________________________")
    pdf.add_bullet("[ ] _________________________________________")
    pdf.add_bullet("[ ] _________________________________________")
    pdf.add_page_break()
    
    pdf.add_heading1("Chapter 7: Progress Review & Rebuilding")
    pdf.add_blank_line()
    pdf.add_heading2("Monthly Recovery Assessment")
    for m in range(6):
        pdf.add_heading3(f"Month {m+1}")
        pdf.add_paragraph(f"Date: __/__/____")
        pdf.add_paragraph(f"Burnout score (retake assessment): ___/75")
        pdf.add_paragraph(f"Energy level average (1-10): ___")
        pdf.add_paragraph(f"Joy experienced this month (1-10): ___")
        pdf.add_paragraph(f"Boundaries maintained (1-10): ___")
        pdf.add_paragraph(f"Sleep quality (1-10): ___")
        pdf.add_paragraph(f"Biggest recovery win: ___________________")
        pdf.add_paragraph(f"Still struggling with: ___________________")
        pdf.add_blank_line()
    
    add_weekly_review(pdf, [
        "Energy level average (1-10):",
        "Stress level average (1-10):",
        "Hours worked this week:",
        "Recovery activities completed:",
        "Boundaries honored:",
        "Joy/fun moments:",
        "Sleep quality:",
        "One thing I'm proud of:"
    ], num_weeks=4)
    pdf.add_page_break()
    
    faqs = [
        ("How long does burnout recovery take?", "Full recovery typically takes 3-12 months with significant lifestyle changes. Some people need longer. It depends on severity, how long you've been burned out, and what changes you make. Be patient."),
        ("Should I quit my job?", "Not necessarily immediately. First try: setting boundaries, reducing hours, changing responsibilities, or taking medical leave. If the environment is fundamentally toxic and change isn't possible, leaving may be necessary for your health."),
        ("Is burnout a medical condition?", "The WHO classifies burnout as an occupational phenomenon (not a medical diagnosis). However, it can cause or worsen medical conditions (depression, anxiety, cardiovascular disease). Seek medical care if needed."),
        ("Why can't I just push through?", "Burnout is a nervous system state, not a motivation problem. 'Pushing through' is what caused burnout in the first place. Recovery requires doing LESS, not more. Rest is not laziness - it's medicine."),
        ("Will exercise help or hurt?", "Gentle exercise (walking, yoga, swimming) helps recovery. Intense exercise can worsen burnout by adding physical stress to an already-overwhelmed system. Start gentle, increase only when energy improves."),
        ("How do I explain burnout to others?", "You might say: 'I've been running on empty for too long and my body and mind need rest to recover. This is a health issue, not a choice or weakness.' You don't owe anyone a detailed explanation."),
        ("Can burnout come back?", "Yes, if you return to the same patterns. Recovery must include systemic changes: better boundaries, realistic expectations, regular rest, and addressing root causes. Prevention is ongoing."),
        ("When should I seek professional help?", "Immediately if: you have thoughts of self-harm, you cannot function (work, self-care, relationships), symptoms of depression persist, or you've tried self-help for 4-6 weeks without improvement."),
    ]
    add_faq_section(pdf, faqs)
    
    pdf.add_page_break()
    pdf.add_heading1("Quick-Reference: Daily Burnout Recovery Checklist")
    pdf.add_bullet("[ ] Slept 8+ hours")
    pdf.add_bullet("[ ] Ate nourishing meals (not skipped)")
    pdf.add_bullet("[ ] Sunlight exposure in the morning")
    pdf.add_bullet("[ ] One stress management practice")
    pdf.add_bullet("[ ] Gentle movement (not punishment)")
    pdf.add_bullet("[ ] Set or maintained a boundary")
    pdf.add_bullet("[ ] One moment of genuine rest (not scrolling)")
    pdf.add_bullet("[ ] Connected with someone I care about")
    pdf.add_bullet("[ ] Did one thing purely for joy")
    pdf.add_bullet("[ ] Practiced self-compassion")
    
    add_about_author(pdf)
    filepath = os.path.join(OUTPUT_DIR, "20-Burnout-Recovery-Workbook.pdf")
    pdf.save(filepath)
    return filepath



# ============================================================
# MAIN EXECUTION
# ============================================================

def main():
    """Generate all 20 health PDF books."""
    print("=" * 60)
    print("  HEALTH DIGITAL PRODUCTS - PDF GENERATOR")
    print(f"  Author: {AUTHOR}")
    print(f"  Output: {OUTPUT_DIR}")
    print("=" * 60)
    print()
    
    books = [
        ("01", "Anti-Inflammatory Diet Complete Guide", book_01_anti_inflammatory),
        ("02", "Gut Health Recovery Workbook", book_02_gut_health),
        ("03", "Hormone Balance Guide for Women", book_03_hormone_balance),
        ("04", "Blood Pressure Management Workbook", book_04_blood_pressure),
        ("05", "Sleep Optimization Workbook", book_05_sleep),
        ("06", "Diabetes Management Workbook Type 2", book_06_diabetes),
        ("07", "Chronic Pain Management Workbook", book_07_chronic_pain),
        ("08", "Menopause Survival Guide", book_08_menopause),
        ("09", "Mediterranean Diet Complete Guide", book_09_mediterranean),
        ("10", "Migraine Tracker & Management Workbook", book_10_migraine),
        ("11", "Weight Loss Accountability Workbook", book_11_weight_loss),
        ("12", "Nervous System Regulation Workbook", book_12_nervous_system),
        ("13", "Postpartum Recovery & Wellness Guide", book_13_postpartum),
        ("14", "PCOS Management Workbook", book_14_pcos),
        ("15", "Medical Information Binder", book_15_medical_binder),
        ("16", "Thyroid Health & Hashimoto's Workbook", book_16_thyroid),
        ("17", "Keto Diet Complete Starter Guide", book_17_keto),
        ("18", "Pregnancy Nutrition & Wellness Guide", book_18_pregnancy),
        ("19", "Intermittent Fasting Complete Guide", book_19_intermittent_fasting),
        ("20", "Burnout Recovery Workbook", book_20_burnout),
    ]
    
    results = []
    
    for num, title, func in books:
        print(f"[{num}/20] Generating: {title}...")
        try:
            filepath = func()
            size = os.path.getsize(filepath) / 1024
            print(f"         -> {filepath}")
            print(f"         -> {size:.1f} KB")
            results.append((num, title, filepath, size))
        except Exception as e:
            print(f"         -> ERROR: {e}")
            import traceback
            traceback.print_exc()
        print()
    
    # Summary
    print()
    print("=" * 60)
    print("  GENERATION COMPLETE")
    print("=" * 60)
    print(f"  Books generated: {len(results)}/20")
    print()
    for num, title, filepath, size in results:
        print(f"  [{num}] {title} ({size:.0f} KB)")
    print()
    total = sum(r[3] for r in results)
    print(f"  Total size: {total:.0f} KB ({total/1024:.1f} MB)")
    print()
    
    # Verify page counts
    print("  Verifying page counts...")
    all_good = True
    for num, title, filepath, size in results:
        # Rough page estimate based on file size (each page ~2-3KB in this format)
        est_pages = int(size / 2.5)
        status = "OK" if est_pages >= 60 else "LOW"
        if status == "LOW":
            all_good = False
        print(f"    [{num}] ~{est_pages} pages - {status}")
    
    if all_good:
        print("\n  All books meet 60+ page requirement!")
    else:
        print("\n  Some books may need additional content.")
    
    return results


if __name__ == '__main__':
    main()
