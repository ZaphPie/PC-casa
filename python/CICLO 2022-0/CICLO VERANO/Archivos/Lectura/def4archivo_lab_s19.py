"""
¿Cómo leer los datos de un archivo?
- La manera más sencilla de leer un archivo es usando la sentencia for:

for <cadena_linea> in <objeto_archivo>:
    <sentencias>
    
- La lectura se realiza dentro del cuerpo del bucle.
- Cada iteración del bucle leerá una línea del archivo en un string:
inputFile= open("datos.txt","r")
for cadena in inputFile:
    print(cadena)
- Considerar que al leer el archivo, también se lee el carácter de fin de línea.
"""