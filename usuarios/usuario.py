
#Invocaciones
import hashlib
import mysql.connector
import datetime
import usuarios.conexiones as conexion

connect = conexion.conectar()
database = connect[0]
cursor= connect[1]


class Usuario:

    def __init__(self, nombre, apellido, email, password): 
        self.nombre = nombre
        self.apellidos = apellido
        self.email = email
        self.password = password

    def registrar(self):
        fecha = datetime.datetime.now()

        #Cifrar Contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))



        sql ="INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)
        
        try:
            cursor.execute(sql, usuario)
            database.commit()
            return [cursor.rowcount, self]
        except:
            result = [0, self]
        

    
    def identificar(self):
        #Consulta para comprobar si existe el usuario
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"


        #Cifrado de Contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        #Datos para la Consulta
        usuario = (self.email, cifrado.hexdigest())

        cursor.execute(sql, usuario)
        result= cursor.fetchone()

        return result
        


