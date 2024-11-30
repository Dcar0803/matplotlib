import numpy as np
import matplotlib.pyplot as plt
from main import plot_normal_distribution

def test_plot_normal_distribution():

    try:
        plot_normal_distribution()
        print("Test for normal distribution passed")
    except Exception as e:
        print(f"Test for plot_normal_distribution failed: {e}")