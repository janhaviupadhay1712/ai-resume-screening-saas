# 🚀 HireAI — AI-Powered Resume Screening System

HireAI is an AI-powered Applicant Tracking System (ATS) designed to automate resume screening, candidate ranking, and job matching using Natural Language Processing (NLP) and Machine Learning.

The platform helps recruiters and HR teams efficiently shortlist candidates by analyzing resumes against job descriptions and generating intelligent match scores.

---

# 📌 Features

✅ AI-powered Resume Screening
✅ Resume Parsing (PDF Support)
✅ Candidate Ranking System
✅ Semantic Job Matching using NLP
✅ Real-time Analytics Dashboard
✅ Interactive Streamlit UI
✅ FastAPI Backend APIs
✅ ATS-Friendly Candidate Evaluation
✅ Dark Themed Modern Dashboard UI

---

# 🧠 System Architecture

```text
Frontend (Streamlit)
        ↓
FastAPI Backend APIs
        ↓
Resume Parser + NLP Matching Engine
        ↓
Candidate Ranking & Analytics
```

---

# 🛠️ Tech Stack

## Frontend

* Streamlit
* HTML/CSS

## Backend

* FastAPI
* Python

## AI / Machine Learning

* Sentence Transformers
* Scikit-learn
* FAISS
* NLP

## Resume Processing

* PyPDF2
* PDFMiner
* PyMuPDF

## Deployment & Tools

* Git
* GitHub
* Streamlit Cloud
* Render

---

# 📂 Project Structure

```text
HireAI/
│
├── app/
│   ├── main.py
│   ├── matching.py
│   ├── resume_parser.py
│
├── uploaded_resumes/
│
├── frontend.py
├── requirements.txt
├── README.md
├── data.json
│
└── test_rank.py
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/ai-resume-screening-saas.git
```

---

## 2️⃣ Move to Project Directory

```bash
cd ai-resume-screening-saas
```

---

## 3️⃣ Create Virtual Environment

### Windows

```bash
python -m venv .venv
```

### Activate Virtual Environment

```bash
.venv\Scripts\activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Backend

Run FastAPI backend:

```bash
uvicorn app.main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

Swagger API Docs:

```text
http://127.0.0.1:8000/docs
```

---

# ▶️ Running the Frontend

Run Streamlit frontend:

```bash
streamlit run frontend.py
```

Frontend runs on:

```text
http://localhost:8501
```

---

# 📊 Modules

## 📄 Resume Parser

Extracts:

* Email IDs
* Skills
* Experience
* Resume Text

Supported Format:

* PDF

---

## 🤖 Resume Matching Engine

Uses NLP and semantic similarity to compare:

* Resume Content
* Job Description

Generates:

* Match Score
* Candidate Ranking

---

## 📈 Analytics Dashboard

Displays:

* Total Resumes Processed
* Average Match Score
* Top Candidate Score
* Ranking Insights

---

# 🔥 API Endpoints

## Upload Resume

```http
POST /upload-resume/
```

---

## Match Resume

```http
POST /match-resume/
```

---

## Rank Multiple Resumes

```http
POST /rank-resumes/
```

---

# 🧪 Sample Workflow

1. Upload resumes (PDF)
2. Enter job description
3. AI analyzes resumes
4. Candidates ranked automatically
5. Dashboard updates in real time

---

# 💡 Future Improvements

* Multi-user authentication
* Recruiter dashboard
* Resume recommendation system
* AI interview assistant
* Candidate skill gap analysis
* Cloud database integration
* Email notifications

---

# 🎯 Use Cases

* HR Recruitment Automation
* Applicant Tracking Systems (ATS)
* Resume Screening
* Campus Placement Systems
* Hiring Platforms

---

# 👨‍💻 Author

## Janhavi Upadhyay

B.Tech CSE (Artificial Intelligence)

GitHub:

```text
https://github.com/yourusername
```

LinkedIn:

```text
https://linkedin.com/in/yourprofile
```

---

# ⭐ If You Like This Project

Give this repository a star ⭐ on GitHub.

