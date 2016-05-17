.. title: Ejercicios varios
.. slug: cfp/prog/06
.. date: 2016-04-06 08:02:11 UTC-03:00
.. tags:
.. category:
.. link:
.. description:
.. type: text

1. Hacer una función que reciba un `string` S y un `número` N; tiene que
   devolver un `string` repitiendo las N primeras letras de S, luego las N-1,
   luego N-2… etc.

.. code-block:: python

    repeatFront("Chocolate", 4) --> "ChocChoChC"
    repeatFront("Chocolate", 3) --> "ChoChC"
    repeatFront("Ice Cream", 2) --> "IcI"
    repeatFront("abcde",3) --> abcaba


2. Hacer una función que recibe S1 y S2 y devuelve `True` si S1 termina con S2,
   o S2 termina en S1. Si no devuelve `False`.
   Mayúsculas y minúsculas se consideran iguales.

.. code-block:: python

    endOther("Hiabc", "abc") --> True
    endOther("AbC", "HiaBc") --> True
    endOther("abc", "abXabc") --> True


3. Hacer una funcion que devuelva `True` un `string` S, que recibe como
   parámetro, es palíndroma.

4. Hacer una función que recibe S1 y S2 (dos `strings`) y devuelve un `string`
   S formada por la primer letra de S1, la primer letra de S2, la segunda de S1,
   la segunda de S2 etc.

.. code-block:: python

    mezclar("uno", "dos") --> udnoos
    mezclar("abcd", "mnopqr") --> ambncodpqr


5. Hacer una función que devuelva una `lista` de C números aleatorios entre N1
   y N2

.. code-block:: python

    def crearLista(6, 2, 8) --> [2, 4, 4, 6, 7, 7]


6. Hacer una función que redondee un número decimal F a una cantidad D de
   decimales.

.. code-block:: python

    redondear(14.672, 1) -> 14.7
    redondear(14.672, 2) -> 14.67
    redondear(14.679, 0) -> 14


7. Usar la función del punto anterior en una función que recibe una lista de
   números decimales y devuelve una lista con todos sus números redondeados a 1
   decimal.

.. code-block:: python

    redondeaTodo([1.55, 5, 2.69, 0.258]) -> [1.6, 5, 2.7, 0.3]


8. Hacer un programa que genere un número de N cifras y pregunte al usuario
   números hasta que lo adivine.
   Mostrar la cantidad de intentos usados para adivinar el número.

9. Hacer una función que reciba como parámetros N1 y N2 y devuelva cuántos
   múltiplos de N1 hay que sean menores que N2.
   Hacerlo con ``for`` y con ``while`` ¿Cuál es la ventaja de cada una?

.. code-block:: python

    mulMenores(2, 15) -> 6    (4,6, 8, 10, 12, 14)


10. Hacer un programa que permita jugar al Mastermind:

Explicación del juego:

    Cada vez que se empieza un partido, el programa debe "eligir" un número de
    cuatro cifras (sin cifras repetidas), que será el código que el jugador
    debe adivinar en la menor cantidad de intentos posibles.

    Cada intento consiste en una propuesta de un código posible que tipea el
    jugador, y una respuesta del programa. Las respuestas le darán pistas al
    jugador para que pueda deducir el código.

    Estas pistas indican cuán cerca estuvo el número propuesto de la solución a
    través de dos valores:
    La cantidad de aciertos es la cantidad de dígitos que propuso el jugador
    que también están en el código en la misma posición.
    La cantidad de coincidencias es la cantidad de digitos que propuso el
    jugador que también están en el código pero en una posición distinta.

    Por ejemplo, si el código que eligió el programa es el 2607, y el jugador
    propone el 1406, el programa le debe responder un acierto (el 0, que está
    en el código original en el mismo lugar, el tercero), y una coincidencia
    (el 6, que también está en el código original, pero en la segunda posición,
    no en el cuarto como fue propuesto).

    Si el jugador hubiera propuesto  3591, habría obtenido como respuesta
    ningún acierto y ninguna coincidencia,
    ya que no hay números en común con el código original, y si se obtienen
    cuatro aciertos es porque el jugador adivinó el código y ganó el juego.


----

.. listing:: prog/palindroma_v1.py python3

.. listing:: prog/palindroma_v2.py python3

.. listing:: prog/filter.py python3

.. listing:: prog/map.py python3

.. listing:: prog/lambdas.py python3

.. listing:: prog/reduce.py python3
