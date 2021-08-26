from tkinter import *

ventana = Tk()
ventana.geometry("700x500")
ventana.title("Formularios 2")

encabezado=Label(ventana, text="Formularios 2")
encabezado.config(
    padx=15,
    pady=15,
    fg="white",
    bg ="green",
    font=("Arial", 20 )
)
encabezado.grid(row=0, column=0, sticky=W, columnspan=5)

def mostrarprofecion():
    texto = ""

    if web.get():
        texto += "Desarrollo web"
    
    mostrar.config(
        text=texto,
        bg="green",
        fg="white"
        )

    if python.get():
        texto += "Python developer"
    
    mostrar.config(text=texto)

#Botones Check o Checkbo en html

web = IntVar()
python = IntVar()
Label(ventana, text="A que te dedicas?").grid(row=1, column=1, sticky=W)
Checkbutton(ventana,
         text="Desarrollo web",
         variable=web,
         onvalue=1,
         offvalue=0,
         command=mostrarprofecion
         ).grid(row=2, column=1, sticky=W)

Checkbutton(ventana, 
text="Python devoluper",
    variable=python,
    onvalue=1,
    offvalue=0,
    command=mostrarprofecion
).grid(row=3, column=1, sticky=W)

mostrar = Label(ventana)
mostrar.grid(row=4, column=0)

#Radio Button
opcion = StringVar()
opcion.set(None)

def marcardo():
    marcar.config(
        text=opcion.get()
    )

Label(ventana, text="Cual es tu sexo? ").grid(row=5)
Radiobutton(
    ventana,
    text="masculino",
    value="masculino",
    variable=opcion,
    command=marcardo
    ).grid(row=6)

Radiobutton(
    ventana,
    text="femenino",
    value="femenino",
    variable=opcion,
    command=marcardo
    ).grid(row=7)

marcar = Label(ventana)
marcar.grid(row=8)

#option menu
option = StringVar()
option.set("Opcion 1")
Label(ventana, text="Selecciona una opcion? ").grid(row=5, column=1)

select = OptionMenu(ventana,option, "Opcion 1","Opcion 2", "Opcion 3")
select.grid(row=6, column=1)
ventana.mainloop()