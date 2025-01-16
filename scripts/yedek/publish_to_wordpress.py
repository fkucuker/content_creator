import requests
from dotenv import load_dotenv
import os

load_dotenv()

class WordPressPublisher:
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.api_url = f"{self.base_url}/wp-json/wp/v2/posts"

    def publish_article(self, article_data):
        post_data = {
            "title": article_data["title"],
            "content": article_data["content"],
            "status": "publish",
            "excerpt": article_data["excerpt"],
            "categories": article_data["categories"],
            "tags": article_data["tags"],
            "featured_media": self.upload_featured_image(article_data["featured_image"]),
            "author": article_data["author"],
            "date": article_data["date"],
            "slug": article_data["slug"],
            "meta": {
                "description": article_data["meta"]["description"]
            }
        }

        try:
            response = requests.post(
                self.api_url,
                json=post_data,
                auth=(self.username, self.password)
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return f"Hata: {e}"

    def upload_featured_image(self, image_url):
        if not image_url:
            return None

        image_data = requests.get(image_url).content
        upload_url = f"{self.base_url}/wp-json/wp/v2/media"
        headers = {
            "Content-Disposition": f'attachment; filename="{image_url.split("/")[-1]}"',
            "Content-Type": "image/jpeg"
        }
        response = requests.post(
            upload_url,
            data=image_data,
            headers=headers,
            auth=(self.username, self.password)
        )
        response.raise_for_status()
        return response.json()["id"]

def publish_article_to_wordpress(article_data, base_url, username, password):
    publisher = WordPressPublisher(base_url, username, password)
    return publisher.publish_article(article_data)
