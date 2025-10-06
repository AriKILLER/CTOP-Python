from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista = [x for x in range(20)] # Lista del 0 al 19 generado automaticamente

print(choice(my_list)) # Elige un elemento al azar
print(sample(my_list, 5)) # Elige 5 elementos al azar, sin repeticion
print(sample(my_list, 10)) # Elige 10 elementos al azar, sin repeticion