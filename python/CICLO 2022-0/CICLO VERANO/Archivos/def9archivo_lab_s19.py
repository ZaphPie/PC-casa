"""
Cerrando un archivo: close()
Para cerrar un archivo, se utiliza la función close():
<objeto_archivo>.close()

- Un archivo se cierra automáticamente al finalizar el programa. Sin embargo, es una buena práctica cerrarlo explícitamente cuando el programa dejará de usarlo.
- En caso exista un error en el programa y el archivo haya quedado abierto, es posible que este permanezca bloqueado y no pueda ser utilizado. 

inputFile = open("datos.txt","r")
cadenas = inputFile.readlines()
print(cadenas)
inputFile.close()
"""