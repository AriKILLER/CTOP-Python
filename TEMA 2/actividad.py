try:
    numero = int(input("Ingrese un numero: "))
except ValueError as e:
    print("Ha ocurrido un error: ", e)
else:
    print("Número procesado sin errores.")
finally:
    print("Ejecución finalizada.")
