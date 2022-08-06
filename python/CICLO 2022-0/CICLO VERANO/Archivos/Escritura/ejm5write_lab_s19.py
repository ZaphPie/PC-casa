#-------------------------------------------------------------
#-- Datos de entrada: n (int), nombre del archivo (str)
#-- Dato de salida : un archivos con los numeros pares desde
#                    cero hasta n
#--------------------------------------------------------------

nombredelArchivo = input("Nombre físico del archivo: ")
n=int(input("Numero : "))

miArchivo=open("./"+nombredelArchivo,"w")
for item in range(0,n+1,2):
    miArchivo.write(str(item)+"\n")
miArchivo.close()