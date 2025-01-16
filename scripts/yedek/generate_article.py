from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

class OpenAIGenerator:
    def __init__(self, openai_api_key):
        self.client = OpenAI(api_key=openai_api_key)

    def generate_article(self, file_paths):
        # Tüm transkriptleri birleştir
        combined_text = ""
        for file_path in file_paths:
            with open(file_path, 'r', encoding='utf-8') as file:
                combined_text += file.read() + "\n"

        # OpenAI'ye gönderilecek prompt
        prompt = (
            "Sen başarılı bir makale yazarısın. Aşağıdaki transkriptleri okuyup değerlendirerek, "
            "okuması yaklaşık 5 dakika süren bir makale yazar mısın? Makale, transkriptlerdeki "
            "ana fikirleri içermeli ve akıcı bir şekilde yazılmalıdır.\n\n"
            f"Transkriptler:\n{combined_text}"
        )

        # OpenAI API'sine istek gönder
        response = self.client.chat.completions.create(
            model="gpt-4",  # veya "gpt-3.5-turbo" kullanabilirsiniz
            messages=[
                {"role": "system", "content": "Sen başarılı bir makale yazarısın."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=2000,  # Makalenin uzunluğunu sınırla
            temperature=0.7,  # Yaratıcılık seviyesi (0-1 arası)
        )

        # Makaleyi döndür
        return {
            "title": "Oluşturulan Makale",
            "content": response.choices[0].message.content,
            "excerpt": response.choices[0].message.content[:150] + "...",  # Özet
            "categories": [],  # Kategoriler (isteğe bağlı)
            "tags": [],  # Etiketler (isteğe bağlı)
            "featured_image": "",  # Öne çıkan görsel (sonradan eklenebilir)
            "author": "AI",  # Yazar
            "date": "2023-10-15T10:00:00",  # Tarih
            "slug": "olusturulan-makale",  # URL için slug
            "meta": {
                "description": response.choices[0].message.content[:150] + "..."  # Meta açıklama
            }
        }

def generate_article_from_transcripts(file_paths, openai_api_key):
    generator = OpenAIGenerator(openai_api_key)
    print("OpenAI API Key:", os.getenv("OPENAI_API_KEY"))
    return generator.generate_article(file_paths)
