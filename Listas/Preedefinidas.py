cantantes = ["2pac", "drake", "Julio Iglesias"]
numeros = [1 ,2 ,5 ,7 ,8 , 4]

print(numeros)
numeros.sort()
print(numeros)

#añadir elementos
cantantes.append("Disturb")
print(cantantes)
cantantes.insert(1, "BVB") # para colocar elementos de una manera especifica
print(cantantes)

#eliminar elementos de la lista 
cantantes.pop(0)
print(cantantes)

cantantes.remove("drake")
print(cantantes)

#dar la vuelta al orden de la lista 
numeros.reverse()
print(numeros)

#buscar resultadoos en una lista 
print("BVB" in cantantes) # y la respuesta sale true o false diciendote si esta o no ahi

# contar elementos 
