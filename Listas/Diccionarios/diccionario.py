"""
Diccionario: es un tipo de datos que almacena conjunto de datos 
en formato clave > valor """

personas = {
    "nombre": "Rene ", 
    "apellidos": "Franco",
    "web": "rene.com"
}

#Puedo acceder a los indices invocando la funcion y usando corchetes

#LISTA CON DICCIONARIOS

contactos = [
    {
        "nombre": "Rene",
        "apellidos": "rene@gmail.com"

    },
    {
        "nombre": "Luis",
        "email": "luis.com"
    },
    {
        "nombre": "victor",
        "email": "victor.com"
    }
]

print(contactos[0]["nombre"])

for contactos in contactos:
    print(f"El nombre es :  {contacto[ "nombre" ]} ")