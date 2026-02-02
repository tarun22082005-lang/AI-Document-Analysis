import re


def summarize(text, max_sentences=5):
    sentences = re.split(r"[.!?]", text)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 30]

    if not sentences:
        return text[:500]

    return ". ".join(sentences[:max_sentences])

