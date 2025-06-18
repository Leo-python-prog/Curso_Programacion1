### Desafío 1:

Crea una función que tome una lista de números y devuelva la suma y el promedio de esos números.

Para este caso, se define una función, la cual llamaremos como `def suma_prom` la cual recibirá la lista de números previamente creada y retornará la suma de los números de la lista así como también el promedio de los mismos.

En la solución 1, se define la función, la cual recibirá la lista con números, luego se crea una variable suma la cual la iniciamos en 0 (cero), posteriormente usamos un bucle `for` para recorrer la lista e ir sumando en cada iteración los números.

Luego creamos otra variable llamada prom la cual calculará la suma de los valores previamente conseguida y lo dividirá por el largo de la lista en cuestión, de esta manera se obtiene el promedio.

En la solución 2, se repite el proceso de definir la función, la cual se le pasará como argumento la lista de números, dentro se usa la función `sum`, la cual es nativa de Python y nos facilita mucho las cosas, ya que solo debemos pasarle la lista y dicha función suma por nosotros, es más eficiente desde el punto de vista de "ahorrar" líneas de código.

El resto del código es similar a la solución 1.