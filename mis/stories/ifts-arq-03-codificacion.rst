.. title: Codificación de Datos
.. slug: ifts/arq/codificacion
.. date: 2015-08-26 15:18:41 UTC-03:00
.. tags:
.. category:
.. link:
.. description:
.. type: text

Definiciones:
=============

:DATOS: conjunto de símbolos que representan un objeto concreto o abstracto.

:INFORMACIÓN:
    es el resultado que se obtiene al procesar los datos. Es decir, darle
    significado a los datos, son interpretados y relacionados dentro de un
    contexto. La información disminuye la incertidumbre al momento de tomar
    decisiones.
    Por ejemplo si decimos 38°C → ¿día de mucho calor o fiebre?

:SISTEMA DE INFORMACIÓN:
    se utiliza para referirse al conjunto coordinado de elementos, datos y
    procesos cuya interacción permite la obtención de información.

¿Qué significa procesar datos?
------------------------------

* Cálculo
* Comparación
* Clasificación (ordenamientos, intercalaciones)
* Transformación (ej: datos numéricos → gráficos)
* Transferencia (comunicación)
* Almacenamiento (para utilización posterior)
* Consulta (de datos almacenados)

Representación de datos
-----------------------

* Sistema binario
* Sistema octal
* Sistema hexadecimal
* Sistemas codificados:
    - 5 bits: Código Baudot – 1874. Utilizado en teletipos (tty) principios s.XX
    - 6 bits: FIELDATA – 1956 al 62. US Army
    - 7 bits: ASCII – 1963. ANSI estandarización internacional.
    - 8 bits:
            + ASCII Extendido – (IBM) 1981.
            + EDCDIC: mainframes IBM. No es estandar. “Signo Austral”.
    - Unicode: 1991. Estandar. ISO/IEC (International Organization for Standardization/International Electrotechnical Commission)

    - Codificación Números:
        + BCD Natural: (8421) – Error de 10 a 15 en binario. Sumar (suma 6 – 0110).
        + BCD Aiken: (2421) – Simetría – Autocomplementable.
        + BCD Xs3: Sin pesos – Simetría – Autocomplementable.

Algunos Sitios Interesantes:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ACM - Assotiation for Computing Machinery (http://www.acm.org)
* CPCI - Consejo Profesional en Ciencias Informáticas (http://www.cpci.org.ar)
    - Prov. Bs. As. – http://www.cpciba.org.ar/
    - Prov. Córdoba – http://www.cpcipc.org.ar//portal/index.php?option=com_content&task=view&id=17&Itemid=33
