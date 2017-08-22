.. title: Programación Estructurada
.. slug: ifts/par/prog-estructurada
.. date: 2015-08-26 15:18:41 UTC-03:00
.. tags:
.. category:
.. link:
.. description:
.. type: text

.. class:: alert alert-info pull-right

.. contents::

Hasta el momento hemos trabajado con **Python** bajo el paradigma de programación que se conoce como 
**Programación Estructurada**. Es decir, hemos estado utilizando en nuestros programas sólo tres estructuras:

- Secuencia
- Condicionales
- Iteraciones

Los conceptos que vamos a trabajar a lo largo de la cursada nos ayudarán a comprender el paradigma de *Programación
orientada a objetos*.

Paradigmas de Programación
==========================

Un **Paradigma de programación** es un conjunto de reglas, métodos, propuestas... básicamente una forma de modelar
la realidad para poder implementar soluciones a los problemas computacionales que se presetan. Un **paradigma**
representa un enfoque de cómo entender el problema en cuestión. Se puede entender que un **paradigma** es el lente
que nos colocamos para observar la realidad que nos rodea.

Existen varios paradigmas de programación, entre los más conocidos podemos mencionar:

- Programación estructurada
- Programación orientada a objetos
- Programación funcional
- Programación declarativa

Los lenguajes y los paradigmas de programación
----------------------------------------------

En general los lenguajes de programación van a implemetar algún paradigma. En particular cuando hablamos de *Python*
decimos que es multiparadigma ya que soporta la utilización de varios paradigmas, aunque lo mejor de todo es que no
te obliga a utilizar un único paradigma.

Muchas veces tendemos a asociar los paradigmas de programación a un lenguaje. Pero eso se debe a que son populares
en la implementación de dicho paradigma. Aunque la idea de paradigma es un tanto más amplia que el lenguaje con el
que se trabaja. Es un concepto complejo de explicar y que lleva varios años comprender la diferencia entre los distintos
paradigmas, sus ventajas y desventajas.

Ningún paradigma es una *bala de plata*, todos sirven para una (o muchas) situación en particular, pero siempre habrá
casos donde convendrá utilizar otro enfoque. Por eso tampoco hay que convertirse en un fundamentalista del paradigma
en el que estás trabajando, ya que eso te imposibilitaría la oportunidad de resolver un problema de una mejor manera.


Archivos
========

Un archivo es un conjunto de *bytes* que está almacenado en un dispositivo. Se los identifica por un nombre único
dentro del *filesystem* (sistema de archivos). El nombre de un archivo, también llamado ruta o *path*, está compuesto
por la ubicación del archivo, un nombre y generalmente una extensíón. 

Si tenemos un archivo llamado ``despacito.mp3`` dentro de la carpeta ``Música`` en nuestro sistema GNU/Linux la ruta
del mismo será, por ejemplo:

``/home/usuario/Música/despacito.mp3``

Donde podemos identificar que ``/home/usuario/Música/`` es la carpeta donde está almacenado el archivo, ``despacito``
es el nombre y ``mp3`` es la extensión del archivo. La extensión del archivo nos permite clasificar a los mismos según
su contenido y nos permite asociar las aplicaciones que serán capaces de interpretar correctamente la información que
estos almacenan.

Tipos de archivos
-----------------

Como mencionamos anteriormente los archivos son conjuntos de *bytes*. Ya sabemos que todo lo que la computadora puede 
almacenar son *bytes*, es decir, conjuntos de ``1`` y ``0``. Si bien toda la información que tenemos en la máquina es
binaria, algunos archivos están codificados de manera que todos los *bytes* que contienen pueden ser interpretados como
caracteres de texto. Es por eso que diremos que esos archivos son **archivos de texto**, mientras que al resto de los
archivos los llamaremos simplemente **archivos binarios**.

Manejo de archivos con Python
-----------------------------

Supongamos que tenemos un archivo con los nombres de diferentes usuarios y queremos abrirlo y procesarlo con Python.
Para ello tendremos que abrir el archivo e ir leyendo la información del mismo, línea por línea.

.. listing:: par/usuarios.txt text

Python nos provee de la función ``open`` que espera como argumento el *path* del archivo que se quiere abrir. Cuando 
abrimos un archivo nos devuelve un objeto ``_io.TextIOWrapper`` este tiene varios métodos para procesar
la información dentro del archivo, en particular el método ``readline`` que leerá la información hasta que encuentre 
un salto de línea, es decir el caracter ``\n``. Cuando se leyó todo el archivo, el método ``readline`` devuelve el 
string vacío ``''``.
No hay que olvidar de cerrar el archivo luego de procesarlo para evitar corromper la información que hay dentro. Para
eso hay que usar el método ``close``. 

.. code-block:: ipython

    In [1]: archivo = open('usuarios.txt')

    In [2]: type(archivo)
    Out[2]: _io.TextIOWrapper

    In [3]: archivo.readline()
    Out[3]: 'juan\n'

    In [4]: archivo.readline()
    Out[4]: 'pedro\n'

    ...

    In [13]: archivo.readline()
    Out[13]: ''

    In [14]: archivo.close()


