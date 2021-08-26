from tkinter import *

ventana = Tk()
ventana.geometry("600x600")

#Menu principal 
mi_menu = Menu(ventana)
#debes decirle a la venta q quieres crear un menu e indicarle cual de todos los menus es 
ventana.config(menu=mi_menu)

#menu secundario o el menu para desplegar
#le indicas al menu secundario en cual menu quieres agregarlo
archivo = Menu(mi_menu, tearoff=0) #el segundo parametro es para evitar q te salga una linea antes del menu desplegable
#luego le añades comandos a tu menu secundario los command son como las opciones 
archivo.add_command(label="Nuevo archivo ")
archivo.add_command(label="Nuevo ventana ")
#para separar los elementos en el menu secundario usas 
archivo.add_separator()
archivo.add_command(label="abrir archivo")
archivo.add_command(label="abrir carpeta")
archivo.add_separator()
archivo.add_command(label="Salir", command=ventana.quit) # esta funcion se utiliza para cerrar el programa


#luego tienes q indicarle al menu principal
#en el q tiene cascade pasarle el menu secundario como parametro
mi_menu.add_cascade(label="Archivo", menu=archivo)
mi_menu.add_command(label="Editar")
mi_menu.add_command(label="Seleccion")

ventana.mainloop()