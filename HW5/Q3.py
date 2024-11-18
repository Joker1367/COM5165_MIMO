import numpy as np
from scipy.linalg import sqrtm
import matplotlib.pyplot as plt

# Parameters
rho = np.concatenate([np.arange(0, 1, 0.1)])  # rho values
Nr = 4
Nt = 4
samples = 1000

# Initialize results
avg_condition_independent = []
avg_condition_correlated = []

# Independent Rayleigh fading
for n in range(len(rho)):
    avg = 0
    for sample in range(samples):
        # Generate random H (i.i.d Rayleigh fading)
        H = np.sqrt(0.5) * (np.random.rand(Nr, Nt) + 1j * np.random.rand(Nr, Nt))
        singular_values = np.linalg.svd(H, compute_uv=False)  # Get singular values
        avg += max(singular_values) / min(singular_values)
    avg_condition_independent.append(avg / samples)

# Correlated Rayleigh fading
for n in range(len(rho)):
    avg = 0
    # Correlation matrix R
    R = np.array([
        [1, rho[n], rho[n]**2, rho[n]**3],
        [rho[n], 1, rho[n], rho[n]**2],
        [rho[n]**2, rho[n], 1, rho[n]],
        [rho[n]**3, rho[n]**2, rho[n], 1]
    ])
    R_sqrt = sqrtm(R)
    
    for sample in range(samples):
        # Generate random H
        H = np.sqrt(0.5) * (np.random.rand(Nr, Nt) + 1j * np.random.rand(Nr, Nt))
        
        correlated_H = np.dot(R_sqrt, np.dot(H, R_sqrt))  # Apply correlation
        singular_values = np.linalg.svd(correlated_H, compute_uv=False)
        avg += max(singular_values) / min(singular_values)
    avg_condition_correlated.append(avg / samples)

# Plot results
plt.figure()
plt.plot(rho, avg_condition_independent, label="i.i.d Rayleigh fading")
plt.plot(rho, avg_condition_correlated, label="Correlated Rayleigh fading")
plt.xlabel(r"$\rho$")
plt.ylabel("Condition number")
plt.legend()
plt.grid()
plt.show()
