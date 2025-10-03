import os

from docx import Document
from PyPDF2 import PdfReader


def load_document(file_path):
    """Loads a PDF or DOCX document and returns its text"""
    if file_path.endswith(".pdf"):
        reader = PdfReader(file_path)
        text = " ".join([page.extract_text() for page in reader.pages])
    elif file_path.endswith(".docx"):
        doc = Document(file_path)
        text = " ".join([para.text for para in doc.paragraphs])
    else:
        raise ValueError("Unsupported file format")
    return text


def load_all_cvs(folder_path):
    """Loads all CVs from a folder"""
    cvs = {}
    for filename in os.listdir(folder_path):
        if filename.endswith((".pdf", ".docx")):
            path = os.path.join(folder_path, filename)
            cvs[filename] = load_document(path)
    return cvs
