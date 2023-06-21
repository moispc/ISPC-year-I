class Usuario:
    def __init__(self, nombre, contraseña):
        self.nombre = nombre
        self.contraseña = contraseña
        
    def leer_ley(self):
        
        print("llamar a una funcion para leer la ley")
        

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
    
    
    def borrar_ley(self):
        
        print("llamar a una funcion para borrar una ley")
        
       
    def agregar_ley(self):
        
        print("llamar a una funcion para agregar una ley")
        
        
    def modificar_ley(self):
        
        print("llamar a una funcion para modificar una ley")
        

###############################################################################
