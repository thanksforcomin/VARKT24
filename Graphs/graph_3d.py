import json
import math
import datetime
import matplotlib.pyplot as plt

# The file name should be added manualy before running this file
# For example: "kRPC\\Logs\\to_orbit-18-12-2024-22-38.json"
file_name = ""

ax = plt.figure().add_subplot(projection='3d')

positions = []

with open(file_name, "r") as file:
    for line in file:
        data = json.loads(line)
        positions.append(data["pos"])

# Plotting Kerbin
r = 600_000 # Kerbin radius in meters
u, v = np.mgrid[0:2 * np.pi:30j, 0:np.pi:20j]
x = r * np.cos(u) * np.sin(v)
y = r * np.sin(u) * np.sin(v)
z = r * np.cos(v)

# Plot the surface
ax.plot_surface(x, y, z)


x = [pos[0] for pos in positions]
y = [pos[1] for pos in positions]
z = [pos[2] for pos in positions]

plt.plot(x, y, z, 'r', label="trajectory of rocket")


current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M")
plt.savefig(f"graphs/{current_time}")
plt.show()
