"""Una pila es una estructura donde se almacenan datos.
La pila a implementar es LIFO (Last In - First Out). Es decir, 
último en entrar, primero en salir.
Ej. Una pila de monedas organizada en vertical sobre una mesa, 
la ultima que se coloca es la primera que se puede tomar.
"""

# ------------------------------
#  Enfoque procedimental
# ------------------------------


# La pila se modela como una lista
pila = []


def push_pila(val):
    """Colocar un elemento en la pila"""
    pila.append(val)


def pop_pila():
    """Obtener y quitar de la pila el último elemento"""
    val = pila.pop(-1)
    return val


push_pila(3)
push_pila(3)
push_pila(1)

print(pila)
pop_pila()
print(pila)

# Desventajas:
# se puede modificar la pila accidentalmente
# siempre que necesite una pila, debo crear otra lista
# tal como está implementada necesitaría crear funciones para cada pila que necesite

# ------------------------------
# Enfoque POO
# ------------------------------

print("""

Con clases:

""")


class Pila:
    def __init__(self):
        self.listaPila = []

    def push(self, val):
        self.listaPila.append(val)

    def pop(self):
        self.listaPila.pop()


objetoPila = Pila()
objetoPila.push(1)
objetoPila.push(2)
objetoPila.push(3)
print(objetoPila.listaPila)
print("Longitud de la pila ", len(objetoPila.listaPila))
objetoPila.pop()
print(objetoPila.listaPila)
print("Longitud de la pila ", len(objetoPila.listaPila))
