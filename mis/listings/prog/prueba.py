#!/usr/bin/env python3

# funcion que calcula el promedio
# de dos numeros
def promedio(numero1, numero2):
    prom = (numero1 + numero2) / 2

    return prom

print(promedio(8, 5))

p = int(input("ingrese un num: " ))
q = int(input("ingrese otro num: " ))

t = promedio(p, q)

print(t)

print(promedio(promedio(10,20), promedio(30,40)))
