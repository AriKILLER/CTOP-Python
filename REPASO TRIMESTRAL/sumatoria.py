activo = True
sumatoria = 0
while activo:
    try:
        n = int(input("Ingrese un número entero positivo e ingrese 0 para terminar: "))
    except Exception:
        print("Error: Debe ingresar un número entero válido.")
    else:
        if n != 0:
            sumatoria += n
        elif n == 0:
            activo = False
print(f"Suma total de los numeros introducidos {sumatoria}")
