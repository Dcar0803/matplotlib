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
    
def plot_line(y_intercept, slope, x_min, x_max):

    """Plots a line based on the formula y = mx + b in a specified range.
    
    Parameters:
        y_intercept (float): The y-intercept of the line.
        slope (float): The slope of the line.
        x_min (float): The starting x value for the plot.
        x_max (float): The ending x value for the plot.
        
    The function plots the line within the range defined by x_min and x_max.
    """
    
    x = np.linspace(x_min, x_max, 400)
    y = (slope * x) + y_intercept
    plt.plot(x, y, label=f'y = {slope}x + {y_intercept}')
    plt.title("Line Plot")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(color = 'green')
    plt.show()