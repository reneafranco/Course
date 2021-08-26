import random

def juegoNumero():
    print("**********Juego Adivina el numero************")

num_random = random.randint(0,10)
num_usuario = int(input("Ingrese el numero: "))

while num_usuario != num_random:

    if num_usuario > num_random:
        print(f"El numero {num_usuario}  es mayor al numero del juego")
        num_usuario = int(input("Ingrese el numero: "))

    elif num_usuario < num_random:
        print(f"El numero {num_usuario}  es menor que el numero del juego")
        num_usuario = int(input("Ingrese el numero: "))
    
else:
    if num_usuario == num_random:
        print("Felicidades...ganaste")


#Calculadora 
Seleccion = "+"
num1 = 1
num2 = 1
def calculadora(num1, num2,Seleccion):
    if Seleccion == "+":
        return num1 + num2
    elif Seleccion == "-":
        return num1 - num2    