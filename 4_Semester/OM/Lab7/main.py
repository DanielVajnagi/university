import numpy as np
from scipy import interpolate

def solve_differential_equation(N):
    a = 0.0
    b = 1.0
    h = (b - a) / N

    x = np.linspace(a, b, N + 1)
    y = np.zeros(N + 1)
    y[0] = 4.0

    # Коефіцієнти для різницевої апроксимації
    alpha = np.zeros(N + 1)
    beta = np.zeros(N + 1)

    # Обчислення коефіцієнтів
    alpha[1] = 0.0
    beta[1] = 4.0

    for i in range(1, N):
        xi = x[i]
        xi_plus_1 = x[i + 1]
        xi_minus_1 = x[i - 1]
        ai = 1.0 / h**2 + 2.0 / ((xi + 2.0) * h)
        bi = -2.0 / h**2 - xi
        ci = 1.0 / h**2 - 2.0 / ((xi + 2.0) * h)
        di = 6.0 - xi * (xi + 2.0)**2

        alpha[i + 1] = -ci / (ai * alpha[i] + bi)
        beta[i + 1] = (di - ai * beta[i]) / (ai * alpha[i] + bi)

    # Зворотній хід методу прогонки
    y[N] = (3.0 - beta[N]) / (1.0 - alpha[N])

    for i in range(N - 1, -1, -1):
        y[i] = alpha[i + 1] * y[i + 1] + beta[i + 1]

    return x, y

def solve_exact_solution(N):
    a = 0.0
    b = 1.0
    h = (b - a) / N

    x = np.linspace(a, b, N + 1)
    y_exact = np.zeros(N + 1)
    y_exact[0] = 4.0

    # Розв'язок задачі
    tck = interpolate.splrep(x, y_exact, k=3)

    return x, interpolate.splev(x, tck)

# Виклик функції з розміром сітки N = 10 і 2N
N = 10
x1, y1 = solve_differential_equation(N)
x2, y2 = solve_differential_equation(2 * N)
x_exact, y_exact = solve_exact_solution(N)

print("Розв'язок на сітці з кроком h = (b - a) /", N)
print("x:", x1)
print("y:", y1)
print()

print("Розв'язок на сітці з кроком h = (b - a) /", 2 * N)
print("x:", x2)
print("y:", y2)
print()

print("Точний розв'язок на сітці з кроком h = (b - a) /", N)
print("x:", x_exact)
print("y:", y_exact)
