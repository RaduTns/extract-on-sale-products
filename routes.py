from fastapi import APIRouter, UploadFile, File
from config import PDF_PATH
import os
import shutil
from models.product import Product

from service.extraction import extract_products_via_gemini
from utils.pdf_processing import pdf_to_jpeg, delete_local_pdf
from service.supabase_service import save_to_supabase

router = APIRouter()


@router.get("/hello")
def say_hello():
    return {"message": "Hello from routes.py"}

@router.post("/upload-pdf")
async def pdf_to_image(file: UploadFile = File(...)):
    file_path = os.path.join(PDF_PATH, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"message": "Extraordinar"}

@router.get("/process-pdf")
def process_pdf():
    try:
        pdf_to_jpeg()
        delete_local_pdf()
        return {"message": "PDF processed and deleted"}
    except Exception as e:
        return {"message": e}

@router.get("/process-images")
def process_images():
    response = extract_products_via_gemini()
    return {"message": response}

@router.post("/save-data")
def save_products():
    response = extract_products_via_gemini()
    products = []
    for r in response:
        for product in r:
            products.append(Product.createObjectFromJson(product))
    try:
        for product in products:
            save_to_supabase(product.dict())
    except Exception as e:
        return {"message": e}
    return {"message": "success"}

