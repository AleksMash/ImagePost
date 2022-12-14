import argparse
import datetime as dt
import os

import requests
from dotenv import load_dotenv

from common import load_image


def get_images(params):
    response = requests.get("https://api.nasa.gov/EPIC/api/natural/images", params=params)
    response.raise_for_status()
    return response.json()


def save_images(images, max_count, params):
    for image_num, image in enumerate(images[:max_count]):
        file_name = image["image"]
        image_date = dt.datetime.fromisoformat(image["date"]).strftime("%Y/%m/%d")
        url = f"https://api.nasa.gov/EPIC/archive/natural/" f"{image_date}/png/{file_name}.png"
        load_image(url, "images", f"nasa_epic_{image_num}.png", params)


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description="Load images of the" " Earth from NASA API")
    parser.add_argument("max", nargs="?", type=int, default=7, help="max number of images")
    args = parser.parse_args()
    params = {"api_key": os.environ["NASA_TOKEN"]}
    images = get_images(params)
    max_count = args.max if args.max <= len(images) else len(images)
    save_images(images, max_count, params)


if __name__ == "__main__":
    main()
