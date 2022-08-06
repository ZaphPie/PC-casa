"""
#1
#input: num(int) -> num>10
#output: sigPrimo,antPrimo (int)
#--------------------------------------------------------
def esPrimo(num):
    if num == 1:
        return False
    divisor = 2
    while divisor < num:
        if num % divisor == 0:
            return False
        divisor = divisor + 1
    return True


def siguientePrimo(numero):
    cont = numero + 1
    while not(esPrimo(cont)):
        cont = cont + 1
    return cont


def anteriorPrimo(numero):
    cont = numero - 1
    while not(esPrimo(cont)):
        cont = cont - 1
    return cont


#--------------------------------------
num = int(input(""))

print("Siguiente numero primo", siguientePrimo(num))
print("Anterior numero primo", anteriorPrimo(num))

#2
#Input: número (int) -> numero > 1000
#Output: Mensaje "Es capicua" o "No es capicua"


def alReves(num):
    numInv = 0
    while num > 0:
        digito = num % 10
        numInv = numInv * 10 + digito
        num = num // 10
    return numInv


#-------------------------------------------------
numero = int(input(""))

ni = alReves(numero)
if numero == ni:
    print("Es capicua")
else:
    print("No es capicua")

#3
dia=int(input(""))
mes= input("").lower()
if mes=="enero"or mes== "febrero"or mes=="marzo" or mes=="abril":
    if dia %2==0:
        print("Esmeralda")
    else:
        print("Zafiro")
if mes == "mayo" or mes == "junio" or mes == "julio" or mes == "agosto":
    if dia%2==0:
        print("Rubi")
    else:
        print("Topacio")
elif mes == "setiembre" or mes == "octubre" or mes == "noviembre" or mes == "diciembre":
    if dia % 2 == 0:
        print("Amatista")
    else:
        print("Jade")


#4
def masLargo(lista):
    palabra_longitud=[]
    for p in lista:
        palabra_longitud.append((len(p),p))
    palabra_longitud.sort()
    return palabra_longitud[-1][1]
#---------------------
n=int(input())
cont = 1
l=[]
while cont<=n:
    a=input()
    l.append(a)
    cont+=1
print(masLargo(l))
"""
# 5

print("Juan")
print("Maria")
print("Rosa")