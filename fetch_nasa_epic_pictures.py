import requests
import datetime as dt
from common import load_image, get_file_extension
from dotenv import load_dotenv
import os


load_dotenv()


nasa_token = os.environ['NASA_TOKEN']
params = {'api_key': nasa_token}
response = requests.get('https://api.nasa.gov/EPIC/api/natural/images', params=params)
response.raise_for_status()
images = response.json()
for i in range(7):
    file_name = images[i]['image']
    image_date = dt.datetime.fromisoformat(images[i]['date'])
    url = f'https://api.nasa.gov/EPIC/archive/natural/{image_date.year}' \
          f'/{image_date.month}/{image_date.day:02}/png/{file_name}.png?api_key={nasa_token}'
    load_image(url, 'images', f'nasa_epic_{i}.png')
