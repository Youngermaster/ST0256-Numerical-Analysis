import numpy as np
from math import *

ecuacion = input("Ingrese la función a resolver: ")
aValor = float(input("Ingrese el extremo inferior del intervalo: "))
bValor = float(input("Ingrese el extremo superior del intervalo: "))
tolerancia = float(input("Ingrese la tolerancia del método: "))
maximoIteraciones = int(input("Ingrese el máximo de iteraciones a realizar: "))
op = float(
    input(
        "Escoga el criterio de aproximacion 1 = |f(x)| \t  2 = |xn- xn-1|  \t 3 = |xn - xn-1|/xn \n"
    )
)


def f(x):
    return eval(ecuacion)


a = aValor
b = bValor


def fe(a, b, op):
    if op == 1:
        return abs(f(a))
    elif op == 2:
        return abs(b - a)

    elif op == 3:
        return abs(b - a) / b


error = 10
niter = 0


m = aValor + (bValor - aValor) / 2

fa = f(aValor)
fb = f(bValor)
fm = f(m)


print("# iter\t\t a \t\t f(a) \t\t b \t\t f(b) \t\t m \t\t f(m)  \t\t error")
print(
    "{0} \t\t {1:6.4f} \t {2:6.4f} \t {3:6.4f} \t {4:6.4f} \t {5:6.4f} \t {6:6.4f} \t {7:6.9f}".format(
        niter, aValor, fa, bValor, fb, m, fm, error
    )
)

while error > tolerancia and niter < maximoIteraciones:
    m = aValor + (bValor - aValor) / 2
    if np.sign(fa) == np.sign(fm):
        aValor = m
        fa = f(aValor)
    else:
        bValor = m
        fb = f(bValor)
    m = aValor + (bValor - aValor) / 2
    fm = f(m)
    error = fe(aValor, bValor, op)

    niter += 1
    print(
        "{0} \t\t {1:6.4f} \t {2:6.4f} \t {3:6.4f} \t {4:6.4f} \t {5:6.4f} \t {6:6.4f} \t {7:6.9f}".format(
            niter, aValor, fa, bValor, fb, m, fm, error
        )
    )

print(
    "La raiz de la funcion dada en el intervalo [{0:6.4f},{1:6.4f}] es {2:6.4f}".format(
        a, b, m
    )
)

print("el errores {0:6.8f}".format(error))
