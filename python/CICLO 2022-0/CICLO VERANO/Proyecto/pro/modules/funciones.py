from sys import exit
from os.path import exists as file_exists
from platform import system as OS
from .menu import print_unvalid_arg, print_unvalid_axis

# Maximo número de errores al pedir input
ERROR_COUNT = 10


# Funcion para determinar el margen de error adecuado de la funcion circulo en funcion del radio.
def circle_error_margin(radio):

    # Haciendo uso de un algoritmo predictivo:
    # https://www.dcode.fr/function-equation-finder
    margin = 1.14286 * radio - 2

    return margin


# Funcion para determinar el margen de error adecuado de la funcion linea en funcion de la pendiente.
def line_error_margin(pendiente):

    margin = 0.97619 * pendiente + 1.74971

    return margin

# Función para crear un cuadro vacio en el caso de que no se halla cargado ninguno
# Opcion por defecto en entrega #1


def dibujar_cuadro_vacio():

    width = 82
    height = 42
    mat = []

    mat.append([])
    mat[0] = ["." for x in range(width)]
    for row in range(1, height - 1):
        mat.append([])
        mat[row].append(".")
        for col in range(1, width - 1):
            mat[row].append(" ")
        mat[row].append(".")
    mat.append([])
    mat[-1] = ["." for x in range(width)]

    return mat


def imprimir_mat(mat):
    for row in mat:
        for col in row:
            print(col, end="")
        print()

###################################################################################

# Funciones para verificar que el dato ingresado es el adecuado


def valid_file_name(file_name):

    # Lists of invalid chars per OS
    invalid_linux_chars = ["\\", "NUL"]
    invalid_mac_chars = ["/", ":"]
    invalid_win_chars = ["NUL", "\\", "/", ":", "*", "?", "<", ">", "|", ]

    # If Linux
    if OS.find("Linux"):
        for char in invalid_linux_chars:
            if char in file_name:
                return False
        return True

    # If Windows
    elif OS.find("Windows"):
        for char in invalid_win_chars:
            if char in file_name:
                return False
        return True

    # If Mac
    elif OS.find("Mac"):
        for char in invalid_mac_chars:
            if char in file_name:
                return False
        return True
    else:
        print("Unable to identify operating system")
        return True


def is_float(arg):
    print(arg)
    try:
        arg = float(arg)
        return True
    except:
        return False


def is_int(arg):
    try:
        arg = int(arg)
        return True
    except:
        return False


def is_cord(arg):

    arg = arg.split(",")

    if len(arg) == 2:
        try:

            arg = list(map(int, arg))
            return True

        except:
            return False

    else:
        return False


axis_dict = {
    "x": 81,
    "y": 41
}


def validate_axis(arg, axis):

    if arg in range(axis_dict[axis] + 1):
        return True
    else:
        print_unvalid_axis(arg, axis_dict[axis], axis)
        return False


# Tipos de dato posibles
type_verify = {
    "int": is_int,
    "float": is_float,
    "cord": is_cord,
    "write_file": valid_file_name,
    "read_file": file_exists
}

# Función utilizada para obtener el input


def ask_args(args, type_args):

    if args[0] == None:
        return []

    args_list = []
    for arg, type_arg in zip(args, type_args):

        for tries in range(ERROR_COUNT):

            return_arg = (input(f"ingrese el/la {arg}: "))

            # Verificar el tipo de dato
            if type_verify[type_arg](return_arg):

                if type_arg == "cord":

                    return_arg = list(map(int, return_arg.split(",")))

                    # Validate if coord x/y are inside the mat
                    if validate_axis(return_arg[0], "x") and validate_axis(return_arg[1], "y"):

                        args_list.append(return_arg)
                        break

                else:

                    args_list.append(return_arg)
                    break

            else:
                # Informar al usuario en caso de tipo de dato erroneo
                print_unvalid_arg(return_arg, type_arg)

            # Terminar programa tras ERROR_COUNT intentos
            if tries == ERROR_COUNT - 1:
                exit()

    return args_list
