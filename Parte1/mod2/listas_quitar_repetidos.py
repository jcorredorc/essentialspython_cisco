miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
Lista=[]
## ----------------------------------------
#con continue ..
## ----------------------------------------
# for i in range(len(miLista)):
#     if miLista[i] in miLista[i+1:-1]:
#         continue
#     else:
#         Lista.append(miLista[i])

# print("La lista solo con elementos únicos:")
# print(Lista)
## ----------------------------------------
## sin usar continue ...
## ----------------------------------------
for i in range(len(miLista)):
    if  miLista[i] not in miLista[i+1:-1]:
        Lista.append(miLista[i])

print("La lista solo con elementos únicos:")
print(Lista)