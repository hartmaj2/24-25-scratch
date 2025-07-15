# Demonstrates how we can create a .wav sound file using Python

# Can be interesting to test which frequencies we an hear and which not
# My hearing range is from 20 Hz to 15_000 Hz

import numpy as np
import scipy.io.wavfile

# Function to generate a sine wave
def generate_sine_wave(freq, duration, sample_rate):
    timesteps = np.linspace(0, duration, int(sample_rate * duration))
    wave = np.sin(2 * np.pi * freq * timesteps)
    return wave

# Generates tones displaced by an octave
sample_rate = 44100  # Samples per second
duration = 0.2
tones = []
freq = 30
while freq < 2000:
    tones.append(generate_sine_wave(freq,duration,sample_rate))
    freq *= 2

# Concatenate notes
sequence = np.concatenate(tones)

# Normalize to 16-bit PCM and save as WAV file (PCM = Pulse Code Modulation)
sixteen_bit = np.pow(2,15) - 1
sequence = np.int16(sequence / np.max(np.abs(sequence)) * sixteen_bit) # First normalize to range (-1,1) then to (-32767,32767)
file_name = "tones.wav"
scipy.io.wavfile.write(file_name, sample_rate, sequence)

print(f"Sound file saved as '{file_name}'")