import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import os


# pdf file을 가져오기
pdf_path = '/Users/jinsang/OCR/XAI-OCR/DO_File/LA/11-29-2022/23PO-1522.pdf'
images = convert_from_path(pdf_path)

# pytesseract 모델로 텍스트 읽기  
for image in images:
    text = pytesseract.image_to_string(image)
    print(text)

print(pytesseract.get_tesseract_version())


