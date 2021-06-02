from newtonRaphson import *

def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4

def test_newton_raphson():
    x0 = -20
    tol = 0.00001
    nmax = 20
    error = 100
    assert newtonRaphson.newtonRaphson(x0, tol, nmax, error) == -1.000000000000011