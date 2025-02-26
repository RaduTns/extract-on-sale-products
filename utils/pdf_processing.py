from pdf2image import convert_from_path
import os
from config import IMAGES_PATH, PDF_PATH

def pdf_to_jpeg():
    pdf_files = [f for f in os.listdir(PDF_PATH) if f.lower().endswith('.pdf')]
    for pdf_file in pdf_files:
        pdf_path = os.path.join(PDF_PATH, pdf_file)
        pages = convert_from_path(pdf_path)
        for count, page in enumerate(pages):
            image_filename = f'page{count}.jpg'
            output_path = os.path.join(IMAGES_PATH, image_filename)
            page.save(output_path, 'JPEG')

def delete_local_pdf():
    pdf_files = [f for f in os.listdir(PDF_PATH) if f.lower().endswith('.pdf')]
    for pdf_file in pdf_files:
        pdf_path = os.path.join(PDF_PATH, pdf_file)
        os.remove(pdf_path)

