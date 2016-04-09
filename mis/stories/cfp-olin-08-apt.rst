.. title: Manejo de paquetes
.. slug: bitson/olin/apt
.. date: 2015-08-26 15:41:53 UTC-03:00
.. tags:
.. category:
.. link:
.. description:
.. type: text

.. class:: alert alert-info pull-right

.. contents::

::

    Debian ---> APT (Advanced Package Tool)
                extensión = .deb

    Arch -----> PACMAN (Package Manager)

    RedHat ---> YUM
                extesión = .rpm

----

Archivo de configuración:
-------------------------

``/etc/apt/sources.list``

.. code:: console

    deb http://sito.ejemplo.com/debian distribucion rama1 rama2 rama3
    deb-src http://sito.ejemplo.com/debian distribucion rama1 rama2 rama3


deb/deb-src
    si dice deb, entonces busca en el repositorio los archvios binarios.
    Si dice deb-src busca los códigos fuente.

URL
    la ubicación del repositorio.

distribución
    el nombre clave de la versión o la clase de la versión
    (Por ejemplo: wheezy= nombre clave, clase=stable).

ramas
     son distintos canales del repositorio con paquetes de diferentes características.
     (libre | "semi"-libres | no-libres)

----

**IMPORTANTE!!**

**PARA EDITAR EL ARCHIVO**
``/etc/apt/sources.list``
**TENEMOS QUE SER EL SUPERUSUARIO.**

----

Para actualizar las cabeceras de los paquetes

.. code-block:: console

	$ sudo apt update

Para actualizar los paquetes (el sistema)

.. code-block:: console

	$ sudo apt upgrade

Para instalar paquetes

.. code-block:: console

	$ sudo apt install *<nombre_del_paquete>*

Ejemplo: suponganse que queremos instalar el paquete mc (Midnight Commander).

.. code-block:: console

	$ sudo apt install mc

Otro ejemplo: ahora queremos instalar el programa htop y terminator.

.. code-block:: console

	$ sudo apt install htop terminator

Para desinstalar paquetes

.. code-block:: console

	$ sudo apt remove <nombre_del_paquete>

Para desinstalar y borrar todos los archivos de configuración

.. code-block:: console

	$ sudo apt purge <nombre_del_paquete>

----

Para buscar paquetes por nombres (o partes de nombres).

.. code-block:: console

	$ sudo apt-cache search <nombre>

Para mostrar la información del paquete:

.. code-block:: console

	$ sudo apt-cache show <nombre>
