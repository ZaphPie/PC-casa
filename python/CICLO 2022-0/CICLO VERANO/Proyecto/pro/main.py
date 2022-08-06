#   Grupo #5

#   Oscar Daniel Rodenas Rocha          - 202110312
#   Nicolás Alejandro Llerena Silva     - 202110190
#   Jonathan David Taipe Santos         - 202120560
#   Enrique Francisco Flores Teniente   - 202010009

from sys import exit

import modules

# Limit number of posible errors
# ERROR_COUNT = 10
ERROR_COUNT = modules.ERROR_COUNT


# Dict with otions
options = {

    # Agregar una línea
    "1": (modules.dibujar_linea, ["cord_inicial", "cord_final"], ["cord", "cord"]),

    # Agregar una elipse o círculo
    "2": (modules.dibujar_elipse, ["centro (centroX, centroY)", "radio"], ["cord", "int"]),

    # Agregar un rectángulo o cuadrado
    "3": (modules.dibujar_rectangulo, ["punto inferior (puntoX, puntoY)", "base", "altura"], ["cord", "int", "int"]),

    # Agregar un triángulo
    "4": (modules.dibujar_triangulo, ["punto inferior (puntoX, puntoY)", "base", "altura"], ["cord", "int", "int"]),

    # Grabar un dibujo
    "5": (modules.grabar_dibujo, ["archivo donde guardar"], ["write_file"]),

    # Leer un dibujo
    "6": (modules.leer_dibujo, ["archivo a leer"], ["read_file"]),

    # Mostrar un dibujo
    "7": (modules.mostrar_dibujo, [None], [None]),

    # Salir del programa
    "0": None

}


def main():

    current_mat = modules.dibujar_cuadro_vacio()

    # Print menu from menu.py
    modules.print_title()
    modules.print_space()

    while True:

        # Print instructions
        modules.print_instructions()
        modules.print_space()
        modules.print_options()
        modules.print_space()

        # Read option until its valid
        for tries in range(ERROR_COUNT):

            # Get input as string
            option = input("Select an option:\n")

            # Verificar que la opcion sea valida (0 - 7)
            if option not in options.keys():
                modules.print_unvalid_option(option)

                # Terminar programa tras ERROR_COUNT intentos
                if tries == ERROR_COUNT - 1:
                    exit()
                continue

            # Verify option 0
            if option == "0":
                print("Are you sure you want to exit? (yes/no)")
                if input().lower() == "yes":
                    exit()
            else:
                break

        # name of function to execute
        function = options[option][0]

        # list of needed arguments
        args = options[option][1]

        # List of type for each argument
        type_args = options[option][2]

        # Ask and verify each argument
        pass_args = modules.ask_args(args, type_args)

        if option in "12346":

            # Pass function and arguments
            current_mat = function(current_mat, pass_args)

        else:
            function(current_mat, pass_args)

    return


if __name__ == "__main__":
    main()
