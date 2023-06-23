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
        
        print("llamar a una funcion para leer la ley")


    def leer_palabra(self, connection):
        """ muestra la ley dependiendo del numero de ley introducido """
        

    

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
        
        print("llamar a una funcion para borrar una ley")
        
    # C - CREATE   
    def agregar_ley(self, connection):
        
        print("llamar a una funcion para agregar una ley")
        
    # U - UPDATE
    def modificar_ley(self):
        
        print("llamar a una funcion para modificar una ley")
        

###############################################################################
