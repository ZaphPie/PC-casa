#INPUT: edad(int)
#OUTPUT: mensaje(str) "Eres mayor de edad" o "Eres menor de edad"

edad = int(input("Edad: "))
rpta = edad>=18
print(rpta*"Eres mayor de edad" + (not(rpta))*"Eres menor de edad")