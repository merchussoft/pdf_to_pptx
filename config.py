import os

# ⚙️ Ruta al ejecutable de Tesseract (ajústala según tu instalación)
# Si instalaste Tesseract con el instalador de UB Mannheim (recomendado):
# https://github.com/UB-Mannheim/tesseract/wiki
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Idioma del OCR
OCR_LANGUAGE = "spa"

# Directorio de salida
OUTPUT_DIR = os.path.join(os.getcwd(), "output")

# DPI (resolución de lectura del PDF)
PDF_DPI = 300
