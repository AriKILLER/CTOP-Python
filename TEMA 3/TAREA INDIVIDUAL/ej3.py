# Autor: Arianna Vilchez Liebanas
# Fecha: 14/11/2025
# Descripcion: Programa que solicita dos numeros enteros y una operacion aritmetica, y muestra el resultado con manejo de errores.

try:
    n1 = int(input("Ingrese el primer numero: ")) # Ejemplo de entrada: 8
    n2 = int(input("Ingrese el segundo numero: ")) # Ejemplo de entrada: 4
    op = input("Ingrese la operacion a realizar (+, -, *, /): ") # Ejemplo de entrada: / 
except ValueError:
    print("Error: Por favor ingrese solo numeros enteros.") # Manejo de error si el usuario no ingresa un numero entero
else:   
    match op: # Estructura condicional para seleccionar la operacion aritmetica
        case "+":
            print("El resultado de la suma es:", n1 + n2)
        case "-":
            print("El resultado de la resta es:", n1 - n2)
        case "*":
            print("El resultado de la multiplicacion es:", n1 * n2)
        case "/":
            if n2 != 0: # Manejo de error para division por cero
                print("El resultado de la division es:", n1 / n2) # Ejemplo de salida: El resultado de la division es: 2.0
            else:
                print("Error: No se puede dividir por cero.")
        case _:
            print("Error: Operacion no valida.") # Manejo de error para operacion no valida