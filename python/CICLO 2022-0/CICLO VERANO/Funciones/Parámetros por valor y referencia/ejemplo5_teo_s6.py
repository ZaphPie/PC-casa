#input: limite(int)
#output: todos los números primos desde el 2 hasta límite
#--------------------------------------------------------
def esPrimo(num):
    if num==1:
        return False
    divisor = 2
    while divisor < num:
        if num % divisor == 0:
            return False
        divisor = divisor + 1
    return True

#--------------------------------------------------------
limite =int(input("Limite: "))
while limite<2:
    limite = int(input("Limite: "))
print()
for cont in range(2, limite+1,1):
    if esPrimo(cont):
        print(cont)
print("\nFin.")