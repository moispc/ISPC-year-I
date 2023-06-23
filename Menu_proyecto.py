from classes.connection import Connection
from classes.users import Usuario, Admin

modoin = int(input("1.Admin\n2.Usuario"))

contador = 0

intentos = 3

if modoin == 1:
    contraseña = input("ingrese la contraseña de sql: ")
    conexion = Connection(contraseña)
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


        if user in user_ok and password in user_ok[user]:
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


    print("======================================")
    print("BUSCADOR DE LEYES\nListado de opciones")
    print("======================================")
    #Menu admin
    while True:
        conexion.connect()
        administrador.create_database(conexion)
        print("======================================")
        print("1) Consultar por palabra clave\n2) Consultar por numero de ley\n3) Modificar\n4) Eliminar\n5) Salir")
        print("======================================")
        print("======================================")
        opcion = int(input("Ingrese su Eleccion: "))
        
        if opcion == 1:#Consulta a la BDD por palabra clave
            
            print("======================================")
            print("Ud esta realizando una consulta")
            administrador.leer_palabra(conexion)
            
            print("\nVolviendo al menu Principal...")

        if opcion ==2:#Consulta a la BDD por numero de ley
            
            print("======================================")
            print("Ud esta realizando una consulta")
            administrador.leer_ley(conexion)
            
            print("\nVolviendo al menu Principal...")
        
        elif opcion == 3:#Modifica la BDD
            
            print("======================================")
            print("Ud esta por modificar la Ley")
            administrador.modificar_ley(conexion)
            
            print("======================================")
            print("\nVolviendo al menu Principal...")
            
            
    
        elif opcion == 4: #Elimina una entrada de la BDD
            
            print("======================================")
            print("Ud esta por eliminar una Ley")
            administrador.borrar_ley(conexion)
            print(f'\nVolviendo al menu Principal...')
        
        elif opcion == 5: # Despedida del Programa
            
            print("======================================")
            print("Gracias Por usar el Consultor de Leyes\nHasta Luego!!!")
            exit()
        else: #opcion invalida
            print("======================================")
            print("INGRESE UNA OPCION VALIDA\nOPCIONES DEL 1 AL 4!!!")        
            
    if contador == 3:
        print("======================================")
        print("CUENTA BLOQUEADA")
        print("======================================")
        exit()
    
elif modoin == 2:
    contraseña = input("ingrese la contraseña de sql: ")
    conexion = Connection(contraseña)
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
    opcion = int(input("Ingrese su Eleccion: "))
    
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
        print("INGRESE UNA OPCION VALIDA\nOPCIONES 1 O 2!!!")



