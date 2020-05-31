#listas


peliculas=["batman","spider man","otras","2012","breaking"]

print(peliculas)
print("saco del 0 al 3")
print(peliculas[0:3])
print("saco a partir del 3")
print(peliculas[3:])
cantantes=list(("2pac","drake","damas gratis"))

print(cantantes)
print(cantantes[1])

print(peliculas[2])

listavariada=["zipora",10,True]

print(listavariada)
print("agrego un elemento")
listavariada.append("nuevo eleemento")

print(listavariada)

#recorrer lista

print("---------listado peliculas----------------")


"""
nuevapeli=""
while nuevapeli != "parar":
    nuevapeli=input("Ingrese la nueva pelicula o parar para salir")
    if nuevapeli!="parar":

        peliculas.append(nuevapeli)

for pelicula in peliculas:
    print(peliculas.index(pelicula)+1,pelicula)
"""
print("ejemplo---------------LISTADO DE CONTACTOS----------------------------")

contactos=[
    [
        'Antonio',
        'antonio.gmail.com'
    ],
    [
        'juan',
        'gmail.com'
    ]




]
print(contactos)