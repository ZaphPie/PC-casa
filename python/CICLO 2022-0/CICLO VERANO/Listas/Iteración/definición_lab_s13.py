"""
Listas: Características
Una lista es una estructura de datos mutable, es decir, es modificable, e incluso permite tener elementos repetidos
Para definir una lista debemos usar corchetes ([ ]) y dentro de ellos debemos incluir los elementos de la lista separados por comas (,)

Listas e índices
Los strings, que son colecciones de caracteres, podemos hacer referencia a uno de estos elementos a través de índices usando el operador corchete y un número (que representa el índice)
En las listas, también es posible hacerlo y de esta forma podremos seleccionar un elemento específico de la lista. Recordar que los índices inician en 0

Índices negativos y longitud (len)
Aunque los índices inicia de 0 y van hacia adelante, también podemos usar índices negativos
El índice -1 hace referencia al último elemento
El índice -2 hace referencia al penúltimo elemento y así sucesivamente
Por otro lado, podemos usar la función len para obtener el número de elementos de la lista

Entonces... ¿Cuál es el último elemento de una lista?
Si el primer elemento de una lista se encuentra en la posición o índice cero, entonces el último elemento de una lista tiene la posición o índice N-1, donde N es el número de elementos de la lista

Mutables e Inmutables (listas vs strings)
Una comparación entre strings y listas nos ayudará a ver la diferencia entre un objeto cuyos elementos son inmutables y otro cuyos elementos son mutables.

¿Qué tipos de datos podemos almacenar en una lista?
Los elementos en una lista pueden ser del mismo tipo o de diferentes tipos
Una lista puede contener listas (sublistas)
Una lista puede crearse sin valores. Si a una lista se le da un valor inicial None, no es una lista vacía. Además, algunos elementos en una lista pueden ser variables ya existente
None =  Ausencia de dato

Operaciones con listas
Suma -> Una lista puede ser sumada a otra lista
Agregar elementos a una lista -> Podemos usar la función append para agregar elementos a una lista
in ; not in -> El operador in permite determinar si un valor está dentro de una lista.
                La combinación not in permite determinar si un valor no está dentro de una lista
                En ambos casos, se retorna True o False según corresponda
Asignación múltiple partiendo de una lista -> La asignación múltiple te permite asignar múltiples variables con los valores de una lista en una línea de código.
Iterar o recorrer una lista -> Podemos recorrer una lista con un for de varias maneras
                                Podemos iterar la lista usando la función enumerate
                                En cada iteración, enumerate nos retornará tanto el índice como el elemento de la lista correspondiente.
                                Es útil cuando necesitas tanto el índice como su valor en el recorrido de listas.




"""