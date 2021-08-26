from tkinter import *
from tkinter import messagebox as Messagebox


class Calculadora:
    
    def __init__(self, alertas):
            self.numero1 = StringVar()
            self.numero2 = StringVar()
            self.result = StringVar()
            self.alertas = alertas

    def Suma(self):
        try:
            self.result.set(float(self.numero1.get())+float(self.numero2.get()))
            self.mostrar()
        except:
            self.mostrar_error()
    def Resta(self):
        try:
            self.result.set(float(self.numero1.get())-float(self.numero2.get()))
            self.mostrar()
        except:
            self.mostrar_error()

    def Divicion(self):
        try:
            self.result.set(float(self.numero1.get())/ float(self.numero2.get()))
            self.mostrar()
        except:
            self.mostrar_error()

    def Multiplicacion(self):
        try:
            self.result.set(float(self.numero1.get())*float(self.numero2.get()))
            self.mostrar()
        except:
            self.mostrar_error()
            
    def mostrar(self):
        self.alertas.showinfo("Resultado",f" {self.result.get()} ")
        self.numero1.set("")
        self.numero2.set("")

    def mostrar_error(self):
        self.alertas.showerror("Erro","Introdusca bien los datos")
        self.numero1.set("")
        self.numero2.set("")

ventana = Tk()
ventana.title("Calculadora")
marco = Frame(ventana, width=500, height=500)
marco.config(
        bd=15,
        relief="solid"
        
)
marco.pack()
calculadora = Calculadora(Messagebox)

Label(marco, text="Numero 1:").pack()
Entry(marco, textvariable=calculadora.numero1).pack()
Label(marco, text="numero 2:").pack()
Entry(marco, textvariable=calculadora.numero2).pack()
Label(marco).pack()

boton1= Button(marco, text="Suma", command=calculadora.Suma).pack(side=LEFT, fill=X, expand=YES)
boton2= Button(marco, text="Resta",command=calculadora.Resta).pack(side=LEFT, fill=X, expand=YES)
boton3= Button(marco, text="Divicion",command=calculadora.Divicion).pack(side=LEFT, fill=X, expand=YES)
boton4= Button(marco, text="Multiplicacion", command=calculadora.Multiplicacion).pack(side=LEFT, fill=X, expand=YES)

ventana.mainloop()
