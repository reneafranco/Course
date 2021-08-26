#parte sobre todo es igual al % sobre 100
# p = %

total = float(input("Ingrese la cantidad a la cual desea buscar el porciento: "))
porciento = float(input("Ingrese el porciento que desea obtener: "))

if total > porciento:
    parte = ((porciento * total)/100)
    print(parte)

