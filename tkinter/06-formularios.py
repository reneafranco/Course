from tkinter import *

ventana = Tk()
ventana.title("Encabezado de Formulario")
ventana.geometry("700x400")

#Texto encabezado 
encabezado = Label(ventana, text="Formularios con Tkinter")
encabezado.config(
                fg="white",
                bg="darkgray",
                font=("Open Sans", 18), 
                padx=10,
                pady=10,                       
)
#para pegar los elemntos a un lado de la pantalla  usas sticky
#para dividir campo puedo usar columnspan
encabezado.grid(row=0, column=0, sticky=W, columnspan= 12 )

#Crear campo de texto (nombre)
#Para crearlo usas la funcion Entry y lo empaquetas donde quieras

#texto al lado del campo
label = Label(ventana, text="Introduce el nombre:")
label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

campo_texto = Entry(ventana) #(nombre)
#Para empaquetar parametros con presicion usas grid() e indicas row= filas y column=colunmas
campo_texto.grid(row=1, column=1, padx=5, pady=5, sticky=W)
campo_texto.config(justify="right", state="normal")

#Crear campo de texto (apellidos)
#Para crearlo usas la funcion Entry y lo empaquetas donde quieras

#texto al lado del campo
label = Label(ventana, text="Introduce el apellido:")
label.grid(row=2, column=0, padx=5, pady=5, sticky=W)

campo_texto = Entry(ventana) #(apellido)
#Para empaquetar parametros con presicion usas grid() e indicas row= filas y column=colunmas
campo_texto.grid(row=2, column=1, padx=5, pady=5, sticky=W)
campo_texto.config(justify="right", state="normal")

#texto al lado del campo GRANDE
label = Label(ventana, text="Descripcion:")
label.grid(row=3, column=0, padx=5, pady=5, sticky=NW)

#Campo de texto grande
campo_grande = Text(ventana)
campo_grande.grid(row=3, column=1, padx=4, pady=5, sticky=W)
#para cambiar el tamaño del campo tipo texto grande debes config
campo_grande.config(
        width=30,
        height=5 
)


ventana.mainloop()