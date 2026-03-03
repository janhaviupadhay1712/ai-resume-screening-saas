import re
from pdfminer.high_level import extract_text as pdf_extract_text



# Resume Text Extraction


def extract_resume_text(file_path: str) -> str:
    """
    Extracts raw text from a PDF resume.
    """
    try:
        text = pdf_extract_text(file_path)
        return text if text else ""
    except Exception as e:
        print(f"Error extracting text: {e}")
        return ""



# Email Extraction


def extract_email(text: str):
    """
    Extracts first email found in resume text.
    """
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    match = re.search(pattern, text)
    return match.group(0) if match else None



# Skills Extraction


SKILLS_DB = [
    "python", "java", "c++", "sql",
    "machine learning", "deep learning",
    "fastapi", "django", "flask",
    "react", "node", "aws",
    "docker", "kubernetes",
    "pandas", "numpy",
    "tensorflow", "pytorch"
]

def extract_skills(text: str):
    """
    Extracts predefined technical skills from resume text.
    """
    text = text.lower()
    found_skills = []

    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))



# Experience Extraction (Basic Regex)


def extract_experience(text: str):
    """
    Extracts maximum years of experience mentioned.
    Example matches:
    - 2 years
    - 3+ years
    """
    pattern = r"(\d+)\+?\s+years?"
    matches = re.findall(pattern, text.lower())

    if matches:

        years = [int(x) for x in matches]
        return max(years)

    return None