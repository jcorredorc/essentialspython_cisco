class ClaseEjemplo:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


objetoEjemplo = ClaseEjemplo(1)

print(objetoEjemplo.a)
try:
    print(objetoEjemplo.b)  # Esta linea genera error!
except AttributeError:
    pass

"""
En este caso el objeto solo puede tener uno de los dos atributos
a o b, por esto genera el error AttributeError
cuando se usa el atributo 'b' ya que no existe!
"""

# ----------------------------------------

"""
Podemos verificar con la función hasattr()
función que puede verificar con seguridad si algún 
objeto / clase contiene una propiedad específica. 
"""


class ClaseEjemplo2:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


objetoEjemplo2 = ClaseEjemplo2(1)
print(objetoEjemplo2.a)

if hasattr(objetoEjemplo2, 'b'):
    print(objetoEjemplo2.b)

""" 
Probando con una variable de clase
"""


class ClaseEjemplo3:
    attr = 1


print(hasattr(ClaseEjemplo3, 'attr'))
print(hasattr(ClaseEjemplo3, 'prop'))
