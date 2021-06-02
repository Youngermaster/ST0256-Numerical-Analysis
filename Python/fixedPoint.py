import numpy as np
from math import *


"""
# Entradas
ecuacion = input("Ingrese la ecuacion \n")
p0 = float(input("Ingrese el punto inicial \n"))
tol = float(input("ingrese la tolerecia \n"))
nmax = float(input("Ingrese el numero maximo de iteracciones \n"))
iteri = 0


def g(x):
    return eval(ecuacion)

"""

p0 = 0
tol = 0.00001
nmax = 100
iteri = 0


def g(x):
    return (2 - (np.exp(x)) + x**2) / 3


# Ejecucion
while iteri < nmax:
    p = g(p0)
    print("p = \t" + str(p))
    error = abs(p0 - p)
    if error < tol:
        break
    p0 = p
    print("p0 = \t" + str(p0))
    print()
    iteri += 1


# Salida

if iteri > nmax:
    print("El metodo no converge")
else:
    print("El punto de la funcion g(x) es \t" + str(p))
