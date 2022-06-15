"""
Observe que finalmente python puede dejar borrar la lista (privada)
Vamos a programar un método (show) que permitan acceder a la lista
sin generar error.
"""


class Pila:
    def __init__(self):
        self.__listaPila = []
        self.__var = 1

    def push(self, val):
        self.__listaPila.append(val)

    def pop(self):
        self.__listaPila.pop()

    def show(self):
        print(self.__listaPila)
        return len(self.__listaPila)

    def update_var(self, value):
        self.__var = value

    def show_var(self):
        print(self.__var)


objetoPila = Pila()
objetoPila.push(1)
objetoPila.push(2)
objetoPila.push(3)
print(objetoPila.show())
print("Longitud de la pila ", objetoPila.show())
objetoPila.pop()
print(objetoPila.show())
print("Longitud de la pila ", objetoPila.show())

# Igual puedo modificar la lista
objetoPila.__listaPila = [10, 20, 20, 40]
print("La lista modificada es: ", objetoPila.__listaPila)
objetoPila.show()


# Que pasa con una variable diferente a lista?
objetoPila.__var = 2
print("__var modificada fuera de la clase: ", objetoPila.__var)
objetoPila.show_var()
objetoPila.update_var(34)
objetoPila.show_var()

objetoPila.te = 20
print(objetoPila)
