from google import genai
from google.genai import types
from config import GOOGLE_GENAI_API_KEY
import PIL.Image

client = genai.Client(api_key=GOOGLE_GENAI_API_KEY)

question = """Extract products and their prices from the image in a json format having elements 
of the type {product_name, initial_price, discounted_price}. Provide only the JSON Output"""

def ask_gemini(img_path):
    img = PIL.Image.open(img_path)
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[question, img])
    return response.text