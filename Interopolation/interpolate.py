import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata

# Provided data
points = [
    [121.39, 13.51],
    [126.19, 12.02],
    [130.27, 13.11],
    [127.42, 10.09],
    [126.14, 15.33],
    [125.96, 14],
    [123.15, 10.88],
    [130.5, 11.18],
    [129.08, 15.78],
    [122.74, 7.137],
]
values = [1.494, 1.934, 2.148, 9.155, 2.221, 8.1, 2.039, 1.196, 3.729, 7.137]

# Create the rows and columns, then grid them
y_range = np.linspace(10.0, 16.0, 50)
x_range = np.linspace(121.0, 131.0, 70)
grid_x, grid_y = np.meshgrid(x_range, y_range)

# Scipy's griddata interpolation
new_vals = griddata(points, values, (grid_x, grid_y), method="nearest")

# Plot interpolated data
ax = plt.axes()
graph = ax.pcolormesh(x_range, y_range, new_vals, cmap="nipy_spectral")
plt.colorbar(graph)
plt.grid(True)
plt.show()
