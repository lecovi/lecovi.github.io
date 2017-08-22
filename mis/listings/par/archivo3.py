#!/usr/bin/env python

with open('usuarios.txt') as archivo:
    for linea in archivo:
        print(linea, end='')
