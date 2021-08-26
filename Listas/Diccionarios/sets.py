"""es un tipo de datos q no tienen indice y ningun orden es para tener una coleccion de valores"""

personas = {"Rene", "Victor", "Manolo"}
print(personas)
print(type(personas))

personas.add("paco")

print(personas)

personas.remove("Manolo")

print(personas )