#importar el modulo

import sqlite3

#conexion

conexion = sqlite3.connect('pruebas.db')

#crear cursor
cursor= conexion.cursor()

#crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id INTEGER PRIMARY KEY AUTOINCREMENT, "+
"nombre_producto varchar(20), "+
"descripcion text, "+
"precio int(222)"+

")")

#insertar datos
cursor.execute("INSERT INTO productos VALUES(null,'yerba','taragui','55')")


#listar datos
cursor.execute("SELECT * FROM productos    ")
productos= cursor.fetchall()
#INSERTAR MUCHOS DATOS DE GOLPE
produs =[
    ("harina","tipo 4 cero",74),
    ("aceite","girasol",53),
    ("aceite","mezcla",12),

]
cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)",produs)

conexion.commit()


#borrar registros
cursor.execute("DELETE FROM productos WHERE descripcion = 'mezcla'")
#GUARDAR CAMBIOS
conexion.commit()

for prod in productos:
    print("Producto: ",prod)

#cerrar conexion
conexion.close()