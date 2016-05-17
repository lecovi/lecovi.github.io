.. title: Como NO realizar una práctica de programación
.. slug: como-no-realizar-una-practica-de-programacion
.. date: 2013-03-20 10:11:40 UTC-03:00
.. tags: programacion
.. category:
.. link: http://www.agustincernuda.info/noprog_ESP.html
.. description:
.. type: text

Agustín Cernuda nos comparte algunas recomendaciones al momento de ponernos a estudiar programación por primera vez.

----

.. TEASER_END

.. class:: alert alert-info pull-right

.. contents::

Inevitablemente, los alumnos (¡y muchos profesionales!) repiten ciertos patrones de comportamiento muy nocivos al hacer prácticas de programación. Este documento pretende recoger los peores hábitos, reunirlos, y presentarlos de forma que un alumno (¡o un programador profesional!) pueda identificarlos fácilmente y evitarlos. Si su intención es poner a prueba al profesor, sin embargo, no debería evitarlos, sino seguir estas instrucciones al pie de la letra.

Quiero dejar constancia de que esta página, aunque esté escrita en tono relativamente jocoso y exagerado (con el fin de hacer más llevadera su lectura y desdramatizar), no pretende en modo alguno ser una burla hacia los alumnos, hacia los que siento un gran respeto. Gran parte de esta página la he escrito por el simple mecanismo de ridiculizarme a mí mismo, ya que en un momento u otro he cometido muchas de estas faltas, y las entiendo muy bien. Otras me parecen increíbles, pero en fin... El caso es que sólo se pueden evitar con cierta disciplina, y darse cuenta de lo absurdos que son ciertos comportamientos puede ser una buena forma de adquirir esa disciplina (el miedo al ridículo hace milagros).

De la programación propiamente dicha
------------------------------------

Ignora los mensajes de error
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Los compiladores, los sistemas operativos, etc. emiten mensajes de error sólo para que los usen sus creadores, o para justificar sus sueldos.

Leer esos mensajes, además, lleva un tiempo precioso que se podría dedicar a escribir más código, por lo que atentan contra nuestra productividad.

Y por último, para entender esos mensajes hacen falta conocimientos informáticos -cosa que no debemos cultivar, ya que en realidad todos estamos estudiando para jefes-, y encima... ¡la mayoría de las veces esos mensajes están en inglés! No caigas en la trampa. Ignóralos.

Ignora las advertencias, *"warnings"* o *"hints"*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Al igual que en el caso de los errores, estos mensajes son difíciles de entender (por lo menos más difíciles que los mensajes cortos de los móviles), y encima suelen estar en inglés.

Es más, ignorar los "warnings" le da a uno una pátina de programador profesional que no tiene miedo de los ordenadores. ¿Qué mejor demostración de madurez como programador que presentar un programa que al compilar da decenas, no, cientos de warnings, sin que su autor se inmute? Se nota que es un programador experimentado, que no se amilana por nada, y que además está demasiado ocupado para perder el tiempo con tonterías.

Escribe el código directamente sin pensar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Al final, no nos engañemos. ¿Qué es lo que estamos construyendo? Un programa. ¿Qué es lo único imprescindible en un programa? El código. ¿Qué es lo que de verdad funciona? El código. No hay que perder ni un minuto en usar medios arcaicos como lápices, bolígrafos o papel. Tú eres un miembro de pleno derecho de la generación WAP. No haces el ridículo escribiendo costosas sílabas, ¿verdad? Pues no hagas el ridículo pensando en nada, cuando hay tanto código por escribir.

Cuanto antes te quites de enmedio este rollo de programar, mejor. Y eso, muñeco, sólo lo puedes acelerar escribiendo más y más líneas.

Aunque el código no compile o no funcione, sigue escribiendo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Es sabido que los mensajes de error son una interrupción inadmisible, una traba estúpida a nuestro trabajo. ¿Qué puedes hacer si tienes un error de compilación? Ya hemos visto que leérselo y comprenderlo no es una opción válida.

