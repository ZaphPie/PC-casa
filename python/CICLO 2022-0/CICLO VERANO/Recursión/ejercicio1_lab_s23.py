#Input: numdelTermino (int) 
#Output: termino (int) de la serie Fibonacci
def fibonacci(nt):
    if nt <2:
        return nt
    return fibonacci(nt-1)+fibonacci(nt-2)


#-----bloque principal--------------
numdelTermino = int(input("Numero del termino: "))
while numdelTermino<0:
    numdelTermino=int(input("Numero del termino: "))
print("El término de la serie Fibonacci es: ",  fibonacci(numdelTermino))
