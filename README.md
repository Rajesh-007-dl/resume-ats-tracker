# 📄 Resume ATS Tracker

An **AI-powered Resume Analysis Tool** built with **Streamlit** and **Google Gemini API** that evaluates resumes against a given job description using **ATS-style scoring**.  
It calculates **JD Match %**, identifies **Missing Keywords**, and provides a **Profile Summary** to help job seekers improve their resumes.

---

## 🚀 Features
- 📊 **JD Match Percentage** — See how closely your resume matches the job description.
- ❌ **Missing Keywords** — Identify important skills or keywords missing in your resume.
- 📝 **Profile Summary** — Get a concise summary of your resume.
- ⚡ **Fast & Interactive** — Powered by **Streamlit** UI for instant feedback.

---

## 🛠 Tech Stack
- [Streamlit](https://streamlit.io/) — Frontend UI
- [Google Generative AI](https://ai.google.dev/) — AI analysis
- [PyPDF2](https://pypi.org/project/PyPDF2/) — PDF text extraction
- **python-dotenv** — Environment variable management

---

## 📦 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Rajesh-007-dl/resume-ats-tracker.git
cd resume-ats-tracker
```

### 2️⃣ Install dependencies
```bash
pip install -r req.txt
```

### 3️⃣ Set up environment variables  
Create a `.env` file in the project root and add:
```env
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

---

## ▶️ Usage
Run the Streamlit app:
```bash
streamlit run app.py
```

1. **Paste the Job Description** in the text area.
2. **Upload your Resume (PDF)**.
3. Click **Analyze** to get:
   - JD Match %
   - Missing Keywords
   - Profile Summary

---

## 📂 Project Structure
```
resume-ats-tracker/
│-- app.py               # Main Streamlit app
│-- req.txt              # Python dependencies
│-- .env                 # API key 
│-- README.md            # Documentation
```

---

## 📸 Screenshots
### Home Page


<img width="1863" height="892" alt="Screenshot 1" src="https://github.com/user-attachments/assets/c188e652-82ff-4038-a1f2-dfedc6eefd24" />


---
### Analysis Example


<img width="1873" height="861" alt="Screenshot 2" src="https://github.com/user-attachments/assets/75ed3d47-7ca5-4103-a641-5a2b18bf7db2" />

---
### 🎥 Demo Video 


https://github.com/user-attachments/assets/ab6b94a2-82e7-4582-ad41-107ada86dac6



---

## ⚠️ Notes
- The accuracy depends on the **quality of your resume** and **clarity of the job description**.
- Ensure your **Google Gemini API key** has access to the `gemini-2.5-pro` model.

---
