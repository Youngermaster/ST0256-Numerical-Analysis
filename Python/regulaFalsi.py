import numpy as np

# Global variables
NMAX = 100
ERROR = 100
TOLERANCE = 0.00001
OP = 1


# This Function is in charge of choosing the approximation criterion
def fe(a, b, op, f):
    if op == 1:
        return abs(f(a))
    elif op == 2:
        return abs(b - a)

    elif op == 3:
        return abs(b - a) / b


def regula_falsi(lower_end, upper_end, error, f, test):
    # Assignment of interval values
    a = lower_end
    b = upper_end

    # Error and initial number of iterations
    error = 100
    niter = 0

    # Evaluation of the functions at the ends of the intervals
    fa = f(lower_end)
    fb = f(upper_end)

    # Middle value
    m = lower_end - fa * (upper_end - lower_end) / (fb - fa)

    # Value of the function evaluated at the middle value
    fm = f(m)
    if not test:
        print("# iter\t\t a \t\t f(a) \t\t b \t\t f(b) \t\t m \t\t f(m)  \t\t error")
        print(
            "{0} \t\t {1:6.4f} \t {2:6.4f} \t {3:6.4f} \t {4:6.4f} \t {5:6.4f} \t {6:6.4f} \t {7:6.4f}".format(
                niter, lower_end, fa, upper_end, fb, m, fm, error
            )
        )

    # Cycle in charge of executing the iterations
    while error > TOLERANCE and niter < NMAX:
        m = lower_end - fa * (upper_end - lower_end) / (fb - fa)
        if np.sign(fa) == np.sign(fm):
            lower_end = m
            fa = f(lower_end)
        else:
            upper_end = m
            fb = f(upper_end)
        m = lower_end - fa * (upper_end - lower_end) / (fb - fa)
        fm = f(m)
        error = fe(lower_end, upper_end, OP, f)
        niter += 1
        if not test:
            print(
                "{0} \t\t {1:6.4f} \t {2:6.4f} \t {3:6.4f} \t {4:6.4f} \t {5:6.4f} \t {6:6.4f} \t {7:6.4f}".format(
                    niter, lower_end, fa, upper_end, fb, m, fm, error
                )
            )
    if not test:
        print(
            "The root of the function between [{0:6.4f},{1:6.4f}] is: {2:6.6f}".format(
                a, b, m
            )
        )
    else:
        return m


def f_test_1(x):
    return np.cos(x) - x * (np.exp(x))


if __name__ == "__main__":
    lower_end = 0
    upper_end = 2
    regula_falsi(lower_end, upper_end, ERROR, f_test_1, False)


# Tests
def test_1():
    lower_end = 0
    upper_end = 2
    assert regula_falsi(lower_end, upper_end, ERROR,
                        f_test_1, True) == 0.5177551702890896
