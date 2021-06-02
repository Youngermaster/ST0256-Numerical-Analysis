import numpy as np
import sympy as sp
"""
# Parametros que se reciben para la ejecucion
ecuacion = input("Ingrese la ecuacion \n ")
x0 = float(input("Ingrese el punto inicial \n "))
x1 = float(input("Ingrese el segundo punto \n "))
tol = float(input("Ingrese la tolerancia \n "))
nmax = float(input("Ingrese el numero maximo de iteracciones \n "))

x = sp.Symbol('x')

# Funcion que se va evaluar
def f(x):
    return eval(ecuacion)


# Derivada de la funcion a evaluar
def dev():
    return sp.diff(ecuacion, x)

# Funcion que evalua la derivda de la funcion
def df(x):
    return eval(dev())
"""

x0 = 0
x1 = 2
tol = 0.00001
nmax = 100

def f(x):
    return x ** 3 + 1

def df(x):
    return 3 * (x**2)

# error y iteracion inicial
error = 100
ni = 0


print("# iter\t\t x \t\t f(x) \t\t error")
print("{0:d}\t{1:8.6f}\t{2:8.6f}\t{3:8.6f}".format(ni, x1, f(x1), error))

# Ejecucion del proceso
while error > tol and ni < nmax:
    x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
    ni += 1
    error = abs(x2 - x1)
    print("{0:d}\t{1:8.4f}\t{2:8.6f}\t{3:8.6f}".format(ni, x1, x2, error))
    x0 = x1
    x1 = x2

print("La raiz es: ", x1)