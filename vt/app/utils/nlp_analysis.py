# utils/nlp_analysis.py
import spacy

nlp = spacy.load('en_core_web_sm')

def extract_keywords(text):
    doc = nlp(text)
    keywords = [token.text for token in doc if token.is_alpha and not token.is_stop]
    return keywords[:10]  # Retourne les 10 mots-clés principaux
