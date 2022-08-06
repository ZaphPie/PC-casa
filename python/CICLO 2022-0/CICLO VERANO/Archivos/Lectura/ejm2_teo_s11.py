"""
Lee información del archivo texto llamado refranes.txt que se encuentra en el directorio por default
Y lo muestra en pantalla.
"""
#Input: No hay
#Output: Mostramos la información del archivo
#----------------------------------------------------

myFile=open("./refranes.txt","r")
for unaLinea in myFile:
    print(unaLinea)
myFile.close()
print()
#SOLUCIÓN 2:
miFile = open("./refranes.txt", "r")
unaLinea = miFile.readline()
while unaLinea!="":
   print(unaLinea,end="")
   unaLinea = miFile.readline()
miFile.close()
print()
#SOLUCIÓN 3:
maiFile=open("./refranes.txt","r")
todo=maiFile.readlines() #Lee todo el archivo, devuelve una lista
for unaLinea in todo:
   print(unaLinea.rstrip("\n"))
maiFile.close()

