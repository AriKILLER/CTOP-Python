limite = 21
def numeros_suerte(limite):
    inicio = 1
    while inicio <= limite:
        yield inicio
        inicio += 1

def numeros_suerte_pares(limite):
    inicio = 2
    while inicio <= limite:
        yield inicio
        inicio += 2

print("Numeros de la suerte:")
for numero in numeros_suerte(limite):
    print(numero)

print("\nNumeros de la suerte pares:")
for numero in numeros_suerte_pares(limite):
    print(numero)