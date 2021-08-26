"""listas = arreglos para acceder a ella podemos usar indice numericos"""

pelicula = "Batman"
#definir lista
peliculas = ["batman", "Spiderman", "Señor de los anillos"]
cantantes = list(("2pac", "Drake", "Lopez"))
years = list(range(2020,2050))
variada = ["Rene", 30, 4.4, True, "Texto"]

print(pelicula)
print(peliculas)
print(cantantes )
print(years)
print(variada)

#Indices, como acceder a cada uno de ellos en especificos

print(peliculas[1])
print(peliculas[-2])# tambien puedes acceder poniendolos de forma negativa pero ahi empieza a contar de atrs hacia adelante
print(cantantes[0:3]) # puedes hacer como un mini rango de esta forma te muestras los indices q quieras
print(peliculas[1:]) #puedo hacer un rango sin final usando esto 

#Puedes cambiar el valor q hay en determinado indice usando esto 
peliculas[1] = "Gran Torino "
print(peliculas)

#como añadir elementos a un lista debes usar un metodo en contreto .append
cantantes.append("Kase O")
print(cantantes)

#recorrer lista con bucle for 
"""
nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce nueva pelicula: ")
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

for pelicula in peliculas:
    print(pelicula)
    print(f" {peliculas.index(pelicula)}.  {pelicula} ")"""

# ejemplo listas multidimensionales 
# Es una lista q contiene dentro otras litas 

#print("Lista de contactos ")

contactos = [
    [
        'luis',
        'luis@luis.com'
    ],
    [
        "rene", "reneadonay@gmail.com"
    ]
]

print(contactos)
print(contactos[0][1])