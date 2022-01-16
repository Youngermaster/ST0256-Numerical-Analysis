Un problema potencial en la aplicación del método Newton-Raphson es la evaluación de la derivada. Aunque esto no es inconveniente para los polinomios y muchas otras funciones, hay ciertas funciones cuyas derivadas pueden ser extremadamente difíciles o inconvenientes de evaluar. Para estos casos, la derivada puede aproximarse mediante una diferencia directa:

$$
\tag{1} f^{'}(x_{i}) = \frac{f(x_{i+1}) - f(x_{i})}{x_{i+1} - x_{i}}

$$

En lugar de utilizar dos valores de x, el método de la **secante modificada** introduce una pequeña fracción de perturbación, $ \delta $, tal que **(1)** se convierte en:

$$
\tag{2} f^{'}(x_{i}) = \frac{f(x_{i} + \delta x_{i}) - f(x_{i})}{\delta x_{i}}

$$
Sustituyendo **(2)** en la fórmula de Newton-Rhapson,

$$
\tag{3} x_{i+1} = x_{i} - \frac{\delta x_{i} f(x_{i})}{f(x_{i} + \delta x_{i}) - f(x_{i})}

$$

***

La elección de un valor adecuado para $ \delta $ no es automática. Si $ \delta $ es demasiado pequeño, el método se vuelve vulnerable a los errores de redondeo causados por la cancelación sustractiva en el denominador de **(3)**. Si es demasiado grande, la técnica puede resultar ineficiente e incluso divergente. Sin embargo, si se elige correctamente, proporciona una buena alternativa para los casos en que la evaluación de la derivada es difícil y el desarrollo de dos conjeturas iniciales es inconveniente.