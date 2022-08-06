#input: nota1,nota2, nota3 (float)
#output: promedio(float)

def promedio(n1,n2,n3):
    return (n1+n2+n3)/3
#---------------------------
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
prom = promedio(nota1, nota2, nota3) #invocando la función / transfiriendo variables nota1 ->n1 ; nota2 -> n2; nota3 ->n3  #copia del dato
print("El promedio es %10.2f"% (prom))


