import numpy as np
from math import *

# Global variables
NMAX = 100
TOLERANCE = 0.00001
OP = 1


def fe(a, b, op, f):
    if op == 1:
        return abs(f(a))
    elif op == 2:
        return abs(b - a)

    elif op == 3:
        return abs(b - a) / b


def bisection(lower_end, upper_end,  test, f):
    a = lower_end
    b = upper_end
    niter = 0
    m = lower_end + (upper_end - lower_end) / 2

    fa = f(lower_end)
    fb = f(upper_end)
    fm = f(m)
    ERROR = 100
    if not test:
        print("# iter\t\t a \t\t f(a) \t\t b \t\t f(b) \t\t m \t\t f(m)  \t\t ERROR")
        print(
            "{0} \t\t {1:6.4f} \t {2:6.4f} \t {3:6.4f} \t {4:6.4f} \t {5:6.4f} \t {6:6.4f} \t {7:6.9f}".format(
                niter, lower_end, fa, upper_end, fb, m, fm, ERROR
            )
        )

    while ERROR > TOLERANCE and niter < NMAX:
        m = lower_end + (upper_end - lower_end) / 2
        if np.sign(fa) == np.sign(fm):
            lower_end = m
            fa = f(lower_end)
        else:
            upper_end = m
            fb = f(upper_end)
        m = lower_end + (upper_end - lower_end) / 2
        fm = f(m)
        ERROR = fe(lower_end, upper_end, OP, f)

        niter += 1
        if not test:
            print(
                "{0} \t\t {1:6.4f} \t {2:6.4f} \t {3:6.4f} \t {4:6.4f} \t {5:6.4f} \t {6:6.4f} \t {7:6.9f}".format(
                    niter, lower_end, fa, upper_end, fb, m, fm, ERROR
                )
            )
    if not test:
        print(
            "The root of the function between [{0:6.4f}, {1:6.4f}] is: {2:6.4f}".format(
                a, b, m
            )
        )
        print("The estimated ERROR is: {0:6.8f}".format(ERROR))
    else:
        return m


def f_test_1(x):
    return (3 * x**3) - (2 * x) - 5


if __name__ == "__main__":
    lower_end = 0
    upper_end = 2
    bisection(lower_end, upper_end, False, f_test_1)


# Tests
def test_1():
    lower_end = 0
    upper_end = 2
    assert bisection(lower_end, upper_end,
                     True, f_test_1) == 1.3717398643493652


"""
ecuacion = input("Ingrese la función a resolver: ")
lower_end = float(input("Ingrese el extremo inferior del intervalo: "))
upper_end = float(input("Ingrese el extremo superior del intervalo: "))
TOLERANCE = float(input("Ingrese la TOLERANCE del método: "))
NMAX = int(input("Ingrese el máximo de iteraciones a realizar: "))
op = float(
    input(
        "Escoga el criterio de aproximacion 1 = |f(x)| \t  2 = |xn- xn-1|  \t 3 = |xn - xn-1|/xn \n"
    )
)

def f(x):
    return eval(ecuacion)
"""
