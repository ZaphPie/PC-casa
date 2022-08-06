#input: número (int)
#output: mensaje "Es primo" o "No es primo"
#---------------------------------------------
def esPrimo(num):
    if num ==1:
        return False
    for divisor in range(2,num,1):
        if num %divisor==0:
            return False
    return True





#---------------------------------------------

numero = int(input("Número: "))
while numero <1:
    numero = int(input("Número: "))
if esPrimo(numero):
    print("El número es primo!")
else:
    print("El número no es Primo!")