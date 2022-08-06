#input: nombredelArchivo (str), num(int)
#output: Graba en el archivo números pares desde el cero hasta num
#-----------------------------------------------------------------

nombreFisico=input("Nombre del archivo: ")
numero = int(input("Numero: "))

miFile = open("./" + nombreFisico, "w")
for num in range(0,numero+1,2):
   miFile.write( str(num) + "\n")
miFile.close()
