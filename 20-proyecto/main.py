"""
Proyecto python
Login: identificar al usuario + crear notas, borrar actualizar
Registro: Se creara un usuario en la bd
"""
from usuarios import acciones
print("""
Acciones Disponibles:
    -Registro
    -Login

""")
hazEl = acciones.Acciones() #creo el objeto hasEl que lo tengo en el paquete acciones
accion= input("Que desea hacer ?")

if accion == 'registro':
    hazEl.registro()

elif accion == "login":
    hazEl.login()
    

#cambio algo en el login, para tener en la rama login