'''
Muestra los enteros del 1 al 5 en una sola línea, separados por comas.

'''

'''
for i in range(1,6):
    print(i, end=", ")
'''
# Numeros pares del 1 al 20

for i in range(0,21):
    if i % 2 == 0:
        print(i, end=", ")

pares = [p for p in range(0,21) if p%2==0]

for i in pares:
    print(i, end=", ")
