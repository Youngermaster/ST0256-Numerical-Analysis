import numpy as np

# Global variables
NMAX = 100
ERROR = 100
TOLERANCE = 0.00001
OP = 1


# Funcion que se encarga de escoger el criterio de aproximacion
def fe(a, b, op, f):
    if op == 1:
        return abs(f(a))
    elif op == 2:
        return abs(b - a)

    elif op == 3:
        return abs(b - a) / b


def regula_falsi(aValor, bValor, tolerancia, maximoIteraciones, error, f, test):
    # Asignacion de los valores de los intervalos
    a = aValor
    b = bValor

    # Error y numero inicial de iteraciones
    error = 100
    niter = 0

    # Evaluacion de las funciones en los extremos de los intervalos
    fa = f(aValor)
    fb = f(bValor)

    # Valor medio
    m = aValor - fa * (bValor - aValor) / (fb - fa)

    # Valor de la funcion evaluado en el punto medio
    fm = f(m)
    if not test:
        print("# iter\t\t a \t\t f(a) \t\t b \t\t f(b) \t\t m \t\t f(m)  \t\t error")
        print(
            "{0} \t\t {1:6.4f} \t {2:6.4f} \t {3:6.4f} \t {4:6.4f} \t {5:6.4f} \t {6:6.4f} \t {7:6.4f}".format(
                niter, aValor, fa, bValor, fb, m, fm, error
            )
        )

    # Ciclo que se encarga de ejecutar las iteraccione
    while error > tolerancia and niter < maximoIteraciones:
        m = aValor - fa * (bValor - aValor) / (fb - fa)
        if np.sign(fa) == np.sign(fm):
            aValor = m
            fa = f(aValor)
        else:
            bValor = m
            fb = f(bValor)
        m = aValor - fa * (bValor - aValor) / (fb - fa)
        fm = f(m)
        error = fe(aValor, bValor, OP, f)
        niter += 1
        if not test:
            print(
                "{0} \t\t {1:6.4f} \t {2:6.4f} \t {3:6.4f} \t {4:6.4f} \t {5:6.4f} \t {6:6.4f} \t {7:6.4f}".format(
                    niter, aValor, fa, bValor, fb, m, fm, error
                )
            )
    if not test:
        print(
            "La raiz de la funcion dada en el intervalo [{0:6.4f},{1:6.4f}] es {2:6.6f}".format(
                a, b, m
            )
        )
    else:
        return m


def f_test_1(x):
    return np.cos(x) - x * (np.exp(x))


if __name__ == "__main__":
    aValor = 0
    bValor = 2
    regula_falsi(aValor, bValor, TOLERANCE, NMAX, ERROR, f_test_1, False)


# Tests
def test_1():
    aValor = 0
    bValor = 2
    assert regula_falsi(aValor, bValor, TOLERANCE, NMAX,
                        ERROR, f_test_1, True) == 0.5177551702890896


"""
# Parametros que se reciben para la ejecucion de los metodos
ecuacion = input("Ingrese la función a resolver: ")
aValor = float(input("Ingrese el extremo inferior del intervalo: "))
bValor = float(input("Ingrese el extremo inferior del intervalo: "))
tolerancia = float(input("Ingrese la tolerancia del método: "))
maximoIteraciones = int(input("Ingrese el máximo de iteraciones a realizar: "))
op = float(
    input(
        "Escoga el criterio de aproximacion 1 = |f(x)| \t  2 = |xn- xn-1  \t 3 = |xn - xn-1|/xn \n"
    )
)

# Funcion a evaluar
def f(x):
    return eval(ecuacion)
"""
