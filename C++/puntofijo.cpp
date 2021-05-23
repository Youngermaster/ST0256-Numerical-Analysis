#include <stdio.h>
#include <math.h>
#define e 2.718281828
#include <cstdlib>

double fun (double);

main (){
/*Para resolver la funcion siguiente x = 2 - e^x + x^2/3
con N = 10 o mas iteraciones TOL = 0.001 P0 = 0
y el resultado se da en la 6ta. iteracion*/

double P0,TOL,P,b;
int i, N, OK;

printf("Antes de continuar, cambia la funcion para un nuevo prblema\n");
printf ("Metodo Punto Fijo\n");
printf("Aproximacion inicial P0: ");
scanf ("%lf", &P0);
printf("Tolerancia TOL: ");
scanf("%lf", &TOL);
printf("Numero maximo de iteraciones: ");
scanf("%d", &N);
//paso 1
i = 1;
OK = 1;
//paso 2
printf("\n\nI\t\tP\n");
while(i <= N && OK == 1){
//paso 3
P = fun (P0);
printf("%d\t%12.8f\n", i, P);
//paso 4
b = fabs(P - P0);
if(b < TOL){
printf("Solucion aproximada P = %12.8f\n", P);
printf("Numero de iteraciones N = %d\n", i);
printf("Tolerancia TOL = %5.11f\n\n", TOL);
OK = 0;
}

else{
//paso 5
i++;
//paso 6
P0 = P;
}
}
//paso 7
if(OK == 1)
printf("\n\nEl metodo fallo con un numero de iteraciones N = %d\n\n",

N);

system("pause");
return 0;
}//cambia la funcion para un nuevo problema

double fun(double x){
double a;
a = (2 - pow (e, x) + x*x)/3;
return a;
}