import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

N_t = 4
SNR_dB = [10, 20, 30]
SNR = 10**(np.array(SNR_dB) / 10)

r_list = np.linspace(0, 1, 100)
theoretical = (1 - r_list) * N_t

result = []

for snr in SNR:
    tmp = []
    for r in r_list:
        R = r * np.log2(snr)
        outage = chi2.cdf((2**R - 1) / snr, 2*N_t)
        tmp.append(-np.log2(outage) / np.log2(snr))

    result.append(tmp)

print(result)

plt.figure()
plt.plot(r_list, theoretical, label=f'DMT (Theoretical)')
for i in range(len(SNR_dB)):
    plt.plot(r_list, result[i], label=f'DMT (simulation) SNR = {SNR_dB[i]}')

plt.title('Diversity Multiplexing trasedoff')
plt.xlabel('Spatial Mutiplexing Gain r')
plt.ylabel('Diversity gain d(r)')
plt.grid(True)
plt.legend()
plt.show()