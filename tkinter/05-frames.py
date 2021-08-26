from tkinter import *  

ventana = Tk()
ventana.title("FRAMES")
ventana.geometry("700x700")


marco_padre = Frame(ventana, width=250, height=250)

marco_padre.pack(side=BOTTOM,anchor=S, fill=X, expand=YES)  


marco = Frame(marco_padre, width=250, height=250)
marco.config(
        bg="red",
        bd=5,
        relief="solid",
)
marco.pack(side=LEFT)

texto = Label(marco, text="Primer marco")
texto.config(
                bg="red",
                fg="white",
                font=("Arial", 20),
                #height=10,
                #width=10,
                anchor= CENTER,
                bd=3,
                relief = SOLID

)
texto.pack(fill=Y, expand=YES)
marco.pack_propagate(False) #esto es para q el marco no cambie de tamaño 

marco = Frame(marco_padre, width=250, height=250)
marco.config(
        bg="green",
        bd=5,
        relief="solid"
)
marco.pack(side=RIGHT)



marco_padre2 = Frame(ventana, width=250, height=250)

marco_padre2.pack(side=BOTTOM,anchor=N, fill=X, expand=YES)  

marco = Frame(marco_padre2, width=250, height=250) 
marco.config(
        bg="blue",
        bd=5,
        relief="solid"
)
marco.pack(side=LEFT)

marco = Frame(marco_padre2, width=250, height=250) 
marco.config(
        bg="orange",
        bd=5,
        relief="solid"
)
marco.pack(side=RIGHT)




ventana.mainloop()
