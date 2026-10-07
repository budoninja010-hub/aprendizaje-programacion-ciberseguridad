# Módulo 1 — GNU, Linux, kernel y distribuciones

Manual Maestro de Linux y Shell Scripting — Edición 2026 · v3 · Primera entrega.

[Índice y arquitectura](00-indice-arquitectura.md) · [Auditoría y fuentes](02-auditoria-fuentes.md)

## 1. Objetivo y diagnóstico inicial

Al terminar podrás distinguir un núcleo, una distribución y una shell; identificar qué sistema estás usando; y explicar para qué servirá `~/linux-lab`.

No necesitas saber programar. Antes de la práctica responde: ¿trabajas en Linux instalado, una máquina virtual, una distribución dentro de WSL o todavía solo en Windows? ¿Has escrito alguna orden en una terminal? Si no lo sabes, estudia primero los conceptos y deja pendiente la ejecución. No hace falta instalar nada para leer este módulo.

En Windows, PowerShell no interpreta las órdenes de Bash de la misma forma. Abre la terminal de tu distribución Linux ya preparada. Si no tienes una, la preparación del entorno será una actividad guiada aparte; no improvises una instalación ni un particionado. Git Bash sirve para ciertas prácticas de shell, pero no equivale a disponer de un sistema Linux completo.

## 2. Qué es un sistema operativo

Es el conjunto de programas que permite usar los recursos del equipo y ejecutar aplicaciones. Coordina tareas como reservar memoria, acceder a archivos y comunicarse con dispositivos.

**Para qué te sirve saberlo:** al aparecer un problema, podrás distinguir si está en una aplicación, una herramienta o una parte del sistema.

Ejemplo: al abrir una nota, el editor presenta el texto; otras partes del sistema permiten leer los datos del almacenamiento. El editor no es por sí solo todo el sistema operativo.

**Error frecuente:** llamar «sistema operativo» a la ventana de terminal. La terminal es solo una interfaz para interactuar con programas.

**Tu ejercicio:** menciona una aplicación que uses y una tarea del sistema que necesite para funcionar.

## 3. Qué es Linux y qué significa kernel

**Kernel** significa núcleo. Linux es un núcleo: participa en la gestión de procesador, memoria, procesos y dispositivos. Un proceso es un programa en ejecución. El núcleo ofrece mecanismos que utilizan los programas; no es el escritorio ni la terminal.

**Para qué sirve:** permite que varias aplicaciones compartan los recursos del equipo bajo las reglas del sistema.

Ejemplo: si escuchas audio y editas texto, hay varios procesos que necesitan tiempo de procesador. No necesitas conocer todavía el algoritmo que organiza esa ejecución.

Esquema conceptual simplificado:

```text
Persona
  ↕
Aplicaciones y herramientas
  ↕
Núcleo Linux
  ↕
Hardware: procesador, memoria y dispositivos
```

Las flechas representan interacción entre capas. El esquema omite detalles como bibliotecas y controladores para empezar con lo esencial.

**Error frecuente:** creer que una versión del kernel identifica por sí sola a Ubuntu o Debian. Distintas distribuciones pueden usar núcleos relacionados y mantener cambios propios.

