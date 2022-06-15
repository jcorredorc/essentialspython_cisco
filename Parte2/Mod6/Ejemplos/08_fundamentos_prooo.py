"""
Cada clase de Python y cada objeto de Python está pre-equipado con un conjunto 
de atributos útiles que pueden usarse para examinar sus capacidades.

por ejemplo 

__dict__

__name__

__module__

__bases__

"""


class conClase:
    varia = 1

    def __init__(self):
        self.var = 2

    def metodo(self):
        pass

    def __oculto(self):
        pass


obj = conClase()

print(obj.__dict__)
print(conClase.__dict__)

# -----------------------------------


class otraClase:
    pass


print(otraClase.__name__)
obj = otraClase()
print(type(obj).__name__)

# observe que print(obj.__name__) causará un error


# -----------------------------------


class mClase:
    pass


print(mClase.__module__)
obj = mClase()
print(obj.__module__)


# -----------------------------------
# __bases__ es una tupla. La tupla contiene clases
# (no nombres de clases) que son superclases directas para la clase.
# Nota: solo las clases tienen este atributo - los objetos no.

class SuperUno:
    pass


class SuperDos:
    pass


class Sub(SuperUno, SuperDos):
    pass


def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


printBases(SuperUno)
printBases(SuperDos)
printBases(Sub)
