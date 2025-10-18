from docx import Document
from docx.shared import Inches
import os

def create_docx(pages, texts, output_path):
    """Genera un Word editable con OCR y opcionalmente imágenes."""
    doc = Document()

    for page, text in zip(pages, texts):
        doc.add_paragraph(text)
        # Opcional: agregar la imagen debajo del texto
        img_path = os.path.join("temp_page.png")
        page.save(img_path)
        doc.add_picture(img_path, width=Inches(6))

    doc.save(output_path)
    print(f"🎯 Word generado en: {output_path}")
