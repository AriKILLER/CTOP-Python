almacen = {
    "Zapatillas":{
        "Precio": 15,
        "Stock": 10
    },
    "Camiseta":{
        "Precio": 10,
        "Stock": 25
    },
    "Pulsera":{
        "Precio": 5,
        "Stock": 30
    },
    "Vaqueros":{
        "Precio": 20,
        "Stock": 15
    },
    "Chaqueton":{
        "Precio": 50,
        "Stock": 5
    }
};

print("Precio de la pulsera: ", almacen["Pulsera"]["Precio"]);
print("Productos con stock menor a 20:" );
for producto in almacen:
    if almacen[producto]["Stock"] < 20:
        print("-", producto);

def valorTotal(almacen):
    total = 0
    for producto in almacen:
        precio = almacen[producto]["Precio"]
        stock = almacen[producto]["Stock"]
        total += precio * stock
    return total
print("Valor total del almacen: ", valorTotal(almacen));