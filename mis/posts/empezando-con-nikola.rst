.. title: Empezando con Nikola
.. slug: empezando-con-nikola
.. date: 2015-10-14 13:37:37 UTC-03:00
.. tags: blog,python,nikola,github,git
.. category: tutorial
.. link:
.. description: Tutorial Nikola GitHub Pages
.. type: text
.. version: 0.2

Hace tiempo que vengo con intenciones de sentarme y recopilar los diferentes
tutoriales y artículos que vengo pensando y escribiendo. Después de buscar
diferentes herramientás finalmente me decidí por usar `Nikola` y quiero
contarles cómo la uso.

Asi que, qué mejor manera de empezar que escribiendo un tutorial sobre las
herramientas que voy a usar para escribir...

En este tutorial voy a explicarte los pasos para instalar los paquetes
necesarios para que `Nikola` funcione con `GitHub Pages` desde cero.
Para eso vamos a:

#. Instalar y configurar nuestro entorno de `Python` para nuestro sitio.
#. Instalar y configurar `git` como sistema de control de versiones distribuido.
#. Crear nuestro sitio con `Nikola`.
#. Configurar nuestra cuenta en `GitHub` para el uso de `GitHub Pages`.

.. TEASER_END

.. class:: alert alert-info pull-right

.. contents::

Primeros Pasos
==============

Voy a suponer que no tenés nada instalado y que no tenés seteado tu ambiente de
laburo. Estos pasos los probé y los fui haciendo en una máquina virtual con
`Linux Mint Debian Edition "Betsy" <http://www.linuxmint.com/download_lmde.php>`_,
por lo que deberían ser 100% compatibles con cualquier *distro* basada en
`Debian` o `Ubuntu`.

Para poder trabajar con `Nikola`, primero tenemos que setear nuestro ambiente
de `Python`. `Nikola` es un generador de sitios estáticos escrito en `Python`
por el gran `Roberto Alsina <https://twitter.com/ralsina>`_ y el `equipo de
colaboradores <https://getnikola.com/contact.html>`_ que se ha ido sumando.
Podés ver la documentación en el `sitio oficial <https://getnikola.com/>`_

Desde mi humilde perspectiva es una excelente herramienta para desarrolladores,
SysAdmins, DevOps y entusiastas que están en la búsqueda de tener un blog/sitio
fácil de usar, de administrar y de rápida publicación. Además como se genera un
sitio estático, podés aprovechar el uso de las `GitHub Pages
<https://pages.github.com/>`_.

Instalación paquetes de sistema
-------------------------------

Vamos a usar `Nikola` con `Python 3`. Necesitamos tener instalado los
siguientes paquetes, son herramientas súper comunes, si desarrollás en Python,
seguramente ya las tenés instaladas. Para instalar los paquetes necesario tenés
que ejecutar el comando:

.. sidebar:: Paquetes de sistema

    .. class:: alert alert-info small

    - ``python3-dev``: es el paquete que contiene los archivos fuente para que se puedan compilar al momento de la instalación de nuevos paquetes.
    - ``python-pip``: es el manejador de paquetes de Python, con esto vas a poder instalar la mayoría de los paquetes para tus programas.
    - ``libxml2-dev``: librería de desarrollo de `XML`, necesaria para desarrollar usando la librería de `GNOME XML`
    - ``libxslt1-dev``: librería de desarrollo para la conversión de archivos `XML` a cualquier otro formato, por ejemplo: `HTML`
    - ``zlib1g-dev``: librería de desarrollo que implementa el método de compresión «deflate» usando `gzip` y `PKZIP`.
    - ``git``: el programa que te proporciona soporte para el control distribuido de versiones.

.. code-block:: bash

    $ sudo apt install python3-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev git
    [sudo] password for leo:

Luego de esto, vamos a instalar `virtualenvwrapper`. Ésta es una herramienta
que sirve para manejar nuestros entornos virtuales de `Python`. Muchas veces
tenemos que estar trabajando en varios proyectos. Y al darse esa situación,
aparecen conflictos entre diferentes librerías y versiones de paquetes que hay
que usar. Por eso la mejor manera de prevenirlo es contar con una instalación
"limpia" para cada proyecto.

