import numpy as np
import matplotlib.pyplot as plt

# Коефіцієнти моделі Лоренца
σ = 10
r = 28
b = 8/3

# Початкові умови
x0 = 3.05
y0 = 1.58
z0 = 15.62

# Крок сітки
h = 0.01

# Кількість кроків
n_steps = int(50 / h)

x = np.zeros(n_steps)
y = np.zeros(n_steps)
z = np.zeros(n_steps)

x[0] = x0
y[0] = y0
z[0] = z0

# Обчислення за методом Рунге–Кутти другого порядку
for i in range(1, n_steps):
    # Обчислення кроку
    k1x = h * σ * (y[i-1] - x[i-1])
    k1y = h * (x[i-1] * (r - z[i-1]) - y[i-1])
    k1z = h * (x[i-1] * y[i-1] - b * z[i-1])

    k2x = h * σ * (y[i-1] - (x[i-1] + 0.5 * k1x))
    k2y = h * ((x[i-1] + 0.5 * k1x) * (r - (z[i-1] + 0.5 * k1z)) - (y[i-1] + 0.5 * k1y))
    k2z = h * ((x[i-1] + 0.5 * k1x) * (y[i-1] + 0.5 * k1y) - b * (z[i-1] + 0.5 * k1z))

    # Обчислення нових значень
    x[i] = x[i-1] + k2x
    y[i] = y[i-1] + k2y
    z[i] = z[i-1] + k2z

# Побудова траєкторії в фазовому просторі
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
