.. title: Jugando con Python
.. slug: cfp/prog/03
.. date: 2016-04-06 08:02:11 UTC-03:00
.. tags:
.. category:
.. link:
.. description:
.. type: text

.. class:: alert alert-info pull-right

.. contents::

Antes de ponernos a jugar con Python, veamos algunos conceptos necesarios...

Valores Lógicos
===============

Son valores *verdaderos* o *falsos*. En python son:

* ``True`` 
* ``False``

*NOTA*: Por convención se toma que cualquier valor que no sea ``False`` o 
``None`` es considerado como *verdadero*.

Operadores Relacionales
=======================

Los operadores relacionales devuelven valores lógicos según la relación de sus
operandos:

* Igualdad: ``==``
* Deigualdad: ``!=``
* Mayor: ``>``
* Mayor o igual: ``>=``
* Menor: ``<``
* Menor o igual: ``<=``

Operadores Lógicos
==================

Los operadores lógicos devuelven valores lógicos según los operandos:

* ``not``: devuelve ``True`` si el operando es ``False`` y viceversa.
* ``or``: devuelve ``False`` si y sólo si todos sus operandos son ``False``.
* ``or``: devuelve ``True`` si y sólo si todos sus operandos son ``True``.

Condicionales
=============

Simples
-------

.. code-block:: python

    if <condicion>:
        <sentencias que se ejecutan si 'condicion' es verdadero>

Con "sino"
----------

.. code-block:: python

    if <condicion>:
        <sentencias que se ejecutan si 'condicion' es verdadero>
    else:
        <sentencias que se ejecutan si 'condicion' es falso>

Anidados
--------

.. code-block:: python

    if <condicion1>:
        <sentencias que se ejecutan si 'condicion1' es verdadero>
    elif <condicion2>:
        <sentencias que se ejecutan si 'condicion2' es verdadero>
    else:
        <sentencias que se ejecutan si 'condicion1' y 'condicion2' es falso>

Ejemplos
========

Informa si el interés es mayor al 30%, sino informa el importe total:

.. code-block:: python

    int(input("Ingrese monto: "))

    interes = float(input("Ingrese interés mensual: "))

    if interes > 30:
        print("El interés ingresado es incorrecto")
    else:
        monto_final = monto * (1 + interes / 100)
        print("Monto final: %08.2f" % monto_final)
        print("FIN").. code-block:: python

interes.py_

.. _interes.py: /prog/interes.py

Informa si el número ingresado está entre 1 y 7:

.. code-block:: python

    numero = int(input("Ingrese un número: "))

    if numero >= 1 and numero <= 7:
        print("El número ingresado está entre 1 y 7")
    else:
        print("El número ingresado NO está entre 1 y 7")

entre1y7.py_

.. _entre1y7.py: /prog/entre1y7.py

Informa si el numero es positivo, negativo o 0:

.. code-block:: python

    numero = int(input("Ingrese número: "))

    if numero >0:
        print("positivo")
    elif numero < 0:
        print("negativo")
    else:
        print("cero")

signo.py_

.. _signo.py: /prog/signo.py

Ejercicios
==========

1) Decir si un numero es par o impar
2) De dos números que se ingresan, informar el mayor.
3) Calcular el seno de un angulo ingresado.
   Si es mayor a 1 asumir que es en grados, de lo contrario usar radianes.

Turtle
======

.. class:: align-center

    .. raw:: html

        <iframe src="https://docs.google.com/presentation/d/1Y9rEGUf3puS-9HKbmODBVWiSIpwqJ-MId-W-A9VwJTs/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="629" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

.. class:: align-right

Seguí la presentación en este |turtle|.

.. |turtle| raw:: html

    <a href="https://docs.google.com/presentation/d/1Y9rEGUf3puS-9HKbmODBVWiSIpwqJ-MId-W-A9VwJTs/present#slide=id.p" target="_blank">link</a>

Ejercicios resueltos
====================

#. Par o impar: parimpar.py_
#. Mayor: mayor.py_
#. Seno: seno.py_

.. _parimpar.py: /prog/parimpar.py
.. _mayor.py: /prog/mayor.py
.. _seno.py: /prog/seno.py

Ejercicios con Turtle
=====================

#. **Dibujar un rectángulo**
#. Dibujar una dona
#. Dibujar una círculo dividido en 8 sectores iguales.
#. Dibujar un cubo.
#. Dibujar un cilindro.
#. **Pedir al usuario que ingrese cantidad de lados y radio y dibujar el polígono correspondiente.**
#. Al anterior agregar: que permita ingresar
    #) coordenadas de inicio
    #) color
#. **Pensar el 1, 2, 3 como funciones que reciben todos los datos necesarios para el dibujo (coordenadas de inicio, tamaño, color, etc.)**
#. Ingresar 3 valores entre 0 y 100 y generar un gráfico de barras (usar 8.1)
#. Ingresar 3 valores entre 0 y 100 y generar un gráfico de torta (usar 8.3)
#. Generar un gráfico de barras o torta con hasta 10 valores diferentes entre 0% y 100% c/u. Validar entrada de datos. 

