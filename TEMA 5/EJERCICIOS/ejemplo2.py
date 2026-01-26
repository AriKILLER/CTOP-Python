class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self._edad = edad
        self.__dni = dni

    def getEdad(self):
        return self._edad
p = Persona("Hugo", 20, "12345678A")

print(p._edad)
print(p.getEdad())
print(p._Persona__dni)