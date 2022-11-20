import requests
import argparse
import datetime as dt
from common import load_image
from dotenv import load_dotenv
import os


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description='Load images of the'
                                                 ' Earth from NASA API')
    parser.add_argument('max', nargs='?', type=int,
                        default=7, help='max number of images')
    args = parser.parse_args()
    max_count = args.max
    nasa_token = os.environ['NASA_TOKEN']
    params = {'api_key': nasa_token}
    response = requests.get('https://api.nasa.gov/EPIC/api/natural/images',
                            params=params)
    response.raise_for_status()
    images = response.json()
    for image_num, image in enumerate(images):
        file_name = image['image']
        image_date = dt.datetime.fromisoformat(image['date']).strftime('%Y/%m/%d')
        url = f'https://api.nasa.gov/EPIC/archive/natural/' \
              f'{image_date}/png/{file_name}.png'
        load_image(url, 'images', f'nasa_epic_{image_num}.png', params)
        if image_num == max_count - 1:
            break


if __name__ == "__main__":
    main()
