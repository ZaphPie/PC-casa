#input: número (int)
#output: factorial

def factorial(num):
    fact = 1
    for cont in range(2, num+1,1):
        fact =fact * cont
    return fact
#----------------------------------
numero = int(input("Número: "))
print("El factorial es: ", factorial(numero))
print("Fin.")