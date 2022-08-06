#Input: n (int) n>=1
#Output: suma de los cuadrados
def sumaDeCuadrados(n):
    if n==1:
        return 1
    return n*n +sumaDeCuadrados(n-1)


#-----------Bloque principal
n = int(input("Numero : "))
while n < 1:
    n = int(input("Numero : "))
print("La suma de los cuadrados desde 1 hasta",n,"es: ", sumaDeCuadrados(n))