.. title: Introducción a Flask
.. slug: ifts/edd/intro-flask
.. date: 2015-08-26 15:18:41 UTC-03:00
.. tags:
.. category:
.. link:
.. description:
.. type: text

.. class:: alert alert-info pull-right

.. contents::

.. class:: jumbotron

    **Objetivos**:
        - Comprender la arquitectura de la Web.
        - Familiarizarse con los conceptos básicos y terminologías utilizadas.
        - Instalar un entorno virtual de Python para nuestros proyectos.
        - Realizar una aplicación ``"Hello World!"`` con Flask.

.. TODO: poner explicación de Internet y redes básico. Cubrir los siguientes conceptos: socket, IP, puertos, DNS, Request-Reply, URL, Protocolos.

.. class:: row

Arquitectura de la web
==================================

Cuando hablamos de web tenemos que hacer la distinción entre WWW(Word wide web) e Internet. **No son lo mismo**

Por un lado la WWW es es una colección global de documentos de textos y otros recursos, unidos por hyperlinks(enlaces) y URIs(uniform resource identifies). En cambio internet es un sistema global de redes de computadoras conectadas.

Cómo funciona la web
----------------------

Sabemos que para acceder a la web necesitamos un navegador(browser), como por ejemplo Internet Explorer (por favor no uses ese), MozillaFirefox, Chrome, Opera, Safari, etc, y una dirección de internet, digamos «www.google.com.ar». Al apretar *ir* o apretar la tecla enter, suceden varian cosas.

Por un lado el navegador envía por internet la petición de la página que queremos alcanzar, para ello existe el DNS(Domain Name Service), que se encarga de traducir el *nombre de dominio* «google.com.ar» a una dirección IP(Internet Protocol), que es un número que identifica a un recurso en un servidor(computadora), como por ejemplo 192.169.255.1. Así la petición que estamos haciendo llega al destino indicado, es asi como el navegador "sabe" dónde ir a buscar los contenidos de cada sitio que visitamos.

Socket designa un concepto abstracto por el cual dos programas (posiblemente situados en computadoras distintas) pueden intercambiar cualquier flujo de datos, generalmente de manera fiable y ordenada.

El término socket es también usado como el nombre de una interfaz de programación de aplicaciones (API) para la familia de protocolos de Internet TCP/IP, provista usualmente por el sistema operativo.

Un puerto de red es una interfaz para comunicarse con un programa a través de una red

.. TODO: reemplazar por el link correcto

.. class:: col-xs-12 col-md-8 col-md-offset-1 embed-responsive embed-responsive-16by9

    .. raw:: html

        <iframe class="embed-responsive-item"
        src="http://bitson.github.io/cursos/python1"
        scrolling="no"></iframe>


Instalación de Paquetes necesarios
==================================

#. Instalar ``pip``.
#. Instalar ``virtualenv``.

Así como nuestro GNU/Linux tiene una herramienta para la instalación de paquetes como ``apt`` o ``yum/dnf``, con Python también tenemos algo similar. Por suerte existe ``pip`` y la instalación de paquetes es muy sencilla.

Necesitamos tener instalado en nuestro sistema opertativo esta herramienta. Para eso debemos instalar los paquetes ``python3-pip`` para usar ``pip3`` con Python 3.x y ``python-pip`` para usar ``pip`` con Python 2.x:

.. code-block:: bash

    $ sudo apt install python-pip python3-pip

Ahora que tenemos instalado ``pip`` podemos usarlo para instalar ``virtualenv``.

.. code-block:: bash

    $ sudo pip install virtualenv

Creando el proyecto
===================

#. Crear el entorno virtual.
#. Instalar Flask.
#. Armando la aplicación.

Creando el entorno virtual
--------------------------

Con las herramientas necesarias ya instaladas, tenemos que crear un directorio donde vamos a contener los archivos necesarios. Creamos una carpeta que se llame ``hello_world_app`` y nos movemos dentro de ella para instalar el entorno virtual de Python.

.. code-block:: bash

    ~ ➜ mkdir hello_world_app
    ~ ➜ cd hello_world_app
    ~/hello_world_app ➜

Todo el trabajo de nuestros proyecto web lo realizaremos dentro de esta carpeta ``hello_world_app``. Si queremos pasar nuestro trabajo a otra máquina basta con copiar esta carpeta a destino y tenemos nuestros proyecto donde querramos.

Para instalar el entorno virtual, debemos darle un nombre, ``flasky`` es el que elegimos para este proyecto. Simplemente para no confundir el nombre del entorno virtual con el paquete `Flask`. Vamos a usar Python 3 en nuestra aplicación. Para averiguar dónde está el binario de Python 3 usamos el comando ``which``:


.. code-block:: bash

    ~/hello_world_app ➜ which python3
    /usr/bin/python3
    ~/hello_world_app ➜


Ahora le pasamos esa ruta al comando ``virtualenv`` para que nos cree el entorno virtual con Python 3 utilizando el parámetro ``-p``:

.. code-block:: bash

    ~/hello_world_app ➜ virtualenv -p /usr/bin/python3 flasky

Esto creará una carpeta llamada `flasky` que contiene una instalación de Python.

.. TIP::

    O podemos hacer todo junto en un mismo comando:

    .. code-block:: bash

        ~/hello_world_app ➜ virtualenv -p $(which python3) flasky


.. image:: /images/edd/virtualenv_tree.png
    :scale: 50 %
    :alt: Árbol del entorno virtual.
    :class: align-center


Dentro de esta carpeta nos interesa el archivo ``activate`` que va a servir para activar nuestro entorno virtual en nuestra sesión activa de la terminal. Lo activamos usando el comando ``source`` de la siguiente manera:


.. code-block:: bash

    ~/hello_world_app ➜ source flasky/bin/activate
    (flasky) ~/hello_world_app ➜


Luego podemos usar el comando ``deactivate`` para volver a tener nuestra terminal normalmente.

.. code-block:: bash

    (flasky) ~/hello_world_app ➜ deactivate
    ~/hello_world_app ➜

.. TIP::

    Activar el entorno virtual implica que cuando ejecutemos el comando ``python`` se llamará al binario del entorno virtual y no al de la instalación normal de nuestro sistema operativo. En el entorno virtual podemos instalar diferentes paquetes y versiones y quedarán para uso exclusivo de este entorno.

Instalando Flask
----------------

Con el entorno virtual activo instalamos ``Flask`` usando ``pip``.

.. code-block:: bash

    (flasky) ~/hello_world_app ➜ pip install Flask


.. TIP::

    Otra ventaja del entorno virtual es que nos deja instalar paquetes de `Python` a través de ``pip`` sin tener que tener privilegios administrativos. Es decir, sin usar ``sudo``.


Armando la aplicación
---------------------

Y creamos las carpetas necesarias para nuestra aplicación:

.. code-block:: bash

    (flasky) ~/hello_world_app ➜ mkdir app
    (flasky) ~/hello_world_app ➜ mkdir app/static
    (flasky) ~/hello_world_app ➜ mkdir app/templates

Dentro de ``app`` tendremos crearemos todos los archivos de la aplicación de `Flask`. Dentro de ella creamos un archivo llamado ``routes.py`` con el siguiente contenido:

.. listing:: edd/routes.py python3

Luego podemos ejecutar nuestra aplicación de prueba que escuchará peticiones en la ip 127.0.0.1 en el puerto 5000. Para cortar el servidor podemos presionar ``Ctrl+C``:

.. code-block:: bash

    (flasky) ~/hello_world_app ➜ python routes.py
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    * Restarting with stat
    * Debugger is active!
    * Debugger pin code: 459-745-705
