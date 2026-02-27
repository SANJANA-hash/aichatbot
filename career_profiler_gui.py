import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

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

# Questions (shortened here — keep your full 10 list)
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

root = tk.Tk()
root.title("Career Profiler")
root.geometry("750x600")
style = ttk.Style()
style.theme_use("clam")

root.configure(bg="#f4f6f9")
question_index = 0
selected_option = tk.StringVar()

# ---------------- PROGRESS UPDATE ---------------- #

def update_progress():
    progress = (question_index / len(questions)) * 100
    progress_bar["value"] = progress
    percent_label.config(text=f"{int(progress)}% Completed")

# ---------------- SHOW QUESTION ---------------- #

def show_question():
    selected_option.set(None)

    q = questions[question_index]
    question_label.config(text=q["question"])
    progress_label.config(text=f"Question {question_index+1} of {len(questions)}")

    for widget in options_frame.winfo_children():
        widget.destroy()

    for key, value in q["options"].items():
        tk.Radiobutton(
            options_frame,
            text=value[0],
            variable=selected_option,
            value=key,
            font=("Helvetica", 12),
            wraplength=650,
            justify="left",
            bg="#f4f6f9",
            activebackground="#f4f6f9",
            selectcolor="#dfe6e9"
        ).pack(anchor="w", pady=6)

    update_progress()

# ---------------- NEXT QUESTION ---------------- #

def next_question():
    global question_index

    answer = selected_option.get()

    if not answer:
        messagebox.showwarning("Warning", "Please select an option.")
        return

    for career, points in questions[question_index]["options"][answer][1].items():
        scores[career] += points

    question_index += 1

    if question_index < len(questions):
        show_question()
    else:
        show_result()

# ---------------- RESTART ---------------- #

def restart_quiz():
    global question_index

    question_index = 0

    for career in scores:
        scores[career] = 0

    # Clear entire window
    for widget in root.winfo_children():
        widget.destroy()

    # Rebuild clean UI
    build_main_ui()
    show_question()

# ---------------- RESULT ---------------- #
roadmaps = {
    "Software Developer (Backend)": [
        "Learn Data Structures & Algorithms",
        "Master one backend language (Python/Java)",
        "Understand REST APIs & Databases",
        "Build real-world backend projects",
        "Learn System Design basics"
    ],

    "Machine Learning Engineer": [
        "Strong Python foundation",
        "Learn NumPy, Pandas, Matplotlib",
        "Study ML algorithms (Regression, Classification)",
        "Build ML projects",
        "Learn Deep Learning (TensorFlow/PyTorch)"
    ],

    "Cloud Engineer": [
        "Understand Linux & Networking basics",
        "Learn AWS/Azure/GCP fundamentals",
        "Study Cloud Architecture",
        "Practice deploying applications",
        "Prepare for Cloud Certifications"
    ],

    "Cybersecurity Analyst": [
        "Learn Networking & OS fundamentals",
        "Study Security principles",
        "Practice Ethical Hacking basics",
        "Learn tools like Wireshark & Nmap",
        "Prepare for Security certifications"
    ],

    "DevOps Engineer": [
        "Learn Linux deeply",
        "Understand CI/CD pipelines",
        "Master Docker & Kubernetes",
        "Automate deployments",
        "Learn Monitoring tools"
    ],

    "UI/UX Designer": [
        "Learn Design principles",
        "Master Figma/Adobe XD",
        "Study User Research techniques",
        "Build UI case studies",
        "Understand basic frontend tech"
    ],

    "Data Analyst": [
        "Learn Excel & SQL",
        "Master Python (Pandas)",
        "Study Data Visualization",
        "Work on real datasets",
        "Build dashboard projects"
    ],

    "Frontend Developer": [
        "Learn HTML, CSS, JavaScript",
        "Master React or Angular",
        "Understand Responsive Design",
        "Build portfolio projects",
        "Learn UI performance optimization"
    ],

    "Full Stack Developer": [
        "Learn frontend fundamentals",
        "Learn backend frameworks",
        "Understand databases",
        "Deploy full stack apps",
        "Learn cloud basics"
    ],

    "Mobile App Developer": [
        "Learn Flutter / React Native",
        "Understand mobile UI principles",
        "Work with APIs",
        "Publish apps to store",
        "Optimize performance"
    ]
}

def generate_pdf_report(primary, secondary, confidence):
    file_name = "Career_Profile_Report.pdf"
    doc = SimpleDocTemplate(file_name)
    elements = []

    styles = getSampleStyleSheet()

    elements.append(Paragraph("Career Profiling Report", styles["Heading1"]))
    elements.append(Spacer(1, 0.3 * inch))

    elements.append(Paragraph(f"<b>Primary Career:</b> {primary}", styles["Normal"]))
    elements.append(Spacer(1, 0.2 * inch))

    elements.append(Paragraph(f"<b>Confidence Level:</b> {confidence:.2f}%", styles["Normal"]))
    elements.append(Spacer(1, 0.2 * inch))

    elements.append(Paragraph(f"<b>Secondary Career:</b> {secondary}", styles["Normal"]))
    elements.append(Spacer(1, 0.3 * inch))

    elements.append(Paragraph("<b>Suggested Learning Roadmap:</b>", styles["Normal"]))
    elements.append(Spacer(1, 0.2 * inch))

    roadmap_items = []
    for step in roadmaps.get(primary, []):
        roadmap_items.append(ListItem(Paragraph(step, styles["Normal"])))

    elements.append(ListFlowable(roadmap_items, bulletType="bullet"))

    doc.build(elements)

    messagebox.showinfo("Success", f"Report saved as {file_name}")

