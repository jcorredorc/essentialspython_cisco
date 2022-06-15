"""
Variables de clase: Ejemplo
"""


# ---------------------------------------------------------

class ClaseEjemplo:
    varia = 1

    def __init__(self, val):
        self.varia = val
        ClaseEjemplo.varia = 100


print(ClaseEjemplo.__dict__)

# Observe que no se ha creado aun un objeto de la clase
print("Variable de clase 'varia' es: ", ClaseEjemplo.varia)


# Creamos la clase
objetoEjemplo = ClaseEjemplo(2)
print("La variable 'varia' de objeto es ", objetoEjemplo.varia)
print("Variable de clase", ClaseEjemplo.varia)

print(ClaseEjemplo.__dict__)
print(objetoEjemplo.__dict__)
