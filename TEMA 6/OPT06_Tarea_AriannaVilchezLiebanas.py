"""-----EJERCICIO 1: Generar cuadrados utilizando un generador -----"""
limite = int(input("Ingrese el limite para la generacion de cuadrados: "))

def cuadrados(limite):
    inicio = 1
    while inicio <= limite:
        yield inicio ** 2
        inicio += 1

for numero in cuadrados(limite):
    print(f"Cuadrado: {numero}")

"""---- EJERCICIO 2: Funciones lambda y map ----"""

generados = list(cuadrados(limite))
lista_suma_10 = list(map(lambda numero: numero + 10, generados))
print(f"Lista de generados + 10 = {lista_suma_10}")

"""---- EJERCICIO 3: Cierres ----"""

def crear_incrementador(n):
    def incrementar(x):
        return x + n
    return incrementar

incrementar_5 = crear_incrementador(5)
lista_incremento_5 = list(map(incrementar_5, cuadrados(limite)))
print(f"Lista con incremento de 5 = {lista_incremento_5}")
