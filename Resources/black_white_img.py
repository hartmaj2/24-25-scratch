from PIL import Image
import numpy as np
import random

# Define an 8x8 grid for a smiley face
# 0 = black, 1 = white
smiley = [
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
]

# colorful = []

# for i in range(len(smiley)):
#     colorful.append([])
#     for j in range(len(smiley[i])):
#         if smiley[i][j] == 0:
#             colorful[i].append([0,0,0])
#         else:
#             colorful[i].append([255,0,0])

image_data = np.full((8,8,3),128,dtype=np.uint8)

for i in range(image_data.shape[0]):
    for j in range(image_data.shape[1]):
        if smiley[i][j] == 1:
            image_data[i][j][0] = random.randint(0,255)
            image_data[i][j][1] = random.randint(0,255)
            image_data[i][j][2] = random.randint(0,255)

        else:
            image_data[i][j][0] = 0
            image_data[i][j][1] = 0
            image_data[i][j][2] = 0


# Create the image from the data
image = Image.fromarray(image_data, 'RGB')
file_path = "random_colors_8x8.bmp"
image.save(file_path)

# Create a new image with mode '1' (1-bit pixels, black and white)
img = Image.new('1', (8, 8))

# Load the pixel data
pixels = img.load()

# Set the pixels
for y, row in enumerate(smiley):
    for x, value in enumerate(row):
        pixels[x, y] = value

# Save the image as a BMP
img.save("smiley.bmp")
print("8x8 smiley face saved as 'smiley.bmp'")
