.. title: ¿Qué hay bajó el capó de tu máquina?
.. slug: que-hay-bajo-el-capo-de-tu-maquina
.. date: 2014-08-25 09:53:39 UTC-03:00
.. tags: arquitectura,cpu
.. category: tutorial
.. link: http://www.linuxito.com/gnu-linux/nivel-alto/386-que-hay-bajo-el-capo-de-tu-maquina
.. description:
.. type: text

Les comparto un artículo interesante sobre arquitectura de computadoras y cómo con simples comandos de consola podemos ver de qué está hecha nuestra compu.

.. class:: text-right

    Fuente Original: http://www.linuxito.com/gnu-linux/nivel-alto/386-que-hay-bajo-el-capo-de-tu-maquina

.. TEASER_END

En este artículo voy a presentar diferentes técnicas y herramientas para obtener
información detallada acerca del procesador o CPU de un sistema, como siempre
desde GNU/Linux.

Este cuatrimestre estoy desempeñándome como ayudante en la cátedra "Arquitectura
de Computadoras" para la carrera de Ingeniería en Computación. Una de las
mejores materias de la carrera si me preguntan, donde se explora a fondo el
procesador o CPU (Central Processing Unit), el corazón de todo sistema
informático. En la materia se cubre una gran cantidad de temas, desde técnicas
digitales, circuitos secuenciales, circuitos aritméticos (sumadores,
multiplicadores, divisores), pasando por pipelining, caché y memoria, hasta
otros tópicos más avanzados como ILP (paralelismo a nivel de instrucciones) y
arquitecturas múltiple issue (como superescalares y VLIW, Very Long Instruction
Word).

En fin, una cantidad importante de temas altamente interesantes para los amantes
de los fierros y la electrónica. Claro que lamentablemente muchos estudiantes
están enfocados en hacer una carrera en la industria del desarrollo de software,
por lo que estos temas les resultan aburridos, tediosos o poco interesantes (así
funciona el software después...).

Es cierto que algunos de los conocimientos más avanzados entre estos temas no se
aplicarán luego en el ámbito laboral, salvo claro que algún día terminemos
trabajando en Intel o AMD (el sueño del pibe...), por citar ejemplos. Pero es
imprescindible conocer cómo trabaja un procesador para así poder desarrollar
código eficiente, por más que se trate de código de alto nivel.

Para tratar de motivar a los alumnos, se intenta bajar a tierra estos conceptos
(pipeline, cores, frecuencia, caché, etc.) que parecen tan abstractos, perdidos
en un espacio microscópico dentro de una pastilla de silicio... O más que bajar
a tierra, abrir el capó (o cofre como llaman en otros lares) y ver que "motor"
tiene nuestra máquina, qué hay *"under the hood"*.

Información general del procesador
----------------------------------

Seguramente todos sepan cómo obtener información del procesador desde el
filesystem ``/proc`` (el pseudo-filesystem que funciona como interfaz a las estructuras de datos del kernel Linux), ya que es la forma más común y conocida:

