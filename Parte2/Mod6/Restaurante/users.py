class Users:
    """ Modelan los usuarios"""

    def __init__(self, first_name, last_name, id):
        self.first_name = first_name
        self.last_name = last_name
        self.id = int(id)

    def describe_user(self):
        print("""
        Nombres: %s
        Apellidos: %s
        ID: %i 
        """ % (self.first_name, self.last_name, self.id))

    def greet_user(self):
        print("""


        %s %s 

        Bienvenido 

        ID: %i

        """)

class admin(Users):
    def __init__(self, first_name, last_name, id):
        super().__init__(first_name, last_name, id)
        self.privilegios = ["crear usuarios","ver cuentas","modificar menu"]

    def show_privilegios(self):
        print(self.privilegios)

class empleados(Users):
    def __init__(self, first_name, last_name, id, privilegios,cargo="empleado"):
        super().__init__(first_name, last_name, id)
        self.cargo = cargo
        self.privilegios = privilegios
    
    def show_privilegios(self):
        print(self.privilegos)
    
    def describe_user(self):
        print("""
        Nombres: %s
        Apellidos: %s
        ID: %i 
        Cargo: %s
        """ % (self.first_name, self.last_name, self.id, self.cargo))


if __name__ == '__main__':
    cliente1 = Users("pedro", "matias", 2345)
    cliente1.describe_user()

    admin= admin("Pablo","Ramirez",123456)
    admin.show_privilegios()

    cajero1 = empleados("Robin","Perez",12321,["tomar orden","crear cliente"],"cajero")
    cajero1.describe_user()