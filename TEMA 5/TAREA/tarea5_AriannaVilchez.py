"""---- EJERCICIO 1 y 2 ----"""
class Producto:
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.__precio = precio if precio >= 0 else 0
    
    def informarcion(self):
        return f"ID: {self.id} - Nombre: {self.nombre} - Precio: {self.__precio}€"
    
    def getPrecio(self):
        return self.__precio
    
    def setPrecio(self, nuevo_precio):
        if nuevo_precio >= 0:
            self.__precio = nuevo_precio
        else:
            print("El precio no puede ser negativo")

p1 = Producto(1, "Portatil", 800)
p2 = Producto(2, "Ratón", 20)
print(p1.informarcion())
print(p2.informarcion())

"""---- EJERCICIO 3 ----"""
class ProductoAlimenticio(Producto):
    def __init__(self, id, nombre, precio, fecha_caducidad):
        super().__init__(id, nombre, precio)
        self.fecha_caducidad = fecha_caducidad
    
    def caducado(self, fecha_actual):
        if self.fecha_caducidad > fecha_actual:
            return "El producto no esta caducado"
        else:
            return "El producto esta caducado"
        
pa1 = ProductoAlimenticio(3, "Leche", 1.5, "2023-12-31")
print(pa1.caducado("2024-10-01"))

"""---- EJERCICIO 4 y 5 ----"""
import sqlite3

class GestorBD:
    def __init__(self, nombre_bd='tienda.db'):
        self.nombre_bd = nombre_bd
        self.conexion = sqlite3.connect(self.nombre_bd)
        self.cursor = self.conexion.cursor()
        self.crear_tabla()
    
    def crear_tabla(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            precio REAL,
            tipo TEXT, 
            fecha_caducidad TEXT
        )
        ''')
        self.conexion.commit()
    
    def insertar_producto(self, producto):
        self.cursor.execute("""
        INSERT INTO productos (id, nombre, precio, tipo)
        VALUES (?,?,?,?)""", (producto.id, producto.nombre, producto.getPrecio(), 'Normal'))
        print(f"Producto '{producto.nombre}' insertado en la base de datos.")
        self.conexion.commit()

    def insertar_alimenticio(self, producto_alimenticio):
        self.cursor.execute("""
        INSERT INTO productos (id, nombre, precio, tipo, fecha_caducidad)
        VALUES (?,?,?,?,?)""", (producto_alimenticio.id, producto_alimenticio.nombre, producto_alimenticio.getPrecio(), 'Alimenticio', producto_alimenticio.fecha_caducidad))
        print(f"Producto alimenticio '{producto_alimenticio.nombre}' insertado en la base de datos.")
        self.conexion.commit()

    def obtener_productos(self):
        self.cursor.execute("SELECT id, nombre, precio, tipo, fecha_caducidad FROM productos")
        productos = self.cursor.fetchall()
        for prod in productos:
            print(f"ID: {prod[0]}, Nombre: {prod[1]}, Precio: {prod[2]}€, Tipo: {prod[3]}, Fecha de Caducidad: {prod[4]}")
    
    def cerrar(self):
        self.conexion.close()

gestion = GestorBD()
gestion.insertar_producto(p1)
gestion.insertar_producto(p2)
gestion.insertar_alimenticio(pa1)
gestion.obtener_productos()
gestion.cerrar()
    

    

