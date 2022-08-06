"""
Ubicar un objeto dentro de un conjunto de elementos
"""

def linear_search(lista,e):
    for i in range(len(lista)):
        if lista[i]==e:
            return True
    return False
    
lista = [10,14,19,26,27,31,33,35,42,44]
result = linear_search(lista,33)#result = True
print(result)