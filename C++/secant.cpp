#include <math.h>
#include <stdio.h>

#include <cmath>
#include <iostream>
#define ERROR 0.00001

using namespace std;

double calculaError(int t, double vant, double vact) {
    double err = 0.0;
    switch (t) {
        case 0:
            // Absolut error
            err = vant - vact;
            break;
        case 1:
            // Relative error
            err = (vant - vact) / vant;
            break;
        case 2:
            // Porcentual Error
            err = ((vant - vact) / vant) * 100;
            break;
    }
    return err;
}

double f(double x) {
    return (pow(x, 3)) + 1;
}

int counter;
double xa, xb, res, error;

double Secante(double x1, double x0) {
    xa = x1;
    xb = x0;
    counter = 0;
    do {
        res = xa - ((f(xa) * (xb - xa)) / (f(xb) - f(xa)));
        error = calculaError(1, xa, res);
        xa = xb;
        xb = res;
        counter++;

        if (res != res) {
            cout << "La función se indeterminada: " << '\n';
            return res;
        }
    } while (abs(error) > ERROR);  // ERROR
    cout << counter << " interacion(es)." << '\n';
    return res;
}

int main(int argc, char const *argv[]) {
    double x1(0), x0(2);

    double raiz = Secante(x1, x0);
    cout << "La raíz es: " << raiz << '\n';

    return 0;
}