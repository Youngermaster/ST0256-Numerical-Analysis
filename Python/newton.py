import numpy as np
from math import *


def f(x):
    return 2200 * np.log(160000 / (160000 - 2680 * x)) - 9.81 * x


def df(x):
    return (147400 / (-67 * x + 4000)) - 9.81


x0 = 22
tol = 0.0000001
error = 100
nmax = 100
ni = 0


print("# iter\t\t x \t\t f(x) \t\t error")
print("{0:d}\t{1:8.6f}\t{2:8.6f}\t{3:8.6f}".format(ni, x0, f(x0), error))

while error > tol and ni < nmax:
    x1 = x0 - (f(x0) / df(x0))
    ni += 1
    error = abs(x1 - x0)
    print("{0:d}\t{1:8.6f}\t{2:8.4f}\t{3:8.6f}".format(ni, x0, x1, error))
    x0 = x1