Se puede intentar hacer algún cambio aleatorio en el código fuente, a ver si hay forma de engañar a ese estúpido compilador. Pero si eso no funciona, no pierdas más tiempo. NO, no caigas en la tentación de leer el mensaje de error o intentar comprenderlo (tú tienes un prestigio al que te debes). Sigue escribiendo código, que es de lo que se trata para acabar con esta asquerosa asignatura. Más adelante, ya arreglarás el error. Es sabido, además, que los errores tienden a desaparecer solos con el tiempo si no se los mira mucho. Cuando eso pase, ya tendrás el programa casi acabado. Compilarás, ejecutarás, y si probases (que tampoco hace falta) verías que todo funciona perfectamente.

Si el código compila, eso ya es el paraíso; nada nos impide seguir escribiendo código para liquidar de una vez esta odiosa práctica. El que el programa no haga lo que se quería que hiciera no es tan importante, ya lo arreglaremos más tarde, cuando esté acabado. Además, siempre puede pasar que en un golpe de suerte los profesores cambien el enunciado de la práctica y entonces sí que encaje con nuestro programa, así que no hay que arriesgarse a hacer trabajo inútil arreglando un programa que va descarriado.

Si el código tiene un error que no se produce siempre, ignóralo y sigue escribiendo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Mejor aún que en el punto anterior. Si el error no se produce siempre, va a ser difícil de encontrar, y además puede que en la demostración de la práctica no salga, y además puede que desaparezca solo si no lo miras. Así que no te preocupes, seguro que no es nada grave.

Si el código tiene un error que se produce siempre, cambia cosas aleatoriamente hasta que desaparezca
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ya hemos hablado en contra de pararse y pensar. Si hay un error que, por algún capricho, quieres eliminar, simplemente prueba a escribir el mismo código de otras formas diversas. Esto tiene la ventaja de que a lo mejor se soluciona, y además habrás conseguido que se solucione:

1) sin entender cuál era la causa, y
2) sin dejar de escribir código. Claramente, este es el comportamiento más profesional.

Construye enormes porciones de código sin compilar / ejecutar / probar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
No compiles con frecuencia; no des pasos pequeñitos. Tú eres un profesional, y tienes que dar pasos de gigante. Escribe miles de líneas de código, y ya después compila. Así será mucho más entretenido buscar los errores de compilación y arreglar el código, lo que constituye un excelente ejercicio.

Respecto a ejecutar el programa que escribes, si intentas tener siempre un programa que funcione parcialmente, descubrirás los errores muy pronto, y además al haber hecho pocas modificaciones desde la última vez, te será demasiado fácil saber dónde has introducido el nuevo error. Esto sólo lo hacen los miedicas. Un verdadero programador hace el programa entero, y luego lo digiere entero, como una boa. Nada sustituye a la maravillosa sensación de buscar un error que se oculta en las últimas 10.000 líneas de código que has escrito; si sólo son 10 ó 20, la cosa no tiene ciencia.

No escribas comentarios, salvo los obligatorios
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Ya lo hemos dicho antes. ¿Cuál es el objetivo de todo esto? Hacer un programa. ¿Y de qué consta un programa? De código. Todo código que no sea ejecutable no es realmente necesario. Poner comentarios explicando algo es un insulto a la inteligencia de un programador; cualquiera que vea un programa, si conoce el lenguaje de programación, sabe perfectamente lo que hace ese programa, cómo y por qué.

Si hay comentarios obligatorios (descripciones de funciones y toda esa morralla), esos sí hay que ponerlos, aunque no se tenga nada interesante que decir. A los profesores les gustan esas tonterías y te pondrán más nota.

