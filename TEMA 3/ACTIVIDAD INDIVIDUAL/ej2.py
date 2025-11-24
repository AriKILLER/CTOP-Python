try:
    n1 = int(input("Ingrese un numero del 5 al 12: "))
except ValueError:
    print("Error: Debe ingresar un numero entero.")
else:
    if n1 < 5 or n1 > 12:
        print("Error: El numero debe estar entre 5 y 12.")
    else:
        print(f"Tabla de multiplicar del {n1}:")
        for i in range(1, 11):  
            print(f"{n1} x {i} = {n1 * i}")

