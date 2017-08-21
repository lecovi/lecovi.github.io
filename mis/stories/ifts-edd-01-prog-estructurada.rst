.. title: Programación Estructurada
.. slug: ifts/edd/prog-estructurada
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

Concepto de Tipo de Dato Abstracto
----------------------------------

La *abstracción* es el mecanismo que permite seleccionar partes de un todo complejo para su consideración, 
ignorando el resto. Esto nos permite filtrar aquellos aspectos relevantes, y nos permite obtener soluciones 
más generales.

El concepto de *abstracción* nos remite a la posibilidad de considerar la resolución de un problema sin tener
en cuenta los detalles por debajo de cierto nivel.

El concepto de **Tipo de Dato Abstracto** (TDA en castellano, ‘Abstract Data Type’ o ADT en inglés) surgió para
facilitar el trabajo con tipos de datos haciendo abstracción de la implementación de los mismos.
Un TDA está dado por un grupo de datos que cumplen cierta condición especificada, más un conjunto de operaciones
que representan el comportamiento del TDA.

.. sidebar:: En **Python**: *todos somos adultos responsables*

    .. class:: alert alert-info small

    En muchos lenguajes orientado a objetos (C++, Java, C#, etc) se implementa el concepto de privacidad de los
    atributos y métodos. En **Python** todos los atributos y métodos *son públicos*.


La entidad TDA expone sus características por medio de las operaciones. La implementación de la estructura del
TDA, y de las operaciones propias son privadas.
No se permite acceso ni visibilidad a la implementacion de un TDA. Esta parte oculta está constituída por la
maquinaria algorítmica que implementa la semántica de los operadores. De este modo un TDA encapsula ciertos tipos
de datos en cuanto a la definición  del tipo y todas las operaciones del mismo en una sección del código.

Los TDA constituyen una forma de generalización y encapsulamiento de los aspectos más importantes de la
información que se debe manejar en la resolución de un problema, sin considerar las cuestiones relativas a la
implementación.
Un TDA define una nueva clase de concepto que puede manejarse con independencia de la estructura de datos para
representarlo. Es una generalizaciones de los tipos de datos básicos y de las operaciones primitivas.
Es decir:

.. class:: alert alert-success

TDA = Representación (estructuras de datos) + Operaciones (métodos)

Objetos en Python
-----------------

Los *objetos* son una forma de organizar datos y de relacionar esos datos con el código apropiado para manejarlo.
Son los protagonistas de un paradigma de programación llamado *Programación Orientada a Objetos* y son la forma
práctica de trabajar con TAD en Python.

Nosotros ya usamos objetos en Python sin mencionarlo explícitamente. Es más, todos los
tipos de datos que Python nos provee son, en realidad, objetos.

De forma que, cuando utilizamos ``cadena.upper()`` , le estamos diciendo a Python que llame
a la función upper del tipo ``str`` para cadena que es lo mismo que decir que llame al *método* upper
del objeto ``cadena``.
A su vez, a las variables que un objeto contiene se las llama *atributos*.

Nuestros propios objetos
~~~~~~~~~~~~~~~~~~~~~~~~

Para crear nuestros propios objetos en Python se usa la palabra reservada  ``class`` que nos ayuda a definir una
nueva *clase*. Un clase es un nuevo tipo de dato que existe para invocar en nuestro programa. 

.. code-block:: python

    class Billetera:
        pass

Utilizando estas sentencias, tenemos la posibilidad de llamar en nuestro programa a los objetos del tipo ``Billetera``.

.. code-block:: ipython

    In [1]: class Billetera:
    ...:     pass
    ...: 

    In [2]: mi_billetera = Billetera()

    In [3]: mi_billetera
    Out[3]: <__main__.Billetera at 0x7f368cd8f630>

    In [4]: tu_billetera = Billetera()

    In [5]: tu_billetera
    Out[5]: <__main__.Billetera at 0x7f368ce49c88>

Como podemos ver en el código anterior, creamos la clase ``Billetera`` y luego creamos dos *instancias*, ``mi_billetera``
y ``tu_billetera``.

.. code-block:: ipython

    In [6]: mi_billetera.compartimiento_1 = 100

    In [7]: mi_billetera.compartimiento_1
    Out[7]: 100

    In [8]: tu_billetera.compartimiento_1
    ---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)
    <ipython-input-8-1f6438ef5671> in <module>()
    ----> 1 tu_billetera.compartimiento_1

    AttributeError: 'Billetera' object has no attribute 'compartimiento_1'

