#variable local y global

frase= "hola como estas"

print(frase)


def saludo():
    frase="hola mundo"
    print(frase)
    global correo
    correo="juanca.fernandez18"

saludo()

print(correo) #imprime la variable global definida en la funcion.