import os
from pytube import YouTube 


def get_yt_id(url):
    return url.split("/")[-1]

def video_to_path(download_path, url):
    yt_id = get_yt_id(url)
    return os.path.join(download_path, yt_id + ".mp3")

def check_video_exists(download_path, url):
    p = video_to_path(download_path, url)
    if os.path.exists(p):
        return p

def download_youtube_audio(url, download_path):
    print(f"Downloading {url}")
    yt_id = get_yt_id(url)
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first() 
    path = video.download(
        output_path=download_path,
        filename=yt_id + ".mp3",
    ) 
    print(f"{yt.title} has been successfully downloaded to {path}")
    return path, video
