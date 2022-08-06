#EJERCICIO 1:

print("Fecha de nacimiento")
dia1=int(input("Dia: "))
mes1=int(input("Mes: "))
año1=int(input("Año: "))
print("Fecha actual")
dia2=int(input("Dia: "))
mes2= int(input("Mes: "))
año2= int(input("Año: "))
print()
restadia=dia2-dia1
restames=mes2-mes1
restaaño=año2-año1
if restames<0:
    restaaño=restaaño-1
elif restames==0:
    if restadia>0:
        restaaño =restaaño-1
print("Su edad es",restaaño)

if restaaño<0 or restaaño > 116:
    print("Ha ingresado un dato no válido")
else:
    if restaaño<13:
        print("Su generación aun no tiene nombre asignado")
    elif restaaño<=20:
        print("Su generación es la Generación Z")
    elif restaaño<= 35:
        print("Su generación es la Generación Y")
    elif restaaño<= 59:
        print("Su generación es la Generación X")
    else:
        print("Su generación es la Generación Baby Boomers")





