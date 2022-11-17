import urllib.parse
import os
import requests
from pathlib2 import Path


def get_file_extension(file_url):
    url_parts=urllib.parse.urlsplit(file_url, scheme='', allow_fragments=True)
    path=urllib.parse.unquote(url_parts[2],encoding='utf-8', errors='replace')
    return os.path.splitext(path)[1]


def load_image(url, dir, name, params={}):
    os.makedirs(dir, exist_ok=True)
    filename = Path.cwd()/dir/name
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


def send_image_to_tgchannel(image_file_path, tg_bot, channel):
    with open(image_file_path, 'rb') as f:
        tg_bot.send_document(chat_id=channel, document=f)
