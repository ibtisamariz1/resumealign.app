# frontend/streamlit_app.py

import streamlit as st
import requests

st.set_page_config(page_title="Resume + Job Fit Matcher", layout="centered")

st.title("🤖 Resume + Job Fit Matcher")
st.write("Upload your resume and a job description to see how well they match!")

# Upload Resume (PDF)
resume_file = st.file_uploader("📄 Upload your Resume (PDF)", type=["pdf"])

# Upload Job Description (PDF or TXT)
jd_file = st.file_uploader("📑 Upload Job Description (PDF or TXT)", type=["pdf", "txt"])

# Submit button
if st.button("🔍 Match My Resume!"):
    if resume_file is None or jd_file is None:
        st.warning("Please upload both files to continue.")
    else:
        # Send to FastAPI backend
        with st.spinner("🔎 Analyzing... please wait..."):
            files = {
                "resume": resume_file,
                "job_description": jd_file
            }

            try:
                response = requests.post("http://localhost:8000/match", files=files)
                result = response.json()

                st.success(f"✅ Match Score: **{result['score']}**")
                st.markdown(f"### Feedback:\n{result['feedback']}")

            except Exception as e:
                st.error(f"❌ Error: {e}")
