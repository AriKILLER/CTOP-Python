
TUTORIAL – ESTRUCTURAS DE DATOS EN PYTHON (CLI)
=================================================


EJERCICIO 1 – Listas
-------------------
Crea una lista con 5 números enteros:

numeros = [1, 2, 3, 4, 5]

Añade un número al final
>>> numeros.append(6)
>>> numeros
[1, 2, 3, 4, 5, 6]

Elimina el último número
>>> numeros.pop()
6
>>> numeros
[1, 2, 3, 4, 5]

Muestra solo los 3 primeros elementos
>>> numeros[0:3]
[1, 2, 3]

EJERCICIO 2 – Listas
-------------------
Dada una lista de nombres, comprueba si "Ana" está en la lista.
nombres = ["Luis", "Ana", "Pedro", "Marta"]

>>> nombres = ["Luis", "Ana", "Pedro", "Marta"]
>>> 'Ana' in nombres
True

EJERCICIO 3 – Tuplas
-------------------
Crea una tupla con 4 colores y:
colores = ("azul", "verde", "rojo", "amarillo")

Accede al segundo color
>>> colores = ("azul", "verde", "rojo", "amarillo")
>>> colores[1]
'verde'

Comprueba si "rojo" está en la tupla
>>> 'rojo' in colores
True


EJERCICIO 4 – Tuplas
-------------------
Intenta modificar un elemento de la tupla.
👉 Observa el error y entiende por qué ocurre.

No se puede modificar directamente un elemento porque las tuplas son inmutables

EJERCICIO 5 – Arrays
-------------------
Crea un array de enteros y:

from array import array
nums = array( ... )

Cambia el valor del primer elemento
>>> from array import array
>>> nums = array('i', [1,2,3,4,5])
>>> nums
array('i', [1, 2, 3, 4, 5])
>>> nums[0] = 10
>>> nums
array('i', [10, 2, 3, 4, 5])

Intenta asignar un valor de tipo incorrecto
>>> nums[1] = 'hola'
Traceback (most recent call last):
  File "<python-input-5>", line 1, in <module>
    nums[1] = 'hola'
    ~~~~^^^
TypeError: 'str' object cannot be interpreted as an integer

No deja porque hemos creado el array para que guarde solo enteros


EJERCICIO 6 – Diccionarios
--------------------------
Crea un diccionario con información de una persona:

nombre
edad

>>> persona = {'nombre': 'Arianna', 'edad': 20}
>>> persona
{'nombre': 'Arianna', 'edad': 20}

Luego, añade la clave "ciudad"
>>> persona['ciudad'] = 'Granada'
>>> persona
{'nombre': 'Arianna', 'edad': 20, 'ciudad': 'Granada'}

Elimina la clave "edad"
>>> persona.pop('edad')
20
>>> persona
{'nombre': 'Arianna', 'ciudad': 'Granada'}


EJERCICIO 7 – Diccionarios
--------------------------
Recorre el diccionario anterior e imprime las claves y valores.
>>> for clave,valor in persona.items():
...     print(clave, ',' ,valor)
...
nombre , Arianna
ciudad , Granada


EJERCICIO 8 – Pila (stack)
-------------------------
Simula una pila usando una lista:

pila = []

Añade 3 números
>>> pila = []
>>> pila.append(1)
>>> pila.append(4)
>>> pila.append(5)
>>> pila
[1, 4, 5]

Elimina el último
>>> pila.pop()
5

Muestra la pila final
>>> pila
[1, 4]

EJERCICIO 9 – Cola (queue)
-------------------------
Simula una cola usando deque:

from collections import deque

Añade 3 elementos
>>> cola = deque()
>>> cola.append(3)
>>> cola.append(5)
>>> cola.append(1)
>>> cola
deque([3, 5, 1])

Elimina el primero
>>> cola.popleft()
3

Muestra la cola resultante
>>> cola
deque([5, 1])

append() → añadir
popleft() → quitar el primero


EJERCICIO 10 – Extra
-------------------
Dada una lista de números:

nums = [4, 7, 1, 9, 2]

Ordénala
Obtén el valor máximo
Obtén el valor mínimo




