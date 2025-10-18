import os

def ensure_output_dir(path):
    """Crea la carpeta de salida si no existe."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"📁 Carpeta de salida creada: {path}")
