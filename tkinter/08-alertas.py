from tkinter import *
from tkinter import messagebox as Messagebox


ventana = Tk()
ventana.title("Alertas")
ventana.geometry("350x350")

def sacaralerta():
    #Existen 3 tipos de alerta:
    #1 Showinfo saca un cartelito con la bandera azul
    #2 Showwarning saca un cartelito con la bandera amarilla
    #3 Showerror saca un carletilo con la bandera roja 
    Messagebox.showinfo("Alerta", "Hola soy Cacharro")
    

Button(ventana, text="Mostrar alerta!!", command=sacaralerta).pack()

def salir(nombre):
    #tambien hay alertas q te permiten tomar una decicion como salir o continuar
    resultado = Messagebox.askquestion("Salir?", "Quieres seguir?")

    if resultado != "yes":
        #para mostrar una alerta al cerrar la app haces
        Messagebox.showinfo("Chao", f"Chao pescao {nombre} ")
        ventana.destroy()

Button(ventana, text="Salir", command=lambda: salir("Cacharro")).pack()


ventana.mainloop()
