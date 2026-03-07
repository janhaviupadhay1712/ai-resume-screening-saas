# AI Resume Screening SaaS 🚀

An AI-powered backend system that analyzes resumes and matches them with job descriptions.

## Features

* 📄 Resume PDF upload
* 📧 Email extraction from resume
* 🛠 Skill extraction
* ⏳ Experience detection
* 📊 Resume–Job Description matching using TF-IDF and cosine similarity

## Tech Stack

* Python
* FastAPI
* Scikit-learn
* PDFMiner
* Git & GitHub

## API Endpoints

### Upload Resume

`POST /upload-resume/`

Returns:

* email
* skills
* experience years

### Resume Matching

`POST /match-resume/`

Returns:

* match score percentage between resume and job description

## Project Structure

```
app/
 ├── main.py
 ├── resume_parser.py
 ├── matching.py
```

## Run Locally

Install dependencies:

```
pip install -r requirements.txt
```

Start server:

```
uvicorn app.main:app --reload
```

Open API docs:

```
http://127.0.0.1:8000/docs
```

## Future Improvements

* Resume embeddings using Sentence Transformers
* Vector database (FAISS)
* Recruiter dashboard
* AI-powered resume recommendations

---

Built while learning backend systems and AI applications.

