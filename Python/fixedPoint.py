import numpy as np
from math import *

# Global variables
NMAX = 20
TOLERANCE = 0.00001


def fixedPoint(p0,  g, test):
    iteri = 0
    while iteri < NMAX:
        p = g(p0)
        if not test:
            print("p = \t" + str(p))
        error = abs(p0 - p)
        if error < TOLERANCE:
            break
        p0 = p
        if not test:
            print("p0 = \t" + str(p0))
            print()
        iteri += 1

    # Salida
    if iteri > NMAX:
        print("The method does not converge")
    else:
        if not test:
            print("The point of the function g(x) is: \t" + str(p))
        else:
            return p


def g_test_1(x):
    return (2 - (np.exp(x)) + x**2) / 3


if __name__ == "__main__":
    p0 = 0
    fixedPoint(p0, g_test_1, False)


# Tests
def test_1():
    p0 = 0
    assert fixedPoint(p0, g_test_1, True) == 0.25753180626753985


"""
# Entradas
ecuacion = input("Ingrese la ecuacion \n")
p0 = float(input("Ingrese el punto inicial \n"))
TOLERANCE = float(input("ingrese la tolerecia \n"))
NMAX = float(input("Ingrese el numero maximo de iteracciones \n"))
iteri = 0


def g(x):
    return eval(ecuacion)

"""
