import matplotlib.pyplot as plt
import numpy as np
import subprocess
import sys
import os
import json


# Get data from the Javascript function
def run_node_mandelbrot(path: str, *args):
    try:
        result = subprocess.run(
            ["node", path, *args],
            capture_output=True,
            text=True,
            check=True,
            # stderr=subprocess.PIPE,
        )
    except subprocess.CalledProcessError as e:
        print("STDOUT:", e.stdout)
        print("STDERR:", e.stderr)
        raise RuntimeError(
            "command '{}' returned error (code {}):\n{}".format(
                e.cmd, e.returncode, e.stderr
            )
        )
    return json.loads(result.stdout)


# Create the plot
def mandelbrot_plot(
    x_domain: list[float], y_domain: list[float], data: np.array
):
    ax = plt.axes()
    ax.set_aspect("equal")
    graph = ax.pcolormesh(x_domain, y_domain, data, cmap="nipy_spectral")
    plt.colorbar(graph)
    plt.xlabel("Real-Axis")
    plt.ylabel("Imaginary-Axis")
    plt.show()


if __name__ == "__main__":
    # Check if user provided filename for plot
    plot_file = sys.argv[0]
    if plot_file is None:
        plot_file = "mandelbrot"

    # Call the nodejs mandelbrot package
    dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    # Determine os type for slashes
    if "/" in dir:
        mandelbrot_js_file = dir + "/mandelbrotJS/index.js"
    else:
        mandelbrot_js_file = dir + "\\mandelbrotJS\\index.js"
    output = run_node_mandelbrot(
        mandelbrot_js_file,
        "mandelbrot",
        "0",
        "0",
        "2",
        "2",
        "0.008016",
        "--max-iterations",
        "50",
    )
    mandelbrot_plot(
        output["x_domain"], output["y_domain"], np.asarray(output["iterArr"])
    )
