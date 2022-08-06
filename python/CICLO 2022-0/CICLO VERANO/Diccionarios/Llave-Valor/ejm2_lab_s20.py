diccionario = {
    "20212345":"Ana Torres",
    "202123499":"Daniel Ore",
    "202178654":"Yenifer Yucra",
    "202134123":"Richard Pareja"
}
print(diccionario)
diccionario["202133333"]="Fernando Trelles"
print(diccionario)
print(diccionario["202123499"])
#--- recorrer el diccionario
print("")
for elem in diccionario:
    print("%12s %-15s"%(elem,diccionario[elem]))
print("Las claves: ", diccionario.keys())
print("Los valores asociados a las claves: ",diccionario.values())
