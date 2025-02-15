# 🚀 AI Resume Matcher

An AI-powered resume matching system that helps job seekers find the best job opportunities based on their resumes. It uses **FAISS** for fast similarity search, **OpenAI’s GPT model** to generate professional job recommendations, and **Streamlit** for an interactive user interface.

---

## 📌 Features

✅ Upload your resume (PDF format).  
✅ AI extracts text and matches it with job descriptions using **FAISS**.  
✅ OpenAI’s LLM generates professional job recommendations.  
✅ FastAPI backend for processing requests.  
✅ Streamlit frontend for an easy-to-use interface.  

---

## 🛠 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/AmmanSajid1/End-to-End-AI-Resume-Matcher.git
cd End-to-End-AI-Resume-Matcher
```

### 2️⃣ Create and Activate Conda Environment
```bash
conda create --name resume_matcher python=3.10 -y
conda activate resume_matcher
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a ```.env``` file in the root directory and add your OpenAI API key:
```ini
OPENAI_API_KEY=your_openai_api_key_here
```

## ▶️ How to Run

### 1️⃣ Start FastAPI Backend
```bash
uvicorn app:app --reload
```
This starts the backend at ```http://127.0.0.1:8000/```.

### 2️⃣ Start Streamlit Frontend
```bash
streamlit run streamlit_app.py
```
This launches the frontend where users can upload their resumes.

## 🛠 API Endpoints

| **Method** | **Endpoint**          | **Description**                          |
|------------|-----------------------|------------------------------------------|
| ```POST``` | ```/upload_resume/``` | Uploads a resume and returns job matches |








