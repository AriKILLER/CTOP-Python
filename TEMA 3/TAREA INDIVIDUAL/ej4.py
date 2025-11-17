def area_rectangulo(base, altura):
 area = base * altura # Correccion de simbolo de multiplicacion
 return area
base = int(input('Introduce la base: ')) # Falta la conversión a entero o float
altura = int(input('Introduce la altura: ')) # Falta la conversión a entero o float
area = area_rectangulo(base, altura)
print('El area es: ' ,area) # Falta la coma para concatenar el texto con la variable area
