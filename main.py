import os
from modules.pdf_converter import pdf_to_images
from modules.ocr_processor import extract_text_from_image
from modules.pptx_builder import create_presentation
from modules.utils import ensure_output_dir
from config import OUTPUT_DIR

def main():
    print("=== 🧠 PDF a PowerPoint con OCR (by SoyMerchX) ===")
    pdf_path = input("📂 Ingresa la ruta del archivo PDF: ").strip().replace('"', '')

    ensure_output_dir(OUTPUT_DIR)

    # 1️⃣ Convertir PDF a imágenes
    pages = pdf_to_images(pdf_path)

    # 2️⃣ Aplicar OCR a cada página
    print("🔍 Extrayendo texto (OCR en progreso)...")
    texts = [extract_text_from_image(page) for page in pages]

    # 3️⃣ Crear PowerPoint editable
    output_path = os.path.join(OUTPUT_DIR, "presentacion_editable.pptx")
    create_presentation(pages, texts, output_path)

    print("\n✅ Conversión completa.")
    print(f"📁 Archivo final: {output_path}")

if __name__ == "__main__":
    main()
