.. title: Empaquetado y compresión de paquetes
.. slug: bitson/olin/tgz
.. date: 2015-08-26 15:41:37 UTC-03:00
.. tags:
.. category:
.. link:
.. description:
.. type: text

.. class:: alert alert-info pull-right

.. contents::

Empaquetado
===========

Juntar archivos y directorios en un único archivo.
Para el empaquetado se utiliza el comando ``tar``.
Por lo general, los archivos resultantes del empaquetado
los llamaremos con una extensión ``.tar``.

TAR
---

.. code::  bash

    $ tar [opciones] <nombre_del_paquete>.tar <fuentes>

Ejemplo
~~~~~~~

Creemos la carpeta empaquetados dentro del HOME de nuestro usuario

.. code::  bash

    ~ $ mkdir empaquetados

Entremos en este nuevo directorio:

.. code::  bash

        ~ $ cd empaquetados

Copiemos el contenido de la carpeta /etc dentro de este nuevo directorio:

.. code::  bash

    ~/empaquetados $ cp -r /etc .

Entremos en el nuevo directorio etc:

.. code::  bash

    ~/empaquetados $ cd etc

Empaquetemos algunos de los archivos y direcotorios que tenemos dentro:

.. code::  bash

    ~/empaquetados/etc $ tar cf paquete.tar acpi/ alternatives/ hostname hosts PackageKit/ perl/ bluetooth/ python*

Ahora si listamos el contenido de este direcotorio, vamos a encontrar nuestro nuevo archivo ``paquete.tar``
Movemos el paquete al directorio padre:

.. code::  bash

    ~/empaquetados/etc $ mv paquete.tar ..

Y saltamos al directorio padre:

.. code::  bash

    ~/empaquetados/etc $ cd ..

Para desempaquetar (extraer):

.. code::  bash

    ~/empaquetados $ tar xf paquete.tar

----

Compresión
==========

La compresión de un archivo es la reducción del espacio que ocupa.
La idea es hacerlo ocupar menos espacio para almacenamiento o copia
de seguridad. Se hace pasar la información a través de un algoritmo
que reduce el espacio utilizado pero que después puede volver a tener
su tamaño original. Es lo que se conoce como *Compresión sin pérdida de datos*.
Para comprimir y descomprimir podemos usar los comandos ``gzip`` y ``bzip2``.

GZIP
----

Para comprimir:

.. code::  bash

    $ gzip <archivo_a_comprimir>

Después de comprimir el archivo se sobreescribe comprimido y con la extensión ``.gz`` agregada.

Para descomprimir:

.. code::  bash

    $ gunzip <archivo_a_comprimir>

Después de descomprimir el archivo se sobreescribe descomprimido y con la extensión ``.gz`` quitada.

BZIP2
-----

Para comprimir:

.. code::  bash

    $ bzip2 <archivo_a_comprimir>

Después de comprimir el archivo se sobreescribe comprimido y con la extensión ``.bz2`` agregada.

Para descomprimir:

.. code::  bash

    $ bunzip2 <archivo_a_comprimir>

Después de descomprimir el archivo se sobreescribe descomprimido y con la extensión ``.bz2`` quitada.

Comparación entre GZIP y BZIP2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    - GZIP es más rápido pero comprime menos.
    - BZIP2 comprime más pero es más lento.

Por ejemplo en clase:

    paquete.tar     = 230K
    paquete.tar.gz  = 21K
    paquete.tar.bz2 = 17K

----

Empaquetado y compresión
========================

Para empaquetar y comprimir con ``tar`` y ``gzip``:

.. code::  bash

    ~ $ tar cfz paquete.tgz <fuentes>

Para empaquetar y descomprimir con ``tar`` y ``gzip``:

.. code::  bash

    ~ $ tar xfz paquete.tgz

Para empaquetar y comprimir con ``tar`` y ``bzip2``:

.. code::  bash

    ~ $ tar cfj paquete.tbz2 <fuentes>

Para empaquetar y descomprimir con ``tar`` y ``bzip2``:

.. code::  bash

    ~ $ tar xfj paquete.tbz2

----

Algunos comandos mas
====================

``shutdown``
    para apagar la máquina (tiene que hacerlo root ó a través de sudo).

``halt``
    también para apagar la máquina.

``poweroff``
    también para apagar la máquina.

``reboot``
    reinicia la máquina (tiene que hacerlo root ó a través de sudo).

``cat``
    este comando concatena archivos y los imprime en la salida.

.. code:: bash

        ~ $ cat <archivo1> <archivo2> ... <archivoX>

        ABORTAR = Ctrl+C (^C) ---> Va a terminar el proceso que se esté ejecutando.

``more``
    sirve para paginar el resultado impreso en pantalla.

``less``
    sirve para paginar el resultado impreso en pantalla. MEJOR! (q para salir).

``tail``
    muestra "la cola" del archivo, es decir, el final. Las 10 últimas líneas.

``head``
    muestra "la cabeza" del archivo, es decir, el principio. Las 10 primeras líneas.

``wc``
    (Word Count, conteo de palabras).

.. code:: bash

    ~ $ wc archivo1.txt
          105  636 4264 archivo1.txt
          |    |    |
          |    |    +--> Cantidad de Caracteres
          |    +-------> Cantidad de Palabras
          +------------> Cantidad de Líneas

``diff``
    muestra las diferencias entre 2 archivos.

``updatedb``
    actualiza la base de datos de nombres de archivos (y directorios) para que con el comando "locate" podamos encontrarlo (debe ejecutarse como root o con sudo).

``locate``
    busca nombres de archivos y directorios.

``find``
    busca con parámetros de búsqueda más extendidos que locate y no necesita de la base de datos.

``whereis``
    busca la ruta del binario (ejecutable), el fuente y/o la página de manual de un comando.

``which``
    nos indica en qué directorio del PATH está el comando que le pasamos como argumento.

 ``grep``
    (Globally Regular Expressions Pattern). Buscador de expresiones regulares (RegEx) dentro de archivos..
