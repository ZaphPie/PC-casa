#Input: edad(int)
#Output: mensaje(str)

edad=int(input("Edad: "))
if edad<0 or edad > 116:
    print("Ha ingresado un dato no válido")
else:
    if edad<13:
        print("Su generación aún no tiene nombre")
    elif edad<=20:
        print("Su generación es la Z")
    elif edad<= 35:
        print("Su generación esla Y")
    elif edad<= 59:
        print("Su generación es la X")
    else:
        print("Su generación es la Baby Boomers")
print("Adiós...")