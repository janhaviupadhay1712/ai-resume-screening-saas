from fastapi import FastAPI, UploadFile, File, Form
from app.resume_parser import (
    extract_resume_text,
    extract_email,
    extract_skills,
    extract_experience
)
from app.matching import calculate_match_score
import shutil
import os

app = FastAPI(
    title="AI Resume Screening SaaS",
    version="1.0.0"
)

UPLOAD_FOLDER = "uploaded_resumes"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)



# Home Route


@app.get("/")
def home():
    return {"message": "AI Resume Screening SaaS Backend Running 🚀"}



# Resume Parsing API


@app.post("/upload-resume/")
async def upload_resume(file: UploadFile = File(...)):

    if not file.filename.endswith(".pdf"):
        return {"error": "Only PDF files allowed"}

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_resume_text(file_path)

    email = extract_email(text)
    skills = extract_skills(text)
    experience = extract_experience(text)

    return {
        "email": email,
        "skills": skills,
        "experience_years": experience
    }



# Resume Matching API


@app.post("/match-resume/")
async def match_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):

    if not file.filename.endswith(".pdf"):
        return {"error": "Only PDF files allowed"}

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resume_text = extract_resume_text(file_path)

    match_score = calculate_match_score(resume_text, job_description)

    return {
        "match_score_percent": match_score
    }