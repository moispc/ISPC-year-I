# pylint: disable=consider-using-f-string

from mysql.connector import connect, Error


class Connection:
    """
    A class to represent a Connection.

    """
    def __init__(self, password) -> None:
        try:
            self.connect = connect(
            host='localhost',
            port=3306,
            user='root',
            passwd=password,
            )
            self.cursor = self.connect.cursor()
            print("se realizó la conexión")

        except Error as ex:
            print("Error de conexión: {0}".format(ex))


    def create_database(self):
        if self.connect.is_connected():
            try:
                """ MySQL Workbench Forward Engineering """
                self.cursor.execute("SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;")
                self.cursor.execute("SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;")
                self.cursor.execute("SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';")
                """ Schema lawdb2 """
                self.cursor.execute("CREATE SCHEMA IF NOT EXISTS `lawdb2` DEFAULT CHARACTER SET utf8")
                self.cursor.execute("USE `lawdb2`")
                """ Table lawdb.jurisdiccion """
                self.cursor.execute("CREATE TABLE IF NOT EXISTS lawdb2.Jurisdiccion (`idJurisdiccion` INT NOT NULL AUTO_INCREMENT,  `Jurisdiccion` VARCHAR(100) NOT NULL,  `Organo Legislativo` VARCHAR(100) NOT NULL,  PRIMARY KEY (`idJurisdiccion`),  UNIQUE INDEX `Organo Legislativo_UNIQUE` (`Organo Legislativo` ASC) VISIBLE) ENGINE = InnoDB")
                """ Table lawdb.Ley """  
                self.cursor.execute("CREATE TABLE IF NOT EXISTS lawdb2.Ley (`Nro. Registro` INT NOT NULL AUTO_INCREMENT, `Tipo de normativa` VARCHAR(45) NOT NULL, `Nro. Normativa` INT NOT NULL, `Fecha` DATE NOT NULL, `Descripción` VARCHAR(400) NOT NULL, `Categoria` VARCHAR(45) NOT NULL, `Jurisdiccion_idJurisdiccion` INT NOT NULL, PRIMARY KEY (`Nro. Registro`, `Jurisdiccion_idJurisdiccion`), INDEX `fk_Ley_Jurisdiccion1_idx` (`Jurisdiccion_idJurisdiccion` ASC) VISIBLE, CONSTRAINT `fk_Ley_Jurisdiccion1` FOREIGN KEY (`Jurisdiccion_idJurisdiccion`) REFERENCES `lawdb2`.`Jurisdiccion` (`idJurisdiccion`) ON DELETE NO ACTION ON UPDATE NO ACTION) ENGINE = InnoDB")
                """ Table lawdb.Palabras """
                self.cursor.execute("CREATE TABLE IF NOT EXISTS lawdb2.Palabras (`idPalabras` INT NOT NULL AUTO_INCREMENT, `Palabras clave` VARCHAR(100) NULL, PRIMARY KEY (`idPalabras`), UNIQUE INDEX `Palabras clave_UNIQUE` (`Palabras clave` ASC) VISIBLE) ENGINE = InnoDB")
                """ Table lawdb.Palabras_Ley """
                self.cursor.execute("CREATE TABLE IF NOT EXISTS lawdb2.Palabras_Ley ( `Palabras_idPalabras` INT NOT NULL AUTO_INCREMENT, `Ley_Nro. Registro` INT NOT NULL, PRIMARY KEY (`Palabras_idPalabras`, `Ley_Nro. Registro`), INDEX `fk_Palabras_has_Ley_Ley1_idx` (`Ley_Nro. Registro` ASC) VISIBLE, INDEX `fk_Palabras_has_Ley_Palabras_idx` (`Palabras_idPalabras` ASC) VISIBLE, CONSTRAINT `fk_Palabras_has_Ley_Palabras` FOREIGN KEY (`Palabras_idPalabras`) REFERENCES `lawdb2`.`Palabras` (`idPalabras`) ON DELETE NO ACTION ON UPDATE NO ACTION, CONSTRAINT `fk_Palabras_has_Ley_Ley1` FOREIGN KEY (`Ley_Nro. Registro`) REFERENCES `lawdb2`.`Ley` (`Nro. Registro`) ON DELETE NO ACTION ON UPDATE NO ACTION) ENGINE = InnoDB")
                self.cursor.execute("SET SQL_MODE=@OLD_SQL_MODE;")
                self.cursor.execute("SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;")
                self.cursor.execute("SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;")
            except Error as err:
                print("Error de conexión: {0}".format(err))
            print("está conectado")
        

  

    def close_connection(self):
        '''Method to close the connection'''
        if self.connect.is_connected():
            self.connect.close()
            print("Se cerró la conexión")

         
""" getpass("Enter password: ") """
c = Connection(input("Ingrese su contraseña: "))
""" c.read_laws()

c.create_law()
 """


c.create_database()

c.close_connection()

