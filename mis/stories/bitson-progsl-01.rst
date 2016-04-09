.. title: Algunos conceptos básicos
.. slug: bitson/prog-sl/01
.. date: 2015-08-25 13:27:56 UTC-03:00
.. tags: mathjax
.. category:
.. link:
.. description:
.. type: text

.. class:: col-md-2

    .. raw:: html

        <p></p>

.. class:: col-md-8 embed-responsive embed-responsive-16by9

    .. raw:: html

        <iframe class="embed-responsive-item"
        src="http://bitson.github.io/cursos/python1"
        scrolling="no"></iframe>

.. class:: col-md-2

    .. raw:: html

        <p></p>

.. class:: row

.. class:: col-md-12 align-right

    Mirá la |presentation_link|.

    .. |presentation_link| raw:: html

       <a href="http://bitson.github.io/cursos/python1" target="_blank">presentación aparte</a>


.. class:: alert alert-info pull-right

.. contents::

.. class:: col-md-12

En esta unidad hablaremos de lo que es un programa de
computadora e introduciremos unos cuantos conceptos referidos a la
programación y a la ejecución de programas. Utilizaremos en todo
momento el lenguaje de programación Python para ilustrar esos
conceptos.


Computadoras y programas
------------------------

En la actualidad, la mayoría de nosotros utilizamos computadoras
permanentemente: para mandar correos electrónicos, navegar por Internet,
chatear, jugar, escribir textos.

Las computadoras se usan para actividades tan disímiles como predecir las
condiciones meteorológicas de la próxima semana, guardar historias clínicas,
diseñar aviones, llevar la contabilidad de las empresas o controlar una
fábrica. Y lo interesante aquí (y lo que hace apasionante a esta carrera) es
que el mismo aparato sirve para realizar todas estas actividades: uno no
cambia de computadora cuando se cansa de chatear y quiere jugar al solitario.

Muchos definen una computadora moderna como "una máquina que
almacena y manipula información bajo el control de un programa que
puede cambiar". Aparecen acá dos conceptos que son claves: por un
lado se habla de una *máquina* que almacena información, y por
el otro lado, esta máquina está controlada por *un programa
que puede cambiar*.

Una calculadora sencilla, de esas que sólo tienen 10 teclas para
los dígitos, una tecla para cada una de las 4 operaciones, un
signo igual, encendido y CLEAR, también es una máquina que
almacena información y que está controlada por un programa. Pero
lo que diferencia a esta calculadora de una computadora es que en
la calculadora el programa no puede cambiar.

Un *programa de computadora* es un conjunto de *instrucciones* paso a paso que le indican a una computadora cómo
realizar una tarea dada, y en cada momento uno puede elegir
ejecutar un programa de acuerdo a la tarea que quiere realizar.

Las instrucciones se deben escribir en un lenguaje que nuestra
computadora entienda. Los lenguajes de programación son
lenguajes diseñados especialmente para dar
órdenes a una computadora, de manera exacta y no ambigua. Sería
muy agradable poder darle las órdenes a la computadora en
castellano, pero el problema del castellano, y de las lenguas
habladas en general, es su ambigüedad:

Si alguien nos dice *"Comprá el collar sin monedas"*, no sabremos
si nos pide que compremos el collar que no tiene monedas, o que compremos
un collar y que no usemos monedas para la compra. Habrá que preguntarle
a quien nos da la orden cuál es la interpretación correcta. Pero tales
dudas no pueden aparecer cuando se le dan órdenes a una computadora.

Este curso va a tratar precisamente de cómo se escriben programas
para hacer que una computadora realice una determinada tarea.
Vamos a usar un lenguaje específico (Python) porque es sencillo y
elegante, pero éste no será un curso de Python sino un curso de
programación.

.. class:: alert alert-success pull-right

    Existen una gran cantidad de programas desarrollados en Python, desde
    herramientas para servidores, como **mailman**, hasta programas amigables
    para usuarios finales, como **emesene**, pasando por aplicaciones
    empresariales, **openerp**, **tryton**; herramientas de desarrollo,
    **meld**, **mercurial**, **bazaar**, **trac**; plataformas web,
    **django**, **turbogears**, **zope**; clientes de bittorrent, **bittorrent**,
    **bittornado**, **deluge**; montones de juegos de todo
    tipo, y muchísimas aplicaciones más.
    Todas estas aplicaciones son software libre, por lo que se puede obtener y
    estudiar el código con el que están hechas


El mito de la máquina todopoderosa
----------------------------------

Muchas veces la gente se imagina que con la computadora se puede
hacer cualquier cosa, que no hay tareas imposibles de realizar.
Más aún, se imaginan que si bien hubo cosas que eran imposibles de
realizar hace 50 años, ya no lo son más, o no lo serán dentro de
algunos años, cuando las computadoras crezcan en poder (memoria,
velocidad), y la computadora se vuelva una máquina todopoderosa.

Sin embargo eso no es así: existen algunos problemas, llamados
*no computables* que nunca podrán ser resueltos por una
computadora digital, por más poderosa que ésta sea. La
computabilidad es la rama de la computación que se ocupa de
estudiar qué tareas son computables y qué tareas no lo son.

De la mano del mito anterior, viene el mito del lenguaje
todopoderoso: hay problemas que son no computables porque en
realidad se utiliza algún lenguaje que no es el apropiado.

