#!/usr/bin/env python
"""
EDD: Creando objetos - Alumno.

Importamos el módulo random para que la creación de objetos sea pseudo-aleatoria.
"""

import random


class Alumno:
    """ Nuestra propia clase Alumno. """
    def __init__(self, nombre, edad=18, materias=[]):
        self.nombre = nombre
        self.edad = edad
        self.materias = materias

    def __repr__(self):
        return '<Alumno {}>'.format(self.nombre)

    def __str__(self):
        return 'Soy {}'.format(self.nombre)

    def inscribir(self, materia):
        """ Inscripción a materias. """
        self.materias.append(materia)
    
    def listar_materias(self):
        """ Lista cada una de las materias del alumno, una por línea. """
        print('Listado de materias:')
        if not self.materias:
            print('\tEl alumno no está inscripto en materias.')
            return
        for materia in self.materias:
            print('\t- {}'.format(materia))


if __name__ == '__main__':
    MATERIAS = ['ARQ', 'EDD', 'DLO', 'PAR', 'TIC', 'ANA', 'LOG']
    NOMBRES = ['Pluto', 'Silvestre', 'Nemo', 'Piolín']

    alumno = Alumno(nombre=random.choice(NOMBRES))

    print(alumno)
    alumno.inscribir(materia=random.choice(MATERIAS))
    alumno.inscribir(materia=random.choice(MATERIAS))

    alumno.listar_materias()