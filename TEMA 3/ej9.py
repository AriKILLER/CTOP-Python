try:
    numero = int(input("Ingrese un numero para ver su tabla de multiplicar: "))
except ValueError:
    print("Error: Ingrese un numero.")
else:
    for i in range(1,11):
        resultado = numero * i;
        print(f"{numero} x {i} = {resultado}");