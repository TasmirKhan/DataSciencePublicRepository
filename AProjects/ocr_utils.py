# ocr_utils.py

from PIL import Image
import pytesseract
import io
from docx import Document
import csv
from pdf2image import convert_from_path

def image_to_text(path, lang="eng"):
    """
    Extract text from an image or PDF.
    path: path to image or PDF file
    lang: language code for Tesseract (default English)
    """
    ext = path.rsplit('.', 1)[1].lower()
    text = ""

    if ext == "pdf":
        images = convert_from_path(path)
    else:
        images = [Image.open(path)]

    for img in images:
        text += pytesseract.image_to_string(img, lang=lang) + "\n"

    return text.strip()


# Functions to convert text to bytes for downloading

def text_to_txt_bytes(text):
    bio = io.BytesIO()
    bio.write(text.encode('utf-8'))
    bio.seek(0)
    return bio

def text_to_docx_bytes(text):
    bio = io.BytesIO()
    doc = Document()
    for line in text.splitlines():
        doc.add_paragraph(line)
    doc.save(bio)
    bio.seek(0)
    return bio

def text_to_csv_bytes(text):
    bio = io.BytesIO()
    writer = csv.writer(io.TextIOWrapper(bio, encoding='utf-8', newline=''))
    for line in text.splitlines():
        writer.writerow([line])
    bio.seek(0)
    return bio
