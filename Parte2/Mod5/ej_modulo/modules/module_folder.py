#!/usr/bin/env python3

"""" module_test.py - an example of Pyhton module """

__counter1 = 0


def sum1(list):
    global __counter1
    __counter1 += 1
    sum = 0
    for e1 in list:
        sum += e1
    return sum


def prod1(list):
    global __counter1
    __counter1 += 1
    prod = 0
    for e1 in list:
        prod += e1
    return prod


if __name__ == "__main__":
    print("I prefer to be a module, but I can do some tests for you")
    l = [i+1 for i in range(5)]
    print(sum1(l) == 15)
    print(prod1(l) == 120)
