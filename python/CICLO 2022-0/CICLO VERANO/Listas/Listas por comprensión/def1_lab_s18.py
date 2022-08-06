"""
¿Qué es Comprensión en Python?
Es una forma de instrucción que permite de manera concisa la construcción de una colección secuencial.

Comprensión se basa en la notación por comprensión de conjuntos. Desde la perspectiva computacional Comprensión utiliza un estilo declarativo y funcional.

Es común en programación crear nuevas listas donde:
-Cada elemento es el resultado de alguna operación aplicada a cada miembro dde otra secuencia o iterable.
-Queremos crear una secuencia parcial con sólo aquellos elementos que satisfacen cierta condición.

-List comprehension es generalmente más compacto y rápido que utilizar estructuras de control de bucles regulares y llamadas a función para crear la lista.

Sintaxis:
La sintaxis de comprensión de listas consiste de corchetes rodeando una <expresión> seguida de la declaración for y luego cero o más declaraciones for o if.

El resultado será una nueva lista que resulta de evaluar la <expresión> en el contexto de los for o if que le siguen.

Ejemplo:
lista = [expresion for item in iterable]
lista = [expresion for item in iterable if condition]
"""