Sabiendo que ``readline`` lee las líneas del archivo y devuelve una línea vacía cuando ya no hay más, podríamos
generar un ciclo para leer todo el archivo e ir imprimiendo la información en la pantalla.

.. listing:: par/archivo1.py python3

Podemos obtener el mismo resultado con un ciclo ``for`` con la ventaja que **Python** ya sabe cómo tiene que iterar 
sobre un objeto archivo y para cada ciclo nos devolverá una línea del archivo.

.. listing:: par/archivo2.py python3

También nos provee de una sintaxis mucho más limpia utilizando el bloque ``with`` que además se ocupa de cerrar el
archivo cuando se sale del bloque.

.. listing:: par/archivo3.py python3


Modo de apertura
~~~~~~~~~~~~~~~~

La función ``open`` recibe un parámetro opcional el modo en que se abrirá el archivo. 
Hay tres modos de apertura que se pueden especificar:

- **Sólo lectura** (``'r'``). En este caso no es posible realizar modificaciones, solamente leer su contenido.
- **Sólo escritura** (``'w'``). En este caso el archivo es truncado (vaciado) si existe, y se lo crea si no existe.
- **Agregando** (``'a'``). En este caso se crea el archivo, si no existe, pero en caso de que exista se posiciona al final, manteniendo el contenido original.


Además, en cualquiera de estos modos se puede agregar un ``+`` para pasar a un modo
lectura-escritura. El comportamiento de ``r+`` y de ``w+`` no es el mismo, ya que en el primer caso se
tiene el archivo completo, y en el segundo caso se trunca el archivo, perdiendo así los datos.

.. class:: alert alert-info small

Si un archivo no existe y se lo intenta abrir en modo lectura, se generará un error; en cambio si se lo
abre para escritura, Python se encargará de crear el archivo al momento de abrirlo, ya sea con ``'w'``,
``'a'``, ``'w+'`` o con ``'a+'``).

En caso de que no se especifique el modo, los archivos serán abiertos en modo sólo lectura (``r``). 

Escribiendo archivos
--------------------

Si abrimos el archivo con ``w`` creamos un nuevo archivo con cada ejecución del siguiente programa.

.. listing:: par/archivo4.py python3

Si en cambio lo abrimos con ``a``, vamos a agregar al contenido que ya teníamos.

.. listing:: par/archivo5.py python3

Archivos binarios
-----------------

Si agregamos ``b`` al modificador de apertura el contenido del archivo será leído directamente como
*bytes*. Al abrir así el archivo, en vez de leer línea por línea debemos leer *byte* por *byte*. 
Usaremos dos métodos que nos servirán para controlar el cursor: ``tell`` y ``seek``. El primero nos 
dice en qué posición está ubicado el cursor, mientras que el otro nos permite mover el cursor *n bytes*
como se le pase como argumento.

.. code-block:: ipython

    In [1]: archivo = open('usuarios.txt', 'rb')

    In [2]: archivo.tell()
    Out[2]: 0

    In [3]: archivo.read(5)
    Out[3]: b'juan\n'

    In [4]: archivo.tell()
    Out[4]: 5

    In [5]: archivo.read(5)
    Out[5]: b'pedro'

    In [6]: archivo.tell()
    Out[6]: 10

    In [7]: archivo.read(5)
    Out[7]: b'\nana\n'

    In [8]: archivo.tell()
    Out[8]: 15

    In [9]: archivo.seek(21)
    Out[9]: 21

    In [10]: archivo.tell()
    Out[10]: 21

    In [11]: archivo.read(6)
    Out[11]: b'luc\xc3\xada'

Cabe destacar que la salida de la lectura nos muestra ``b'\nana\n'``, con una ``b`` antes de mostrar
la cadena. Eso quiere decir que nos está mostrando los *bytes*, y la forma de representación de esos
*bytes* es la codificación en UTF-8. Por ejemplo, para la última lectura, la salida es ``b'luc\xc3\xada'``
indicándonos que luego de la ``c`` hay 2 *bytes* representados en hexadecimal ``c3`` y ``ad`` que
representan la ``í``. 

Ejercicios
----------

#. Escribir un programa, llamado ``head.py`` que reciba un archivo y un número N e imprima las primeras N líneas del archivo.
#. Escribir un programa, llamado ``wc.py`` que reciba un archivo, lo procese e imprima por pantalla cuántas líneas, cuantas palabras y cuántos caracteres contiene el archivo.
#. Escribir un programa, llamado ``cp.py``, que copie todo el contenido de un archivo (sea de texto o binario) a otro, de modo que quede exactamente igual. **Nota**: utilizar ``archivo.read(bytes)`` para leer como máximo una cantidad de bytes.

:doc:`Solución <ifts/par/prog-estructurada-solucion>`