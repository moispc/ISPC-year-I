# pylint: disable=consider-using-f-stringest
from mysql.connector import connect, Error

class Connection:
    """
    A class to represent a Connection.

    """
    def __init__(self, password) -> None:
        self.error = Error
        self.password = password
        self.host = 'localhost'
        self.port = 3306
        self.user = 'root'
    
    def connect(self):
        try:
            self.connection = connect(
            host = self.host,
            port = self.port,
            user = self.user,
            passwd = self.password,
            )
            self.cursor = self.connection.cursor()
            print("se realizó la conexión")
        except Error as err:
            print("Error de conexión: {0}".format(err))
  
    def close_connection(self):
        '''Method to close the connection'''
        if self.connection.is_connected():
            self.connection.close()
            print("Se cerró la conexión")

