import telegram
import argparse
from dotenv import load_dotenv
from random import shuffle
import os
from pathlib2 import Path
from common import send_image_to_tgchannel


class NetworkProblem(BaseException):
    pass

def main():
    load_dotenv()
    channel = os.environ['TG_CHANNEL']
    parser = argparse.ArgumentParser(
        description='Publish images from the folder images'
                    ' in specified interval (hours)'
    )
    parser.add_argument('interval', nargs='?', type=float,
                        default=4, help='publishing interval (hours)')
    parser.add_argument('image_folder_path', nargs='?', type=str,
                        default='images', help='Path to the image folder')
    args = parser.parse_args()
    interval = os.getenv('PUBLISHING_INTERVAL')
    if interval:
        interval = float(interval)*3600
    else:
        interval = args.interval*3600
    image_folder_path = args.image_folder_path
    images = os.listdir(image_folder_path)
    bot = telegram.Bot(token=os.environ['TG_BOT_TOKEN'])
    while True:
        shuffle(images)
        for image in images:
            file_path = Path.cwd() / image_folder_path / image
            send_image_to_tgchannel(file_path, bot, channel)


if __name__ == "__main__":
    main()

