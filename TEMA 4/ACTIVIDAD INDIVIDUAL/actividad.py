# Ejercicio 1
estudiantes = ["Arianna", "Hugo", "Marta"];
print(estudiantes);
nuevoEstudiante = input("Ingrese el nombre del nuevo estudiante a agregar: ");
estudiantes.append(nuevoEstudiante); # Agregar nuevo estudiante por el usuario
del estudiantes[2]; # Eliminar el tercer estudiante
sorted(estudiantes); # Ordenar la lista alfabeticamente
print("Lista actualizada de estudiantes:", estudiantes);
print("------------------------------------------");

# Ejercicio 2
calificaciones = {"Arianna": 9, "Hugo": 8, "Jaime": 10};
calificaciones["Hugo"] = 7; # Actualizar la calificacion de Hugo
print("Calificacion de Arianna: ",calificaciones.get("Arianna")); # Consultar nota usando get()
for clave, valor in calificaciones.items(): 
    print(f"Estudiante: {clave}, Calificacion: {valor}");
notaMedia = sum(calificaciones.values()) / len(calificaciones); # Calcular la nota media
print("La nota media es: ", notaMedia);
print("------------------------------------------");

# Ejercicio 3
import os
ruta_archivo = os.path.join(os.path.dirname(__file__), "alumnos.txt") # Ruta del archivo alumnos.txt porque si no no lo detecta y no se escribe bien
with open(ruta_archivo, "w") as archivo:
    for clave, valor in calificaciones.items():
        archivo.write(f"Nombre: {clave} - Nota: {valor}\n")

