Si la conjetura inicial de la raíz es $ x_{i} $, se puede extender una tangente/recta desde el punto $ (x_{i}, f(x_{i})) $. El punto donde esta tangente cruza el eje x representa una estimación mejorada de la raíz.

El método **Newton-Raphson** puede derivarse a partir de esta interpretación geométrica. La derivada en un punto es:

$$
f^{'}(x_{i}) = \frac{f(x_{i+1}) - f(x_{i})}{x_{i+1} - x_{i}}
$$

Setting $ f(x_{i+1}) = 0 $, we obtain:

$$
f^{'}(x_{i}) = \frac{0 - f(x_{i})}{x_{i+1} - x_{i}}

\\ \tag{1} x_{i+1} = x_{i} - \frac{f(x_{i})}{f^{'}(x_{i})}

$$

**(1)** se denomina fórmula de Newton-Rhapson y parte de un valor inicial, $ x_{0} $.

***
Aunque el método Newton-Raphson suele ser muy eficaz, 
hay situaciones en las que no funciona bien. Su convergencia depende de la naturaleza de la función y de la precisión de la estimación inicial.
* Si se produce un punto de inflexión ($ f^{''}(x) = 0 $) cerca de la raíz, la técnica de Newton-Raphson puede oscilar alrededor de un máximo o un mínimo local.
* El peor escenario es un extremo ($ f^{'}(x) = 0 $) que provoca una división por cero porque la solución se dispara horizontalmente y nunca llega al eje x.