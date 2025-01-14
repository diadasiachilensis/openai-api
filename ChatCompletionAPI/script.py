import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client= OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

responde=client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {
        "role": "system",
        "content": "¿Cuál es la capital de España?" #reglas de comportamiento
    },
    {
        "role": "user",
        "content": "Hola, como estas?" #respuesta a la pregunta
    },
    {
        "role": "assistant",
        "content": "Que es Madrid?" #respuesta al usuario con la información obtenida del modelo de OpenAI
    }
    ],
    #maxima de informacion que puede porvver el modelo 
    #Define la cantidad máxima de tokens (palabras o fragmentos de palabras) que puede devolver la respuesta. Controla la longitud de la salida generada
    max_tokens=100,
    #Ajusta el tono de la respuesta 
    #Ajusta la creatividad de las respuestas. Un valor bajo (cerca de 0.1) produce respuestas más predecibles y deterministas, mientras que un valor alto (cerca de 1) genera respuestas más creativas y variadas.
    #0.7 es lo recomendable. 
    #en maatemticas qyue no sea tan creativo y la tempeerature debe ser maximo 0.2
    #generar una hisotria o un texto debe ser superior a 0.5
    temperature=0.7
)

print(responde.choices[0].message.content)