Instalando el entorno virtual
-----------------------------

Con `virtualenvwrapper` podemos no sólo crear estos ambientes sino que además
vamos a tener todos los ambientes centralizados en un mismo directorio.
Además provee comandos para el manejo de los entornos virtuales. Consultá la
`documentación oficial <http://virtualenvwrapper.readthedocs.org/en/latest/>`_
del proyecto.

Para instalarlo, ahora que tenemos `pip`, simplemente ejecutamos:

.. code-block:: bash

    $ sudo pip install virtualenvwrapper
    [sudo] password for leo:

.. sidebar:: ¿Por qué con instalamos `virtualenvwrapper` con `sudo`?

    .. class:: alert alert-info small

    Necesitamos instalar `virtualenvwrapper` como `sudoer` porque necesitamos
    tenerlo en nuestra instalación global de Python.

Ahora ya tenemos `virtualenvwrapper` instalado. Para que los nuevos comandos de
funcionen en nuestro SHELL, tenés que agregar lo siguiente al final de tu
`.bashrc` (siempre y cuando uses BASH, si tenés ZSH y estás usando `Oh my zsh`
basta con agregar `virtualenvwrapper` a la lista de plugins):

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
O simplemente podés cerrar y volver a abrir una terminal.

.. code-block:: bash

    $ . .bashrc
    $ mkdir -p $WORKON_HOME

Ahora estamos en condiciones de crear nuestro entorno virtual, al que llamaremos
`mis` (una abreviación de *"Make it So"*). Lo creamos con la instrucción:

.. code-block:: console

    $ mkvirtualenv -p /usr/bin/python3 mis
    (mis) $

Como verán, entre paréntesis nos indica el nombre del entorno virtual en el que
estamos trabajando. Si ejecutamos ``python``, vamos a ver que nos indica que
la versión a la que llamamos es `Python 3` y no `Python 2`.

.. code-block:: bash

    (mis) $ python
    Python 3.4.2 (default, Oct  8 2014, 10:45:20)
    [GCC 4.9.1] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Para salir del entorno virtual, ejecutamos el comando ``deactivate``, o
simplemente cerramos la terminal en la que estamos trabajando.

Podemos ejecutar ``python`` nuevamente, para ver cómo se desactivó el entorno.
En este caso, se ejecuta `Python 2`.

