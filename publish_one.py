import telegram
import argparse
from dotenv import load_dotenv
from random import randint
import os
from pathlib2 import Path
from common import send_image_to_tgchannel

class NoImagesError(BaseException):
    pass

def publish_random_image(tg_bot):
    images = os.listdir('images')
    if images:
        image=images[randint(0,len(images)-1)]
        file_path = Path.cwd() / 'images' / image
        send_image_to_tgchannel(file_path, tg_bot, channel)
    else:
        raise NoImagesError('There are no images. You should download them first.')


load_dotenv()
channel=os.environ['TG_CHANNEL']
parser = argparse.ArgumentParser(description='Publish specified images from the folder images')
parser.add_argument('image_file', nargs='?', type=str, default='', help='image file to publish')
args = parser.parse_args()
image_file=args.image_file
bot = telegram.Bot(token=os.environ['TG_BOT_TOKEN'])
if image_file:
    try:
        file_path = Path.cwd() / 'images' / image_file
        send_image_to_tgchannel(file_path, bot, channel)
    except FileNotFoundError:
        print('no such file')
        publish_random_image(bot)
else:
    publish_random_image(bot)
