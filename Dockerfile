# Imagen base con Python
FROM python:3.12-slim

# Instalar Poppler (para pdf2image) y Tesseract (para OCR)
RUN apt-get update && apt-get install -y \
    poppler-utils \
    tesseract-ocr \
    tesseract-ocr-spa \
    && rm -rf /var/lib/apt/lists/*

# Crear directorio de trabajo
WORKDIR /app

# Copiar requirements y luego instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
COPY . .

# Exponer el puerto de Flask
EXPOSE 5000

# Comando por defecto
CMD ["python", "app.py"]
