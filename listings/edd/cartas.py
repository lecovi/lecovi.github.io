#!/usr/bin/env python
"""
EDD: Creando objetos - Carta.

Importamos el módulo random para que la creación de objetos sea pseudo-aleatoria.
"""

import random


class Carta:
    """ Nuestra propia clase Carta. """
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

    def __repr__(self):
        return '<Carta {} de {}>'.format(self.valor, self.palo)

    def __str__(self):
        return 'El {} de {}'.format(self.valor, self.palo)


if __name__ == '__main__':
    PALOS = ['oros', 'bastos', 'copas', 'espadas']

    carta = Carta(
        valor=random.randint(1, 12),
        palo=random.choice(PALOS),
    )

    print(carta)
