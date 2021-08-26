print("------------------------------")
print("--Bienvenido a la pizeria Bella Napol--")
print("-------------------------------\n")

print("Actualmente ofrecemos pizzas veganas\n")
print("Seleccione 1 para pizzas regulares")
print("Seleccione 2 para pizzas veganas\n")

seleccion = input("Ingrese q clase de pizza desea ordenar: ")

def regular():
    print("has elegido pizzas regulares")
    print("""
    Actualmente solo puedes elegir un ingrediente
    Seleccione:
    1-para agregar peperoni
    2-para jamon
    3-para salmon""")


def vegana():
    print("has elegido pizzas vegana")
    print("""
    Actualmente solo puedes elegir un ingrediente
    Seleccione:
    1-para agregar Pimiento 
    2-para agrgar Tofu""")

pizza = ["Mozarella", "tomate"]

if seleccion == "si":
    regular()
    ingrediente = int(input("eliga el ingrediente que desea agregar: "))
    if ingrediente == 1:
        pizza.append("peperoni")
        print("la pizza es regular", pizza)