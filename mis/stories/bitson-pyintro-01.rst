.. title: Introducción a Python - PyConAR2018
.. slug: bitson/pyintro2018
.. date: 2018-11-21 09:37:50 UTC-03:00
.. tags:
.. category:
.. link:
.. description:
.. type: text

Instalación Python
===================

Entrar a |python_org| y descargá la versión que corresponda a tu sistema operativo.

.. |python_org| raw:: html

    <a href="https://www.python.org" target="_blank">python.org</a>

.. image:: /images/pyintro/python.org.png
    :scale: 50 %
    :alt: Python ORG Homepage
    :class: align-center

Instalación de un Editor de Texto
=================================

Para programar en Python (así como en cualquier lenguaje), vamos a necesitar un editor de texto.
Podés usar el que más te guste: Vim, Vi, Nano, Atom, VSCode, SublimeText, etc...

Te recomiendo que uses |vscode|.

.. |vscode| raw:: html

    <a href="https://code.visualstudio.com/Download" target="_blank">VSCode</a>

.. image:: /images/pyintro/vscode.png
    :scale: 50 %
    :alt: VS Code Download Page
    :class: align-center

----

REPL - Shell - Intérprete
=========================

REPL, Shell, Intérprete interactivo o consola de Python son sinónimos.

.. class:: alert alert-info small

    REPL significa Run, Eval, Print, Loop. Es decir, ejecutar, evaluar, imprimir e iterar.

