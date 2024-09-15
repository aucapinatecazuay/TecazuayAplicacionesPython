estudiantes = {
    "Daniel": ["Matematica", "Computacion"],
    "Maria": ["Matematica", "Fisica"]
}

def devolver_materias(nombre):
    try:
        return estudiantes[nombre]
    except KeyError:
        print(f"El estudiante {nombre} no está registrado.")