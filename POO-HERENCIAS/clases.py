"""Herencia: es la posibilidad de compartir atributos y metodos 
entre clases . Y que diferentes hereden de otras """

class persona:
    """
    nombre 
    apellidos 
    altura 
    edad 
    """ 

    def getNombre(self):
        return self.nombre
    
    def getApellidos(self):
        return self.apellidos
    
    def getAltura(self):
        return self.altura 
    
    def getEdad(self):
        return self.edad
    
    def setNombre(self, nombre):
        self.nombre = nombre
    def setApellidos(self, apellidos):
        self.apellidos = apellidos
    def setAltura(self, altura):
        self.altura = altura
    def setEdad(self, edad):
        self.edad = edad
    
    def hablar(self):
        return "Estoy hablando"
    def caminar(self):
        return "Estoy caminando"
    def dormir(self):
        return "Estoy durmiento"

class informatico(persona):
    """
    lenguaje
    experiencia
    """

    def __init__(self):
        self.lenguaje = "HTML, CSS, JAVASRIPT, PHP"
        self.experiencia = 5

    def getLenguajes(self):
        return lenguajes
    
    def aprender(self, lenguaje):
        self.lenguajes += lenguaje
        return self.lenguaje

    def programar(self):
        return "Estoy programando"
    
    def repararPC(self):
        return "Estoy reparando"


class tecnico(informatico):

    def __init__(self):
        super().__init__() #esto es para acceder a la constructor de la clase padre xq cada constructor es exclusivo
        self.auditar_redes = 'experto'
        self.experienciaRedes = 15