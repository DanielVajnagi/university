import matplotlib.pyplot as plt
import numpy as np
import sympy as sym

A = (-2, -4)
B = (5, 4)
C = (5, -1)
L = (2, -1, 2)  # (a, b, c) - рівняння прямої L: ax + by + c = 0
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)  
ax.set_ylim(-10, 10)
# Побудова прямої L
x = np.linspace(-10, 10, 100)
y = (-L[2] - L[0] * x) / L[1]
ax.plot(x, y, 'g-', label='Пряма L')

def reflect_point(point,line):
    a, b, c = line
    x0, y0 = point    
    denominator = a**2 + b**2    
    symmetric_x = x0 - 2 * (a * x0 + b * y0 + c) * a / denominator
    symmetric_y = y0 - 2 * (a * x0 + b * y0 + c) * b / denominator
    
    return symmetric_x, symmetric_y

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
plt.pause(2)

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
