#funciones


def muestraNombre():

    print("NOMBRE: JUANCA")
    print("APELLIDO: FERNANDEZ")



muestraNombre()                 #invoco a la funcion
print("-------------------------------")
def mostarTunombre(nombre):
    print("Tu nombre es: ",nombre)



nombre=input("Ingresa tu nombre")

mostarTunombre(nombre)

print("----------ejemplo 3---------------------")
"""
def tabla(numero):
    print("Esta es la tabla del numero: ",numero)
    print("")
    for cont in range (1,11):
        operacion = (numero * cont)
        print(numero," x ",cont," = ",operacion)
        
"""

#numero=int(input("Ingresa el numero que quieres saber la tabla del 1 al 10 "))

#tabla(numero)

 #parametros opcionales

def getEmpleado(nombre,dni= False): #con el igual de digo que es NO OBLIGATORIO
    print("Empleado")
    print("Nombre: ",nombre)
    print("Dni:",dni) 

getEmpleado("Juanca")


def saludo(nombre):
    salud=("Hola como estas",nombre)
    return(salud)

print(saludo("la zipora"))