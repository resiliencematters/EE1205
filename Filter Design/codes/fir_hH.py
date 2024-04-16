import numpy as np
import matplotlib.pyplot as plt

#Filter parameters
r = 11059       
sigma = 16
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

omega_l = (omega_p1 - omega_p2)/2
delta_omega = 2*np.pi*0.3/Fs

A = -20*np.log10(delta)
# N = np.ceil((A - 8)/(4.57 * delta_omega))
N = 100

def w(n, N):
    return np.where(np.logical_and(-N <= n, n <= N), 1, 0)
    
def h_lp(n, N):
    return  np.where(n!=0, np.sin(n * omega_l) * w(n, N)/ (n * np.pi), omega_l/np.pi)

n = np.arange(-N, N+1)
n1 = np.arange(-120, 121, 2) #For better plot of h_val


plt.stem(n1, h_lp(n1, N), linefmt='b', markerfmt='bo', basefmt='r')
plt.xlim(-120, 120)
plt.xlabel('n')
plt.ylabel('$h_{lp}(n)$')
plt.grid()
plt.tight_layout()
plt.savefig('fir_hlp.png')
plt.show()
plt.clf()

h_val = h_lp(n, N)
omega = np.linspace(-np.pi/2, np.pi/2, 500)
H = np.abs(np.polyval(h_val, np.exp(-1j*omega)))

plt.plot(omega/np.pi, np.abs(H), color = 'blue')
plt.xlim(-0.5, 0.5)
plt.xlabel('$\\frac{\\omega}{\\pi}$')
plt.ylabel('$|H_{lp}(j\\omega)|$')
plt.grid()
plt.savefig('firHLP.png')
plt.show()