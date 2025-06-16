from sentence_transformers import SentenceTransformer, util
from keybert import KeyBERT

model = SentenceTransformer('all-MiniLM-L6-v2')
Kw_model = KeyBERT()

def match_calc(resume_text, job_text):
    if isinstance(resume_text, str):
        resume_text = [resume_text]
    if isinstance(job_text, str):
        job_text = [job_text]

    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    job_embedding = model.encode(job_text, convert_to_tensor=True)
    
    similarity = util.cos_sim(resume_embedding[0], job_embedding[0]).item()
    return round(similarity * 100)

def missing_key(resume_text, job_text):
    job_keywords = Kw_model.extract_keywords(job_text, keyphrase_ngram_range=(1, 2), stop_words='english', top_n=10)
    job_keywords = [kw[0].lower() for kw in job_keywords]
    missing = [kw for kw in job_keywords if kw not in resume_text.lower()]
    return missing


