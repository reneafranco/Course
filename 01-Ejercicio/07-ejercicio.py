num_uno = int(input("Ingrese el primer numero: "))
num_dos = int(input("Ingrese el segundo numero: "))
num_dos += 1

contador = 0

if num_uno < num_dos:
    for contador in range(num_uno,num_dos):
        resultado = contador % 2
        if resultado != 0:
            print(f"el numero {contador} es impar")
else:
    print("El primer numero debe ser mayor que el segundo")
