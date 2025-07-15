# Demonstrates how we can create an image using Python

import numpy as np
from PIL import Image
import random

image_data = np.full((8,8,3),128,dtype=np.uint8)

for i in range(image_data.shape[0]):
    for j in range(image_data.shape[1]):
        image_data[i][j][0] = random.randint(0,255)
        image_data[i][j][1] = random.randint(0,255)
        image_data[i][j][2] = random.randint(0,255)


# Create the image from the data
image = Image.fromarray(image_data, 'RGB')

# Save the image as BMP
file_name= "random_colors_8x8.bmp"
image.save(file_name)
print(f"Image saved as '{file_name}'")