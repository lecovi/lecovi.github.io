#!/usr/bin/env python

archivo = open('usuarios.txt')

for linea in archivo:
    print(linea, end='')

archivo.close()