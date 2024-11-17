import numpy as np
import matplotlib.pyplot as plt

# Parameters
mean = 0  # Mean
sigma = 0.5  # Standard deviation
size = int(1e6)  # Sample size

# Generate the real and imaginary parts
real_part = np.random.normal(loc=mean, scale=sigma, size=size)  # Real part
imag_part = np.random.normal(loc=mean, scale=sigma, size=size)  # Imaginary part

# Combine to form complex numbers
complex_normal = real_part + 1j * imag_part

# First histogram for abs(complex_normal) with probability density
plt.figure()  # Create a new figure
plt.hist(abs(complex_normal), bins=30, alpha=0.7, color='blue', edgecolor='black', density=True)
plt.xlabel('Magnitude')
plt.ylabel('Probability Density')
plt.grid(True)

# Show the first figure
plt.show()

# Second histogram for 0.5 * abs(complex_normal) with probability density
plt.figure()  # Create another new figure
plt.hist(0.5 * abs(complex_normal), bins=30, alpha=0.7, color='blue', edgecolor='black', density=True)
plt.xlabel('Magnitude (Scaled by 0.5)')
plt.ylabel('Probability Density')
plt.grid(True)

# Show the second figure
plt.show()