Ignora los enunciados
~~~~~~~~~~~~~~~~~~~~~
Los enunciados y las especificaciones son un rollo. Hablan de problemas que no nos interesan, son largos, prolijos, y en realidad no son más que un simple ejercicio de narcisismo de los profesores para que veamos cuánto creen que saben. Limítate a echar un vistazo, decide más o menos qué te están pidiendo, y es suficiente; seguir leyendo el enunciado, o volver a leerlo más adelante, es un obstáculo en nuestra verdadera misión. Que no es otra, por supuesto, que escribir el código. Por tanto, una vez intuido más o menos lo que se pide, entierra el enunciado en el fondo de la pila de papeles más alta que tengas, o en las profundidades del directorio temporal de tu ordenador.

Ignora las normas de programación y presentación
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Las normas que dicen cómo debe escribirse el código, o cómo debe presentarse la práctica, son un ejercicio de prepotencia por parte de los profesores. A ellos les gusta dominarnos, obligarnos a hacer cosas que no tienen ningún sentido, y por eso escriben normas. No te prestes a ese juego. Todas esas normas son totalmente innecesarias, ya que aun sin ellas las prácticas entregadas cumplirán los requisitos de calidad exigibles. Respecto a la facilidad de manejo por su parte, ¿no cobran para corregirlas? No te molestes siquiera en poner tu nombre o tu curso en las prácticas, ya que en realidad no tienen mayor dificultad en recordar tu cara, tu estilo inconfundible de programación, y sabrán que la práctica es tuya de todas formas.

Escribe la documentación al final
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

¿Cómo vas a escribir un documento describiendo un programa que no existe? Por otra parte, ¿qué sentido tiene escribir documentos para ti mismo sobre lo que vas haciendo? ¡Todo lo que puedas leer en ellos, ya lo sabes, puesto que lo habrás escrito tú! Así que el único motivo para escribir documentación de un programa es que los profesores la piden. Y eso puede solucionarse el día anterior a la entrega. Si, además, haces el programa durante los días previos a la fecha de entrega, no tendrás el problema de que se te olvide algo y necesites mirar documentos; todo estará muy reciente en tu cabeza.

No aprendas a utilizar el depurador ni otras herramientas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Si se produce un error en tu código, al fin y al cabo todo lo que sabes sobre programación te lo han enseñado los profesores. ¿De quién es, pues, la culpa de que tú tengas un error? Es del profesor; por tanto, que sea él quien lo busque y lo solucione. Los errores de programación son algo excepcional, cuando seas profesional no tendrás que enfrentarte a ellos, por lo que en tu etapa de formación es normal que no emplees tiempo ni esfuerzo en aprender a arreglarlos.

No utilices jamás breakpoints al depurar un programa
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
En primer lugar, ya hemos dicho que no aprendas a utilizar las herramientas. ¿Qué demonios haces con el depurador, entonces?

Si a pesar de todo lo utilizas, no uses breakpoints. De todos es sabido que la mejor forma de depurar un programa es recorriendo paso a paso todo el código hasta llegar a la función que está provocando el error; si hay que recorrer 1000 líneas de código simplemente se le da más rápido a la tecla F7. Los breakpoints son algo esotérico, que permite que pongas a ejecutar un programa y la ejecución se pare justo donde está el breakpoint; pero siempre que podamos ejecutar todo desde el principio estaremos más seguros de que ha llegado a donde queremos.

De la relación con el profesor
------------------------------

No pidas ayuda
~~~~~~~~~~~~~~
Si no sabes hacer algo, si tienes alguna duda, si te has perdido, nunca pidas ayuda, nunca hagas preguntas en clase, ni vayas a ninguna tutoría. Hay miles de razones para esto, pero aquí daremos sólo algunas:

