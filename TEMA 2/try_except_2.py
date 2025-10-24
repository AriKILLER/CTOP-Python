import sys

lista = [1,2,3,4]

try:
    for n in range(5):
        print(lista[n]) # print(n) para imprimir correctamente
except IndexError as e:
    print("Error",e)
else:
    print("Realizado sin errores")
finally:
    sys.exit()