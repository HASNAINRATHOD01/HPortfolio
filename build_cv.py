from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

WIDTH, HEIGHT = letter
DARK = HexColor('#111827')
GREY = HexColor('#4b5563')
ACCENT = HexColor('#0f766e')
LINE = HexColor('#d1d5db')

c = canvas.Canvas("/home/claude/Hasnain_Rathod_Resume.pdf", pagesize=letter)

margin = 0.6 * inch
y = HEIGHT - 0.55 * inch

# --- Photo (top right, circular) ---
photo = ImageReader('/home/claude/cv_photo_circle.png')
photo_size = 0.85 * inch
photo_top_y = HEIGHT - 0.5 * inch
photo_x = WIDTH - margin - photo_size
photo_bottom_y = photo_top_y - photo_size
c.drawImage(photo, photo_x, photo_bottom_y, width=photo_size, height=photo_size, mask='auto')

# --- Name & Title ---
c.setFont("Helvetica-Bold", 20)
c.setFillColor(DARK)
c.drawString(margin, y, "Hasnain Rathod")
y -= 20
c.setFont("Helvetica", 11)
c.setFillColor(ACCENT)
c.drawString(margin, y, "Aspiring Full Stack Developer & CSE Student")
y -= 16

# Make sure the contact line starts below the photo so nothing overlaps it
y = min(y, photo_bottom_y - 10)

c.setFont("Helvetica", 8.5)
c.setFillColor(GREY)
contact_line = "Ahmedabad, India  |  hasnainrathod78@gmail.com  |  github.com/HASNAINRATHOD01  |  linkedin.com/in/HASNAINRATHOD"
c.drawString(margin, y, contact_line)
y -= 14

c.setStrokeColor(LINE)
c.setLineWidth(0.75)
c.line(margin, y, WIDTH - margin, y)
y -= 20

def section_title(title, y):
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(ACCENT)
    c.drawString(margin, y, title)
    y -= 4
    c.setStrokeColor(LINE)
    c.setLineWidth(0.5)
    c.line(margin, y, WIDTH - margin, y)
    return y - 14

def wrap_text(text, font, size, max_width):
    words = text.split(' ')
    lines, cur = [], ''
    for w in words:
        test = (cur + ' ' + w).strip()
        if c.stringWidth(test, font, size) <= max_width:
            cur = test
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def body_para(text, y, size=9, leading=12, color=GREY, indent=0):
    c.setFont("Helvetica", size)
    c.setFillColor(color)
    lines = wrap_text(text, "Helvetica", size, WIDTH - 2*margin - indent)
    for line in lines:
        c.drawString(margin + indent, y, line)
        y -= leading
    return y

def bullet(text, y, size=8.5, leading=11.5):
    c.setFont("Helvetica", size)
    c.setFillColor(GREY)
    bullet_x = margin + 12
    text_x = margin + 20
    lines = wrap_text(text, "Helvetica", size, WIDTH - text_x - margin)
    first = True
    for line in lines:
        if first:
            c.drawString(bullet_x, y, "•")
            first = False
        c.drawString(text_x, y, line)
        y -= leading
    return y

# --- SUMMARY ---
y = section_title("SUMMARY", y)
summary = ("Computer Science Engineering student at LJ Institute of Engineering & Technology, Ahmedabad "
           "(B.Tech, 2028). Proficient in Java, Python, and MERN stack development. Experienced in building "
           "full-stack web applications with REST API design, backend development, and database management. "
           "Strong fundamentals in DSA, OOPs, and DBMS.")
y = body_para(summary, y)
y -= 12

# --- TECHNICAL SKILLS ---
y = section_title("TECHNICAL SKILLS", y)
skills = [
    ("Languages: ", "Java, Python, JavaScript, SQL, HTML/CSS"),
    ("Frameworks & Libraries: ", "React.js, Node.js, Express.js, Django"),
    ("Databases: ", "MongoDB, PostgreSQL"),
    ("Core CS: ", "Data Structures & Algorithms, OOPs, DBMS, OS Basics"),
    ("Tools: ", "Git, GitHub, VS Code, Postman, npm"),
    ("Exploring: ", "Machine Learning, AI API Integration (Gemini)"),
]
for label, val in skills:
    c.setFont("Helvetica-Bold", 8.8)
    c.setFillColor(DARK)
    c.drawString(margin, y, label)
    lw = c.stringWidth(label, "Helvetica-Bold", 8.8)
    c.setFont("Helvetica", 8.8)
    c.setFillColor(GREY)
    c.drawString(margin + lw, y, val)
    y -= 13
y -= 6

# --- PROJECTS ---
y = section_title("PROJECTS", y)

projects = [
    ("Hotel Management System", "Semester 3", "HTML, CSS, JavaScript", [
        "Built web-based system to manage hotel operations including room booking, guest check-in/out and billing.",
        "Implemented responsive UI with clean design for seamless hotel staff experience."
    ]),
    ("MultiStore Management System", "Semester 2", "Java, OOPs, DSA", [
        "Built multi-branch store management system handling inventory tracking across multiple locations.",
        "Used data structures for efficient search, sorting, and data management operations."
    ]),
    ("Pharmacy Management System", "Semester 1", "Java, OOPs, File I/O", [
        "Developed Java desktop application for pharmacy inventory, billing, and customer record management.",
        "Applied core OOP principles: inheritance, encapsulation, and polymorphism throughout the codebase."
    ]),
]

for title, sem, stack, bullets in projects:
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(DARK)
    c.drawString(margin, y, title)
    c.setFont("Helvetica-Oblique", 8.5)
    c.setFillColor(GREY)
    c.drawRightString(WIDTH - margin, y, sem)
    y -= 12
    c.setFont("Helvetica-Oblique", 8.3)
    c.setFillColor(ACCENT)
    c.drawString(margin, y, stack)
    y -= 12
    for b in bullets:
        y = bullet(b, y)
    y -= 6

# --- EDUCATION ---
y = section_title("EDUCATION", y)
c.setFont("Helvetica-Bold", 9.5)
c.setFillColor(DARK)
c.drawString(margin, y, "B.Tech, Computer Science Engineering")
c.setFont("Helvetica-Oblique", 8.5)
c.setFillColor(GREY)
c.drawRightString(WIDTH - margin, y, "2024 - 2028")
y -= 12
c.setFont("Helvetica", 8.8)
c.setFillColor(GREY)
c.drawString(margin, y, "LJ Institute of Engineering & Technology, Ahmedabad")
y -= 20

# --- CERTIFICATIONS ---
y = section_title("CERTIFICATIONS & ACHIEVEMENTS", y)
certs = [
    "Coursera — Introduction to Java (LearnQuest)",
    "Coursera — Inheritance & Data Structures in Java (University of Pennsylvania)",
    "Coursera — Introduction to HTML, CSS & JavaScript (IBM)",
    "Active GitHub contributor since Semester 1 — consistent project development",
]
for cert in certs:
    y = bullet(cert, y)

# --- Footer ---
c.setStrokeColor(LINE)
c.setLineWidth(0.5)
c.line(margin, 0.5*inch, WIDTH - margin, 0.5*inch)
c.setFont("Helvetica", 7.5)
c.setFillColor(GREY)
c.drawCentredString(WIDTH/2, 0.35*inch, "hasnainrathod78@gmail.com  |  github.com/HASNAINRATHOD01  |  Ahmedabad, Gujarat, India")

c.save()
print("PDF built")
