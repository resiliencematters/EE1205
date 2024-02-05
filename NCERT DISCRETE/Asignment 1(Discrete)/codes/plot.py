import matplotlib.pyplot as plt

import os

cwd = os.getcwd()  
files = os.listdir(cwd) 
print("Files in %r: %s" % (cwd, files))


with open('values.dat', 'r') as file:

    lines = []

    
    line = file.readline()

    
with open('values.dat', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

n_values = list(range(15)) 
y_values = [lines[n] for n in n_values]


plt.stem(n_values, y_values, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.xlabel('n')
plt.ylabel('y(n)')


plt.title('Stem plot of y(n)')
plt.grid(True)
plt.show()



