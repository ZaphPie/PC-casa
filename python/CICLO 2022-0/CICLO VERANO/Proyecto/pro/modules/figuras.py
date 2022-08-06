from .funciones import line_error_margin, circle_error_margin, imprimir_mat


def dibujar_linea(mat_previa, args):

    # 42
    height = len(mat_previa)
    # 82
    width = len(mat_previa[0])

    # Format inputs for easier usage

    cord_inicial, cord_final = args

    cord_inicial = list(map(int, cord_inicial))
    cord_final = list(map(int, cord_final))

    cord_inicialx, cord_inicialy = cord_inicial
    cord_finalx, cord_finaly = cord_final

    try:
        pendiente = float(((cord_inicialy) - (cord_finaly)) /
                          ((cord_inicialx) - (cord_finalx)))
    except ZeroDivisionError:
        pendiente = 0

    # Ecuacion de la interseccion
    # Interseccion = Y - (pendiente * X)
    interseccion = float(cord_inicialy - (pendiente * cord_inicialx))

    cord_menorx = min(cord_inicialx, cord_finalx)
    cord_menory = min(cord_inicialy, cord_finaly)

    sizex = abs(cord_inicialx - cord_finalx)
    sizey = abs(cord_inicialy - cord_finaly)

    range_x = [x for x in range(cord_menorx, cord_menorx + sizex + 1)]
    range_y = [y for y in range(cord_menory, cord_menory + sizey + 1)]

    error_margin = line_error_margin(pendiente)

    nueva_matriz = []

    for y in range(height - 1, -1, -1):
        nueva_matriz.append([])
        for x in range(width):

            linea_actual = abs(y - (height - 1))

            in_line_ecuation = abs(y - (pendiente * x) - interseccion)

            in_line_range = x in range_x and y in range_y

            # Check if the ecuation of a straight line corresponds to the value X and Y
            if in_line_ecuation <= error_margin and in_line_range:

                nueva_matriz[linea_actual].append("X")
            else:
                nueva_matriz[linea_actual].append(mat_previa[linea_actual][x])

    return nueva_matriz


# Enrique
def dibujar_elipse(mat_previa, args):

    # 42
    height = len(mat_previa)
    # 82
    width = len(mat_previa[0])

    # Format inputs for easy usage
    centro, radio = args
    centrox, centroy = centro

    radio = int(radio)

    error_margin = circle_error_margin(radio)

    nueva_matriz = []

    for y in range(height - 1, -1, -1):
        nueva_matriz.append([])
        for x in range(width):

            linea_actual = abs(y - (height - 1))

            # Check if the ecuation of the elipse corresponds to the value X and Y
            if abs((radio ** 2) - ((x - centrox) ** 2 + (y - centroy) ** 2)) <= error_margin:
                nueva_matriz[linea_actual].append("X")
            else:
                nueva_matriz[linea_actual].append(mat_previa[linea_actual][x])
    return nueva_matriz


# Nicolas
def dibujar_rectangulo(mat_previa, args):
    nueva_matriz = []

    punto_inferior, base, altura = args

    # 42
    height = len(mat_previa)
    # 82
    width = len(mat_previa[0])

    # Format inputs for easy usage
    puntox, puntoy = punto_inferior

    base = int(base)
    altura = int(altura)

    rangox = [a for a in range(puntox, puntox + base)]
    rangoy = [b for b in range(puntoy, puntoy + altura)]

    for y in range(height - 1, -1, -1):
        nueva_matriz.append([])
        for x in range(width):
            linea_actual = abs(y - (height - 1))

            if (x == rangox[0] or x == rangox[-1]) and y in rangoy:
                nueva_matriz[linea_actual].append("X")

            elif (y == rangoy[0] or y == rangoy[-1]) and x in rangox:
                nueva_matriz[linea_actual].append("X")

            else:
                nueva_matriz[linea_actual].append(mat_previa[linea_actual][x])
    return nueva_matriz


##############################################################
# ToDo

# David
def dibujar_triangulo(mat_previa, args):
    nueva_matriz = []

    punto_inferior_izquierdo, base, altura = args

    # 42
    height = len(mat_previa)
    # 82
    width = len(mat_previa[0])

    # Format inputs for easy usage
    punto_infX, punto_infY = punto_inferior_izquierdo

    base = int(base)
    altura = int(altura)

    punto_inferior_derecho = [punto_infX + base, punto_infY]
    punto_superior = [punto_infX + round(base/2), punto_infY + altura]

    nueva_matriz = dibujar_linea(
        mat_previa, [punto_inferior_izquierdo, punto_inferior_derecho])
    nueva_matriz = dibujar_linea(
        nueva_matriz, [punto_inferior_derecho, punto_superior])

    nueva_matriz = dibujar_linea(
        nueva_matriz, [punto_superior, punto_inferior_izquierdo])

    return nueva_matriz

# ToDo


def grabar_dibujo(current_mat, destination_file):
    with open(destination_file, "w") as write_file:

        for col in current_mat:
            for line in col:
                write_file.write(line)
            write_file.write("\n")

    return

# ToDo


def leer_dibujo(current_mat, from_file):
    with open(from_file[0], "r") as read_file:
        lines = read_file.readlines()
        return [list(line) for line in lines]

# ToDo


def mostrar_dibujo(current_mat, empty_list):
    imprimir_mat(current_mat)
    return
