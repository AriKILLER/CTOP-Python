numero = int(input("Ingrese un numero entero: "))
suma_pares = 0
for i in range(numero, 0, -1):
    if i % 2 == 0:
        print(i)
        suma_pares += i
    else:
        continue

print(f"La suma total de los números pares es: {suma_pares}")
