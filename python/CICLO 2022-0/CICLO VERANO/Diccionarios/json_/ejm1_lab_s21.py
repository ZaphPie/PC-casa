"JSON CON PYTHON"

import json
# Un objeto de tipo diccionario:
obj = {
    "nombre": "Nicolas Llerena",
    "edad": "18",
    "ciudad": "Lima"
}
# Guardar en un archivo JSON:
with open('data.json', 'w') as outfile:
    # convertir a JSON:
    json.dump(obj, outfile)
