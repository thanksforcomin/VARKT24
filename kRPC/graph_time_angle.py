import json
import math
import datetime
import matplotlib.pyplot as plt
import numpy as np

# print("Введите путь до логов, по которым хотите построить график: ")
# file_name = input()
file_name = "kRPC\\Logs\\to_orbit-18-12-2024-22-38.json"

positions = []
dots_ksp = []
dots_math = []

with open(file_name, "r") as file:
    for line in file:
        data = json.loads(line)
        dots_ksp.append((data["time"], data["angle"]))

with open("angle.json", "r") as file:
    heights_math = json.load(file)

dots_math = [(float(k), v) for k, v in heights_math.items()]

plt.plot(
    [data[0] for data in dots_ksp],
    [data[1] for data in dots_ksp],
    "b",
)
plt.plot(
    [data[0] for data in dots_math],
    [data[1] for data in dots_math],
    "r",
)

plt.legend(("Полёт в ксп", "Мат. Модель"))

plt.xlabel("Время (с.)")
plt.ylabel("Угол (градусы)")
plt.title("Зависимость высоты от времени")
plt.xticks([10 * i for i in range(33)])
plt.yticks([3 * i for i in range(int(31) + 2)])
plt.grid(color="grey", linestyle="-")

current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M")
plt.savefig(f"graphs/{current_time}")
plt.show()
