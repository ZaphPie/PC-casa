#Ejemplo 4
#Input: edad(int)
#Output: precio(float)

edad= int(input("Edad: "))
if edad < 0 or edad > 115:
    print("La edad es incorrecta!")
elif edad<=17:
    print("El precio es 15")
elif edad<=30:
    print("El precio es 25")
elif edad<=45:
    print("El precio es 30")
else:
    print("El precio es 10")
print("Adiós...")


