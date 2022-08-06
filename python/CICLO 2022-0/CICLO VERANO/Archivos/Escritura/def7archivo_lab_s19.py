"""
Escribir un archivo

-Para escribir un archivo se utiliza la función write
-Otra forma de leer un archivo, es utilizando la instrucción readlines():
<objeto_archivo>.write(<cadena>)

-Se recomienda usar el modo w+ al abrir el archivo, esto permite abrir el archivo en modo lectura y escritura.
-La función write se usa sobre el objeto archivo.
-La función write solo acepta como parámetro un dato de tipo texto.

inputFile = open("datos.txt","w+")
inputFile.write("UTEC\n")
inputFile.write("Bienvenidos al curso de ICC\n")
inputFile.write("del 2019-1\n")
inputFile.close()
"""