#!/usr/bin/env python
"""
EDD: Creando objetos - Mascota.

Importamos el módulo random para que la creación de objetos sea pseudo-aleatoria.
"""

import random


class Mascota:
    """ Nuestra propia clase Mascota. """
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo

    def __repr__(self):
        return '<Mascota {}: {}>'.format(self.nombre, self.tipo)

    def __str__(self):
        return 'Soy {}'.format(self.nombre)

    def saludar(self):
        """ Saludo de la mascota. """
        print('Hola! Me llamo {}, tengo {} y soy un {}'.format(self.nombre, self.edad, self.tipo))


if __name__ == '__main__':
    TIPOS = ['perro', 'gato', 'pez', 'canario']
    NOMBRES = ['Pluto', 'Silvestre', 'Nemo', 'Piolín']

    mascota = Mascota(
        nombre=random.choice(NOMBRES),
        edad=random.randint(1,20),
        tipo=random.choice(TIPOS)
        )

    print(mascota)
    mascota.saludar()
