// C++ program for implementation of Newton Raphson Method for
// solving equations
// #include <bits/stdc++.h>
#include <math.h>

#include <iostream>

#define EPSILON 0.001
using namespace std;

// An example function whose solution is determined using
// Bisection Method. The function is x^3 - x^2 + 2
double func(double x) {
    return x * x * x - x * x + 2;
}

// Derivative of the above function which is 3*x^x - 2*x
double derivFunc(double x) {
    return 3 * x * x - 2 * x;
}

// Function to find the root
void newtonRaphson(double x) {
    int iterations(0);
    double h = func(x) / derivFunc(x);
    while (abs(h) >= EPSILON) {
        h = func(x) / derivFunc(x);

        // x(i+1) = x(i) - f(x) / f'(x)
        x -= h;
        iterations++;
    }
    cout << "Iterations: " << iterations << endl;
    cout << "The value of the root is : " << x << endl;
}

// Driver program to test above
int main() {
    double x0 = -20;  // Initial values assumed
    newtonRaphson(x0);
    return 0;
}
