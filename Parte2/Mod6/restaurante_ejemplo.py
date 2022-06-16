import datetime as dt

class restaurante():
    def __init__(self, nombre, mesas, menu):
        self.name = nombre
        self.num_tables = mesas
        self.menu = menu

    def msg_bienvenida(self):
        ahora = dt.datetime.now()
        # print(dt.datetime.now().hour)
        if ahora.hour <= 12:
            print("Buenos días ", self.name)
        elif 12 < ahora.hour <= 18:
            print("Buenas tardes ", self.name)
        else:
            print("Buenas noches ", self.name)

    def msg_horario(self):
        print("El horario de atención en ",self.name," es de 11AM a 3 PM L- V ")


el_recuerdo = restaurante("Recuerdo", 5, ['arroz', 'papa', 'carne', 'vedura', 'jugo'])
print(el_recuerdo.menu)
print(el_recuerdo.name)
print(el_recuerdo.num_tables)

el_recuerdo.msg_bienvenida()
el_recuerdo.msg_horario()
