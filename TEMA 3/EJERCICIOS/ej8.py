numero = 0;
suma = 0;
activo = True;

while(activo):
    numero+=2;
    suma+=numero;
    if(numero == 20):
        activo = False;
print(f"La suma de los numeros pares hasta el 20 es: {suma}");
        