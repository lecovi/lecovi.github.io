.. title: Introducción al Curso
.. slug: ifts/dlo/introduccion-dlo
.. date: 2015-08-26 15:18:41 UTC-03:00
.. tags:
.. category:
.. link:
.. description:
.. type: text

.. class:: alert alert-info pull-right

.. contents::

A lo largo del curso vamos a trabajar con una máquina virtual con *Linux Mint
Debian Edition*. Si querés podés conseguir la imagen `.iso` para instalar en
este |lmde|.

.. |lmde| raw:: html

    <a href="https://www.linuxmint.com/download_lmde.php" target="_blank">link</a>

LMDE viene en 2 *sabores*:

#. Cinnamon
#. MATE

A nosotros, como Argentinos, nos gusta mucho el MATE, por eso optamos por esta
versión. Además consume un poco menos de recursos, ya que el entorno gráfico
MATE es más ligero que Cinnamon y en el uso con las máquinas virtuales se nota
un poco la diferencia.

Recursos
========

Máquinas Virtuales & Bibliografía
---------------------------------

En la sección de recursos_ podés descargar las máquinas virtuales y la
bibliografía del curso.

Para ver un paso a paso de cómo instalar tu máquina virtual:

* :doc:`Máquinas virtuales <bitson/olin/vbox-olin>`

GNU/Linux
---------

Para saber un poco más sobre GNU/Linux:

* :doc:`Software Libre y GNU/Linux <bitson/olin/introduccion-olin>`

.. _recursos: /resources

Comandos GNU/Linux
==================

Prompt
------

Cuando abrimos nuestra terminal, nos muestra el *prompt*. Éste es el indicador
de que la terminal está esperando que le demos comandos para ejecutar.

.. code-block:: console

    alumno@vm-lmde-mate-32b ~ $


En nuestro caso, identificamos 5 secciones en el *prompt*.

#. ``alumno``: el nombre del usuario con el que estamos logueados.
#. ``@``: el símbolo arroba que significa *at* en inglés (en).
#. ``vm-lmde-mate-32b``: el *hostname*, es decir, el nombre de la máquina.
#. ``~``: el símbolo de tilde, o ñuflo o también llamado *el cosito de la eñe*, nos indica que estamos en el **home del usuario**
#. ``$``: el terminador del *prompt*, que nos indica que ahí terminó el prompt. Por ser el símbolo de ``$``, sabemos que estamos conectados con un usuario sin privilegios. Sino, terminaría con ``#``.

Print Working Directory
-----------------------

Este comando nos imprime en pantalla en qué *carpeta* estamos parados. Simplemente ejecutando ``pwd``.

.. code-block:: console

    alumno@vm-lmde-mate-32b ~ $ pwd
    /home/alumno
    alumno@vm-lmde-mate-32b ~ $

Como estamos parados en el *home de alumno* nos dice ``/home/alumno``. En esta
ruta (también llamado comunmente *path*) lo primero que identificamos es que el
separador de carpetas (o directorios) es el símbolo de ``/``.

Además, notamos que no nos indica ningún tipo de unidad como sucede en otros
sistemas operativos. No existe el `C:`, `D:` o `E:`. Todo nuestro sistema de
archivos (*filesystem*) está montado sobre una única raíz, llamada **root** que
se simboliza con barra **/**. Entonces, en la ruta

    ``/home/alumno``

Identificamos 3 partes:

#. ``/``: barra, *root* o raíz del sistema de archivos. Es lo equivalente a `C:\\`.
#. ``home``: un directorio que está dentro de la raíz de nuestro *filesystem*.
#. ``alumno``: un directorio que está dentro del directorio ``home``.

Si lo ejemplificamos en forma de árbol sería algo así:

    * **/**
        - ``home``
            + ``alumno``

List
----

Si queremos ver cuál es el contenido del directorio, ejecutamos el comando
``ls``.

.. code-block:: console

    alumno@vm-lmde-mate-32b ~ $ ls
    Descargas  Documentos  Escritorio  Imágenes  Música  Plantillas  Público
    Vídeos
    alumno@vm-lmde-mate-32b ~ $

El comando ``ls`` acepta varios modificadores para obtener mayor información
sobre los elementos que encontramos en el directorio.

Change Directory
----------------

Con el comando ``cd`` podemos cambiar el directorio de trabajo. Para ejecutarlo,
debemos escribir ``cd`` seguido del nombre del directorio al cual nos queremos
mover. Por ejemplo, dentro de nuestro *home* tenemos un directorio llamado
``Documentos``, si queremos movernos dentro ejecutamos:

.. code-block:: console

    alumno@vm-lmde-mate-32b ~ $ cd Documentos/
    alumno@vm-lmde-mate-32b ~/Documentos $

Notemos ahora cómo cambió el *prompt*, en la sección donde nos muestra el
directorio de trabajo ahora dice ``~/Documentos``, indicándonos que estamos
dentro del directorio. Esto es lo mismo que hacer doble click sobre la carpeta
en el entorno gráfico.

El comando ``cd`` acepta algunos *atajos* especiales:

* ``..``: siempre que veamos dos puntos seguidos, estaremos haciendo referencia al directorio padre.
* ``-``: si ejecutamos como argumento con un guión medio, ``cd`` nos llevará al directorio donde estábamos parados anteriormente.
* ``~``: podemos usar este símbolo para evitar escribir el *path* de nuestro `HOME`.
* `sin argumentos`: si ejecutamos ``cd`` sin argumentos, nos llevará a nuestro `HOME` sin importar dónde estemos parados.
