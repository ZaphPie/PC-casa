"""
Dado el texto = "10,20,33,40,11,90"

Escribir un programa que genere una lista con los 6 valores numéricos
incluidos en el texto y luego calcular la suma de aquellos valores
múltiplos de 10.

"""

texto = "10,20,33,40,11,90"
lista1 = texto.split(",")
print(lista1)
l2 = [int(elem) for elem in lista1 if int(elem) % 10 == 0]
print(sum(l2))
