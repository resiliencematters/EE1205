import numpy as np
import matplotlib.pyplot as plt

# Define the range of omega values
omega = np.linspace(0, 100000, 1000)  # Adjust the range as needed

# Compute the magnitude in decibels
magnitude_dB = 20 * np.log10(np.abs(1 + 1j * omega * 0.0001))

# Plot the magnitude response
plt.figure(figsize=(10, 6))
plt.plot(omega, magnitude_dB, color='red')
plt.xlabel('ω')
plt.ylabel('H(ω)(dB)')
plt.grid(True)
plt.show()
