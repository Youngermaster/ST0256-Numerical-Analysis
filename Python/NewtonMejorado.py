import numpy as np


def f(x):
    return (x ** 3) - 5 * (x ** 2) + 7 * x - 3


def df(x):
    return 3 * (x ** 2) - 10 * x + 7


def dp(x):
    return 6 * x - 10


x0 = 0
tol = 0.0000001
error = 100
nmax = 100
ni = 0


print("# iter\t\t x \t\t f(x) \t\t error")
print("{0:d}\t{1:8.6f}\t{2:8.6f}\t{3:8.6f}".format(ni, x0, f(x0), error))

while error > tol and ni < nmax:
    x1 = x0 - ((f(x0) * df(x0)) / (((df(x0)) ** 2) - f(x0) * dp(x0)))
    ni += 1
    error = abs(x1 - x0)
    print("{0:d}\t{1:8.6f}\t{2:8.6f}\t{3:8.6f}".format(ni, x0, x1, error))
    x0 = x1
