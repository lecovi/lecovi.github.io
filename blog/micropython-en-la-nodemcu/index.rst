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
poco con micropython, así que decidimos empezar usando la nodemcu_.

Les voy a contar cómo instalar micropython_ en la
placa, cómo conectarse y jugar con el led integrado. Manos a la obra!

Qué necesitamos
---------------

Para seguir el artículo vamos a necesitar:

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

.. image:: /images/blog/upython/flashing.png
    :scale: 50 %
    :alt: Flasheando la nodemcu
    :class: align-center

Conectándose a la `nodemcu` con ``picocom``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ahora con ``picocom`` (o ``minicom`` o el que más te guste) con la placa
conectada al USB ejecutás:

.. code-block:: bash

    sudo picocom /dev/ttyUSB0 -b115200

Si tenés permisos sobre el dispositivo USB el `picocom` se va a conectar a la
placa sin ningún tipo de problemas. Luego del mensaje ``Terminal ready``
presionamos la tecla `enter` y tendremos que ver el prompt del REPL de Python
``>>>`` y *voilà!*, micropython está instalado y funcionando en la `nodemcu`.

Fácil! Verdad?

.. image:: /images/blog/upython/picocom.png
    :scale: 50 %
    :alt: conexión usando picocom
    :class: align-center

Un paso más
-----------

Probemos que nuestra instalación de micropython funciona correctamente.
Escribamos el famoso `Hola Mundo!`.

.. code-block:: python3

    >>> print("Hola nodemcu")
    Hola nodemcu
    >>> 34 + 5
    39
    >>>

Que se haga la luz!
~~~~~~~~~~~~~~~~~~~

Genial! Todo funciona de maravillas. Hagamos algo un poco más interesante.
Prendamos el led que tiene la placa.

.. code-block:: python3

    >>> import machine
    >>> led = machine.Pin(2, machine.Pin.OUT)
    >>> led.off()
    >>> led.on()
    >>> led.off()
    >>>

Impecable! Todo funciona de maravillas. Ahora hagamos parpadear al led...

.. code-block:: python3

    >>> import time
    >>> for i in range(5):
    ...     led.off()
    ...     time.sleep(0.5)
    ...     led.on()
    ...     time.sleep(0.5)
    ...
    ...
    ...
    >>>

.. image:: /images/blog/upython/repl.png
    :scale: 50 %
    :alt: usando el intérprete de micropython
    :class: align-center

Conectate!
~~~~~~~~~~

Hagamos esto un poco más interesante. Conectémonos a la red WiFi de casa.

.. code-block:: python3

    >>> import network
    >>> iface = network.WLAN(network.STA_IF)
    >>> iface.active()
    False
    >>> iface.active(True)
    #5 ets_task(4020ed88, 28, 3fff9f90, 10)
    >>> iface.active()
    True
    >>> iface.connect('ThiagoBenjamin', '<escribí-tu-clave>')
    >>> iface.isconnected()
    True
    >>> iface.ifconfig()
    ('192.168.1.13', '255.255.255.0', '192.168.1.1', '192.168.1.1')
    >>>

done!

Referencias:
------------

- `Instalando Micropython en la nodemcu - Prometec <https://www.prometec.net/micropython-nodemcu/#>`_
- `Micropython - Official Site | Downloads <http://micropython.org/download>`_
- `Documentación oficial Micropython <http://docs.micropython.org/en/latest/esp8266/index.html>`_
- `NodeMCU con Micropython - Maker Edition <http://www.makeredition.com/micropython-y-nodemcu/>`_
- `Getting started with a fresh NodeMCU ESP8266 <http://baitisj.blogspot.com.ar/2015/10/one-minute-tutorial-getting-started.html>`_
- `MicroPython and the NodeMCU ESP8266 <https://www.kenwalger.com/blog/iot/micropython-and-nodemcu-esp8266/>`_
- `Blink LED - Adafruit <https://learn.adafruit.com/micropython-basics-blink-a-led/blink-led>`_

