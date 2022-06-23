"""
Ejemplo de case cajero modificando 
atributo de otra clase, cliente.
"""

class Cliente():
    def __init__(self,nombre):
        self.name = nombre
        self.__orden=[]
    def ingrese_orden(self,pedido):
        self.orden=pedido

class Cajero():
    def __init__(self,nombre):
        self.name = nombre
    def update_orden(self,obj_clase_cliente,new_orden):
        obj_clase_cliente.ingrese_orden(new_orden)



usuario1= Cliente("Pedro")
usuario1.ingrese_orden(["plato1","plato2","bebida"])
print(usuario1.orden)
usuario2= Cliente("Alberto")
usuario2.ingrese_orden(["plato3","plato4","bebida1"])

cajero= Cajero("Carlos")
cajero.update_orden(usuario1,["plato5","plato6"])
print("orden modificada:",usuario1.orden)



