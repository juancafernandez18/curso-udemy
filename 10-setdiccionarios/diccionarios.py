"""
un diccionario es un tipo de dato que almacena un conjunto de datos
en formato clave > valor
parecido a un array asociativo
"""

persona = {
    "nombre":"victor",
    "apellido": "robles",


}

print(persona)

contactos = [
    {
        'nombre': 'juan',
        'apellido': 'fernandez',
        'numero': '3794744867'
    },
    {
        'nombre': 'zipora',
        'apellido': 'fernandez',
        'numero': '374654'
    }

]
print(contactos)

print("LISTADO DE CONTACTOS")
print("---------------------")
for contacto in contactos:
    print("Nombre del contacto",contacto['nombre'])
    print("Apellido:",contacto['apellido'])
    print("Celular:",contacto['numero'])
    print("---------------------------------------")

