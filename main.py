import requests
import datetime as dt
import urllib.parse
import os
from dotenv import load_dotenv


load_dotenv()


def get_file_extension(file_url):
    url_parts=urllib.parse.urlsplit(file_url, scheme='', allow_fragments=True)
    path=urllib.parse.unquote(url_parts[2],encoding='utf-8', errors='replace')
    return os.path.splitext(path)[1]


def load_image(url, dir, name):
    if not os.path.exists(dir):
        os.makedirs(dir)
    filename = f'images\\{name}'
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v5/launches/latest'
    response = requests.get(url)
    response.raise_for_status()
    images = response.json()['links']['flickr']['original']
    if not len(images):
        url = 'https://api.spacexdata.com/v5/launches'
        response = requests.get(url)
        response.raise_for_status()
        all_launches = response.json()
        for launch in all_launches:
            images = launch['links']['flickr']['original']
            # находим первый запуск где более одного фото
            if len(images) > 1:
                break
    i = 1
    for image_num, image_url in enumerate(images):
        load_image(image_url, 'images', f'spacex_{image_num}.jpg')


def fetch_nasa_apod_pictures():
    nasa_token = os.environ['NASA_TOKEN']
    params={'api_key':nasa_token, 'count':30, 'thumbs':True}
    response=requests.get('https://api.nasa.gov/planetary/apod', params=params)
    response.raise_for_status()
    medias=response.json()
    for image_num, media in enumerate(medias):
        image_url=media['url']
        ext=get_file_extension(image_url)
        load_image(image_url,'images',f'nasa_apod_{image_num}{ext}')


def fetch_nasa_epic_pictures():
    nasa_token = os.environ['NASA_TOKEN']
    params = {'api_key': nasa_token}
    response=requests.get('https://api.nasa.gov/EPIC/api/natural/images', params=params)
    response.raise_for_status()
    images=response.json()
    for i in range(7):
        file_name=images[i]['image']
        image_date=dt.datetime.fromisoformat(images[i]['date'])
        url=f'https://api.nasa.gov/EPIC/archive/natural/{image_date.year}' \
            f'/{image_date.month}/{image_date.day:02}/png/{file_name}.png?api_key={nasa_token}'
        load_image(url,'images',f'nasa_epic_{i}.png')


if __name__ == '__main__':
    load_dotenv()
    response = requests.get(f'https://api.spacexdata.com/v5/launches/gbvhncgbfv')
    print(response.status_code)


    # put any test calls here ...
