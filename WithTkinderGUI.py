'''
This is just Tknider GUI based project.
1. Recommended to create your own API key to use, from https://api.nasa.gov/
2. Save the code on your on premises IDE or IDLE and enjoy the view of Mars.
'''
import requests
import random
import os
from PIL import Image
from io import BytesIO
import tkinter as tk
from tkinter import messagebox

class MarsImageDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mars Image Downloader")
        # Replace with your Personal Key in the place {API KEY} NASA API key
        # You will get the key for https://api.nasa.gov/
        self.nasa_api_key = "API KEY"

        self.download_button = tk.Button(
            root, text="Download Random Mars Image", command=self.download_image
        )
        self.download_button.pack(pady=20)

    def get_mars_image(self):
        base_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
        params = {
            "sol": random.randint(100, 2000),
            "api_key": self.nasa_api_key,
        }

        response = requests.get(base_url, params=params)
        data = response.json()

        if "photos" in data and len(data["photos"]) > 0:
            random_photo = random.choice(data["photos"])
            return random_photo["img_src"]
        else:
            return None

    def download_and_save_image(self):
        image_url = self.get_mars_image()
        if image_url:
            output_folder = "mars_images"
            os.makedirs(output_folder, exist_ok=True)
            image_name = os.path.basename(image_url)
            image_path = os.path.join(output_folder, image_name)

            response = requests.get(image_url)
            if response.status_code == 200:
                image_bytes = BytesIO(response.content)
                image = Image.open(image_bytes)
                image.save(image_path, format="JPEG")
                messagebox.showinfo("Image Downloaded", f"Image saved as {image_path}")
            else:
                messagebox.showerror("Error", "Failed to download image.")
        else:
            messagebox.showinfo("No Images", "No images found.")

    def download_image(self):
        self.download_and_save_image()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x200")  # Set the window size (width x height)
    app = MarsImageDownloaderApp(root)
    root.mainloop()
