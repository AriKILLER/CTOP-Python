lista = []
contador = 0

while True:
    try:
        palabra = input("Introduce una palabra: ")
    except ValueError:
        print("Error: No has introducido una palabra valida.")
    else:
        if palabra == "basta":
            print(f"Has soportado estoicamente {contador} preguntas.")
            break
        
        lista.append(palabra)
        contador += 1
        print(f"Lista actual: {lista}")