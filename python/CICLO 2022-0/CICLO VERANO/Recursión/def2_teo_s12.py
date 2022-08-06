"""
Condición base:

- Para evitar una recursión infinita siempre se debe considerar (al menos) una condición base.

-La condición base es el caso particular de la definición recursiva de la que se conoce el resultado, por lo tanto, no es necesario seguir invocando la recursión.
-Caso contrario:
[Previous line repeated 996 more times]
RecursionError: maximum recursion depth exceeded

-Es necesario controlar el tope de la recursión, de lo contrario se genera un error.
"""