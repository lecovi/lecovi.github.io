#!/usr/bin/env python

filename = input('Ingrese el nombre de archivo: ')
cant_lineas = int(input('Ingrese la cantidad de líneas a leer: '))

with open(filename, 'r') as archivo:
    for i in range(cant_lineas):
        linea = archivo.readline()
        print(linea, end='')
