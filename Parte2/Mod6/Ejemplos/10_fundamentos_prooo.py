"""
Ejemplo coómo se pueden modificar atributos entre clases
por medio de métodos

"""


class Clase1:

    def __init__(self, doc):
        self.doc = doc

    def print_doc(self):
        print("doc:", self.doc)

    def update_doc(self, nuevo_doc):
        self.doc = nuevo_doc


class Clase2:
    def __init__(self):
        self.msg = "clase2"

    def update_msg(self, obj_clase1, msg):
        """ Actualiza un atributo de un objeto de otra clase
        se pasa como argumento el objeto y se hace uso de su metodo
        para actualizar el parámetro
        """
        obj_clase1.update_doc(msg)
        print("Desde", self.msg, "actualizo doc a:", msg)


if __name__ == "__main__":
    user1 = Clase1("clase1")
    user1.print_doc()
    user2 = Clase2()
    user2.update_msg(user1, "actualizo un atributo de user1 desde user2")
    user1.print_doc()
