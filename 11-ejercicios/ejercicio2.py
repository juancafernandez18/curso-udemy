"""
escribir un programa que añada valores a una lista
mientras que su longitud sea menor a 120 y luego mostrar la lista
usar while y for

"""

coleccion=[]
print("--------Muestro con un for-------------------")
for contador in range(0,120):
    coleccion.append(f"elemento: {contador}")
    print("Mostrando el "+coleccion[contador])


print("-----------Muestro con un while-------")

coleccion=[]
x=0
while x < 120:
    coleccion.append(f"elemento-{x}")
    print("Muestro el "+coleccion[x])
    x +=1

