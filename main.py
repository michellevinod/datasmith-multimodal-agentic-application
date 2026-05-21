from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from services.ocr_service import extract_text_from_image
from services.orchestrator import process_request
from services.pdf_service import extract_text_from_pdf
from services.audio_service import (
    transcribe_audio
)
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request,
        "index.html"
    )


@app.post("/chat")
async def chat(
    message: str = Form(""),
    file: UploadFile = File(None)
):

    uploaded_filename = None

    extracted_text = ""
    audio_duration = None

    if file and file.filename:

        uploaded_filename = file.filename

        file_path = f"uploads/{file.filename}"

        with open(file_path, "wb") as f:
            f.write(await file.read())

        if file.filename.endswith(
            (".png", ".jpg", ".jpeg")
        ):

            extracted_text = extract_text_from_image(
                file_path
            )

        elif file.filename.endswith(".pdf"):

            extracted_text = extract_text_from_pdf(
                file_path
            )

        elif file.filename.endswith(
            (".mp3", ".wav", ".m4a")
        ):

            audio_result = transcribe_audio(
            file_path
            )

            extracted_text = (
            audio_result["transcript"]
            )

            audio_duration = (
            audio_result["duration"]
            )

    result = process_request(
        message,
        extracted_text
    )

    return {
    "message": message,
    "uploaded_file": uploaded_filename,
    "audio_duration": audio_duration,
    "extracted_text": extracted_text,
    "result": result
    }