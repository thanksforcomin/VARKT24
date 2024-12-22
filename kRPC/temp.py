import numpy as np
import math

x1, y1, z1 = 0, 0, 0
x2, y2, z2 = 6, 1, 1
l1, m1, n1 = 10/3, 4/3, 2
l2, m2, n2 = -4, 1, 0

v = np.array([[x2 - x1, y2 - y1, z2 - z1], [l1, m1, n1], [l2, m2, n2]])
d1 = np.array([[l1, m1], [l2, m2]])
d2 = np.array([[m1, n1], [m2, n2]])
d3 = np.array([[n1, l1], [n2, l2]])
print(np.linalg.det(v))

res = (abs(np.linalg.det(v))) / (math.sqrt(np.linalg.det(d1) ** 2 + np.linalg.det(d2)**2 + np.linalg.det(d3)**2))

print(res)
