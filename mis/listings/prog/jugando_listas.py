#!/usr/bin/env python3

# Crear una lista de veinte elementos aleatorios entre 1 y 10
# Mostrar:
#   La lista ordenada
#   El numero mayor
#   El numero menor
#   Cuantas veces aparece en la lista el numero mayor

import random

def lista_aleatoria(cantidad, minimo=1, maximo=10):
    lista = list()
    for i in range(cantidad):
        numero = random.randint(minimo, maximo)
        lista.append(numero)
    return lista

def busco_max(lista):
    maximo = lista[0]
    for item in lista[1:]:
        if item > maximo:
            maximo = item
    return maximo

def busco_min(lista):
    minimo = lista[0]
    for item in lista[1:]:
        if item < minimo:
            minimo = item
    return minimo

def ordenamos(lista):
    for passnum in range(len(lista)-1,0,-1):
        for i in range(passnum):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]

CANT = 20

print("Genero una lista de {} numeros".format(CANT))
lista = lista_aleatoria(CANT)
print(lista)
print("La muestro ordenada...")
# La ordenamos
lista.sort()
# La mostramos
print(lista)
maximo = busco_max(lista)
print("El maximo de la lista es: {}".format(maximo))
repeticiones_maximo = lista.count(maximo)
print("El maximo aparece en la lista {} veces".format(repeticiones_maximo))
minimo = busco_min(lista)
print("El minimo de la lista es: {}".format(minimo))
