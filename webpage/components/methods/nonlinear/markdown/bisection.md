El método de **bisección** es un método cerrado para encontrar una

solución de una ecuación de la forma $ f(x) = 0 $ dentro de un intervalo dado $ [a, b] $ .

***

Algoritmo:
1. Elegir el primer intervalo encontrando los puntos $ a $ y $ b $ tales que exista una solución entre ellos. Es decir, que $ f(a) $ y $ f(b) $ tengan signos diferentes tales que $ f(a) f(b) < 0 $.

2. Calcular la primera estimación de la solución numérica: $$ m = \frac{a+b}{2} $$

3. Esto se hace comprobando el signo del producto $ f(a) \cdot f(m) $ :
    * Si $ f(a) \cdot f(m) < 0 $, la verdadera solución está entre $ x_{a} $ y $ m $

    * Si $ f(a) \cdot f(m > 0 $, la solución verdadera está entre $ m $ y $ b $

4. Seleccione un nuevo subintervalo que contenga la verdadera solución, ya sea $ [a, m] $ o $ [m, b] $.

5. Los pasos 1 a 4 se repiten hasta que se alcance una tolerancia o límite de error especificado.


