listaNombres= []

nombre=""

while nombre != "s":

    nombre=input("Ingrese nombre a cargar y/o para salir S ")
    if nombre != "s":
        listaNombres.append(nombre)


    
print("-------Lista de Nombres cargados------")

numero= len(listaNombres)

for cont in range(0,numero):
    print("Nombre: ",listaNombres[cont])
print("-----------------------------------")
print("Total de nombres cargados: ",numero)
