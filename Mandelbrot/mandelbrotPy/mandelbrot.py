import matplotlib.pyplot as plt
import subprocess
import sys


# Get data from the Javascript function
def run_node_mandelbrot(path: str):
    result = subprocess.run(
        ["node", path], capture_output=True, text=True, check=True
    )
    return result.stdout


if __name__ == "__main__":
    # Check if user provided filename for plot
    plot_file = sys.argv[0]
    if plot_file is None:
        plot_file = "mandelbrot"
