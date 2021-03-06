.. title: Condicionales
.. slug: bitson/prog-sl/04
.. date: 2015-08-25 13:27:56 UTC-03:00
.. tags:
.. category:
.. link:
.. description:
.. type: text

.. class:: alert alert-info pull-right

.. contents::

Qué pasa si...
==============

Supongamos que tengamos el siguiente problema.

.. admonition:: **Problema 4.1**

    Debemos leer un número y, si el número es positivo, debemos escribir en
    pantalla el cartel “``Número positivo``”.

    *Solución*: se deberá leer un número ``x``. Si `x > 0` se escribe el mensaje
    "``Número positivo``".

Diseñamos nuestra solución:

#. Solicitar al usuario un número, guardarlo en ``x``.
#. Si ``x > 0``, imprimir "``Número positivo``"

Es claro que la primera línea se puede traducir como:

.. code-block:: python

    x = int(input("Ingrese un numero: "))

Sin embargo, con las instrucciones que vimos hasta ahora no podemos tomar el
tipo de decisiones que nos planteamos en la segunda línea de este diseño.
Para resolver este problema introducimos una nueva instrucción que llamaremos
**condicional** que tiene la siguiente forma:

.. code-block:: python

    if <condición>:
        <hacer algo si se da la condición>

Donde ``if`` es una de las 31 palabra reservadas que tiene el lenguaje Python.

¿Qué es la condición que aparece luego de la palabra reservada ``if``?

Antes de seguir adelante con la construcción debemos introducir un nuevo tipo de
expresión que nos indicará si se da una cierta situación o no. Hasta ahora las
expresiones con las que trabajamos fueron de tipo numérica y de tipo texto. Pero
ahora la respuesta que buscamos es de tipo sí o no.

Expresiones booleanas
---------------------

Además de los números y los textos que vimos hasta ahora, Python introduce las
constantes ``True`` y ``False`` para representar los valores de verdad verdadero
y falso respectivamente.
Vimos que una expresión es un trozo de código Python que produce o calcula un
valor (resultado). Una expresión booleana o expresión lógica es una expresión
que vale o bien ``True`` o bien ``False``.

Operadores relacionales
~~~~~~~~~~~~~~~~~~~~~~~

En el ejemplo que queremos resolver, la condición que queremos ver si se cumple
o no es que ``x`` sea mayor que cero. Python provee las llamadas expresiones de
comparación que sirven para comparar valores entre sí, y que por lo tanto
permiten codificar ese tipo de pregunta. En particular la pregunta de si ``x``
es mayor que cero, se codifica en Python como ``x > 0``.

De esta forma, ``5 > 3`` es una expresión booleana cuyo valor es ``True``, y
``5 < 3`` también es una expresión booleana, pero su valor es ``False``.

    >>> 5 > 3
    True
    >>> 3 > 5
    False
    >>>

Los operadores booleanos de comparación que provee Python son los siguientes:

.. class:: col-md-12 text-center

.. class:: align-center

    +-----------------------------------+------------+
    | Significado                       | Expresión  |
    +===================================+============+
    |``a`` **es igual a** ``b``         | ``a == b`` |
    +-----------------------------------+------------+
    |`a` **no es igual a** ``b``        | ``a != b`` |
    +-----------------------------------+------------+
    |``a`` **es mayor a** ``b``         | ``a > b``  |
    +-----------------------------------+------------+
    |``a`` **es menor a** ``b``         | ``a < b``  |
    +-----------------------------------+------------+
    |``a`` **es mayor o igual a** ``b`` | ``a >= b`` |
    +-----------------------------------+------------+
    |``a`` **es menor o igual a** ``b`` | ``a <= b`` |
    +-----------------------------------+------------+

Operadores lógicos
~~~~~~~~~~~~~~~~~~

De la misma manera que se puede operar entre números mediante las operaciones de
suma, resta, etc., también existen tres operadores lógicos para combinar
expresiones booleanas: ``and`` (y), ``or`` (o) y ``not`` (no).

El significado de estos operadores es igual al del castellano, pero vale la pena
recordarlo:

:``not a``:
    El resultado es ``True`` si ``a`` es ``False``.
    Y el resultado es ``False`` si ``a`` es ``True``.
:``a and b``:
    El resultado es ``True`` solamente si ``a`` y ``b`` valen ``True``.
    Sino el resultado es ``False``.
