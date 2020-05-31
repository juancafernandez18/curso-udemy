#mostrar todos los numers que esten entre dos numeros que diga el usuario

numero1=int(input("Ingrese el primer numero"))
numero2=int(input("Ingrese el segundo numero"))
cont=numero1
if numero1 < numero2:

    print("los numeros entre ",numero1,"y ",numero2,"son:")
    for cont in range(numero1,numero2):
        print(cont)
else:
    print("el numer1 debe ser menor al numero 2")