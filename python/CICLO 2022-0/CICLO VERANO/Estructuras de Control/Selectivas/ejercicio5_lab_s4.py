#Ejemplo 5
#Input: Denominación(int)
#Output: Mensaje(string)

den = int(input("Denominación: "))
if den == 1:
    print("George Washington")
elif den ==2:
    print("Thomas Jefferson")
elif den==5:
    print("Abraham Lincoln")
elif den==10:
    print("Alexander Hamilton")
elif den ==20:
    print("Andrew Jackson")
elif den== 50:
    print("Ulysses S. Grant")
elif den== 100:
    print("Benjamin Franklin")
elif den== 500 or den ==1000 or den==5000 or den==10000:
    print("Denominación descontinuada")
else:
    print("No existe esa denominación")
print("Adiós...")