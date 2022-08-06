# Ahora consumiremos datos desde un servicio web (API) usando Python.

import requests
import json

# parametro
name = "Nicolas"

# url del API REST
url = "https://api.nationalize.io/?name=" + name

# invoca el servicio web
# se recibe en un diccionario
result = requests.get(url).json()

# muestra el resultado
print(json.dumps(result, indent=4))
