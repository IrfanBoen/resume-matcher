from flask import Flask, render_template, request
from resume_reader import extract_text_from_pdf
from skill_extractor import extract_skills
from matcher import match_jobs

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        file = request.files["resume"]
        if file and file.filename.endswith(".pdf"):
            text = extract_text_from_pdf(file)
            skills = extract_skills(text)
            results = match_jobs(skills)
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
