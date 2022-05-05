# lst = [1, 2]
# for v in range(2):
#     lst.insert(-1, lst[v]) # inserta en el primer argumento, lo que hay en el segundo arg
# print(lst)

# ---------------------------------------

# # None * None

# ---------------------------------------

# z = 0
# y = 0
# x = y < z and z > y or y > z and z < y
# print(x)

# ---------------------------------------
# list = [x*x for x in range(5)]
# print(list)


# def fun(lst):
#     del lst[lst[2]]
#     return lst


# print(fun(list))

# ---------------------------------------

# x = 1
# y = 2
# x, y, z = x, x, y
# z, y, z = x, y, z
# print(x, y, z)

# ---------------------------------------

# lst = [i for i in range(-1, -2)]
# print(lst)

# ---------------------------------------

# tup = (1, 2, 4, 8)
# tup = tup[-2:-1]
# print(tup)
# tup = tup[-1]
# print(tup)

# ---------------------------------------

# dct = {}
# dct['1'] = (1, 2)
# dct['2'] = (2, 1)
# for x in dct.keys():
#     print(dct[x][1], end='')

# ---------------------------------------

# lst = [[x for x in range(3)] for y in range(3)]
# print(lst)
# for r in range(3):
#     for c in range(3):
#         if lst[r][c] % 2 != 0:
#             print("#")
