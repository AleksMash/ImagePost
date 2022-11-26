import argparse
import requests
from common import load_image, get_file_extension


class NoLaunchError(BaseException):
    pass


class NoLaunchImagesError(BaseException):
    pass


def get_images(launch_id):
    response = requests.get(
        f'https://api.spacexdata.com/v5/launches/{launch_id}'
    )
    if not response.ok:
        if response.status_code==404:
            raise NoLaunchError('There is no launch with specified ID')
        else:
            if response.status_code in (404, 500):
                response.raise_for_status()
    images = response.json()['links']['flickr']['original']
    if not images:
        raise NoLaunchImagesError(f'There is no images for'
                                  f' the launch: {launch_id}')
    return images


def save_images(images):
    for image_num, image_url in enumerate(images):
        file_ext = get_file_extension(image_url)
        load_image(image_url, 'images', f'spacex_{image_num}.{file_ext}')


def main():
    parser = argparse.ArgumentParser(
        description='Fetch launch images from spacex API for the specified ID'
                    ' (or for the latest launch if ID is not specified)'
    )
    parser.add_argument('launch_id', nargs='?',
                        default='latest', help='ID of the launch')
    args = parser.parse_args()
    images = get_images(args.launch_id)
    save_images(images)


if __name__ == "__main__":
    main()
