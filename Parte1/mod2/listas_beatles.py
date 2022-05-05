# paso 1
beatles=[]
print("Paso 1:", beatles)

# paso 2
print("Paso 2:", beatles)
beatles.append("Jhon Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")


# paso 3
print("Paso 3:", beatles)
for i in ["Stu Sutcliffe", "Pete Best"]:
    user_name=input("ingrese a " + i + ":")
    beatles.append(user_name)

# etapa 4
print("Paso 4:", beatles)
del beatles[-1]
del beatles[-1]

# paso 5
beatles.insert(3,'Ringo Starr')
print("Paso 5:", beatles)



# probando la longitud de la lista
print("Los Fab", len(beatles))