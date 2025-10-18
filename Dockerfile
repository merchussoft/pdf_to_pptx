# imagen base con python
FROM python:3.12-slim

## Intalar Poppler (necesario para pdf2image)
RUN apt-get update && apt-get dist-upgrade -y && apt-get update && \
    apt-get install -y poppler-utils && \
    rm -rf /vasr/lib/apt/lists/*

# Crear directorio de trabajo
WORKDIR /app

## Copiar requirements.txt y luego instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

## Copiar el resto de la aplicacion

COPY . .

# Comando por defecto 
CMD ["python", "main.py"]