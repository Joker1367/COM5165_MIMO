from scipy.stats import expon, chi2
from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt
import math

epsilon = 0.01
SNR = np.linspace(start = -10, stop = 40, num = 11, endpoint = True)
X = np.power(10, np.linspace(start = -10, stop = 40, num = 11, endpoint = True) / 10)

markers = ['o', 's', 'D', 'X', '^']
sample_size = int(1e6)

for L in range(1, 6):
    C_AWGN = np.log2(1 + L * X)

    df = 2 * L

    def equation(x):
        return chi2.cdf(x, df) - epsilon
    
    initial_guess = 0
    solution = fsolve(equation, initial_guess)

    C_epsilon_theoretical = np.log2(1 + max(solution)*X)
    plt.plot(SNR, C_epsilon_theoretical / C_AWGN, label = f'L = {L} (Theoretical)')

    chi2_samples = chi2.rvs(df, size = sample_size)
    chi2_samples.sort()
    C_epsilon_simulation = np.log2(1 + chi2_samples[int(sample_size * epsilon) - 1]*X)
    plt.plot(SNR, C_epsilon_simulation / C_AWGN , label = f'L = {L} (Simulated)', marker=markers[L-1], linestyle='None')


plt.title(r'$\epsilon$-outage capacity')
plt.xlabel('SNR (dB)')
plt.ylabel(r'$\frac{C_{\epsilon}}{C_{awgn}}$')
plt.legend()
plt.show()