"""
¿Qué es string?
Una cadena (string) es un tipo de dato en Python (str) que consiste en una secuencia ordenada de caracteres.
Una cadena contiene caracteres que pueden ser: letras números, signos de puntuación, espacios en blanco, caracteres especiales, etc.

Cadenas: Operaciones:
Concatenación (+)
Repetición (*)

Cadenas: Inmutables:
Los string en Python son inmutables. No pueden ser cambiados. No es válida una asignación.


Cadenas:Métodos:
str → casting
Cuando queremos utilizar un número como cadena debemos usar la función str() que convierte el valor numérico en una cadena de caracteres

len → Longitud
len encuentra el largo de un string o cantidad de caracteres

find → búsqueda
Permite determinar si un string está contenido en otro string. Retorna el índice donde comienza el string hallado.
Retorna -1 si el string no es encontrado
"La vida es mucho mejor con Python".find("Python")
>>27

replace → reemplazar
Reemplaza el string a buscar por el indicado.
"Mejor con Python".replace("Python","Jython")
>>"Mejor con Jython"

Capitaliza el primer carácter de la cadena.
capitalize()
Convierta la cadena en minúscula
lower()
Convierta la cadena en mayúscula
upper()
Elimina los espacios en blanco de los costados
strip()

Cadenas: Caracteres especiales y alineación

Retorno/Salto de linea -> \n

Tabulación -> \t

Alinear a la izquierda -> '{:100}'.format(s)
Alinear al centro -> '{:^100}'.format(s)
Alinear a la derecha -> '{:>100}'.format(s)

Cadena
join->unir
Devuelve una nueva cadena donde los valores de la cadena original que llama a join() aparecen separados por un caracter que fue pasado al join() como argumento.

"""

#Ejemplo:
pais = "Perú"
print(pais*20)
frase1 = "Campeón"
frase2 = pais + " "+ frase1
print(frase2)

