#input: número (int)
#output: mensaje "Es primo" o "No es primo"
#---------------------------------------------
def esPrimo(num):
    if num==1:
        return False
    divisor = 2
    while divisor < num:
        if num % divisor == 0:
            return False
        divisor = divisor + 1
    return True
#---------------------------------------------

numero = int(input("Número: "))
while numero <1:
    numero = int(input("Número: "))
if esPrimo(numero):
    print("El número es primo!")
else:
    print("El número no es Primo!")