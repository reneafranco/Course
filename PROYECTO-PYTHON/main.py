#PRIMEROS PASOS
#1 preguntas basicas del asistente 

from usuarios import acciones 
print("""
Acciones disponibles:
-Login
-Registro 
""")

#Aqui materialisas la clase 
hazEl = acciones.Acciones()
accion = input("Que quieres hacer?: ")
accion.lower()

if accion == "registro":
    hazEl.registro()

elif accion == "login":
    hazEl.login()


else:
    print("Debes seleccionar una de las 2 opciones anteriores")
 

 