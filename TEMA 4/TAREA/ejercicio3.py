stock = {
    "Zapatillas": 10,
    "Camiseta": 25,
    "Pulsera": 30,
    "Vaqueros": 15,
    "Chaqueton": 5
};

def totalDisponible(stock):
    total = 0
    for cantidad in stock.values():
        total += cantidad
    return total
print("Total de productos disponibles en stock: ", totalDisponible(stock));

def cantidadMayorA20(stock):
    productos = []
    for producto, cantidad in stock.items():
        if cantidad > 20:
            productos.append(producto)
    return productos
print("Productos con cantidad de stock mayor a 20: ", cantidadMayorA20(stock));