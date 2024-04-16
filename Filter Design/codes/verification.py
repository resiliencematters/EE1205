import numpy as np
import matplotlib.pyplot as plt

e = 0.4
N = 4
beta = ((np.sqrt(1 + e**2) + 1)/e)**(1/4)

r1 = (beta**2 - 1)/(2*beta)
r2 = (beta**2 + 1)/(2*beta)

k = np.arange(0, 4, 1)
phi = np.pi / 2 + ((2*k+1)*np.pi)/(2*N)

s0 = (r1*np.cos(phi[0]) + 1j * r2* np.sin(phi[0]))
s1 = (r1*np.cos(phi[1]) + 1j * r2* np.sin(phi[1]))
s2 = (r1*np.cos(phi[2]) + 1j * r2* np.sin(phi[2]))
s3 = (r1*np.cos(phi[3]) + 1j * r2* np.sin(phi[3]))

print(f"s0 = {s0}")
print(f"s1 = {s1}")
print(f"s2 = {s2}")
print(f"s3 = {s3}\n")

a1 = 1
a2 = -(s0 + s1 + s2 + s3)
a3 = s0*s1 + s0*s2 + s0*s3 + s1*s2 + s1*s3 + s2*s3
a4 = -(s0*s1*s2 + s1*s0*s3 + s2*s3*s0 + s3*s1*s2)
a5 = s0*s1*s2*s3

print(f"a1 = {a1}")
print(f"a2 = {a2}")
print(f"a3 = {a3}")
print(f"a4 = {a4}")
print(f"a5 = {a5}\n")

G = a5/np.sqrt(1.16)
print(f"G = {G}\n")

def H_stable(sl):
    return G / ((sl - s0)*(sl - s1)*(sl - s2)*(sl - s3))


def H_cheb(s):
    return 1 / np.sqrt(1 + 0.16 * ((8*s**4 - 8*s**2 + 1)**2))

w = np.arange(0, 2, 0.01)

plt.plot(w, np.abs(H_stable(1j*w)), 'ro', fillstyle = 'none', label='Design')
plt.plot(w, np.abs(H_cheb(w)), label='Specification', color = 'blue')

plt.xlabel('$\\Omega$')
plt.ylabel('$|H_{a,LP}(j\\Omega|$')
plt.legend()
plt.grid()
plt.savefig('figs/verification.png')
plt.show()