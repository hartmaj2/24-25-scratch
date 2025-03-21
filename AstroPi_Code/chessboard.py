# Import the libraries
from sense_hat import SenseHat
from time import sleep

# Set up the Sense HAT
sense = SenseHat()
sense.set_rotation(270, False)

# Set up the colour sensor
sense.color.gain = 60 # Set the sensitivity of the sensor
sense.color.integration_cycles = 64 # The interval at which the reading will be taken


width = 8
image = []

b = (0,0,0)
data = sense.color
s = (data.red,data.green,data.blue)

for i in range(width):
    for j in range(width):
        if (j + i) % 2 == 0:
            image.append(s)
        else:
            image.append(b)

sense.set_pixels(image)
# Display the image

# Display the image
