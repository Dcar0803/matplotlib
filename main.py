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

def live_graph():

    """Generates and plots one random point per second, continuously updating the graph.
    
      Only the 10 most recent points are displayed on the graph.
    """
    plt.ion() #Interactive mode on
    fig, ax = plt.subplots()

    x_data, y_data = [],[]

    for i in range(100):
        x_data.append(i)
        y_data.append(np.random.randon()) #Generates random y axis values
        
        if  len(x_data)> 10:
            x_data.pop(0) 
            y_data.pop(0)
    
        ax.clear()
        ax.plot(x_data, y_data, 'o-', label='Live Data Points')
        ax.set_title('Live Graph')
        ax.set_xlabel('Time (s)')
        ax.set_ylabel('Value')
        ax.legend()
        
        # Update the graph
        plt.pause(1) 

    plt.ioff()
    plt.show()
    