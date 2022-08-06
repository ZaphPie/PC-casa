sumatotal = 0
nAprobados = 0

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
    sumatotal= sumatotal + promedio
    if promedio >=11:
        nAprobados = nAprobados + 1
    print("--------------------------------")
promedioDelSalon = sumatotal /7
print("El promedio del salón es: ", promedioDelSalon)
print("Número de Aprobados: ", nAprobados)
print("Numero de Desaprobados  : ", 7 - nAprobados)