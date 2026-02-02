from PyPDF2 import PdfReader


def extract_text(pdf_file):
    try:
        reader = PdfReader(pdf_file)

        if reader.is_encrypted:
            reader.decrypt("")

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        if not text.strip():
            return None

        return text

    except Exception as e:
        return None

