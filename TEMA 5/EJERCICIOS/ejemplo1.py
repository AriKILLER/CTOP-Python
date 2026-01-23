'''
Este ejemplo combina POO y bases de datos
'''

class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
u = Usuario("Arianna", 20)

import sqlite3
conexion = sqlite3.connect("usuarios.db")
cursor = conexion.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS usuario (nombre TEXT, edad INTEGER)")
cursor.execute("INSERT INTO usuario VALUES (?, ?)", (u.nombre, u.edad))

conexion.commit()
print("Base de datos actualizada")
conexion.close()
