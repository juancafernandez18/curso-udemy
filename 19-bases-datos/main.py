import mysql.connector

#conexion

database= mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="mpython"


)

#conexion correcta ?
#print(database)
#cursor
cursor = database.cursor(buffered=True)

"""cursor.execute("CREATE DATABASE IF NOT EXISTS  mpython")

cursor.execute("SHOW DATABASES")

for db in cursor:
    print(db)"""

#crear tablas

cursor.execute("""
CREATE TABLE IF NOT EXISTS autos(
id int(10) auto_increment not null,
patente varchar(10) not null,
marca varchar(10),
modelo varchar(15),
color varchar(10),
CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")

#insertar datos

cursor.execute("INSERT INTO autos VALUES(null,'nes822','vw','gol','negro')")
database.commit()
#cargo varios registros
coches=[
    ('aa22','ranault','clio','blanco'),
    ('zmc24','ford','mondeo','negro mate'),
    ('22aaa','camaro','rs','azul')


]
cursor.executemany("INSERT INTO autos VALUES(null,%s,%s,%s,%s)",coches)
database.commit()

#consultar datos
"""cursor.execute("SELECT * FROM autos WHERE marca='ford'")
result = cursor.fetchall()
print("-----TODOS LOS AUTOS FORD-----")
print("ID PATENTE MARCA MODELO COLOR")
for auto in result:
    print(auto)"""


#BORAR REGISTROS
cursor.execute("DELETE FROM autos WHERE marca='ford'")
database.commit()

print(cursor.rowcount,"borrados!!")

#Actualizar
cursor.execute("UPDATE autos SET modelo='gol trend' WHERE marca='vw'")
database.commit()
print(cursor.rowcount,"Actualizados!")