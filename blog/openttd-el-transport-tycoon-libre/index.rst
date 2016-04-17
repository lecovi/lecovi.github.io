.. title: OpenTTD: el Transport Tycoon libre!
.. slug: openttd-el-transport-tycoon-libre
.. date: 2014-08-22 13:22:29 UTC-03:00
.. tags:
.. category:
.. link:
.. description:
.. type: text

|openttd| es un juego gratuito y con licencia libre en el que un jugador crea su propia **compañía de transportes** partiendo de un presupuesto inicial, eligiendo entre diferentes **mapas** donde establecerse y utilizando su **flota de camiones, trenes, barcos y aviones** para transportar mercancías y hacer más dinero con el que expandir las diferentes infraestructuras (como carreteras, vias de tren, aeropuertos, etc..) así como adquirir nuevos equipos y tecnologías de transporte.

.. |openttd| raw:: html

    <a href="http://www.openttd.org/en/" target="_blank">
    OpenTTD
    </a>

.. TEASER_END

.. image:: /images/blog/openttd-game.jpg
    :scale: 50 %
    :alt: OpenTTD Game screenshot
    :class: align-center

Ahora acaba de salir la versión 1.4.2, así que puede ser un buen momento para probar este openTTD, surgido como un *clon* del popular juego de Microsoft  *“Transport Tycoon Deluxe“*, al que en los últimos años se han añadido constantemente **nuevas características y mejoras**.

Algunas de ellas tan significativas como el aumento en el tamaño de los **mapas**, modo **multijugador** para hasta 255 jugadores, nuevos elementos como **embarcaderos, canales o acueductos,** la posibilidad de **construir** en laderas y costas (parece que la ley de protección de costas no nos afecta demasiado) y posiblemente ligado con lo anterior ahora también **podemos sobornar a las autoridades** de la ciudad (a muchos políticos en España les gusta esto ;-) ), algo que seguramente nos ayudará a la hora de enfrentarnos a empresas rivales.

Los desarrolladores también han conseguido que prácticamente todas las herramientas de este **simulador** de transportes, integren la función de **arrastrar y soltar**, soporte para color *32 bits*, y la posibilidad de hacer zoom con la rueda del ratón.

OpenTTD está disponible para BSD, (especialmente FreeBSD, NetBSD y  OpenBSD) Linux, Solaris, Windows y plataformas móviles como iOS, Windows Mobile o |android|.

.. |android| raw:: html

    <a href="https://play.google.com/store/apps/details?id=org.openttd.sdl" target="_blank">
    Android
    </a>

Si os decidís a instalarlo no esperéis grandes gráficos, espectaculares efectos 3D o maravillosa música, porque eso no es el fuerte de este juego. Lo que si vais a poder encontrar es un interesante juego de estrategia en tiempo real, con una excelente |documentación| y |tutoriales| disponibles en castellano.

.. |documentación| raw:: html

    <a href="http://wiki.openttd.org/P%C3%A1gina_principal/Es" target="_blank">
    documentación
    </a>

.. |tutoriales| raw:: html

    <a href="https://wiki.openttd.org/Tutorial/Es" target="_blank">
    tutoriales
    </a>

Hablando de instalar… en la web de descargas del programa encontraréis la última versión disponible en paquetes deb para Debian y Ubuntu, así como en código fuente.

.. |paquete| raw:: html

    <a href="http://www.openttd.org/en/download-stable" target="_blank">
    paquetes deb
    </a>

Nota:

Si no te funciona la música, posiblemente sea porque no tenés instalado el paquete que reproduce los midi. Para solucionar esto basta que en Debian instales el paquete ``timidity``. Para eso, como root o con `sudo`:

.. code-block:: console

    # apt-get install timidity
