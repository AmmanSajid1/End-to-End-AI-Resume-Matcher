import openai
import os
from dotenv import load_dotenv
from src.faiss_search import find_top_jobs

load_dotenv()
openai_client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_rag_response(resume_pdf_path: str, top_k=3):
    """
    Retrieves top_k job descriptions using FAISS and generates a summary using an LLM.
    """

    # Step 1: Retrieve top_k job descriptions using FAISS
    matched_jobs = find_top_jobs(resume_pdf_path, top_k)

    # Step 2: Format job descriptions as input for LLM
    job_texts = "\n\n".join([f"- {desc}" for desc in matched_jobs.tolist()])

    # Step 3: Define LLM prompt
    prompt = f"""
    You are an AI career assistant helping job seekers. The user has uploaded a resume, 
    and you've retrieved the most relevant job descriptions. Your task is to take these
    jobs and present them to the user in a professional, informative and readable manner.

    The job descriptions:
    {job_texts}

    Be concise and professional.
    """

    # Step 4: Call OpenAI GPT API (Replace with your API key)
    try:
        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a career coach."},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        print("OpenAI API Error:", e)
        return "An error occurred while generating the response."


