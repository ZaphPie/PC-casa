from shutil import get_terminal_size


title = [

    "/$$       /$$   /$$     /$$     /$$                  /$$$$$$   /$$$$$$  /$$$$$$$         /$$$$$$  /$$$$$$$ ",
    "| $$      |__/  | $$    | $$    | $$                 /$$__  $$ /$$__  $$| $$__  $$       /$$__  $$| $$__  $$",
    "| $$       /$$ /$$$$$$ /$$$$$$  | $$  /$$$$$$       | $$  \__/| $$  \ $$| $$  \ $$      |__/  \ $$| $$  \ $$",
    "| $$      | $$|_  $$_/|_  $$_/  | $$ /$$__  $$      | $$      | $$$$$$$$| $$  | $$        /$$$$$$/| $$  | $$",
    "| $$      | $$  | $$    | $$    | $$| $$$$$$$$      | $$      | $$__  $$| $$  | $$       /$$____/ | $$  | $$",
    "| $$      | $$  | $$ /$$| $$ /$$| $$| $$_____/      | $$    $$| $$  | $$| $$  | $$      | $$      | $$  | $$",
    "| $$$$$$$$| $$  |  $$$$/|  $$$$/| $$|  $$$$$$$      |  $$$$$$/| $$  | $$| $$$$$$$/      | $$$$$$$$| $$$$$$$/",
    "|________/|__/   \___/   \___/  |__/ \_______/       \______/ |__/  |__/|_______/       |________/|_______/ "

]


instructions = [
    "Little CAD 2D es un programa que permite dibujar un conjunto básico de figuras geométricas:",
    "líneas, triangulos, rectángulos, elipses, círculos. Dentro de una matriz de 82 x 42 (largo x alto)."
]

option_menu = [

    "Eliga una de las siguientes opciones para iniciar:\n",
    "1. Agregar una línea",
    "2. Agregar una elipse o círculo",
    "3. Agregar un rectángulo o cuadrado",
    "4. Agregar un tríangulo",
    "5. Grabar un dibujo",
    "6. Leer un dibujo",
    "7. Mostrar un dibujo",
    "0. Salir del programa"

]

term_width = get_terminal_size()[0]


def print_title():
    print_lines(title)


def print_instructions():
    print_lines(instructions)


def print_options():
    print_lines(option_menu)


def print_space():
    print("#" * term_width)

# Output for invalid option


def print_unvalid_option(option):
    print(f"'{option}' is not a valid option, it must be a number from 0 through 7")

# Output for invalid argument


def print_unvalid_arg(arg, arg_type):
    print(f"'{arg}' is not a valid argument, it must be a/an {arg_type}.")


def print_unvalid_axis(cord, ran, axis):
    print(f"{cord} is not a valid coordinate for the {axis} axis, it must be between 0 and {ran}.")

# Print list of strings


def print_lines(text):
    for line in text:
        print(line)
    return
