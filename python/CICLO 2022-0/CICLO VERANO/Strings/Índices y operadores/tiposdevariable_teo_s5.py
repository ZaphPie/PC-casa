"""
¿Qué es una variable?
Un valor con nombre, que potencialmente se puede cambiar a medida que se ejecuta el programa
Almacena difentes tipos de datos

¿Dónde se almacena?
Las variables de un programa son almacenadas con la ayuda del Sistema Operativo en la memoria RAM de un computador.

¿Qué es un string?
Un string o cadena es uan secuencia de caracteres
"""
import sys
#EJEMPLO 1
print("EJEMPLO 1:")
print()
pc1 = 18
pc2= 16
pc3= 20
print("pc1: ",pc1)
print("pc2: ",pc2)
print("pc3: ",pc3)
print()
input("ID:")
print(id(pc1))
print(id(pc2))
print(id(pc3))
print()
input("Size:")
print(sys.getsizeof(pc1),"bytes")
print(sys.getsizeof(pc2),"bytes")
print(sys.getsizeof(pc3),"bytes")

input("-----------------------------------")
#EJEMPLO 2:
print("EJEMPLO 2")
print()
deletrea1= 'U'
deletrea2= 'UT'
deletrea3= 'UTE'
deletrea4= 'UTEC'
print("d1",deletrea1)
print("d2",deletrea2)
print("d3",deletrea3)
print("d4",deletrea4)
print()
input("ID:")
print(id(deletrea1))
print(id(deletrea2))
print(id(deletrea3))
print(id(deletrea4))
print()
input("SIZE:")
print(sys.getsizeof(deletrea1),"bytes")
print(sys.getsizeof(deletrea2),"bytes")
print(sys.getsizeof(deletrea3),"bytes")
print(sys.getsizeof(deletrea4),"bytes")