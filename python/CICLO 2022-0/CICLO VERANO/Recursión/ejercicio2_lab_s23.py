#Input: numdelTermino (int)
#Output: Todos los términos desde 0 hasta numdeltermino de la serie Fibonacci

def fibonacci(nt):
    if nt<2:
        return nt
    return fibonacci(nt-1)+fibonacci(nt-2)


#---------Bloque principal------------
numdelTermino=int(input("Numero del termino: "))
while numdelTermino <0:
    numdelTermino = int(input("Numero del termino: "))
#----------armamos la tabla
print("%20s  %15s" % ("Num del termino", "Termino"))
for cont in range(0, numdelTermino+1, 1):
    print("%20d  %15d" % (cont, fibonacci(cont)))