* Si vas a una tutoría a hacer preguntas, estás admitiendo que eres estúpido.
* Si vas a una tutoría a hacer preguntas, les darás trabajo y te cogerán manía.
* Si no entiendes algo, la culpa es del profesor. Pero ¿y si vas y te lo explican y sigues sin entenderlo? Entonces, la culpa pasará a ser tuya, ¿podrás soportar esa vergüenza?
* Si preguntas, puede quedar en evidencia que no sabes algo que deberías saber. Es mejor continuar en la ignorancia que correr ese riesgo.
* Si preguntas en clase, no sólo es que te oiga el profesor. Es que, claro, también te oirán tus compañeros. Y es evidente que tú vas a ser la única persona en la sala que necesite esa explicación, porque los demás, que nacieron aprendidos, seguro que lo entienden. Con lo cual seguro que pasan a opinar que eres estúpido.
* Si preguntas en clase, a lo mejor el profesor te resuelve la duda. Pero claro, obtendrá una valiosa información; a partir de las preguntas de los alumnos, puede que se dé cuenta de que su explicación no ha sido buena, de que la organización del curso no es adecuada, de que está yendo demasiado rápido, o cualquier otra cosa. ¿Acaso vas a darle esta información gratis? ¿Y si se le ocurre utilizar esa información para mejorar sus explicaciones? No seas insensato, no le facilites las cosas. ¿Acaso te beneficia en algo que vaya convirtiéndose en mejor profesor?.

**Conclusión:** nunca pidas ayuda ni acudas a una tutoría. Es mucho mejor confiar en tus compañeros, ya que al fin y al cabo están en tu situación, mientras que el profesor es tu contrincante, tu oponente, tu enemigo.

Sólo hay dos excepciones a esta regla:

#. puedes preguntar si te has encontrado con algún problema y no te da la gana buscarlo. Entonces, sí está justificado que acudas al profesor para que sea él el que haga tu trabajo. Si se niega, critícale en los pasillos.
#. La segunda es que se puede acudir a tutorías en la semana previa a la entrega del programa. Estará lleno de gente, el profesor se dedicará en exclusiva a atender alumnos obviando otras tareas, y además si no te atiende podrás criticarlo en los pasillos. Cada vez que vayas, tendrás que esperar durante horas, y eso te permitirá relacionarte con compañeros en la cola. Todo son ventajas.

Nunca describas un problema en detalle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Si a pesar de todo decides saltarte el punto anterior, y pides ayuda, ten en cuenta una regla de oro que te será también muy útil en tu vida profesional (no en vano la siguen multitud de profesionales y usuarios de la informática). NUNCA describas un problema en detalle.

Ejemplo. Si durante el desarrollo de un programa se produce algún suceso que te resulta desagradable, acude al profesor y dile: "Ayer me pasó algo que no me agrada". El pondrá cara de esperar más datos; aguanta, no digas nada más. No se te ocurra entrar en detalles como estos:

* Si el suceso desagradable se produjo durante la compilación del programa o durante la ejecución.
* Si el suceso desagradable hizo que el programa terminase súbitamente su ejecución o bien hizo que la ejecución continuase indefinidamente, o simplemente el programa no hizo lo que esperabas que hicera desde un punto de vista funcional.

Otro ejemplo. Si el suceso desagradable se produjo durante la compilación, no le digas al profesor el mensaje de error y la línea en la que se produjo dicho error. Dile sólo algo como "Me daba no sé qué error, o algo".

Otro ejemplo. Si el suceso desagradable se produjo durante la ejecución, y provocó la súbita terminación del programa, nunca anotes el mensaje producido, ni le digas al profesor el texto del mismo. Di simplemente "Me daba no sé qué error, o algo".

Evidentemente, si el suceso desagradable consistía en que el programa no hacía lo que esperabas, no se te ocurra decirle al profesor en qué situación exacta lo producía (si era al leer un fichero vacío, o antes o después de que pasase alguna otra cosa). Evita una descripción como "El error se produce siempre que cargo un segundo fichero y el primero estaba vacío". Tú di sólo la frase mágica: "Me daba no sé qué error, o algo".

¿Lo vas pillando?

