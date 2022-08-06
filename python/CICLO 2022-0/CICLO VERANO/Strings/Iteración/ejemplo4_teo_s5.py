#Input: palabra (str)
#Output: indica si la palabra es palíndromo

palabra = input("Palabra: ")
alreves=""
pos = len(palabra)-1 #corre de la última posición a la primera
while pos>=0:
   alreves = alreves + palabra[pos]
   pos = pos - 1
if palabra == alreves:
   print("Es palíndromo")
else:
   print("No es palíndromo")
