#sacar un cierto porcentaje de un numero ingresado por el usuario

numero=int(input("Ingrese el numero a calcular porcentaje "))
porcentaje=int(input("Ingrese que porcentaje quiere saber del numero ingresado"))

total= (porcentaje*numero)/100

print("El ",porcentaje," porciento del numero, ",numero,"es: ",total)


