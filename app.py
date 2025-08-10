import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json
import re

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Gemini response function
def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-2.5-pro')
    response = model.generate_content(input)
    return response.text

# PDF text extraction
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += str(page.extract_text())
    return text

# Safe JSON extraction
def safe_json_parse(response):
    json_match = re.search(r"\{.*\}", response, re.DOTALL)
    if json_match:
        try:
            return json.loads(json_match.group())
        except json.JSONDecodeError:
            return None
    return None

# Prompt Template
input_prompt_template = """
Hey, act like a skilled ATS (Application Tracking System) with deep understanding of software engineering, 
data science, data analysis, and big data engineering. Your task is to evaluate the resume 
based on the given job description.

Assign:
- The percentage match between JD and resume
- Missing important keywords
- A short profile summary

Return the result ONLY in this exact JSON format without extra text:
{{"JD Match":"85%","MissingKeywords":["Python","Machine Learning"],"Profile Summary":"Strong background in backend development with Python and cloud services."}}

Resume: {text}
Job Description: {jd}
"""


# Streamlit UI
st.set_page_config(page_title="Resume ATS Tracker", layout="wide")
st.title("📄 Resume ATS Tracker")
st.markdown("Upload your resume and paste the job description to get an **ATS-based analysis**.")

# Inputs
jd = st.text_area("📌 Paste the Job Description")
uploaded_file = st.file_uploader("📂 Upload Your Resume (PDF)", type="pdf", help="Please upload a PDF file of your resume")

if st.button("🚀 Analyze"):
    if uploaded_file is not None and jd.strip():
        with st.spinner("Analyzing resume..."):
            resume_text = input_pdf_text(uploaded_file)
            final_prompt = input_prompt_template.format(text=resume_text, jd=jd)
            response = get_gemini_response(final_prompt)

        data = safe_json_parse(response)
        if data is None:
            st.error("⚠️ Could not parse AI response into JSON.")
            st.text(response)  # Show raw output for debugging
        else:
            # Display JD Match
            match_percent = int(data["JD Match"].replace("%", ""))
            st.subheader("📊 Job Description Match Percentage")
            st.progress(match_percent / 100)
            st.write(f"**Match:** {match_percent}%")

            # Display Missing Keywords
            st.subheader("❌ Missing Keywords")
            if data["MissingKeywords"]:
                st.markdown(" ".join([f"`{kw}`" for kw in data["MissingKeywords"]]))
            else:
                st.success("No missing keywords found! ✅")

            # Display Profile Summary
            st.subheader("📝 Profile Summary")
            st.info(data["Profile Summary"])

    else:
        st.warning("Please provide both a Job Description and a Resume file.")
