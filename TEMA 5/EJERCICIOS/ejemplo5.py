class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self._precio = precio
    
    def obtener_precio(self):
        return self._precio

class Pedido: 
    def __init__(self, productos):
        self.productos = productos

    def calcular_total(self):
        total = 0
        for p in self.productos:
            total += p.obtener_precio()
        return total

p1 = Producto("Movil", 500)
p2 = Producto("Mando", 20)
p3 = Producto("Tablet", 350)

pedido = Pedido([p1, p2, p3])
print(f"El total es: {pedido.calcular_total()}")