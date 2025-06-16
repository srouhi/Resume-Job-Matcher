# 🤖 Resume-Job Matcher AI

Match your resume to any job description with AI — get instant feedback, missing skills, and improvement tips.

Built with NLP, embeddings, keyword extraction, and large language models. Hosted on [Hugging Face Spaces](https://huggingface.co/spaces/Srouhi/resume-job-matcher) with Streamlit.

---

## Demo

--> **Try it live**: [Resume-Job Matcher on Hugging Face Spaces](https://huggingface.co/spaces/Srouhi/resume-job-matcher)

---

## Overview

This AI-powered web app helps job applicants:

- ✅ Upload a resume and a job description (PDF, DOCX, TXT)
- 📊 Get a **match score** based on semantic similarity
- 🧠 See **missing skills and keywords** (via keyphrase extraction)
- ✍️ Receive **custom feedback suggestions** (via FLAN-T5 LLM)

---

## Technologies Used

| Category | Tools / Models |
|---------|----------------|
| Language Embeddings | [`sentence-transformers`](https://www.sbert.net/) — `all-MiniLM-L6-v2` |
| Keyword Extraction | [`KeyBERT`](https://github.com/MaartenGr/KeyBERT) |
| Feedback Generation | [`google/flan-t5-large`](https://huggingface.co/google/flan-t5-large) from Hugging Face Transformers |
| File Handling | PDF (PyPDF), DOCX, TXT support |
| App Framework | [`Streamlit`](https://streamlit.io) |
| Hosting | [`Hugging Face Spaces`](https://huggingface.co/spaces) |

---

## Project Structure
resume-job-matcher/
│
├── app.py # Streamlit UI logic
├── Embeddings.py # Similarity score logic
├── Feedbacks.py # LLM-based feedback generation
├── FileLoader.py # File upload and preprocessing
├── requirements.txt # Dependency list
└── README.md # Project overview and documentation


---

## 💡 Use Case

Ideal for:
- Candidates preparing resumes for different roles
- Career services & job coaches
- Resume optimization tools powered by AI

---

## Skills Demonstrated

✅ Natural Language Processing (NLP)  
✅ Semantic Search with Transformers  
✅ Keyword Extraction using BERT  
✅ Prompt Engineering for Feedback Generation  
✅ Streamlit App Development  
✅ Hosting AI apps with Hugging Face Spaces  
✅ Git & Version Control

---

## How to Run Locally

# Clone the repository
git clone https://github.com/Srouhi/resume-job-matcher.git
cd resume-job-matcher

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py

---

## Links

- 🎯 **[Live Demo on Hugging Face](https://huggingface.co/spaces/Srouhi/resume-job-matcher)**
- 📬 **Contact Me:** srouhi2@huskers.unl.edu
- 🧠 **[My Data Science Portfolio](https://github.com/Srouhi)**

---

## Author

**Shaghayegh Rouhi**  
Data Science | AI/ML Development | NLP Applications
🌐 Portfolio Website
🌐 [LinkedIn Profile](https://www.linkedin.com/in/Shay-shaghayegh-rouhi-aba3892a1)
