import time as t

try:
    n = int(input("Introduce un numero entre 5 y 50: "))
except ValueError as e:
    print("Error: ", e)
else:
    if n < 5 or n > 50:
        print("Error: El numero debe estar entre 5 y 50.")
    else:
        for i in range(n, 0, -1):
            print(i)
            t.sleep(0.5)
