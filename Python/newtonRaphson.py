import numpy as np
from math import *
import sympy as sp


def newtonRaphson(x0, tol, nmax, error, test, f, df):
    ni = 0
    if not test:
        print("# iter\t\tx\t\t\tf(x)\t\t\terror\t\t\t")
        print("{0:d}\t\t{1:8.6f}\t\t{2:8.6f}\t\t{3:8.6f}".format(
            ni, x0, f(x0), error))

    root_solution = 0
    # Ejecucion del programa
    while error > tol and ni < nmax:
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


if __name__ == "__main__":
    x0 = -20
    tol = 0.00001
    nmax = 20
    error = 100
    newtonRaphson(x0, tol, nmax, error, False, f_test_1, df_test_1)


# Tests
def test_1():
    x0 = -20
    tol = 0.00001
    nmax = 20
    error = 100
    assert newtonRaphson(x0, tol, nmax, error, True,
                         f_test_1, df_test_1) == -1.000000000000011


def test_2():
    x0 = 2
    tol = 0.00001
    nmax = 20
    error = 100
    assert newtonRaphson(x0, tol, nmax, error, True,
                         f_test_2, df_test_2) == 1.6005985449336209


"""
# Datos necesarios para la ejecucion
ecuacion = input("Ingrese la ecuacion: ")
x0 = float(input("Ingrese el punto inicial: "))
tol = float(input("Ingrese la tolerancia: "))
nmax = float(input("ingrese el numero maximo de iteracciones: "))


x = sp.Symbol('x')

# Funcion a evaluar
def f(x):
    return eval(ecuacion)


# Evaluacionde la derivada de la funcion
def df(x):
    return eval(str(dev()))

# Derivada de la funcion a evaluar
def dev():
    return sp.diff(ecuacion, x)
"""
