#Input: num (int) ; num>=0
#Output: factorial

#SOLUCIÓN 1-> de manera iterativa
def factorial(numero):
    f=1
    for cont in range(2, numero+1,1):
        f*=cont
    return f

num = int(input("Número: "))
while num <0:
    num=input("Número:")
print("El factorial es: ", factorial(num))