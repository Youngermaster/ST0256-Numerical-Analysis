import numpy as np
from math import *
import sympy as sp

# Datos necesarios para la ejecucion
ecuacion = input("Ingrese la ecuacion \n ")
x0 = float(input("Ingrese el punto inicial"))
tol = float(input("Ingrese la tolerancia"))



x = sp.Symbol('x')


# Funcion a evaluar
def f(x):
    return eval(ecuacion)


# Evaluacionde la derivada de la funcion
def df(x):
    return eval(str(dev()))

# Derivada de la funcion a evaluar
def dev():
     return sp.diff(ecuacion,x)


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