En la consola del sistema operativo, donde tirás los comandos, ejecutá ``python3``. Vas a ver
que cambia el prompt a ``>>>```, eso quiere decir que estás ejecutando Python y que está esperando
que vos le escribas instrucciones para que él las pueda ejecutar.

.. image:: /images/pyintro/repl.png
    :scale: 50 %
    :alt: Ejecutando el REPL
    :class: align-center

Jugando con números
===================

En Python podemos realizar un poco de matemática simple:

.. code-block:: python

    >>> 2 + 2
    4

Como en cualquier lenguaje de programación podemos usar números y hacer cuentas.

.. code-block:: python

    >>> 1.6 + 3.28
    4.88

Se puede sumar, restar, multiplicar y dividir.

.. code-block:: python

    >>> 5 - 1
    4
    >>> 3 * 2
    6
    >>> 8 / 4
    2.0

.. class:: alert alert-info small

    En Python cuando hacés el cociente entre 2 números, siempre te da un número decimal (``float``).

Si querés sólo la parte entera, usá el operador ``//``.

.. code-block:: python

    >>> 8 // 4
    2

Y si querés el módulo (resto), el operador ``%``:

.. code-block:: python

    >>> 3 % 2
    1
    >>> 4 % 2
    0

Incluso podés calcular la potencia de un número. 

.. code-block:: python

    >>> 2 ** 8
    256
    >>> 2 ** 1000
    1071508607186267320948425049060001810561404811705533607443750388370351051124936122493198378815695858127594672917
    5531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267
    398767559165543946077062914571196477686542167660429831652624386837205668069376

Aunque sean muy grandes!

Ahora te toca a vos
-------------------

Jugá un poco con el REPL, ejecutá ``python3`` y usá las preguntas como guía.

Ejercicios:

#. Sumá algunos números, restá otros, y sentite comod@ con el REPL
#. ¿Qué pasa si escribís con espacios entre los números y los operadores?¿Y si no?
#. ¿Probaste usando paréntesis?
#. Jugá un poco con multiplicar, dividir (no te olvides de la división entera).
#. ¿Qué pasa si mezclás números enteros con números decimales?

Extra
~~~~~

#. ¿Qué pasa si intentás poner un texto?

Jugando con Texto
=================

¿Qué pasa si queremos escribir cadenas de texto?

.. code-block:: python

    >>> guido

¡Tenemos un error!

.. code-block:: python

    >>> guido
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    NameError: name 'guido' is not defined

Nos dice que ``guido`` no está definido. Para poder usar texto tenemos que usar comillas.

.. code-block:: python

    >>> 'guido'
    'guido'
    >>> "guido"
    'guido'

.. class:: alert alert-info small

    Podés usar comillas dobles ``"`` o ``'`` simples, pero tenés que ser consistente.

¿Podés sumar números con texto?

.. code-block:: python

    >>> 'Guido' + 2018

¡No! Python no nos deja sumar números con texto. En todo caso deberíamos convertir ese número a texto,
encerrándolo entre comillas.

.. code-block:: python

    >>> 'Guido' + "2018"
    'Guido2018'
    >>> 'Guido ' + "2018"
    'Guido 2018

Ahora te toca a vos
--------------------

Ejercicios:

#. ¿Cuántas cadenas de texto podés concatenar?¿Hay algún límite?
#. Usamos ``+`` para intentar sumar texto con números, intentá con algún otro operador a ver qué pasa.
#. ¿Qué pasa si hacés ``"2" + "3"``?
#. ¿Qué pasa si mezclás ``"`` con ``'``?
#. Y si quiero usar la ``"`` en mi texto, ¿cómo podrías hacer?
#. ¿Se te ocurre cómo hacer un texto multilínea?

Extra
~~~~~

Echale un ojo a la documentación de Python sobre |str_methods| y fijate si encontrás cómo hacer para pasar una cadena
de texto a todas mayúsculas, a todas minúsculas o en formato de título.

.. |str_methods| raw:: html

    <a href="https://docs.python.org/3.6/library/stdtypes.html#string-methods" target="_blank">métodos de cadenas</a>

.. class:: alert alert-success small

    Es lo que se conoce como métodos de cadenas. Por el momento no hace falta saber exactamente cómo es que funciona,
    pero sí es útil saber usarlo. Para eso, agregá al final de la cadena ``.nombre_del_método()`` para cambiar lo que 
    querés cambiar.

Variables
=========

Como en cualquier lenguaje de programación, Python también tiene variables. Para definir una variable
tenemos que ponerle un nombre y asignarle un valor.

.. code-block:: python

    >>> x = 4
    >>> x
    4
    >>> x * 3
    12

Las variables en Python pueden contener cualquier tipo de dato, de hecho, pueden contener cualquier cosa.

.. class:: alert alert-warning small

    Es importante entender que en Python el símbolo ``=`` es el operador de asignación. No es el igual matemático.
    Cuando en matemática decís **x = 2**, estás diciendo que la **x** vale **2** y que el **2** es **x**. Mientras que si escribís en
    Python ``x = 2`` estás diciendo: guardá el valor ``2`` en la variable ``x``. En Python si escribís ``2 = x`` no tiene
    sentido, mientras que en matemática escribir **x = 2** o **2 = x** es lo mismo.

Bien, las variables se pueden usar como cualquier otro valor que vimos hasta ahora.

.. code-block:: python

    >>> alumnos = 36
    >>> profes = 3
    >>> personas = alumnos + profes
    >>> personas
    39

Ahora te toca a vos
--------------------

Ejercicios:

#. Creá una variable ``x`` que contenga un número. Hacé otra variable ``y`` que contenga el cuadrado de el anterior.
#. Mostrá los valores de ``x`` y de ``y``.
#. Creá una variable ``nombre`` que contenga tu nombre.
#. ¿Es posible usar los métodos de las cadenas con las variables? ¿En qué casos?

Extra
~~~~~

¿Qué valor contiene ``z``?

.. code-block:: python

    >>> x = 10
    >>> y = 15
    >>> z = x * y
    >>> z = 100
    >>> z

Formateo de cadenas
====================

¿Qué pasa si querés por ejemplo hacer un mensaje de bienvenida? Por ejemplo, algo que nos sirva para usar en todas
las PyConAR. Podríamos usar una variable que guarde el año y con concatenar lo con ``PyConAR``.

.. code-block:: python

    >>> año = "2018"
    >>> conferencia = "PyConAR"
    >>> 'Qué buena que está la ' + conferencia + " " + año + "!"

Si bien lo podemos hacer de esta manera, resulta un poco compleja de escribir, y hasta de leer. Por suerte Python 
tiene una manera mejor, *f-strings*!.

.. code-block:: python

    >>> año = "2018"
    >>> conferencia = "PyConAR"
    >>> f'Qué buena que está la {conferencia} {año}!'

.. class:: alert alert-warning small

    Las *f-strings* están sólo disponibles para versiones a Python 3.6 o superior. Si tenés Python 3.5 o inferor
    no va a funcionar.

Al incluir una ``f`` al comienzo de la cadena, convertimos una simple cadena de texto en una poderosa *f-string*.
Esta nos permite insertar variables (y expresiones) dentro de ``{}`` y la *f-string* va a evaluar y mostrar el texto
con el contenido. 
**Además es mucho más fácil de leer!**

----

Scripts
=======

Jugar con el REPL es muy divertido y útil, pero no nos sirve para hacer programas completos. ¡Ojo! No te confundas,
vas a usar un montón el REPL en tu día a día, pero más que nada para hacer pruebas cortas y para exploración. 
Vamos a armar programas en Python!

Programas sencillos
--------------------

Un *programa* es un archivo que contiene código fuente, es decir, instrucciones. En nuestro caso, serán instrucciones
de Python. A los programas sencillos se los suele llamar "Scripts". Nuestros primeros programas van a ser programas
de línea de comandos. Es decir, programas que son para ejecutarse en la consola del sistema operativo.

.. class:: alert alert-success small

    Haciendo click en "Código fuente" podés descarte el archivo por si no lo tenés en tu máquina.

.. listing:: pyintro/saludo.py python3

Y si lo queremos ejecutar, entonces hacemos:

.. code-block:: console

    $ python3 saludo.py
    $

¿Qué pasó? ¡Nada! Porque lo que tenemos en el archivo ``saludo.py`` es una cadena de texto que no se está imprimiendo.
Es diferente a lo que pasa en el REPL (recuerden la P). Cuando usamos el shell de Python (REPL), éste se ocupa de
mostrarnos esos valores. Pero cuando estamos escribiendo un programa nosotros tenemos que decirle qué queremos imprimir.
Para ello vamos a usar la función ``print()``.

Modifiquemos el archivo para que quede de la siguiente manera:

.. code-block:: python3

    print("Hola amigues!")

Y volvamos a ejecutar!

.. code-block:: console

    $ python3 saludo.py
    Hola amigues!
    $

¡Ahora si! Lo hicimos.

Ahora te toca a vos
--------------------

Ejercicios:

.. listing:: pyintro/rand.py python3

.. listing:: pyintro/pausa.py python3


#. Copiá el archivo ``rand.py`` a un nuevo archivo que se llame ``números.py`` y hacé que se cree una variable ``x`` y que se muestre su valor. Ejecutá el programa varias veces para ver cómo ``x`` cambia de valor.
#. Copiá el archivo ``pausa.py`` a un nuevo archivo que se llame ``meditar.py`` que sirva para ayudar a los usuarios a realizar 6.5 respiraciones por minuto imprimiendo "Inspira", esperando un tiempo y luego imprimiendo "Expira". El programa debe durar 2 minutos ejecutándose.
#. Copiá el archivo ``rand.py`` a un nuevo archivo que se llame ``dados.py`` y hacé que imprima un valor aleatorio del 1 al 6.

Entrada del usuario
===================

Ahora vamos a jugar un poco con que el usuario de nuestro programa nos ingrese valores. Para esto en Python existe la
función ``input()``. Esta función nos permite pedirle al usuario algún tipo de dato. Ahora podemos hacer nuestro programa
un poco más interactivo. *Más divertido!*

Un ejemplo rápido:

.. code-block:: python3

    nombre = input('Hola manola! Decime cuál es tu nombre:')
    print(f'¿Cómo dice que le va {nombre}?')

Si esto lo guardamos en un archivo y lo ejecutamos.

.. code-block:: console

    $ python3 saludar.py
    Hola manola! Decime cuál es tu nombre:Leandro
    ¿Cómo dice que le va Leandro?

Se ve un poco feo porque ``input()`` nos muestra el mensaje tal cual lo escribimos. Mejoremos un poco la UX de nuestro
programa agregando el espacio luego de los 2 puntos y volvamos a probar.

.. code-block:: python3

    nombre = input('Hola manola! Decime cuál es tu nombre: ')
    print(f'¿Cómo dice que le va {nombre}?')

Si esto lo guardamos en un archivo y lo ejecutamos.

.. code-block:: console

    $ python3 saludar.py
    Hola manola! Decime cuál es tu nombre: Leandro
    ¿Cómo dice que le va Leandro?

**¡Un lujo!** Silicon Valley, allá vamos!

Probemos algo un poco más interesante. Intentemos hacer una programa que sume 2 números. Creemos un archivo
que se llame ``sumar.py`` con el siguiente contenido:

.. code-block:: python

    numero1 = input('¿Cuál es el primer número? ')
    numero2 = input('¿y el segundo? ')

    resultado = numero1 + numero2

    print(f'La suma de ambos número es {resultado}')

.. code-block:: console

    $ python3 sumar.py
    ¿Cuál es el primer número? 3
    ¿y el segundo? 7
    La suma de ambos número es 37

Ups! Algo no salió como esperábamos... ¿Qué pasó?


Bueno, si recordamos cuando eramos unos neófitos en Python y jugábamos con el REPL, cuando sumábamos 2 números
nos daba el resultado correcto. Ahora cuando aplicábamos el operador ``+`` entre cadenas (strings) éstas se 
concatenaban. Parece ser lo que está sucediendo acá.

Podemos usar la función ``type()`` que nos devuelve qué tipo de objeto es lo que le pasamos como argumento.
Modifiquemos ``sumar.py`` para que nos muestre qué es lo que tenemos en ``numero1`` y en ``numero2``.

.. code-block:: python

    numero1 = input('¿Cuál es el primer número? ')
    numero2 = input('¿y el segundo? ')

    print(type(numero1))
    print(type(numero2))

.. code-block:: console

    $ python3 sumar.py
    ¿Cuál es el primer número? 3
    ¿y el segundo? 7
    <class 'str'>
    <class 'str'>

¡Ajá! Son *strings*. Los datos que ingresás usando la función ``input()`` son siempre Strings. Los podemos convertir
a números enteros con ``int()`` o a números con coma con ``float()``.
Modifiquemos ``sumar.py`` a ver qué pasa.

.. code-block:: python

    numero1 = input('¿Cuál es el primer número? ')
    numero2 = input('¿y el segundo? ')

    resultado = float(numero1) + float(numero2)

    print(f'La suma de ambos número es {resultado}')

.. code-block:: console

    $ python3 sumar.py
    ¿Cuál es el primer número? 3
    ¿y el segundo? 7
    La suma de ambos número es 10.0

¡Genial! Ahora sí. Nuestro sueño de Silicon Valley sigue intacto... xD

.. class:: alert alert-info small

    La función ``float()`` la podríamos haber puesto también mientras asignámos el ``input()`` a la variable.
    Por ejemplo: numero1 = float(input('¿Cuál es el primer número? '))

Ahora te toca a vos
-------------------

Ejercicios:

#. Hacé un programa que le pida al usuario 2 números e imprima su diferencia.
#. Hacé un programa que le pida al usuario un precio final y le muestre al usuario el valor neto y el IVA.
#. Hacé un programa que le pida al usuario un precio y calcule el precio final con IVA.
#. Hacé un programa que le pida al usuario al menos 1 sustantivo, 1 verbo y 1 adjetivo y construya una oración con eso.
#. Hacé un programa que le pida al usuario la cotización del dólar y un precio en dólares y devuelva el precio en ARS.

Condicionales
=============

Cuando programamos generalmente necesitamos hacer preguntas cerradas para determinar qué hacer después en nuestro programa.
Cómo cuando pensás qué hacer en la vida misma. ¿Ya cobramos el sueldo? Sí. ¿Llegamos a la esquina y tengo que esperar a
que corte el semáforo para cruzar? Si. ¿Tengo que aprender Python? ¡Sí!

Veamos entonces cómo podemos hacer esto en nuestro programas.

Booleanos
---------

Cuando tenés valores como 1 o 0, Verdadero o Falso, Si o No, se llaman *Booleanos*. 

.. |boole| raw:: html

    <a href="https://es.wikipedia.org/wiki/George_Boole" target="_blank">George Boole</a>


.. class:: alert alert-success small

    Los valores booleanos llevan su nombre en honor a |boole| quién desarrolló un sistema de reglas para trabajar
    con este tipo de valores.

Python tiene esos valores representados en ``True`` y en ``False``. Y tiene diferentes operadores que devuelven
valores booleanos. Como por ejemplo ``==`` o ``!=`` que son operadores relacionales y sirven para comparar si ambos
valores a los lados del operador son iguales o no respectivamente.

.. code-block:: python3

    >>> 1 == 0
    False
    >>> 1 == 1
    True
    >>> 1 != 0
    True

.. class:: alert alert-info small

    Notar que en ``True`` la ``T`` es mayúscula y en ``False`` la ``F`` es mayúscula.

También tenemos otros operadores relacionales como mayor (``>``), mayor o igual (``>=``), menor (``<``) y menor o igual (``<=``).

.. code-block:: python3

    >>> 1 > 0
    True
    >>> 3 >= 1
    True
    >>> -1 < -5
    False
    >>> 3 * 2 <= 10
    True

Con los números es muy fácil entender cómo funciona. Pero, ¿qué pasa si intentamos con *strings*?

.. code-block:: python3

    >>> 'a' < 'b'

Es ``True``! Porque ``a`` viene antes que ``b`` alfabéticamente entonces se considera "menor". Las comparaciones
sirver tanto para números como para cadenas y para otros tipos de objetos que aún no conocemos.

.. code-block:: python3

    >>> "a" == "A"
    False
    >>> "a" == "a"
    True>>> "a" < "b"
    True
    >>> "apple" < "animal"
    False

Y, ¿qué pasa en este caso?

.. code-block:: python3

    >>> "Z" < "a"

También es ``True``! Porque aunque todos sabemos que ``Z`` viene después que la ``a`` en el alfabeto, Python
utiliza una codificación y "convierte" esas letras en números. En esa "conversión" las mayúsuculas están antes
que las minúsculas. Incluso tampoco están las letrs acentuadas. Las codificación es ASCII.

Python cuenta además con otros operadores que nos devuelven valores booleanos: ``in`` es uno de ellos y sirve para
determinar si un objeto "está" dentro de otro. Por ejemplo:

.. code-block:: python3

    >>> "H" in "¡Hola!"
    True
    >>> "x" in "¡Hola!"
    False

Se puede usar ``not in`` para determinar si no está:

.. code-block:: python3

    >>> "H" not in "¡Hola!"
    False
    >>> "x" not in "¡Hola!"
    True

Operadores lógicos
------------------

Así como con los números se pueden realizar operaciones aritméticas, con operadores booleanos se pueden
realizar operaciones lógicas. Las básicas son 3: *suma lógica*, *producto lógico* y *negación*. En Python
estos operadores son ``or``, ``and`` y ``not`` respectivamente.

Si bien estos operadores tienen su lógica, la explicación de ésta escapa el objetivo del taller. Por que
sólo nos vamos a limitar a recordar cómo es que funcionan.

Negación
~~~~~~~~

Es el más simple de los operadores lógicos. Es un operador unario, ya que sólo necesitamos de un valor
booleano para obtener el resultado. Y básicamente lo que hace es devolver el resultado opuesto. Es decir,
si le damos ``True`` devuelve ``False`` y viceversa.

.. code-block:: python3

    >>> not True
    False
    >>> not False
    True

Suma lógica
~~~~~~~~~~~

Éste es un operador binario, es decir, necesita dos valores, uno a cada lado, como los operadores aritméticos.
Y devuelve ``False`` sí y sólo si ambos operadores son ``False``. Como tenemos 2 valores posibles a cada lado
del operador, entonces tenemos 4 resultados posibles:

.. code-block:: python3

    >>> True or True
    True
    >>> True or False
    True
    >>> False or True
    True
    >>> False or False
    False

Producto lógico
~~~~~~~~~~~~~~~

Análogo al anterior con la diferencia que nos devuelve ``True`` si y sólo si ambos operandos son ``True``.

.. code-block:: python3

    >>> True and True
    True
    >>> True and False
    False
    >>> False and True
    False
    >>> False and False
    False

Expresiones condicionales
-------------------------

Podemos usar ``if`` para evaluar una expresión booleana y actuar según el valor de la respuesta de ese
valor booleano. Por ejemplo:

.. code-block:: python3

    >>> año = 2018
    >>> if año == 2018:
    ...     print('Genial. Un gran año para aprender Python.')
    ... 
    Genial. Un gran año para aprender Python.

.. class:: alert alert-info small

    Habrás notado que escribimos el ``print`` con una sangría. Eso lo solemos llamar *indentación*.
    En Python la indentación es **súper** importante. Es lo que usa internamente Python para identificar
    los bloques de sentencias. Fijate que después de la instrucción ``print`` dejamos una línea en blanco
    para indicarle al REPL que nuestro bloque de sentencias terminó. Así sabe que lo puede ejecutar.
    Si queremos escribir sentencias que estén fuera del bloque lo que hacemos es "romper" esa *indentación*
    escribiendo sin la sangría que insertamos anteriormente.

También podemos agregar una sección ``else`` para ejecutar código cuando la expresión booleana se evalúa
como ``False``.

.. code-block:: python3

    >>> año = 2017
    >>> if año == 2018:
    ...     print('¡Genial! Un gran año para aprender Python.')
    ... else:
    ...     print('Uf... me perdí la PyConAR, a esperar...')
    Uf... me perdí la PyConAR, a esperar...

Ahora te toca a vos
-------------------

#. Escribí un programa que pida al usuario la temperatura que hay en el ambiente y según tu criterio le imprima si hace calor o hace frío.
#. **Bonus**: modificá el programa anterior para que si la temperatura es menor a 0 diga: "Me congelo!"
#. Escribí un programa que sirva para jugar "Piedra, Papel o Tijera". Pida al usuario lo que hizo cada jugador y determine quién ganó.
#. Hacé un programa ``adivina_numero.py`` que genere un número al azar de 1 a 10 y le pida al usuario que adivine el número. Si el usuario adivinó, que le muestre un mensaje de felicitaciones.
#. Escribí un programa que le pida al usuario una frase y luego una palabra. Que el programa informe si la palabra ingresada está en la frase.
#. Hacé un programa que reciba una fecha de nacimiento e imprima algunas fechas importantes que tengan en el futuro: mayor de edad, 30 años, 50 años, 65 años y 90 años.

.. |datetime| raw:: html

    <a href="https://docs.python.org/3/library/datetime.html#datetime.datetime" target="_blank">datetime</a>


.. class:: alert alert-info small

    Podés ayudarte leyendo la documentación sobre |datetime|.

Listas
======

¿Quién no hace listas para su día a día? Por ejemplo, yo a la mañana suelo hacer una lista de las cosas
que tengo que hacer en el día. Todo el tiempo necesitamos de listas. En Python las listas son colecciones
de datos ordenados. Para definir una lista en Python necesitamos una variable y ponemos los valores que
debe contener la lista entre corchetes.

.. code-block:: python3

    >>> adjetivos_pyconar = ['genial', 'fantástica', 'impresionante', 'fabulantástica']
    >>> adjetivos_pyconar
    ['genial', 'fantástica', 'impresionante', 'fabulantástica']

Las listas pueden contener cualquier tipo de objeto que hay en Python, incluso otras listas.

.. code-block:: python3

    >>> cosas = [5, True, 'Hola', adjetivos_pyconar]
    >>> adjetivos_pyconar
    [5, True, 'Hola', ['genial', 'fantástica', 'impresionante', 'fabulantástica']]

Como con cualquier otro tipo de objeto en Python podemos usar ``type``:

.. code-block:: python3

    >>> type(adjetivos_pyconar)
    <class 'list'>

Y podemos usar también el operador ``in`` para saber si un objeto está en la lista:

.. code-block:: python3

    >>> False in cosas
    False
    >>> 5 in cosas
    True

Ahora te toca a vos
--------------------

Ejercicios:

#. Creá un programa ``evento.py`` que tenga una lista de nombres y le pida al usuario su nombre. Si el nombre ingresado está en la lista que le imprima un mensaje de bienvenida, sino que le informque que no está en la lista de invitados.
#. Escribí un programa ``amigo.py`` que contenga 2 listas de emociones y le pregunte al usuario cómo está. Según lo que responda el usuario, si está en alguna de esas listas responda apropiadamente. Si no está en ninguna lista que imprima, "No sé como entenderte". Si el usuario ingresa "Cómo estás vos?" (en mayúsculas y/o minúsculas) que responda aleatoriamente con algun valor de las listas de emociones.
#. Acabás de adquirir una compañía de tecnología "Bitson SA". Hacé un programa que contenga una lista con ``tus_propiedades`` que contenga tus objetos y una lista con las propiedades de ``bitson_propiedades`` que tiene los bienes de la compañía. Hacé que el programa presente una nueva lista con todos esos elementos combinados. *Ojo*: que no sea una lista de 2 listas, sino una única lista con los objetos de esas listas.
#. Mejorá el programa anterior de "Piedra, papel o tijera" haciéndolo interactivo. Que el programa le pida al usuario su movimiento y luego la computadora debe elegir un movimiento aleatorio e informar si ganó el usuario o la computadora.
#. Creá un programa que se llame ``bola_8_magica.py`` que acepte preguntas del usuario y aleatoriamente conteste "sí", "no" o "puede ser".
#. Hacé un programa ``ayudante_cocina.py``. Tiene que tener una lista de contenidos que puede tener un sandwich (proteinas, vegetales, fiambres, tipo de pan, etc...). Cuando se ejecuta el programa éste imprime por pantalla un elemento de cada lista para que el ayudante de cocina pueda armar el sandwich.

.. code-block:: console

    $ python3 ayudante_cocina.py
    lomito
    queso brie
    mayonesa
    tomate
    pan integral

.. |random_choice| raw:: html

    <a href="https://docs.python.org/3/library/random.html?highlight=random#random.choice" target="_blank">random</a>


.. class:: alert alert-info small

    Podés usar ``random.choice()`` para la selección. Leelo en la documentación de |random_choice|.

Más listas
===========

Obteniendo objetos de la lista
-------------------------------

Como mencionamos anteriormente las listas son colecciones ordenadas de objetos. Es decir, su contenido tiene
un orden. Es decir, podemos ubicar a las cosas en la lista por el lugar que ocupan en ella. Esa posición
en general se la conoce como índice. Para poder acceder a los elementos de una lista, necesitás tener 
presente 2 cosas:

1. Las listas empiezan en ``0``, no en ``1``.
2. Obtenemos el objeto con el nombre de la lista y usando los ``[]``.

Por ejemplo, si queremos obtener ``"genial"`` de la lista ``adjetivos_pyconar``:

.. code-block:: python3

    >>> adjetivos_pyconar = ['genial', 'fantástica', 'impresionante', 'fabulantástica']
    >>> adjetivos_pyconar[0]
    'genial'

¡Genial! También podés obtener un rango de la lista. Por ejemplo:

.. code-block:: python3

    >>> adjetivos_pyconar[1:2]
    ['fantástica']

Pará, pará, pará! Le pedimos a la lista que nos dé las cosas desde el 1 al 2 y sólo nos mostró ``'fantástica'``.

Esto es porque cuando usamos esta sintáxis de "rebanado" o *slicing* nos trae desde el valor que indicamos inicialmente
hasta el que indicamos como final no incluyendo éste último.

¿Y si tenemos una lista dentro de otra lista? ¿Cómo accedemos a elementos de esa otra lista? Recuerden nuestra
lista de ``cosas``, si queremos obtener ``'impresionante'``:

.. code-block:: python3

    >>> cosas
    [5, True, 'Hola', ['genial', 'fantástica', 'impresionante', 'fabulantástica']]
    >>> cosas[3][2]
    'impresionante'

¡Fabulantástico!

Modificando la lista
---------------------

Puedo agregar elementos a una lista con ``.append()`` pasándole como argumento el elemento a agregar. Por ejemplo:

.. code-block:: python3

    >>> adjetivos_pyconar.append('espectacular')
    >>> adjetivos_pyconar
    ['genial', 'fantástica', 'impresionante', 'fabulantástica', 'espectacular']

Se puede modificar un elemento de una lista asignando un nuevo valor a ese elemento.

.. code-block:: python3

    >>> adjetivos_pyconar[3] = 'fabulosa'
    >>> adjetivos_pyconar
    ['genial', 'fantástica', 'impresionante', 'fabulosa', 'espectacular']

También se pueden sacar elementos de una lista. Podemos usar ``.remove()`` que hay que pasarle el elemento 
que queremos borrar:

.. code-block:: python3

    >>> adjetivos_pyconar.remove('impresionante')
    >>> adjetivos_pyconar
    ['genial', 'fantástica', 'fabulantástica', 'espectacular']

O podemos usar ``.pop()`` que saca el último elemento de la lista:

.. code-block:: python3

    >>> adjetivos_pyconar.pop()
    'espectacular'
    >>> adjetivos_pyconar
    ['genial', 'fantástica', 'fabulantástica']

Que también admite que le pasemo un índice:

.. code-block:: python3

    >>> adjetivos_pyconar.pop(1)
    'fantástica'
    >>> adjetivos_pyconar
    ['genial', 'fabulantástica']

Ahora te toca a vos
-------------------

Ejercicios:

.. listing:: pyintro/capitales.py python3

#. Creá un programa que te ayude a planear tus próximas 5 vacaciones. El programa debe pedir 5 destinos. Luego debe elegir uno de esos aleatoriamente elige aleatoriamente también una cantidad de días e imprime el resultado de las 5 vacaciones. No se deben repetir los destinos.
#. Copiá el contenido de ``capitales.py`` y creá el archivo ``adivina_capital.py``. En este nuevo archivo creá un programa que elija aleatoriamente una provincia y le pida al usuario que escriba la capital. Si el usuario acertó, que el programa lo felicite. Sino le agradezca por intentarlo.
#. Mejorá el programa ``ayudante_cocina.py``. Creá una lista de nombres *copados* para tus sandwiches y hacé que el programa te imprima el menú de los sándwiches con esos ingredientes.

.. class:: alert alert-success small

    Si no hiciste el programa anterior, podés usar estas listas:

    .. code-block:: python3

        proteinas = ["jamón", "pollo", "lomito", "lentejas"]
        condimentos = ["mostaza", "ketchup", "hummus", "barbacoa", "mayonesa"]
        vegetales = ["tomate", "lechuga", "cebolla", "pepino"]
        panes = ["blanco", "lactal", "negro", "integral"]

Ciclos
======

Los ciclos son ideales para esas tareas repetitivas, especialmente cuando tenemos que hacer cosas con todos los
elementos de una lista.

Ciclo For
---------

Si podemos usar un ciclo ``for`` entonces tenemos lo que llamamos en Python como *iterable*. Las listas y las cadenas
de texto son ambos *iterables*.

Hagamos un ciclo para que nos imprima los elementos de una lista:

.. code-block:: python3

    >>> frutas = ['bananas', 'frutillas', 'kiwis', 'peras', 'manzanas']
    >>> for fruta in frutas:
    ...     print(fruta)
    bananas
    frutillas
    kiwis
    peras
    manzanas

En este ciclo ``for`` estamos creando la variable ``fruta`` que sirve para iterar sobre la lista ``frutas``. 
Cada elemento de la lista en cada ciclo estará almacenado en la variable ``fruta``.

.. class:: alert alert-success small

    Podemos usar cualquier nombre para esa variable. En general es una buena práctica ponerle nombre
    descriptivo a las variables. Por eso usamos la palabra ``fruta``. Pero podríamos haber usado cualquier
    otra cosa.

Ahora te toca a vos
-------------------

Ejercicios:

#. Creá una lista de nombres y hacé que salude a cada uno de esas personas.
#. Mejorá ``adivina_numero.py`` haciendo que el usuario sólo pueda intentarlo 3 veces.
#. Creá una copia de ``capitales.py`` y hacé que el programa muestre la lista de capitales con sus respectivas provincias de manera amigable.
#. Hacé un programa ``todo.py``. Creá una lista cosas para hacer y dos listas: ``hacer_ahora`` y ``hacer_despues``. Hacé que aleatoriamente cada uno de los elementos en la lista de pendientes vaya a la lista de ``hacer_ahora`` o de ``hacer_despues``. Mostrá el resultado de manera amigable.

Archivos
========

Vamos a ver cómo hacer para leer archivos. Hasta ahora sólo hemos cargado información a nuestros programas
definiéndola en nuestro código o pidiéndole al usuario con ``input``. Es habitual adquirir información para nuestros
programas desde archivos.

Agarremos cualquier archivo de texto que tengamos en nuestra computadora y copiémoslo en nuestro directorio de trabajo
con el nombre ``lorem.txt``.

.. |lorem| raw:: html

    <a href="https://es.lipsum.com/" target="_blank">Lorem Ipsum</a>


.. class:: alert alert-info small

    Si no encontraste ningún archivo TXT en tu máquina podés ir a |lorem| generar un texto aleatorio y
    usarlo. Esto es muy útil para cuando tenés que hacer pruebas y no tenés datos reales.
    Generalo y guardalo en un archivo de texto ``lorem.txt`` en el directorio que venís trabajando.

.. code-block:: python3

    >>> lorem_file = open('lorem.txt')
    >>> contenido = lorem_file.read()
    >>> print(contenido)
    ... 
    *el contenido del archivo*
    ... 
    >>> lorem_file.close()

Como verán lo primero que hacemos es abrir el archivo. Luego leemos el contenido, ese contenido es un *string*.
Después imprimimos ese contenido para verlo en pantalla y finalmente cerramos el archivo.

Creemos un programa ``lorem_stats.py`` que nos sirva para contar las palabras de nuestro texto.

.. listing:: pyintro/lorem_stats.py python3

.. class:: alert alert-info small

    Si observamos detenidamente estamos usando un método ``.split()`` que lo que hace es separar una cadena de texto
    por los espacios devolviendo una lista con todas las palabras.

    Además estamos usando sobre esa lista la función ``len()`` que devuelve la longitud de la lista.

.. class:: alert alert-warning small

    Si te quedaron dudas, jugá un poco en el REPL con un *string* que contenga 1 o 2 oraciones usando ``.split()`` y 
    ``len()``.

Cerrar archivos
----------------

Siempre necesitamos recordar que es necesario cerrar los archivos. No afecta mucho cuando leemos los archivos,
pero si queremos escribir en ellos, es **súper** importante que no lo olvidemos.
Es útil usar el ``with`` que ayuda a que no nos olvidemos ya que lo hace *automágicamente* para nosotros.

.. listing:: pyintro/lorem_stats_with.py python3

Este bloque ``with`` es lo que se conoce en Python como un `context manager`. Éstos nos permiten establecer
algunas tareas particulares de limpieza. Como en este caso, cerrar el archivo.

.. class:: alert alert-warning small

    No te preocupes por enteder los `context manager` completamente. Por ahora recordemos que siempre que
    usemos un ``open()`` lo vamos a hacer con un ``with``.

Modo de lectura y codificación
-------------------------------

Por defecto cuando usamos ``open()`` si no lo especificamos nos abrirá el archivo en modo *texto* e intentará
decodificar su contenido en *utf-8*. La función ``open()`` acepta estos parámetros como argumento. Si queremos
ser más explícitos:

.. listing:: pyintro/lorem_stats_with_mode.py python3

Escribiendo archivos
---------------------

Si queremos escribir en el archivo, tenemos que cambiar el modo a ``w`` y usar el método ``write()``.

.. code-block:: python3

    >>> with open('prueba.txt', mode='wt', encoding='utf-8') as prueba_file:
    ...     prueba_file.write("Hola mundo!\n")
    ... 
    12

El método ``write()`` de nuestro archivo escribe cada caracter que le pasemos. Luego devuelve la cantidad
de bytes que escribió.

Tomemos un descanso para que puedan ustedes practicar un poco.

Ahora te toca a vos
-------------------

Ejercicios:

#. Crear un programa que sirva para agendar nuestros contactos en un CSV (nombre, mail, celular y twitter). *Ojo*: asegurate de que el programa agregue la información al CSV así vas agregando los datos.
#. Usar el archivo ``capitales.py`` para crear un archivo CSV que contenga las provincias y sus respectivas capitales.
#. Hacer un programa que lea ``contactos.csv`` y lo muestre ordenado alfabéticamente de manera amigable para el usuario.
#. Hacé un programa que le pida al usuario una oración y la guarde en un archivo. *Ojo*: asegurate de que el programa agregue la información al archivo así vas agregando las oraciones.


.. class:: alert alert-info small

    Para agregar en los archivos tenemos que usar el modo ``a``.

.. class:: alert alert-info small

    Para ordenar en Python se puede usar la función ``sorted()``.

.. code-block:: console

    $ python3 contactos.py
    Nombre: Leo
    mail: leo@bitson.group
    celular: (11) 3001-5328
    twitter: lecovi

Y la salida debería ser:

.. code-block:: console

    $ cat contactos.csv
    Leo,leo@bitson.group,(11) 3001-5328,lecovi

Rangos
======

Python viene con una función ``range()`` que nos sirve para generar rangos de números:

.. code-block:: python3

    >>> for n in range(0, 5):
    ...     print(n)
    ... 
    0  
    1
    2
    3
    4

.. class:: alert alert-warning small

    Notemos que sucede lo mismo que cuando hacemos *slicing* en una lista. El valor inicial está incluido, pero
    el final no.

Si vamos a arrancar desde 0, podemos omitirlo:

.. code-block:: python3

    >>> for n in range(5):
    ...     print(n)
    ... 
    0  
    1
    2
    3
    4

Y podemos incluir un tercer argumento que es el paso o salto que va a dar. Por ejemplo, de a decenas:


.. code-block:: python3

    >>> for n in range(0, 100, 10):
    ...     print(n)
    ... 
    0
    10
    20
    30
    40
    50
    60
    70
    80
    90

Ahora te toca a vos
--------------------

Ejercicios:

#. Mejoremos el ``meditar.py``. Haciendo que después de cada exhalación nos pida escribir lo que estamos pensando. Al finalizar el programa que nos muestre qué pensamos en la meditación.
#. Rehacé tu programa ``adivina_numero`` para que use un rango.

Funciones
=========

En Python como en todos los lenguajes de programación podemos crear nuestras propias funciones.
¿Qué son las funciones? Son grupos de sentencias de código que se asocian a un nombre. Hemos estado usando varias
de las que vienen con Python: ``print()``, ``type()``, ``len()``...

.. class:: alert alert-info small

    Como regla general podemos pensar que todo lo que sea un ``nombre`` con `()` es una función.

Si queremos definir nuestras propias funciones usamos la palabra reservada ``def``:

.. code-block:: python3

    >>> def mi_funcion_de_prueba(nombre):
    ...     print('Hola {nombre}')
    ...     edad = int(input('Ingrese su edad: '))
    ...     if edad >= 18:
    ...         print('Ya podemos ir a tomar unas cervezas...')
    ...     else:
    ...         print('Tomamos un juguito?')
    ... 
    >>> mi_funcion_de_prueba('Leo')
    Hola Leo
    Ingrese su edad: 37
    Ya podemos ir a tomar unas cervezas...
    >>>

Ahora te toca a vos
-------------------

Ejercicios:

#. Escribir una función que permita calcular la duración en segundos de un intervalo dado en horas, minutos y segundos.
#. Escribir una función que permita calcular la duración en horas, minutos y segundos de un intervalo dado en segundos.
#. Escribir una función que reciba un precio final y devuelva el valor neto y el IVA
#. Escribir una función que reciba un precio y devuelva el valor final con el IVA. **Bonus**: mejorar la función que acepte un argumento que sea la alícuota de IVA, si no es ingresada que tome 21% por defecto.

Diccionarios
============

Los diccionarios son colecciones no ordenadas de conjuntos claves-valor. Como cuando buscamos una palabra en el
diccionario español. La palabra buscada sería la *clave* y el significado el *valor*.

.. code-block:: python3

    >>> meses = {'Enero': 31, 'Febrero': 28, 'Marzo': 31}
    >>> meses
    {'Enero': 31, 'Febrero': 28, 'Marzo': 31}
    >>> type(meses)
    <class 'dict'>
    >>> meses['Enero']
    31
    >>> meses['Febrero'] = 29
    >>> meses
    {'Enero': 31, 'Febrero': 29, 'Marzo': 31}
    >>> meses['Abril'] = 30
    >>> meses
    {'Enero': 31, 'Febrero': 29, 'Marzo': 31, 'Abril': 30}

Como verán es muy sencillo crear diccionarios. Sólo necesitamos escribir entre ``{}`` los conjuntos de claves-valor
separados por ``,`` y las claves están separadas por ``:`` de los valores. Por lo general para las claves
se utilizan *strings*.

Para agregar nuevas claves al diccionario, sólo tenemos que llamar al diccionario existente y entre ``[]`` escribimos
la nueva clave y le asignamos el valor correspondiente.
En el caso de que la clave exista previamente, el valor se actualizará.

Si queremos borrar elementos del diccionario, usamos ``del``:

.. code-block:: python3

    >>> del meses['Febrero']
    >>> meses
    {'Enero': 31, 'Marzo': 31, 'Abril': 30}

Ahora si intentamos acceder a esa clave:

.. code-block:: python3

    >>> meses['Febrero']
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    KeyError: 'Febrero'

Podemos iterar sobre el diccionario y nos devolverá las claves:

.. code-block:: python3

    >>> for mes in meses:
    ...     print(mes)
    Enero
    Marzo
    Abril

Si queremos obtener los valores claves valor, podemos iterar con el método ``.items()``:

.. code-block:: python3

    >>> for mes, días in meses.items():
    ...     print(f'{mes} tiene {días} días')
    Enero tiene 31 días
    Marzo tiene 31 días
    Abril tiene 30 días

Si usamos el operador ``in`` en un diccionario buscará en las claves. 

.. code-block:: python3

    >>> 'Enero' in meses
    True
    >>> 'Febrero' in meses
    False

Ahora te toca a vos
--------------------

Ejercicios:

.. |rpssl| raw:: html

    <a href="http://www.samkass.com/theories/RPSSL.html" target="_blank">Rock, Paper, Scissors, Spock, Lizard</a>

#. Pensando en la experiencia que hicimos creando "Piedra, Papel o Tijera" creemos ``rpssl.py`` para jugar |rpssl| usando un diccionario para determinar el ganador.
    #. Hacer que la computadora elija un movimiento.
    #. Pedirle al usuario que elija un movimiento.
    #. Informar el ganador.
#. Contemplar que el usuario pueda ingresar en mayúscula y/o minúsculas y que esto no afecte el funcionamiento.
#. Mejorar el programa para que maneje los ingresos erróneos por parte del usuario.


Para seguir aprendiendo
=======================

Andá a la sección de `recursos </resources/#id4>`_.