Lleva siempre los fuentes equivocados
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Supongamos que, contra todos nuestros consejos anteriores, acudes al profesor, y además vas a preguntarle por un problema concreto. Si el profesor se niega a examinar tus fuentes, podrás criticarle en los pasillos y advertir a futuros alumnos contra él, pero puede darse el caso de que el tío te reciba y tú acabes entrando y preguntando. Haces mal, pero la situación aún tiene arreglo: procura llevar los fuentes equivocados. Por ejemplo, si tienes un problema, y haces diversas modificaciones que no dan resultado, o incluso generan problemas nuevos, acude con los últimos fuentes, pero pregunta por el problema original. Así, el profesor buscará inútilmente un error cuando se le producirá otro. Entonces di algo como "Ah, bueno es que después probé una cosa. Quita esa línea de ahí..."

Si manejas este proceso con habilidad, puedes realizar toda una sesión de codificación allí mismo, en las tutorías. Esto es particularmente aconsejable si hay otros compañeros esperando fuera. El profesor cogerá mala fama, trabajará más tiempo, harás que el resto de los alumnos tengan más trabas para avanzar, con lo que el nivel de la clase se mantendrá en cierto equilibrio y así no pensarán en ampliar el temario en futuros años... Tómatelo como un servicio a la comunidad.

No aísles el problema
~~~~~~~~~~~~~~~~~~~~~
Volvamos a suponer que eres un irresponsable y acudes a una tutoría. No se te ocurra aislar el problema antes de ir. Si se produce un error en un fichero de entrada de 1 MB, no intentes ir probando con ficheros más pequeños hasta acotar qué produce el error, ni intentes crear un mini-programa que reproduzca el mismo error. Eso podría permitir al profesor averiguar el problema de manera certera y rápida. Es mucho mejor que se lea miles de líneas de código y que haga trazas con centenares de miles de pasos. De este modo, ejercitará notablemente sus artes adivinatorias y podrás verificar su capacidad de deducción. Por supuesto, si se niega a buscar tu error, critícale en los pasillos.

Usa el correo electrónico con habilidad
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Hay preguntas que son prácticamente imposibles de resolver por correo electrónico, si se hacen bien. Cultiva este arte. Haz que tu pregunta sea totalmente inconcreta. Ejemplo: "Me da no sé qué error, o algo. Aquí te mando el fuente". También puedes hacer una pregunta un tanto más concreta, pero no mandar el fuente: "En mi clase TDispositivo en el constructor me da no sé qué error, o algo". Si el profesor no resuelve el problema, critícalo en los pasillos por incompetente.

Por supuesto, escribe el mensaje de corrido y mándalo; no lo leas por segunda vez intentando ponerte en el lugar del profesor. Eso te podría llevar a detectar errores, y no es eso lo que se pretende.

Eskríbelo todo cn abrvtrs o konsonantes ekstrañas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Los profesores son unos puretas. Tú eres generación WAP. O si no, al menos serás un poko radikal. Intenta escribir mensajes que no resulten fáciles de leer. El tío, aunque crea que no, tendrá que hacer un esfuerzo extra, y además en la pantalla de un ordenador, ante la que quizás lleve varias horas. Eso facilitará su concentración y aumentará su buen humor.

Comete faltas de ortografía
~~~~~~~~~~~~~~~~~~~~~~~~~~~
La ortografía es una burda convención; hasta Juan Ramón Jiménez ponía jotas donde le daba la gana, y hasta Gabriel García Márquez abogaba por eliminar la ortografía. Evidentemente, tú no eres menos que ellos, así que tienes el mismo derecho a escribir como quieras.

¿Que no tienes costumbre de cometer faltas de ortografía? Es bien fácil. Puedes empezar por el ejercicio más fácil, más frecuente y más provechoso: "Haber si me sale". Ya, ya sé; la forma correcta es "A ver si me sale" (como diciendo "veamos si me sale"), pero ¿no encierra una brutal poesía esa brusca contracción de dos palabras en una, esa alteración semántica de utilizar el verbo "haber" sin significado alguno, esa hermosa palabra que arroja simultáneamente una B y una H (las letras más peligrosas de la ortografía española) a los ojos del lector? Si te apetece darle al profesor una bofetada y no tienes arrestos, escríbele un "Haber si puedo ir mañana a tutorías", que es lo más parecido.

