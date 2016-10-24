.. title: Flask Web Forms
.. slug: ifts/edd/flask-forms
.. date: 2015-08-26 15:18:41 UTC-03:00
.. tags:
.. category:
.. link:
.. description:
.. type: text

Web Forms
===================

Los web forms son elementos html de formulario para enviar datos al backend (servidor). Por ejemplo, inicios de sesion, consultas, contactos.

El form lleva el atributo action que le indica a qué archivo(script) hace referencia.

.. code-block:: html

    <form action="action_page.php" method="post">

Las peticiones y la información van desde el cliente al backend, hay dos maneras de enviarlo:

GET y POST
---------------

El metodo por defecto es el GET, pasa informacion al servidor a través de la url (action + la concatenacion de las variables que le paso a la funcion)

POST, viaja en el cuerpo del paquete, no en la url, no es visible al cliente

.. TIP::

    Para elejir que tipo de metodo debes tener en cuenta:

    - qué tipo de info voy a mandar/necesitar?
    - a dónde, qué acción ?

Elementos dentro de un form
------------------------------
Los elementos básicos que tiene que tener un formulario para que responda como tal son

    - Inicio y fin de la etiqueta <form>
    - Atributo en esa etiqueta del método y el script
    - Al menos un elemento de tipo texto, radio, checkbox, email, password, etc.
    - Botón de <submit> para enviar el formulario

.. |w3schools| raw:: html

    <a href="http://www.w3schools.com/html/html_forms.asp" target="_blank">w3schools.com formularios</a>

.. TIP::
    podes consultar más sobre esto y otras etiquetas en |w3schools| 
