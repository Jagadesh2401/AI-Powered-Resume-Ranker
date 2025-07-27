
import fitz  # PyMuPDF
import spacy

nlp = spacy.load("en_core_web_sm")

def save_resume_and_extract_text(path):
    text = ""
    with fitz.open(path) as doc:
        for page in doc:
            text += page.get_text()
    return preprocess_text(text)

def preprocess_text(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens)
