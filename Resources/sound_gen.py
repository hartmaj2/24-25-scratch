import numpy as np
from scipy.io.wavfile import write

# Function to generate a sine wave
def generate_sine_wave(freq, duration, sample_rate=44100, amplitude=0.5):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = amplitude * np.sin(2 * np.pi * freq * t)
    return wave

# Define notes (frequencies in Hz)
notes = {
    'C': 261.63 * 0.5,  # Frequency of C4
    'E': 329.63 * 0.5,  # Frequency of E4
    'G': 392.00 * 0.5,  # Frequency of G4
}

# Generate sound for each note
sample_rate = 44100  # Samples per second
c_wave = generate_sine_wave(notes['C'], 0.33, sample_rate)
e_wave = generate_sine_wave(notes['E'], 0.33, sample_rate)
g_wave = generate_sine_wave(notes['G'], 0.34, sample_rate)

# Concatenate notes
sequence = np.concatenate([c_wave, e_wave, g_wave])

# Normalize to 16-bit PCM and save as WAV file
sixteen_bit = np.pow(2,15) - 1
sequence = np.int16(sequence / np.max(np.abs(sequence)) * sixteen_bit)
write("c_major_sequence_alternative.wav", sample_rate, sequence)

print("C major sequence saved as 'c_major_sequence_alternative.wav'")
