#Invertir un número
#Input: número(int) -> El número es de 3 digitos
#Output: número invertido (int)

numero= int(input("Número: "))
unidades= numero %10
decenas= numero//10%10
centenas=numero//100
ni= unidades *100 + decenas *10 +centenas
print("El número invertido es: ",ni)