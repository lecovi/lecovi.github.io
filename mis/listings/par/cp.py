#!/usr/bin/env python

BUFFER = 10
filename = input('Ingrese el nombre de archivo: ')

with open(filename, 'rb') as archivo:
    if '.' in filename:
        nombre, extension = filename.split('.')
        copia_filename = '{}_copia.{}'.format(nombre, extension)
    else:
        copia_filename = '{}_copia'.format(filename)
    with open(copia_filename, 'wb') as copia:
        buffer = archivo.read(BUFFER)
        while buffer != b'':
            copia.write(buffer)
            buffer = archivo.read(BUFFER)
