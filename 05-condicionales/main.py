#condicionales

edad=int(input("ingresa tu edad"))

if (edad >= 18) :
    print("eres mayor de edad !!")
else:
    print("eres menor de edad")

print("--------------------ejemplo 2 ---------------")
entrada=input("para ingresar al juego ingrese s ")
while entrada== "s": 
    numero=int(input("Intenta adivinar mi numero favorito "))

    if (numero == 18):
        print("Has acertado al numero !!")
    elif (numero >= 15)and (numero <=25):
        print("estas cerca del numero")
    else:
        print("estas muy lejos, intentalo de nuevo")
    entrada=input("para volver al juego ingrese S, para salir X")


#---------------------ejemplo bucles

contador= 0
resultado= 10
for contador in range(0,10):
    print("Voy en la vuelta, ",str(contador))
    print("voy sumando de 10 en 10, resultado: ",str(resultado))
    resultado +=10
