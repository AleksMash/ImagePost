import requests
import argparse
from common import load_image, get_file_extension
from dotenv import load_dotenv
import os


def get_medias(token, count):
    params = {'api_key': token, 'count': count}
    response = requests.get('https://api.nasa.gov/planetary/apod',
                            params=params)
    response.raise_for_status()
    return response.json()


def save_images(medias):
    for image_num, media in enumerate(medias):
        if media['media_type'] == 'image':
            image_url = media['url']
            ext = get_file_extension(image_url)
            load_image(image_url, 'images', f'nasa_apod_{image_num}{ext}')


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description='Load images of the'
                                                 ' day from NASA API')
    parser.add_argument('-c', nargs='?', type=int,
                        default=15, help='number of images (default=15)')
    args = parser.parse_args()
    medias = get_medias(os.environ['NASA_TOKEN'], args.c)
    save_images(medias)


if __name__ == "__main__":
    main()
