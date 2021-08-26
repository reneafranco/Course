from clases import *

personas = persona()
personas.setNombre("Rene")
personas.setApellidos("Franco")
personas.setAltura(178)
personas.setEdad(200)

print(f"La persona es {personas.getNombre()} {personas.getApellidos()} ")

informatica = informatico()
informatica.setNombre("Paquito")
informatica.setApellidos("Cabezon")
informatica.setAltura(160)
informatica.setEdad(30)

print(f"La persona es : {informatica.getNombre()} {informatica.getApellidos()} ")

