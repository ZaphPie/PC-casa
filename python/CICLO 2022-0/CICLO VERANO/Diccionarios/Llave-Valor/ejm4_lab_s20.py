"""
Desarrolle un programa que permita registrar en un diccionario el DNI y el nombre de varias personas. El ingreso de datos termina cuando se ingresa la palabra “fin”. Note entonces que el DNI sera una cadena.
Luego el programa permita buscar el nombre de una persona según el DNI.


"""


#-----------------------------------------------
# Dato de entrada:  DNI (str), nombre (str)
# Dato de salida : diccionario
#-----------------------------------------------
dic={}
dni = input("DNI: ")
while dni !="fin":
    nombre = input("Nombre: ")
    if dni not in dic:
        dic[dni]=nombre #### esta insertando la pareja de valores en el diccionario (NO FUNCIÓN APPEND)
    dni = input("DNI: ")
print(dic)
#-----buscamos ene el diccionario según el dni
print()
dato=input("DNI a buscar: ")
if dato in dic:
    print("El valor asociado a esa clave es: ",dic[dato])
else:
    print("El dato no existe en el diccionario")