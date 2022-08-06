#Input: numdeNotas(int), notas(float)
#Output: promedio(float)

numdeNotas=int(input("Número de notas: "))
notas=[]
i = 1
suma =0
while i<=numdeNotas:
    nota=float(input("Nota % d :"% (i)))
    while 0<nota>20:
        nota=float(input("Nota % d :"% (i)))
    notas.append(nota)
    suma+=nota
    i = i+1
print(notas)
prom = suma/len(notas)
print("El promedio es  %10.2f " % (prom))