:``a or b``:
    El resultado es ``False`` solamente si ``a`` y ``b`` valen ``False``.
    Sino el resultado es ``True``.

Comparaciones simples
---------------------

Volvemos al problema que nos plantearon: Debemos leer un número y, si el número
es positivo, debemos escribir en pantalla el mensaje "``Número positivo``".

Utilizando la instrucción ``if`` que acabamos de introducir y que sirve para
tomar decisiones simples. Dijimos que su formato más sencillo es:

.. code-block:: python

    if <condición>:
        <hacer algo si se da la condición>

cuyo significado es el siguiente: se evalúa el valor de ``<condición>`` y si el
resultado es ``True`` (verdadero) se ejecutan las acciones indicadas como
``<hacer algo si se da la condición>``.

Como ahora ya sabemos también cómo construir condiciones de comparación, estamos
en condiciones de implementar nuestra solución. Escribimos la función
``es_positivo()`` que hace lo pedido:

.. code-block:: python

    def es_positivo():
        x = int(input("Ingrese un numero: "))
        if x > 0:
            print("Número positivo")

y podemos probarla:

    >>> es_positivo()
    Ingrese un numero: 4
    Numero positivo
    >>> es_positivo()
    Ingrese un numero: -25
    >>> es_positivo()
    Ingrese un numero: 0
    >>>

.. class:: col-md-12

Y si no...
==========

.. admonition:: **Problema 4.2**

    En la etapa de mantenimiento nos dicen que, en realidad, también se
    necesitaría un mensaje "``Número no positivo``" cuando no se cumple la
    condición.

Modificamos la especificación consistentemente y modificamos el diseño:

#. Solicitar al usuario un número, guardarlo en ``x``.
#. Si ``x > 0``, imprimir "``Número positivo``"
#. Si no se cumple ``x > 0``, imprimir "``Número no positivo``"

La negación de ``x > 0`` es `¬(x > 0)` que se traduce en Python como
``not (x > 0)``, por lo que implementamos nuestra solución en Python como:

.. code-block:: python

    def positivo_o_no():
        x = input("Ingrese un número: ")
        if x > 0:
            print("Número positivo")
        if not (x > 0):
            print("Número no positivo")

Probamos la nueva solución y obtenemos el resultado buscado:

    >>> positivo_o_no()
    Ingrese un numero: 4
    Numero positivo
    >>> positivo_o_no()
    Ingrese un numero: -25
    Numero no positivo
    >>> positivo_o_no()
    Ingrese un numero: 0
    Numero no positivo
    >>>50

Sin embargo hay algo que nos preocupa: si ya averiguamos una vez, en la segunda
línea del cuerpo, ``si x > 0``, ¿Es realmente necesario volver a preguntarlo en
la cuarta?.

Existe una construcción alternativa para la estructura de decisión:

**Si se da la condición `C`, hacer `S`, de lo contrario, hacer `T`**. Esta
estructura tiene la forma:

.. code-block:: python

    if <condición>:
        <hacer algo si se da la condición>
    else:
        <hacer otra cosa si no se da la condición>

Donde ``if`` y ``else`` son palabras reservadas.

Su significado es el siguiente: se evalúa ``<condición>``, si el resultado es
``True`` (verdadero) se ejecutan las acciones indicadas como ``<hacer algo si
se da la condición>``, y si el resultado es ``False`` (falso) se ejecutan las
acciones indicadas como ``<hacer otra cosa si no se da la condición>``.

Volvemos a nuestro diseño:

#. Solicitar al usuario un número, guardarlo en ``x``.
#. Si ``x > 0``, imprimir "``Número positivo``".
#. De lo contrario, imprimir "``Número no positivo``".

Este diseño se implementa como:

.. code-block:: python

    def positivo_o_no_nue():
        x = input("Ingrese un numero: ")
        if x > 0:
            print("Número positivo")
        else:
            print("Número no positivo")

y lo probamos:

    >>> positivo_o_no_nue()
    Ingrese un numero: 4
    Numero positivo
    >>> positivo_o_no_nue()
    Ingrese un numero: -25
    Numero no positivo
    >>> positivo_o_no_nue()
    Ingrese un numero: 0
    Numero no positivo
    >>>