"Haber si..." es la número uno, pero aquí tienes otras sugerencias, todas ellas casos rigurosamente verídicos:

* Si le hes posible, mándeme...
* Desarroyo
* Interfac
* Habro una ventana...
* ...va ha ser...
* Las fechas de exámenes calendariadas... (esta no es de un alumno, sino de una circular interna de una institución universitaria)
* Estrayendo
* Habre un fichero
* Un herror léxico (esta expresión es metafísica, recursiva... no sé cómo definirla)
* Gracias al echo de que... Dejando aparte este echo...
* Se deshecha esta opción
* Que ya estén echas
* Que los valla almacenando en memoria
* En caso de que no halla un fichero cargado en memoria
* Fue echa de manera que
* ...más aya de...
* ...no yeva el nombre de la clase...
* ¿Ha qué hora es el examen...?
* Yegué tarde a inscribirme...

No te identifiques
~~~~~~~~~~~~~~~~~~
El correo electrónico tiene otra cosa divertida. Puedes empezar a largar sin que el tío sepa ni de qué grupo eres, ni quién eres. Todo se arreglará si en ese caso lo tuteas, porque así aumenta la familiaridad y no hace falta el nombre. Mejor aún es escribir un mensaje en el que no sepa ni de qué titulación eres. Sí, por ejemplo: "¿Cuál es la fecha de entrega para la primera práctica? Firmado: Fefu". Si el profesor da más de una asignatura en diferentes carreras (cosa extraordinariamente probable), será un buen ejercicio para él coger las listas de alumnos de todas ellas y buscar algo que pueda casar con "Fefu".

Y, sobre todo...
----------------

Deja el trabajo para el final
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Desde el primer día, el profesor insistirá en intentar pedir cosas para la semana siguiente. Intentará avisar de que hay que ir haciendo el trabajo a un ritmo constante y decidido desde el principio.

No le escuches
~~~~~~~~~~~~~~
La programación de ordenadores, aunque es una disciplina joven, tiene ya sagradas tradiciones, y una de ellas es la prisa en los días previos a una entrega. Evitar ese estrés sería una nefasta preparación para tu vida profesional. Deja que el trabajo se acumule, desoye las advertencias o los signos de retraso. No interrumpas tu vida ni dejes de ir a esquiar para recuperar tiempo perdido. Y cuando ya estés al límite del desastre, cuando falten dos semanas para la entrega de un programa estimado para cuatro meses... entonces empieza a escribir código como si no hubiera un mañana.

¿Qué aliciente tendría esta profesión si los programas se construyeran sin prisa y sin pausa? ¿Qué sería de la imagen del melenudo barbudo (o melenuda barbuda) maloliente (por no tener tiempo para afeitarse / cortarse las puntas / ducharse) con una camiseta de Megadeth (en las camisetas jeviatas se ven menos las manchas, gracias a su color negro y a los complejos dibujos), que lleva 48 horas ininterrumpidas dándole a la tecla? ¿Estarías acaso preparado para ir a la Campus Party y matar monstruos en una pantalla, con el culo sobre una silla de melamina y la cabeza bajo un techo de lona a 35ºC, durante tres días seguidos? ¿Cómo podríamos sentirnos un poquito héroes si todos los días nos vamos a dormir cuando nos entra el sueño? ¿Qué sería de las fábricas de Cocacola, qué sería de Juan Valdés, qué sería de las refinerías de cafeína que destinan la mitad de su producción a los programadores? ¿Acaso Sandra Bullock o Robert Redford cuando hacían de hackers se sentaban con sus apuntes al lado del ordenador, pensaban, tecleaban sin prisa y a la hora habitual se iban al gimnasio o al bar de la esquina, y así un día tras otro durante cuatro meses? ¿Acaso el tío ese de "Operación Swordfish" habría roto la clave del Pentágono si no hubiera estado un esbirro del Travolta apuntántole con una pistola mientras otra esbirra del Travolta lo distraía?

