import os
import openai
from fastapi import FastAPI, UploadFile, File
from dotenv import load_dotenv
from src.data_processor import extract_text_from_pdf
from src.faiss_search import find_top_jobs
from src.openai_rag import generate_rag_response

# Load API keys
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

UPLOAD_FOLDER = "uploaded_resumes"  # Directory to store uploaded resumes
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Ensure the directory exists

@app.post("/upload_resume/")
async def upload_resume(resume: UploadFile = File(...)):

    try:
        # Save the uploaded file temporarily
        resume_path = os.path.join(UPLOAD_FOLDER, resume.filename)

        with open(resume_path, "wb") as f:
            f.write(await resume.read())  # Read file content and write to disk


        # Retrieve job recommendations using FAISS
        response = generate_rag_response(resume_pdf_path=resume_path, top_k=3) 
        return {"llm_response": response}  # Ensure the key matches

    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, host="0.0.0.0", port=8000)
