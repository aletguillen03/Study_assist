import os
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_summary(text):
    try:
        messages: list[ChatCompletionMessageParam] = [
            {
                "role": "system",
                "content": "Resumí el siguiente texto en español de forma clara, concisa y bien estructurada."
            },
            {
                "role": "user",
                "content": text[:3000]
            }
        ]

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.5,
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error al generar resumen: {str(e)}"