En realidad todas las computadoras pueden resolver los mismos
problemas, y eso es independiente del lenguaje de programación que
se use. Las soluciones a los problemas computables se pueden
escribir en cualquier lenguaje de programación. Eso no significa
que no haya lenguajes más adecuados que otros para la resolución
de determinados problemas, pero la adecuación está relacionada con
temas tales como la elegancia, la velocidad, la facilidad para
describir un problema de manera simple, etc., nunca con la
capacidad de resolución.

Los problemas no computables no son los únicos escollos que se le
presentan a la computación. Hay otros problemas que si bien son
computables demandan para su resolución un esfuerzo enorme en
tiempo y en memoria. Estos problemas se llaman *intratables*.
El análisis de algoritmos se ocupa de separar los problemas
tratables de los intratables, encontrar la solución más barata
para resolver un problema dado, y en el caso de los intratables,
resolverlos de manera aproximada: no encontramos la verdadera
solución porque no nos alcanzan los recursos para eso, pero
encontramos una solución bastante buena y que nos insume muchos
menos recursos (el orden de las respuestas de Google a una
búsqueda es un buen ejemplo de una solución aproximada pero no
necesariamente óptima).

En este curso trabajaremos con problemas no sólo computables sino
también tratables. Y aprenderemos a medir los recursos que nos
demanda una solución, y empezaremos a buscar la solución menos
demandante en cada caso particular.

Algunos ejemplos de los problemas que encararemos y de sus
soluciones:

.. admonition:: **Problema**

    Dado un número :math:`N` se quiere calcular :math:`N^{33}`

Una solución posible, por supuesto, es hacer el producto :math:`N × N × . . . × N` , que involucra 32 multiplicaciones.

Otra solución, mucho más eficiente es:

* Calcular :math:`N × N`.
* Al resultado anterior mutiplicarlo por sí mismo con lo cual ya disponemos de :math:`N^{4}`.
* Al resultado anterior mutiplicarlo por sí mismo con lo cual ya disponemos de :math:`N^{8}`.
* Al resultado anterior mutiplicarlo por sí mismo con lo cual ya disponemos de :math:`N^{16}`.
* Al resultado anterior mutiplicarlo por sí mismo con lo cual ya disponemos de :math:`N^{32}`.
* Al resultado anterior mutiplicarlo por :math:`N` con lo cual conseguimos el resultado deseado con sólo 6 multiplicaciones.

Cada una de estas soluciones representa un *algoritmo*, es decir un método de
cálculo, diferente. Para un mismo problema puede haber algoritmos diferentes que
lo resuelven, cada uno con un costo distinto en términos de recursos
computacionales involucrados.

.. class:: alert alert-success pull-right

    La palabra algoritmo no es una variación de *logaritmo*, sino que proviene
    de *algorismo*. En la antigüedad, los *algoristas* eran los que calculaban
    usando la numeración arábiga y mientras que los *abacistas* eran los que
    calculaban usando ábacos. Con el tiempo el *algorismo* se deformó en
    *algoritmo*, influenciado por el término *aritmética*.

    A su vez el uso de la palabra *algorismo* proviene del nombre de un
    matemático persa famoso, en su época y para los estudiosos de esa época,
    "Abu Abdallah Muhammad ibn Mûsâ al-Jwârizmî", que literalmente significa:
    "Padre de Ja’far Mohammed, hijo de Moises, nativo de Jiva". Al-Juarismi,
    como se lo llama usualmente, escribió en el año 825 el libro "Al-Kitâb
    al-mukhtasar fî hîsâb al-gabr wa’l-muqâbala" (Compendio del cálculo por el
    método de completado y balanceado), del cual surgió también la palabra
    *"álgebra"*.

    Hasta hace no mucho tiempo se utilizaba el término algoritmo para referirse
    únicamente a formas de realizar ciertos cálculos, pero con el surgimiento de
    la computación, el término algoritmo pasó a abarcar cualquier método para
    obtener un resultado.

.. admonition:: **Problema**

    Tenemos que permitir la actualización y consulta de una guía telefónica.

Para este problema no hay una solución única: hay muchas y cada
una está relacionada con un contexto de uso. ¿De qué guía estamos
hablando: la guía de una pequeña oficina, un pequeño pueblo, una
gran ciudad, la guía de la Argentina? Y en cada caso ¿de qué tipo
de consulta estamos hablando: hay que imprimir un listado una vez
por mes con la guía completa, se trata de una consulta en línea,
etc.? Para cada contexto hay una solución diferente, con los datos
guardados en una *estructura de datos* apropiada, y con
diferentes algoritmos para la actualización y la consulta.

Cómo darle instrucciones a la máquina usando Python
---------------------------------------------------

.. class:: alert alert-success pull-right

    Python fue creado a finales de los años 80, por un programador holandés
    llamado Guido van Rossum, quien sigue siendo aún hoy el líder del
    desarrollo del lenguaje.

    La versión 2.0, lanzada en 2000, fue un paso muy importante para el
    lenguaje ya que era mucho más madura, incluyendo un *recolector de
    basura*.  La versión 2.2, lanzada en diciembre de 2001, fue también un hito
    importante ya que mejoró la orientación a objetos.  La última versión de
    esta línea es la 2.7 que fue lanzada en noviembre de 2010 y aún está vigente.

    En diciembre de 2008, se lanzó la rama 3.0, cuya versión actual es la
    3.5, de septiembre de 2015. Sin embargo, debido a que estas versiones
    introducen importantes cambios y no son totalmente compatibles
    con las versiones anteriores, todavía no se la utiliza extensamente.
