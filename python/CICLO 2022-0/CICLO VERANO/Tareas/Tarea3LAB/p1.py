def imprimir(lista):
    print("[")
    for item in lista:
        print(item)
    print("]")
def nuevaLista(lista):
    nuevaLista=[]
    for d in lista:
        undiccionario={}
        undiccionario["codigo"]=d["codigo"]
        undiccionario["notas"]=sum(d["notas"])/len(d["notas"])
        nuevaLista.append(undiccionario)
    return nuevaLista


#----------------
sec201 = [
    {"codigo": "202120084", "nombre": "Yuli Apaza",
        "notas": [12, 14, 15, 13, 9]},
    {"codigo": "202120627", "nombre": "Tamara Aquino",
        "notas": [18, 15, 15, 12, 18, 9]},
    {"codigo": "202120087", "nombre": "Drussila Aranda",
        "notas": [19, 18, 16]},
    {"codigo": "202120376", "nombre": "Ivan Malpartida",
        "notas": [19, 15, 13, 14, 15, 16, 17, 20, 20]},
    {"codigo": "202120339", "nombre": "Anderson Malca",
        "notas": [12, 16, 19, 20]},
    {"codigo": "202120329", "nombre": "Eduardo Gordillo",
        "notas": [13, 20, 16, 17, 12, 15, 14]},
    {"codigo": "202120333", "nombre": "Andra Gamboa",
        "notas": [20, 18]}


]

print("Nueva Lista")
nl=nuevaLista(sec201)
imprimir(nl)