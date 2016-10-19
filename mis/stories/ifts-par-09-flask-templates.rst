.. title: Flask Templates
.. slug: ifts/par/flask-templates
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
        - Conocer las etiquetas HTML5 más utilizadas.
        - Usar el sistema de plantillas HTML que utiliza Flask para armar las páginas web de una aplicación.
        - Conocer la sintáxis de Jinja2.

Etiquetas HTML5
===============

Las etiquetas HTML son elementos con nombre encerrados por los símbolos de mayor (``<``) y menor (``>``):

.. TIP::

    ``<nombre>contenido...</nombre>``

Consideraciones:

- La mayoria de las etiquetas se usan de a pares, por ejemplo: ``<p>`` y ``</p>``.
- Se las llaman `etiqueta de apertura` y `etiqueta de cierre` respectivamente.
- La etiqueta de cierre se escribe igual que la de apertura, pero el nombre comienza con barra (``/``).
- Si bien HTML no es sensible a las mayúsculas y minúsculas, las buenas prácticas dicen que las etiquetas deben escribirse con minúscula.
- Todas los documentos HTML consisten en elementos HTML anidados.

.. WARNING::

    No hay que olvidarse las etiquetas de cierre.

.. |w3schools| raw:: html

    <a href="http://www.w3schools.com/html/default.asp" target="_blank">w3schools.com</a>

Estructura de un documento HTML
-------------------------------

Un excelente lugar para aprender HTML5 es |w3schools|. El documento más simple
que podemos armar en HTML5 es:

.. listing:: par/encabezados.html html

.. image:: /images/par/estructura_html.png
    :class: align-center

.. TIP::

    - Todos los elementos que están dentro de la etiqueta ``<body>`` son los que vemos en el navegador web.
    - El elemento ``<head>`` es un contenedor de metadata. La metadata HTML es información sobre el documento HTML en sí. La metadata no se muestra en el navegador web.

Atributos HTML
~~~~~~~~~~~~~~

- Todos los elementos HTML pueden tener atributos.
- Los atributos proveen información adicional sobre los elementos.
- Los atributos siempre van dentro de la etiqueta de apertura.
- Los atributos usualmente vienen en pares `nombre-valor`, como: ``name="value"``.

Enlaces
-------

.. listing:: par/enlaces.html html

Imágenes
--------

.. listing:: par/imagenes.html html

Reglas horizontales
-------------------

.. listing:: par/hr.html html

Texto preformateado
-------------------

.. listing:: par/pre.html html

Formateando elementos
---------------------

.. listing:: par/format.html html

Tooltip
-------

.. listing:: par/tooltip.html html

Comentario
----------

.. listing:: par/comentario.html html

Plantillas de Flask
===================

Flask devuelve un HTML
----------------------

.. listing:: par/routes2.py python3

Flask renderiza una plantilla
-----------------------------

.. listing:: par/routes3.py python3

.. listing:: par/user.html html

Estructuras de control en las plantillas
----------------------------------------

.. listing:: par/routes4.py python3

.. listing:: par/users.html html
