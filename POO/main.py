"""CLASE
una clase es un molde para crear varios objetos con caracteristicas parecidas
ATRIBUTOS
son las particulidades de la clase como nombre y propiedades
METODOS
son las funciones de la clase basicamente las funciones que le otorgues para que pueda realizarse"""

#Definir una clase (Molde para crear mas objetos de ese tipo) (coche ejemplo)

class Coche:
    #crear propiedades(Variables)
    #Caracteristicas del objetos
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = int(300)
    caballaje = 500
    plazas = 2
    
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

# Instanciar un objeto es crear un objeto fisico basado en el modelo de la clase
coche = Coche()
coche.setColor("amarillo")
coche.setModelo("Portofino")
print(coche.getMarca(), coche.getModelo(), coche.getColor())
print(coche.velocidad)

#llamar metodos(llamar funciones)(Ojo aqui interactuar directamente con el modelo)
#lo recomendable es alterar las propiedades del objeto en especifico para no alterar el molde
coche.accelerar()
coche.accelerar()
coche.accelerar()
coche.accelerar()
coche.frenar()

#crear multiples objetos con el mismo molde pero con propiedades y metodos parecidos mas no iguales


lambo = Coche()
lambo.setColor("negro")
lambo.setModelo("murcielago")
lambo.setMarca("Lamborgini")
print(lambo.getMarca(), lambo.getModelo(), lambo.getColor())



lambo.accelerar()
lambo.accelerar()
lambo.accelerar()
lambo.accelerar()
lambo.frenar()

print(lambo.getvelocidad()) 
