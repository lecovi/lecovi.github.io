.. title: Ver mensajes en el booteo
.. slug: ver-mensajes-en-el-booteo
.. date: 2016-01-07 12:53:16 UTC-03:00
.. tags: boot,splash,quiet,mensajes 
.. category: 
.. link: 
.. description: 
.. type: text

En este breve post, la idea es mostrar los pasos a seguir para sacar la imagen
de inicio del sistema. En lo personal me gusta ver qué es lo que está cargando
el sistema al momento del inicio. Por eso le suelo sacar la imagen que oculta
esos mensajes. Comencemos...

Edición de los parámetros de inicio
===================================

.. code-block:: console

    $ sudo vim /etc/default/grub

Hay que editar el archivo ``/etc/default/grub`` en este archivo vamos a
encontrar una línea que dice:

.. code-block:: console

    GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"


Tenemos que remover la opción de ``"quiet splas"`` para que la línea en
cuestión quede como:

.. code-block:: console

    GRUB_CMDLINE_LINUX_DEFAULT=""

Actualizando GRUB
=================

Finalmente actualizamos las opciones de GRUB con el comando:

.. code-block:: console

    $ sudo update-grub

Listo! En el próximo inicio veremos como se va cargando el sistema.