Dentro de cada instancia podemos crear nuevas variables y asignarles valores. Pero es importante destacar que cuando
hacemos esto, lo estamos hacienod sólo a nivel de cada *instancia*. Para ``mi_billetera`` creamos el ``compartimiento_1``
donde ponemos el valor 100. Si tratamos de acceder a ``compartimiento_1`` pero de ``tu_billetera`` nos saldrá un 
``AttributeError`` ya que el atributo ``compartimiento_1`` sólo existe para ``mi_billetera``.

Si queremos que todos las intancias de la clase ``Billetera`` tengan el ``compartimiento_1``, tenemos que redefinir
la clase. 

.. code-block:: ipython

    In [9]: class Billera:
   ...:     compartimiento_1 = 0
   ...:     

    In [10]: mi_billetera.compartimiento_1
    Out[10]: 100

    In [11]: mi_billetera = Billera()

    In [12]: mi_billetera.compartimiento_1
    Out[12]: 0

    In [13]: tu_billetera = Billera()

    In [14]: tu_billetera.compartimiento_1
    Out[14]: 0

Métodos
-------

.. code-block: ipython

    In [1]: class Alumno:
    ...:     name =  ''
    ...:     age = 0
    ...:     courses = list()
    ...:     

    In [2]: chino = Alumno()

    In [3]: chino.name
    Out[3]: ''

    In [4]: chino.age
    Out[4]: 0

    In [5]: chino.courses
    Out[5]: []

    In [6]: chino.name = 'Victor'

    In [7]: chino.age = 21

    In [8]: chino.courses.append('EDD')

    In [9]: chino.name
    Out[9]: 'Victor'

    In [10]: chino.age
    Out[10]: 21

    In [11]: chino.courses
    Out[11]: ['EDD']

.. sidebar:: ``self``

    .. class:: alert alert-success small

    Todos los métodos de cualquier clase reciben como primer parámetro a la instancia sobre la que está trabajando.
    Por **convención** a ese primer parámetro se lo suele llamar ``self`` (que podríamos traducir como *yo mismo*), 
    pero puede llamarse de cualquier forma.

Si observamos con detenimiento, con esta forma de crear los objetos cada vez que creamos uno, luego tenemos
que ir llamando a cada uno de los atributos para asignarle un valor. Por suerte hay una mejor forma de hacerlo!

Tenemos que usar un método que se llama al crear la instancia. Este método en particular se lo conoce como el
método constructor y en **Python** se llama ``__init__``. Definir un método constructor nos permite crear una 
instancia de un objecto con los parámetros necesarios. Modificando la clase ``Alumno`` con un método constructor
ahora nos obliga a instanciar objetos sólo con los parámetros indicados como obligatorios. En este caso indicamos
los tres parámetros: ``name``, ``age`` y ``courses`` como obligatorios. 

Un **método** es una función de Python que queda **encapsulada** dentro de la clase para la cual está
definiéndose. Es decir, un **método** tiene las mismas reglas de definición que las funciones en python:
nombres, argumentos, valores por defecto y demás... 

.. code-block:: ipython

    In [12]: class Alumno:
        ...:     def __init__(self, name, age, courses):
        ...:         self.name =  name
        ...:         self.age = age
        ...:         self.courses = courses
        ...:     

    In [13]: chino = Alumno()
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-13-c040beabd969> in <module>()
    ----> 1 chino = Alumno()

    TypeError: __init__() missing 3 required positional arguments: 'name', 'age', and 'courses'

    In [14]: chino = Alumno(name='Victor', age=21, courses=['EDD', 'PAR'])

    In [15]: chino.name
    Out[15]: 'Victor'

    In [16]: chino.age
    Out[16]: 21

    In [17]: chino.courses
    Out[17]: ['EDD', 'PAR']

Métodos especiales
~~~~~~~~~~~~~~~~~~

En Python existen una serie de métodos que son un tanto especiales, también llamados métodos mágicos o métodos *dunder*.
El método constructor ``__init__`` es uno de estos métodos mágicos. 

