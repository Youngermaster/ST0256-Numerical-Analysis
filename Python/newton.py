import numpy as np
from math import *
import sympy as sp

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

x0 = -20
tol = 0.00001
nmax = 20


def f(x):
    return (x**3) - (x**2) + 2


def df(x):
    return (3*x**2) - (2*x)


# error e iteracion inicial
error = 100
ni = 0


print("# iter\t\tx\t\t\tf(x)\t\t\terror\t\t\t")
print("{0:d}\t\t{1:8.6f}\t\t{2:8.6f}\t\t{3:8.6f}".format(ni, x0, f(x0), error))

root_solution = 0
# Ejecucion del programa
while error > tol and ni < nmax:
    x1 = x0 - (f(x0) / df(x0))
    ni += 1
    error = abs(x1 - x0)
    print("{0:d}\t\t{1:8.6f}\t\t{2:8.4f}\t\t{3:8.6f}".format(ni, x0, x1, error))
    x0 = x1
    root_solution = x1

print("The value of the root is: ", root_solution)
