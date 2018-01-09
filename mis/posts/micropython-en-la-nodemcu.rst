.. title: Micropython en la nodemcu
.. slug: micropython-en-la-nodemcu
.. date: 2018-01-09 11:45:06 UTC-03:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text

.. _bitson: http://bitson.group

.. _nodemcu: http://www.nodemcu.com/index_en.html

.. _micropython: http://micropython.org/

En bitson_ se nos ocurrió que podíamos empezar a jugar un
poco con micropython, así qeu decidimos empezar usando la nodemcu_.

Les voy a contar cómo instalar micropython_ en la
placa, cómo conectarse y jugar con el led integrado. Manos a la obra!

Qué necesitamos
---------------

Para seguir este artículo vamos a necesitar:

- nodemcu
- ``picocom``
- ``esptool``
- `firmware`

Instalando ``picocom``
~~~~~~~~~~~~~~~~~~~~~~

Para Fedora:

.. code-block:: bash

    sudo dnf install picocom

Para Debian y derivados:

.. code-block:: bash

    sudo apt install picocom

Instalando ``esptool``
~~~~~~~~~~~~~~~~~~~~~~

    Es conveniente instalarlo con el flag ``--user`` para que no quede
    instalado entre los paquetes del sistema. Pero tenés que asegurarte que tu
    usuario tenga permisos para acceder a los dispositivos serie
    (`/dev/ttyUSB`).

.. code-block:: bash

    pip install esptool

Descargar el `firmware`
~~~~~~~~~~~~~~~~~~~~~~~

La última versión estable del `firmware` la podés encontrar en
http://micropython.org/download en la sección **Firmware for ESP8266 boards**
te descargás el binario para flashear la placa.

    Al momento de escribir este artículo:
    http://micropython.org/resources/firmware/esp8266-20171101-v1.9.3.bin

Flasehando la `nodemcu`
~~~~~~~~~~~~~~~~~~~~~~~

Ahora que tenemos todo listo vamos a borrar la flash de la placa y depsués a
cargar el nuevo firmware con ``esptool``.

#. Conectar la placa con un cable microUSB.
#. ``esptool.py --port /dev/ttyUSB0 erase_flash``
#. ``esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20171101-v1.9.3.bin``

Conectándose a la `nodemcu` con ``picocom``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ahora con ``picocom`` (o ``minicom`` o el que más te guste) con la placa
conectada al USB ejecutás:

.. code-block:: bash

    sudo picocom /dev/ttyUSB0 -b115200


