import os

# List of professional page names and their corresponding route filenames
pages = {
    "Home": "index.html",
    "About Me": "about.html",
    "Resume": "resume.html",
    "Placement Overview": "placement.html",
    "Professional Practice": "practice.html",
    "Observation, Assessment & Planning": "observation.html",
    "Documentation Samples": "documentation.html",
    "Play Pedagogies & Curriculum Provision": "play.html",
    "Holistic Child Development": "development.html",
    "Diversity, Equity & Inclusion": "inclusion.html",
    "Curriculum & Quality Standards": "standards.html",
    "Teaching Standards & Ethics": "ethics.html",
    "Health, Safety & Wellbeing": "wellbeing.html",
    "Aboriginal & Torres Strait Islander Cultures": "cultures.html",
    "Feedback & Evaluation": "feedback.html",
    "Reflective Practice": "reflection.html",
    "Professional Learning & Development": "learning.html",
    "Regulatory & Legal Frameworks": "legal.html",
    "Achievements & Certifications": "certificates.html",
    "Contact": "contact.html"
}

# Create directory structure
os.makedirs("app/templates", exist_ok=True)
os.makedirs("app/static/css", exist_ok=True)
os.makedirs("app/static/js", exist_ok=True)
os.makedirs("app/static/images", exist_ok=True)

# Create __init__.py
with open("app/__init__.py", "w") as f:
    f.write("""from flask import Flask

app = Flask(__name__)

from app import routes
""")

# Create run.py
with open("run.py", "w") as f:
    f.write("""from app import app

if __name__ == "__main__":
    app.run(debug=True)
""")

# Create layout.html (base layout)
with open("app/templates/layout.html", "w") as f:
    f.write("""<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
</head>
<body>
    <header><h1>{{ title }}</h1></header>
    <nav>
        <a href="/">Home</a>
        {% for name, file in pages.items() if file != 'index.html' %}
        <a href="/{{ file[:-5] }}">{{ name }}</a>
        {% endfor %}
    </nav>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
""")

# Create styles.css
with open("app/static/css/styles.css", "w") as f:
    f.write("""body {
    font-family: Arial, sans-serif;
    margin: 20px;
    padding: 0;
    background-color: #f9f9f9;
}
header {
    background-color: #004080;
    color: white;
    padding: 10px;
}
nav a {
    margin: 5px;
    text-decoration: none;
}
""")

# Create each HTML page
for title, filename in pages.items():
    with open(f"app/templates/{filename}", "w") as f:
        f.write(f"""{{% extends "layout.html" %}}

{{% block content %}}
<h2>{title}</h2>
<p>This is the {title.lower()} page.</p>
{{% endblock %}}
""")

# Create routes.py
with open("app/routes.py", "w") as f:
    f.write("from flask import render_template\nfrom app import app\n\n")

    for title, filename in pages.items():
        route_name = filename[:-5]  # remove .html
        if route_name == "index":
            f.write(f"""@app.route("/")
def index():
    return render_template("{filename}", title="{title}")
\n""")
        else:
            f.write(f"""@app.route("/{route_name}")
def {route_name}():
    return render_template("{filename}", title="{title}")
\n""")

print("✅ Portfolio project files generated successfully.")
