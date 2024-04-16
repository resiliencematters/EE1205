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
# print(G)

def H(sl, G, s):
    return G / den((sl**2 + 0.897**2)/(0.142 * sl), s)

Gbp = 1/(H(1j*0.972, G, s))
print(np.abs(Gbp))

w = np.arange(-3, 3, 0.001)

plt.plot(w, np.abs(Gbp*H(1j*w, G, s)), color = 'blue')
plt.xlim(-1.25, 1.25)
plt.xlabel('$\\Omega$')
plt.ylabel('$|H_{a, BP}(j\\Omega)|$')
plt.grid()
plt.savefig('Hbp.png')
plt.show()
