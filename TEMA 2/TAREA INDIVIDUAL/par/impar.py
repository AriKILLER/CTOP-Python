try:
    numero = int(input("Ingrese un número entero: "))
except ValueError:
    print("Por favor, ingrese un número entero válido.")
else:
    if numero % 2 == 0:
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")