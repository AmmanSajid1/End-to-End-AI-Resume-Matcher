import faiss 
import numpy as np
import os
import pandas as pd
import boto3
from sentence_transformers import SentenceTransformer
from src.data_processor import extract_text_from_pdf

# S3 Configuration
S3_BUCKET = "joblistingsdata"
FILE_NAME = "jobs_desc_clean.csv"
LOCAL_PATH = "/app/data/jobs_desc_clean.csv"

def download_from_s3():
    """Download the jobs dataset from S3 if it doesn't exist locally."""
    s3 = boto3.client("s3")
    
    try:
        if not os.path.exists("/app/data"):
            os.makedirs("/app/data")

        print(f"Downloading {FILE_NAME} from S3...")
        s3.download_file(S3_BUCKET, FILE_NAME, LOCAL_PATH)
        print("Download complete.")

    except Exception as e:
        print(f"Error downloading file from S3: {e}")
        exit(1)  # Stop execution if file can't be downloaded

# Download before proceeding
download_from_s3()

# Load the job descriptions dataset
if not os.path.exists(LOCAL_PATH):
    print("Error: CSV file not found after download.")
    exit(1)

jobs_df = pd.read_csv(LOCAL_PATH)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create FAISS index
job_embeddings = model.encode(jobs_df["description"].tolist())
index = faiss.IndexFlatL2(job_embeddings.shape[1])
index.add(np.array(job_embeddings))

def find_top_jobs(resume_path, top_k=5):
    """Find top job matches based on resume similarity."""
    # Extract text from Resume PDF file
    resume_text = extract_text_from_pdf(resume_path)
    
    # Generate embeddings for the given resume
    resume_vector = model.encode([resume_text]).astype("float32")

    # Perform similarity search in FAISS
    distances, indices = index.search(resume_vector, top_k)

    matched_jobs = jobs_df.iloc[indices[0]]["description"]
    
    return matched_jobs
