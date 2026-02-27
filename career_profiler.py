# Personality-Based Career Profiler Bot

# Initialize scores
scores = {
    "Software Developer (Backend)": 0,
    "Frontend Developer": 0,
    "Full Stack Developer": 0,
    "Machine Learning Engineer": 0,
    "Data Analyst": 0,
    "Cloud Engineer": 0,
    "DevOps Engineer": 0,
    "Cybersecurity Analyst": 0,
    "UI/UX Designer": 0,
    "Mobile App Developer": 0
}

# Updated Balanced Questions
questions = [

    {
        "question": "1. When a system slows down in production, what do you investigate first?",
        "options": {
            "A": ("Backend code and database performance", {"Software Developer (Backend)": 3}),
            "B": ("Server capacity and scaling", {"Cloud Engineer": 3}),
            "C": ("Frontend rendering efficiency", {"Frontend Developer": 3}),
            "D": ("Security vulnerabilities or breaches", {"Cybersecurity Analyst": 3})
        }
    },

    {
        "question": "2. Which activity excites you most?",
        "options": {
            "A": ("Solving complex algorithm problems", {"Software Developer (Backend)": 3}),
            "B": ("Designing user interfaces", {"UI/UX Designer": 3}),
            "C": ("Building predictive AI models", {"Machine Learning Engineer": 3}),
            "D": ("Automating deployments and pipelines", {"DevOps Engineer": 3})
        }
    },

    {
        "question": "3. What kind of problems do you enjoy?",
        "options": {
            "A": ("Logic-heavy system design", {"Software Developer (Backend)": 3}),
            "B": ("Understanding data patterns", {"Data Analyst": 3}),
            "C": ("Infrastructure architecture", {"Cloud Engineer": 3}),
            "D": ("Protecting systems from threats", {"Cybersecurity Analyst": 3})
        }
    },

    {
        "question": "4. In a team project, you prefer to handle:",
        "options": {
            "A": ("Core backend logic", {"Software Developer (Backend)": 3}),
            "B": ("User interface and experience", {"UI/UX Designer": 3}),
            "C": ("Data analysis or AI module", {"Machine Learning Engineer": 3}),
            "D": ("Deployment and reliability", {"DevOps Engineer": 3})
        }
    },

    {
        "question": "5. Which success makes you proudest?",
        "options": {
            "A": ("System running at high efficiency", {"Software Developer (Backend)": 3}),
            "B": ("AI model achieving high accuracy", {"Machine Learning Engineer": 3}),
            "C": ("Application scaling to millions", {"Cloud Engineer": 3}),
            "D": ("Preventing a cyber attack", {"Cybersecurity Analyst": 3})
        }
    },

    {
        "question": "6. You are naturally stronger at:",
        "options": {
            "A": ("Logical reasoning", {"Software Developer (Backend)": 3}),
            "B": ("Creative thinking", {"UI/UX Designer": 3}),
            "C": ("Statistical analysis", {"Data Analyst": 3}),
            "D": ("Monitoring system health", {"DevOps Engineer": 3})
        }
    },

    {
        "question": "7. Which tool would you enjoy mastering?",
        "options": {
            "A": ("Backend frameworks", {"Software Developer (Backend)": 3}),
            "B": ("AI/ML libraries", {"Machine Learning Engineer": 3}),
            "C": ("Cloud platforms", {"Cloud Engineer": 3}),
            "D": ("Security testing tools", {"Cybersecurity Analyst": 3})
        }
    },

    {
        "question": "8. When faced with uncertainty, you:",
        "options": {
            "A": ("Break it into logical modules", {"Software Developer (Backend)": 3}),
            "B": ("Experiment visually and prototype", {"UI/UX Designer": 3}),
            "C": ("Analyze data to find patterns", {"Data Analyst": 3}),
            "D": ("Strengthen system reliability", {"DevOps Engineer": 3})
        }
    },

    {
        "question": "9. Which environment attracts you most?",
        "options": {
            "A": ("Software product development team", {"Software Developer (Backend)": 3}),
            "B": ("AI research lab", {"Machine Learning Engineer": 3}),
            "C": ("Enterprise cloud operations", {"Cloud Engineer": 3}),
            "D": ("Security operations center", {"Cybersecurity Analyst": 3})
        }
    },

    {
        "question": "10. Your long-term vision is to:",
        "options": {
            "A": ("Build powerful software systems", {"Software Developer (Backend)": 3}),
            "B": ("Create intelligent machines", {"Machine Learning Engineer": 3}),
            "C": ("Design scalable infrastructure", {"Cloud Engineer": 3}),
            "D": ("Defend digital systems", {"Cybersecurity Analyst": 3})
        }
    }
]

print("\n" + "=" * 60)
print("        PERSONALITY-BASED CAREER PROFILER")
print("=" * 60 + "\n")

for q in questions:
    print(q["question"])
    for key, value in q["options"].items():
        print(f"{key}) {value[0]}")

    while True:
        answer = input("Choose A/B/C/D: ").upper()
        if answer in q["options"]:
            for career, points in q["options"][answer][1].items():
                scores[career] += points
            break
        else:
            print("Invalid input. Please choose A, B, C, or D.")

    print()

# ---------------- RESULT CALCULATION ---------------- #

sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

primary = sorted_scores[0]
secondary = sorted_scores[1]

primary_score = primary[1]
secondary_score = secondary[1]

total_points = sum(scores.values())

# --- Improved Smart Confidence Logic ---

if total_points == 0:
    confidence = 50
else:
    # Share of dominance compared to all responses
    dominance_strength = primary_score / total_points

    # Gap strength between top two careers
    gap_strength = (primary_score - secondary_score) / (primary_score + 1)

    # Final weighted confidence calculation
    confidence = (dominance_strength * 60) + (gap_strength * 35)

confidence = min(max(confidence, 60), 95)

# --- Personality Classification ---

if confidence >= 85:
    personality = "Highly Focused Specialist"
elif confidence >= 75:
    personality = "Strong Inclination Explorer"
else:
    personality = "Versatile Tech Enthusiast"

# --- Progress Bar Function ---

def progress_bar(percentage):
    bars = int(percentage // 2)
    return "█" * bars + "-" * (50 - bars)

# ---------------- DISPLAY RESULT ---------------- #

print("\n" + "=" * 60)
print("                    RESULT")
print("=" * 60)

print(f"\n🎯 Primary Career Recommendation: {primary[0]}")
print(f"📊 Confidence Level: {confidence:.2f}%")
print(f"🧠 Personality Type: {personality}")

print(f"\n📌 Secondary Career Option: {secondary[0]}")

print("\n📈 Confidence Visualization:")
print(progress_bar(confidence))

print("\n🔎 Top 5 Career Scores:")

for career, score in sorted_scores[:5]:
    percent = (score / total_points) * 100 if total_points != 0 else 0
    print(f"{career:<30} : {percent:.2f}%")

print("\n" + "=" * 60)
print("Thank you for using the Career Profiler!")
print("=" * 60)