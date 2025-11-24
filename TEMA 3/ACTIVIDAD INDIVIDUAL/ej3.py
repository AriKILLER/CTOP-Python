try:
    n1 = int(input("Ingrese un numero para calcular la media aritmetica: "))
    n2 = int(input("Ingrese otro numero para calcular la media aritmetica: "))
except ValueError:
    print("Error: Debe ingresar numeros enteros.")
else:
    def mediaAritmetica(n1, n2):
        return (n1 + n2) / 2
    resultado = mediaAritmetica(n1, n2)
    print(f"La media aritmetica de {n1} y {n2} es: {resultado}")