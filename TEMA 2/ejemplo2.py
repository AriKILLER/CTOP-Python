frase = 'Hola, aqui programando en Python'
vocales = 'aeiouAEIOU'
    
def contar_vocales(frase):
    contador = 0
    for vocal in vocales:
        contador += frase.count(vocal)
    return contador
print("Vocales en la frase: ", contar_vocales(frase))