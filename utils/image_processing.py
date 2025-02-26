from config import IMAGES_PATH
import os

from service.google_llama import ask_gemini
from utils.text_processing import process_raw_json_from_gemini


def extract_products_via_gemini():
    images = [f for f in os.listdir(IMAGES_PATH) if f.lower().endswith('.jpg')]
    response = []
    for image in images:
        img_path = os.path.join(IMAGES_PATH, image)
        response.append(process_raw_json_from_gemini(ask_gemini(img_path)))
        break
    return response
