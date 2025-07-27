from flask import Flask, render_template, request
from resume_ranker import rank_resumes
from utils import save_resume_and_extract_text
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        resumes = request.files.getlist("resumes")
        job_description = request.form["jd"]
        results = []

        for resume in resumes:
            if resume.filename.endswith(".pdf"):
                resume_path = os.path.join(UPLOAD_FOLDER, resume.filename)
                resume.save(resume_path)
                text = save_resume_and_extract_text(resume_path)
                score = rank_resumes(text, job_description)
                results.append((resume.filename, score))

        results.sort(key=lambda x: x[1], reverse=True)
        return render_template("index.html", results=results)

    return render_template("index.html", results=[])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
