### Desafío 2:

Diseña una función que tome una cadena y devuelva la misma cadena, pero con el primer carácter de cada palabra en mayúsculas.

Primero tuve que buscar en la documentación de Python, la página es https://www.w3schools.com, aquí encontré un método nativo de Python el cual se llama `capitalize` sin embargo, este método sólo pone la primer letra de una frase como mayúsculas, para este desafío no me sirve, sin embargo puede ser una solución adecuada, por ejemplo, para cuando le solicitamos a un usuario que escriba su nombre, independientemente de que lo escriba en minúsculas, con la primer letra en mayúsculas, todo en mayúsculas o con la primer letra en minúscula y el resto en mayúsculas.

Buscando un poco más en la documentación, encontré el método `title` el cual sí me sirve para este propósito, ya que permite que cada palabra dentro de una cadena de texto, comience con la mayúscula, lo que mencioné anteriormente sobre que no importa como recibe la frase, la devuelve de manera "correcta"