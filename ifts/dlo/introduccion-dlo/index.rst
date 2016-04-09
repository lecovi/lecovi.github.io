.. title: Introducción al Curso
.. slug: ifts/dlo/introduccion-dlo
.. date: 2015-08-26 15:18:41 UTC-03:00
.. tags:
.. category:
.. link:
.. description:
.. type: text

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

Máquinas Virtuales & GNU/Linux
==============================

Fijate en este artículos:

#. :doc:`Software Libre y GNU/Linux <cfp/olin/introduccion-olin>`
#. :doc:`Máquinas virtuales <cfp/olin/vbox-olin>`

Acá podés descargar las |maquinas_virtuales|.

.. |maquinas_virtuales| raw:: html

    <a href="https://mega.nz/#F!yYxDgDbJ!CmVGhOgD-F4XnxPrM7BXTg" target="_blank">máquinas virtuales</a>

Comandos GNU/Linux
-------------------

Prompt
~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~

Este comando nos imprime en pantalla en qué *carpeta* estamos parados. Simplemente ejecutando ``pwd``.

.. code-block:: console

    alumno@vm-lmde-mate-32b ~ $ pwd
    /home/alumno
    alumno@vm-lmde-mate-32b ~ $

Como estamos parados en el *home de alumno* nos dice ``/home/alumno``. En esta ruta (también llamado comunmente *path*) lo primero que identificamos es que el separador de carpetas (o directorios) es el símbolo de ``/``.

Además, notamos que no nos indica ningún tipo de unidad como sucede en otros sistemas operativos. No existe el `C:`, `D:` o `E:`. Todo nuestro sistema de archivos (*filesystem*) está montado sobre una única raíz, llamada **root** que se simboliza con barra **/**. Entonces, en la ruta

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
~~~~

Si queremos ver cuál es el contenido del directorio, ejecutamos el comando ``ls``.

.. code-block:: console

    alumno@vm-lmde-mate-32b ~ $ ls
    Descargas  Documentos  Escritorio  Imágenes  Música  Plantillas  Público
    Vídeos
    alumno@vm-lmde-mate-32b ~ $

El comando ``ls`` acepta varios modificadores para obtener mayor información sobre los elementos que encontramos en el directorio.

Change Directory
~~~~~~~~~~~~~~~~

Con el comando ``cd`` podemos cambiar el directorio de trabajo. Para ejecutarlo, debemos escribir ``cd`` seguido del nombre del directorio al cual nos queremos mover.

Bibliografía
============

#. **Aprenda a pensar como un programador con Python**, *Allen Downey, Jeffrey Elkner & Chris Meyers* |libro|.
#. **Algoritmos y programación 1 | Aprendiendo a programar usando Python como herramienta**, *Rosita Wachenchauzer & Colaboradores* |apunte_7540|.
#. **Tutorial de Python Argentina**, *PyAr* |tuto_pyar|.
#. **Python para todos**, *Raúl González Duque* |ppt|.
#. **Think Python 2e**, *Allen B. Downey* [inglés] |think_python|.

.. |libro| raw:: html

    <a href="https://github.com/lecovi/thinkcs-py_es/releases/download/v3.0.0-b1/top.pdf" target="_blank">Descarga</a>

.. |apunte_7540| raw:: html

    <a href="https://drive.google.com/file/d/0B5YeA72NbAFYTHhhWVc0TlVWUDg/view?usp=sharing" target="_blank">Descarga</a>

.. |think_python| raw:: html

    <a href="http://greenteapress.com/wp/think-python-2e/" target="_blank">Descarga</a>

.. |tuto_pyar| raw:: html

    <a href="http://docs.python.org.ar/tutorial/" target="_blank">Descarga</a>

.. |ppt| raw:: html

    <a href="http://mundogeek.net/tutorial-python/" target="_blank">Descarga</a>
