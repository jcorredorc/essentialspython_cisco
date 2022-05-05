import module
import module_test as mt
print(module.counter)

# -- module_test call
zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(mt.sum1(zeroes))
print(mt.prod1(ones))
print(mt.prod1(ones))
print("Se ha llamado las funciones: ", mt.__counter)
