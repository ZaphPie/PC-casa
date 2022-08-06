"""
BUCLES ANIDADOS (NESTED LOOP)

Los bucles anidados son bucles dentro de otros bucles
Se puede combinar cualquer sentencia condicional o estructura de control dentro de otra.
La finalidad es expresar relaciones entre condiciones y/o repeticiones

Durante la ejecución de este algoritmo, por cada ejecución del bucle exterior, se ejecutará completamente el bucle interior.

Es decir, si el bucle exterior se ejecuta n veces y el interior m veces; el total de instrucciones será n * m veces.

La cantidad de veces que se ejecuta un bucle dentro de otro tiene implicancias en el tiempo de ejecución de los algoritmos.

A mayor nivel de bucles anidados, mayor cantidad de operaciones y con ello mayor uso de recursos (tiempo y memoria) del algoritmo.

"""

#EJEMPLO:

for x in range(1, n): #BUCLE EXTERIOR
    for y in range(1,m): #BUCLE INTERIOR
        print("*", end="")
    print()