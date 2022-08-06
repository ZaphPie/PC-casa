#Realice un programa que imprima los números desde el 1 al 1000
#Pero indicando al costado si el número es primo
#
#Input: No tiene
#Output: Lista de números desde el 1 al 1000 indicando cuales son primos
#           SUMA DE LOS PRIMOS
#

suma = 0
for contador in range(1,1001,1):
    if contador ==1:
        print(contador)
    else:
        esPrimo = True
        for divisor in range(2, contador, 1):
            if contador % divisor == 0:
                esPrimo = False
        if esPrimo:
            print(contador,"Es Primo")
            suma = suma +contador
        else:
            print(contador)
print("\nLa suma de todos los números primos desde 1 al 1000 es: ",suma)
print("Adiós...")
