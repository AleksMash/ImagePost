import telegram
import argparse
from dotenv import load_dotenv
from random import shuffle
from time import sleep
import os


load_dotenv()
channel=os.environ['TEL_CHANNEL']
try:
    interval=float(os.environ['PUBLISHING_INTERVAL'])*3600
except KeyError:
   parser=argparse.ArgumentParser(
        description='Publish images from the folder images'
                    ' in specified interval (hours)'
    )
   parser.add_argument('interval', nargs='?', type=float, default=4, help='publishing interval (hours)')
   args = parser.parse_args()
   interval=args.interval*3600
images=os.listdir('images')
bot = telegram.Bot(token=os.environ['BOT_TOKEN'])
while True:
    shuffle(images)
    for image in images:
        bot.send_document(chat_id=channel, document=open(f'images/{image}', 'rb'))
        sleep(interval)
