#importar modulo

import sqlite3

#enlasar base de datos con el archivo principal

conexion=sqlite3.connect("prueba.db")

"""Para hacer consultas a una base de datos debes crear un cursor 
de la siguiente manera """

cursor = conexion.cursor()

#crear tabla 
"""Para crear una tabla debes usar la funcion cursor.execute(luego entre estos parentesis
poner en letras mayusculas y entre" las letas y condiciones luego poner el nombre )
ejemplo: """

cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"ID int(10) AUTOINCREMENT not null, " #la coma siempre debe ir dentro de las comillas
"Titulo VARCHAR(255), " +
"Descripcion TEXT, " + #el tipo de dato q valla a ser la columna puede ir el mayuscula o en minuscula
"Precio int(255)"+
")")

#Cerrar enlace
conexion.close()