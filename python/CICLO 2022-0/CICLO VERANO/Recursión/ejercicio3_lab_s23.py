#Input:n1,n2 (int) n1>0 y n2>0
#Output: producto (int) pero utilizando una función recursiva

def producto(n1,n2):
    if n2==1:
        return n1
    return n1+ producto(n1,n2-1)


#-----Bloque principal-----------
n1 = int(input("Numero 1: "))
while n1 <1:
    n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))
while n2<1:
    n2 = int(input("Numero 2: "))
print("El producto es: ",producto(n1,n2))