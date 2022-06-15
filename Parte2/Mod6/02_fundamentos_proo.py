"""
Cómo hacer privada la pila?  osea que no se pueda acceder a la lista
y poder modificarla?
"""


class Pila:
    def __init__(self):
        self.__listaPila = []

    def push(self, val):
        self.__listaPila.append(val)

    def pop(self):
        self.__listaPila.pop()


objetoPila = Pila()
objetoPila.push(1)
objetoPila.push(2)
objetoPila.push(3)
try:
    print(objetoPila.__listaPila)
    print("Longitud de la pila ", len(objetoPila.__listaPila))
    objetoPila.pop()
    print(objetoPila.__listaPila)
    print("Longitud de la pila ", len(objetoPila.__listaPila))
except:
    print("""
    No se pude acceder a la variable __listaPila porque..

    Al agregar dos rayas al piso al inicio del nombre del método o del atributo, 
    se vuelve privado y no permite acceder a esta variable.
    
    El error genera una excepción del tipo AttributeError 

    pero... :S
    """)

"""Observe que la siguiente linea de código no genera un error
y me permite borrar la lista "privada" __listaPila
"""

objetoPila.__listaPila = []

try:
    print("la lista modificada es: ", objetoPila.__listaPila)
    print("la long de lista modificada es: ", len(objetoPila.__listaPila))
except:
    print("Esto si genera error ???")

"""
Se puede considerar que esto es una convención que los programadores deben
conocer (nombre que inicia con _ _ es privado), pero en realidad Python no impide que se pueda 
acceder a  la variable privada (otros lenguajes como java, c++, etc si lo permiten)   
"""
