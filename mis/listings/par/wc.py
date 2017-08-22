#!/usr/bin/env python

filename = input('Ingrese el nombre de archivo: ')
cant_lineas = 0
cant_palabras = 0
cant_caracteres = 0

with open(filename, 'r') as archivo:
    linea = archivo.readline()
    while linea != '':
        cant_lineas += 1
        cant_caracteres += len(linea)
        cant_palabras += len(linea.split())
        linea = archivo.readline()

print('Cantidad de Líneas: {}'.format(cant_lineas))
print('Cantidad de Palabras: {}'.format(cant_palabras))
print('Cantidad de Caracteres: {}'.format(cant_caracteres))