#----------------------------
#Input: Número (int) número>0
#Output: nDigitos (int)
#----------------------------
def cuentaDigitos(num):
    cd=0
    while num>0:
        digito=num%10
        cd+=1
        num=num//10
    return cd



#-----------------------------
numero = int(input("Número: "))
while numero<=0:
    numero = int(input("Número: "))

print("El número tiene %d digitos" % (cuentaDigitos(numero)))
