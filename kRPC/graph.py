import json
import math
import datetime
import matplotlib.pyplot as plt


def vec3_length(vec3):
    return math.sqrt(vec3[0] ** 2 + vec3[1] ** 2 + vec3[2] ** 2)


velocities = []
altitudes = []


print("Введите путь до логов, по которым хотите построить график: ")
file_name = input()

with open(file_name, "r") as file:
    for line in file:
        data = json.loads(line)
        velocities.append(vec3_length(data["Velocity"]))
        altitudes.append(data["Altitude"])

# Построенние графика
plt.figure(figsize=(8, 6))
plt.plot(velocities, altitudes, "b")
plt.title("Длина вектора скорости и высота")
plt.xlabel("Длина вектора скорости")
plt.ylabel("Высота")


current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M")
plt.savefig(f"graphs/{current_time}")
plt.show()
