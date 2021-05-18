import numpy as np
from math import *

ecuacion = input("Ingrese la funcion  g(x) \n ")


def g(x):
    return eval(ecuacion)


def puntofijo(a, tolera, iteramax=15):
    i = 0  # iteración
    b = g(a)
    print("b es :" + str(b))
    error = abs(b - a)
    while error >= tolera and i <= iteramax:
        a = b
        b = g(a)
        print("b es :" + str(b))

        error = abs(b - a)
        print("El error es:" + str(error))
        i = i + 1
    respuesta = b

    # Validar respuesta
    if i >= iteramax:
        respuesta = np.nan
    return respuesta


# PROGRAMA ---------


# y = float(input("Ingrese la funcion g(x) \n"))
# INGRESO
# fx = lambda x: x ** 2 - x

a = 1  # intervalo

tolera = 0.001
iteramax = 15  # itera máximo
muestras = 51  # gráfico
error = 50

# PROCEDIMIENTO
respuesta = puntofijo(a, tolera)

# SALIDA
print(respuesta)
