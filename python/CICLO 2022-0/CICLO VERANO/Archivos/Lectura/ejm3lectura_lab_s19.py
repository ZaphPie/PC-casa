miFile =open("./Documentos/trabalenguas2.txt","r")
todo = miFile.readlines()
for elemento in todo:
    print(elemento.rstrip("\n")) 
miFile.close()