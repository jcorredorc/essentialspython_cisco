miLista = [8, 10, 6, 2, 4] # lista para ordenar

for i in range(len(miLista) - 1): # necesitamos (5 - 1) comparaciones
    if miLista[i] > miLista[i + 1]: # compara elementos adyacentes
        miLista[i], miLista [i + 1] = miLista[i + 1], miLista[i] # si terminamos aquí 
        #significa que tenemos que intercambiar los elementos.

miLista = [8, 10, 6, 2, 4] # lista para ordenar
swapped = True # lo necesitamos verdadero (True) para ingresar al bucle while

while swapped:
    swapped = False # no hay swaps hasta ahora
    for i in range(len(miLista) - 1):
        if miLista[i] > miLista[i + 1]:
            swapped= True # ocurrió el intercambio!
            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]

# version interaciva ----
miLista = []
swapped = True
num = int (input("¿Cuántos elementos deseas ordenar?:"))

for i in range(num):
    val = float(input("Introduce un elemento de la lista:"))
    miLista.append(val)

while swapped:
    swapped = False
    for i in range(len(miLista) - 1):
        if miLista[i] > miLista[i + 1]:
            swapped = True
            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]

print("\nOrdenado:")
print(miLista)