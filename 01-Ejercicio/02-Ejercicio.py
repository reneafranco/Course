numeros = 0
pares = 0

for numeros in range(1,121):
    pares = numeros % 2
    if pares == 0:
        print(numeros)
