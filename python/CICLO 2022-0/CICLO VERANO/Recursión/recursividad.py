
def cuenta_regresiva(numero):
    numero -= 1
    if numero > 0:
        print(numero)
        cuenta_regresiva(numero)
    else:
        print("oo!")
#cuenta_regresiva(5)
def fibonacci(numero):
    if numero==0:
        return 1
    else:
        return numero*fibonacci(numero-1)
#print(fibonacci(4))
def maximo(l):
    if len(l)==1:
        return l[0]
    else:
        return max(l[0],maximo(l[1:]))
#print(maximo([3,8,2,13,7,5,1]))

#---------------------------------------------------------------------------
def nivel1_0(numero):
    '''CANTIDAD DE DIGITOS'''
    if numero == 0:
        return 0
    return 1 + nivel1_0(numero//10) 

def nivel1_1(numero):
    '''SUMA ARMONICA'''
    if numero==1:
        return 1
    else:
        return 1/numero + nivel1_1(numero-1)

def nivel1_2(numero):
    '''FACTORIAL'''
    if numero==0:
        return 1
    else:
        return numero * nivel1_2(numero-1)

def nivel1_3(numero,resto):
    '''FORMA DECRECIENTE '''
    if numero<1:
        print('Fin')
        return 0
    else:
        print(numero,end=' ')
        return numero-nivel1_3(numero-resto,resto)
    
def nivel1_4(numero,resto):
    '''POTENCIA DE UN NUMERO'''
    resto-=1
    if resto==-1:
        return 1
    else:
        return numero * nivel1_4(numero,resto)

print(nivel1_4(4,2))