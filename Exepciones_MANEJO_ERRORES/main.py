#capturar exepciones o errores en codigo suceptible
"""try:
    nombre = input("Cual es tu nombre : ")

    if len(nombre) >= 1:
        nombre_usuario = "el nombre es ",nombre
    print(nombre_usuario)
except:
    print("ha ocurrido un error")
else:
    print("todo ha ido bien")
finally:
    print("fin del programa")""" 

#multiples errores
"""try:
    numero = int(input("Numero para elevarlo al cuadrado: "))
    print("el cuadrado del numero es " + str(numero*numero))
except TypeError:
    print("Debes convertir tus cadenas a enteros")
    except ValueError:
    print("introduce un numero correcto")
except Exception as e:
    print("Ha ocurrido un error: ", type(e).__name__)"""

#exepciones personalisadas

nombre = input("Introduce el nombre: ")
edad = int(input("Introduce la edad: "))

try:
    if edad < 5 or edad > 100:
        raise ValueError("la edad introducida no es real ")
    if len(nombre) <= 1 or nombre != str():
        raise TypeError("el nombre no es correcto: ")
    else:
        print(f"Bienvenido al master {nombre} ")
except ValueError:
    print(f"La edad no es correcta {edad} ")
except TypeError:
    print("El nombre no es correcto ({})".format(nombre))



 