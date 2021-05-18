import numpy as np


def f(x):
    return np.exp(2 * x) - 2 * (x ** 3) * np.exp(x) + x ** 6 - 0.6


def df(x):
    return (-2 / x ** 3) - 20 * np.sin(10 * x) * np.cos(10 * x)


x0 = 4
x1 = 1
tol = 0.0000001
error = 100
nmax = 100
ni = 0


print("# iter\t\t x \t\t f(x) \t\t error")
print("{0:d}\t{1:8.6f}\t{2:8.6f}\t{3:8.6f}".format(ni, x1, f(x1), error))

while error > tol and ni < nmax:
    x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
    ni += 1
    error = abs(x2 - x1)
    print("{0:d}\t{1:8.4f}\t{2:8.6f}\t{3:8.6f}".format(ni, x1, x2, error))
    x0 = x1
    x1 = x2
