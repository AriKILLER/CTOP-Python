alumno1 = {"nombre": "Arianna", "edad": 20, "estudiante": True}
alumno2 = {"nombre": "Bruno", "edad": 26, "estudiante": False}
alumno3 = {"nombre": "Carla", "edad": 17, "estudiante": True}
alumno3["curso"] = "2B"

def edad(alumno):
    if alumno["edad"] <18:
        return "Eres menor de edad"
    elif 18 <= alumno["edad"] <= 25:
        return "Eres muy joven"
    elif 26 <= alumno["edad"] <= 40:
        return "Eres joven"
    else:
        return "Ya no eres tan joven"

print(edad(alumno1))
print(edad(alumno2))
print(edad(alumno3))