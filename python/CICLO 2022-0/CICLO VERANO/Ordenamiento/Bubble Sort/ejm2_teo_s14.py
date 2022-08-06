import random as rd
def bubble_sort(lista):
    n_iter = 0
    for tope in range(len(lista)-1, 0, -1):
        for i in range(tope):
            n_iter += 1
            if lista[i] > lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
    return n_iter


def generate_list(n):
    random_list = []
    for i in range(n):
        n_random = rd.randint(0, n)
        random_list.append(n_random)
    return random_list


#-----------bloque principal----------
lista = generate_list(100)
n_iter = bubble_sort(lista, e)
