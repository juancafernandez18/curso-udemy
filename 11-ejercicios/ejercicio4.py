variable= None

print("----------------------------")
if variable is None:
    print("variable vacia")
else:
    print("la variable tiene algo")


print("----------------------------")

variable=input("ingrese algun valor")

if len(variable.strip()) == 0:             #con strip saco los espacios
    variable="la relleno con algo"
    print(variable.upper())
    
else:
    print("la variable tiene contenido")