import module_folder as mt
from sys import path
path.append('..\\modules')
# path.append('C:\\Users\\user\\py\\modules')## insert()


zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(mt.sum1(zeroes))
print(mt.prod1(ones))
print(mt.prod1(ones))
print("Se ha llamado las funciones: ", mt.__counter)
