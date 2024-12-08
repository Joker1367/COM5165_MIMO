import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

# Parameters
N_t = 4
SNR_dB = [10, 20, 30]  # SNR values in dB
SNR = 10**(np.array(SNR_dB) / 10)  # Convert to linear scale
r_list = np.linspace(0, 1, 100)  # Spatial Multiplexing Gain
theoretical = (1 - r_list) * N_t  # Theoretical DMT

# Generate simulation results
result = []
for snr in SNR:
    tmp = []
    for r in r_list:
        R = r * np.log2(snr)
        outage = chi2.cdf((2**R - 1) / snr, 2*N_t)
        tmp.append(-np.log2(outage) / np.log2(snr))
    result.append(tmp)

# Define markers and styles for each SNR
markers = ['o', 's', '^']  # Different marker styles
colors = ['red', 'blue', 'green']  # Different line colors
linestyles = ['-', '--', '-.']  # Different line styles

# Plot
plt.figure()
plt.plot(r_list, theoretical, label='DMT (Theoretical)', color='black', linestyle='-')

for i in range(len(SNR_dB)):
    plt.plot(
        r_list, 
        result[i], 
        label=f'DMT (simulation) SNR = {SNR_dB[i]} dB', 
        color=colors[i], 
        linestyle=linestyles[i], 
        marker=markers[i], 
        markevery=10  # Display markers at intervals
    )

# Add title, labels, and legend
plt.title('Diversity Multiplexing Tradeoff')
plt.xlabel('Spatial Multiplexing Gain $r$')
plt.ylabel('Diversity Gain $d(r)$')
plt.grid(True)
plt.legend()
plt.show()