Es importante destacar que, en general, negar la condición del ``if`` y poner
``else`` no son intercambiables, no necesariamente producen el mismo efecto en
el programa. Notar qué sucede en los dos programas que se transcriben a
continuación. ¿Por qué se dan estos resultados?

.. class:: col-md-6

    >>> def pn():
    ...     x = int(input("Ingrese un número: "))
    ...     if x > 0:
    ...         print("Número positivo")
    ...     x = -x
    ...     if x < 0:
    ...         print("Número no positivo")
    ...
    >>> pn()
    Ingrese un numero: 25
    Número positivo
    Número no positivo
    >>>

.. class:: col-md-6

    >>> def pn1():
    ...     x = int(input("Ingrese un numero: "))
    ...     if x > 0:
    ...     print("Número positivo")
    ...     x = -x
    ...     else:
    ...     print("Número no positivo")
    ...
    >>> pn1()
    Ingrese un numero: 25
    Numero positivo
    >>>

.. class:: col-md-12

Y si si, y si no...?
====================

Múltiples condicionales anidados
--------------------------------

La decisión de incluir una alternativa en un programa, parte de una lectura
cuidadosa de la especificación. En nuestro caso la especificación nos decía:

    Si el número es positivo escribir un mensaje "``Número positivo``", de lo
    contrario escribir un mensaje "``Número no positivo``".

Veamos qué se puede hacer cuando se presentan tres o más alternativas:

.. admonition:: **Problema 4.3**

    Si el número es positivo escribir un mensaje "``Número positivo``", si el
    número es igual a 0 un mensaje "``Igual a 0``", y si el número es negativo
    escribir un mensaje "``Número negativo``".

Una posibilidad es considerar que se trata de una estructura con dos casos como
antes, sólo que el segundo caso es complejo (es nuevamente una alternativa):

    1. Solicitar al usuario un número, guardarlo en ``x``.
    2. Si ``x > 0``, imprimir "``Número positivo``".
    3. De lo contrario:

        a. Si ``x = 0``, imprimir "``Igual a 0``"
        b. De lo contrario, imprimir "``Número no positivo``"

Este diseño se implementa como:

.. code-block:: python

    def pcn1():
        x = int(input("Ingrese un número: "))
        if x > 0:
            print("Número positivo")
        else:
            if x == 0:
                print("Igual a 0")
            else:
                print("Numero negativo")

Esta estructura se conoce como de alternativas anidadas ya que dentro de una de
las ramas de la alternativa (en este caso la rama del else) se anida otra
alternativa.

Pero ésta no es la única forma de implementarlo. Existe otra construcción,
equivalente a la anterior pero que no exige sangrías cada vez mayores en el
texto. Se trata de la estructura de alternativas encadenadas, que tiene la
forma:

.. code-block:: python

    if <condición_1>:
        <hacer algo_1 si se da la condición_1>
    elif <condición_2>:
        <hacer algo_2 si se da la condición_2>
    ...
    elif <condición_n>:
        <hacer algo_n si se da la condición_n>
    else:
        <hacer otra cosa si no se da ninguna de las condiciones anteriores>

Donde ``if``, ``elif`` y ``else`` son palabras reservadas.

En nuestro ejemplo:

.. code-block:: python

    def pcn2():
        x = int(input("Ingrese un número: "))
        if x > 0:
            print("Número positivo")
        elif x == 0:
            print("Igual a 0")
        else:
            print("Número negativo")

Se evalúa la primera alternativa, si es verdadera se ejecuta su cuerpo. De lo
contrario se evalúa la segunda alternativa, si es verdadera se ejecuta su
cuerpo, etc. Finalmente, si todas las alternativas anteriores fallaron, se
ejecuta el cuerpo del ``else``.


.. class:: alert alert-info

    No sólo mediante los operadores vistos (como ``>`` o ``=``) es posible
    obtener expresiones booleanas. En Python, se consideran verdaderos los
    valores numéricos distintos de 0, las cadenas de caracteres que no son
    vacías, y en general cualquier valor que no sea ``0`` o vacío. Mientras
    que los valores 0 o vacíos se consideran falsos.

    Así, el ejemplo anterior también podría escribirse de la siguiente manera:

    .. code-block:: python

        def pcn2():
            x = int(input("Ingrese un número: "))
                if x > 0:
                    print("Número positivo")
                elif not x:
                    print("Igual a 0")
                else:
                    print("Número negativo")
