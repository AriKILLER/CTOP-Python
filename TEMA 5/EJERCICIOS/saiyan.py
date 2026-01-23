class saiyan:
    planeta = "Sadala"
    def __init__(self, nombre):
        self.nombre = nombre

class Goku(saiyan):
    pass

class Vegeta(saiyan):
    pass

personaje1 = Goku("Goku");
personaje2 = Vegeta("Vegeta");

print(personaje1.nombre);