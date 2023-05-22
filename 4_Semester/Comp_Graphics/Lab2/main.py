import math
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np

# Функція f(z)
def f(z):
    return z**5 - 1

# Похідна функції f(z)
def df(z):
    return 5*z**4

# Обчислення коренів методом Ньютона
def newton(z, max_iter=50, epsilon=1e-5):
    for i in range(max_iter):
        dz = df(z)
        if dz == 0: 
            return None
        z = z - f(z) / dz
        if abs(f(z)) < epsilon:
            return z
    return None


def map_color(z):
    root1 = 1
    root2 = complex(-0.5, math.sqrt(3)/2)
    root3 = complex(-0.5, -math.sqrt(3)/2)
    
    if abs(z - root1) < 1e-5:
        return 255, 0, 0  # Червоний колір для першого кореня
    elif abs(z - root2) < 1e-5:
        return 0, 255, 0  # Зелений колір для другого кореня
    elif abs(z - root3) < 1e-5:
        return 0, 0, 255  # Синій колір для третього кореня
    else:
        return 0, 0, 0  # Чорний колір для інших точок


# Малювання фрактала Ньютона
def draw_fractal(width, height, zoom, x_offset, y_offset):
    window = tk.Tk()
    canvas = tk.Canvas(window, width=width, height=height)
    canvas.pack()

    image = Image.new("RGB", (width, height))
    pixels = image.load()

    for x in range(width):
        for y in range(height):
            zx = 1.5 * (x - width / 2) / (0.5 * zoom * width) + x_offset
            zy = 1.0 * (y - height / 2) / (0.5 * zoom * height) + y_offset
            z = complex(zx, zy)
            root = newton(z)
            if root is not None:
                color = map_color(root)
                pixels[x, y] = color

    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, image=photo, anchor=tk.NW)
    window.mainloop()

# Виклик функції малювання фрактала
width = 800
height = 600
zoom = 1.0
x_offset = 0.0
y_offset = 0.0
draw_fractal(width, height, zoom, x_offset, y_offset)