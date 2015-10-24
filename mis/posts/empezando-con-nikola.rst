.. title: Empezando con Nikola
.. slug: empezando-con-nikola
.. date: 2015-10-14 13:37:37 UTC-03:00
.. tags: blog,python,nikola,github
.. category: tutorial nikola github
.. link:
.. description: Tutorial Nikola GitHub Pages
.. type: text

.. class:: alert alert-info pull-right

.. contents::

Hace tiempo que venía con intenciones de sentarme a recopilar los diferentes
tutoriales y artículos que vengo pensando y escribiendo muchas veces en papel.

Y qué mejor manera de empezar que escribiendo sobre cómo voy a escribir...

Primeros Pasos
==============

Voy a suponer que no tenés nada instalado y que no tenés seteado tu ambiente de
laburo. Estos pasos los probé y los fui haciendo en una máquina virtual con
Linux Mint Debian Edition "Betsy", por lo que deberían ser 100% compatibles con
cualquier distro basada en Debian.

Para poder trabajar con Nikola, primero tenemos que setear nuestro ambiente de
Python. Nikola es un generador de sitios estáticos escrito en Python por el
gran `Roberto Alsina <https://twitter.com/ralsina>`_ y el `equipo de
colaboradores <https://getnikola.com/contact.html>`_ que se ha ido sumando.
Podés ver la documentación en el `sitio oficial <https://getnikola.com/>`_

Desde mi humilde perspectiva es una excelente herramienta para desarrolladores,
SysAdmins, DevOps y similares que están en la búsqueda de tener un blog/sitio
fácil de usar, de administrar y de rápida publicación. Además como se genera un
sitio estático, podés aprovechar el uso de las `GitHub Pages
<https://pages.github.com/>`_.

Instalación paquetes de sistema
-------------------------------

Vamos a usar Nikola con Python 3. Necesitamos tener instalado los siguientes
paquetes, son herramientas súper comunes, si desarrollás en Python, seguramente ya las tenés instaladas:

.. sidebar:: Paquetes de sistema

    .. class:: alert alert-info small

    - ``python3-dev``: es el paquete que contiene los archivos fuente para que se puedan compilar al momento de la instalación de nuevos paquetes.
    - ``python-pip``: es el manejador de paquetes de Python, con esto vas a poder instalar la mayoría de los paquetes para tus programas.
    - ``libxml2-dev``: librería de desarrollo de `XML`, necesaria para desarrollar usando la librería de `GNOME XML`
    - ``libxslt1-dev``: librería de desarrollo para la conversión de archivos `XML` a cualquier otro formato, por ejemplo: `HTML`
    - ``zlib1g-dev``: librería de desarrollo que implementa el método de compresión «deflate» usando `gzip` y `PKZIP`.

.. code-block:: bash

    $ sudo apt install python3-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev

Luego de esto, vamos a instalar `virtualenvwrapper`. Ésta es una herramienta
que sirve para manejar nuestros entornos virtuales de Python. Muchas veces
tenemos que estar trabajando en varios proyectos. Y al darse esa situación,
aparecen conflictos entre diferentes librerías y versiones de paquetes que hay
que usar. Por eso la mejor manera de prevenirlo es contar con una instalación
"limpia" para cada proyecto.

Instalando el entorno virtual
-----------------------------

Con `virtualenvwrapper` podemos no sólo crear estos ambientes sino que además
vamos a tener todos los ambientes centralizados en un mismo directorio.
Además provee comandos para el manejo de los entornos virtuales. Consultá la
`documentación oficial <http://virtualenvwrapper.readthedocs.org/en/latest/>`_ del proyecto.

Para instalarlo, ahora que tenemos `pip`, simplemente ejecutamos:

.. code-block:: bash

    $ sudo pip install virtualenvwrapper

.. sidebar:: ¿Por qué con instalamos `virtualenvwrapper` con `sudo`?

    .. class:: alert alert-info small

    Necesitamos instalar `virtualenvwrapper` como `sudoer` porque necesitamos
    tenerlo en nuestra instalación global de Python.

Ahora ya tenemos `virtualenvwrapper` instalado. Para que los nuevos comandos de
`virtualenvwrapper` funcionen en nuestro sistema, tenés que agregar lo siguiente
a tu `.bashrc`, agregalo al final del archivo y va a funcionar de 10:

.. code-block:: console

    export WORKON_HOME=~/.envs
    source /usr/local/bin/virtualenvwrapper.sh

