#Invocaciones
import usuarios.usuario as modelo


class Acciones:

    def registro(self):  
        print("\nExcelente. Vamos a registrarte...")
        print("Recuerde que las Opciones marcadas con * son OBLIGATORIAS.\n")
        nombre = input("¿Cual es tu nombre?: ")
        apellido = input("¿Cual es tu apellido?: ")
        email = input("¿Cual es tu Email?*: ")
        password = input("Introduzca una contraseña*: ")

        usuario = modelo.Usuario(nombre, apellido, email,password)
        registro = usuario.registrar()

        if registro [0] >= 1:
            print(f"Perfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("No te has registrado correctamente.")


    def login(self):
        
        print("\n Excelente. Introduzca sus datos por favor...\n ")
        email = input("¿Cual es tu Email?: ")
        password = input("Introduzca una contraseña: ") 

        usuario= modelo.Usuario("", "", email, password)
        login = usuario.identificar()

        if email == login[3]:
            print(f"Bienvenido {login[1]}, te has registrado el {login[5]} ")
            
