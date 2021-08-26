operacion = 0

while operacion == 0:
    numero = int(input("Ingrese un numero: "))
    if numero != 111:
        print(numero)
    elif numero == 111:
        operacion = 1

print("Fin")