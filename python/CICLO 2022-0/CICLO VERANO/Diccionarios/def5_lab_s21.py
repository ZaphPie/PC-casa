#¿Cómo eliminar datos?
#Eliminando un diccionario usando el comando "del"
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female'},
          4: {'name': 'Peter', 'age': '29', 'sex': 'Male'}}

# eliminar diccionario "3" y "4"
del people[3], people[4]
print(people)
print("--------------------------------")
#Eliminando un elemento del diccionario interno

people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'},
          4: {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}}

# se elimina la propiedad "married"
del people[3]['married']
del people[4]['married']
print(people)