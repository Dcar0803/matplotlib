import numpy as np
import matplotlib.pyplot as plt
from main import plot_normal_distribution, plot_line, live_graph

def test_plot_normal_distribution():

    try:
        plot_normal_distribution()
        print("Test for normal distribution passed")
    except Exception as e:
        print(f"Test for plot_normal_distribution failed: {e}")


def test_plot_line():
    try:
        plot_line(y_intercept=1, slope=2, x_min=-10, x_max=10)
        print("Test for plot_line passed.")
    except Exception as e:
        print(f"Test for plot_line failed: {e}")


def test_live_graph():

    try:
        live_graph()
        print("Test for live graph passed.")
    except Exception as e: 
        print(f"Test for live_graph failed: {e}")
    
