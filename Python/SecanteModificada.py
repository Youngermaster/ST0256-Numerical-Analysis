import numpy as np
import sympy as sp


ecuacion = input("Ingrese la ecuacion \n ")
x0 = float(input("Ingrese el punto inicial \n "))
x1 = float(input("Ingrese el segundo punto \n "))
tol = float(input("Ingrese la tolerancia \n "))
nmax = float(input("Ingrese el numero maximo de iteracciones \n "))
roz =  float(input("Ingrese la fraccion de rozamiento"))
x = sp.Symbol('x')  

def f(x):
    return eval(ecuacion)

  
def dev():
     return sp.diff(ecuacion,x)

def df(x):
    return eval(dev())



error = 100
ni = 0


print("# iter\t\t x \t\t f(x) \t\t error")
print("{0:d}\t{1:8.6f}\t{2:8.6f}\t{3:8.6f}".format(ni, x1, f(x1), error))

while error > tol and ni < nmax:
    x2 = x1 - (f(x1) * (x1*roz) / (f(x1 + x1 *roz) - f(x1))
    ni += 1
    error = abs(x2 - x1)
    print("{0:d}\t{1:8.4f}\t{2:8.6f}\t{3:8.6f}".format(ni, x1, x2, error))
    x0 = x1
    x1 = x2