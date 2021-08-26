from tkinter import *
from tkinter import messagebox as Messagebox

ventana = Tk()
ventana.title("Calculadora")
marco = Frame(ventana, width=500, height=500)
marco.config(
        bd=15,
        relief="solid"
        
)
marco.pack()

result = StringVar()
def Suma():
    try:
        result.set(float(numero1.get())+float(numero2.get()))
        mostrar()
    except:
        mostrar_error()
def Resta():
    try:
        result.set(float(numero1.get())-float(numero2.get()))
        mostrar()
    except:
        mostrar_error()

def Divicion():
    try:
        result.set(float(numero1.get())/ float(numero2.get()))
        mostrar()
    except:
        mostrar_error()

def Multiplicacion():
    try:
        result.set(float(numero1.get())*float(numero2.get()))
        mostrar()
    except:
        mostrar_error()
        
def mostrar():
    Messagebox.showinfo("Resultado",f" {result.get()} ")
    numero1.set("")
    numero2.set("")

def mostrar_error():
    Messagebox.showerror("Erro","Introdusca bien los datos")
    numero1.set("")
    numero2.set("")


numero1 = StringVar()
numero2 = StringVar()

Label(marco, text="Numero 1:").pack()
Entry(marco, textvariable=numero1).pack()
Label(marco, text="numero 2:").pack()
Entry(marco, textvariable=numero2).pack()
Label(marco).pack()

boton1= Button(marco, text="Suma", command=Suma).pack(side=LEFT, fill=X, expand=YES)
boton2= Button(marco, text="Resta",command=Resta).pack(side=LEFT, fill=X, expand=YES)
boton3= Button(marco, text="Divicion",command=Divicion).pack(side=LEFT, fill=X, expand=YES)
boton4= Button(marco, text="Multiplicacion", command=Multiplicacion).pack(side=LEFT, fill=X, expand=YES)

ventana.mainloop()
