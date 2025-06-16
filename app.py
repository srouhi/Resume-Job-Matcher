import streamlit as st
import os
from FileLoader import Read_n_Clean
from Embeddings import match_calc, missing_key
from Feedbacks import gen_feedback

st.title("Resume-Job Matcher")

resume_file = st.file_uploader("Upload Resume (.pdf, .docx, .txt)", type=["pdf", "docx", "txt"])
job_file = st.file_uploader("Upload Job Description (.pdf, .docx, .txt)", type=["pdf", "docx", "txt"])

if resume_file and job_file:
    resume_text = Read_n_Clean(resume_file)
    job_text = Read_n_Clean(job_file)

    matchScore = match_calc(resume_text, job_text)
    st.write(f"**Match Score:** {matchScore}%")

    missing_keywords = missing_key(resume_text, job_text)
    if missing_keywords:
        st.write("**Missing Skills:**")
        for Kw in missing_keywords:
            st.write(f"- {Kw}")
    else:
        st.write("Great! Your resume covers the key terms.")

    feedback = gen_feedback(resume_text, job_text, missing_keywords)

    with st.expander("Show Feedback"):
        st.markdown("**Feedback:**")
        for line in feedback.split("\n"):
            st.markdown(f"- {line.strip()}")

