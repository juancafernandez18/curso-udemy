import mysql.connector
def conectar():
    database= mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="proyecto_python",
        port=3308
    )
    cursor= database.cursor(buffered=True)

    return[database,cursor]