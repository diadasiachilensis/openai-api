import os
from openai import OpenAI
from dotenv import load_dotenv
import base64
import json  # Necesario para serializar la lista


load_dotenv()

client= OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

#esta funcion permite pasar en binario base64 la imagen
def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Lista de objetos en el campo "content"
user_message_content = [
    {
        "type": "text",
        "text": "Hola, ¿puedes analizar esta imagen?"
    },
    {
        "type": "image_url",
        "image_url": {
            "url": f"data:image/png;base64,{encode_image_to_base64('images/panoramica.jpg')}"
        }
    }
]

# Mensajes para la solicitud
messages = [
    {
        "role": "system",
        "content": "Eres un asistente que analiza las imágenes con gran detalle."
    },
    {
        "role": "user",
        "content": json.dumps(user_message_content)  # Serializamos la lista como un string JSON
    }
]

response=client.chat.completions.create(
    model='gpt-4o',
    messages=messages,
    temperature=0.5
)

print('Respuesta del analisis de la iamgen')
print(response.choices[0].message.content)