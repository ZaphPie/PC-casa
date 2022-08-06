#Algoritmos de busqueda
def bubble_sort(lista):
    for tope in range(len(lista)-1, 0, -1):
        for i in range(tope):
            if lista[i]["dni"] > lista[i+1]["dni"]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
                

def imprimir(lista):
    print("[")
    for item in lista:
        print(item)
    print("]")
#-----------bloque principal

lista = [
    {"dni": "1234", "nombre": "Delsy Salinas",
     "edad": 19, "talla": 1.65, "peso": 68},
    {"dni": "2345", "nombre": "Juan Salazar",
     "edad": 23, "talla": 1.80, "peso": 80},
    {"dni": "6789", "nombre": "Sandra Flores",
     "edad": 34, "talla": 1.77, "peso": 77},
    {"dni": "4545", "nombre": "Lilian Pacheco",
     "edad": 17, "talla": 1.61, "peso": 57},
    {"dni": "2321", "nombre": "Paty Arce", "edad": 23, "talla": 1.60, "peso": 55},
    {"dni": "9867", "nombre": "Jose Villanueva",
     "edad": 18, "talla": 1.63, "peso": 58},
    {"dni": "9098", "nombre": "Carlos Diaz",
     "edad": 17, "talla": 1.73, "peso": 78},
    {"dni": "9790", "nombre": "Marilu Sanchez",
     "edad": 21, "talla": 1.59, "peso": 63},
    {"dni": "3436", "nombre": "Sergio Quiroz",
     "edad": 24, "talla": 1.89, "peso": 90},
    {"dni": "7643", "nombre": "Fabian Torres",
     "edad": 34, "talla": 1.64, "peso": 68},
    {"dni": "9954", "nombre": "Luis Castro",
     "edad": 33, "talla": 1.72, "peso": 89},
    {"dni": "2390", "nombre": "Edson Velasquez",
     "edad": 21, "talla": 1.73, "peso": 82},
    {"dni": "6543", "nombre": "Mariana Rosas",
     "edad": 29, "talla": 1.69, "peso": 70},
    {"dni": "6345", "nombre": "Mirian Perez",
     "edad": 18, "talla": 1.49, "peso": 62},
    {"dni": "9154", "nombre": "Juana Berrios",
     "edad": 17, "talla": 1.77, "peso": 70},
    {"dni": "9023", "nombre": "Eva Castro", "edad": 28, "talla": 1.72, "peso": 77},
    {"dni": "1414", "nombre": "Milagros Lam",
     "edad": 23, "talla": 1.68, "peso": 60},
    {"dni": "6734", "nombre": "Jorge Dongo",
     "edad": 15, "talla": 1.58, "peso": 53},
    {"dni": "8823", "nombre": "Luis Perales",
     "edad": 17, "talla": 1.72, "peso": 79},
    {"dni": "7732", "nombre": "Diana Fuentes",
     "edad": 24, "talla": 1.55, "peso": 59}
]
print("Las 5 personas mas bajas")
imprimir(lista)
print("")
print("Las 5 personas con mas peso")
bubble_sort(lista)
imprimir(lista)