.. code-block:: console

    [root@hal9000 ~]# cat /proc/cpuinfo
    processor       : 0
    vendor_id       : GenuineIntel
    cpu family      : 6
    model           : 42
    model name      : Intel(R) Core(TM) i3-2100 CPU @ 3.10GHz
    stepping        : 7
    cpu MHz         : 1600.000
    cache size      : 3072 KB
    physical id     : 0
    siblings        : 4
    core id         : 0
    cpu cores       : 2
    apicid          : 0
    initial apicid  : 0
    fpu             : yes
    fpu_exception   : yes
    cpuid level     : 13
    wp              : yes
    flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good xtopology nonstop_tsc aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 popcnt tsc_deadline_timer xsave avx lahf_lm arat epb xsaveopt pln pts dts tpr_shadow vnmi flexpriority ept vpid
    bogomips        : 6186.44
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 36 bits physical, 48 bits virtual
    power management:

    processor       : 1
    vendor_id       : GenuineIntel
    cpu family      : 6
    model           : 42
    model name      : Intel(R) Core(TM) i3-2100 CPU @ 3.10GHz
    stepping        : 7
    cpu MHz         : 1600.000
    cache size      : 3072 KB
    physical id     : 0
    siblings        : 4
    core id         : 1
    cpu cores       : 2
    apicid          : 2
    initial apicid  : 2
    fpu             : yes
    fpu_exception   : yes
    cpuid level     : 13
    wp              : yes
    flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good xtopology nonstop_tsc aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 popcnt tsc_deadline_timer xsave avx lahf_lm arat epb xsaveopt pln pts dts tpr_shadow vnmi flexpriority ept vpid
    bogomips        : 6186.44
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 36 bits physical, 48 bits virtual
    power management:

    processor       : 2
    vendor_id       : GenuineIntel
    cpu family      : 6
    model           : 42
    model name      : Intel(R) Core(TM) i3-2100 CPU @ 3.10GHz
    stepping        : 7
    cpu MHz         : 1600.000
    cache size      : 3072 KB
    physical id     : 0
    siblings        : 4
    core id         : 0
    cpu cores       : 2
    apicid          : 1
    initial apicid  : 1
    fpu             : yes
    fpu_exception   : yes
    cpuid level     : 13
    wp              : yes
    flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good xtopology nonstop_tsc aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 popcnt tsc_deadline_timer xsave avx lahf_lm arat epb xsaveopt pln pts dts tpr_shadow vnmi flexpriority ept vpid
    bogomips        : 6186.44
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 36 bits physical, 48 bits virtual
    power management:

    processor       : 3
    vendor_id       : GenuineIntel
    cpu family      : 6
    model           : 42
    model name      : Intel(R) Core(TM) i3-2100 CPU @ 3.10GHz
    stepping        : 7
    cpu MHz         : 1600.000
    cache size      : 3072 KB
    physical id     : 0
    siblings        : 4
    core id         : 1
    cpu cores       : 2
    apicid          : 3
    initial apicid  : 3
    fpu             : yes
    fpu_exception   : yes
    cpuid level     : 13
    wp              : yes
    flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good xtopology nonstop_tsc aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 popcnt tsc_deadline_timer xsave avx lahf_lm arat epb xsaveopt pln pts dts tpr_shadow vnmi flexpriority ept vpid
    bogomips        : 6186.44
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 36 bits physical, 48 bits virtual
    power management:

El archivo ``/proc/cpuinfo`` contiene una cantidad importante de información de
la CPU, tal como la detecta el kernel Linux. El único inconveniente es que esta
información aparece replicada para cada unidad de procesamiento, lo cual resulta
algo incómodo. Por ejemplo, si contamos con un procesador Intel Core i3, el cual
posee 2 núcleos (cores) con 2 hilos de procesamiento (threads) cada uno (4 CPUs
en total), la información aparece replicada cuatro veces.

Entre la información que se puede encontrar en el archivo ``/proc/cpuinfo``, se
lista el fabricante y modelo del procesador, la frecuencia de reloj (en este
ejemplo es 1600 MHz), el tamaño de la memoria caché (sin discriminar niveles), y
los flags (los cuales determinan las características que soporta el procesador).

Una alternativa al archivo ``/proc/cpuinfo`` consiste en utilizar la herramienta
``dmidecode`` para obtener información de la CPU desde la BIOS del sistema:

