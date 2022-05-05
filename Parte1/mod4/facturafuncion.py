factura = {}

datos={"FACTURA","factura:01","VENDEDOR:JUAN","DATOS DEL CLIENTE","BRAYAN CARDENAS","DOCUMENTO:1034779623",
"TELEFONO:3208140534"}
continuar = True
while continuar:
    item = input('Introduce un artículo: ')
    codigo = input('introduces codigo de articulo:')
    precio = float(input('Introduce el precio de ' + item + ': '))
    factura[item] = precio
    continuar = input('¿Quieres añadir artículos a la lista (Si/No)? ') == "Si"
coste = 0
print('Lista de la compra')
for i in (datos):
    print(i)
for item, precio in factura.items():
    print('codigo de articulo:',codigo,'\n',item, '\n', precio)
    coste += precio
print('Coste total: ', coste,)
