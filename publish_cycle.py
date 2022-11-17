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
        # try to send for 5 times if having troubles with Internet connection, otherwise raise our exception (see above)
        for i in range(5):
            connection_ok=False
            try:
                file_path = Path.cwd() / 'images' / image
                send_image_to_tgchannel(file_path, bot, channel)
            except telegram.error.NetworkError:
                print('Попытка', i)
                if i>0:
                    sleep(3)
            else:
                connection_ok=True
                break
        if connection_ok:
            sleep(interval)
        else:
            raise NetworkProblem('Проблема с сетевым подключением')