.. code-block:: console

    [root@hal9000 ~]# dmidecode -t processor
    # dmidecode 2.12
    SMBIOS 2.6 present.

    Handle 0x0004, DMI type 4, 42 bytes
    Processor Information
            Socket Designation: LGA1155 CPU 1
            Type: Central Processor
            Family: Core i3
            Manufacturer: Intel Corporation
            ID: A7 06 02 00 FF FB EB BF
            Signature: Type 0, Family 6, Model 42, Stepping 7
            Flags:
                    FPU (Floating-point unit on-chip)
                    VME (Virtual mode extension)
                    DE (Debugging extension)
                    PSE (Page size extension)
                    TSC (Time stamp counter)
                    MSR (Model specific registers)
                    PAE (Physical address extension)
                    MCE (Machine check exception)
                    CX8 (CMPXCHG8 instruction supported)
                    APIC (On-chip APIC hardware supported)
                    SEP (Fast system call)
                    MTRR (Memory type range registers)
                    PGE (Page global enable)
                    MCA (Machine check architecture)
                    CMOV (Conditional move instruction supported)
                    PAT (Page attribute table)
                    PSE-36 (36-bit page size extension)
                    CLFSH (CLFLUSH instruction supported)
                    DS (Debug store)
                    ACPI (ACPI supported)
                    MMX (MMX technology supported)
                    FXSR (FXSAVE and FXSTOR instructions supported)
                    SSE (Streaming SIMD extensions)
                    SSE2 (Streaming SIMD extensions 2)
                    SS (Self-snoop)
                    HTT (Multi-threading)
                    TM (Thermal monitor supported)
                    PBE (Pending break enabled)
            Version: Intel(R) Core(TM) i3-2100 CPU @ 3.10GHz
            Voltage: 1.7 V
            External Clock: 100 MHz
            Max Speed: 4000 MHz
            Current Speed: 3100 MHz
            Status: Populated, Enabled
            Upgrade: Socket LGA1156
            L1 Cache Handle: 0x0005
            L2 Cache Handle: 0x0006
            L3 Cache Handle: 0x0007
            Serial Number: To Be Filled By O.E.M.
            Asset Tag: To Be Filled By O.E.M.
            Part Number: To Be Filled By O.E.M.
            Core Count: 2
            Core Enabled: 1
            Thread Count: 2
            Characteristics:
                    64-bit capable

``dmidecode`` presenta casi la misma información que se encuentra en
``/proc/cpuinfo``, pero mejor organizada. Lo más interesante es que agrega la descripción de cada flag de CPU, los niveles de caché, y el voltaje de trabajo.

La herramienta ``lscpu`` tal vez presenta la salida más amigable y sintética.
Pienso que es la alternativa preferida para obtener rápidamente información
básica del procesador:

.. code-block:: console

    [root@hal9000 ~]# lscpu
    Architecture:          x86_64
    CPU op-mode(s):        32-bit, 64-bit
    Byte Order:            Little Endian
    CPU(s):                4
    On-line CPU(s) list:   0-3
    Thread(s) per core:    2
    Core(s) per socket:    2
    Socket(s):             1
    NUMA node(s):          1
    Vendor ID:             GenuineIntel
    CPU family:            6
    Model:                 42
    Stepping:              7
    CPU MHz:               1600.000
    BogoMIPS:              6186.44
    Virtualization:        VT-x
    L1d cache:             32K
    L1i cache:             32K
    L2 cache:              256K
    L3 cache:              3072K
    NUMA node0 CPU(s):     0-3

Lo que más me gusta de ésta herramienta es que, a diferencia de las anteriores,
lscpu muestra el ordenamiento de bytes del procesador (en este caso Little
Endian), discrimina los niveles de caché junto con su tamaño (recién con esta
herramienta es posible notar que este procesador utiliza caché independiente
para datos e instrucciones en L1), y muestra rápidamente que el procesador
soporta virtualización por hardware.

Memoria caché
-------------

¿Cómo es posible obtener más información acerca de la memoria caché, esa pequeña
memoria interna del procesador que se utiliza para reducir el gap de performance
entre las CPUs y la memoria principal (RAM)?

Más allá de los niveles y tamaño de cada uno es interesante conocer la
distribución y topología de cada nivel, el nivel de asociatividad, y el modo de
operación.

Una vez más es posible recurrir a la herramienta ``dmidecode``:

