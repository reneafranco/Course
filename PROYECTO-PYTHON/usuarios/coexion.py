#para conectarte a la base de datos y poder hacer consultas sql primero debes enlasar los argumentos con la base de datos 
import mysql.connector

def conectar():
    database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Rene2516",
    database = "master_python",
    port = 3306
    )

    #para comprobar si la conexion ha salido bien solo haces
    #print(database)

    #para poder hacer las consultas sql nesecitas crearte un cursor
    cursor = database.cursor(buffered=True)

    return [database, cursor]