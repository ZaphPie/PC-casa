#input: numero(int) numero>1
#output: se deletrea el número (str)
#----------------------------------------------------------------
def nombreDelDigito(n):
    if n == 0:
        return("cero")
    elif n ==1:
        return("uno")
    elif n ==2:
        return("dos")
    elif n ==3:
        return("tres")
    elif n ==4:
        return("cuatro")
    elif n ==5:
        return("cinco")
    elif n ==6:
        return("seis")
    elif n ==7:
        return("siete")
    elif n ==8:
        return("ocho")
    else:
        return("nueve")

def deNumeroaCadena(num):
    frase=""
    while num>0:
        digito = num %10
        frase = nombreDelDigito(digito) +frase
        num = num//10
    return frase
#----------------------------------------------------------------
numero= int(input("Número [mayor a 1]: "))
while numero <=1:
    numero = int(input("Número [mayor a 1]: "))
cadena = deNumeroaCadena(numero)
print(cadena)