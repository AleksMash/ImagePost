import telegram
import argparse
from dotenv import load_dotenv
from random import randint
import os

class NoImagesError(BaseException):
    pass

def publish_random_image():
    global bot
    images = os.listdir('images')
    if images:
        image=images[randint(0,len(images)-1)]
        with open(f'images/{image}', 'rb') as f:
            bot.send_document(chat_id=channel, document=f)
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
        with open(f'images/{image_file}', 'rb') as f:
            bot.send_document(chat_id=channel, document=f)
    except FileNotFoundError:
        print('no such file')
        publish_random_image()
else:
    publish_random_image()
