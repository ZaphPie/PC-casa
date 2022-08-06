#Ejemplo 1

#Input: edad(int)
#Output: Mensaje(string) -> "Es mayor de edad" o "Es menor de edad"


edad=int(input("Edad: "))
if edad < 18:
    print("Es menor de edad")
if edad >= 18:
    print("Es mayor de edad")
print("Adiós...")

#NOTA: mientras menos condiciones hayan, será mejor