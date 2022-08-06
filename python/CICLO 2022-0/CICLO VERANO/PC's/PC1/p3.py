lim = int(input("Limite: "))
numlin= int(input("Números por linea: "))

cont = 1
cdelinea = 1
while cont<=lim:
    print("%5d" %(cont),end="")
    cont = cont + 1
    if cdelinea== numlin:
        print()
        cdelinea = 1
    else:
        cdelinea = cdelinea + 1