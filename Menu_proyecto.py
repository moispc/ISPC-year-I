print("======================================")
print("BUSCADOR DE LEYES\nListado de opciones")
print("======================================")

while True:
    print("======================================")
    print("1) Consultar\n2) Modificar\n3) Eliminar\n4) Salir")
    print("======================================")
    print("======================================")
    opcion = int(input("Ingrese su Eleccion: "))
    
    if opcion == 1:#Consulta a la BDD
        
        print("======================================")
        print("Ud esta realizando una consulta")
        
        
        print("\nVolviendo al menu Principal...")
    
    if opcion == 2:#Modifica la BDD
        
        print("======================================")
        print("Ud esta por modificar la Ley")
        
        
        print("======================================")
        print("\nVolviendo al menu Principal...")
        
        

    elif opcion == 3: #Elimina una entrada de la BDD
        
        print("======================================")
        print("Ud esta por eliminar una Ley")
        print(f'\nVolviendo al menu Principal...')
    
    elif opcion == 4: # Despedida del Programa
        
        print("======================================")
        print("Gracias Por usar el Consultor de Leyes\nHasta Luego!!!")
        break       
    else: #opcion invalida
        print("======================================")
        print("INGRESE UNA OPCION VALIDA\nOPCIONES DEL 1 AL 4!!!")