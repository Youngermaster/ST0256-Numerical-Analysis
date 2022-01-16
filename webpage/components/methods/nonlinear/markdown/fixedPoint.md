El método de **punto fijo** encuentra una solución numérica
de una ecuación de la forma $ f(x) = 0 $ reordenando la ecuación de forma que x esté en el lado izquierdo:

$$
\begin{array}{lcl}
   x &=& g(x)
\\ x_{i+1} &=& g(x_{i})
\end{array}
$$

El método parte de un valor inicial, $ x_{0} $. Se puede demostrar que la convergencia es bastante probable cuando $ g^{'}(x) < |1| $ .