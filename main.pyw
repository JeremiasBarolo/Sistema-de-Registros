#Programa de Registros y Login Creado Por Jeremias Barolo.

#Invocaciones
from usuarios import acciones


print("""
Acciones disponibles:
                -Login
                -Registrarse

""")

hazEl = acciones.Acciones()
accion = input("Que quieres hacer?: ")

try:
    if accion == 'registrarse':
        hazEl.registro()


    elif accion == "login":
        hazEl.login()


except:
    print("Error, reinicie el sistema")
