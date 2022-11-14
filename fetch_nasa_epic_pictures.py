import requests
import datetime as dt
from common import load_image
from dotenv import load_dotenv
import os

load_dotenv()


nasa_token = os.environ['NASA_TOKEN']
params = {'api_key': nasa_token}
response = requests.get('https://api.nasa.gov/EPIC/api/natural/images', params=params)
response.raise_for_status()
images = response.json()
print(len(images))
for image_num, image in enumerate(images):
    file_name = image['image']
    image_date = dt.datetime.fromisoformat(image['date'])
    url = f'https://api.nasa.gov/EPIC/archive/natural/{image_date.year}' \
          f'/{image_date.month}/{image_date.day:02}/png/{file_name}.png'
    load_image(url, 'images', f'nasa_epic_{image_num}.png', params)
    print(image_num)
    if image_num==6:
        break
