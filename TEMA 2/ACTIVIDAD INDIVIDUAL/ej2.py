nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

def notaMedia(nota1, nota2, nota3):
    return (nota1+nota2+nota3)/3

print("La nota media del alumno es: ", format(notaMedia(nota1, nota2, nota3), ".2f"))