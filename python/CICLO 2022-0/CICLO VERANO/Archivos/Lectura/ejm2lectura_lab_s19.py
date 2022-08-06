archivo = open("./Documentos/trabalenguas2.txt","r")
linea =archivo.readline()
while linea != "": #cadena vacía
    print(linea,end="")
    linea =archivo.readline()
archivo.close()