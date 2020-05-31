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
hazEl = acciones.Acciones()
accion= input("Que desea hacer ?")

if accion == 'registro':
    hazEl.registro()

elif accion == "login":
    hazEl.login()
    