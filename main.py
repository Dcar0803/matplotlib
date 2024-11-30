import matplotlib.pyplot as plt
import numpy as np

def plot_normal_distribution():

    """Plots 200 points sampled from a standard normal distribution.
    
    The points are displayed as a scatter plot where the x-axis is the index of the point,
    and the y-axis is the sampled value.
    """
    data = np.random.normal(size=200)
    plt.plot(data, 'o')
    plt.title("Standard Normal Distribution")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.grid(color = 'green')
    plt.show()
    