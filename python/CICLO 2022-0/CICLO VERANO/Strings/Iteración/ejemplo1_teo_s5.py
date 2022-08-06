#-----------------------------------
# Dato de entrada: frase (str)
# Dato de Salida : num (int)
#-----------------------------------

frase = input("Frase:")
numA = 0
i =0
while i <len(frase):
   if frase[i]=="A"  or frase[i]=="a":
       numA= numA + 1
   i = i + 1
print("Numero de veces que aparece la letra a o A : ", numA)