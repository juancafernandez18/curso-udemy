# escribir un programa que nos de el cuadrado de los primeros 60 
# numeros naturales.


contador=0
numero=0
cuadrado=0

while (contador <=60):
    cuadrado=numero*numero
    print("El cuadrado del numero: ",str(numero),"es: ",str(cuadrado))
    numero+=1
    contador+=1