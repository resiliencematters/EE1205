import numpy as np
import matplotlib.pyplot as plt

e = 0.4
N = 4
beta = ((np.sqrt(1 + e**2) + 1)/e)**(1/4)

r1 = (beta**2 - 1)/(2*beta)
r2 = (beta**2 + 1)/(2*beta)

k = np.arange(0, 4, 1)
phi = np.pi / 2 + ((2*k+1)*np.pi)/(2*N)

s = (r1 * np.cos(phi) + 1j * r2 * np.sin(phi))

def den(sl, s):
    return (sl - s[0])*(sl - s[1])*(sl - s[2])*(sl - s[3])

G = np.abs(den(1j, s))/np.sqrt(1 + e**2)

def H(sl, G, s):
    return G / den((sl**2 + 0.897**2)/(0.142 * sl), s)

def H_digital(sl, G, s):
    k = (sl - 1)/(sl + 1)
    return G / den((k**2 + 0.897**2)/(0.142 * k), s)

Gbp = 1/(H(1j*0.972, G, s))

w = np.arange(-3*np.pi, 3*np.pi, 0.001)

plt.plot(w/np.pi, np.abs(Gbp*H_digital((1 + 1j*w)/(1 - 1j*w), G, s)), color = 'blue')
plt.xlim(-0.5, 0.5)
plt.xlabel("$\\frac{\\omega}{\\pi}$")
plt.ylabel('$|H_{d, BP}(\\omega)|$')
plt.grid()
plt.savefig('H_dbp.png')
plt.show()