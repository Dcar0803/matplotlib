import numpy as np
import matplotlib.pyplot as plt

def test_plot_normal_distribution():

    try:
        plot_normal_distribution()
        print("Test for normal distribution passed")
    except:
        print(f"Test for plot_normal_distribution failed: {e}")