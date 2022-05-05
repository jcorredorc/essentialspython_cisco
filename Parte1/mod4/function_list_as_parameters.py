def miFuncion_uno(miLista1):
    print(miLista1)
    miLista1 = [0, 1]

def miFuncion_dos(miLista1):
    print(miLista1)
    del miLista1[0]

miLista2 = [2, 3]
miFuncion_uno(miLista2)
print(miLista2)
## print(miLista1) # no existe!


miLista2 = [2, 3]
miFuncion_dos(miLista2)
print(miLista2)