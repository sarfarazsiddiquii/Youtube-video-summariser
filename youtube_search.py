from googleapiclient.discovery import build
import os
from dotenv import load_dotenv


load_dotenv()

def get_youtube_service():
    api_key = os.getenv('YOUTUBE_API_KEY') 
    return build('youtube', 'v3', developerKey=api_key)

def fetch_video_links(keyword):
    youtube = get_youtube_service()
    search_response = youtube.search().list(
        q=keyword,
        part='id,snippet',
        maxResults=5,
        type='video'
    ).execute()

    links = []
    for item in search_response.get('items', []):
        video_id = item['id']['videoId']
        links.append(f"https://www.youtube.com/watch?v={video_id}")
    return links
