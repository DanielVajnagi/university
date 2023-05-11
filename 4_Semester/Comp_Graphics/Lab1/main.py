import tkinter as tk

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
B = -2
C = 2
P = [(100, 100), (100, -100), (-100, -100), (-100, 200)]

# Створюємо вікно та площину для малювання
root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

# Малюємо координатну систему
canvas.create_line(250, 0, 250, 500)
canvas.create_line(0, 250, 500, 250)

# Малюємо пряму
x1=-300
y1 = (C - A*x1) / B
x2=300
y2 =(C - A*x2) / B
canvas.create_line(x1, y1, x2, y2)

# Малюємо полігон
for i in range(len(P)):
    xi, yi = P[i]
    x, y = xi + 250, yi + 250
    x_next, y_next = P[(i+1) % len(P)]
    x_next, y_next = x_next + 250, y_next + 250
    canvas.create_line(x, y, x_next, y_next)

# Перевіряємо, чи перетинає
if line_polygon_intersection(A, B, C, P):
    canvas.create_text(250, 20, text="Пряма перетинає полігон")
else:
    canvas.create_text(250, 20, text="Пряма НЕ перетинає полігон")

# Запускаємо головний цикл вікна
root.mainloop()
