"""Desarrollar un programa que permita leer el numero de datos y luego forme una lista leyendo los datos desde el teclado.
"""

lista = [int(input("Dato %d : " % (n+1)))
        for n in range(int(input("Numero de elementos : ")))]
print(lista)
