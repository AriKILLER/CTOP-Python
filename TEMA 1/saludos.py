import sys

def saludar(nombre):
    return f"Hola, {nombre}!"

def despedir(nombre):
    return f"Adiós, {nombre}!"

if __name__ == "__main__":
    print('No me ejecutes, !solo soy un modulo!')
    print(__name__)
    sys.exit(1)
else:
    print(__name__)

# __name__ es una variable global que Python asigna dependiendo de cómo se ejecute el script.
# Si se ejecuta como un programa principal, __name__ es igual a "__main__".
# Si se importa como un módulo en otro script, __name__ es igual al nombre del módulo (sin la extensión .py).


