#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import subprocess
import sys
import os
import json


# Get data from the Javascript function
def run_node_mandelbrot(cmd: list):
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print("STDOUT:", e.stdout)
        print("STDERR:", e.stderr)
        raise RuntimeError(
            "command '{}' returned error (code {}):\n{}".format(
                e.cmd, e.returncode, e.stderr
            )
        )
    print(result.stdout)
    return json.loads(result.stdout)


# Create the plot
def mandelbrot_plot(
    x_domain: list[float],
    y_domain: list[float],
    data: np.array,
    plot_name: str,
):
    # Logging for visual user feedback
    print("Creating plot...")

    ax = plt.axes()
    ax.set_aspect("equal")
    graph = ax.pcolormesh(x_domain, y_domain, data, cmap="nipy_spectral")
    plt.colorbar(graph)
    plt.xlabel("Real-Axis")
    plt.ylabel("Imaginary-Axis")
    plt.savefig(f"{plot_name}.jpg")


if __name__ == "__main__":
    # Get environment variables for data
    x_coord = os.environ.get("x_coord")
    y_coord = os.environ.get("y_coord")
    height = os.environ.get("height")
    width = os.environ.get("width")
    step = os.environ.get("step")
    # Optional args
    iters = os.environ.get("iters")
    bound = os.environ.get("bound")
    power = os.environ.get("power")

    try:
        plot_name = sys.argv[1]
    except IndexError:
        plot_name = "mandelbrot"

    dir = os.getcwd()
    # Determine os type for slashes
    if "/" in dir:
        mandelbrot_js_file = dir + "/mandelbrotJS/index.js"
    else:
        mandelbrot_js_file = dir + "\\mandelbrotJS\\index.js"
    cmd = [
        "node",
        mandelbrot_js_file,
        "mandelbrot",
        x_coord,
        y_coord,
        width,
        height,
        step,
    ]
    if iters:
        cmd.extend(["--max-iterations", iters])
    if bound:
        cmd.extend(["--bound", bound])
    if power:
        cmd.extend(["--power", power])
    output = run_node_mandelbrot(cmd)
    mandelbrot_plot(
        output["x_domain"],
        output["y_domain"],
        np.asarray(output["iterArr"]),
        plot_name,
    )
