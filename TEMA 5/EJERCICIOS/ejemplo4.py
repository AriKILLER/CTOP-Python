import sqlite3

conexion = sqlite3.connect("empresa.db")
cursor = conexion.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS empleados (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, salario REAL)")

# insertar empleado
cursor.execute("INSERT INTO empleados (nombre, salario) VALUES (?, ?)", ("Arianna", 3000.0))
conexion.commit()
print("Empleado insertado correctamente")

# leer empleados
cursor.execute("SELECT * FROM empleados")
print("Registros en la tabla empleados:")
for fila in cursor.fetchall():
    print(f"(ID: {fila[0]}) Nombre: {fila[1]}, Salario: {fila[2]}")

cursor.close()
conexion.close()