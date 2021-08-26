#TKINTER
#MODULO PARA CREAR INTERFASES GRAFICAS PARA USUARIOS 

#Paso 1 importar el modulo 
from tkinter import *
import os.path
#crear na ventana RAIZ que es la ventana principal que el programa  va a cargar 
#paso 1 te creas un variable e instancias tk()

ventana = Tk()

#Poner titulo de la ventana
ventana.title("Interfaz grafica con Python")

#Comprobar si existe un archivo sacando la ruta absoluta
ruta_icono = os.path.abspath('./imagenes/descarga.ico')

if not os.path.isfile(ruta_icono):
    ruta_icono = os.path.abspath('./tkinter/imagenes/descarga.ico')


#como cargar un icono para la ventana OJO el archivo tiene que ser .ICO
#puedes poner la ruta absoluta o la relativ(la relativa es mas facil)
ventana.iconbitmap(ruta_icono)


#para mostrar algo dentro del programa haces

texto = Label(ventana, text = ruta_icono)
texto.pack()

#Puedes cambiarle el tamaño de inicio 
ventana.geometry("750x450")

#Para bloquear el tamaño es decir que sea un tamaño especifico 
ventana.resizable(0,0)


#Arrancar y mostrar ventana hasta que se cierre
#OJO es importante que este metodo sea el ultimo xq tienes si tienes q
#hacer cualquier modificacion 

ventana.mainloop()
