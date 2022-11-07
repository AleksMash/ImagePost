import requests
from common import load_image, get_file_extension
from dotenv import load_dotenv
import os


load_dotenv()

nasa_token = os.environ['NASA_TOKEN']
params = {'api_key': nasa_token, 'count': 15, 'thumbs': True}
response = requests.get('https://api.nasa.gov/planetary/apod', params=params)
response.raise_for_status()
medias = response.json()
for image_num, media in enumerate(medias):
    image_url = media['url']
    ext = get_file_extension(image_url)
    load_image(image_url, 'nasa_apod_images', f'nasa_apod_{image_num}{ext}')
