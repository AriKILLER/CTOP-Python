# Autor: Arianna Vilchez Liebanas
# Fecha: 14/11/2025
# Descripcion: Programa que calcula la suma de los números del 1 al 1,000,000 usando la función sum() y mide el tiempo de ejecución.

import time
inicio = time.time() # Inicia la medición del tiempo
suma = sum(range(1, 1000001)) # Calcula la suma de los números del 1 al 1,000,000 usando la función sum()
fin = time.time() # Finaliza la medición del tiempo
print("La suma es:", suma) # Ejemplo de salida: La suma es: 500000500000
print("El tiempo de ejecucion es:", fin - inicio, "segundos") # Muestra el tiempo de ejecución en segundos