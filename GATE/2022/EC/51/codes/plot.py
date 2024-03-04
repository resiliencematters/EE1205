import matplotlib.pyplot as plt

def plot_graph_from_file(file_path):
    x_values = []
    y_values = []

    # Read data from the file
    with open(file_path, 'r') as file:
        for line in file:
            # Split each line into x and y values
            y, x = map(float, line.split())
            x_values.append(x)
            y_values.append(y)

    # Plot the graph
    plt.plot(x_values, y_values, linestyle='-')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.title('Graph from Text File')
    plt.grid(True)
    plt.show()

# Example usage:
file_path = 'output.txt'  # Update with your file path
plot_graph_from_file(file_path)
