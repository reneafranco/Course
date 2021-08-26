""" Aqui puedes crear una clase donde agrupes
todas las funciones para que sea mas facil llamarlas"""
import notas.acciones
import usuarios.usuario as modelo
#AS es para cambiarle el nombre en esta pagina y te sea mas facil invocarlo 


class Acciones:
#ya aqui puedes definirte los diferentes metodos 

    def registro(self):
        print("\nOk!! Vamos a registrarte en el sistema ...")

        nombre = input("Cual es tu nombre?: ")
        apellidos = input("Cuales son tus apellidos?: ")
        email = input("Cual es tu email?: ")
        password = input("Cual deseas que sea tu password?: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        #para registrar este objeto que me he creado solo debo hacerme una variable y usar el metodo que quira
        #ojo no lo guardo porque ya usuario esta usando la funcion 
        registro =  usuario.registrar()

        if registro[0] >= 1:
            print(f"\nperfecto {registro[1].nombre} te has registrado con el email {registro[1].email} ")
        else:
            print("No te has registrado correctamente, el email utilizado ya pertenece a otra cuenta  !!!!")

    def login(self):
        print("\nOk!! Vamos a entrar en el sistema...")
        try:
            email = input("Cual es tu email?: ")
            password = input("Cual es  tu password?: ")

            #aqui creas un objeto con para las funciones q hiciste en los modulos
            usuario = modelo.Usuario('', '', email, password)
            login = usuario.indentificar()

            #luego comprueba q todo esta bien 
            if email == login[3]:
                print(f"bienvenido {login[1]} ,te has registrado con en el sistema el {login[5]}  ")
                self.proximasAcciones(login)
        except Exception as e:
            print(type(e)) 
            print(type(e).__name__)   
            print(f"login incorrecto!!! intentalo mas tarde ")

        
    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
        -Crear nota (crear)
        -Mostrar tus notas (mostrar)
        -Eliminar notas (eliminar)
        -Salir (salir)
        """)


        accion = input("Que quieres hacer?: ")
        #para poder utlizar el metodo que importe debo crearme una variable para instaniar el obejto 
        hazEl = notas.acciones.Acciones()

        if accion == "crear":
            #aqui puedo llamar al obejto q me cree para instanciar el modelo 
            hazEl.crear(usuario)
            #para hacer que el asistente se mantenga preguntandote solo tienes q llamar al metodo
            self.proximasAcciones(usuario)#debes pasarle el usuario tb 

        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "salir":
            print(f"ok {usuario[1]}, hasta pronto! ")
            exit()
        else:
            print("\nComando no disponible")
        