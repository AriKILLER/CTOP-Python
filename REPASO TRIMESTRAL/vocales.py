frase = input("Introduce una frase para contar sus vocales: ")
vocales = 'aeiuoAEIOU'
total = 0

for i in vocales:
    total += frase.count(i)
print(f"Hay un total de {total} vocales en la frase.")
