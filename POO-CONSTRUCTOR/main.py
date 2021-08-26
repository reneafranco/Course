from coche import *

carro = Coche("Amarillo", "Lamborgini", "Gallardo", 300, 450, 2)

carro2 = Coche("Rojo", "ferrari", "portofino", 305, 478, 2)

carro3 = Coche("Verde", "Dodge", "Vipe", 318, 500, 2)

carro4 = Coche("Azul", "Lada", "2107", 150, 150, 4)


print(carro.getInformacion())
print(carro2.getInformacion())
print(carro3.getInformacion())
print(carro4.getInformacion())

#Detectar tipado de de la clase
if type(carro3) == Coche:
    print("Es un objeto correspondiente a la clase coche ")
else:
    print("el objeto no es de la clase coche")

print(carro.soy_publico)
