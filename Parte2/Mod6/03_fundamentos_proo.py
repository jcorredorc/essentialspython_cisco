"""
Vamos a programar dos métodos (show_var y update_var)) que permitan acceder a la 
lista sin generar error.
"""

class Pila:
    def __init__(self):
        self.__listaPila = []
        self.__var = 1

    def push(self, val):
        self.__listaPila.append(val)

    def pop(self):
        self.__listaPila.pop()

    def show_pila(self):
        print(self.__listaPila)

    def update_var(self, value):
        self.__var = value

    def show_var(self):
        print(self.__var)


objetoPila = Pila()
objetoPila.push(1)
objetoPila.push(2)
objetoPila.push(3)
objetoPila.show_pila()
objetoPila.pop()
objetoPila.show_pila()

# Igual puedo modificar la lista
objetoPila.__listaPila = [10, 20, 20, 40]
print("La lista modificada es: ", objetoPila.__listaPila)
objetoPila.show_pila()


# Que pasa con una variable diferente a lista?
objetoPila.__var = 2
print("__var modificada fuera de la clase: ", objetoPila.__var)
objetoPila.show_var()
objetoPila.update_var(34)
objetoPila.show_var()

objetoPila.te = 20
print(objetoPila.te)


""" 
Observación: De acuerdo con lo que se observa en el código anterior
el mecanismo de privacidad funciona, sin embargo, se puede definir 
cualquier variable con punto y se esta creando una nueva variable
"""
