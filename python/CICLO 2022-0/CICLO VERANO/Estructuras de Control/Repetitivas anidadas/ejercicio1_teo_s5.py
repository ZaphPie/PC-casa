#input: filas (int) filas >0 y filas <=9
#output: tríangulo con números

#----------------leemos el dato
filas = int(input("Fila [1 - 9] :"))
while filas <=0 or filas >=10:
    filas = int(input("Fila [1 - 9] :"))
print("Dato leído")
#-----------------dibujamos el tríangulo
print()
for f in range(1, filas+1):
    print(" "*(filas-f),end="")
    for cn in range(1,f+1):
        print(cn,end="")
    print("")
