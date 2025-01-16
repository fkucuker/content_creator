from dotenv import load_dotenv
import os
import sys
import requests  # Görseli indirmek için eklendi
from scripts.fetch_videos import fetch_videos_from_playlist
from scripts.download_transcripts import download_transcripts
from scripts.generate_article import generate_article_from_transcripts
from scripts.publish_to_wordpress import publish_article_to_wordpress
from scripts.generate_image import generate_image_with_dalle
from utils import sanitize_filename, sanitize_date  # utils.py'den fonksiyonları içe aktar

# Projenin kök dizinini Python'a ekle
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# .env dosyasından ortam değişkenlerini yükle
load_dotenv()

def save_image_to_pics(image_url, image_name):
    pics_dir = "pics"
    if not os.path.exists(pics_dir):
        os.makedirs(pics_dir)
    image_path = os.path.join(pics_dir, image_name)
    response = requests.get(image_url)
    with open(image_path, "wb") as f:
        f.write(response.content)
    return image_path

if __name__ == "__main__":
    # API Anahtarları ve Dosya Yolları
    YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
    PLAYLIST_FILE = "youtube_list.txt"
    TRANSCRIPTS_DIR = "transcripts"
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    WORDPRESS_BASE_URL = os.getenv("WORDPRESS_BASE_URL")
    WORDPRESS_USERNAME = os.getenv("WORDPRESS_USERNAME")
    WORDPRESS_PASSWORD = os.getenv("WORDPRESS_PASSWORD")

    # API anahtarını kontrol et
    if not YOUTUBE_API_KEY:
        raise ValueError("YouTube API Key is missing. Please check your .env file.")
    if not OPENAI_API_KEY:
        raise ValueError("OpenAI API Key is missing. Please check your .env file.")

    print("YouTube API Key:", YOUTUBE_API_KEY)
    print("OpenAI API Key:", OPENAI_API_KEY)
    print("Playlist File:", PLAYLIST_FILE)

    # 1. Playlist'ten video bilgilerini çek
    video_data = fetch_videos_from_playlist(YOUTUBE_API_KEY, PLAYLIST_FILE)

    # 2. Her bir playlist için transkript indir
    for playlist in video_data:
        playlist_name = playlist.get("playlist_name")
        videos = playlist.get("videos")
        download_transcripts(videos, TRANSCRIPTS_DIR, playlist_name)

        # 3. Transkriptlerden makale oluştur
        file_paths = [
            os.path.join(TRANSCRIPTS_DIR, playlist_name, f"{sanitize_filename(video['title'], max_length=40)} - {sanitize_date(video['date'])}.txt")
            for video in videos
        ]
        article_data = generate_article_from_transcripts(file_paths, OPENAI_API_KEY)

        # 4. Makale için öne çıkan görsel oluştur
        print(article_data['title'])
        print(article_data['content'])
        safe_prompt = f"Create a hyper-realistic photograph that visually represents the theme of '{article_data['title']}'. The image should be clean, professional, and highly detailed, capturing the essence of the topic in a visually compelling way. Use realistic lighting, textures, and colors to ensure the photo looks authentic and lifelike."
        image_url = generate_image_with_dalle(safe_prompt, OPENAI_API_KEY)
        article_data["featured_image"] = image_url

        # Görseli 'pics' klasörüne kaydet
        image_name = sanitize_filename(article_data['title']) + ".jpg"
        local_image_path = save_image_to_pics(image_url, image_name)
        print(f"Görsel 'pics' klasörüne kaydedildi: {local_image_path}")

        # 5. Makaleyi WordPress'e yayınla
        #publish_article_to_wordpress(article_data, WORDPRESS_BASE_URL, WORDPRESS_USERNAME, WORDPRESS_PASSWORD)
