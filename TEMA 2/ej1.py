# Pide la edad y solo acepte si el valor esta comprendido entre 1 y 120(años)

# Entre 1 y 15 - niño
# Entre 16 y 21 - adolescente
# entre 22 y 35 - joven
# entre 36 y 50 - maduro
# entre 51 y 60 - mediana edad
# entre 61 y 80 -  mayor
# entre 81 y 100 - viejo
# mayor de 100- centenario
while True:
    edad = int(input("Ingresa una edad entre 1 y 120:"))
    if 1 <= edad <= 120:
        break
if 1 <= edad <= 15:
    print("Eres un niño")
elif 16 <= edad <=21:
    print("Eres un adolescente")
elif 22 <= edad <=35:
    print("Eres joven")
elif 36 <= edad <=50:
    print("Eres maduro")
elif 51 <= edad <=60:
    print("Eres de mekdiana edad")
elif 61 <= edad <= 80:
    print("Eres mayor")
elif 81 <= edad <= 100:
    print("Eres viejo")
else:
    print("Eres centenario")
