import os
import shutil
import pytesseract
from PIL import Image
from pdf2image import convert_from_path


# 원본 폴더 경로
source_folder_path = '/Users/jinsang/OCR/XAI-OCR/DO_File'

# 대상 폴더 경로 (PDF 파일을 복사할 폴더)
destination_folder_path = '/Users/jinsang/OCR/XAI-OCR/DO_Result'

# 원본 폴더 구조를 순회하면서 PDF 파일을 찾고 복사하기
for folder_path, _, files in os.walk(source_folder_path):
    for file_name in files:
        if file_name.endswith('.pdf'):
            # PDF 파일인 경우 해당 파일의 경로
            source_pdf_file_path = os.path.join(folder_path, file_name)
            
            # 같은 이름의 txt파일 이름
            new_filename = os.path.splitext(file_name)[0] + '.txt'
            
            # 대상 폴더에 원본 폴더 구조와 동일한 경로 생성
            relative_path = os.path.relpath(folder_path, source_folder_path)
            destination_path = os.path.join(destination_folder_path, relative_path)
            

            # 대상 폴더 경로가 없는 경우 생성
            if not os.path.exists(destination_path):
                os.makedirs(destination_path)
                
             # 새로 생기는 txt파일 
            destination_txt_file_path = os.path.join(destination_path, new_filename)
                
            # pdf file을 가져오기
            pdf_path = source_pdf_file_path
            images = convert_from_path(pdf_path)

            # pytesseract 모델로 텍스트 읽기  
            i = 0
            
            for image in images:
                i += 1
                text = pytesseract.image_to_string(image)
                if i == 1 :
                    with open(destination_txt_file_path, 'w', encoding='utf-8') as txt_file:
                        txt_file.write(text)
                else:
                    with open(destination_txt_file_path, 'a', encoding='utf-8') as txt_file:
                        txt_file.write(text)
        
                
            
            
            
            print(f"Text : {source_pdf_file_path} to {destination_txt_file_path}")