import telegram
import argparse
from dotenv import load_dotenv
from random import randint
import os

def publish_random_image():
    global bot
    images = os.listdir('images')
    if images:
        image=images[randint(0,len(images)-1)]
        bot.send_document(chat_id=channel, document=open(f'images/{image}', 'rb'))
    else:
        raise Exception('There are no images. You should download them first.')


load_dotenv()
channel=os.environ['TEL_CHANNEL']
parser = argparse.ArgumentParser(description='Publish specified images from the folder images')
parser.add_argument('image_file', nargs='?', type=str, default='', help='image file to publish')
args = parser.parse_args()
image_file=args.image_file
bot = telegram.Bot(token=os.environ['BOT_TOKEN'])
if image_file:
    try:
        bot.send_document(chat_id=channel, document=open(f'images/{image_file}', 'rb'))
    except FileNotFoundError:
        print('no such file')
        publish_random_image()
else:
    publish_random_image()
