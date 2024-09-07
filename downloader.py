
import yt_dlp
from pyrogram import Client, enums
import config
import os
import asyncio
import re
import time
from modules.database import DataBase
import subprocess
from PIL import Image

db = DataBase()

def clear_downloads():
    fs = os.listdir('downloads')
    for f in fs:
        delete_file(f"downloads/{f}")

def crop_to_square(image_path, out_path):
    with Image.open(image_path) as img:
        width, height = img.size
        new_size = min(width, height)
        left = (width - new_size) / 2
        top = (height - new_size) / 2
        right = (width + new_size) / 2
        bottom = (height + new_size) / 2
        img = img.crop((left, top, right, bottom))
        img.save(out_path)

def sanitize_filename(text):
    sanitized_text = re.sub(r'[\\/:"*?<>|]+', '', text)
    sanitized_text = sanitized_text.replace(' ', '_')
    return sanitized_text

def download_audio(video_url, output_path, user_id, thumb, bot_username):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        ydl_opts = {
            'format': 'bestaudio/best', 
            'postprocessors': [
                {
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '320',
                },
                {
                    'key': 'FFmpegMetadata',
                },
                {
                    'key': 'EmbedThumbnail',
                }
            ],
            'outtmpl': output_path[:-4],
            'writethumbnail': True,
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
        except:
            ydl_opts['cookiefile'] = 'cookies/youtube.txt'
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
        audio_thumb = f"{thumb[:-4]}_audio.jpg"
        try:
            crop_to_square(thumb, audio_thumb)
        except:
            pass
        app = Client(f"sessions/{user_id}", bot_token=config.bot_token, api_id=config.api_id, api_hash=config.api_hash)
        app.start()
        try:
            app.send_audio(chat_id=user_id, audio=output_path, thumb=audio_thumb, title=output_path[:-4].replace("downloads/", ""), caption=f"💎 <b><a href='https://t.me/{bot_username}'>@{bot_username}</a></b>", parse_mode=enums.ParseMode.HTML)
        except:
            app.send_audio(chat_id=user_id, audio=output_path, title=output_path[:-4].replace("downloads/", ""), caption=f"💎 <b><a href='https://t.me/{bot_username}'>@{bot_username}</a></b>", parse_mode=enums.ParseMode.HTML)
        app.stop()
        delete_file(audio_thumb)
    except Exception as e:
        print(e)
    db.set_work(user_id, 0)
    delete_file(output_path)

def get_video_formats(url, domain):
    ydl_opts = {
        'listformats': True,
        'cookiefile': 'cookies/insta.txt'
    }
    if domain.startswith("youtu"):
        ydl_opts['cookiefile'] = 'cookies/youtube.txt'
    
    if domain == 'instagram.com':
        ydl_opts['cookiefile'] = 'cookies/insta.txt'

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        return info_dict

def get_domain(url):
    domain_pattern = r'^(https?:\/\/)?(www\.)?([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})(\/.*)?$'
    match = re.match(domain_pattern, url)
    if match:
        return match.group(3)
    return None

def delete_file(f_path):
    for _ in range(5):
        try:
            os.remove(f_path)
            break
        except:
            pass
        time.sleep(5)

def simple_downloader(url, output_path, user_id, domain, video_format=None, title_orig="", thumb=None):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': output_path
        }
        if domain == "instagram.com":
            ydl_opts['cookiefile'] = 'cookies/insta.txt'
            ydl_opts['quiet'] = True

        elif domain.startswith("youtu"):
            ydl_opts['format'] = video_format+"+bestaudio"
            ydl_opts['merge_output_format'] = "mp4"

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            info_dict = ydl.extract_info(url, download=False)
            width = 0
            height = 0
            fs = info_dict['formats']
            for f in fs:
                if f['format_id'] == video_format:
                    width = f['width']
                    height = f['height']
            app = Client(f"sessions/{user_id}", bot_token=config.bot_token, api_id=config.api_id, api_hash=config.api_hash)
            app.start()
            app.send_video(chat_id=user_id, video=output_path, caption=title_orig, thumb=thumb, width=width, height=height)
            app.stop()
    except:
        try:
            if domain in ["instagram.com", "twitter.com", "x.com"]:
                output_path = output_path.replace("mp4", "jpg")
                command = [
                    "gallery-dl",
                    "--config", "gallery-dl.conf",
                    "--filename", output_path.replace("downloads/", ""),
                    "--directory", "downloads/",
                    url
                ]
                subprocess.run(command)
                app = Client(f"sessions/{user_id}", bot_token=config.bot_token, api_id=config.api_id, api_hash=config.api_hash)
                app.start()
                app.send_photo(chat_id=user_id, photo=output_path)
                app.stop()
        except:
            pass
    db.set_work(user_id, 0)
    delete_file(output_path)