.. sidebar:: Explicación sobre la edición del `.bashrc`

    .. class:: alert alert-warning small

    Con la directiva ``export`` estamos generando una nueva variable de entorno
    en nuestro `SHELL`, esta directiva apunta a un directorio oculto en nuestro
    `HOME` que se llama ``.envs``.

    .. class:: alert alert-warning small

    Con la directiva ``source`` estamos cargando en nuestro `SHELL` los comandos
    que nos agrega `virtualenvwrapper` para el manejo de entornos virtuales.


Ahora tenemos que recargar el archivo `.bashrc` y crear el directorio donde se
van a alojar todos los entornos virtuales que creemos con `virtualenvwrapper`.

.. code-block:: bash

    $ . .bashrc
    $ mkdir -p $WORKON_HOME

Ahora estamos en condiciones de crear nuestro entorno virtual, al que llamaremos
`nikola`. Lo creamos con la instrucción:

.. code-block:: console

    $ mkvirtualenv -p /usr/bin/python3 nikola
    (nikola) $

Como verán, entre paréntesis nos indica el nombre del entorno virtual en el que
estamos trabajando. Si ejecutamos ``python``, vamos a ver que nos indica que
la versión a la que llamamos es Python 3 y no Python 2.

.. code-block:: bash

    (nikola) $ python
    Python 3.4.2 (default, Oct  8 2014, 10:45:20)
    [GCC 4.9.1] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Para salir del entorno virtual, ejecutamos el comando ``deactivate``, o
simplemente cerramos la terminal en la que estamos trabajando.

Podemos ejecutar ``python`` nuevamente, para ver cómo se desactivó el entorno.
En este caso, se ejecuta Python 2. Perfecto! Todo funciona... ;-)

