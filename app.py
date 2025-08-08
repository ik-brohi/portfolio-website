from flask import Flask, render_template

app = Flask(__name__)

# Dictionary of pages
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
    "Contact": "contact.html",
    "Developmentally Appropriate Practices": "daps.html"
}

# Auto-generate routes
for title, filename in pages.items():
    route = "/" if filename == "index.html" else f"/{filename[:-5]}"
    view_func_name = "index" if filename == "index.html" else filename[:-5]

    def create_view(template, title):
        return lambda: render_template(template, title=title, pages=pages)

    view_func = create_view(filename, title)
    view_func.__name__ = view_func_name
    app.add_url_rule(rule=route, endpoint=view_func_name, view_func=view_func)

if __name__ == "__main__":
    app.run(debug=True)