No, amigo, no. Para vivir tranquilo, te habrías matriculado en otra carrera. ¿Te imaginas ir a clase y que cuando el tío diga "Quién tiene hecho nosequé" tú puedas decirle "yo", y que cuando explique lo siguiente que hay que implementar tú estés atendiendo y entendiendo lo que dice porque lo anterior ya lo tienes funcionando?

Eso es para empollones y flojos de espíritu. Ya lo sabes. Deja todo el trabajo para el final.

Copia las prácticas
~~~~~~~~~~~~~~~~~~~
Copia las prácticas; ya sean las actuales por un compañero de clase, o prácticas del año pasado. Cada profesor puede tener que corregir varias decenas de prácticas; es difícil reconocer similitudes entre tantos programas. Si las reconocen, además, no es fácil demostrarlo, recurre y lleva el caso hasta el Tribunal Constitucional. Te llevará muchísimo más tiempo y esfuerzo que hacer las prácticas, pero el caso es demostrar que eres más listo que el profesor y no dar nunca el brazo a torcer.

La sensación de ahorro de trabajo que da copiar una práctica (o parte de ella) es inigualable y merece la pena. No importa que luego quedes en evidencia en la demostración, o en el examen práctico, o que en el fondo no hayas aprendido lo necesario, ya que el objetivo de las prácticas no es el aprendizaje, sino sólo la obtención de unos asquerosos créditos. Por tanto, copia lo que puedas. Si un profesor te suspende por copiar, critícale en los pasillos.

No vayas a clase
~~~~~~~~~~~~~~~~
No sé si te has enterado de que la Universidad es, teóricamente, un sitio al que acuden universitarios (es decir, adultos). Debes comportarte como tal. Por ejemplo, debes fumar mucho, asistir a todas las fiestas de las facultades (y agarrar una melopea del quince en cada una de ellas, vomitona incluida), debes hacer pintadas en los ascensores y las mesas, en fin, todo ese tipo de cosas que demuestran que no eres un universitario de pacotilla.

He dicho "teóricamente" porque, por desgracia, no todos los que acuden a la Universidad son gente como Dios manda. Los nenés deberían quedarse en casa, pero algunos no lo hacen: se matriculan en la Universidad y luego van a clase. No se te ocurra ser como ellos. La mayoría acabarán como profesores; Dios los cría y ellos se juntan.

Haz caso a los repetidores; ellos han estado antes aquí, y por tanto es evidente que son quienes saben lo que hay y a ellos es a quienes debes imitar. Ir a clase es una pérdida de tiempo. En primer lugar, está todo en los apuntes y en los libros, por lo que puedes preparar perfectamente la asignatura sin ir a ese coñazo de clases. Simplemente, reúnes los apuntes de la fotocopiadora y los que otra gente toma en clase, los comparas y cotejas para que estén completos, y una vez que tengas eso, sabrás lo que se ha dado, y entonces vas y te haces con los libros que ponen en la bibliografía, y te los lees todos y entonces ya está. En segundo lugar, de todas formas lo que se persigue en una práctica de programación es, y no me cansaré de repetirlo, el código, y en clase rara vez se escribe código. Un verdadero universitario estudia así; cuando va a la facultad, es para estar en la cafetería o sentado en los alrededores charlando con los amiguetes, con una actitud interesante y sofisticada. Entrar en clase es como ser un borrego que entra al redil. Tú eres mucho más rebelde que todo eso.

Encima, si algo te sale mal por culpa de la mala organización de la asignatura, ellos tendrán el morro de decirte que la culpa es tuya por no ir a clase, que en clase se avisó de tal o cual cosa, que en clase se explicó nosequé parte del enunciado, y así.

Ah, amigo; así está la Universidad española, que pagas con tus impuestos y luego quienes tienen la obligación de enseñarte no lo consiguen y como excusa te salen con esas. Pero ya sabes cuál es tu obligación como ciudadano: critícales en los pasillos.
