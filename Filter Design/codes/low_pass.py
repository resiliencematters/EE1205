import numpy as np
import matplotlib.pyplot as plt

#Filter parameters
r = 11009
sigma = 11
j = (r - 11000) % sigma

#Sampling freqency (kHz)
Fs = 48

# Constant used to get the normalized digital freqencies
const = 2*np.pi/Fs

# The permissible filter amplitude deviation from unity
delta = 0.15

#Bandpass filter specifications (kHz)

# %Passband F_p2 < F_p1
F_p1 = 4 + 0.6*(j + 2)
F_p2 = 4 + 0.6*j

#Stopband F_s2 < F_p21; F_p1 < F_s1
F_s1 = F_p1 + 0.3
F_s2 = F_p2 - 0.3

#Normalized digital filter specifications (radians/sec)
omega_p1 = const*F_p1
omega_p2 = const*F_p2

omega_s1 = const*F_s1
omega_s2 = const*F_s2

#The analog bandpass filter (design) frequencies 
#obtained using the bilinear transformation
Omega_p1 = np.tan(omega_p1/2)
Omega_p2 = np.tan(omega_p2/2)

Omega_s1 = np.tan(omega_s1/2)
Omega_s2 = np.tan(omega_s2/2)

#The analog bandpass-lowpass (design) transformation
#parameters
Omega_0 = np.sqrt(Omega_p1*Omega_p2)
B = Omega_p1 - Omega_p2

#The lowpass Chebyschev approximation stopband frequency
Omega_Ls = min(abs((Omega_s1**2 - Omega_0**2)/(B*Omega_s1)),abs((Omega_s2**2 - Omega_0**2)/(B*Omega_s2)))


#The lowpass Chebyschev approximation
D1 = 1/((1-delta)**2) - 1
D2 = 1/(delta**2) - 1

#Estimated lowpass Chebyschev filter order
N = np.ceil(np.arccosh(np.sqrt(D2/D1))/np.arccosh(Omega_Ls))

#Range Of the Chebyschev filter parameter epsilon
epsilon1 = np.sqrt(D2)/np.cosh(N*np.arccosh(Omega_Ls))
epsilon2 = np.sqrt(D1)

N = np.ceil(np.arccosh(np.sqrt(D2/D1))/np.arccosh(Omega_Ls))

#PLOTS OF THE LOWPASS CHEBYSCHEV FILTER OF ORDER N AND
N = 4
epsilon = np.arange(0.3, 0.61, 0.05)
Omega = np.arange(0, 3.01, 0.01)

for e in epsilon:
        H = 1/np.sqrt(1 + e**2 * (8 * Omega**4 - 8 * Omega**2 + 1)**2)
        plt.plot(Omega, H, label=f'$\\epsilon$ = {np.round(e, 2)}')

passband = (Omega >= 0) & (Omega <= 1)
transband = (Omega >= 1) & (Omega <= 2)
stopband = (Omega >= 2)
plt.fill_between(Omega, -1, 2, where=passband, color=(0, 1, 0), alpha=0.5, label='Passband')
plt.fill_between(Omega, -1, 2, where=transband, color=(1, 1, 0), alpha=0.5, label='Transition Band')
plt.fill_between(Omega, -1, 2, where=stopband, color=(1, 0, 0), alpha=0.25, label='Stopband')
plt.axhline(0, color='k', linestyle='-', linewidth=1.5)
plt.axvline(0, color='k', linestyle='-', linewidth=1.5)
plt.xlabel('$\\Omega$')
plt.ylabel('$|H_{a,LP}(j\\Omega)|$')
plt.ylim(-0.1, 1.1)
plt.xlim(0, 3)
plt.legend()
plt.grid(True)
plt.savefig('figs/low_pass.png')
plt.show()