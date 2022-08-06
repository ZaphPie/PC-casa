# por otro lado, podemos extraer los datos de un archivo JSON hacia un objeto de tipo diccionario.

import json
# leer el archvio JSON
with open('D:\DESCARGAS\pythonn\CICLO 2022-0\CICLO VERANO\Diccionarios\Llave-Valor\data.json') as json_file:
    # llena un diccionario con los datos leídos
    data = json.load(json_file)
    print('Nombre: '+data['nombre'])
    print('Edad: '+str(data['edad']))
    print('Ciudad: '+data['ciudad'])
    print()
