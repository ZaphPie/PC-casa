#Ejemplo 3
#Input: número(int)
#Output: mensaje ->día de la semana (string)

numero= int(input("Número: "))
if numero ==1:
    print("Lunes")
elif numero ==2:
    print("Martes")
elif numero ==3:
    print("Miércoles")
elif numero==4:
    print("Jueves")
elif numero==5:
    print("Viernes")
elif numero==6:
    print("Sábado")
elif numero==7:
    print("Domingo")
else:
    print("No corresponde a un día de la semana!!")
print("Adiós...")