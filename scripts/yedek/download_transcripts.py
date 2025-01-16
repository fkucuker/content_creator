from utils import sanitize_filename, sanitize_date
import os
from tqdm import tqdm
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled

def download_transcripts(video_data, transcripts_dir, playlist_name):
    playlist_folder = os.path.join(transcripts_dir, sanitize_filename(playlist_name))
    if not os.path.exists(playlist_folder):
        os.makedirs(playlist_folder)

    for video in tqdm(video_data, desc="Downloading Transcripts"):
        # Başlık ve tarih temizliği
        clean_title = sanitize_filename(video["title"], max_length=40)
        clean_date = sanitize_date(video["date"])
        file_name = f"{clean_title} - {clean_date}.txt"
        file_path = os.path.join(playlist_folder, file_name)

        try:
            transcript = YouTubeTranscriptApi.get_transcript(video["id"])
            transcript_text = "\n".join([t["text"] for t in transcript])

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(transcript_text)
        except TranscriptsDisabled:
            print(f"No transcript available for {video['title']}")
        except Exception as e:
            print(f"Error downloading transcript for {video['title']}: {e}")
