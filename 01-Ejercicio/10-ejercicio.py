alumnos = 0
aprobados = 0
desaprobados = 0

for alumnos in range(1,16):
    notas = int(input(f"Ingrese la nota del alumnos {alumnos} "))
    if notas > 6:
        aprobados += 1
    else:
        desaprobados += 1
print(f"Han aprobado {aprobados} alumnos")
print(f"Han desaprobado {desaprobados} alumnos ") 