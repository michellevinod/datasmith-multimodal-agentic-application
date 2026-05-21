import pdfplumber
from pdf2image import convert_from_path
from services.ocr_service import extract_text_from_image


POPPLER_PATH = r"C:\Users\Dell\Downloads\Release-26.02.0-0\poppler-26.02.0\Library\bin"


def extract_text_from_pdf(pdf_path):

    text = ""

    try:

        with pdfplumber.open(pdf_path) as pdf:

            for page in pdf.pages:

                extracted = page.extract_text()

                if extracted:
                    text += extracted + "\n"

    except Exception as e:

        print("PDF extraction error:", e)

    # OCR FALLBACK
    if len(text.strip()) < 20:

        print("Using OCR fallback for scanned PDF")

        images = convert_from_path(
            pdf_path,
            poppler_path=POPPLER_PATH
        )

        for i, image in enumerate(images):

            image_path = f"uploads/page_{i}.png"

            image.save(image_path, "PNG")

            ocr_text = extract_text_from_image(
                image_path
            )

            text += ocr_text + "\n"

    return text