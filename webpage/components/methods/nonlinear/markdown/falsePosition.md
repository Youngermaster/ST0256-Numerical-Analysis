El método de **posición falsa** o **Regula Fasi** es un método de corchetes para encontrar una solución numérica
solución de una ecuación de la forma $ f(x) = 0 $ dentro de un intervalo dado $ [a, b] $ .

En ese intervalo, la ecuación de una recta que une $ a$ y $ b $ es:

$$
\tag{1} y = \frac{f(b) - f(a)}{b - a} (x - b) + f(b)

$$

From **(1)**, the point of $ m $ where the line intersects the x-axis is determined by substituting $ y = 0 $ and solving for $x$:

$$
\tag{2} m = \frac{a\cdot f(b) - b \cdot f(a)}{f(b) - f(a)}

$$

El procedimiento (o algoritmo) para encontrar una solución con el método de regula falsi es casi el mismo que el del método de bisección.

***

Algoritmo:
1. Escoger el primer intervalo encontrando los puntos $ a$ y $ b $ tales que exista una solución entre ellos. Es decir, que $ f(a) $ y $ f(b) $ tengan signos diferentes tales que $ f(a) f(b) < 0 $.

2. Calcular la primera estimación de la solución numérica utilizando **(2)**.

3. Determinar si la verdadera solución está entre $ a$ y $ m $, o entre $ m $ y $ b $. Esto se hace comprobando el signo del producto $ f(a) \cdot f(m) $ :
    * Si $ f(a) \cdot f(m) < 0 $, la verdadera solución está entre $ a$ y $ m $

    * Si $ f(a) \cdot f(m) > 0 $, la verdadera solución está entre $ m $ y $ b $

4. Seleccionar un nuevo subintervalo que contenga la verdadera solución, ya sea $ [a, m] $ o $ [m, b] $.

5. Los pasos 1 a 4 se repiten hasta que se alcance una tolerancia o límite de error especificado.

