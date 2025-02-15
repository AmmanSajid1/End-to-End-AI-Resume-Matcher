import streamlit as st
from src.api_client import send_resume

# ---- Streamlit App Config ----
st.set_page_config(page_title="AI Resume Matcher", layout="wide")

st.title("🔍 AI Resume Matcher")
st.subheader("Find the best job matches for your resume!")

# ---- Sidebar for Settings ----
with st.sidebar:
    st.header("⚙️ Settings")
    top_k = st.slider("Number of job matches:", 1, 10, 3)

# ---- File Upload Section ----
uploaded_file = st.file_uploader("📂 Upload Your Resume (PDF)", type=["pdf"])

if uploaded_file:
    st.info("✅ File uploaded successfully! Click 'Find Jobs' to proceed.")

    if st.button("🔍 Find Jobs"):
        with st.spinner("🔄 Searching for best matches..."):
            response = send_resume(uploaded_file)

        if "error" in response:
            st.error("❌ " + response["error"])
        else:
            st.success("✅ AI-Generated Job Recommendations")
            st.markdown(response["llm_response"])  # Display the LLM's formatted response