.. code-block:: bash

    (nikola) $ deactivate
    $ python
    Python 2.7.9 (default, Mar  1 2015, 12:57:24)
    [GCC 4.9.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Para volver a trabajar en el entorno, usás el comando ``workon`` seguido del
nombre del entorno virtual. Para nosotros, sería:

.. code-block:: bash

    $ workon nikola
    ...
    (nikola) $ deactivate


Instalando Nikola
-----------------

Ahora simplemente nos queda instalar nikola. En la página oficial está muy bien
documentado el proceso de instalación, aunque está en inglés. `Acá <https://getnikola.com/getting-started.html>`_ tenes el link para leerlo.

Igualmente, la forma más fácil es a través de ``pip``:

.. class:: alert alert-warning

    ¡Eso sí! No te olvides de hacer esto en el entorno virtual.

.. code-block:: bash

    $ workon nikola
    (nikola) $ pip install Nikola

Creando nuestro sitio
=====================

Después de que termine de ejecutarse la instalación con ``pip``, seguimos las
instrucciones de la `documentación <https://getnikola.com/getting-started.html>`_.

Si queremos que nuestro sitio se llame, "*tecnotux*", deberíamos ejecutar el
siguiente comando:

.. code-block:: bash

    (nikola) $ nikola init tecnotux

.. sidebar:: Usando datos de demostración

    .. class:: alert alert-success small

    Si queremos tener datos de muestra para aprender a usar Nikola, podemos
    ejecutar el comando de inicialización del sitio con la opción ``--demo``

    .. code-block:: bash

        (nikola) $ nikola init --demo tecnotux

Cuando estamos iniciando nuestro sitio, nikola nos preguntará algunas cosas para
poder configurarlo correctamente.

.. TODO: poner preguntas de nikola (print screen?)

Creando post
------------

Ahora que tenemos nuestro sitio configurado, debemos crear nuestro primer post.
Para eso, debemos ejecutar:

.. code-block:: bash

    (nikola) $ cd tecnotux
    (nikola) $ nikola new_post

Nikola nos preguntará el nombre del post, y creará el archivo dentro del
directorio `posts` con el nombre hayamos completado.

Luego, simplemente con tu editor de texto preferido (en mi caso `Atom <https://atom.io/>`_ o `Vim <http://www.vim.org/>`_) editamos el contenido del
archivo utilizando el formato de texto restructuredText.
Es un formato muy sencillo que se lleva muy bien con Python. Podés consultar una
breve guía en la `página de Nikola <https://getnikola.com/quickref.html>`_.


.. TODO: ejemplo de rst para Nikola

Construyendo el sitio
---------------------

Una vez que terminado o si queremos ver cómo está quedando. Tenemos que
construir el sitio. Y luego ejecutar el servidor web de prueba para que nos lo
muestre en nuestro navegador.

.. code-block:: bash

    (nikola) $ nikola build
    ....
    (nikola) $ nikola serve -b

Publicando nuestro sitio en GitHub
==================================

Para usar GitHub Pages, por supuesto que tenés que tener una cuenta de GitHub.
Es gratuito y te va a servir para publicar, además de tu sitio, tus proyectos
de software libre!

Creando el repositorio para el sitio
------------------------------------

En el `sitio de las páginas de github <https://pages.github.com/>`_ están
explicados los pasos a seguir para crear el repositorio necesario para publicar
con GitHub Pages.

Los pasos son los siguientes:

#. Crear un repositorio para tu usuario con el nombre: ``usuario.github.io``.

    Si tu usuario es `pepito1234` vas a tener que crear un repositorio
    llamado ``pepito1234.github.io``.
    Creá tu repositorio con el archivo ``README.md``, ponele una licencia que te
    parezca y agregale el archivo ``.gitignore`` con archivos de Python.

#. Clonás el repositorio con el comando:

    .. code-block:: console

        $ git clone https://github.com/pepito1234/pepito1234.github.io

#. Entrás a la carpeta ``pepito1234.github.io`` y ahí dentro creás un archivo     ``index.html`` que contenga el siguiente texto:

    .. code-block:: html

        <h1>Este es mi sitio</h1>
        <h2>pepito1234</h2>

#. Agregás el archivo al repositorio

    .. code-block:: console

        $ git add --all

#. *Commiteás* los cambios en el *repo*:

    .. code-block:: console

        $ git commit -m "Iniciando repositorio"

#. *Pusheas* el repositorio a GitHub:

    .. code-block:: console

        $ git push -u origin

#. Ahora a probar! Abrí tu navegador y andá a la dirección: ``http://usuario.github.io``

    Siguiente el ejemplo deberías ir a ``http://pepito1234.github.io``

Poniendo Nikola en el repo
--------------------------

Para que github publique nuestro sitio éste tiene que estar en la rama `master`.
Por eso, primero debemos crear una nueva rama para alojar nuestro código ahí
y después tener los archivos que se van a publicar en la rama `master`.

No te preocupes, esto después lo vas a hacer simplemente con un comando de
Nikola y la publicación va a ser muy fácil...

* Para crear una nueva rama que llamaremos ``src`` ejecutamos dentro del repositorio:

    .. code-block:: console

        $ git checkout -b src

Esto crea la nueva rama y nos cambia automáticamente a ella. Ahora estamos
listos para mover nuestro sitio al repositorio.

Si venís siguiendo el tutorial al "pie de la letra", asumo que tenés los
archivos de tu sitio en el home de tu usuario (``~/tecnotux``).
También debés tener el repositorio en el home del usuario (``pepito1234.github.io``). Tenemos que mover el contenido de `tecnotux` dentro
del directorio del repositorio.

    .. code-block:: console

        $ mv ~/tecnotux ~/pepito1234.github.io

Ahora modificamos el contenido del archivo ``.gitignore`` para que el git no
esté pendiente de los nuevos archivos que Nikola necesita para crear los `html`.
Para eso, tenemos que agregar las siguientes líneas. Podés hacerlo en cualquier
lugar del archivo, pero te recomiendo que lo hagas al final del mismo.

    .. code-block:: console

        # Nikola stuff
        mis/cache/
        mis/output/
        mis/.doit.db*

Ahora tenemos que hacer un pequeño cambio en el ``conf.py``, tenemos que
decirle a Nikola que vamos a estar publicando el sitio con GitHub Pages. Para
eso alrededor de la línea 430 debés tener lo que sigue:

    .. code-block:: console

        # For user.github.io OR organization.github.io pages, the DEPLOY branch
        # MUST be 'master', and 'gh-pages' for other repositories.
        #GITHUB_SOURCE_BRANCH = 'gh-pages'
        GITHUB_DEPLOY_BRANCH = 'master'

        # The name of the remote where you wish to push to, using
        github_deploy.
        GITHUB_REMOTE_NAME = 'origin'

Ya estamos listos, ahora podemos publicar nuestro sitio en GitHub Pages con el
comando:

    .. code-block:: console

        $ nikola github_deploy

Ahora sólo nos resta seguir escribiendo nuestros artículos y páginas y quedarán
publicados en `http://pepito1234.github.io`.

Espero que les sirva!
