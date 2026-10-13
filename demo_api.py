from openai import OpenAI

# Inicializamos el cliente apuntando al servidor local de Ollama
client = OpenAI(
    base_url='http://localhost:11434/v1', # <--- Crucial: añade el '/v1' al final
    api_key='ollama', # <--- Puede ser cualquier texto, Ollama lo ignora
)

# Definimos el comportamiento de nuestro agente
instrucciones_sistema = ("Eres un agente local ultra-eficiente. Responde de forma simple en un máximo de 500 caracteres.")
    # "Eres un agente local ultra-eficiente. Respondes de forma clara, directa y utilizas un tono profesional. Al finalizar de tu respuesta no hagas una pregunta para continuar, simplemente finaliza allí."


try:
    prompt=input("Escribe el prompt: ")
    # Realizamos la llamada utilizando la sintaxis estándar de OpenAI
    response = client.chat.completions.create(
        model='llama3.2', # <--- Asegúrate de haber hecho antes 'ollama run llama3.2'
        messages=[
            {"role": "system", "content": instrucciones_sistema},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7 # Controla la creatividad del agente
    )

    # Extraemos y mostramos la respuesta del agente
    print(response.choices[0].message.content)

except Exception as e:
    print(f"Error al conectar con Ollama: {e}")
    print("Asegúrate de que Ollama se esté ejecutando en tu sistema.")
