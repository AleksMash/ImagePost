import requests
import argparse
from common import load_image, get_file_extension
from dotenv import load_dotenv
import os


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description='Load images of the'
                                                 ' day from NASA API')
    parser.add_argument('-c', nargs='?', type=int,
                        default=15, help='number of images (default=15)')
    args = parser.parse_args()
    nasa_token = os.environ['NASA_TOKEN']
    params = {'api_key': nasa_token, 'count': args.c}
    response = requests.get('https://api.nasa.gov/planetary/apod', params=params)
    response.raise_for_status()
    medias = response.json()
    for image_num, media in enumerate(medias):
        if media['media_type'] == 'image':
            image_url = media['url']
            ext = get_file_extension(image_url)
            load_image(image_url, 'images', f'nasa_apod_{image_num}{ext}')


if __name__ == "__main__":
    main()
