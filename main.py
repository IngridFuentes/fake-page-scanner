import os
import requests
from bs4 import BeautifulSoup
from PIL import Image
import imagehash

"""step1 hash image"""

def hash_image(image_path):
   img = Image.open(image_path)
   hash_value = imagehash.average_hash(img)
   return hash_value

image_path = "images/tmobile-logo.jpg"
hashed_image = hash_image(image_path)

print("Image hashed:", hashed_image)

"""Step2 Web scraping"""

# def download_images_from_url(url, download_folder="images"):
#    if not os.path.exists(download_folder):
#       os.makedirs(download_folder)

#       response = requests.get(url)
#       soup = BeautifulSoup(response.text, "html.parser")

#       img_tags = soup.find_all("img")
#       img_urls = []

#       for img in img_tags:
#          img_url = img.get("src")
#          if img_url:
#             if not img_url.startswith("http"):
#                img_url = url + img_url
#                img_urls.append(img_url)

      # for img_url in img_urls:
      #    try:
      #       img_response = requests.get(img_url, stream=True)
      #       img_name = os.path.join(download_folder, img_url.split("/")[-1])
      #       with open(img_name, "wb") as f:
      #          for chunk in img_response.iter_content(chunk_size=128):
      #             f.write(chunk)
      #             print("fDownloaded: {img_name}")

