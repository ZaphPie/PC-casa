"""
¿Cómo eliminar datos?

- Python permite eliminar datos de tres maneras:
1. A través de la clave
2. Eliminando únicamente un par
3. Eliminando toda la información del diccionario y eliminando completamente el diccionario(como variable).

"""

#EJEMPLO:

d = {'nombre':'Zara','edad':7,'clase':'First'}
del d['nombre'] #elimina par con clave 'nombre'
d.clear()   #elimina todos los datos del diccionario
del d   #elimina el diccionario
print("d['edad']: ",d['edad'])
print("d['colegio']:",d['colegio'])
