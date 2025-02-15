import faiss 
import numpy as np
import os
import pandas as pd
from sentence_transformers import SentenceTransformer
from src.data_processor import extract_text_from_pdf


# Get the absolute path of the project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Construct the correct path to the CSV file
jobs_csv_path = os.path.join(BASE_DIR, "data", "jobs_desc_clean.csv")

# Load the job descriptions dataset
jobs_df = pd.read_csv(jobs_csv_path)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create FAISS index
job_embeddings = model.encode(jobs_df["description"].tolist())
index = faiss.IndexFlatL2(job_embeddings.shape[1])
index.add(np.array(job_embeddings))

def find_top_jobs(resume_path, top_k=5):

    # Extract text from Resume PDF file
    resume_text = extract_text_from_pdf(resume_path)
    # Generate embeddings for the given resume (DO NOT STORE)
    resume_vector = model.encode([resume_text]).astype("float32")

    # Perform similarity search in FAISS
    distances, indices = index.search(resume_vector, top_k)

    matched_jobs = jobs_df.iloc[indices[0]]["description"]

    return matched_jobs

