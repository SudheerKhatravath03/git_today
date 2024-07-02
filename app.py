from PIL import Image


import os

input_folder = '/path/to/image'
output_folder = '/path/to/resized_images'
desired_size = (100, 200)

for filename in os.listdir(input_folder):
    with Image.open(os.path.join(input_folder, filename)) as img:
        img.thumbnail(desired_size)
        img.save(os.path.join(output_folder, filename))
