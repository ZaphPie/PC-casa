#input: nota (float) se lee 4 notas por alumno, en total son 7 alumnos, se leeran 28 notas
#output: promedio de cada alumno (float)

for calumnos in range(1,8,1):
    print("Alumno número ",calumnos)
    suma = 0
    for cnotas in range(1, 5, 1):
        nota = float(input("Nota %d: "%(cnotas)))
        while nota<0 or nota >20:
            nota = float(input("Nota %d: "%(cnotas)))
        suma=suma+nota
    promedio = suma/4
    print("El promedio es %10.2f"%(promedio))
    print("--------------------------------")