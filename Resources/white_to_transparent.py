from PIL import Image, ImageSequence

# Open the GIF
img = Image.open("Resources/baldi-happy.gif")

# Process each frame
frames = []
for frame in ImageSequence.Iterator(img):
    # Convert frame to RGBA to enable transparency
    frame = frame.convert("RGBA")
    datas = frame.getdata()

    # Replace white background with transparency
    new_data = []
    for item in datas:
        # Change all white (also shades of whites)
        # pixels to transparent
        if item[0] > 222 and item[1] > 222 and item[2] > 222:
            new_data.append((255, 255, 255, 0))  # Set transparency
        else:
            new_data.append(item)
    frame.putdata(new_data)
    frames.append(frame)

# Save as a new GIF
frames[0].save(
    "output_gif.gif",
    save_all=True,
    append_images=frames[1:],
    duration=img.info["duration"],
    loop=img.info["loop"],
    disposal=2  # Prevents background overwrite
)
