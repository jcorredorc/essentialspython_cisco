"""
Este script muestra como acceder y manipular un objeto de cualquier clase
en particular, escanea todos los atributos. Si empiezan con la letra i
y son enteros los incrementa en 1
"""


class MiClase:
    pass


obj = MiClase()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.entero = 4
obj.z = 5


def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)


print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)