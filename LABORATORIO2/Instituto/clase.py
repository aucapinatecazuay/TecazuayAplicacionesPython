from estudiantes import devolver_materias

def estudiante_registrado_en_materia(nombre, materia):
    try:
        materias_estudiante = devolver_materias(nombre)
        return materia in materias_estudiante
    except TypeError:
        print("El nombre del estudiante debe ser una cadena de texto.")

