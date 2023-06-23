class Usuario:
    def __init__(self):
        pass
    
    # C - CREATE
    def create_database(self, connection):
        # Creación de la base de datos
        cursor = connection.cursor


        cursor.execute('show databases')
        mysqldbs = connection.cursor.fetchall()

        if ('ispc_lawdb',) in mysqldbs:
            cursor.execute('USE ispc_lawdb')
        else:
            fd = open('bbdd/moispc.sql', 'r')
            sqlFile = fd.read()
            fd.close()

            # Separamos todos los comandos de sql
            sqlCommands = sqlFile.split(';')

            # Execute every command from the input file
            for command in sqlCommands:
            # This will skip and report errors
            # For example, if the tables do not yet exist, this will skip over
            # the DROP TABLE commands
                try:
                    cursor.execute(command)
                except connection.Error as err:
                    print("Error de conexión: {0}".format(err))
    
    # R - READ

    def leer_ley(self, connection):
        """ muestra la ley dependiendo del numero de ley introducido """
        ley = int(input("Introducir el número de ley: "))
        cursor = connection.cursor
        cursor.execute(f'SELECT `Tipo de normativa`, `Nro. Normativa`, Fecha, Descripción, `Organo Legislativo`, Jurisdiccion FROM ley\
                        JOIN jurisdiccion\
                        ON ley.Jurisdiccion_idJurisdiccion=jurisdiccion.idJurisdiccion\
                        WHERE `Nro. Normativa`={ley};')
        rows = cursor.fetchall()

        for row in rows:
            print(row)
            print("")
        


    def leer_palabra(self, connection):
        """ muestra la ley dependiendo del numero de ley introducido """
        palabra = input("Introduzca la palabra clave: ")
        cursor = connection.cursor
        cursor.execute(f'SELECT `Tipo de normativa`, `Nro. Normativa`, Fecha, Descripción, `Organo Legislativo`, Jurisdiccion FROM palabras\
                        JOIN palabras_ley\
                        ON palabras.idPalabras = palabras_ley.Palabras_idPalabras\
                        JOIN ley\
                        ON ley.`Nro. Registro` = palabras_ley.`Ley_Nro. Registro`\
                        JOIN jurisdiccion\
                        ON ley.Jurisdiccion_idJurisdiccion=jurisdiccion.idJurisdiccion\
                        WHERE `Palabras clave` = "{palabra}"')
        rows = cursor.fetchall()

        for row in rows:
            print(row)
            print("")

    

    def ingresar(self):
        print("======================================")
        print("Ingreso Existoso como usuario")
        print("======================================")

###############################################################################
class Admin(Usuario):
    def ingresar(self):
        print("======================================")
        print("Ingreso Existoso como administrador")
        print("======================================")
    
    
    # D - DELETE
    def borrar_ley(self, connection):
        """ muestra la ley dependiendo del numero de ley introducido """
        cursor = connection.cursor
        cursor.execute('SELECT `Nro. Registro`, `Nro. Normativa`, `Organo Legislativo` FROM ley\
                        JOIN jurisdiccion\
                        ON ley.Jurisdiccion_idJurisdiccion=jurisdiccion.idJurisdiccion;')
        rows = cursor.fetchall()

        for row in rows:
            print(row)
        
        id_ley = int(input("Por favor ingrese el id de la ley que desea borrar: "))

        cursor.execute(f"DELETE FROM ley WHERE `Nro. Registro` = {id_ley};")
        connection.connection.commit()
        
       
        
    # C - CREATE   
    def agregar_ley(self, connection):
        cursor = connection.cursor
        sql_ley = "INSERT INTO ley(`Tipo de normativa`, `Nro. Normativa`, Fecha, Descripción, Categoria, Jurisdiccion_idJurisdiccion) VALUES (%s, %s, %s, %s, %s, %s)"
        sql_palabra = "INSERT INTO palabras (`Palabras clave`) VALUES (%s)"
        sql_ley_palabra = "INSERT INTO palabras_ley (`Ley_Nro. Registro`,Palabras_idPalabras) VALUES (%s, %s)"

        tipo_normativa = input("Ingrese el tipo de normativa: ")
        numero_normativa = int(input("Ingrese el numero de la normativa: "))
        fecha_normativa = input("Ingrese la fecha de la normativa con el formato YYYY-MM-DD: ")
        descripcion_normativa = input("Ingrese la descripción de la normativa: ")
        categoria_normativa = input ("Ingrese la categoría de la normativa: ")
        jurisdiccion_normativa = int(input("Ingrese 1 si la normativa es nacional o 2 si es provincial: "))
        palabra_clave = input("Ingrese una palabra clave para esta normativa: ")

        val_ley = (tipo_normativa, numero_normativa, fecha_normativa, descripcion_normativa, categoria_normativa, jurisdiccion_normativa)
        cursor.execute(sql_ley, val_ley)

        ley_id= cursor.lastrowid

        val_palabra = (palabra_clave,)
        cursor.execute(sql_palabra, val_palabra)

        palabra_id= cursor.lastrowid
        
        val_ley_palabra = (ley_id, palabra_id)
        cursor.execute(sql_ley_palabra, val_ley_palabra)

        connection.connection.commit()
        
    
        
    # U - UPDATE
    def modificar_ley(self):
        cursor = connection.cursor
        cursor.execute('SELECT `Nro. Registro`, `Nro. Normativa`, `Organo Legislativo` FROM ley\
                        JOIN jurisdiccion\
                        ON ley.Jurisdiccion_idJurisdiccion=jurisdiccion.idJurisdiccion;')
        rows = cursor.fetchall()

        for row in rows:
            print(row)

        id_ley = int(input("Por favor ingrese el id de la ley que desea modificar: "))
        
        tipo_normativa = input("Ingrese el tipo de normativa: ")
        numero_normativa = int(input("Ingrese el numero de la normativa: "))
        fecha_normativa = input("Ingrese la fecha de la normativa con el formato YYYY-MM-DD: ")
        descripcion_normativa = input("Ingrese la descripción de la normativa: ")
        categoria_normativa = input ("Ingrese la categoría de la normativa: ")
        jurisdiccion_normativa = int(input("Ingrese 1 si la normativa es nacional o 2 si es provincial: "))

        cursor.execute(f"UPDATE ley SET `Tipo de normativa`= '{tipo_normativa}' WHERE `Nro. Registro`={id_ley};")
        cursor.execute(f"UPDATE ley SET `Nro. Normativa`= '{numero_normativa}' WHERE `Nro. Registro`={id_ley};")
        cursor.execute(f"UPDATE ley SET Fecha= '{fecha_normativa}' WHERE `Nro. Registro`={id_ley};")
        cursor.execute(f"UPDATE ley SET Descripción= '{descripcion_normativa}' WHERE `Nro. Registro`={id_ley};")
        cursor.execute(f"UPDATE ley SET Categoria= '{categoria_normativa}' WHERE `Nro. Registro`={id_ley};")
        cursor.execute(f"UPDATE ley SET Jurisdiccion_idJurisdiccion= '{jurisdiccion_normativa}' WHERE `Nro. Registro`={id_ley};")
        connection.connection.commit()

        
        
        

###############################################################################
