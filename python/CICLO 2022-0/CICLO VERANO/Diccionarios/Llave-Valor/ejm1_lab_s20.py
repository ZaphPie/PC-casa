d = {"nombre":"Zara",
     "edad":7,
     "clase":"primero"
     }
print(d)
d["talla"]=1.48
d["peso"]=51
print(d)
d["peso"]=d["peso"]+10
print(d)
d["nombre"]="Dania"
print(d)

"""
{'nombre': 'Zara', 'edad': 7, 'clase': 'primero'}
{'nombre': 'Zara', 'edad': 7, 'clase': 'primero', 'talla': 1.48, 'peso': 51}
{'nombre': 'Zara', 'edad': 7, 'clase': 'primero', 'talla': 1.48, 'peso': 61}
{'nombre': 'Dania', 'edad': 7, 'clase': 'primero', 'talla': 1.48, 'peso': 61}

"""

