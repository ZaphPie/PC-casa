"""
Parámetros por defecto:
Python permite declarar parámetros con valor por defecto. Si se invoca la función sin este parámetro, éste toma el valor por defecto que le fue asignado.
El valor por defecto es asignado al parámetro haciendo uso del operador de asignación =


Es importante siempre tener presente los siguientes puntos cuando se invoca a funciones:

1. En caso se utilice keyword-> el orden de los parámetros no es importante 
2. Únicamente debe haber un valor para cada parámetro.
3. El nombre de los parámetros debe coincidir cuando se utilice keyword
4. En caso se invoque a la función sin keyword -> el orden en que se pasen los parámetros es importante.

"""

#EJEMPLO
def estudiante(nombre, apellido="Rodriguez", standard="Quinto"): #La función tiene un parámetro obligatorio (nombre), y dos opcionales (apellido y standard)
    print(nombre,apellido,"estudia en",standard,"standard")