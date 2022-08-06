#SOLUCIÓN 2-> De manera recursiva

def factorial(num):
    if num==1 or num==0:
        return 1
    return num*factorial(num-1)


num = int(input("Número: "))
while num < 0:
    num = input("Número:")
print("El factorial es: ", factorial(num))
