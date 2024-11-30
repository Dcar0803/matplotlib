import matplotlib.pyplot as plt
import numpy as np

def plot_normal_distribution():
    data = np.random.normal(size=200)
    plt.plot(data, 'o')
    plt.title("Standard Normal Distribution")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.grid(color = 'green')
    plt.show()
    return