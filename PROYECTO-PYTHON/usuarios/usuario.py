"""Para que no engordes mucho los metodos 
de las otras clases te creas un modelo que se encargue de 
manejar los datos """
import usuarios.coexion as conexion  
import datetime
#para poder cifrar las contraseñas y que no te salgan como un texto plano debes usar un modulo de python 
import hashlib

#luego de q importe el modulo de conexion debo crear una variable para instanciar la funcion 
connect = conexion.conectar()
database = connect[0] #x eso hice el return para poder acceder a la conexion y al cursor x separados 
cursor = connect[1]

class Usuario:
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
    
    def registrar(self):
        fecha = datetime.datetime.now()
        #Para cifrar la contraseña primero debes rear una variable para instanciar el metodo hashlib
        cifrado = hashlib.sha256()
        #Luego usas el metodo update para que te actualise la variable contraseña y te la cifre
        cifrado.update(self.password.encode('utf8'))
        #Para cifrar el dato el metodo solo cifra datos en bits por eso debes convertir el str en bits con el encode
        #lo primero que debes hacer es crearte una variable para guardar tus consultas 
        sql = "INSERT INTO usuarios VALUES(NULL, %s, %s, %s, %s, %s)"
        #eso sirve para sustituir los valores por los de una tupla por lo que debes crearte una 
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)


        #para capturar los erores debes ver que parte del codigo es suceptible al codigo 
        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]   


        return result      
        
        #para ejecutar tu consulta o orden en sql debes usar el cursor q creaste 
        #cursor.execute(sql, usuario) #aqui sql es la consulta en especifico que quiero utilizar y usuario son los valores que quiero acompañar con esa consulta 
        #y para guardarla debes hacer el commit
        #database.commit()

        #luego de esto hago un ruturn con un rowcount, y luego el objeto mismo uso self para eso 
        #return [cursor.rowcount, self]


    def indentificar(self):
        #para verificar algo haces una variable con la condicion que quieras y le pones %s para luego sustituirlo
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s "

        #luego debes cifrar la contraseña con el mismo metodo que usaste antes 
        #xq en si la contraseña esta guardad pero esta cifrada 
        #so debes cifrarla para que se comparen

        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        #muy importante cuando creas la tupla para sustituir los datos recuerda no pasar contraseña
        #xq la cintraseña esta guardada y cifrada en la variable q usamos para cifrar..luego le pasas el hexdigest()
        usuario = (self.email, cifrado.hexdigest())

        #luego logica de ejecucion de consulta 
        cursor.execute(sql, usuario)
        #luego guardas la consulta en una variable 
        result = cursor.fetchone()

        return result 
