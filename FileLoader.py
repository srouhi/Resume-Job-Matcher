import io
import re
import string
from docx import Document
from pypdf import PdfReader

def Read_n_Clean(upload_file):
    text= ""
    filename = upload_file.name

    #read files of diff formats
    if filename.endswith(".pdf"):
        reader = PdfReader(upload_file)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "

    elif filename.endswith(".docx"):
        document = Document(upload_file)
        text = "\n".join([p.text for p in document.paragraphs])

    elif filename.endswith(".txt"):
        text = upload_file.read().decode('utf-8')

    else:
        return ""

    #cleaning
    text = text.lower()
    text = re.sub(r'\s+', ' ', text).strip() 
    text = text.translate(str.maketrans('', '', string.punctuation)) 
    return text.strip()
