#Uso del Operador = en Listas

#El operador = no copia una lista a otra. Este operador lo que hace es crear una variable que referencie a los mismos datos. Así, si es que se modifican los datos desde cualquiera de las dos variables involucradas, estos cambios se verán reflejados en ambas.

lista_numeros = [1,2,3,4,5,6,7,8,9,10]
lista_puntero = lista_numeros
print(lista_puntero)
lista_numeros[2]=22
lista_numeros[4]=44
print(lista_puntero)
#[1,2,3,4,5,6,7,8,9,10]
#[1,2,22,4,44,6,7,8,9,10]