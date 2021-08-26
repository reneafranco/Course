

class Coche:
    #crear propiedades(Variables)
    #Caracteristicas del objetos
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = int(300)
    caballaje = 500
    plazas = 2

    soy_publico = "Hola, soy un valor publico"
    __Soy_privado = "Hola, soy privado"


    #El primer metodo que se debe tener es un constructor
    #para poder pasarle los parametros sin tener la nesecitad de usar valores predefinidos

    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas
        
      
        
    #Metodos son acciones que hace el objeto creado (funciones)

    def accelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1
    
    def getvelocidad(self):
        return self.velocidad
    #tambien puedes definirte una funcion seter que es la encargada de cambiar el valor 
    def setColor(self, color):
        self.color = color 
    #tambien puedes hacer un metodo geter que es el encargado de conseguir informacion
    def  getColor(self):
        return self.color
    #mas ejemplos
    def setModelo(self, modelo):
        self.modelo = modelo  
    def getModelo(self):
        return self.modelo
    def setMarca(self, marca):
        self.marca = marca
    def getMarca(self):
        return self.marca 
    def getInformacion(self):
        
        info = ("****INFORMACION****")
        info += "\n Color: " + self.getColor()
        info += "\n Marca: " + self.getMarca()
        info += "\n Modelo: " + self.getModelo()
        info += "\n Velocidad: " + str(self.getvelocidad()) + " km/h"
    
        return info