print("###########CALCULADORA BASICA#############")
print("1. Ingrese 1 para sumar ")
print("2. Ingrese 2 para restar")
print("3. Ingrese 3 para multiplicar ")
print("4. Ingrese 4 para dividir \n")

seleccion = int(input("Que accion desea realizar?: "))

num_uno = int(input("Cual es el primer numero?: "))
num_dos = int(input("Cual es el primer numero?: "))

if seleccion == 1:
    resultado = num_uno + num_dos
    print("El resultado es", resultado)
elif seleccion == 2:
    resultado = num_uno - num_dos
    print("El resultado es", resultado)
elif seleccion == 3:
    resultado = num_uno * num_dos
    print("El resultado es", resultado)
elif seleccion == 4:
    resultado = num_uno / num_dos
    print("El resultado es", resultado)