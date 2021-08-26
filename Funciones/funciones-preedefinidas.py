nombre = "Rene"

print(type(nombre))

#detectar el tipado
comprabar = isinstance(nombre, int)
if comprabar:
    print("esa variable es un string ")
else:
    print("esa variable no es un string")

if not isinstance(nombre, float):
    print("La variable no es un numero con decimales")


#Funciones para trabajar con str

frase = "   mi contenido   "
print(frase)
print(frase.strip())

#eliminar variables
year = 2021 
del year
#print(year)

# comprobar variables vacias
texto = "  ff  "

if len(texto) <= 0:
    print("la variable esta vacia")
else:
    print("la variable tiene: ", len(texto))

#encontrar caracteres dentro de un str
frase = "la vida es bella"

print(frase.find("vida"))

#reemplazar palabras en un str
nueva_frase = frase.replace("vida","moto")
print(nueva_frase)

#procesar mayusculas y minisculas 
print(nombre)
print(nombre.lower())
print(nombre.upper())

nom
    