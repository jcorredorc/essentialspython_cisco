"""
## Ejercicio 8
### Escenario
Tu tarea es escribir una función capaz de ingresar valores enteros y 
verificar si están dentro de un rango especificado.

### La función debe:
Aceptar dos argumentos:  un límite inferior aceptable y 
un límite superior aceptable.

Si el usuario ingresa una cadena que no es un valor entero, 
la función debe emitir el mensaje Error: entrada incorrecta, y 
solicitará al usuario que ingrese el valor nuevamente.

Si el usuario ingresa un número que está fuera del rango especificado,
la función debe emitir el mensaje Error: el valor no está dentro del 
rango permitido (min..max) y solicitará al usuario que ingrese el valor nuevamente.

Si el valor de entrada es válido, será regresado como resultado.

### Datos de Prueba
Prueba tu código cuidadosamente.
Así es como la función debería reaccionar ante la entrada del usuario:
```Python
Ingresa un número entre -10 a 10: 100
Error: el valor no está dentro del rango permitido (-10..10)
Ingresa un número entre -10 a 10: asd
Error: entrada incorrecta
Ingresa un número entre -10 a 10: 1
El número es: 1
```
"""

# def test_numbers():
#     ok=True
#     while ok:
#         try:
#             num=int(input("ingrese el número"))
#             maxm=int(input("ingrese el límite superior"))
#             minm=int(input("ingrese el límite inferior"))
#             ok = False
#         except:
#             print("Error: entrada incorrecta, ingrese nuevamente")
#             ok = True
#     if num<maxm and num > minm:
#         print("ok")
#     else:
#         print("bad")

# test_numbers()

def readint(min, max):
#
# tu codigo aqui
#
    flag = True
    while flag:
        try:
            msg="Ingresa un numero de " + str(min) + " a " + str(max) + " : "
            v= int(input(msg))
            # else:
            #     print("fuera de rango")
            flag = False
            if v > min and v < max:
                print("en el rango")
                return v
        except:
            print("Error: entrada incorrecta")
            flag = True
    
    # if v > min and v < max:
    #     print("en el rango")
    #     return v
    # else:
    #     print("fuera de rango")
    #     readint(min,max)


# v = readint("Ingresa un numero de -10 a 10: ", -10, 10)
v = readint(-10, 10)

print("El numero es:", v)