#!/usr/bin/env python

archivo = open('usuarios.txt')

linea = archivo.readline()
while linea != '':
    print(linea, end='')
    linea = archivo.readline()

archivo.close()