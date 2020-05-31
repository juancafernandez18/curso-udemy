lista=[2,34,56,67,76,7,789,8]
print("recorro la lista")

for nuemero in lista:
    print(nuemero)

print("lista original")
print(lista)

print("lista ordenada")
lista.sort()
print(lista)

print("longitud de la lista:",len(lista))


buscar=int(input("Ingrese un numero a buscar dentro de la lista"))

comprobar = isinstance(buscar,int)


elembuscado= buscar in lista

if (elembuscado is True):
    print("El elemento que ingreso si se encuentra en la lista")
else:
    print("Elemento no encontrado")