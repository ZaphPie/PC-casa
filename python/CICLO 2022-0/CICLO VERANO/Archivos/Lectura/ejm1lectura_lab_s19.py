miArchivo = open("./trabalenguas.txt","r")
for unaLinea in miArchivo:
    print(unaLinea.rstrip("\n")) # print(unaLinea, end="")
miArchivo.close() #IMPORTANTE CERRAR EL ARCHIVO:  EL OS CIERRA EL ARCHIVO.

"""
miArchivo = open("./trabalenguas.txt","r")
for unaLinea in miArchivo:
    print(unaLinea, end="")
miArchivo.close() #IMPORTANTE CERRAR EL ARCHIVO:  EL OS CIERRA EL ARCHIVO.

"""