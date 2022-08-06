#¿Cómo agregar datos?

#Agregar elementos uno a uno

people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

# crear un diccionario vacio "3" en el diccionario "people"
people[3] = {}

# agregar los pares key:value al diccionario "3"
people[3]['name'] = 'Luna'
people[3]['age'] = '24'
people[3]['sex'] = 'Female'
people[3]['married'] = 'No'
#Nuevo diccionario
print(people)
#Agregar un diccionario completo
# agregar nuevo diccionario
people[4] = {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}
print(people)