from google import genai #Instalar la libreria desde comando PIP en consola: pip install google-genai
from getpass import getpass
from key_google import GOOGLE_API_KEY

#IMPORTANTE: Antes de ejecutar el código seguir los pasos para crear una "API Key".

#Una "API Key" es una secuencia cifrada que autentica el uso de la librería de la plataforma Google Gemini u OpenIA ChatGPT a ejecutarse desde el código Pyhton.

#El usuario deberá registrar una cuenta en la plataforma para poder generar su propia "API Key".

#Cada "API Key" es única y privada de cada usuario. Por seguridad nunca debe compartirse o publicarla (ejemplo: No subir el archivo con la API Key en GitHub)


# client = genai.Client(api_key=getpass("Ingrese su API KEY: "))
client = genai.Client(api_key=GOOGLE_API_KEY)

# jugador=input("Ingrese el nombre del jugador: ")
seleccion=input("Ingrese el nombre de la selección: ")

response = client.models.generate_content(
    model="gemini-3.5-flash-lite", #Elegir el modelo de LLM 
    # contents=input("Ingrese su pregunta: "))
    # contents=f"Dime las estadísticas deportivas oficiales de FIFA de {jugador} en su selección: fecha de nacimiento, edad, club al que juega actualmente, fecha de debut en su selección, partidos jugados en su seleccion, minutos jugados en su selección, goles, asistencias, promedio de gol por partido, tarjetas rojas y tarjetas amarillas. Responde el resultado en sólo formato de un diccionario de Python usando 'stats' como nombre de la variable tipo diccionario, sin otro texto ni comentarios. En caso de que el nombre del jugador no exista o no tengas datos oficiales de FIFA, el resultado es un diccionario con valores 'None' en cada clave del diccionario."
    contents=f"Busca el listado oficial de jugadores convocados de FIFA que tengas disponible de la selección de {seleccion}. Entrega el resultado en formato lista de python donde cada elemento de esa lista es el nombre y apellido del jugador, su dorsal y su posición. Ejemplo: seleccion=[['Lionel Messi',10, 'Mediocampista'], ['Emiliano Marinez', 23, 'Arquero']].En el caso que no encuentres información entrega el resultado con una lista vacía. Ejemplo: seleccion=[]. Para todo resultado sólo muestra la lista de Python sin texto ni comentarios.")
print(response.text)
with open("respuesta.txt","w",encoding="utf-8") as respuesta_api:
    respuesta_api.write(response.text)