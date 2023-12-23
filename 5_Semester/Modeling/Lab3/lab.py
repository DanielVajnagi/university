import numpy as np
import pandas as pd

epsilon = 0.001
lbd1, lbd2 = -1001, -1
y10, y20 = 1, 0
t0, t1, T = 0.0, 5 / max(abs(lbd1), abs(lbd2)), 1.0
n = 25
h_min = t1 / n
r = t1 / 3
h_max = 5* h_min
y1=y10
y2=y20
t_values = [t0]
x_values = [y1]
y_values = [y2]

# Тестова задача.
def f(y1_f, y2_f, t_f):
    dx = -501 * (y1_f + t_f) + 500 * (y2_f + t_f)
    dy = 500 * (y1_f + t_f) - 501 * (y2_f + t_f)
    return dx, dy

# Точний розв'язок.
def y1_y2_correct(t_values):
    x,y=[],[]
    for t in t_values:
        x.append(0.5 * (y10 - y20) * np.exp(-1001 * t) + 0.5 * (y10 + y20) * np.exp(t))
        y.append(-0.5 * (y10 - y20) * np.exp(-1001 * t) + 0.5 * (y10 + y20) * np.exp(t))
    return (x,y)

t=t0+h_min
while t<t1:
    t_values.append(t)
    t+=h_min
t+=h_max
while t<=T:
    t_values.append(t)
    t+=h_max


def rk3_x(t, x, y, n,h):
    def k1(n):
        return f(x[n], y[n], t[n])[0]

    def k2(n):
        return f(x[n], y[n] + (h / 3) * k1(n), t[n] + h / 3)[0]

    def k3(n):
        return f(x[n], y[n] + (h * 2 / 3) * k2(n), t[n] + h * 2 / 3)[0]

    return x[n - 1] + (h / 4) * (k1(n - 1) + 3 * k3(n - 1))


def rk3_y(t, x, y, n,h):
    def k1(n):
        return f(x[n], y[n], t[n])[1]

    def k2(n):
        return f(x[n] + (h / 3) * k1(n), y[n], t[n] + h / 3)[1]

    def k3(n):
        return f(x[n] + (h * 2 / 3) * k2(n), y[n], t[n] + h * 2 / 3)[1]

    return y[n - 1] + (h / 4) * (k1(n - 1) + 3 * k3(n - 1))


x_values.append(rk3_x(t_values, x_values, y_values, 1,h_min))
y_values.append(rk3_y(t_values, x_values, y_values, 1,h_min))


def na3_x(t, x, y, n,h):
    x_n0 = x[n - 1] + f(x[n - 1], y[n - 1], t[n - 1])[0]
    y_n0 = y[n - 1] + f(x[n - 1], y[n - 1], t[n - 1])[1]

    while True:
        x_n1 = x[n - 1] + (h / 12) * (
                5 * f(x_n0, y_n0, t[n])[0] + 8 * f(x[n - 1], y[n - 1], t[n - 1])[0] - f(x[n - 2], y[n - 2], t[n - 2])[0])
        y_n1 = y[n - 1] + (h / 12) * (
                5 * f(x_n0, y_n0, t[n])[1] + 8 * f(x[n - 1], y[n - 1], t[n - 1])[1] - f(x[n - 2], y[n - 2], t[n - 2])[1])
        if (abs(x_n1 - x_n0) + abs(y_n1 - y_n0)) < epsilon:
            return [x_n1, y_n1]
        else:
            x_n0 = x_n1
            y_n0 = y_n1

i=2
while t_values[i]<=t1:
    xy_i = na3_x(t_values, x_values, y_values, i,h_min)
    x_values.append(xy_i[0])
    y_values.append(xy_i[1])
    i+=1
while i<len(t_values):
    xy_i = na3_x(t_values, x_values, y_values, i,h_max)
    x_values.append(xy_i[0])
    y_values.append(xy_i[1])
    i+=1


xt, yt = y1_y2_correct(t_values)  
delta_x=[]
delta_y=[]
i=0
while i<len(t_values):
    delta_x.append(abs(xt[i] - x_values[i])) 
    delta_y.append(abs(yt[i] - y_values[i]))
    i+=1

table = pd.DataFrame({'T': t_values, 'X': x_values, 'X_tochne':xt, 'delta_X':delta_x, 'Y': y_values, 'Y_tochne':yt, 'delta_Y':delta_y})
table.to_csv('output.csv', index=False)
print(t1)
print(h_min)
print(h_max)
