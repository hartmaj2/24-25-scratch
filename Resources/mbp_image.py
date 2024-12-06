import numpy as np
from PIL import Image

# random_image_data = np.random.randint(0, 256, (8, 8, 3), dtype=np.uint8)
image_data = np.full((8,8,3),128,dtype=np.uint8)

for i in range(image_data.shape[0]):
    for j in range(image_data.shape[1]):
        image_data[i][j][0] = 255
        image_data[i][j][1] = 0
        image_data[i][j][2] = 0


# Create the image from the data
image = Image.fromarray(image_data, 'RGB')

# Save the image as BMP
file_path = "random_colors_8x8.bmp"
image.save(file_path)