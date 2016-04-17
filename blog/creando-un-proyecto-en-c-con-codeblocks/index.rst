.. title: Creando un proyecto en C con Code::Blocks
.. slug: creando-un-proyecto-en-c-con-codeblocks
.. date: 2014-08-24 09:10:59 UTC-03:00
.. tags: programacion
.. category: tutorial
.. link:
.. description:
.. type: text

Veamos cómo crear un proyecto de C en ``Code::Blocks``.

.. TEASER_END

Pasos a seguir
--------------

.. class:: text-center

    .. youtube:: V7S1QRXmOg8


#. Abrimos ``Code::Blocks``.
#. Vamos al menú `File --> New --> Project...`
    - Esto nos abrirá un cuadro de diálogo que nos asistirá en el proceso de creación de nuestro proyecto.
#. En el cuadro de diálogo elegimos `Console Application` y luego apretamos el botón que dice `Go`.
    - Esto nos permitirá elegir las opciones de la aplicación que estamos por desarrollar
#. En la primer pantalla apretamos el botón de Next, NO tildar la opción de `Skip this page next` time sino la próxima vez no podremos editar estas opciones al momento de crear el proyecto.
#. Ahora debemos seleccionar el lenguaje que utilizaremos para nuestro desarrollo. En nuestro caso, SIEMPRE será **``C``**. NUNCA utilizaremos **``C++``**. Por lo que debemos cambiar la opción por defecto. Elegimos la opción que dice **``C``** y presionamos el botón `Next`.
#. En la siguiente pantalla podremos elegir el nombre del proyecto y el destino en el sistema de archivos. En este caso elegimos:
    - `Project Title` (Título del Proyecto): Proyecto1.
    - `Folder to create project in` (Carpeta donde crear el proyecto): ``/home/alumno/Documentos/Proyectos_CB/``
        + Esto es equivalente a `Carpeta Personal --> Documentos --> Proyectos_CB`
    - `Project filename` (Nombre de archivo del proyecto): NO TOCAR.
        + Con lo que resultará en: `Carpeta Personal --> Documentos --> Proyectos_CB --> Proyecto1`
    - `Resulting filename` (Nombre de archivo final): NO TOCAR.
        + Finalmente: `Carpeta Personal --> Documentos --> Proyectos_CB --> Proyecto1 --> Proyecto1.cbp`
    - Presionamos el botón de `Next`.
#. Ahora en la última opción, nos deja cambiar las opciones del compilador. Dejamos las opciones por defecto, y presionamos `Next`:
    - `GNU GCC Compiler`
    - `Create "Debug" configuration`
    - `Create "Release" configuration`
#. Esto creará el Proyecto dentro de nuestro espacio de trabajo (Workspace). Desplegamos la carpeta `Source` y dentro encontraremos el archivo ``main.c``. En el mismo simplemente encontraremos una versión del clásico ``"Hola Mundo"``. Desde el menú `Build` ejecutamos la opción `Build and Run` para verificar que se compila y ejecuta nuestro código.
    - Eso nos abrirá una terminal que ejecuta el código.

.. class:: text-center

    .. youtube:: 1IMlRHok5N0
