from tkinter import *
from PIL import Image, ImageTk #esto lo importas para poder instanciar la imagen y luego cargarla  

ventana = Tk()
ventana.geometry("700x500")
ventana.title("Imagenes")
#para cargar imagenes tengo varias formas
#1 Puedo usar metos internos de tkinter 
#Usar Pillow

#cargar la imagen creando una variable con la ruta de la imagen
imagen = Image.open('./tkinter/imagenes/itachi.jpg')
#luego creas una variable para poder instanciar la imagen creada
render = ImageTk.PhotoImage(imagen)
#Luego tienes q pasar el render a un label para cargarlo en la pantalla 
texto = Label(ventana, image=render).pack()


ventana.mainloop()