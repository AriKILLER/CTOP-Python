try:
    n = int(input("Introduce un numero para ver su tabla de multiplicar: "))
except Exception:
    print("Error: Introduce un numero entero")
else:
    for i in range(1, 11):
        resultado = i*n
        print(f"{n} * {i} : {resultado}")
