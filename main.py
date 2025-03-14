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

