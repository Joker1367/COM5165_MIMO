import numpy as np
import matplotlib.pyplot as plt

def generate_capacity(M, N, SNR_dB, num_samples):
    SNR = 10**(SNR_dB / 10)
    capacities = []
    
    for _ in range(num_samples):
        H = (np.random.randn(M, N) + 1j * np.random.randn(M, N)) / np.sqrt(2)  # Rayleigh channel
        HH_dagger = np.dot(H, H.conj().T)  # H * H^H
        capacity = np.log2(np.linalg.det(np.eye(M) + (SNR / N) * HH_dagger).real)
        capacities.append(capacity)
    
    return np.sort(capacities)

# Parameters
M1, N1 = 2, 2
M2, N2 = 4, 4
SNR_dB = 10
num_samples = 10000

# Simulate
capacities_2x2 = generate_capacity(M1, N1, SNR_dB, num_samples)
capacities_4x4 = generate_capacity(M2, N2, SNR_dB, num_samples)

# Plot CDF
plt.figure()
plt.plot(capacities_2x2, np.linspace(0, 1, num_samples), label="2x2 MIMO")
plt.plot(capacities_4x4, np.linspace(0, 1, num_samples), label="4x4 MIMO")
plt.xlabel("Capacity (bits/s/Hz)")
plt.ylabel("CDF")
plt.title("CDF of MIMO Channel Capacity")
plt.legend()
plt.grid()
plt.show()
