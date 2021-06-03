#include <cmath>
#include <iostream>

using namespace std;

// Global variables
#define NMAX 100
#define TOLERANCE 0.00001
#define EXACTITUDEC 0.00005

// Actual Function to use
double F(double x) {
    return 3 * pow(x, 3) - 2 * x - 5;
}

/*
* Bisection method 
* a -> lower end
* b -> upper end
* MAXIT -> maximum number of iterations of the algorithm
* TOL -> tolerance of the program to the error
* EX -> exactitude criteria
*/
double bisection(double a, double b, bool test) {
    if (!test)
        printf("# iter\t\t x\t\t\t f(x)\t\t\t error\t\t\t \n");
    int iteration = 1;
    double c;
    double fc;
    while (iteration < NMAX) {
        c = (a + b) / 2;
        fc = F(c);
        if (abs(b - a) < TOLERANCE)
            return c;
        if (abs(fc) < EXACTITUDEC)
            return c;
        if (F(a) * fc < 0)
            b = c;
        if (fc * F(b) < 0)
            a = c;

        if (!test)
            printf("%d\t\t\n", iteration);
        iteration++;
    }
    return c;
}

int main(int argc, char *argv[]) {
    double lowerEnd = 0;
    double upperEnd = 2;
    double result = bisection(lowerEnd, upperEnd, true);
    printf("The root of the function between [%f, %f] is: %f", lowerEnd, upperEnd, result);
    return 0;
}