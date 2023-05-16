import matplotlib.pyplot as plt
import numpy as np

# Вхідні дані
A = (1, 2)
B = (4, 5)
C = (3, -2)
L = (1, -1, 0)  # (a, b, c) - рівняння прямої L: ax + by + c = 0



fig, ax = plt.subplots()

# Побудова прямої L
x = np.linspace(-10, 10, 100)
y = (-L[2] - L[0] * x) / L[1]
ax.plot(x, y, 'g-', label='Пряма L')

#https://gazette.com.ua/edu/yak-znajti-tochku-simetrichnu-vidnosno-pryamoji
# Функція для знаходження відображеної точки
def reflect_point(point, line):
    x, y = point
    a, b, c = line
    factor = 2 * (a * x + b * y + c) / (a ** 2 + b ** 2)
    x_reflected = x - factor * a
    y_reflected = y - factor * b
    return x_reflected, y_reflected

# Виведення початкового трикутника
plt.grid(True)

ax.plot(A[0], A[1], 'ro')
plt.pause(2) 
ax.plot(B[0], B[1], 'ro')
plt.pause(2) 
ax.plot(C[0], C[1], 'ro')
plt.pause(2) 
ax.plot([A[0], B[0], C[0], A[0]], [A[1], B[1], C[1], A[1]], 'b-', label='Початковий трикутник')

plt.xlabel('x')
plt.ylabel('y')
plt.draw()
plt.pause(2)  # Затримка відображення 

# Виведення відображених точок
A_reflected = reflect_point(A, L)
ax.plot(A_reflected[0], A_reflected[1], 'ro')
plt.pause(2) 
B_reflected = reflect_point(B, L)
ax.plot(B_reflected[0], B_reflected[1], 'ro')
plt.pause(2) 
C_reflected = reflect_point(C, L)
ax.plot(C_reflected[0], C_reflected[1], 'ro')
plt.pause(2) 
ax.plot([A_reflected[0], B_reflected[0], C_reflected[0], A_reflected[0]],
        [A_reflected[1], B_reflected[1], C_reflected[1], A_reflected[1]], 'r-', label='Симетричний трикутник')
plt.legend()
plt.draw()
plt.pause(2)  

plt.show()
