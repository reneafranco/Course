from io import open
import pathlib

#abrir archivo 
ruta = str(pathlib.Path().absolute()) + "/Sistema_de_archivos/fichero_texto.txt"
archivo = open(ruta, "a+")

archivo.write("*****Prueba**** \n")
archivo.write("*****Prueba**** \n")
archivo.write("*****Prueba**** \n")
archivo.write("*****Prueba**** \n")
archivo.write("*****Prueba**** \n")
archivo.write("*****Prueba**** \n")
archivo.write("*****Prueba**** \n")

archivo.close()