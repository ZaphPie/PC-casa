#Realice un programa que lea un número y el programa
#Indique si es un número primo o no lo es
#
#Input:num(int)
#Output: Mensaje"Es primo", "No es primo"

num = int(input("Número: "))
if num ==1:
    print("El",num," es Primo")
else:
    esPrimo= True
    for divisor in range(2,num,1):
        if num%divisor ==0:
            esPrimo = False
    if esPrimo:
        print("El",num," es Primo")
    else:
        print("El",num,"no es Primo")

