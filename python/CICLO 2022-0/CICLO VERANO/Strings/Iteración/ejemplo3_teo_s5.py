#---------------------------------------------
# Dato de entrada: frase (str)
# Dato de Salida : imprime la frase al reves
#--------------------------------------------
#---- ahora formamos una cadena nueva
frase = input("Frase: ")
nuevaCadena = ""
pos = len(frase)-1
while pos>=0:
   nuevaCadena = nuevaCadena + frase[pos]
   pos = pos -1
print("Cadena al reves: ", nuevaCadena)