#!/usr/bin/env python

archivo = open('nuevos_usuarios.txt', 'a')

usuario = input('Ingrese nombre de nuevo usuario [ENTER para salir]: ')
while usuario != '':
    archivo.write(usuario)
    archivo.write('\n')
    usuario = input('Ingrese nombre de nuevo usuario [ENTER para salir]: ')

archivo.close()

archivo = open('nuevos_usuarios.txt')

for linea in archivo:
    print(linea, end='')

archivo.close()