lista = [12,13,14,15,16,17]
listacopia = lista.copy()
print(listacopia)
lista[2]=114
print("Lista",lista)
print("Listacopia", listacopia) #NO ALTERA LA LISTA AUXILIAR
print("SEGUNDO CASO")
l3= ["Lunes","Martes","Miércoles","Jueves","Viernes"]
diasLaborables=l3[:] #USANDO LOS SLICE / COPIAMOS LISTA
print(diasLaborables)