.. code-block:: console

    [root@hal9000 ~]# dmidecode -t cache
    # dmidecode 2.12
    SMBIOS 2.6 present.

    Handle 0x0005, DMI type 7, 19 bytes
    Cache Information
            Socket Designation: L1-Cache
            Configuration: Enabled, Not Socketed, Level 1
            Operational Mode: Write Back
            Location: Internal
            Installed Size: 32 kB
            Maximum Size: 32 kB
            Supported SRAM Types:
                    Other
            Installed SRAM Type: Other
            Speed: Unknown
            Error Correction Type: None
            System Type: Unified
            Associativity: 8-way Set-associative

    Handle 0x0006, DMI type 7, 19 bytes
    Cache Information
            Socket Designation: L2-Cache
            Configuration: Enabled, Not Socketed, Level 2
            Operational Mode: Varies With Memory Address
            Location: Internal
            Installed Size: 512 kB
            Maximum Size: 512 kB
            Supported SRAM Types:
                    Other
            Installed SRAM Type: Other
            Speed: Unknown
            Error Correction Type: None
            System Type: Unified
            Associativity: 8-way Set-associative

    Handle 0x0007, DMI type 7, 19 bytes
    Cache Information
            Socket Designation: L3-Cache
            Configuration: Enabled, Not Socketed, Level 3
            Operational Mode: Unknown
            Location: Internal
            Installed Size: 3072 kB
            Maximum Size: 3072 kB
            Supported SRAM Types:
                    Other
            Installed SRAM Type: Other
            Speed: Unknown
            Error Correction Type: None
            System Type: Unified
            Associativity: Other

Analicemos nivel por nivel. Primero L1:

.. code-block:: console

        Socket Designation: L1-Cache
        Configuration: Enabled, Not Socketed, Level 1
        Operational Mode: Write Back
        Location: Internal
        Installed Size: 32 kB
        Maximum Size: 32 kB
        Supported SRAM Types:
                Other
        Installed SRAM Type: Other
        Speed: Unknown
        Error Correction Type: None
        System Type: Unified
        Associativity: 8-way Set-associative

Se observa que el tamaño de la caché nivel 1 es de 32 kbytes. El modo de
operación es *"Write Back"*, esto significa que un bloque modificado en caché no
se escribe en memoria principal hasta que no sea desalojado de la misma (si
fuese escrito inmediatamente en memoria principal el modo de operación sería
*"Write Through"*). Luego se observa que la caché nivel 1 es unificada, aunque
como veremos más adelante al analizar la topología del procesador, no es
unificada para los 4 procesadores sino que es unificada por core. El nivel de
asociatividad es 8-way, esto significa que un bloque desde memoria principal
(más bien desde el nivel subsiguiente) puede ser ubicado en una de 8 locaciones
diferentes posibles en L1. Cuanto mayor es el nivel de asociatividad menor es la
posibilidad de conflictos de bloques, lo que implica una reducción en la tasa de
miss en caché. Como veremos más adelante, la caché L1 de este procesador (Intel
Core i3), de 32 kbytes de tamaño, puede albergar 64 bloques. Lo ideal sería que
un bloque pueda ser almacenado en cualquiera de los 64 bloques de caché
disponibles, pero esto no es alcanzable en la práctica porque aumenta
notoriamente la circuitería (se requiere de una memoria full-asociativa, es
decir direccionable por contenido en lugar de índice o dirección). Por ello
8-way set associative es un muy buen nivel de asociatividad (y me fui por las
ramas...).

Volviendo al cauce, analicemos L2:

.. code-block:: console

        Socket Designation: L2-Cache
        Configuration: Enabled, Not Socketed, Level 2
        Operational Mode: Varies With Memory Address
        Location: Internal
        Installed Size: 512 kB
        Maximum Size: 512 kB
        Supported SRAM Types:
                Other
        Installed SRAM Type: Other
        Speed: Unknown
        Error Correction Type: None
        System Type: Unified
        Associativity: 8-way Set-associative

El tamaño de L2 es de 512 kbytes, 16 veces más grande que L1. El modo de
operación varía de acuerdo a la dirección de memoria. No sé bien que significa
ésto, pero supongo que está asociado al problema de mantener la coherencia entre
cachés de diferentes cores, ya que como veremos más adelante L2 también es
unificada a nivel core (es decir, hay una caché L2 para cada core, y los threads
de cada core la comparten). Al igual que L1 es 8-way set-associative.

