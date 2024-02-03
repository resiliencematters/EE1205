import matplotlib.pyplot as plt

import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))


# Open the file in read mode
with open('values.dat', 'r') as file:
    # Initialize an empty list to store the lines
    lines = []

    # Read the first line
    line = file.readline()

    # Loop through each line until the end of the file
    while line:
        # Append the line to the list
        lines.append(line.strip())  # .strip() removes the newline character at the end of each line

        # Read the next line
        line = file.readline()

# Now lines list contains all the lines from the file
print("Lines from the file:")
print(lines)



# Define the expression as a function
def expression(n):
    return (33/2)*(n)*(n+1) + (9/6)*(n)*(n+1)*(2*n+1) + 24*n

# Generate values for n
n_values = list(range(15))  # Example range from 0 to 9
y_values = [lines[n] for n in n_values]

#plt.plot(lines)
plt.stem(n_values, y_values, linefmt='b-', markerfmt='bo', basefmt='r-')
# Add labels to the axes
plt.xlabel('n')
plt.ylabel('y(n)')

# Add a title to the plot
plt.title('Stem plot of y(n)')
plt.grid(True)
# Show the plot
plt.show()


# Create stem plot

#plt.xlabel('n')
#plt.ylabel('Sn')
#plt.title('Stem Plot of Sn')
#plt.grid(True)
#plt.show()
