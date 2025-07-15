from PIL import Image
import numpy as np
import random

# Define an 8x8 bitmap for the picture
# 0 = black, 1 = white
image_bitmap = [
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
]

def generate_colorful_image(bitmap : list[list[int]]) -> None:
    # (8,8,3) refers to height, width, number of channels
    # We have 3 channels (R,G,B)
    image_data = np.full((8,8,3),128,dtype=np.uint8)

    for i in range(image_data.shape[0]):
        for j in range(image_data.shape[1]):
            if image_bitmap[i][j] == 1:
                image_data[i][j][0] = random.randint(0,255)
                image_data[i][j][1] = random.randint(0,255)
                image_data[i][j][2] = random.randint(0,255)

            else:
                image_data[i][j][0] = 0
                image_data[i][j][1] = 0
                image_data[i][j][2] = 0


    # Create the image from the data
    img = Image.fromarray(image_data, 'RGB')
    filename = "colorful.bmp"
    img.save(filename)
    print(f"8x8 colorful image saved as '{filename}'")

def generate_black_white_image(bitmap : list[list[int]]) -> None:
    # Create a new image with mode '1' (1-bit pixels, black and white)
    img = Image.new('1', (8, 8))

    # Load the pixel data
    pixels = img.load()

    if pixels is None:
        return

    # Set the pixels
    for y, row in enumerate(bitmap):
        for x, value in enumerate(row):
            pixels[x, y] = value

    # Save the image as a BMP
    filename = "black_white.bmp"
    img.save(filename)
    print(f"8x8 black and white image saved as '{filename}'")

def generate_grayscale_image(bitmap : list[list[int]]) -> None:
    # Create a new image with mode 'L' (grayscale)
    img = Image.new('L', (8, 8))

    # Load the pixel data
    pixels = img.load()

    if pixels is None:
        return

    # Set the pixels
    for y, row in enumerate(bitmap):
        for x, value in enumerate(row):
            pixels[x, y] = value * random.randint(1,255)

    # Save the image as a BMP
    filename = "grayscale.bmp"
    img.save(filename)
    print(f"8x8 grayscale image saved as '{filename}'")

generate_colorful_image(image_bitmap)
generate_black_white_image(image_bitmap)
generate_grayscale_image(image_bitmap)

# Pillow Image Modes (mode argument for Image.new, etc.)
#
# Mode   Meaning                    Channels  Bits/channel  Example pixel value
# ------------------------------------------------------------------------------
#  1     1-bit pixels (B/W)         1         1 bit         0 (black) or 1 (white)
#  L     Grayscale (8-bit)          1         8 bits        0 (black) – 255 (white)
#  P     Palettized (8-bit index)   1         8 bits        Palette index (0–255)
#  RGB   True color (24-bit)        3         8 bits        (R, G, B) e.g. (255, 0, 0)
#  RGBA  True color + alpha         4         8 bits        (R, G, B, A)
#  CMYK  Cyan/Magenta/Yellow/Key    4         8 bits        (C, M, Y, K)
#  F     Floating point grayscale   1         32 bits float 0.0 – 1.0
#  I     32-bit signed integer      1         32 bits int   Integer pixel values