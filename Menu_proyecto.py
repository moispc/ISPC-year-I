from classes.connection import Connection
from classes.users import Usuario, Admin

while True:

    try:
        modoin = int(input("1.Admin\n2.Usuario\nSu eleccion: "))
    except Exception as e:
        print(e)
        modoin = "invalido"
    
    contador = 0
    
    intentos = 3
    
    if modoin == 1:
        contrasena = input("Ingrese la contraseña del servidor de MySQL: ")
        conexion = Connection(contrasena)
        administrador = Admin()
        
        # Datos del Admin
        user_ok = {"admin" : "admin"
                }
        
        #Autentificacion
        while contador < 3:
            print("======================================")
            user = input("Ingrese su Usuario: \n")
            password = input("Ingrese su Contraseña: \n")
            print("======================================")
    
    
            if user in user_ok and password == user_ok[user]:
                print("======================================")
                print("Ingreso Existoso")
                print("======================================")
                break
            
            else:
                contador += 1
                print("======================================")
                print("Datos Incorrectos.. Intente nuevamente")
                print("======================================")
                print(f'Le quedan {intentos-contador} Intentos')
                print("======================================")
    
        if contador == 3:
            print("======================================")
            print("CUENTA BLOQUEADA")
            print("======================================")
            exit()
            
        print("======================================")
        print("BUSCADOR DE LEYES\nListado de opciones")
        print("======================================")
        #Menu admin
        while True:
            conexion.connect()
            administrador.create_database(conexion)
            print("======================================")
            print("1) Agregar nueva normativa\n2) Consultar por palabra clave\n3) Consultar por numero de ley\n4) Modificar\n5) Eliminar\n6) Salir")
            print("======================================")
            print("======================================")
            try:
                opcion = int(input("Ingrese su Eleccion: "))
            except Exception as e:
                print(e)
                opcion = "invalid"

            if opcion == 1:#Consulta a la BDD por palabra clave
                
                print("======================================")
                print("Ud esta realizando agregando una nueva normativa")
                administrador.agregar_ley(conexion)
                
                print("\nVolviendo al menu Principal...")
            
            if opcion == 2:#Consulta a la BDD por palabra clave
                
                print("======================================")
                print("Ud esta realizando una consulta")
                administrador.leer_palabra(conexion)
                
                print("\nVolviendo al menu Principal...")
    
            if opcion ==3:#Consulta a la BDD por numero de ley
                
                print("======================================")
                print("Ud esta realizando una consulta")
                administrador.leer_ley(conexion)
                
                print("\nVolviendo al menu Principal...")
            
            elif opcion == 4:#Modifica la BDD
                
                print("======================================")
                print("Ud esta por modificar la Ley")
                administrador.modificar_ley(conexion)
                
                print("======================================")
                print("\nVolviendo al menu Principal...")
                
                
        
            elif opcion == 5: #Elimina una entrada de la BDD
                
                print("======================================")
                print("Ud esta por eliminar una Ley")
                administrador.borrar_ley(conexion)
                print('\nVolviendo al menu Principal...')
            
            elif opcion == 6: # Despedida del Programa
                
                print("======================================")
                print("Gracias Por usar el Consultor de Leyes\nHasta Luego!!!")
                exit()
            else: #opcion invalida
                print("======================================")
                print("INGRESE UNA OPCION VALIDA\nOPCIONES DEL 1 AL 5!!!")        
                
        
        
    elif modoin == 2:
        contrasena = input("Ingrese la contraseña del servidor de MySQL: ")
        conexion = Connection(contrasena)
        usuario = Usuario()
        conexion.connect()
        usuario.create_database(conexion)
        print("======================================")
        print("BUSCADOR DE LEYES\nListado de opciones")
        print("======================================")
    
        while True:
            print("======================================")
            print("1) Consultar por palabra clave\n2) Consultar por numero de ley\n3) Salir")
            print("======================================")
            print("======================================")
            try:
                opcion = int(input("Ingrese su Eleccion: "))
            except Exception as e:
                print(e)
                opcion = "invalida"

            if opcion == 1:#Consulta a la BDD por palabra clave

                print("======================================")
                print("Ud esta realizando una consulta por palabra clave")
                usuario.leer_palabra(conexion)

                print("\nVolviendo al menu Principal...")


            if opcion == 2:#Consulta a la BDD por numero de ley

                print("======================================")
                print("Ud esta realizando una consulta por numero de ley")
                usuario.leer_ley(conexion)

                print("\nVolviendo al menu Principal...")


            elif opcion == 3: # Despedida del Programa

                print("======================================")
                print("Gracias Por usar el Consultor de Leyes\nHasta Luego!!!")
                break       
            else: #opcion invalida
                print("======================================")
                print("INGRESE UNA OPCION VALIDA\nOPCIONES 1, 2 o 3!!!")
        break
    else: #opcion invalida
                print("======================================")
                print("INGRESE UNA OPCION VALIDA\nOPCIONES 1 O 2!!!")


