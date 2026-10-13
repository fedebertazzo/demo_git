from google import genai
from getpass import getpass

client = genai.Client(api_key=getpass())


response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=input("Ingrese su pregunta: "))
print(response.text)
with open("respuesta.md","w",encoding="utf-8") as respuesta_api:
    respuesta_api.write(response.text)