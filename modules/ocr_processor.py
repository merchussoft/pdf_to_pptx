import pytesseract
from config import TESSERACT_PATH, OCR_LANGUAGE

# Configurar Tesseract
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def extract_text_from_image(image):
    """Aplica OCR y devuelve texto editable."""
    text = pytesseract.image_to_string(image, lang=OCR_LANGUAGE)
    return text.strip()
