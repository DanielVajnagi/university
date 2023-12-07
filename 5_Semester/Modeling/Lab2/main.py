import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def fi1(θ):
  return 12 * np.cos(θ) - 12 * np.cos(2 * θ)

def fi2(θ):
  return 12 * np.sin(θ) - 12 * np.sin(2 * θ)

def fi3(θ):
  return 5 * np.cos(2*θ) + 8 * np.cos(θ) + 1

def fi4(θ):
  return 5 * np.sin(2*θ) + 8 * np.sin(θ)

def u(θ):
  return (fi1(θ)*fi3(θ) + fi2(θ)*fi4(θ)) / ((fi3(θ)*fi3(θ)) + (fi4(θ)*fi4(θ)))

def v(θ):
  return (fi2(θ)*fi3(θ) - fi1(θ)*fi4(θ)) / ((fi3(θ)*fi3(θ)) + (fi4(θ)*fi4(θ)))


# Створюємо масив точок θ в діапазоні [0, 2*pi] з кроком pi/100
θ = np.arange(0, 2 * np.pi, np.pi/100)

# Обчислюємо значення функцій v(θ) та u(θ) для кожного θ
v_values = v(θ)
u_values = u(θ)
table = pd.DataFrame({'θ': θ, 'v(θ)': v_values, 'u(θ)': u_values})

# Виведення таблиці


print(table.iloc[0:200])
# Збереження таблиці у файл CSV
table.to_csv('output.csv', index=False)


# Побудова графіка
plt.figure(figsize=(4, 3))
plt.plot(u_values, v_values)
plt.xlabel('u(θ)')
plt.ylabel('v(θ)')
plt.title('Графік')
plt.grid(True)


p = 1/2

G = (12*p - 12*p*p) / (5*p*p + 8*p - 1 )

# Вивід точки (G, 0)
plt.scatter(G, 0, color='red')


# Відображення графіка
plt.show()
