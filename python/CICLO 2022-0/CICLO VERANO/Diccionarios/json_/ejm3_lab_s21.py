#También podemos usar el modulo para imprimir un JSON de manera más legible para los humanos.

import json
#Leer el archivo JSON
data = {'personas':[{'nombre':'Nicolas','email':'nicolas.llerena@utec.edu.pe','ciudad':'Lima'}]}

print(json.dumps(data,indent=4))