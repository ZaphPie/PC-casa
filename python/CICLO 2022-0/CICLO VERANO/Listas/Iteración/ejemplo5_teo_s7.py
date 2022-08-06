#Input: numdeNotas(int), notas(float)
#Output: promedio(float) eliminando la más baja

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
#-------------Hallamos la nota más baja
menorNota= None
for i in range(0,len(notas),1):
    if menorNota ==None or notas[i]<menorNota:
        menorNota=notas[i]
prom=(suma-menorNota)/(len(notas)-1)
print("El promedio eliminado la menor nota es:", prom)
#------------------Segunda manera
input("-----------2-------------------")
promedio = (sum(notas) - min(notas))/(len(notas)-1)
print("El promedio es: ", promedio)
