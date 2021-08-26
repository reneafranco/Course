#Esto es un modelo ...es decir lo q va a interactuar con la base de datos es decir crear y eliminar
import usuarios.coexion as conexion 

#esto es para enlasar la base de datos a este archivo
connect = conexion.conectar() #creas una variable para establecer el metodo conectar
database = connect[0] # creas una variable database y accedes a tu database que esta guardada en el indice 0
cursor = connect[1] #luego creas y accedes a tu cursor que es el indice 1


class Nota:

    def __init__(self, usuario_id, titulo = "", descripcion = ""):#estos son los datos q voy a estar llenando cada vez q agrege una nota 
        #(lo de arriba es el constructor, ahora toca rellenarla para eso hacemos)
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion

        #una ves echo esto debes definirte un metodo para guardar los datos 
    def guardar(self): #aqui ya vamos a hacer consultas a la base de datos para eso importas los otros modulos  
        sql = "INSERT INTO notas VALUES(NULL, %s,  %s, %s, NOW())"
        #la variable de arriba es para hacer los cambios en la base de datos 
        #luego te creas otra variable q contenga los datos y luego lo puedes ejecutar con el cursor 
        nota = (self.usuario_id, self.titulo, self.descripcion)
        #ya luego de esto puedes hacer la consulta con el cursor 
        cursor.execute(sql,nota)
        database.commit()

        return [cursor.rowcount , self]
        #Y CON ESTO YA TIENES EL METODO DE GUARDAR


    def listar(self):
        sql = f"SELECT * FROM notas WHERE usuario_id = {self.usuario_id} "  
        cursor.execute(sql)
        result = cursor.fetchall()

        return result

    def eliminar(self):
        sql = f"DELETE FROM notas WHERE usuario_id = {self.usuario_id} AND titulo LIKE '%{self.titulo}%'"

        cursor.execute(sql)
        database.commit()

        return [cursor.rowcount, self]


