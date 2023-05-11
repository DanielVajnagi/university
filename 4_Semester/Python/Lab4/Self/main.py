import tkinter as tk
import tkinter.messagebox as messagebox
import numpy as np
import matplotlib.pyplot as plt
# Графіки
def plot_sin():
    plt.clf()
    x = np.linspace(-10, 10, 500)
    y = np.sin(x)
    plt.plot(x, y, color='black')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('y = sin(x)')
    plt.show()


def plot_cos():
    plt.clf()
    x = np.linspace(-10, 10, 500)
    y = np.cos(x)
    plt.plot(x, y, color='red')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('y = cos(x)')
    plt.show()
    

# Вікно та меню
window = tk.Tk()
window.title('Графіки функцій')
menu = tk.Menu(window)
window.config(menu=menu)

# Підменю
sub_menu = tk.Menu(menu)
menu.add_cascade(label='Меню', menu=sub_menu)
sub_menu.add_command(label='Графік sin(x)', command=plot_sin)
sub_menu.add_command(label='Графік cos(x)', command=plot_cos)
sub_menu.add_separator()
sub_menu.add_command(label='Інформація про програму', command=lambda: tk.messagebox.showinfo('Інформація',
                                                                                             'Ця програма малює графіки функцій sin(x) та cos(x) на відрізку [-10, 10] у декартовій системі координат. \n Created by @daniel_vajnagi'))
sub_menu.add_command(label='Вихід', command=window.quit)

window.mainloop()
