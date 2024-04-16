import matplotlib.pyplot as plt
import numpy as np

coeff = [10.24, 0, -20.48, 0, 12.8, 0, -2.56, 0, 1.16]
roots = np.roots(coeff)
sk_roots = roots/1j
print(sk_roots)

# Extracting real and imaginary parts of roots
real_parts = np.real(sk_roots)
imaginary_parts = np.imag(sk_roots)

# Plotting
plt.figure(figsize=(8, 6))
plt.scatter(real_parts, imaginary_parts, marker='x', color='r', label='Poles')
plt.scatter([], [], marker='o', color='b', label='Zero')
plt.axhline(0, color='k', linestyle='--', linewidth=1.5)
plt.axvline(0, color='k', linestyle='--', linewidth=1.5)
plt.title('Pole-Zero Plot')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.axis('equal') 
plt.savefig('figs/pole_zero.png')
plt.show()