Finalmente, L3, el último bastión antes de tener que bajar a la terriblemente
lenta memoria RAM:

.. code-block:: console

        Socket Designation: L3-Cache
        Configuration: Enabled, Not Socketed, Level 3
        Operational Mode: Unknown
        Location: Internal
        Installed Size: 3072 kB
        Maximum Size: 3072 kB
        Supported SRAM Types:
                Other
        Installed SRAM Type: Other
        Speed: Unknown
        Error Correction Type: None
        System Type: Unified
        Associativity: Other

Este i3 posee una tremenda caché L3 de 3 megas, así como lo ven, 3 mega bytes de
caché. Esto significa que la mayoría de los transistores de la pastilla (algo
así como tres cuartos del total) se "gastan" en la caché L3. Todo para evitar
acceder a memoria RAM. El modo de operación es "Unknown", o sea, habría que
remitirse a la hoja de datos del procesador para ver si se encuentra información
más detallada acerca de cuándo se escribe un bloque modificado a memoria
principal (RAM). Y esta sí es unificada para los dos cores, y es 12-way set
associative, como ahora veremos.

Topología
---------

Si queremos saber cómo están organizados los threads, cores, y niveles de caché
del procesador, será necesario recurrir al filesystem ``/sys``. Sysfs es un
sistema de archivos virtual (a partir del kernel Linux v2.6) que exporta
información sobre los dispositivos y controladores.

Bajo la ruta ``/sys/devices/system/cpu/`` se encuentran descriptos muchos
atributos globales e individuales de cada CPU:

.. code-block:: console

    [root@hal9000 ~]# cd /sys/devices/system/cpu/
    [root@hal9000 cpu]# ls -l
    total 0
    drwxr-xr-x 8 root root    0 Jun  5 08:50 cpu0
    drwxr-xr-x 8 root root    0 Jun  5 08:50 cpu1
    drwxr-xr-x 8 root root    0 Jun  5 08:50 cpu2
    drwxr-xr-x 8 root root    0 Jun  5 08:50 cpu3
    drwxr-xr-x 3 root root    0 Jun  5 09:25 cpufreq
    drwxr-xr-x 2 root root    0 Jun  5 09:25 cpuidle
    -r--r--r-- 1 root root 4096 Jun  5 09:11 kernel_max
    -r--r--r-- 1 root root 4096 Jun  5 09:25 offline
    -r--r--r-- 1 root root 4096 Jun  5 08:20 online
    -r--r--r-- 1 root root 4096 Jun  5 09:11 possible
    -r--r--r-- 1 root root 4096 Jun  5 07:39 present
    -rw-r--r-- 1 root root 4096 Jun  5 07:38 sched_smt_power_savings

Para cada CPU existe un directorio numerado, desde `cpu0` en adelante, que
contiene información individual de cada una:

.. code-block:: console

    [root@hal9000 ~]# cd /sys/devices/system/cpu/cpu0/
    [root@hal9000 cpu0]# ls -l
    total 0
    drwxr-xr-x 6 root root    0 Jun  5 09:11 cache
    drwxr-xr-x 3 root root    0 Jun  5 09:25 cpufreq
    drwxr-xr-x 6 root root    0 Jun  5 09:25 cpuidle
    -r-------- 1 root root 4096 Jun  5 09:25 crash_notes
    drwxr-xr-x 2 root root    0 Jun  5 09:25 microcode
    lrwxrwxrwx 1 root root    0 Jun  5 09:25 node0 -> ../../node/node0
    drwxr-xr-x 2 root root    0 Jun  5 09:25 thermal_throttle
    drwxr-xr-x 2 root root    0 Jun  5 09:11 topology

Se observan directorios que describen caché, frecuencia, utilización y topología
de cada CPU. Para describir la topología existen los archivos core_siblings_list
y thread_siblings_list. Por ejemplo para cpu0:

.. code-block:: console

    [root@hal9000 cpu0]# cat topology/{core_siblings_list,thread_siblings_list}
    0-3
    0,2

