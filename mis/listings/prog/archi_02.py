#!/usr/bin/env python
# encoding: utf-8

# abro el archivo prueba01.txt
# para escritura
ae = open("prueba01.txt","w")

# escribo una linea
ae.write("primera\n")
# escribo otra linea
ae.write("segunda\n")

# cierro el archivo
ae.close()

# abro el archivo prueba01.txt
# para lectura
ae = open("prueba01.txt","r")

# leo una linea
s1 = ae.readline()
# leo otra linea
s2 = ae.readline()
# muestro las lineas leidas
print(s1, s2)
# cierro el archivo
ae.close()

# abro el archivo prueba01.txt
# para lectura
ae = open("prueba01.txt","r")
for lin in ae:
    print(lin)
# cierro el archivo
ae.close()




