list = []
num = int(input("Numero : "))
list.append(num)
while True:
    num = int(input("Numero : "))
    if num==0:
        break
    else:
        list.append(num)
print("Lista leida: ",list)
print("Ahora se imprimen los elementos desde la posición del medio")
