import matplotlib.pyplot as plt

def line_polygon_intersection(A, B, C, P):
    n = len(P)
    last = n-1
    intersect = False
    
    for i in range(n):
        xi, yi = P[i]
        xj, yj = P[(i+1) % n]
        Ai = A*xi + B*yi + C
        Aj = A*xj + B*yj + C
        
        if Ai * Aj <= 0:
            intersect = True
            break
        elif Ai == 0 or Aj == 0:
            intersect = True
            break
    
    return intersect

# Задаємо коефіцієнти рівняння прямої та координати вершин полігону
A = 1
B = 2
C = 5
P = [(1, 1), (3, 1), (3, 2),(4,3), (1, 2)]

# Перевіряємо, чи перетинає пряма полігон та виводимо результат
if line_polygon_intersection(A, B, C, P):
    print("Пряма перетинає полігон")
else:
    print("Пряма не перетинає полігон")

# Візуалізуємо полігон та пряму
fig, ax = plt.subplots()
ax.set_aspect('equal')

# Побудова полігону
x, y = zip(*P)
ax.fill(x, y, alpha=0.3)

# Побудова прямої
x_min, x_max = ax.get_xlim()
y_min, y_max = ax.get_ylim()
if B != 0:
    x1 = x_min
    y1 = (-A*x1 - C)/B
    x2 = x_max
    y2 = (-A*x2 - C)/B
else:
    x1 = -C/A
    y1 = y_min
    x2 = -C/A
    y2 = y_max
if line_polygon_intersection(A, B, C, P):        
    ax.plot([x1, x2], [y1, y2], color='red')
else:
    ax.plot([x1, x2], [y1, y2], color='green')
# Відображення графіки
plt.show()
