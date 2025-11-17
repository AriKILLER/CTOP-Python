# Autor: Arianna Vilchez Liebanas
# Fecha: 14/11/2025
# Descripcion: Programa que solicita un número entero y muestra todos los números desde 0 hasta ese número con manejo de errores.

try:
    numero = int(input("Ingrese un número entero: ")) # Ejemplo de entrada: 5
except ValueError:
    print("Error: Por favor ingrese solo numeros enteros.") # Manejo de error si el usuario no ingresa un numero entero
else:
    for i in range(numero+1): # numero+1 para incluir el número ingresado en la iteración
        print(i) # Ejemplo de salida: 0 1 2 3 4 5