try:
    n1 = int(input("Introduce un numero: "))
    n2 = int(input("Introduce el segundo numero: "))
except ValueError:
    print("Error: No has introducido un valor de tipo numerico.")
else:
    if(n1 > n2):
        print(f"El numero {n1} es mayor que {n2}.")
    elif(n2 > n1):
        print(f"El numero {n2} es mayor que {n1}.")
    else:
        print(f"Los numeros {n1} y {n2} son iguales.")