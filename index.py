""" Importamos cla clase connection para poder conectarnos a la base de datos Mysql """
from classes.connection import Connection
from classes.users import Usuario, Admin


contraseña = input("ingrese la contraseña de sql: ")
c = Connection(contraseña)

usuario = Admin()

c.connect()

""" usuario.create_database(c) """

usuario.create_database(c)

# usuario.leer_palabra(c)

#usuario.leer_palabra(c)

#    usuario.agregar_ley(c)

usuario.borrar_ley(c)

# usuario.modificar_ley(c)

# usuario.agregar_ley(c)




c.close_connection()

