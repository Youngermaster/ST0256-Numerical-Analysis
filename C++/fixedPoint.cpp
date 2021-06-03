#include <math.h>
#include <stdio.h>

#include <cstdlib>
// Global variables
#define e 2.718281828
#define NMAX 100
#define TOLERANCE 0.00001
#define EXACTITUDEC 0.00005

double fun(double);

int main() {
    double P0, TOL, P, b;
    int i, N, OK;

    P0 = 0;
    TOL = 0.00001;
    N = 10;

    // step 1
    i = 1;
    OK = 1;
    // step 2
    printf("\n\nI\t\tP\n");
    while (i <= N && OK == 1) {
        // step 3
        P = fun(P0);
        printf("%d\t%12.8f\n", i, P);
        // step 4
        b = fabs(P - P0);
        if (b < TOL) {
            printf("Approximate solution P = %12.8f\n", P);
            printf("Number of iterations N = %d\n", i);
            printf("Tolerance TOL = %5.11f\n\n", TOL);
            OK = 0;
        }

        else {
            // step 5
            i++;
            // step 6
            P0 = P;
        }
    }
    // step 7
    if (OK == 1)
        printf("\n\nEl metodo fallo con un numero de iteraciones N = %d\n\n", N);

    return 0;
}

double fun(double x) {
    return (2 - pow(e, x) + x * x) / 3;
}