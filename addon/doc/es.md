---
author:
- Rémy Ruiz &lt;<remyruiz@gmail.com>&gt;
autonumber-headings: 1
css:
- style.css
date: martes 4 de agosto de 2020
extratags: 1
extratags-back: 0
filename: doc_es
include-after:
- '%addonDir%/doc/dependencies.md'
keywords: documentación, MarkdownForever, NVDA, complemento, español
lang: es
langd: es
subtitle: Convertidor Markdown y HTML completo para NVDA
template: default
title: Documentación de MarkdownForever %addonVersion%
toc: 1
...

**Índice**

%toc%

## Introducción

MarkdownForever es un complemento para NVDA que puede convertir fácilmente el contenido Markdown o HTML. Sólo tienes que escribir o mostrar cualquier texto en  formato Markdown o HTML y ejecutar un simple atajo para convertir  o mostrar una vista previa instantáneamente de los resultados en cualquier momento, tal y como aparecerá en tu página Web final, o en código fuente HTML, listo para pegar en cualquier campo de texto suportando el código HTML.

MarkdownForever puede:

* Convertir de Markdown en HTML
* Convertir de Markdown en código fuente HTML
* Convertir de HTML en Markdown
* Convertir de Markdown en HTML formateado

## Pero el Markdown, ¿Qué es?

Según Wikipédia,
> Markdown es un lenguaje de marcado ligero creado por John Gruber que trata de conseguir la máxima legibilidad y facilidad de publicación tanto en su forma de entrada como de salida, inspirándose en muchas convenciones existentes para marcar mensajes de correo electrónico usando texto plano.

