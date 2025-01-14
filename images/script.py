import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client= OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

response = [{
    "role": "system",
    "content": "Eres un aisstenet que analiza las iamgenes con gran detalle."
},
{
    "role": "user",
    "content": "hola, puedes analizar esta imange?"
}
]