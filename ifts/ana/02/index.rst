.. title: Sistemas
.. slug: ifts/ana/02
.. date: 2016-04-09 10:50:49 UTC-03:00
.. tags:
.. category:
.. link:
.. description:
.. type: text

.. class:: alert alert-info pull-right

.. contents::

Es el estudio de un problema que antecede a la toma de una acción en el ámbito Informático. Se refiere al estudio de un área de trabajo o de una aplicación, que conduce casi siempre a la especificación de un nuevo sistema y su posterior diseño. La acción posterior se refiere a la implementación del sistema.

Clasificación de los sistemas
=============================

- Sistemas naturales: No hechos por el hombre.
- Sistemas efectuados por el hombre

Sistemas Naturales
------------------

- Sistemas físicos.
- Sistemas estelares: galaxias, sistemas solares.
- Sistemas geológicos: ríos cordilleras.
- Sistemas moleculares: organizaciones complejas de átomos.
- Sistemas vivientes: Miller llegó a catalogar a los sistemas vivos sean estos de nivel celular o un sistema supraracional, y a dividirlos en los siguientes subsistemas:
    + Reproductor: capaz de crear otro sistema semejante. Analogía: planeamiento + Delimitador: mantiene la cohesión de los componentes y los protege de problemas ambientales, permitiendo o impidiendo la entrada de informaciones. Analogía seguridad o control de ingreso.

Sistemas Hechos por el Hombre
-----------------------------

- Sistemas sociales: Organizaciones de ley, Doctrinas costumbres.
- Colecciones organizadas y disciplinadas de ideas: Sistema decimal o sistema de organización de biblioteca.
- Sistemas de transportes: Sistemas de rutas, canales líneas aéreas, petroleros.
- Sistemas de comunicaciones: teléfonos telex, señales para el público.
- Sistemas de manufacturas: Fábricas.
- Sistemas financieros: Contabilidad Inventario.

Sistemas Automatizados
----------------------

Son sistemas hechos por el hombre controlados por computadoras. Sus componentes principales son:

- Hardware: CPU, terminales e impresoras
- Software: Sistemas operativos, Sistemas de aplicación, Sistema de Base de datos
- Personas: Operadores que proveen entradas y utilizan salidas
- Datos : Las informaciones que el sistema conserva por un período de tiempo.
- Procedimientos: Instrucciones y determinaciones para la operación del Sistema.


Clasificación:
~~~~~~~~~~~~~~

- Sistemas en línea
- Sistemas en tiempo real
- Sistemas de apoyo a decisiones y Sistemas de planeación estratégica
- Sistemas basados en el conocimiento

Sistemas En Línea
+++++++++++++++++

Son aquellos que aceptan material de entrada directamente del área donde se creó. También es el sistema en el que el material de salida, o el resultado de la computación, se devuelven directamente a donde es requerido.
Los datos pueden ser modificados o recuperados o ambas cosas (rápidamente) y sin tener que efectuar accesos a otros componentes de información del sistema.
Yourdon : En línea versus en lote?. Confusión con sistemas en tiempo real?
"Sistemas en línea:" Interactivo, Es decir el analista debe tener alguna manera de modelar diferentes estados. Rapidez en la recuperación de la información.

Sistemas en Tiempo Real
+++++++++++++++++++++++
*James Martín*
Un sistema computacional de tiempo real puede definirse como aquel que controla un ambiente recibiendo datos, procesándolos y devolviéndolos con la suficiente rapidez como para influir en dicho ambiente en ese momento.
Algunos autores utilizan indistinto con el sistema en línea.
Otros autores asocian la definición a tiempo de respuesta (el intervalo transcurrido entre que el operador oprimió la última tecla y la respuesta del sistema al evento).

*E. Yourdon.*
Interactúan con el ambiente y no con personas.
Problema sustentado sobre el tiempo real, que por falta de tiempo adecuado no queden cosas fuera de control
Interés marcado en el comportamiento tiempo-dependiente del sistema. Importancia de la utilización de los diagramas de transición de estados.
Muchas actividades simultáneas: se deben establecer prioridades Debe contemplarse interrupciones de actividades de baja prioridad, para dar lugar a una alta
Existen comunicaciones extensivas entre tareas
Acceso simultáneo a datos de uso común
Uso dinámico y almacenamiento en memoria de alta velocidad-

Sistemas de Apoyo a la Decisión
+++++++++++++++++++++++++++++++

Son sistemas de procesamiento que no toman decisiones por sí mismo, pero que auxilian a los gerentes y otros profesionales de una organización a tomar decisiones inteligentes y bien informadas en varios aspectos de las operaciones de la organización. Ej.. Planilla electrónica
Algunos son útiles para articular y mecanizar las reglas utilizadas para llegar a alguna decisión de negocios. El usuario debe identificar los criterios que se utilizaran para tomar la decisión, Algunos de ellos son binarios, otros deben transformarse a binarios en el diseño.De acuerdo a la prioridad se le puede dar "pesos" para que vayan definiendo criterios que conduzcan a alternativas que puedan ser evaluadas y analizadas.

Sistemas de planeación estratégica
++++++++++++++++++++++++++++++++++
Son utilizados por los gerentes para evaluar y analizar la misión de la organización. Estos sistemas ofrecen acerca de alguna decisión de negocios aislada, estos sistemas ofrecen consejos más amplios y generales acerca de la naturaleza del mercado, preferencias de consumidores, comportamiento de la competencia, etc..

Sistemas Basados en el Conocimiento
+++++++++++++++++++++++++++++++++++
También llamados Sistemas Expertos, Sistemas Especialistas (tienen embebido el conocimiento y la capacidad que le permiten funcionar como especialistas en base al conocimiento de especialistas humanos). Sistemas de Inteligencia artificial, Redes Neuronales (sistemas que pretenden emular el pensamiento del ser humano actuando y aprendiendo de sus errores). Lenguaje como el PROLOG o el LISP son lo más utilizados en esta área.

**¿Por qué no debieran automatizarse algunos sistemas de procesamiento de información?**

- **Costo:** Puede ser más barato continuar llevando a cabo las funciones y almacenando la información del sistema en forma manual.
- **Conveniencia:** Puede ocupar demasiado espacio, hacer ruido o consumir mucha electricidad.
- **Seguridad:** Puede el usuario creer que la información está más segura sólo si físicamente está bajo llave y en papel.
- **Facilidad de mantenimiento:** conocido por todos.
