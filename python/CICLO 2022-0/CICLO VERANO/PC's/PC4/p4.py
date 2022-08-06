def busquedaBinaria(lista, dato):
    izq = 0
    der = len(lista)-1
    encontrado = False
    while (izq <= der) and not encontrado:
        medio = (izq + der)//2
        if lista[medio]['region'] == dato:
            encontrado = True
        else:
            if dato < lista[medio]['region']:
                der = medio - 1
            else:
                izq = medio + 1
    if encontrado:
        return medio
    else:
        return -1


def imprimir(lista):
    print("[")
    for item in lista:
        print(item)
    print("]")


#----------------------------------------------------------------
lista = [

    {" region ": " Amazonas ", " vacunados ": 39801},
    {" region ": " La Libertad ", " vacunados ": 269996},
    {" region ": " Lambayeque ", " vacunados ": 174088},
    {" region ": " Ica ", " vacunados ": 123644},
    {" region ": " Junin ", " vacunados ": 200466},
    {" region ": " Madre de Dios ", " vacunados ": 12380},
    {" region ": " Moquegua ", " vacunados ": 38560},
    {" region ": " Ancash ", " vacunados ": 175488},
    {" region ": " Apurimac ", " vacunados ": 51561},
    {" region ": " Tacna ", " vacunados ": 78894},
    {" region ": " Tumbes ", " vacunados ": 27503},
    {" region ": " Arequipa ", " vacunados ": 294325},
    {" region ": " Callao ", " vacunados ": 305542},
    {" region ": " Huanuco ", " vacunados ": 60471},
    {" region ": " Lima ", " vacunados ": 2516347},
    {" region ": " Loreto ", " vacunados ": 84279},
    {" region ": " Pasco ", " vacunados ": 29754},
    {" region ": " Piura ", " vacunados ": 193003},
    {" region ": " Puno ", " vacunados ": 84724},
    {" region ": " Ayacucho ", " vacunados ": 72996},
    {" region ": " Cajamarca ", " vacunados ": 156021},
    {" region ": " San Martin ", " vacunados ": 79341},
    {" region ": " Ucayali ", " vacunados ": 36590},
    {" region ": " Cusco ", " vacunados ": 140218},
    {" region ": " Huancavelica ", " vacunados ": 41175},
]
region = input("Departamento: ")
posicion = busquedaBinaria(lista, region)
if posicion != -1:
    print(lista[posicion])
else:
    print("La region no existe")
