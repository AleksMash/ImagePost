import urllib.parse
import os
import requests


def get_file_extension(file_url):
    url_parts=urllib.parse.urlsplit(file_url, scheme='', allow_fragments=True)
    path=urllib.parse.unquote(url_parts[2],encoding='utf-8', errors='replace')
    return os.path.splitext(path)[1]


def load_image(url, dir, name):
    if not os.path.exists(dir):
        os.makedirs(dir)
    filename = f'{dir}\\{name}'
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)