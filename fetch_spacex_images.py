import argparse
import requests
from common import load_image, get_file_extension


parser=argparse.ArgumentParser(
    description='Fetch launch images from spacex API for the specified ID'
                ' (or for the latest launch if ID is not specified)'
)
parser.add_argument('--launch_id', type=str, default='', help='ID of the launch')
args = parser.parse_args()
launch_id=args.launch_id
if launch_id:
    response = requests.get(f'https://api.spacexdata.com/v5/launches/{launch_id}')
    if not response.status_code==200:
        raise Exception('There is no launch with specified ID')
    images = response.json()['links']['flickr']['original']
    if not len(images):
        raise Exception('No images for the launch with specidied ID')
else:
    response = requests.get('https://api.spacexdata.com/v5/launches/latest')
    response.raise_for_status()
    images = response.json()['links']['flickr']['original']
    if not len(images):
        raise Exception('No images for the latest launch')
for image_num, image_url in enumerate(images):
        file_ext = get_file_extension(image_url)
        load_image(image_url, 'spacex_images', f'spacex_{image_num}.{file_ext}')
