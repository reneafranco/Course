import notas.nota as modelo



 
class Acciones:

    def crear(self,usuario): #le paso el parametro usuario para saber quien esta creando las notas y haciendo cambio
        print(f"ok {usuario[1]}, vamos a crear una nueva nota ")
        titulo = input("Itroduce un titulo para la nota: ")
        descripcion = input("Instroduce el contenido de tu nota ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        #luego comprueba 

        if guardar[0] >= 1:
            print(f"Perfecto {usuario[1]}!! has guardado la nota: {nota.titulo} ")
        else:
            print("No salio bien")
    
    def mostrar(self, usuario):
        print(f"\nVale {usuario[1]}, aqui tienes tu nostas:  ")

        #create un objeto para instanciar la funcion
        nota = modelo.Nota(usuario[0], "", "")
        notas = nota.listar()
        #para mostrar las notas ordenadas usas un for

        for nota in notas:
            print("\n******************************")
            print(f"titulo: {nota[2]} ")
            print(f"descripcion: {nota[3]} ")
            print(f"fecha: {nota[4]} ")

    def borrar(self, usuario):
        print(f"\n OK {usuario[1]}, vamos a borrar notas")
        titulo = input("Introcude el titulo de la nota a borrar: ")
        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()  

        if eliminar[0] >= 1: 
            print(f"Hemos borrado la nota {nota.titulo} ")
        else:
            print("No se ha borrado nada ")