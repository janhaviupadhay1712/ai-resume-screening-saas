from fastapi import FastAPI, UploadFile, File, Form
from typing import List
import shutil
import os

from app.resume_parser import (
    extract_resume_text,
    extract_email,
    extract_skills,
    extract_experience
)

from app.matching import calculate_match_score, rank_resumes

app = FastAPI(
    title="AI Resume Screening SaaS",
    version="1.0.0"
)

UPLOAD_FOLDER = "uploaded_resumes"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ---------------------------
# Home Route
# ---------------------------

@app.get("/")
def home():
    return {"message": "AI Resume Screening SaaS Backend Running 🚀"}


# ---------------------------
# Resume Parsing API
# ---------------------------

@app.post("/upload-resume/")
async def upload_resume(file: UploadFile = File(...)):

    if not file.filename.endswith(".pdf"):
        return {"error": "Only PDF files allowed"}

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_resume_text(file_path)

    return {
        "email": extract_email(text),
        "skills": extract_skills(text),
        "experience_years": extract_experience(text)
    }


# ---------------------------
# Resume Matching API
# ---------------------------

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



# Resume Ranking API
from typing import List
from fastapi import UploadFile, File, Form


@app.post("/rank-resumes/")
async def rank_resumes_api(
        files: List[UploadFile] = File(..., description="Upload multiple PDF resumes"),
        job_description: str = Form(...)
):
    resume_texts = []

    for file in files:
        if not file.filename.endswith(".pdf"):
            continue

        file_path = os.path.join(UPLOAD_FOLDER, file.filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        text = extract_resume_text(file_path)
        resume_texts.append(text)

    ranked_results = rank_resumes(resume_texts, job_description)

    return {
        "ranked_candidates": ranked_results
    }

from app.vector_store import add_resumes, search_resumes


@app.post("/faiss-search/")
async def faiss_search_api(
    files: list[UploadFile] = File(...),
    job_description: str = Form(...)
):

    texts = []

    for file in files:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        text = extract_resume_text(file_path)
        texts.append(text)

    add_resumes(texts)

    results = search_resumes(job_description)

    return {
        "top_candidates": results
    }