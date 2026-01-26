"""---- APARTADO 1 ----"""
class Libro:
    def __init__(self, titulo, autor, isbn):
        self._titulo = titulo
        self._autor = autor
        self._isbn = isbn
    
    def obtenerTitulo(self):
        return self._titulo
    
    def obtenerAutor(self):
        return self._autor
    
    def informacion(self):
        return f"Titulo: {self._titulo} - Autor: {self._autor} - ISBN: {self._isbn}"
    
libro1 = Libro("El señor de los anillos", "JRR Tolkien", "956-454686")
libro2 = Libro("Una cancion de hielo y fuego", "George R R Martin", "123-456789")
print(libro1.obtenerAutor())
print(libro1.obtenerTitulo())
print(libro1.informacion())
print(libro2.obtenerAutor())
print(libro2.obtenerTitulo())
print(libro2.informacion())


"""---- APARTADO 2 ----"""

class LibroDigital(Libro):
    def __init__(self, titulo, autor, isbn, tamano_mb):
        super().__init__(titulo, autor, isbn)
        self._tamano_mb = tamano_mb

    def informacion(self):
        info = super().informacion()
        return f"{info} - Tamaño: {self._tamano_mb} MB"
    
libroDig1 = LibroDigital("Chainsaw Man", "Tatsuki Fujimoto", "965-654888", 4)
libroDig2 = LibroDigital("Attack on Titan", "Hajime Isayama", "985-879845", 5)
print(libroDig1.informacion())
print(libroDig2.informacion())

"""---- APARTADO 3 ----"""
import sqlite3
conexion = sqlite3.connect("biblioteca.db")
cursor = conexion.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS libros (id INTEGER PRIMARY KEY AUTOINCREMENT,titulo TEXT,autor TEXT,isbn TEXT)")

def insertar_libro(libro):
    cursor.execute("INSERT INTO libros (titulo, autor, isbn) VALUES (?, ?, ?)",
                   (libro._titulo, libro._autor, libro._isbn))
    print(f"Libro '{libro._titulo}' insertado en la base de datos.")
    conexion.commit()

def obtener_libros():
    cursor.execute("SELECT titulo, autor, isbn FROM libros")
    libros = cursor.fetchall()
    for libro in libros:
        print(f"Titulo: {libro[0]}, Autor: {libro[1]}, ISBN: {libro[2]}")

insertar_libro(libro1)
obtener_libros()
