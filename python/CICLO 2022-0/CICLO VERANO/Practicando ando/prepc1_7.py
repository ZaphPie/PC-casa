a = float(input("Ingrese el valor del primer producto: "))
if a<0:
    a = float(input("Por favor ingrese un precio correcto para el primer producto: "))
b = float(input("Ingrese el valor del segundo producto: "))
if b<0:
    b= float(input("Por favor ingrese un precio correcto para el segundo producto: "))
c = float(input("Ingrese el valor del tercer producto: "))
if c<0:
    c=float(input("Por favor ingrese un precio correcto para el tercer producto: "))

suma = a + b + c

if suma >500:
    suma = suma - (suma)*(3/20)
    print("El total (aplica descuento) es:", round(suma,2))
elif 200<suma<500:
    suma = suma - (suma)*(1/20)
    print("El total (aplica descuento) es:", round(suma,2))
else:
    print("El total (no aplica descuento) es:", round(suma,2))


