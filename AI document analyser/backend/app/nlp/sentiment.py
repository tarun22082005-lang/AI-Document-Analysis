from textblob import TextBlob


def analyze_sentiment(text):
    if not text.strip():
        return "Neutral"

    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0.05:
        return "Positive"
    elif polarity < -0.05:
        return "Negative"
    else:
        return "Neutral"
