import telegram
import argparse
from dotenv import load_dotenv
from random import shuffle
from time import sleep
import os
from pathlib2 import Path
from common import send_image_to_tgchannel

class NetworkProblem(BaseException):
    pass

load_dotenv()
channel=os.environ['TG_CHANNEL']
parser = argparse.ArgumentParser(
    description='Publish images from the folder images'
                ' in specified interval (hours)'
)
parser.add_argument('interval', nargs='?', type=float, default=4, help='publishing interval (hours)')
args = parser.parse_args()
try:
    interval=float(os.environ['PUBLISHING_INTERVAL'])*3600
except KeyError:
   interval=args.interval*3600
images=os.listdir('images')
bot = telegram.Bot(token=os.environ['TG_BOT_TOKEN'])
while True:
    shuffle(images)
    for image in images:
        file_path = Path.cwd() / 'images' / image
        send_image_to_tgchannel(file_path, bot, channel)
