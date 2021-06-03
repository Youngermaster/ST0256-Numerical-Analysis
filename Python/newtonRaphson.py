import numpy as np
from math import *
import sympy as sp

# Global variables
NMAX = 100
ERROR = 100
TOLERANCE = 0.00001


def newtonRaphson(x0,  error, test, f, df):
    ni = 0
    if not test:
        print("# iter\t\tx\t\t\tf(x)\t\t\terror\t\t\t")
        print("{0:d}\t\t{1:8.6f}\t\t{2:8.6f}\t\t{3:8.6f}".format(
            ni, x0, f(x0), error))

    root_solution = 0
    # Ejecucion del programa
    while error > TOLERANCE and ni < NMAX:
        x1 = x0 - (f(x0) / df(x0))
        ni += 1
        error = abs(x1 - x0)
        if not test:
            print("{0:d}\t\t{1:8.6f}\t\t{2:8.4f}\t\t{3:8.6f}".format(
                ni, x0, x1, error))
        x0 = x1
        root_solution = x1

    if test:
        return root_solution
    else:
        print("The value of the root is: ", root_solution)


def f_test_1(x):
    return (x**3) - (x**2) + 2


def df_test_1(x):
    return (3*x**2) - (2*x)


def f_test_2(x):
    return (2 * x**3) - (2 * x) - 5


def df_test_2(x):
    return (6 * x**2) - 2


def f_test_3(x):
    return x - np.cos(x)


def df_test_3(x):
    return 1 + np.sin(x)


if __name__ == "__main__":
    x0 = -20
    newtonRaphson(x0, ERROR, False, f_test_1, df_test_1)


# Tests
def test_1():
    x0 = -20
    assert newtonRaphson(x0, ERROR, True,
                         f_test_1, df_test_1) == -1.000000000000011


def test_2():
    x0 = 2
    assert newtonRaphson(x0, ERROR, True,
                         f_test_2, df_test_2) == 1.6005985449336209


def test_3():
    x0 = 0
    assert newtonRaphson(x0, ERROR, True, f_test_3,
                         df_test_3) == 0.7390851332151607
