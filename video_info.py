import re
import requests
from bs4 import BeautifulSoup
from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(link):
    if "youtube.com" in link:
        pattern = r'youtube\.com/watch\?v=([a-zA-Z0-9_-]+)'
        match = re.search(pattern, link)
        return match.group(1) if match else None
    elif "youtu.be" in link:
        pattern = r"youtu\.be/([a-zA-Z0-9_-]+)"
        match = re.search(pattern, link)
        return match.group(1) if match else None
    return None


def get_video_title(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    title_tag = soup.find("meta", property="og:title")
    return title_tag["content"] if title_tag else "Title not found"


def get_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([item['text'] for item in transcript_list])
    except Exception as e:
        return str(e)


def get_transcript_with_timestamps(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_with_timestamps = ""
        for item in transcript_list:
            start_time = item['start']
            text = item['text']
            transcript_with_timestamps += f"{start_time}: {text}\n"
        return transcript_with_timestamps
    except Exception as e:
        return str(e)
