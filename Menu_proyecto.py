from classes.connection import Connection
from classes.users import Usuario, Admin

modoin = int(input("1.Admin\n2.Usuario"))

contador = 0

intentos = 3

if modoin == 1:
    conexion = Connection()
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
    print("======================================")
    print("1) Consultar\n2) Modificar\n3) Eliminar\n4) Salir")
    print("======================================")
    print("======================================")
    opcion = int(input("Ingrese su Eleccion: "))
    
    if opcion == 1:#Consulta a la BDD
        
        print("======================================")
        print("Ud esta realizando una consulta")
        Usuario.leer_palabra()
        
        print("\nVolviendo al menu Principal...")
    
    elif opcion == 2:#Modifica la BDD
        
        print("======================================")
        print("Ud esta por modificar la Ley")
        Usuario.agregar_ley()
        
        print("======================================")
        print("\nVolviendo al menu Principal...")
        
        

    elif opcion == 3: #Elimina una entrada de la BDD
        
        print("======================================")
        print("Ud esta por eliminar una Ley")
        Usuario.borrar_ley()
        print(f'\nVolviendo al menu Principal...')
    
    elif opcion == 4: # Despedida del Programa
        
        print("======================================")
        print("Gracias Por usar el Consultor de Leyes\nHasta Luego!!!")
        break       
    else: #opcion invalida
        print("======================================")
        print("INGRESE UNA OPCION VALIDA\nOPCIONES DEL 1 AL 4!!!")        
        
if contador == 3:
    print("======================================")
    print("CUENTA BLOQUEADA")
    print("======================================")
    exit()

elif modoin == 2 :
    conexion = Connection()
    usuario = Usuario()
    print("======================================")
    print("BUSCADOR DE LEYES\nListado de opciones")
    print("======================================")

while True:
    print("======================================")
    print("1) Consultar\n2) Salir")
    print("======================================")
    print("======================================")
    opcion = int(input("Ingrese su Eleccion: "))
    
    if opcion == 1:#Consulta a la BDD
        
        print("======================================")
        print("Ud esta realizando una consulta")
        Usuario.leer_palabra()
        
        print("\nVolviendo al menu Principal...")
    
    
    elif opcion == 2: # Despedida del Programa
        
        print("======================================")
        print("Gracias Por usar el Consultor de Leyes\nHasta Luego!!!")
        break       
    else: #opcion invalida
        print("======================================")
        print("INGRESE UNA OPCION VALIDA\nOPCIONES 1 O 2!!!")