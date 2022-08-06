"""
Leyendo datos de un archivo: readlines()

- Otra forma de leer un archivo, es utilizando la instrucción readlines():

<lista_cadena> = <objeto_archivo>.readlines()

- El método readlines() permite obtener todas las líneas de un archivo.
- La función devuelve una lista, en la cual cada elemento es una línea del archivo.

inputFile= open("datos.txt","r")
cadenas = inputFile.readlines()     #LEE TODO EL ARCHIVO
print(cadenas)

"""