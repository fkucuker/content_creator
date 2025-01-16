from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

class OpenAIGenerator:
    def __init__(self, openai_api_key):
        self.client = OpenAI(api_key=openai_api_key)

    def ask_openai(self, prompt, max_tokens=2000, temperature=0.7):
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Sen başarılı bir içerik üreticisisin."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=temperature,
        )
        return response.choices[0].message.content.strip()

    def generate_article(self, file_paths):
        combined_text = ""
        for file_path in file_paths:
            with open(file_path, 'r', encoding='utf-8') as file:
                combined_text += file.read() + "\n"

        # Başlık oluşturma
        title_prompt = (
            "Aşağıdaki transkriptleri inceleyerek ilgi çekici ve özgün bir makale başlığı oluştur.\n\n"
            f"Transkriptler:\n{combined_text}"
        )
        title = self.ask_openai(title_prompt, max_tokens=60)

        # İçerik oluşturma
        content_prompt = (
            "Aşağıdaki transkriptleri temel alarak 2000 kelimelik detaylı, bilgilendirici ve akıcı bir makale yaz.\n\n"
            f"Transkriptler:\n{combined_text}"
        )
        content = self.ask_openai(content_prompt)

        # Özet oluşturma
        excerpt_prompt = (
            "Aşağıdaki makaleden etkileyici ve bilgilendirici bir özet çıkar (en fazla 150 kelime):\n\n"
            f"{content}"
        )
        excerpt = self.ask_openai(excerpt_prompt, max_tokens=150)

        # Kategori belirleme
        category_prompt = (
            "Aşağıdaki makale için uygun bir kategori belirle. Sadece kategori ismini yaz:\n\n"
            f"{content}"
        )
        category = self.ask_openai(category_prompt, max_tokens=20)

        # Etiketler oluşturma
        tags_prompt = (
            "Aşağıdaki makale için ilgili 5 tane etiket (anahtar kelime) oluştur. Etiketleri virgülle ayır:\n\n"
            f"{content}"
        )
        tags = self.ask_openai(tags_prompt, max_tokens=50).split(',')

        # Meta açıklama oluşturma
        meta_description_prompt = (
            "SEO için aşağıdaki makaleye uygun, dikkat çekici bir meta açıklama oluştur (en fazla 160 karakter):\n\n"
            f"{content}"
        )
        meta_description = self.ask_openai(meta_description_prompt, max_tokens=160)

        return {
            "title": title,
            "content": content,
            "excerpt": excerpt,
            "categories": [category.strip()],
            "tags": [tag.strip() for tag in tags],
            "featured_image": "",
            "author": "AI",
            "date": "2023-10-15T10:00:00",
            "slug": title.lower().replace(" ", "-"),
            "meta": {
                "description": meta_description
            }
        }

def generate_article_from_transcripts(file_paths, openai_api_key):
    generator = OpenAIGenerator(openai_api_key)
    return generator.generate_article(file_paths)
