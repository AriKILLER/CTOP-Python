texto = ""

try:
    f = open("archivo.txt", "w")
    # texto = f.read()
    f.write("hola mundo")
except IOError as e:
    print("Ocurrio un error", e)
else:
    print("Archivo escrito correctamente")
finally:
    f.close()
