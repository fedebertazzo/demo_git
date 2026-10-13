import os
import io
from google import genai
from google.genai import types
from PIL import Image

# 1. Inicializa el cliente oficial
client = genai.Client()

# 2. Configura los parámetros usando GenerateContentConfig (CORREGIDO)
config = types.GenerateContentConfig(
    response_modalities=["IMAGE"],  # Fuerza al modelo a devolver solo imágenes
    image_config=types.ImageConfig(
        aspect_ratio="1:1"          # Opciones válidas: "1:1", "3:4", "16:9", etc.
    )
)

print("Generando imagen con Nano Banana...")

# 3. Llama al modelo mediante generate_content
response = client.models.generate_content(
    model="gemini-nano-banana-2.1",  # O utiliza "gemini-nano-banana-2.1"
    contents=input("Prompt de Nano Banana: "),
    config=config
)

# 4. Extrae la imagen utilizando los métodos nativos del SDK
for part in response.parts:
    if part.inline_data:
        image_bytes = part.inline_data.data
        
        # Guardamos los bytes en un archivo de imagen usando Pillow
        image = Image.open(io.BytesIO(image_bytes))
        output_filename = "resultado_final.jpg"
        image.save(output_filename)
        
        print(f"¡Éxito! Imagen guardada como: {output_filename}")


