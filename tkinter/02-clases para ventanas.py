"""Puedes crearte una clase que tenga todas las caracteristicas 
de la ventana es decir q llamando la clase ya tengas predefinido 
un molde para la ventana """
from tkinter import *
import os.path 


class Programa:
    #luego de esto te defines un constructor para pasarle todos los parametros
    def __init__(self):
        self.title = "Master en Python"
        self.icon = './imagenes/descarga.ico'
        self.icon_alt = './tkinter/imagenes/descarga.ico'
        self.size = "770x470"
        self.resizable = False
    
    def cargar(self):
        
        #Crear ventana
        ventana = Tk()
        #puedes hacer q ventana sea una propiedad q pueda ser utilizada en otros metodos
        self.ventana = ventana

        #porner titulo a ventana
        ventana.title(self.title)

        #definir ruta del icono 
        ruta_icono = os.path.abspath(self.icon)

        #definir ruta alternativa por si no me encuentra el icono 
        #defino ruta absoluta copn path 
        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon_alt)

        #mostar incono 
        ventana.iconbitmap(ruta_icono)

        #mostrar texto
        texto = Label(ventana, text = ruta_icono)
        #imprimir texto en pantalla 
        texto.pack()

        #Dar dimensiones a la ventana 
        ventana.geometry(self.size)

        #Definir si la ventana se puede redimencionar 
        if self.resizable:
            ventana.resizable(0,0)
        else:
             ventana.resizable(1,1)

      
    #Luego puedes crearte infinidad de metodos q hagan cosas q quieras y luego llamarlos
    def addTexto(self, dato):
        texto = Label(self.ventana, text =dato)
        texto.pack()

    #Para no confundirte puedes hacer el mainloop al final para q despues q hagas todo puedas cargarlo y asi no te de errores
    def mostrar(self):
        #importante q esto sea lo ultimo xq es el mainloop q ejecuta la ventana 
        self.ventana.mainloop()


# Por ultimo puedes instanciar el objeto 
programa = Programa()
#luego llamas la funcion que carga el programa
programa.cargar()
programa.addTexto("Hola soy Rene ")
programa.addTexto("vamos a smpamear")
programa.addTexto("luego crearemos un virus sencillo")
programa.mostrar()
# Un dato super interesante es q si quieres ejecutarlo
#es decir ejecutarlo desde afuera sin q python se ejecute
#solo le cambias el nombre al final x pyw 