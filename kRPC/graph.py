import json
import math
import datetime
import matplotlib.pyplot as plt
import numpy as np

ax = plt.figure().add_subplot(projection='3d')

# print("Введите путь до логов, по которым хотите построить график: ")
# file_name = input()
file_name = "kRPC\\Logs\\to_orbit-17-12-2024-15-44.json"

positions = []

with open(file_name, "r") as file:
    for line in file:
        data = json.loads(line)
        positions.append(data["pos"])
        # velocities.append(vec3_length(data["Velocity"]))
        # altitudes.append(data["Altitude"])

# plotting Kerbin
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
