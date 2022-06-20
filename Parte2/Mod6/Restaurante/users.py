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


if __name__ == '__main__':
    cliente1 = Users("pedro", "matias", 2345)
    cliente1.describe_user()
