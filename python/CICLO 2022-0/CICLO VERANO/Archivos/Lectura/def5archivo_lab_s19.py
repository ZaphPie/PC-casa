"""
Leyendo datos de un archivo: readline()

Para leer datos de un archivo tambióen se utiliza la función readline()

<cadena_lineal> =<objeto_archivo>.readline()
-El método readline() permite obtener una línea de texto de un archivo.
-Cuando un archivo es abierto, se utiliza un puntero que indica la posición última línea leída. Cada vez que se hace readline() el puntero avanza a la siguiente línea. 

inputfile = open("datos.txt", "r")
cadena = inputFile.readline()
while cadena != '':
    print(cadena, end= "")
cadena = inputFile.readline()
"""