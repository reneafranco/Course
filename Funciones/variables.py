"""Una variable local es una variable definida dentro de la funcion
y solo puede ser usada dentro de la funcion

las variables globales estan definidas fuera de la funcion 
y pueden usarse dentro y fuera de la funcion"""
 
#Variables globales

frase = "Ni los genios son tan genios, ni los mediocres tan mediocres"
print(frase)

def HolaMundo():
    frase = "Hola mundo"
    print(frase)

HolaMundo()

