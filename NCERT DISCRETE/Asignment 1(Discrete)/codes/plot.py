import matplotlib.pyplot as plt

# Define the expression as a function
def expression(n):
    return (33/2)*(n)*(n+1) + (9/6)*(n)*(n+1)*(2*n+1) + 24*n

# Generate values for n
n_values = list(range(15))  # Example range from 0 to 9
y_values = [expression(n) for n in n_values]

# Create stem plot
plt.stem(n_values, y_values, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.xlabel('n')
plt.ylabel('Sn')
plt.title('Stem Plot of Sn')
plt.grid(True)
plt.show()