def show_result():
    for widget in root.winfo_children():
        widget.destroy()

    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    primary = sorted_scores[0]
    secondary = sorted_scores[1]
    primary_name = primary[0]
    secondary_name = secondary[0]

    total_points = sum(scores.values())
    final_confidence = (primary[1] / total_points) * 100 if total_points != 0 else 0

    container = tk.Frame(root, bg="#f4f6f9")
    container.pack(fill="both", expand=True)


    tk.Label(container,
             text=f"Primary Career:\n{primary[0]}",
             font=("Helvetica", 14),
             bg="#f4f6f9").pack(pady=10)

    # Animated Confidence Label
    confidence_label = tk.Label(container,
                                 text="Confidence Level: 0%",
                                 font=("Helvetica", 13),
                                 bg="#f4f6f9")
    confidence_label.pack(pady=5)

    animated_bar = ttk.Progressbar(container,
                                    length=500,
                                    mode="determinate")
    animated_bar.pack(pady=10)
    title_label = tk.Label(container,
                           text="",
                           font=("Helvetica", 20, "bold"),
                           bg="#f4f6f9",
                           fg="#2c3e50")
    title_label.pack(pady=20)

    full_title = "Career Profiling Result"
    title_index = 0

    def animate_title():
        nonlocal title_index
        if title_index < len(full_title):
            title_label.config(text=full_title[:title_index + 1])
            title_index += 1
            root.after(60, animate_title)
        else:
            animate()  # Start confidence animation after title finishes

    animate_title()
    tk.Label(container,
             text=f"Secondary Option: {secondary[0]}",
             font=("Helvetica", 12),
             bg="#f4f6f9").pack(pady=5)

    # ---- Animation Logic ---- #

    current_value = 0

    def animate():
        nonlocal current_value
        if current_value < final_confidence:
            current_value += 1
            confidence_label.config(text=f"Confidence Level: {int(current_value)}%")
            animated_bar["value"] = current_value
            root.after(15, animate)
        else:
            show_roadmap(container, primary_name, secondary_name, final_confidence)

    ttk.Button(container,
               text="Restart",
               command=restart_quiz).pack(pady=15)

    ttk.Button(container,
               text="Exit",
               command=root.quit).pack()
def show_roadmap(container, primary_name, secondary_name, confidence_value):

    tk.Label(container,
             text="Suggested Learning Roadmap:",
             font=("Helvetica", 14, "bold"),
             bg="#f4f6f9").pack(pady=15)

    for step in roadmaps.get(primary_name, []):
        tk.Label(container,
                 text="• " + step,
                 font=("Helvetica", 11),
                 bg="#f4f6f9",
                 wraplength=650,
                 justify="left").pack(anchor="w", padx=40)

    ttk.Button(container,
               text="Download Report (PDF)",
               command=lambda: generate_pdf_report(
                   primary_name,
                   secondary_name,
                   confidence_value
               )
               ).pack(pady=10)

# ---------------- BUILD MAIN UI ---------------- #

def build_main_ui():
    global question_label, progress_label, progress_bar, percent_label, options_frame

    container = tk.Frame(root, bg="#f4f6f9")
    container.pack(fill="both", expand=True)

    title = tk.Label(container,
                     text="Career Personality Profiler",
                     font=("Helvetica", 18, "bold"),
                     bg="#f4f6f9",
                     fg="#2c3e50")
    title.pack(pady=15)

    question_label = tk.Label(container,
                              text="",
                              font=("Helvetica", 14),
                              wraplength=700,
                              bg="#f4f6f9",
                              fg="#34495e")
    question_label.pack(pady=10)

    progress_label = tk.Label(container,
                              text="",
                              font=("Helvetica", 10),
                              bg="#f4f6f9",
                              fg="#7f8c8d")
    progress_label.pack()

    progress_bar = ttk.Progressbar(container,
                                   length=500,
                                   mode="determinate")
    progress_bar.pack(pady=5)

    percent_label = tk.Label(container,
                             text="0% Completed",
                             font=("Helvetica", 9),
                             bg="#f4f6f9",
                             fg="#7f8c8d")
    percent_label.pack()

    options_frame = tk.Frame(container, bg="#f4f6f9")
    options_frame.pack(pady=20)

    ttk.Button(container,
               text="Next",
               command=next_question).pack(pady=10)

    ttk.Button(container,
               text="Restart",
               command=restart_quiz).pack(pady=5)

    ttk.Button(container,
               text="Exit",
               command=root.quit).pack(pady=5)
# ---------------- START APP ---------------- #

build_main_ui()
show_question()

root.mainloop()