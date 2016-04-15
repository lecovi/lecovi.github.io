#!/usr/bin/env python3

# Calcular el seno de un angulo ingresado.
# Si es mayor a 1 asumir que es en grados,
# de lo contrario usar radianes

import math

ang = input("Ingrese un ángulo: ")

ang = float(ang)

if ang > 1:
    ang = math.radians(ang)
    
seno = math.sin(ang)

print("El seno del ángulo {} es {}".format(ang, seno))
