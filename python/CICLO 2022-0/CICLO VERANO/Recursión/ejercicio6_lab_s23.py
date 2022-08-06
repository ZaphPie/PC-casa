#Input: numero (int) numero >0
#Output: sumadeDigitos
def sumadeDigitos(num):
    if num<=9:
        return num
    return num%10 +sumadeDigitos(num//10)


#--------Bloque principal

numero = int(input("Numero :"))
while numero <1:
    numero =int(input("Numero: "))
print("La suma de los digitos es: ",sumadeDigitos(numero))