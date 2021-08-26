from tkinter import *

ventana = Tk()

ventana.title("Textos")

ventana.geometry("720x480")

texto = Label(ventana, text='Bienvenido a mi programa' )
texto.pack()

texto = Label(ventana, text='Soy Rene Franco' )
#tambine puedo configurar el texto a mi antojo
#Puedo usar la funcion config y pasarle key_argument q son parametros especiales de esas funciones
texto.config(
            fg="white", #color de la letra
            bg="black", #color del backgraund
            padx=20   , #pad es margen y la x o y indican el eje en el q quieres poner margen
            font=("Arial, 30"), #puedo cambiarle el tipo de letra y el tamaño q quiero q esta tenga
            #width= 40, #puedo definir anchura 
            #height= 40,#puedo definir altura
            cursor="circle", #puedo pasarle esto para q cada vez que el mause pase x encima del texto cambie su figura

 )
texto.pack()

def prueba(nombre, apellidos, pais):
    return f"Hola {nombre} {apellidos} veo que eres de {pais} "



texto = Label(ventana, text=prueba("Rene","Franco","Cuba") )
#tambine puedo configurar el texto a mi antojo
#Puedo usar la funcion config y pasarle key_argument q son parametros especiales de esas funciones
texto.config(
            fg="white", #color de la letra
            bg="orange", #color del backgraund
            padx=20   , #pad es margen y la x o y indican el eje en el q quieres poner margen
            font=("Arial, 30"), #puedo cambiarle el tipo de letra y el tamaño q quiero q esta tenga
            #width= 40, #puedo definir anchura 
            #height= 40,#puedo definir altura
            cursor="circle", #puedo pasarle esto para q cada vez que el mause pase x encima del texto cambie su figura
            
 )
texto.pack(anchor=W)






ventana.mainloop()