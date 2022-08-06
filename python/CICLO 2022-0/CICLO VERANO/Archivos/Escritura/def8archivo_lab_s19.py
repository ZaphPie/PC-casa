"""
Escribir un archivo sin sobreescribirlo.

- Cuando se desea añadir información en un archivo a partri de la última línea del mismo, se utiliza el modo "a" al momento de abrirlo.
-La forma en que se usa write no cambia

inputFile = open("datos.txt","a")
inputFile.write("Finalmente\n")
inputFile.write("Bienvenidos al curso de ICC\n")
inputFile.write("del 2019-1\n")
inputFile.close()

"""