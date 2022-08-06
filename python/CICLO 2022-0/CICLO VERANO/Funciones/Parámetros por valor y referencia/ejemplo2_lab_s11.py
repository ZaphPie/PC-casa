#Input: número (int) -> numero > 1000
#Output: Mensaje "Es capicua" o "No es capicua"

def alReves(num):
    numInv = 0
    while num>0:
        digito = num%10
        numInv = numInv *10 +digito
        num = num //10
    return numInv




#-------------------------------------------------
numero = int(input("Número [mayor a 1000]: "))
while numero<=1000:
    numero = int(input("Número [mayor a 1000]: "))
ni = alReves(numero)
if numero ==ni:
    print("El número es capicua")
else:
    print("El número no es capicua")