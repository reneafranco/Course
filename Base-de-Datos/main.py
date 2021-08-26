import mysql.connector

#hacer conexion 

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Rene2516",
    database = "master_python"
)

#Para comprobar que en el enlase salio bien haces un print
print(database)

cursor = database.cursor(buffered=True)#SE pone para cunado ejecutes diferentes consultas con el cursos no te de errores 

"""#Crear base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

#PARA SABER SI SE CREO
cursor.execute("SHOW DATABASES")

#ver el contenido de las bases de datos agregadas en el cursor 
for bd in cursor:
    print(bd)"""

#como crear tablas 
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) AUTO_INCREMENT NOT NULL,
    marca varchar(40) not null,
    modelo VARCHAR(40) not null,
    precio float(10,2) not null, 
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")

#Como instertar datos en una tabla 

#cursor.execute("INSERT INTO vehiculos VALUES(null,'ferrari', 'portofino', '280.00')")
#database.commit()

#Instertar datos de manera masiva 
lista =[
    ('Lamborgini', 'huracan', '36000'),
    ('Maserati', 'Tacate los huevis', '25000')
]

#cursor.executemany("INSERT INTO vehiculos VALUES (NULL, %s, %s, %s)", lista)
database.commit()

#como sacar los datos de una tabla 
cursor.execute("SELECT * FROM vehiculos")
#hago una variable para poder extraer el resutado 
result = cursor.fetchall()

for carros in result:
    print(carros)

#como borrar datos 
cursor.execute("DELETE FROM vehiculos WHERE marca = 'Lamborgini'")
database.commit()

#otra manera de ver q ha borrado es ejecutar esto 
print(cursor.rowcount, "borrados!!!") #Esto te dira cuantos registros se borraron 

#Como actualizar datos ya existentes 
cursor.execute("UPDATE vehiculos SET modelo = 'F150' WHERE modelo = 'portofino'")
database.commit()
print(cursor.rowcount, "Actualizados!!!")#Esto sirve para tener un conteo de todo lo que cambia en las tablas
