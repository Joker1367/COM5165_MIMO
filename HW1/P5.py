import numpy as np
import matplotlib.pyplot as plt
from scipy.special import iv  # Bessel function I_0
from scipy.stats import rice

# Step 1: Generate random samples from the Rician distribution
v = 2.0  # LoS power is v^2 = 4
sigma = 1.0  #  nLoS power is 2*sigma^2 = 1
K = v**2 / 2*sigma**2

num_samples = 100000

# Generate Rician-distributed random samples using scipy.stats.rice
samples = rice.rvs(v/sigma, scale=1.0, size=num_samples)

# Step 2: Plot the histogram of the simulated samples
plt.hist(samples, bins=50, density=True, alpha=0.6, color='g', label="samples from rician distribution")

# Step 3: Plot the theoretical PDF fA(a)
a = np.linspace(0, 10, 1000)  # Define the range for 'a'
pdf_theoretical = (a / sigma**2) * np.exp(-(a**2 + v**2) / (2 * sigma**2)) * iv(0, (a * v) / sigma**2)

plt.plot(a, pdf_theoretical, 'r-', lw=2, label="$f_A(a)$")
plt.xlabel('a')
plt.ylabel('Density')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
