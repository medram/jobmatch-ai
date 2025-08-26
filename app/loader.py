from PyPDF2 import PdfReader
from docx import Document
import os

def load_document(file_path):
    """Charge un document PDF ou DOCX et retourne son texte"""
    if file_path.endswith('.pdf'):
        reader = PdfReader(file_path)
        text = " ".join([page.extract_text() for page in reader.pages])
    elif file_path.endswith('.docx'):
        doc = Document(file_path)
        text = " ".join([para.text for para in doc.paragraphs])
    else:
        raise ValueError("Format de fichier non supporté")
    return text

def load_all_cvs(folder_path):
    """Charge tous les CVs d'un dossier"""
    cvs = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(('.pdf', '.docx')):
            path = os.path.join(folder_path, filename)
            cvs[filename] = load_document(path)
    return cvs