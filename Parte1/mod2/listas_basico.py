numeros = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numeros) # imprime el contenido de la lista original

numeros[0] = 111 
print("Nuevo contenido de la lista:", numeros) # contenido de la lista actual.

## Indexación --------
numeros = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numeros) # imprimiendo contenido de la lista original.

numeros[0] = 111
print("\nPrevio contenido de la lista:", numeros) # imprimiendo contenido de la lista anterior.

numeros[1] = numeros[4]  # copiando el valor del quinto elemento al segundo
print("Nuevo contenido de la lista:", numeros) # imprimiendo el contenido de la lista actual.

## Funcion len()
print("\nLongitud de la lista:", len(numeros)) # imprimiendo la longitud de la lista

## instruccion del - eliminar elementos de la lista
del numeros[1] # eliminando el segundo elemento de la lista
print("Longitud de la nueva lista:", len(numeros)) # imprimiendo nueva longitud de la lista
print("\nNuevo contenido de la lista:", numeros) # imprimiendo el contenido de la lista actual

## error! ----
# print(numeros[4])
# numeros[4] = 1

## indices negativos
#Un elemento con un índice igual a -1 es el último en la lista.
print(numeros[-1])
# Del mismo modo, el elemento con un índice igual a -2 es el anterior al último en la lista.
print(numeros[-2])
# El último elemento accesible en nuestra lista es numeros[-4] (el primero).

## Metodos listas
numeros = [111, 7, 2, 1]
print(len(numeros))
print(numeros)

###

numeros.append(4)

print(len(numeros))
print(numeros)

###

numeros.insert(0,222)
print(len(numeros))
print(numeros)

#

## Agregamdo elementos a la lista
miLista = [] # creando una lista vacía

for i in range (5):
    miLista.append (i + 1)

print(miLista)

miLista = [] # creando una lista vacía

for i in range(5):
    miLista.insert(0, i + 1) # inset desplaza hacia la derecha
print(miLista)

## reorganizar listas

variable1 = 1
variable2 = 2

variable1, variable2 = variable2, variable1 


## punteros??
lista1 = [1]
lista2 = lista1
lista1[0] = 2
print(lista2)

## copiar lista
# Copiando toda la lista
lista1 = [1]
lista2 = lista1[:]
lista1[0] = 2
print(lista2)

# Copiando parte de la lista
miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista[1:3]
print(nuevaLista) 

#indices negativos
miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista [1:-1]
print(nuevaLista)

# salida vacia
miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista [-1:1]
print(nuevaLista)

# del con rodaja
miLista = [10, 8, 6, 4, 2]
del miLista[1:3] 
print(miLista)

#in not in
miLista = [0, 3, 12, 8, 2]

print(5 in miLista)
print(5 not in miLista)
print(12 in miLista)