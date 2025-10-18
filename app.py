import os
from flask import Flask, render_template, request, send_file, flash, redirect, url_for
from modules.pdf_converter import pdf_to_images
from modules.ocr_processor import extract_text_from_image
from modules.pptx_builder import create_presentation
from modules.utils import ensure_output_dir
from config import OUTPUT_DIR

app = Flask(__name__)
app.secret_key = "soymerchx-secret"  # Para mensajes flash

ensure_output_dir(OUTPUT_DIR)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "pdf_file" not in request.files:
            flash("No se seleccionó archivo PDF")
            return redirect(request.url)
        pdf_file = request.files["pdf_file"]
        if pdf_file.filename == "":
            flash("Nombre de archivo vacío")
            return redirect(request.url)

        # Guardar PDF temporalmente
        pdf_path = os.path.join(OUTPUT_DIR, pdf_file.filename)
        pdf_file.save(pdf_path)

        # Convertir PDF a imágenes
        pages = pdf_to_images(pdf_path)

        # OCR
        texts = [extract_text_from_image(page) for page in pages]

        # Crear PowerPoint
        output_path = os.path.join(OUTPUT_DIR, pdf_file.filename.replace(".pdf", "_editable.pptx"))
        create_presentation(pages, texts, output_path)

        return send_file(output_path, as_attachment=True)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
