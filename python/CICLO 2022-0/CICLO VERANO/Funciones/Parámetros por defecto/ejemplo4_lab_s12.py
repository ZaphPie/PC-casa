def estudiante(nombre, apellido="Mark", standard="Quinto"):
    print(nombre, apellido, " estudia en ", standard, "standard")


# --- 1 parametro posicional
estudiante("John")

# --- 3 parametros posicionales
estudiante("John", "Gates", "Séptimo")

# --- 2 parametros posicionales
estudiante("John", "Gates")
estudiante("John", "Séptimo")
estudiante("John","segundo")