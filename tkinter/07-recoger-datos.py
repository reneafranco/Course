from tkinter import *

ventana = Tk()
ventana.title("Recoger datos")
ventana.geometry("700x700")
ventana.config(
        bd=50,
        bg="#ccc"
)

def getDato():
    resultado.set(dato.get())
dato = StringVar()
resultado = StringVar()


Label(ventana, text="Mete un texto: ").pack( anchor= NW)
Entry(ventana, textvariable=dato).pack(anchor=NW)

Label(ventana, text="Dato recogido: ").pack( anchor= NW)
Label(ventana, textvariable= resultado).pack( anchor= NW)

#para darle funcionalida a un boton debes lamar la funcion a traves de command = funcion
#si a la funcion debes pasarle parametros debes usar un lambda es decir command= lambda(funcion())
Button(ventana, text="Mostar dato",command=getDato).pack(anchor=NW)

ventana.mainloop()