class ClaseEjemplo:
    __contador = 0  # variable clase

    def __init__(self, val=1):  # observe que si no se pasa ningun valor a 'val' por defecto es 1
        self.__primera = val
        ClaseEjemplo.__contador += 1  # se le suma 1 cada vez que se crea un objeto


objetoEjemplo1 = ClaseEjemplo()
objetoEjemplo2 = ClaseEjemplo(2)
objetoEjemplo3 = ClaseEjemplo(4)

print(objetoEjemplo1.__dict__, objetoEjemplo1._ClaseEjemplo__contador)
print(objetoEjemplo2.__dict__, objetoEjemplo2._ClaseEjemplo__contador)
print(objetoEjemplo3.__dict__, objetoEjemplo3._ClaseEjemplo__contador)

# Las variables de clase no se muestran en el diccionario de un objeto __dict__
# (esto es natural ya que las variables de clase no son partes de un objeto)

# Una variable de clase siempre presenta el mismo valor en todas las instancias de clase (objetos).
