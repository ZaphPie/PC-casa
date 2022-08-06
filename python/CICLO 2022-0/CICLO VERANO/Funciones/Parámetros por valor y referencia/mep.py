dia = int(input("Dia: "))
mes = int(input("Mes: "))
año = int(input("Año: "))

def hallaDias(dia, mes, año):
    result = 0
    while mes != 13:
        if mes in [1, 3, 5, 7, 8, 10, 12]:
            dias = 31
        elif mes in [4, 6, 9, 11]:
            dias = 30
        else:
            if año % 4 == 0:
                dias = 29
            else:
                dias = 28
        result += dias
        mes+=1

    return result - dia

print("Los dias que falta para año nuevo: ", hallaDias(dia,mes,año))