**Tu ejercicio:** explica con tus palabras por qué una aplicación y el kernel no son lo mismo. [Referencia conceptual de Debian](https://www.debian.org/intro/about).

## 4. Qué es GNU

GNU es un proyecto de software libre y un sistema operativo desarrollado mediante muchos componentes. Entre sus programas están Bash y las utilidades GNU Coreutils. Cuando un sistema combina componentes de GNU con el núcleo Linux se suele denominar **GNU/Linux**. En el uso cotidiano también se emplea «Linux» para hablar de distribuciones completas; aquí aclararemos cuándo nos referimos específicamente al núcleo. [Terminología del proyecto GNU](https://www.gnu.org/prep/maintain/html_node/GNU-and-Linux.html).

**Para qué sirve distinguirlos:** la documentación del núcleo y la de un comando no responden necesariamente a la misma pregunta. Para estudiar una opción de `ls`, se consulta la documentación de la implementación de esa utilidad, por ejemplo GNU Coreutils.

Ejemplo: Bash interpreta órdenes; `ls` muestra entradas de directorio; Linux es el núcleo. Ninguno de esos nombres es sinónimo de los otros.

**Error frecuente:** creer que todos los sistemas que usan el núcleo Linux incluyen exactamente las mismas herramientas. Hay distintas combinaciones; este curso se centra en entornos GNU/Linux habituales.

**Tu ejercicio:** clasifica Linux como núcleo y Bash como herramienta de interacción. Explica qué relación tienen dentro de un sistema.

## 5. Qué es una distribución

Una distribución selecciona, integra y distribuye componentes: núcleo, herramientas, paquetes, configuraciones y mecanismos de actualización. Puede ofrecer instalación gráfica o funcionar sin escritorio.

**Para qué sirve:** evita tener que reunir y mantener por tu cuenta cada componente del sistema.

Debian, Ubuntu, Fedora y Red Hat Enterprise Linux (RHEL) son ejemplos de distribuciones. Comparten conceptos, pero difieren en decisiones de integración, versiones y administración. Se estudian en detalle en los módulos 15 y 16; hoy no instalarás paquetes.

| Término | Qué identifica | Ejemplo |
|---|---|---|
| Núcleo | Una parte central del sistema | Linux |
| Distribución | Un sistema integrado y mantenido | Debian |
| Shell | Un intérprete de órdenes | Bash |
| Terminal | Una interfaz de entrada y salida de texto | La ventana donde escribes órdenes |

**Error frecuente:** copiar una guía de otra distribución porque también dice «Linux». Primero se comprueba el sistema y después la compatibilidad de la instrucción.

**Tu ejercicio:** ¿por qué dos equipos con núcleo Linux podrían necesitar instrucciones diferentes para instalar un programa? No necesitas nombrar todavía ningún gestor.

## 6. Terminal y shell: solo lo necesario para empezar

La terminal muestra texto y recibe lo que escribes. La shell interpreta la orden. Bash es una shell, pero no la única. CLI significa interfaz de línea de comandos. En el Módulo 2 se profundizará en estas diferencias.

Una orden sencilla suele tener esta forma:

```text
comando opción argumento
```

El comando indica la acción; una opción cambia cómo actúa; un argumento puede señalar el objeto sobre el que trabaja. No todas las órdenes necesitan las tres partes.

En los bloques siguientes copia únicamente la orden. No añadas los símbolos `$` o `#` que algunas guías muestran como indicador de entrada. Ejecuta una línea, lee la respuesta y solo después pasa a la siguiente. Las salidas y los mensajes pueden aparecer en otro idioma.

## 7. Práctica A — Identificar el entorno sin cambiar su configuración

**Tipo:** consulta. **Privilegios:** usuario normal. **Requisito:** terminal de Linux, no PowerShell. Las órdenes consultan información; no actualizan ni instalan software.

### Paso 1. Nombre del núcleo

```bash
uname -s
```

- `uname` muestra información del sistema.
- `-s` pide el nombre del núcleo.
- En el entorno Linux previsto se espera `Linux`.

Si ves otra cosa, conserva el mensaje y revisa el entorno antes de seguir. La salida anterior es esperada, no una medición de tu computadora. [GNU: uname](https://www.gnu.org/software/coreutils/manual/html_node/uname-invocation.html).

### Paso 2. Versión de ejecución del núcleo

```bash
uname -r
```

- Se utiliza otra vez `uname`.
- `-r` solicita la identificación de la versión de ejecución del núcleo.
- Anota el resultado tal como aparece; puede incluir letras y sufijos del proveedor. No se espera un número fijo para aprobar.

Esto no indica por sí solo la versión de la distribución. [GNU: uname](https://www.gnu.org/software/coreutils/manual/html_node/uname-invocation.html).

### Paso 3. Identidad de la distribución

```bash
cat /etc/os-release
```

- `cat` muestra el contenido del archivo indicado.
- `/etc/os-release` es una ruta absoluta: empieza por `/`, la raíz del árbol de archivos.
- Busca `PRETTY_NAME`, un nombre legible del sistema; `ID` identifica la distribución y `VERSION_ID`, cuando existe, su versión.

No ejecutes como órdenes las líneas que aparecen en la salida. Solo léelas. En un contenedor, esos datos describen su entorno de usuarios; no bastan para deducir la distribución del equipo anfitrión. [Especificación de os-release, fuente del proyecto systemd](https://github.com/systemd/systemd/blob/main/man/os-release.xml).

Si el archivo no existe, no lo crees ni lo descargues: registra el error. La práctica deberá adaptarse al entorno. Su presencia tampoco prueba por sí sola que systemd esté actuando como gestor del sistema.

**Ejercicio corto:** indica qué orden usarías para conocer la distribución y cuál para consultar el núcleo. Explica por qué son dos consultas diferentes.

## 8. Práctica B — Preparar `~/linux-lab`

**Tipo:** navegación y creación de una carpeta. **Privilegios:** usuario normal. Esta práctica crea un directorio si no existe; no borra ni vacía contenidos. Aun así, lee cada paso antes de ejecutarlo.

Un directorio es una carpeta. `~` representa tu directorio personal en Bash cuando se usa como en los ejemplos. `~/linux-lab` será nuestra carpeta de ejercicios. No es un contenedor ni una protección automática contra errores.

### Paso 1. Ir al directorio personal

```bash
cd ~
```

`cd` cambia el directorio de trabajo de la shell. `~` señala tu directorio personal. No mueve ni cambia archivos. Si falla, detente. No pegues los pasos restantes como un bloque automático.

### Paso 2. Comprobar dónde estás

```bash
pwd
```

`pwd` muestra el directorio de trabajo actual. Una ruta ilustrativa es `/home/estudiante`; en tu equipo puede ser diferente. No copies esa ruta ilustrativa como si fuera la tuya.

Si estás trabajando como administrador del sistema o la ubicación no corresponde a tu usuario normal, pausa la práctica y revisa la sesión. No uses `sudo` para resolverlo.

### Paso 3. Inspeccionar el contenido

```bash
ls
```

`ls` muestra las entradas no ocultas del directorio actual. Una salida vacía no implica un fallo. Los archivos ocultos se estudiarán después.

Si aparece `linux-lab`, inspecciona esa entrada antes de continuar:

```bash
ls -ld ~/linux-lab
```

`-l` solicita detalles y `-d` muestra la entrada de la carpeta en lugar de listar su interior. El primer carácter `d` identifica un directorio, `l` un enlace y `-` un archivo ordinario. Si es un enlace o no es un directorio, detente: no lo reemplaces. Si no comprendes la salida, pide ayuda antes de continuar. Los enlaces se explicarán en el Módulo 5.

### Paso 4. Crear la carpeta de trabajo

```bash
mkdir -p ~/linux-lab
```

- `mkdir` crea directorios.
- `-p` permite crear componentes necesarios y no falla únicamente porque el directorio ya exista.
- `~/linux-lab` fija el destino en tu carpeta personal; no depende de escribir un nombre de usuario.

Si ya existe una carpeta normal con ese nombre, sus archivos se conservan. Si hay un archivo ordinario con ese nombre, la orden falla: no lo borres. Si hay un error de permisos, detente y revisa usuario y ruta; no añadas `sudo` automáticamente. [GNU: mkdir](https://www.gnu.org/software/coreutils/manual/html_node/mkdir-invocation.html).

### Paso 5. Entrar y verificar

Ejecuta una línea cada vez:

```bash
cd ~/linux-lab
pwd
ls
```

1. `cd ~/linux-lab` cambia a la carpeta del laboratorio. Si falla, no continúes.
2. `pwd` permite verificar la ubicación. Debe corresponder al laboratorio de tu usuario; si hay una diferencia inesperada, pausa y revísala.
3. `ls` permite observar su contenido. Puede estar vacío o conservar trabajos anteriores. No elimines nada para que coincida con un ejemplo.

**Resultado esperado:** puedes explicar dónde está el laboratorio y cómo comprobar que has entrado. No necesitas que esté vacío.

**Error de comillas:** no escribas `cd "~/linux-lab"` en Bash esperando la misma expansión. Las comillas impiden que ese `~` inicial se expanda. En este caso usamos `cd ~/linux-lab`. Más adelante aprenderás a citar variables de ruta según su contexto. [GNU Bash: expansión de tilde](https://www.gnu.org/s/bash/manual/html_node/Tilde-Expansion.html).

## 9. Errores frecuentes y corrección mínima

| Situación | Causa posible | Qué hacer |
|---|---|---|
| `command not found` | Orden mal escrita o entorno diferente | Revisar la escritura y qué terminal se abrió; no instalar al azar |
| `No such file or directory` | Ruta ausente o mal escrita | Comparar la ruta con la lección; detener la secuencia |
| `Permission denied` | Usuario o ubicación inadecuados | Revisar sesión y destino; no anteponer `sudo` automáticamente |
| `mkdir` informa que existe un archivo | El nombre puede estar ocupado por un archivo | Conservarlo y revisar; no borrarlo para continuar |
| `uname -r` no muestra «Ubuntu» | Se consultó el núcleo | Usar la consulta de distribución, sin modificar nada |
| El laboratorio tiene archivos | Puede contener prácticas previas | Conservarlas; no es requisito dejarlo vacío |

## 10. Práctica independiente y comprobación

Primero responde sin volver a los ejemplos:

1. Explica núcleo, distribución y shell usando tus propias palabras.
2. Identifica qué consulta permite conocer tu distribución. Ejecútala solo si el entorno está preparado.
3. Entra al laboratorio y comprueba tu ubicación sin copiar la secuencia.
4. Detecta el problema en esta afirmación: «Si `cd` falla, puedo ejecutar igualmente el siguiente comando de modificación».
5. Explica por qué una carpeta de laboratorio no impide afectar otros archivos.

Pistas si te bloqueas: la orden que cambia de directorio empieza con `c`; la que muestra dónde estás empieza con `p`. Si no puedes continuar, vuelve al paso concreto y registra qué no comprendiste.

### Mini evaluación

- ¿Linux y Bash son el mismo tipo de componente?
- ¿Conocer el núcleo basta para elegir instrucciones de administración para cualquier distribución?
- ¿`mkdir -p` vacía una carpeta existente?
- ¿Por qué debes leer el resultado de una orden antes de ejecutar la siguiente?

No se incluyen respuestas junto a las preguntas para que puedas intentarlo primero. La corrección debe señalar aciertos, explicar cada error y proponer una variante. En la siguiente sesión se repetirá una comprobación con otro ejemplo; una ejecución correcta hoy no certifica dominio.

## 11. Registro de aprendizaje y entrega

Puedes responder en el chat con esta ficha. No hace falta crear archivos adicionales ni aprender un editor todavía.

```text
Entorno: Linux / máquina virtual / WSL / pendiente de identificar
Distribución y versión, si las pude consultar:
Nombre y versión del núcleo, si los pude consultar:
En mis palabras, un núcleo es:
En mis palabras, una distribución es:
En mis palabras, una shell es:
¿Pude entrar al laboratorio y comprobarlo?:
Un error que sé reconocer:
Qué necesito practicar otra vez:
Estado: EN APRENDIZAJE / PRACTICADO
```

Antes de compartir o guardar la ficha, omite nombres personales, rutas que identifiquen personas, nombres privados de equipos, direcciones de red y cualquier secreto. No copies automáticamente toda la salida de tu terminal. El tutor revisará la ficha antes de conservarla en GitHub con un nombre nuevo, sin sobrescribir ejercicios previos.

**Estado de esta lección:** revisada documentalmente. Las consultas específicas de Linux y la práctica en la distribución del estudiante deben validarse en ese entorno; no se presentan como ejecutadas en su equipo.
