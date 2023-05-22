import math

def integrand(t, a, b):
    return math.sqrt((a * math.cos(t))**2 + (b * math.sin(t))**2)

def trapezoidal_rule(a, b, h):
    n = int((b - a) / h)
    integral = 0.5 * (integrand(a, a, b) + integrand(b, a, b))
    for i in range(1, n):
        integral += integrand(a + i * h, a, b)
    return integral * h

a = 152.098232
b = 147.098200
start = 0
end = 2 * math.pi

h1 = 0.01
integral1 = trapezoidal_rule(start, end, h1)

h2 = 0.001
integral2 = trapezoidal_rule(start, end, h2)

distance1 = integral1 * a
distance2 = integral2 * a

print("Відстань з кроком h = 0.01:", distance1, "млн. км")
print("Відстань з кроком h = 0.001:", distance2, "млн. км")
