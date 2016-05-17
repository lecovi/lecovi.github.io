# -*- coding: utf-8 -*-
# generar una lista
# con los numeros de num
# mayores que 3

num = [10, 5, 6, 2, 8, 1]

# version 1 - con for
j = []
for n in num:
    if n > 3:
       j.append(n)

print(j)

# version 2 - con filter y una funcion
def mayor_a_3(x):
    return (x > 3)

g = list(filter(mayor_a_3, num))
print(g)

# version 3 - con filter y lambda
h = list(filter(lambda n: n > 3, num))
print(h)
