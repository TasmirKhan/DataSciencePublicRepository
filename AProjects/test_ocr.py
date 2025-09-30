# test_ocr.py
from ocr_utils import image_to_text

text = image_to_text("sample_image.png")  # replace with your image or PDF
print("Extracted text:\n")
print(text)
