'''
1. Recommended to create your own API key to use, from https://api.nasa.gov/
2. Save the code on your on premises IDE or IDLE and enjoy the view of Mars.
'''

import requests
import random
import os
from PIL import Image
from io import BytesIO

def get_mars_image(api_key):
    base_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
    params = {
        "sol": random.randint(100, 2000),
        "api_key": api_key,
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if "photos" in data and len(data["photos"]) > 0:
        random_photo = random.choice(data["photos"])
        return random_photo["img_src"]
    else:
        return None

def download_and_save_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        image_bytes = BytesIO(response.content)
        image = Image.open(image_bytes)
        image.save(save_path, format="JPEG")
        print("Image saved:", save_path)
    else:
        print("Failed to download image.")

def main():
    # Replace with your Personal Key in the place {API KEY} NASA API key
    # You will get the key for https://api.nasa.gov/
    nasa_api_key = "API KEY"

    image_url = get_mars_image(nasa_api_key)
    if image_url:
        output_folder = "mars_images"
        os.makedirs(output_folder, exist_ok=True)
        image_name = os.path.basename(image_url)
        image_path = os.path.join(output_folder, image_name)
        download_and_save_image(image_url, image_path)
    else:
        print("No images found.")

if __name__ == "__main__":
    main()
