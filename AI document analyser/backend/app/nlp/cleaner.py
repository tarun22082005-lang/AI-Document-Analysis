import re


def clean_text(text):
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"\S+@\S+", "", text)
    text = re.sub(r"\b\d{10,}\b", "", text)
    text = re.sub(r"\b(19|20)\d{2}\b", "", text)
    text = re.sub(r"[^a-zA-Z., ]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


