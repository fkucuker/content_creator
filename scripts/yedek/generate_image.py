from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def generate_image_with_dalle(prompt, openai_api_key):
    """
    DALL·E 3 ile bir görsel oluşturur ve URL'sini döndürür.

    :param prompt: Görsel oluşturma için metin
    :param openai_api_key: OpenAI API anahtarı
    :return: Görselin URL'si
    """
    client = OpenAI(api_key=openai_api_key)
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    return response.data[0].url
