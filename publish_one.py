import telegram
import argparse
from dotenv import load_dotenv
from random import randint
import os
from pathlib2 import Path
from common import send_image_to_tgchannel


class NoImagesError(BaseException):
    pass


def publish_random_image(tg_bot, channel, image_folder_path):
    images = os.listdir(image_folder_path)
    if not images:
        raise NoImagesError('There are no images.'
                            ' You should download them first.')
    image = images[randint(0, len(images)-1)]
    file_path = Path.cwd() / image_folder_path / image
    send_image_to_tgchannel(file_path, tg_bot, channel)


def main():
    load_dotenv()
    channel = os.environ['TG_CHANNEL']
    parser = argparse.ArgumentParser(description='Publish specified'
                                                 ' images from the folder images')
    parser.add_argument('-file', 'image_file', nargs='?', type=str,
                        default='', help='image file to publish')
    parser.add_argument('-folder', 'image_folder_path', nargs='?', type=str,
                        default='images', help='Path to the image folder')
    args = parser.parse_args()
    image_file = args.image_file
    image_folder_path=args.image_folder_path
    bot = telegram.Bot(token=os.environ['TG_BOT_TOKEN'])
    if image_file:
        file_path = Path.cwd() / image_folder_path / image_file
        send_image_to_tgchannel(file_path, bot, channel)
    else:
        publish_random_image(bot, channel, image_folder_path)


if __name__ == "__main__":
    main()
