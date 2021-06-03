#include <math.h>

#include <iostream>

#define EPSILON 0.00001
using namespace std;

double func(double x) {
    return x * x * x - x * x + 2;
}

double derivFunc(double x) {
    return 3 * x * x - 2 * x;
}

void newtonRaphson(double x) {
    printf("# iter\t\t x\t\t\t f(x)\t\t\t error\t\t\t \n");
    int iterations(0);
    double error(0);
    double h = func(x) / derivFunc(x);
    while (abs(h) >= EPSILON) {
        error = x;
        double x0 = x;

        h = func(x) / derivFunc(x);
        // x(i+1) = x(i) - f(x) / f'(x)
        x -= h;
        error = abs(x - error);

        printf("%d\t\t %f\t\t %f\t\t %f\t\t \n", iterations, x0, x, error);
        iterations++;
    }
    cout << "The value of the root is : " << x << endl;
}

int main() {
    double x0 = -20;
    newtonRaphson(x0);
    return 0;
}
