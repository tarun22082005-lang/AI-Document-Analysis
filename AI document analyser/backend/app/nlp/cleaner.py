import re


def clean_text(text):
    # remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # remove emails
    text = re.sub(r"\S+@\S+", "", text)

    # remove phone numbers
    text = re.sub(r"\b\d{10,}\b", "", text)

    # remove years
    text = re.sub(r"\b(19|20)\d{2}\b", "", text)

    # remove extra symbols
    text = re.sub(r"[^a-zA-Z., ]", " ", text)

    # remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()
