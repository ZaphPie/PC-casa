
def esPrimo(numero):
    if numero==1:
        return False
    for divisor in range(2,numero,1):
        if numero%divisor==0:
            return False
    return True

#----------------------------------------------------------------
milista=[]
numero=int(input("Número [ 0 termina] : "))
while numero!=0:
    milista.append(numero)
    numero=int(input("Número [ 0 termina ] : "))
print(milista)

listadePrimos=[]
listadeNoPrimos=[] 

for dato in milista:
    if esPrimo(dato):
        listadePrimos.append(dato)
    else:
        listadeNoPrimos.append(dato)
if len(listadePrimos)==0:
    print("No se ha ingresado un número primo")
else:
    print("Lista de primos: ", listadePrimos)
    print("Lista de no primos: ", listadeNoPrimos)