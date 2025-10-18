from pdf2image import convert_from_path
from config import PDF_DPI

def pdf_to_images(pdf_path: str):
    """Convierte el PDF en imágenes (una por página)."""
    print(f"📄 Convirtiendo PDF a imágenes... ({pdf_path})")
    pages = convert_from_path(pdf_path, dpi=PDF_DPI)
    print(f"✅ Se generaron {len(pages)} imágenes.")
    return pages
