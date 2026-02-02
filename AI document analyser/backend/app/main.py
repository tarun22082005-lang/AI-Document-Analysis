from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from app.pdf.extractor import extract_text
from app.nlp.cleaner import clean_text
from app.nlp.summarizer import summarize
from app.nlp.keywords import extract_keywords
from app.nlp.sentiment import analyze_sentiment

app = FastAPI(title="AI Document Analyzer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/analyze")
async def analyze_pdf(file: UploadFile = File(...)):

    try:
        text = extract_text(file.file)

        if not text:
            return {
                "status": "failed",
                "message": "No readable text found in PDF",
                "note": "Scanned or image-based PDFs need OCR"
            }

        text = clean_text(text)

        summary = summarize(text)
        keywords = extract_keywords(text)
        sentiment = analyze_sentiment(text)

        return {
            "status": "success",
            "summary": summary,
            "keywords": keywords,
            "sentiment": sentiment
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
