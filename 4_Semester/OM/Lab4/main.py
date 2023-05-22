import numpy as np
import matplotlib.pyplot as plt


def phi(x_array: np.ndarray, k: int):
    return x_array ** k


def get_coef(x: np.ndarray, y: np.ndarray, n: int): #Отримати коефіцієнти інтерполяційного полінома n-го степеня
    matrix = np.zeros((n, n))
    b = np.zeros(n)

    for i in range(n):
        for j in range(n):
            matrix[i, j] = np.sum(phi(x, i) * phi(x, j))

        b[i] = np.sum(y * phi(x, i))

    return np.linalg.solve(matrix, b)[::-1]

def max_error(f_res: np.ndarray, phi_res: np.ndarray): #Максимальна похибка
    return np.max(np.abs(f_res - phi_res))


def mean_error(f_res: np.ndarray, phi_res: np.ndarray): #Середня похибка
    return np.mean(np.abs(f_res - phi_res))


def mean_squared_error(f_res: np.ndarray, phi_res: np.ndarray): #Середньоквадратична похибка
    return np.sqrt(np.mean((f_res - phi_res) ** 2))


X = np.arange(2006, 2016, dtype = np.float64)
Y = np.array([54512, 79955, 101659, 103396, 117343, 126236, 116454, 135065, 142079, 126308], dtype = np.float64)

new_x = np.linspace(X[0], X[-1], 100)
coef = get_coef(X, Y, 15)


f = np.poly1d(coef) #повертає поліноміальну функцію для заданих коефіціентів


print('Максимальна похибка: ', max_error( Y, f(X) ) )
print('Середня похибка', mean_error( Y, f(X) ) )
print('Середньоквадратична похибка', mean_squared_error( Y, f(X) ) )

plt.figure( figsize = (8, 6) )

plt.plot(new_x, f(new_x), color='black', label='Середньоквадратичне наближення')
plt.plot(X, Y, '--go',  color='blue', label='Початкова функція')

plt.legend()
plt.show()
