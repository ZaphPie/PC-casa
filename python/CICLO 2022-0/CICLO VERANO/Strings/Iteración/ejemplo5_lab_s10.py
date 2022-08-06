#input: frase (str)
#output: imprimir solo los caracteres de posiciones pares

frase = input("Frase: ")
for i in range(0, len(frase),2): #antes era 1
    #if i %2==0:
    print(frase[i])
#print("-----SOLUCIÓN 2------")
#for j in range(0, len(frase), 2):
  #  print(frase[i])
