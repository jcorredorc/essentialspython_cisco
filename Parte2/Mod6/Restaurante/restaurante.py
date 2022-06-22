import datetime as dt

class Restaurante():
    def __init__(self, nombre, tipo_cocina, mesas, menu):
        self.restaurant_name = nombre
        self.cuisine_type = tipo_cocina
        self.num_tables = mesas
        self.menu = menu

    def describe_restaurant(self):
        print("""

        --------------------------------------
        El restaurante %s
        ofrece cocina tipo %s
        --------------------------------------

        """ % (self.restaurant_name, self.cuisine_type))

    def open_restaurant(self):
        print("El restaurante", self.restaurant_name, "esta abierto")

    def msg_bienvenida(self):
        ahora = dt.datetime.now()
        # print(dt.datetime.now().hour)
        if ahora.hour <= 12:
            print("Buenos días ", self.restaurant_name)
        elif 12 < ahora.hour <= 18:
            print("Buenas tardes ", self.restaurant_name)
        else:
            print("Buenas noches ", self.restaurant_name)

    def msg_horario(self):
        print("El horario de atención en ",
              self.restaurant_name, " es de 11AM a 3 PM L- V ")

    def order(self, user, order_id):
        """Revisar si es un usuario válido"""
        # print(type(user))
        try:
            print(user.first_name)
        except:
            print("no pude acceder")


if __name__ == '__main__':
    print()
    print(path)

    el_recuerdo = Restaurante("Recuerdo",
                              "vegetariana",
                              5,
                              ['arroz', 'papa', 'carne', 'vedura', 'jugo'])

    resta1 = Restaurante("El buen gusto",
                         "tipica colombiana",
                         34,
                         ['plato1', 'plato2', 'plato3', 'plato4', 'plato5'])
    rest2 = Restaurante("El paraiso",
                        "italiana",
                        56,
                        ['rissoto', 'pomodoro', 'pasta', 'pizza', 'lasagna'])
    print(el_recuerdo.menu)
    print(el_recuerdo.restaurant_name)
    print(el_recuerdo.num_tables)

    el_recuerdo.msg_bienvenida()
    el_recuerdo.msg_horario()
    el_recuerdo.describe_restaurant()
    el_recuerdo.open_restaurant()