.. code-block:: bash

    (mis) $ deactivate
    $ python
    Python 2.7.9 (default, Mar  1 2015, 12:57:24)
    [GCC 4.9.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Para volver a trabajar en el entorno, usás el comando ``workon`` seguido del
nombre del entorno virtual. Para nosotros, sería:

.. code-block:: bash

    $ workon mis
    ...
    (mis) $ deactivate

Instalando Nikola
-----------------

Ahora simplemente nos queda instalar `Nikola`. En la página oficial está muy
bien documentado el proceso de instalación, aunque está en inglés.
`Acá <https://getnikola.com/getting-started.html>`_ tenes el link para leerlo.

Igualmente, la forma más fácil es a través de ``pip``:

.. class:: alert alert-warning

    ¡Eso sí! No te olvides de hacer esto en el entorno virtual.

.. code-block:: bash

    $ workon mis
    (mis) $ pip install Nikola

Creando nuestro sitio
=====================

Después de que termine de ejecutarse la instalación con ``pip``, seguimos las
instrucciones de la `documentación <https://getnikola.com/getting-started.html>`_.

Si queremos que nuestro sitio se llame, por ejemplo: **"mis"**, deberíamos
ejecutar el siguiente comando:

.. code-block:: bash

    (mis) $ nikola init mis

.. sidebar:: Usando datos de demostración

    .. class:: alert alert-success small

    Si queremos tener datos de muestra para aprender a usar Nikola, podemos
    ejecutar el comando de inicialización del sitio con la opción ``--demo``

    .. code-block:: bash

        (mis) $ nikola init --demo mis

Cuando estamos iniciando nuestro sitio, `Nikola` nos preguntará algunas cosas
para poder configurarlo correctamente.

.. TODO: poner preguntas de nikola (print screen?). No, mejor un gif animado!!!

Creando post
------------

Ahora que tenemos nuestro sitio configurado, debemos crear nuestro primer post.
Para eso, debemos ejecutar:

.. code-block:: bash

    (mis) $ cd mis
    (mis) $ nikola new_post

`Nikola` nos preguntará el nombre del post, y creará el archivo dentro del
directorio `posts` con el nombre hayamos completado.

Luego, simplemente con tu editor de texto preferido (en mi caso
`Atom <https://atom.io/>`_ o `Vim <http://www.vim.org/>`_) editamos el
contenido del archivo utilizando el formato de texto `reStructuredText`.
Es un formato muy sencillo que se lleva muy bien con `Python`. Podés consultar
una breve guía en la `página de Nikola <https://getnikola.com/quickref.html>`_.

.. sidebar:: Bajate el código fuente de este artículo

    .. class:: alert alert-success

        #. Hacé click sobre el enlace de código fuente.
        #. Cuando el navegador cargue el archivo, con el botón derecho hacé click en *Guardar archivo como...*
        #. Guardalo dentro del directorio **posts** de tu sitio y listo!

Si no instalaste los archivos de prueba, podés usar este archivo, fijate arriba
en la barra de navegación, tenés el link para bajarte el código fuente de este
artículo.

Construyendo el sitio
---------------------

Una vez terminado o si queremos ver cómo está quedando. Tenemos que construir
el sitio. Es decir, `Nikola` va a leer los archivos que nosotros escribimos en
`reStructuredText`, interpretarlos y generar los correspondientes archivos HTML
para publicar en nuestro sitio.
Luego de contruirlo vamos a ejecutar el servidor web de prueba para que nos lo
muestre en nuestro navegador.

.. code-block:: bash

    (mis) $ nikola build
    ....
    (mis) $ nikola serve -b

Publicando nuestro sitio en GitHub
==================================

Para usar `GitHub Pages`, por supuesto que tenés que tener una cuenta de
`GitHub`. Es gratuito y te va a servir para publicar, además de tu sitio, tus
proyectos de software libre!
Si no tenés una cuenta en `GitHub`, hacé click en este `link
<https://github.com/>`_, elegí un nombre de usuario, una contraseña y poné tu
dirección de correo electrónico.

Configurando Git
----------------

Antes de empezar a usar `git`, tenemos que configurarlo. Como es un sistema de
control de versiones, `git` necesita saber quién está haciendo los cambios en
el repositorio local. Ya que de esa manera después se puede ver quién hizo qué
cambio. Te recomiendo que visites la `documentación de git
<http://git-scm.com/book/es/v2>`_.

En nuestro caso, por ahora, seremos sólo nosotros los que estemos trabajando en
nuestro sitio. Pero eso no tiene por qué ser así. Además también podemos usarlo
en diferentes computadoras y mantenerlo con un repositorio es mucho más fácil
que estar copiando todos los archivos de una máquina a la otra.

Para configurar nuestra identidad simplementen ejecutamos los comandos:

.. class:: alert alert-warning

Obviamente que con tu nombre, tu dirección de correo electrónico y tu editor de
texto preferido

.. code-block:: console

    $ git config --global user.name "Leandro E. Colombo Viña"
    $ git config --global user.email colomboleandro@bitson.com.ar
    $ git config --global core.editor vim


Seteando llaves SSH para usar con GitHub
----------------------------------------

.. sidebar:: ¿Qué son las llaves SSH? ¿Cómo las usamos con GitHub?

    .. class:: alert alert-success

        Son un par de archivos que tenés guardados en tu computadora que te
        identifican. Uno es el que se llama *llave pública* y el otro es la
        *llave privada*.
        La *llave pública* va a estar configurada en nuestra cuenta de `GitHub`
        y cuando querramos hacer un cambio en el repositorio, `git` se va a
        conectar usando nuestra *llave privada*.
        De esta manera nos comunicamos con una seguridad un poco mayor que
        simplemente usando **usuario** y **contraseña** y con la ayuda del
        agente SSH no vamos a tener que estar tipeando estos datos
        continuamente.

El sitio de `GitHub` cuenta con una gran biblioteca de recursos para aprender
diferentes funcionalidades. En este caso quisiera centrarme en configurar
nuestras llaves SSH para nuestra cuenta de `GitHub`.
Podés seguir los pasos de esta `página de ayuda
<https://help.github.com/articles/generating-ssh-keys/>`_ que intentaré resumir
a continuación.

Creamos nuestro par de llaves:

.. code-block:: console

    $ ssh-keygen -t rsa -b 4096 -C "colomboleandro@bitson.com.ar"
    Generating public/private rsa key pair.
    Enter file in which to save the key (/Users/you/.ssh/id_rsa): [Apretá enter]
    Enter passphrase (empty for no passphrase): [Escribí una clave]
    Enter same passphrase again: [Volvé a escribir tu clave]
    Your identification has been saved in /Users/you/.ssh/id_rsa.
    Your public key has been saved in /Users/you/.ssh/id_rsa.pub.
    The key fingerprint is:
    22:5c:2d:6c:00:a4:03:63:62:a1:82:72:08:0a:d5:60 colomboleandro@bitson.com.ar

Si no modificaste nada, entonces ahora tenés dos nuevos archivos
``~/.ssh/id_rsa`` y ``~/.ssh/id_rsa.pub``, donde el primer es tu **llave
privada** (que no vas a compartir) y el segundo es tu **llave pública**.

Para no tener que estar tipeando la clave constantemente, vamos a usar el
`ssh-agent`, que se ocupa de *recordar* nuestra clave por un período de tiempo.
Si queremos que esto se ejecute siempre al momento de loguearnos, tenemos que
agregar a nuestro las siguiente líneas al archivo ``~/.bash_profile``:

.. code-block:: console

    if [ -z "$SSH_AUTH_SOCK" ] ; then
        eval `ssh-agent -s`
        ssh-add
    fi

Verificamos si el agente está ejecutándose:

.. code-block:: console

    $ eval "$(ssh-agent -s)"

Ahora agregamos nuestra **llave privada** al agente con el comando:

.. code-block:: console

    $ ssh-add ~/.ssh/id_rsa

Usando la llave para entrar a GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Entramos a nuestra cuenta de `GitHub` y vamos a las opciones de nuestro perfil
en `<http://github.com/ssh>`_. Ahí vamos a seleccionar **Add SSH Key** para
agregar nuestra llave pública.
Elegimos un nombre para identificar a esta llave, por lo general, pondremos un
nombre descriptivo que tenga que ver con la máquina en la que estás trabajando.
Algo como "Escritorio", "Notebook", "Oficina" o lo que se te ocurra.
Luego tenemos que volcar el contenido de la **llave pública** en `GitHub`.
Ejecutamos en una terminal:

.. code-block:: console

    $ cat ~/.ssh/id_rsa.pub
    ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDGK1HYX1x6/wwxSH3hHExZnbBW66TPnIMAWk
    PZs/OYFR4fiqt87ZV7s1avGQDzUes3vAn00ubDzDd/MfZKMPu92Lmz24DdPLvMTDYutOGAAwu9
    vyCfMT8Htlv+lypg5/K3ZdMeQ/dSKy2ii7zumdAUdKEROgISUuuwaVsudOeyRSCsfO91sCnQ/5
    /0IYUvGG2Hwz0yvqyub55nz2kwj1lJn9rTzCJumlIvORlt3lnCG0vWNGZEDrdRmyrtoiOmvJVF
    Uwj4P9WPOQjzzUHUXmbKOLHB5rbO5uVTyJZTlUC9HWxaR9Ln5HCNpG2/vY+rKLY0MxtR5kYiwS
    CP2dqWsuNz1IHa6HA7CQOt6MXQO5ZIMax2bLKSZ7Ib1XJIR+X/6oglxQ/KXJF9U182JynzmNKD
    TGxIFA2Hp3ZG6WbZ6IBWLmFqC3A7XapYkrNCzp1XSEygPcu+4jP5trUjQS0NayCDECs1GU+/xd
    fjlg80KRMtjndKQbabP+TQnZF6O3Q2qnRiZk+YVzYXUM2PxO/E9JlWY77GxvU+G7HHYKHUy8W5
    gdNfKlNhEruGPxDUyXG2Qs/DZ/CIE9y7zjLtMxOPe9qWu06UZTNJSLNx04yosVkTliuPGKGLPt
    0SOxUaiDSDmmIzNR6nhPANmR3EwIGZcQ8rl/qIDXpznR/qecHQ+WuesQ== colomboleandro@
    bitson.com.ar

Copiamos ese contenido y lo pegamos en el campo de **Key** del formulario de
`GitHub`.
Para finalizar, presionamos sobre el botón **Add Key** y confirmamos con
nuestra clave de usuario.

Para verificar que todo funciona ejecutamos y si nos pregunta si nos queremos
seguir conectando, contestamos ``yes``:

.. code-block:: console

    $ ssh -T git@github.com
    The authenticity of host 'github.com (207.97.227.239)' can't be
    established.
    RSA key fingerprint is 16:27:ac:a5:76:28:2d:36:63:1b:56:4d:eb:df:a6:48.
    Are you sure you want to continue connecting (yes/no)? yes
    Hi lecovi! You've successfully authenticated, but GitHub does not
    provide shell access.

Con esto debería quedar funcionando nuestro SHELL con las llaves registradas. Y
vamos a poder actualizar nuestro repositorio en `GitHub` sin tener que estar
todo el tiempo ingresando la clave. Ahora tenemos que crear el repositorio en
`GitHub` y luego lo clonamos en nuestra computadora.

Creando el repositorio para el sitio
------------------------------------

En el `sitio de las páginas de github <https://pages.github.com/>`_ están
explicados los pasos a seguir para crear el repositorio necesario para publicar
con GitHub Pages.

Los pasos son los siguientes:

#. Crear un repositorio para tu usuario con el nombre: ``usuario.github.io``.

    Si tu usuario es `lecovi` vas a tener que crear un repositorio
    llamado ``lecovi.github.io``.
    Creá tu repositorio con el archivo ``README.md``, ponele una licencia que te
    parezca y agregale el archivo ``.gitignore`` con archivos de Python.

#. Clonás el repositorio con el comando:

    .. code-block:: console

        $ git clone https://github.com/lecovi/lecovi.github.io

#. Entrás a la carpeta ``lecovi.github.io`` y ahí dentro creás un archivo ``index.html`` que contenga el siguiente texto:

    .. code-block:: html

        <h1>Este es mi sitio</h1>
        <h2>lecovi</h2>

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

    Siguiente el ejemplo deberías ir a ``http://lecovi.github.io``

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
archivos de tu sitio en el home de tu usuario (``~/mis``).
También debés tener el repositorio en el home del usuario (``lecovi.github.io``).
Tenemos que mover el contenido de `mis` dentro del directorio del repositorio.

    .. code-block:: console

        $ mv ~/mis ~/lecovi.github.io

Ahora modificamos el contenido del archivo ``.gitignore`` para que el git no
esté pendiente de los nuevos archivos que Nikola necesita para crear los `html`.
Para eso, tenemos que agregar las siguientes líneas. Podés hacerlo en cualquier
lugar del archivo, pero te recomiendo que lo hagas al final del mismo.

    .. code-block:: python

        # Nikola stuff
        mis/cache/
        mis/output/
        mis/.doit.db*

Ahora tenemos que hacer un pequeño cambio en el ``conf.py``, tenemos que
decirle a Nikola que vamos a estar publicando el sitio con GitHub Pages. Para
eso alrededor de la línea 430 debés tener lo que sigue:

    .. code-block:: python

        # For user.github.io OR organization.github.io pages, the DEPLOY branch
        # MUST be 'master', and 'gh-pages' for other repositories.
        #GITHUB_SOURCE_BRANCH = 'gh-pages'
        GITHUB_DEPLOY_BRANCH = 'master'

        # The name of the remote where you wish to push to, using github_deploy.
        GITHUB_REMOTE_NAME = 'origin'

Ya estamos listos, ahora podemos publicar nuestro sitio en GitHub Pages con el
comando:

    .. code-block:: console

        $ nikola github_deploy

Ahora sólo nos resta seguir escribiendo nuestros artículos y páginas y quedarán
publicados en `http://lecovi.github.io`.

Espero que les sirva!

Nos vemos en los comentarios... :-P
