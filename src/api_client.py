import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/upload_resume/")


def send_resume(file):
    "Send resume to FastAPI backend and return job matches"
    files = {"resume": file}
    response = requests.post(API_URL, files=files)

    if response.status_code == 200:
        return response.json()
    
    else:
        return {"error": "Failed to fetch job matches"}