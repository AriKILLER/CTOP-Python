numeros=(1,4,6,3)

def promedio(numeros):
    if len(numeros) == 0:
        print("La lista no puede estar vacia")
        return None
    else:
        sumatoria = 0
        for i in range(len(numeros)):
            sumatoria += numeros[i]
        resultado = sumatoria / len(numeros)
        return resultado
print(promedio(numeros))