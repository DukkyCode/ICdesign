import numpy as np
import matplotlib.pyplot as plt

def binary_to_decimal(binary_value):
    # Ensure that the binary value has 20 bits
    if len(binary_value) != 20:
        raise ValueError("Binary value must have exactly 20 bits")

    # Determine the sign bit (the most significant bit)
    sign_bit = int(binary_value[0])  # 0 for positive, 1 for negative

    # Separate the binary value into integer and fractional parts
    integer_part = binary_value[1:4]  # Next 3 bits are the integer part
    fractional_part = binary_value[4:]  # The rest is the fractional part

    # Convert the integer and fractional parts to decimal
    integer_decimal = int(integer_part, 2)
    fractional_decimal = int(fractional_part, 2) / 2**16  # Scale the fractional part

    # Calculate the final S3.16 value, accounting for the sign bit
    if sign_bit == 1:
        integer_decimal = -(2**3 - integer_decimal)  # 3 bits for the integer part
        
    s3_16_value = integer_decimal + fractional_decimal

    return s3_16_value

# Define parameters
sampling_rate = 2000  # Sampling rate in Hz (2 kHz)
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

# Get the output signal from your data (replace with your actual data)
output_signal = []

with open("sim.out", "r") as file:
    for line in file:
        value = line.strip()
        decimal_value = binary_to_decimal(value)
        output_signal.append(decimal_value)

# Ensure that output_signal has the same length as t
if len(output_signal) != len(t):
    # You can interpolate output_signal to match the length of t if needed
    output_signal = np.interp(t, np.linspace(0, duration, len(output_signal)), output_signal)

# Create subplots
plt.figure(figsize=(10, 6))

# Plot signal1 in blue
plt.plot(t, signal1, label='400Hz Signal', color='blue')

# Plot signal2 in red
plt.plot(t, signal2, label='500Hz Signal', color='red')

# Plot output_signal in green
plt.plot(t, output_signal, label='Output Signal', color='green')

# Add labels and legend
plt.title('Signals Comparison')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()

plt.xlim(0.02, 0.03)
#plt.ylim(-0.5, 0.5)
# Adjust layout and display the plots
plt.tight_layout()
plt.show()

