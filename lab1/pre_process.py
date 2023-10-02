import numpy as np
import matplotlib.pyplot as plt
from fxpmath import Fxp

##Create the input signals
# Define parameters
sampling_rate = 2000 - 1  # Sampling rate in Hz (2 kHz)
duration = 1  # Duration of the signal in seconds

# Create time values from 0 to duration at the specified sampling rate
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Frequency of the first sinusoidal signal (400 Hz)
frequency1 = 400

# Generate the first sinusoidal signal
signal1 = np.sin(2 * np.pi * frequency1 * t)

# Frequency of the second sinusoidal signal (500 Hz)
frequency2 = 500

# Generate the second sinusoidal signal
signal2 = np.sin(2 * np.pi * frequency2 * t)

# Sum the two signals to create the composite signal
composite_signal = signal1 + signal2

input_file = 'in_bin.mem'
with open(input_file, 'w') as in_file:    
    for in_value in composite_signal:
        in_fixed = Fxp(in_value, True, 10, 8)
        in_bin = in_fixed.bin()
        in_file.write(in_bin + '\n')

##Convert the decimal to fixed-point binary
# Open the file in read mode
file_read = 'raw.txt'
file_write = 'coeff_bin.mem'
#format = Fxp(signed=True, n_word=9, n_frac=8)
try:
    with open(file_read, 'r') as file, open(file_write, 'w') as write_file:
        # Iterate through the lines in the file
        for line in file:
            value = float(line.strip())
            fixedPoint = Fxp(value, True, 10, 8)
            binary_representation = fixedPoint.bin()
            #Write the coeffs into the a new_txt file
            write_file.write(binary_representation + '\n')
except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
except IOError:
    print(f"An error occurred while reading the file '{file_path}'.")












