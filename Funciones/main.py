"""
FUNCIONES: Son un conjunto de intruciones agrupadas bajo un nombre concreto 
que puede utilizarse invocando la funcion tantas veces sea necesaria"""

# def nombre_de_mi_funcion(parametros): # puedo dejar el parentesis basio o puedo ponerle parametros 
    #bloque de codigo / instrucciones

#nombre_de_mi_funcion(mi_parametros) # y de esa manera puedes llamarla """"

#ejemplo 1

"""def muestraNombres():
    print("Rene")
    print("Adonay")
    print("Franco")
    print("Perez")

#invocar a la funion
muestraNombres()

#ejemplo 2: parametros """

"""def mostrartuNombre(nombre):
    print(f"tu nombre es: {nombre}")"""

"""nombre = input("Introduce tu nombre: ")
mostrartuNombre(nombre)"""

#Ejemplo 3

def tabla(numero):
    print(f" la tabla de multiplicar del numero:  {numero} ")
 
    for contador in range(11):
        operacion = numero * contador
        print(f" {numero} x {contador} = {operacion} ")

tabla(3)

#Ejemplo # 4 PARAMETROS OPCIONALES

def getEmpleado(nombre, ID = False): # para hacer q un parametro sea opcional solo debes ponerle al final del parametro = y valor q quieras darle
    print("empleado")
    print(f"nombre {nombre} ")
    print(f"ID {ID} ")

# ejemplo 6 parametros opcionales y RETURN

def saludame(nombre):
    saludo = f"hola, saludos {nombre} "

    return saludo

print(saludame("Rene adonay"))

def calculadora(numero1, numero2, basicas = False):

    suma = numero1 + numero2

    resta = numero1 - numero2 

    multi = numero1 * numero2

    divicion = numero1 / numero2

    cadena = " "
    cadena += "Suma: " + str(suma)
    cadena += "\n"
    cadena += "Resta: " + str(resta)
    cadena += "\n"
    cadena += "Multiplicacion: " + str(multi)
    cadena += "\n"
    cadena += "Divicion: " + str(divicion)

    return cadena

print(calculadora(5,5))

#Ejemplo 7
# Funciones dentro de otras funciones

def cogeNombre(nombre):
    texto = f"el nombre es {nombre} "
    return texto 

def cogeapellidos(apellidos):
    texto = f"los apellidos son {apellidos} "
    return texto 

def devuelvetodo(nombre, apellidos):
    texto = cogeNombre + cogeapellidos
    return texto

print(cogeNombre("Rene"), cogeapellidos("franco"))

#ejemplo 8 
# funciones lambda

dime_el_year = lambda year: f"EL año es {year * 2} "

print(dime_el_year(2032))
 

