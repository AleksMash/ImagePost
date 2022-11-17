import argparse
import requests
from common import load_image, get_file_extension

class NoLaunchError(BaseException):
    pass

class NoLaunchImagesError(BaseException):
    pass



parser=argparse.ArgumentParser(
    description='Fetch launch images from spacex API for the specified ID'
                ' (or for the latest launch if ID is not specified)'
)
parser.add_argument('launch_id', nargs='?', default='latest', help='ID of the launch')
args = parser.parse_args()
launch_id=args.launch_id
response = requests.get(f'https://api.spacexdata.com/v5/launches/{launch_id}')
if not response.ok:
    raise NoLaunchError('There is no launch with specified ID')
images = response.json()['links']['flickr']['original']
if not len(images):
    raise NoLaunchImagesError(f'There is no images for the launch: {launch_id}')
for image_num, image_url in enumerate(images):
        file_ext = get_file_extension(image_url)
        load_image(image_url, 'images', f'spacex_{image_num}.{file_ext}')