Esto significa que cpu0 convive en el mismo socket (pastilla) que cpu1, cpu2 y
cpu3, de acuerdo al contenido de core_siblings_list (0-3). Y está dentro del
mismo core que cpu2 (0,2).

De esta forma podemos ver la relación entre cada CPU a nivel core:

.. code-block:: console

    [root@hal9000 ~]# cd /sys/devices/system/cpu/
    [root@hal9000 cpu]# cat cpu{0..3}/topology/thread_siblings_list
    0,2
    1,3
    0,2
    1,3

Respecto a la memoria caché, en los directorios cache dentro de cada directorio `cpui` existe un índice para cada nivel. Por ejemplo para cpu0:

.. code-block:: console

    [root@hal9000 ~]# cd /sys/devices/system/cpu/cpu0/cache/
    [root@hal9000 cache]# ls -l
    total 0
    drwxr-xr-x 2 root root 0 Jun  5 09:11 index0
    drwxr-xr-x 2 root root 0 Jun  5 09:11 index1
    drwxr-xr-x 2 root root 0 Jun  5 09:11 index2
    drwxr-xr-x 2 root root 0 Jun  5 09:11 index3

A pesar de que la caché está estructurada en 3 niveles (L1, L2, y L3), en este
directorio aparecen 4 índices. Esto se debe a que discrimina correctamente L1
según su tipo, ya que está separada en caché L1 para instrucciones y caché L1
para datos:

.. code-block:: console

    [root@hal9000 cache]# cat index{0,1}/level
    1
    1

Además ambas caché L1 se comparten en cada core (por eso L1 figura como caché
unificada en la salida de `dmidecode`):

.. code-block:: console

    [root@hal9000 cache]# cat index{0,1}/{type,shared_cpu_list}
    Data
    0,2
    Instruction
    0,2

Claramente no son unificadas para todas las CPU:

.. code-block:: console

    [root@hal9000 ~]# cd /sys/devices/system/cpu/
    [root@hal9000 cpu]# cat cpu{0..3}/cache/index{0,1}/{type,shared_cpu_list}
    Data
    0,2
    Instruction
    0,2
    Data
    1,3
    Instruction
    1,3
    Data
    0,2
    Instruction
    0,2
    Data
    1,3
    Instruction
    1,3

Al igual que L1, L2 es unificada a nivel siblings, y L3 es unificada a nivel core (para todas las CPU):

.. code-block:: console

    [root@hal9000 ~]# cd /sys/devices/system/cpu/cpu0/cache/
    [root@hal9000 cache]# cat index{0,1,2,3}/{level,type,shared_cpu_list}
    1
    Data
    0,2
    1
    Instruction
    0,2
    2
    Unified
    0,2
    3
    Unified
    0-3

Con todos estos datos es posible describir la topología de un Intel Core i3.
Intel Core i3

¿Por qué separa a L1 en caché para instrucciones y caché para datos? Para
minimizar los conflictos de alocación de bloques en caché (por la "baja"
asociatividad), y para que la etapa de fetch de la instrucción no compita por el
recurso con las instrucciones load/store.

Finalmente había quedado pendiente ver la cantidad de bloques y nivel de
asociatividad de cada nivel de caché (según dmidecode el nivel de asociatividad
de L3 era "Other"):

.. code-block:: console

    [root@hal9000 ~]# cd /sys/devices/system/cpu/cpu0/cache/
    [root@hal9000 cache]# cat index{0,1,2,3}/{number_of_sets,ways_of_associativity}
    64
    8
    64
    8
    512
    8
    4096
    12

Se observa que L1 puede albergar 64 bloques y es 8-way associative, tanto para
instrucciones (L1i) como para datos (L1d). L2 puede albergar 512 bloques y
también es 8-way associative. Y L3 alberga 4096 bloques y es 12-way associative.
Por supuesto L1i, L1d y L2 están replicadas para cada core, ya que en este
volcado estamos analizando una única CPU (cpu0).

¡Espero que les haya gustado!
