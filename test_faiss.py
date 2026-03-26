import requests

url = "http://127.0.0.1:8000/rank-resumes/"

files = [
    ("files", open(r"C:\Users\janha\Downloads\Entry_level_Resume_Template (1).pdf", "rb")),
    ("files", open(r"C:\Users\janha\Downloads\Entry_level_Resume_Template.pdf", "rb"))
]

data = {
    "job_description": "Looking for Python developer with machine learning experience"
}

response = requests.post(url, files=files, data=data)

print(response.json())