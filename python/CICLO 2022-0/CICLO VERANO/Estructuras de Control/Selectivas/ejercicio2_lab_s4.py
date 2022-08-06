#Ejemplo 2
#Input: número(int)
#Output: mensaje(string)

numero=int(input("Número: "))
if numero== 0:
    print("El número es cero")
elif numero%2==0:
    print("El número es par")
else:
    print("El número es impar")
print("Adiós...")