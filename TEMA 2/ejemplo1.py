# SUMAR NUMEROS DE LISTA
lista = [1,2,3,4,5]

def sumar(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

print("Resultado de la suma: ", sumar(lista))

