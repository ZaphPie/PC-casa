n = int(input("Ingrese el primer número: "))
m = int(input("Ingrese el segundo número: "))
f = input("Ingrese la opción [a-b-c-d]: ")

if f == "a":
    print("El área del triángulo es:",(n*m)/2)
elif f == "b":
    print("El promedio es: ",(n+m)/2)
elif f =="c":
    if m ==0:
        print("m no puede ser 0")

    print("La división de los dos números es:", n/m)
elif f == "d":
    print("El mayor número es:",max(n,m))

