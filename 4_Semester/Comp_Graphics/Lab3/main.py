import matplotlib.pyplot as plt
import numpy as np

def bezier_curve(p0, p1, p2, p3):
    t = np.linspace(0, 1, 100)
    x = ((1-t)**3) * p0[0] + 3 * ((1-t)**2) * t * p1[0] + 3 * (1-t) * (t**2) * p2[0] + (t**3) * p3[0]
    y = ((1-t)**3) * p0[1] + 3 * ((1-t)**2) * t * p1[1] + 3 * (1-t) * (t**2) * p2[1] + (t**3) * p3[1]
    return x, y

# Вхідні точки для кривої Безьє
p0 = (1, 1)
p1 = (2, 5)
p2 = (6, 4)
p3 = (7, 2)

x, y = bezier_curve(p0, p1, p2, p3)

# Візуалізація кривої Безьє
plt.plot(x, y, '-b', label='Bezier Curve')
plt.plot([p[0] for p in [p0, p1, p2, p3]], [p[1] for p in [p0, p1, p2, p3]], 'ro')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Cubic Bezier Curve')
plt.legend(loc='best')
plt.grid(True)
plt.show()
