.. title: Instalando la máquina virtual
.. slug: cfp/olin/vbox-olin
.. date: 2015-08-26 15:41:01 UTC-03:00
.. tags:
.. category:
.. link:
.. description:
.. type: text

Instalar la nueva máquina virtual del curso consiste en 3 pasos:

#. Instalar VirtualBox.
#. Instalar el Pack de Extensiones de VirtualBox.
#. Importar la Máquina Virtual del Curso.

Instalando VirtualBox
=====================

Para poder virtualizar máquinas en nuestro sistema necesitamos algún software
que sepa cómo hacerlo. En este caso utilizaremos VirtualBox, un producto de
Oracle. Su sitio oficial es `<https://www.virtualbox.org/>`_. Para más
información se puede consultar el manual oficial en línea de VirtualBox:
`<https://www.virtualbox.org/manual/>`_.

.. thumbnail:: /images/olin/02-vm/01-InstalandoVBox/01-VBoxHomepage.png
    :class: align-center

Para descargar el instalador, debemos ir a la sección de Downloads. Ustedes
seguramente estarán viendo este tutorial desde una computadora con Windows. Por
lo tanto tendrán que descargar el instalador de VirtualBox para anfitriones
Windows (VirtualBox 4.X.X for Windows hosts). No importa la arquitectura de su
procesador ya que el instalador funciona para 32 y 64 bits.

.. thumbnail:: /images/olin/02-vm/01-InstalandoVBox/02-VBoxDownloads.png
    :class: align-center

Cuando hagamos click sobre el link de descarga nos preguntará dónde queremos
guardar el instalador. Por una cuestión de simpleza recomiendo dejarlo en la
carpeta de Descargas.

.. thumbnail:: /images/olin/02-vm/01-InstalandoVBox/03-Guardar_como.jpg
    :class: align-center

Una vez concluida la descarga abrimos la carpeta donde descargamos el
instalador y lo ejecutamos haciendo doble click sobre el mismo.

.. thumbnail:: /images/olin/02-vm/01-InstalandoVBox/04-ejecutar.jpg
    :class: align-center

Cuando quieran ejecutar el archivo, al menos en Windows 7, seguramente les
saldrá una advertencia de seguridad para ver si realmente quieren ejecutar el
archivo. Para poder continuar con la instalación debemos darle al botón de
"Ejecutar".

.. thumbnail:: /images/olin/02-vm/01-InstalandoVBox/05-advertencia_seguridad.jpg
    :class: align-center

Una vez completado esto, arranca el instalador. El instalador es un típico
instalador de Windows... siguiente, siguiente, siguiente, instalar. Y "voilà"!
El programa queda instalado.

.. thumbnail:: /images/olin/02-vm/01-InstalandoVBox/06-instalar1.jpg
    :class: col-md-3

.. thumbnail:: /images/olin/02-vm/01-InstalandoVBox/07-instalar2.jpg
    :class: col-md-2

.. thumbnail:: /images/olin/02-vm/01-InstalandoVBox/08-instalar3.jpg
    :class: col-md-2

.. thumbnail:: /images/olin/02-vm/01-InstalandoVBox/09-instalar4.jpg
    :class: col-md-2

.. thumbnail:: /images/olin/02-vm/01-InstalandoVBox/10-instalar5.jpg
    :class: col-md-3

Durante la instalación, saldrán algunos carteles. Según tu configuración del
UAC (User Account Control, control de cuentas de usuario)

.. thumbnail:: /images/olin/02-vm/01-InstalandoVBox/11-uac1.jpg
    :class: align-center

También para que nuestras máquinas virtuales tengan la posibilidad de
conectarse a una red, VirtualBox necesita instalar un dispositivo virtual de
controlador de red. Cuando el instalador quiera hacerlo les saldrá el aviso de
si quieren instalar. Por supuesto que para continuar con la correcta
instalación, deben aceptarlo.
Si queremos, podemos tildar la opción de "Confiar en el software de Oracle
Corporation" y no nos volverá a preguntar si deseamos instalarlo. Ya que, como
hemos contestado que confiamos en ese software, procederá a instalar.

.. thumbnail:: /images/olin/02-vm/01-InstalandoVBox/12-instalar_red1.jpg
    :class: col-md-4

.. thumbnail:: /images/olin/02-vm/01-InstalandoVBox/13-instalar_red2.jpg
    :class: col-md-4

.. thumbnail:: /images/olin/02-vm/01-InstalandoVBox/14-instalar_red3.jpg
    :class: col-md-4

Cuando termine de instalar los dispositivos, el instalador nos devolverá esta
ventana para terminar la instalación y lanzar la aplicación si deseamos.

.. thumbnail:: /images/olin/02-vm/01-InstalandoVBox/15-finish.jpg
    :class: align-center

NOTA: Si por algún motivo cuando termina el instalador, lanzan la aplicación y
le salta un cartel como el siguiente. Presionen sobre la opción "Este programa
funciona correctamente". Es simplemente un tema de que Windows no reconoce la
instalación inmediatamente después de instalado.

.. thumbnail:: /images/olin/02-vm/01-InstalandoVBox/16-advertencia_compatibilidad.jpg
    :class: align-center

Finalizado todo esto, podemos observar a continuación la pantalla de bienvenida
del VirtualBox. Este programa es el administrador de máquinas virtuales que nos
permitirá controlar las máquinas que deseemos virtualizar.

.. thumbnail:: /images/olin/02-vm/01-InstalandoVBox/17-administrador.jpg
    :class: align-center



