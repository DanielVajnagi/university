import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from tkinter import simpledialog
from tkinter import colorchooser

class Astroid:
    def __init__(self):
        self.x_coords = None
        self.y_coords = None
        self.color = None
        plt.figure(figsize=(5, 5))
    def calculate_coords(self, a):
        t = np.linspace(0, 2*np.pi, 1000)

        self.x_coords = a * np.cos(t)**3
        self.y_coords = a * np.sin(t)**3
    def build(self):
            plt.clf()
            plt.plot(self.x_coords, self.y_coords, color=self.color)
            plt.title("Астроїда")
            plt.xlabel("x")
            plt.ylabel("y")
            plt.axis("equal")
            plt.grid(True)
            plt.show()  
    def __add__(self, angle):
        theta = np.radians(-angle)

        x_new = self.x_coords * np.cos(theta) - self.y_coords * np.sin(theta)
        y_new = self.x_coords * np.sin(theta) + self.y_coords * np.cos(theta)

        self.x_coords = x_new
        self.y_coords = y_new

    def __mul__(self, factor):
        self.x_coords *= factor
        self.y_coords *= factor
          

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Графічна фігура")
        self.geometry("400x400")

        self.astroid = Astroid()

        self.button_astroid = tk.Button(self, text="Побудувати астроїду", command=self.plot_astroid, font=("Arial", 14))
        self.button_astroid.pack(fill=tk.BOTH, padx=20, pady=10)

        self.button_code2 = tk.Button(self, text="Повернути", command=self.rotate, font=("Arial", 14))
        self.button_code2.pack(fill=tk.BOTH, padx=20, pady=10)

        self.button_code3 = tk.Button(self, text="Масштабувати", command=self.resize, font=("Arial", 14))
        self.button_code3.pack(fill=tk.BOTH, padx=20, pady=10)

        self.animation = tk.Button(self, text="Анімація", command=self.resize, font=("Arial", 14))
        self.button_code3.pack(fill=tk.BOTH, padx=20, pady=10)

    def plot_astroid(self):
        dialog = simpledialog.askfloat("Масштабний параметр", "Введіть масштабний параметр астроїди:")
        if dialog is not None:
            self.astroid.calculate_coords(dialog)

            color_dialog = colorchooser.askcolor(title="Виберіть колір астроїди")
            if color_dialog[1] is not None:
                self.astroid.color = color_dialog[1]
                self.astroid.build()

    def rotate(self):
        change = simpledialog.askfloat("Поворот", "Введіть градус повороту астроїди:")
        if change is not None:
            self.astroid+change
            self.astroid.build()


    def resize(self):
        change = simpledialog.askfloat("Маштабування", "Введіть коефіцієнт маштабування астроїди:")
        if change is not None:
            self.astroid*change
            self.astroid.build()

            

if __name__ == "__main__":
    app = Application()
    app.mainloop()
