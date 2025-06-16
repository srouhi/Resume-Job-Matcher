from transformers import pipeline

pipe = pipeline("text2text-generation", model="google/flan-t5-large")

def gen_feedback(resume_text, job_text, missing_skills):
    if not missing_skills:
        return "FEEDBACK:\nYour resume already covers all the important keywords!"

    prompt = f"""
You are a resume reviewer. Some important job skills are missing in this resume.

Missing Skills: {", ".join(missing_skills)}

Resume: {resume_text[:300]}
Job Description: {job_text[:300]}

Write **exactly 3 specific suggestions** to help the candidate improve their resume.
Start with: 'In order to improve your resume to better match the job description, we suggest the following points:'
"""

    result = pipe(prompt, max_length=300, do_sample=False)[0]["generated_text"]
    return result.strip()

