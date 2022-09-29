import mysql.connector
def conectar():
    database= mysql.connector.connect(
        host= "localhost",
        user= "root",
        passwd= "j44.158.467",
        database= "Proyecto_Python",
        port= 3306,
    )

    cursor = database.cursor(buffered=True)

    return [database, cursor]