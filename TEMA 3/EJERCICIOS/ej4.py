alumno = {"nombre": "Arianna", "edad": 20, "curso": "2 DAW"}

for clave, valor in alumno.items():
    print(f"{clave}: {valor}")

print(f"Nombre: {alumno['nombre']}, Edad: {alumno['edad']}, Curso: {alumno['curso']}")
