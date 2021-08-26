texto = "HOLA"
numeros = int(2)
lista = ["alberto el bailarin"]
boleano = True

def ejercicio():
    if isinstance(texto, str):
        print("La variable texto es un: ", type(texto))
    if isinstance(numeros, int):
        print("La variable numeross es un: ", type(numeros))
    if isinstance(lista, list):
        print(type(lista))
    if isinstance(boleano, bool):
        print(type(boleano))

ejercicio()