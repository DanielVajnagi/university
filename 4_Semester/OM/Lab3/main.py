from math import exp
#Метод Ньотона
def f(x):
    return 10 * x * exp(x) + 7 * (exp(x) - 1) - 15

def df(x):
    return 10 * x * exp(x) + 10 * exp(x) + 7 * exp(x)

def newton_method(lambda0, eps):
    lambda_prev = lambda0
    lambda_ = lambda_prev - f(lambda_prev) / df(lambda_prev)
    while abs(lambda_ - lambda_prev) > eps:
        lambda_prev = lambda_
        lambda_ = lambda_prev - f(lambda_prev) / df(lambda_prev)
    return lambda_

#Метод простої ітерації
def g(x):
    return (15 - 7*(exp(x)-1))/ (10*exp(x)+7)

def simple_iter(lambda_0, eps):
    lambda_prev = lambda_0
    lambda_ = g(lambda_prev)
    while abs(lambda_ - lambda_prev) >= eps:
        lambda_prev = lambda_
        lambda_ = g(lambda_prev)
    return lambda_


eps = 0.001
lambda_0 = 1.0

lambda_value = simple_iter(lambda_0, eps)
print(f"Метод простої ітерації: {lambda_value:.3f}")


lambda_value = newton_method( lambda_0, eps)
print(f"Метод Ньотона: {lambda_value:.3f}")
