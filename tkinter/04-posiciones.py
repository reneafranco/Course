from tkinter import *

ventana = Tk()
ventana.title("Posiciones")
#ventana.geometry("720x500")

texto = Label(ventana, text="Hola bienvenidos a mi programa")
texto.config(
            fg="white",
            bg="black",
            padx=30,
            font=("Arial, 30"),
            cursor="circle"
            
)
texto.pack(side=TOP)

texto = Label(ventana, text="Mi nombre es Rene")
texto.config(
            fg="white",
            bg="orange",
            font=("Arial, 30"),
            padx=30,
            cursor="circle"
            
)
texto.pack(side=TOP, expand=YES, fill=X)

texto = Label(ventana, text="basico1")
texto.config(
            fg="white",
            bg="blue",
            padx=30,
            font=("Arial, 20"),
            cursor="circle"
            
)
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text="basico2")
texto.config(
            fg="white",
            bg="pink",
            padx=30,
            font=("Arial, 20"),
            cursor="circle"
            
)
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text="basico3")
texto.config(
            fg="white",
            bg="green",
            padx=30,
            font=("Arial, 20"),
            cursor="circle"
            
)
texto.pack(side=LEFT, fill=X, expand=YES)

ventana.mainloop()