Puedes aprender más acerca de Markdown leyendo el [artículo completo en Wikipedia.](https://es.wikipedia.org/wiki/Markdown)

Así que en lugar de escribir tus documentos web en lenguaje HTML corriendo el riesgo de cometer errores, sólo hay que utilizar etiquetas fáciles de recordar y el trabajo se hará al instante. Con Markdown, tu puedes casi hacer    lo que  HTML puede hacer: títulos, listas ordenadas (enumeradas) o no ordenadas (listas con viñetas), enlaces y incluso tablas.

Por ejemplo, si se quiere realizar un título de nivel 1, solo es necesario escribir  el signo de número (#), seguido por el nombre de tu título, con o sin espacio entre los dos:

> `#Aquí un ejemplo de título de nivel 1`

que aparecerá de la siguiente manera en el documento HTML final:

> <h1>\!Aquí un ejemplo de título de nivel 1</h1>

Para un título de nivel 2, vas a utilizar dos signos de número, tres para un título de nivel 3, etc.
 
Ahora hagamos una lista no ordenada de elementos. Para ello, es necesario prefijar todos los elementos de la lista por un asterisco (*).
 He aquí un ejemplo:

<blockquote>

```
* Naranja
* Azúcar
* Leche
```
</blockquote>

que aparecerá como esto:

> * Naranja
> * Azúcar
> * Leche

También puedes crear un enlace poniendo el título del enlace entre corchetes ([]), seguido de la URL entre paréntesis y sin espacios. Por ejemplo:

    [Has clic aquí para visitar el sitio Web de NVAccess](https://www.nvaccess.org)

esto te dará:

[Has clic aquí para visitar el sitio Web de NVAccess](https://www.nvaccess.org)
 
Incluso tienes la posibilidad de poner un `*texto enfatizado en cursiva*` encerrandolo con asteriscos, o `**escribiendo un texto enfatizado en negrita**` encerrandolo con dos asteriscos... Hay muchas posibilidades. Por ejemplo puedes consultar la [guía definitiva en español para empezar con Markdown](https://markdown.es/sintaxis-markdown/) para aprender más.

## Conversión de Markdown en HTML

Esta característica te permite convertir cualquier texto en Markdown mostrado en la pantalla en HTML, mientras que te permite ver cómo se verá en el documento HTML final. Puede ser un documento que tu  mismo has escrito en Markdown, un archivo .md que ya tienes en tu disco duro o de un texto en Markdown encontrado en una página Web. Por defecto, MarkdownForever convierte todo el texto que se muestra actualmente, pero también se puede seleccionar sólo una parte específica que se desea convertir.

Se pueden utilizar las siguientes teclas de órdenes:

- *NVDA+ALT+b* : El resultado se muestra en forma de  página Web en el navegador predeterminado.
- *NVDA+ALT+n* : El resultado se muestra en forma de  página Web en un tampón virtual de NVDA.

Ten en cuenta que se recomienda utilizar la visualización en el navegador en lugar del tampón virtual de NVDA. Algunas etiquetas, específicamente como las etiquetas HTML5 tal como `<details>,` no son  soportados por el rendido del tampón virtual.

## Conversión de Markdown en código fuente HTML

Esto convierte el texto Markdown en lenguaje HTML puro. Una vez hecho esto, puedes copiar y pegar en un archivo HTML, en un mensaje del foro, o en cualquier campo de texto en la  web donde el código  HTML es soportado.

Las siguientes teclas de órdenes están disponibles:

- *NVDA+ALT+l* : El resultado se muestra en un tampón virtual de NVDA.
- *NVDA+Ctrl+h* : Copia el código fuente HTML al portapapeles.

## Conversión HTML en Markdown

Esta función intenta de generar un texto en Markdown a partir de una fuente HTML. Esto también se aplica a todo el texto mostrado en la pantalla o en una parte seleccionada previamente. Las siguientes teclas de órdenes están disponibles:

- *NVDA+Alt+k* : Muestra el resultado en un tampón virtual de NVDA.
- *NVDA+Maj+g* : Copia el resultado al portapapeles.

También puedes convertir una página web HTML en Markdown, simplemente seleccionando su URL. Sin embargo, primero debes asegurarte de que el motor de conversión HTML2Text está configurado correctamente como  motor de conversión por defecto en los  [ajustes de MarkdownForever,](#ajustes-por-defecto-de-markdownforever) situado en el submenú Preferencias del menú NVDA.
 
## Conversión Markdown en HTML formateado

Esta función  convierte  tu Markdown en HTML formateado y lo copia al portapapeles. El HTML formateado se parecerá a cualquier página Web mostrado  por tu navegador, con enlaces cliqueables, encabezados, etc. Esto sólo se puede generar a partir de un contenido Markdown. Para realizar esta acción, pulsa NVDA+shift+h.

Ten en cuenta que el *HTML formateado* se puede pegar en aplicaciones como Microsoft Word, Wordpad, Thunderbird, un campo de texto enriquecido en una página Web, etc. Sin embargo, no se puede utilizar editores de texto, como el  Notepad (Bloc de notas), Notepad++, etc.

## Modo interactivo

El modo interactivo ofrece todas la funcionalidad de MarkdownForever en un cuadro de diálogo práctico, que te ofrece aún más posibilidades. Para abrir el modo interactivo, pulsa NVDA+CTRL+i.
He aquí una descripción de la pantalla en orden de tabulación:

* "Convertir a": Esta primera lista desplegable te permite seleccionar la dirección de la conversión: HTML, fuente HTML o Markdown. Puedes utilizar las flechas arriba y abajo para elegir.
* "Generar Tabla de Contenido / Índice": Esta casilla de verificación te permite generar o no un índice de los capítulos  de tu documento HTML final, con enlaces cliqueables yendo a cada capítulo. El estado de esta opción también se puede configurar por defecto en los [ajustes de MarkdownForever.](#ajustes-por-defecto-de-markdownforever)
* "Intentar de numerar automáticamente los títulos": Te permite indicar si los títulos deben ser numerados automáticamente o no.
* "Habilitar las super-etiquetas": Si esta opción está marcada, podrás utilizar etiquetas especiales ](#super-etiquetas) en tu Markdown para insertar automáticamente información como la fecha o la hora actual. El estado de esta opción también se puede configurar por defecto en los [ajustes de MarkdownForever.](#ajustes-por-defecto-de-markdownforever)
* "Permitir la reversibilidad de super-etiquetas": Te permite indicar, cuando se convierte en Markdown, si las [super-etiquetas](#super-etiquetas) deben ser restaurados a su forma original (por ejemplo %date%). Esto sólo funciona a partir del contenido HTML generado por Markdown Forever. 
* "Título": Aquí puedes introducir el título del documento HTML, que será visible en el navegador.
* "Generar los metadatos desde la fuente HTML": Al convertir un archivo fuente HTML en Markdown, MarkdownForever intenta extraer los metadatos a partir del código fuente (título, idioma, nombre de archivo, etc.) y genera el [bloque de metadatos](#bloque-de-metadatos-opcional) para ti. Esta opción sólo está disponible cuando se convierte de HTML hacia Markdown.
* "Mostrar en el tampón virtual": Este botón abrirá tu contenido convertido  en un tampón virtual de NVDA.
* "Mostrar en el navegador": El contenido convertido se muestra en tu navegador predeterminado.
* "Copiar al portapapeles": Esto colocará tu contenido convertido al portapapeles de Windows, listo para ser pegado.
* "Guardar como": Esto te pedirá que guardes el documento convertido en tu disco duro mediante un cuadro de diálogo estándar Guardar como de Windows. Una ubicación de almacenamiento por defecto también se puede definir en los [ajustes de MarkdownForever.](#ajustes-por-defecto-de-markdownforever)

## Bloque de metadatos opcional

El Bloque de metadatos te permite establecer  los ajustes específicos para un determinado documento, independientemente de los [ajustes por defecto.](#ajustes-por-defecto-de-markdownforever) Este bloque debe ser colocado al comienzo del documento y debe empezar con tres guiones ("---") y terminarse con tres puntos ("...") o tres guiones ("---"). Cada entrada debe introducirse de la siguiente manera: clave: "valor" (el valor debe estar entre comillas). Una línea vacía debe estar presente después del bloque de metadatos.

### Lista de metadatos soportados

* author (o authors): Permite especificar uno o varios autores en el documento (Véase el ejemplo más abajo). Esto será añadido en el encabezado del archivo HTML. Esta clave no es sensible a las mayúsculas.
* autonumber-headings: Permite indicar si los títulos deben ser numerados automáticamente o no.
* css (o CSS): Permite especificar uno o varios archivos CSS para la presentación de tu documento (Véase el ejemplo más abajo). Esta clave no es sensible a las mayúsculas.
* date: Te permite especificar una fecha de creación de tu documento. Esto será añadido en el encabezado del archivo HTML.
* extratags: Permite establecer si las [super-etiquetas](#super-etiquetas) deben ser interpretados o no. Valores posibles: true (1) o false (0).
* extratags-back: Permite indicar, cuando se convierte en  Markdown, si las [super-etiquetas](#super-etiquetas) deben ser restauradas a su forma original (por ejemplo %date%). Esto sólo funciona a partir de un contenido HTML generado por Markdown Forever. Valores posibles: true (1) o false (0).
* Filename: Permite especificar el nombre del archivo de salida durante el registro.
* Keywords: Permite establecer las palabras clave relacionados al (los) sujeto(s) tratado(s) en tu documento.
* lang: Permite especificar el idioma principal del documento. Si es necesario, utiliza las etiquetas span/div con el atributo lang para indicar los cambios de idioma internos al documento.
* mathjax: Permite establecer si las fórmulas matemáticas escritas en [LaTeX](https://es.wikipedia.org/wiki/LaTeX) deben ser convertidas o no. Valores posibles: true (1) o false (0). Se requiere una conexión a Internet y debes abrir el resultado convertido en tu navegador para mostrarlo correctamente, ya que el LaTeX interpretado no puede ser rendido por el tampón virtual de NVDA.
[Has clic aquí para obtener más información acerca de MathJax](https://es.wikipedia.org/wiki/MathJax)
* path: Permite especificar el directorio en la que el documento debe ser generado. Las variables de entorno %userprofile%, %appdata% y %tmp% son soportados.
* subtitle: Permite especificar un subtítulo para tu documento HTML. Esto será añadido en el encabezado del archivo HTML.
* title: Define el título del documento HTML. En modo interactivo, el campo título  se llena automáticamente con el valor de esta clave.
* toc: Permite indicar Si una tabla de contenidos se debe generar o no. Valores posibles: true (1) o false (0).

### Ejemplo de uso de metadatos
<blockquote>
```
---
title: Un simple título
date: 4 de agosto de 2020
subtitle: Aquí es el subtítulo de tu documento
lang: en
author:
- Juan Pérez
- Pedro Ortiz
CSS:
- %userprofile%/document/main.css
- %userprofile%/document/custom.css
keywords: NVDA, Markdown, HTML
filename: test
path: %userprofile%/desktop
toc: 0
autonumber-headings: 1
mathjax: 0
---

¡Hola Mundo!<span lang="en">Hello World!</span> <span lang="fr">Bonjour le monde !</span>
```
</blockquote>

En el ejemplo  de arriba, el texto va a ser verbalizado en tres idiomas, suponiendo que el Sintetizador  de voz que utilizas admita el cambio Automático de Idioma y que la casilla de verificación  correspondiente está marcada en Opciones de voz de NVDA. Lo  que dará:

> ¡Hola Mundo! <span lang="en">Hello World!</span> <span lang="fr">Bonjour le monde !</span>

## Super-etiquetas

Las super-etiquetas son variables especiales que se pueden colocar en tu contenido Markdown para añadir automáticamente información del sistema como la fecha o la hora actual y que se mostrará  en texto claro en tu documento HTML.

### Super-etiquetas disponibles

| **En el Markdown** | **Explicación** | **Resultado en el navegador** |
| ---------- | :---------- | ---------- |
| `%date%` | Fecha actual | %date% |
| `%time%` | Hora actual | %time% |
| `%now%` | Fecha / hora actual | %now% |
| `%day%` | Día actual (formato largo) | %day% |
| `%dday%` | Día actual (formato decimal) | %dday% |
| `%month%` | Mes actual (formato largo) | %month% |
| `%dmonth%` | Mes actual (formato decimal) | %dmonth% |
| `%year`` | Año actual (2 dígitos) | %year% |
| `%Year%` | Año actual (4 dígitos) | %Year% |
| `%toc%` | Tabla de contenidos en la posición del cursor (si está habilitado por metadatos o ajustes por defecto) | N/A |

## Ajustes por defecto de MarkdownForever

Estos son accesibles desde el menú de NVDA -> Preferencias -> MarkdownForever -> Ajustes y te permiten configurar y establecer  por defecto varias opciones de conversión ya mencionados anteriormente:

* "Generar Tabla de Contenido / Índice": Esta casilla de verificación te permite generar o no un índice de los capítulos de tu documento HTML final, con enlaces cliqueables yendo a cada capítulo. Este comportamiento también puede ser definido específicamente para un documento con la ayuda de la clave "toc" en el [bloque de metadatos opcional](#bloque-de-metadatos-opcional) y colocado dondequieras en el documento con la ayuda de la [super-etiqueta](#super-etiquetas) correspondiente.
* "Habilitar las super-etiquetas": Si esta opción está marcada, se permite el uso de las [super-etiquetas](#super-etiquetas) en tu contenido  Markdown para insertar automáticamente información como la fecha o la hora actual. Este comportamiento también puede ser definido específicamente para un documento con la ayuda de la clave extratags en el [bloque de metadatos opcional.](#bloque-de-metadatos-opcional)
* "Generar los metadatos desde la fuente HTML": Al convertir un archivo fuente HTML en Markdown, MarkdownForever intenta extraer los metadatos a partir del código fuente (título, idioma, nombre de archivo, etc.) y genera el [bloque de metadatos](#bloque-de-metadatos-opcional) para ti.
* "Acción por defecto en modo interactivo": Esto  permite elegir la acción por defecto que se va a realizar al pulsar la tecla Intro en [Modo interactivo:](#modo-interactivo) Mostrar el contenido generado en tu navegador, en un tampón virtual o ponerlo al portapapeles.
* "Motor de conversión": MarkdownForever te permite elegir entre dos motores de conversión, [HTML2Text](https://pypi.org/project/html2text/) y [HTML2Markdown.](https://pypi.org/project/html2markdown/) Sólo basta con experimentar y elegir la que prefieras, de acuerdo a tus necesidades o el resultado  producido.
* "Extensiones de Markdown": configura las funciones compatibles con `markdown-it-py` (tablas, listas de tareas, notas al pie, identificadores de encabezado, etc.).
* "Ruta": Aquí,  puedes establecer una ubicación para guardar por defecto     en tu disco duro tus documentos convertidos, práctico si siempre utilizas la misma carpeta para almacenar todo tu trabajos.
* "Administrar las plantillas HTML": Esto abrirá un cuadro de diálogo permitiendo añadir, editar o eliminar las plantillas HTML. Con  las plantillas, podrás personalizar la apariencia visual de tus documentos HTML mediante  CSS (cascading styles sheets), el lenguaje definiendo la presentación visual de una página Web. Esto te permitirá cambiar los colores, la puesta en página o añadir imagenes a tus producciones y crear una plantilla para cada necesidad específica. Por supuesto, hay muchos tutoriales para aprender CSS disponibles en la web y [éste](https://www.ciudadano2cero.com/aprender-css-basico-desde-cero/) puede ser un buen punto de partida.

## Resumen de órdenes de teclado

- *NVDA+CTRL+i*: Modo interactivo.
- *NVDA+ALT+b*: Conversión Markdown en HTML. El resultado se muestra en tu  navegador predeterminado.
- *NVDA+ALT+n*: Conversión Markdown en HTML. El resultado se muestra en un tampón virtual de NVDA.
- *NVDA+ALT+k*: Conversión HTML en Markdown. El resultado se muestra en un tampón virtual de NVDA.
- *NVDA+ALT+l*: Conversión Markdown en código fuente HTML. El resultado se muestra en un tampón virtual de NVDA.
- *NVDA+SHIFT+g*: Conversión HTML en Markdown. El resultado se copia al portapapeles.
- *NVDA+SHIFT+h*: Conversión Markdown en HTML formateado. El resultado se copia al portapapeles.
- *NVDA+CTRL+h*: Conversión Markdown en código fuente HTML. El resultado se copia al portapapeles.

## Información adicional
* Autor(es):
	- André &lt;<dev@andreabc.net>&gt;: diseñador y mantenedor principal del complemento.
	- Sof &lt;<hellosof@gmail.com>&gt;: documentación en inglés y francés, varias sugerencias.
	- Victor Cai: traducción al chino.
	- Çağrı Dogan, Umut Korkmaz: traducción al turco.
	- Rémy Ruiz &lt;<remyruiz@gmail.com>&gt;: traducción al español.
	- Dang Manh Cuong &lt;<dangmanhcuong@gmail.com>&gt;: traducción vietnamita.
	- ¡Y muchos otros!
* Licencia: Licencia Pública General de GNU, versión 2
* Descargar [versión stable](https://andreabc.net/projects/NVDA_addons/markdownForever.nvda-addon)
* Descargar [versión de desarrollo](https://andreabc.net/projects/NVDA_addons/markdownForever.nvda-addon?channel=dev)
* Repositorio  GitHub: [aaclause/NVDA-markdownForever](https://github.com/aaclause/nvda-markdownForever)
* **Dependencias incluidas** :