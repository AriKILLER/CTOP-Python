# Autor: Arianna Vilchez Liebanas
# Fecha: 14/11/2025
# Descripcion: Programa que solicita tres numeros enteros y muestra el mayor de ellos con manejo de errores.

try:
    n1 = int(input("Ingrese el primer numero: ")) # Ejemplo de entrada: 5
    n2 = int(input("Ingrese el segundo numero: ")) # Ejemplo de entrada: 10
    n3 = int(input("Ingrese el tercer numero: ")) # Ejemplo de entrada: 3
except ValueError:
    print("Error: Por favor ingrese solo numeros enteros.") # Manejo de error si el usuario no ingresa un numero entero
else:
    if n1 > n2 and n1 > n3:
        print("El numero mayor es:", n1)
    elif n2 > n1 and n2 > n3:
        print("El numero mayor es:", n2) # Ejemplo de salida: El numero mayor es: 10
    elif n3 > n1 and n3 > n2:
        print("El numero mayor es:", n3)
    else:
        print("Hay numeros iguales entre los ingresados.") # Manejo de caso donde hay numeros iguales