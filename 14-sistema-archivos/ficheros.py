from io import open
import pathlib
import shutil

#abrir archivo y si no esta creado lo crea.
archivo_lectura= open("fichero_texto.txt", "a+")

#escribir dentro
#archivo_lectura.write(" hoy es martes 19/02. texto metido desde python. hola todo bien")
#cerrar archivo
#archivo_lectura.close()

#abrir archivo con permiso r 
ruta= str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo_lectura= open(ruta,"r")

#leer archivo
#contenido= archivo_lectura.read()

#print(contenido)

#leer linea a linea y guardar en una lista

lista= archivo_lectura.readline()
archivo_lectura.close()
print(lista)
for frase in lista:
    print("-"+ frase.upper())


#copiar
ruta_original= str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva= str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
shutil.copyfile(ruta_original,ruta_nueva)

#mover shutil.move

#eliminar archivo. 
import os
ruta_nueva= str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
os.remove(ruta_nueva)

