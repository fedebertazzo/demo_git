import os
import io
from google import genai #Instalar con comando PIP en consola: pip install genai
from google.genai import types
from PIL import Image #Instalar con comando PIP en consola: pip install Pillow

#IMPORTANTE: Antes de ejecutar el código seguir los pasos para crear una "API Key".

#Una "API Key" es una secuencia cifrada que autentica el uso de la librería de la plataforma Google Gemini u OpenIA ChatGPT a ejecutarse desde el código Pyhton.

#El usuario deberá registrar una cuenta en la plataforma para poder generar su propia "API Key".

#Cada "API Key" es única y privada de cada usuario. Por seguridad nunca debe compartirse o publicarla (ejemplo: No subir el archivo con la API Key en GitHub)

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
    model="gemini-nano-banana-2.1",  # O utiliza el nombre del modelo disponible en la plataforma
    contents=input("Prompt de Nano Banana: "), #Usamos un input para el prompt, pero también puede quedar fijo o sujeto a una variable del código.
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