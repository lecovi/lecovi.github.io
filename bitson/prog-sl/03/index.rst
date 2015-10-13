.. title: Clase 3: Definiciones
.. slug: bitson/prog-sl/03
.. date: 2015-10-13 00:50:56 UTC-03:00
.. tags:
.. category:
.. link:
.. description:
.. type: text

.. class:: alert alert-info pull-right

.. contents::

Identificadores
===============

Los identificadores son un conjunto de símbolos que se usan para denominar a
los elementos de un programa en Python. Estos elementos a los que hacemos
referencia son los nombres de variables, módulos, clases, métodos, funciones, etc...

Para tener un identificador válido en Python este debe cumplir con las siguientes:

    * debe comenzar con una letra.
    * continúa con una secuencia de números, letras y/o guiones bajos.
    * cualquier otro símbolo no está permitido.

*RECORDÁ: Python distingue entre mayúsculas y minúsculas.*

Palabras reservadas en Python:
------------------------------

Python tiene 31 palabras reservadas. Es decir, 31 conjuntos de símbolos que no
se pueden usar como identificadores válidos. Estos son:

.. code:: python

        and       as      assert   break  class
        continue  def     del      elif   else
        except    exec    finally  for    from
        global    if      import   in     is
        lambda    not     or       pass   print
        raise     return  try      while  with
        yield

Expresiones
===========

Una *expresión* es un conjunto de símbolos que representa un valor.

Por ejemplo::

    5 + 3


Representa al valor **8**. Si ejecutamos esta expresión en el intérprete de
python éste nos devolverá el valor de la expresión::

    >>> 5 + 3
    8
    >>>

Funciones
=========

Conjunto de instrucciones que están asociados a un identificador.

¿Cómo se define una función?
----------------------------

.. code:: python

    def identificador(argumentos_separados_por_coma):
        <instrucciones>

Por ejemplo:

.. code:: python

    def saludo(nombre):
        print("Hola {}".format(nombre))

Esto define la función ``saludo()`` que necesita un argumento que
se llama `nombre` y lo que hace es ejecutar la instrucción `print`.

Documentando la función
-----------------------

Para agregar un **docstring** agreamos una cadena de texto en la
primer línea luego de la definición con ``def``:

.. code:: python

    def saludo(nombre):
        """Recibe un nombre y lo saluda."""
        print("Hola {}".format(nombre))

En el intérprete se puede consultar con la función ``help``::

>>> help(saludo)

O usando ``__doc__``::

>>> saludo.__doc__

Metodología para resolver problemas
===================================

1. **Analizar el problema**
    Entender profundamente *cuál* es el problema que se trata de resolver, incluyendo el contexto en el cual se usará.
2. **Especificar la solución**
    Éste es el punto en el cual se describe *qué* debe hacer el programa,
    sin importar el cómo. En el caso de los problemas sencillos que abordaremos,
    deberemos decidir cuáles son los datos de entrada que se nos proveen,
    cuáles son las salidas que debemos producir, y cuál es la relación entre
    todos ellos.
3. **Diseñar la solución.**
    Éste es el punto en el cuál atacamos el *cómo* vamos a resolver el problema,
    cuáles son los algoritmos y las estructuras de datos que usaremos.
    Analizamos posibles variantes, y las decisiones las tomamos usando como dato
    de la realidad el contexto en el que se aplicará la solución, y los costos
    asociados a cada diseño.
4. **Implementar el diseño**
    Traducir a un lenguaje de programación (en nuestro caso, y por    el
    momento, Python) el diseño que elegimos en el punto anterior.
5. **Probar el programa**
    Diseñar un conjunto de pruebas para probar cada una de sus partes por
    separado, y también la correcta integración entre ellas.
    Utilizar el *depurador* como instrumento para descubir dónde se producen
    ciertos errores.
6. **Mantener el programa**
    Realizar los cambios en respuesta a nuevas demandas.