.. class:: alert alert-info

    Se utiliza **dunder** porque son métodos que empiezan con doble guión bajo (double underscore en inglés).
    Como decir *doble guión bajo init doble guión bajo* puede resultar un trabalenguas, se propuso esta nueva
    terminología para identificar a este tipo de métodos.

.. code-block:: ipython

    In [18]: print(chino)
    <__main__.Alumno object at 0x7f7c54949048>

    In [19]: chino
    Out[19]: <__main__.Alumno at 0x7f7c54949048>

Siguiendo con nuestro ejemplo, cuando imprimimos a nuestro querido alumno ``chino`` no nos dice demasiada información
relevante. Lo mismo sucede si consultamos el valor de dicha instancia en el intérprete interactivo. Para modificar el
comportamiento de nuestros objetos cuando se los invoca en la consola de Python tenemos que redefinir el método ``__repr``.
Y para cambiar cómo es que se comporta cuando lo llamemos como argumento de la función ``print`` tenemos que redefinir
el método ``__str__``.

.. code-block:: ipython

    In [20]: class Alumno:
        ...:     def __init__(self, name, age, courses):
        ...:         self.name =  name
        ...:         self.age = age
        ...:         self.courses = courses
        ...:     def __repr__(self):
        ...:         return '<Alumno {}>'.format(self.name)
        ...:     

    In [21]: chino = Alumno(name='Victor', age=21, courses=['EDD', 'PAR'])

    In [22]: chino
    Out[22]: <Alumno Victor>

    In [23]: marce = Alumno(name='Marcela', age=18, courses=['ARQ'])

    In [24]: marce
    Out[24]: <Alumno Marcela>

Ahora modificamos el método ``__repr__`` y podemos observar que cuando consultamos el valor de la instancia
nos devuelve la cadena que nosotros definimos. Hemos modificado la definición de nuestra clase ``Alumno`` y
ahora cuando queremos consultar el valor de nuestras instancias nos devuelve el nombre de la clase seguido
del valor que almacenamos en la variable ``name``.

.. code-block:: ipython

    In [26]: class Alumno:
        ...:     def __init__(self, name, age, courses):
        ...:         self.name =  name
        ...:         self.age = age
        ...:         self.courses = courses
        ...:     def __repr__(self):
        ...:         return '<Alumno {}>'.format(self.name)
        ...:     def __str__(self):
        ...:         return 'Soy el alumno {}, tengo {} años y estoy cursando {}'.format(self.name, self.age, self.courses)
        ...:     

    In [27]: chino = Alumno(name='Victor', age=21, courses=['EDD', 'PAR'])

    In [28]: marce = Alumno(name='Marcela', age=18, courses=['ARQ'])

    In [29]: print(chino)
    Soy el alumno Victor, tengo 21 años y estoy cursando ['EDD', 'PAR']

    In [30]: print(marce)
    Soy el alumno Marcela, tengo 18 años y estoy cursando ['ARQ']

    In [31]: chino
    Out[31]: <Alumno Victor>

    In [32]: marce
    Out[32]: <Alumno Marcela>

En el ejemplo anterior podemos ver cómo hemos incluido la redefinición del método ``__str__`` para
modifcar el comportamiento de nuestros objectos cuando son invocados a través de la función ``print``.

Ejercicios
~~~~~~~~~~

1. Definir una nueva clase ``Carta`` que tenga como atributos el valor y el palo. Utilizar los métodos 
*dunder* para reconocer los diferentes objetos.

2. Definir una nueva clase que sea ``Mascota`` que tenga como atributos el nombre, la edad y qué animal es.
Utilizar los métodos *dunder* para reconocer los diferentes objetos. Crear al menos un nuevo método para
la mascota, como por ejemplo: ``saludar``. 

3. Definir la clase ``Alumno`` que tenga como atributos el nombre y apellido del alumno, la edad y la lista
de materias en las que el alumno está incripto. Definir dos nuevos métodos ``inscribir`` para agregar materias
a la lista de materias del alumno, y ``listar_materias`` para que imprima cada una de las materias en que el 
alumno está inscripto en una materia por línea.

:doc:`Solución <ifts/edd/prog-estructurada-solucion>`
