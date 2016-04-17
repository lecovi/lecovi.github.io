.. title: Instalar Chromium browser
.. slug: instalar-chromium-browser
.. date: 2013-03-10 12:27:46 UTC-03:00
.. tags: chromium
.. category: tutorial
.. link:
.. description:
.. type: text

Si querés tener en tu linux la versión libre de Chrome, tenés que instalarte Chromium. De hecho, Chrome está basado en Chromium sólo que le agrega los componentes no libres de Google.

.. TEASER_END

Instalemos Chromium en 4 pasos
------------------------------

#. Afortunadamente el Chromium se encuentra en los repositorios de nuestro sistema LMDE. Para poder instalarlo debemos ir al `Menu --> Gestor de Software`. |1|
#. En el cuadro de búsqueda escribimos "``chromium``". |2|
#. Hacemos doble click sobre el primer resultado que nos aparece (el mismo que vemos en la imagen anterior). |3|
#. Y apretamos sobre el botón de "`instalar`". Una vez finalizado el proceso, dentro de `Menu --> Internet --> Chromium` podremos encontrar el acceso a este navegador. |4|

.. |1| image:: /images/blog/chromium/InstalaChromium1.png
    :scale: 50 %
    :alt: Abrir gestor de software
    :class: align-center

.. |2| image:: /images/blog/chromium/InstalaChromium2.png
    :scale: 50 %
    :alt: Buscamos chromium
    :class: align-center

.. |3| image:: /images/blog/chromium/InstalaChromium3.png
    :scale: 50 %
    :alt: Seleccionamos el paquete
    :class: align-center

.. |4| image:: /images/blog/chromium/InstalaChromium4.png
    :scale: 50 %
    :alt: Instalamos!
    :class: align-center

Instalamos en 1 paso
--------------------

También podemos instalarlo vía la consola ejecutando:

.. code-block:: console

    $ sudo apt update && sudo apt install chromium-browser
