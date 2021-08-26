from tkinter import *
from tkinter import ttk

#Definir ventana
ventana = Tk()
ventana.geometry("500x500")
ventana.resizable(0,0)
ventana.title("Proyecto Tkinter Python")

#Pantallas
#cada pantalla sera una funcion q cargue de acuerdo al click del usuario
def home():
    #Montar pantallas
    
    home_label.config(
                fg="white",
                bg ="black",
                font=("Arial", 30),
                padx=205,
                pady=20
    )
    home_label.grid(row=0, column=0)
    add_home.grid(row=1)

    #Listar los datos para q aparescan
    for product in products:
        if len(product) == 3:
            product.append("added")
            Label(add_home, text=product[0]).grid()
            Label(add_home, text=product[1]).grid()
            Label(add_home, text=product[2]).grid()
            Label(add_home, text="------------").grid()

    #Ocultar pantallas anteriores
    add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    add_frame.grid_remove()

    return True

def add():
    #Encabezado

    add_label.config(
                fg="white",
                bg ="black",
                font=("Arial", 30),
                padx=80,
                pady=20
    )
    add_label.grid(row=0, column=0, columnspan=4)

    #Campos del formulario
    add_frame.grid(row=1)
    add_name_label.grid(row=1, column=0, padx=5, pady=15,sticky=E)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5,sticky=W)

    add_price_label.grid(row=2, column=0, padx=5, pady=5,sticky=E)
    add_price_entry.grid(row=2, column=1, padx=5, pady=5,sticky=W)

    add_description_label.grid(row=3, column=0,padx=5, pady=5,sticky=NE)
    add_description_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    add_description_entry.config(
                width=30,
                height=5,
                font=("Consolas", 12),
                padx= 12,
                pady= 8
    )
    boton.grid(row=5, column=1,padx=5, pady=3, sticky=W)
    boton.config(
                cursor="hand2",
                bg="green",
                fg="White"
    )
    add_sepatrator.grid(row=4, column=1)

    #Ocultar pantallas anteriores
    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    add_home.grid_remove()
    return True

def info():
    
    info_label.config(
                fg="white",
                bg ="black",
                font=("Arial", 30),
                padx=170,
                pady=20
    )

    info_label.grid(row=0, column=0)
    data_label.grid(row=1, column=0)

    #Ocultar pantallas anteriores
    add_label.grid_remove()
    home_label.grid_remove()
    add_frame.grid_remove()
    add_home.grid_remove()
    return True

def add_products():
    products.append([
        name_data.get(),
        price_data.get(),
        add_description_entry.get("1.0", "end-1c")
    ])
    name_data.set("")
    price_data.set("")
    add_description_entry.delete("1.0", END)

    home()


#Variables importantes 
name_data = StringVar()
price_data = StringVar()
products = []

#Definir campos de pantalla Inicio
home_label = Label(ventana, text="Inicio")

#Definir campos de pantalla Inicio
add_label = Label(ventana, text="Añadir Producto")

#Definir Campos del formulario
add_frame = Frame(ventana)
add_name_label = Label(add_frame, text="Nombre:")
add_name_entry = Entry(add_frame,textvariable=name_data)

add_price_label = Label(add_frame, text="Precio:")
add_price_entry = Entry(add_frame,textvariable=price_data)

add_description_label = Label(add_frame, text="Descripcion:")
add_description_entry = Text(add_frame)

boton = Button(add_frame, text="Guardar", command=add_products)
add_sepatrator = Label(add_frame, text="")

#Definir campos de pantalla Inicio
info_label = Label(ventana, text="Informacion")
add_home = Frame(ventana, width=250)

data_label = Label(ventana, text="Creador Date_Medusa")

#Cargar pantalla inicio
home()

#Definir Menu Superior
menu_superior = Menu(ventana)

menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir",command=add)
menu_superior.add_command(label="Informacion",command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)

#cargar menu superior
ventana.config(menu=menu_superior)

ventana.mainloop()