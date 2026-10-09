# Módulo 2 — Terminal, CLI, shell, Bash, prompt y ayuda

Manual Maestro de Linux y Shell Scripting — Edición 2026 · v3 · Segunda entrega.

[Índice del manual](README.md) · [← Módulo 1](modulo-01-gnu-linux-kernel-distribuciones.md) · [Arquitectura](00-indice-arquitectura.md) · [Módulo 3 →](modulo-03-navegacion-pwd-ls-cd.md)

## 1. Objetivo y requisitos

Al terminar podrás distinguir la ventana de terminal del programa que interpreta tus órdenes, reconocer dónde escribir y elegir una ayuda adecuada. No necesitas memorizar opciones ni dominar la navegación todavía.

Antes de ejecutar, explica con tus palabras la diferencia entre núcleo y distribución. Confirma que trabajas en una terminal de Linux y que el laboratorio del Módulo 1 está preparado. Si todavía no conoces tu entorno, puedes estudiar la parte conceptual y dejar pendiente la práctica.

**Seguridad:** usuario normal, sin `sudo`, instalaciones, borrados, cambios de permisos ni edición de configuración. Las órdenes previstas consultan información o muestran texto. La shell puede registrar lo que escribes en su historial: no introduzcas contraseñas, tokens ni otros secretos como práctica.

La lección está escrita para Bash. Windows Terminal puede alojar PowerShell o una distribución WSL: el nombre de la ventana no identifica el intérprete. No pegues estos ejemplos en PowerShell esperando el mismo comportamiento.

## 2. Terminal: la interfaz donde entra y sale texto

Una terminal permite enviar entrada y recibir salida textual de programas. En un escritorio, normalmente utilizas un **emulador de terminal**, una aplicación que ofrece esa interfaz en una ventana. También existen consolas de texto sin escritorio gráfico.

**Para qué sirve:** permite trabajar con órdenes y programas interactivos. Abrir la ventana no significa que hayas entrado al kernel ni que tengas privilegios de administrador.

Ejemplo conceptual: la ventana muestra tu orden, la salida y después otra invitación para escribir. La ventana y el programa que interpreta la orden cumplen funciones diferentes.

**Error típico:** «Cambié el color de la terminal, por tanto cambié de shell». El aspecto de la interfaz no determina el intérprete.

**Ejercicio corto:** describe qué parte ves en pantalla y qué parte crees que interpreta el texto.

## 3. CLI: una forma de interacción

CLI significa *Command Line Interface*, interfaz de línea de comandos. Describe una forma de dar instrucciones mediante texto. No es el nombre de una aplicación concreta ni de una distribución.

**Para qué sirve:** permite expresar acciones de manera precisa y reproducible. Una interfaz gráfica permite acciones mediante ventanas, botones y menús; ambas formas pueden coexistir.

Ejemplo: escribir una orden para consultar una versión es una interacción de CLI. Pulsar un botón «Acerca de» es una interacción gráfica. No hay que rechazar la interfaz gráfica para aprender Linux.

**Error típico:** creer que «CLI» significa «Bash». Bash permite interacción por línea de comandos, pero el concepto es más amplio.

**Ejercicio corto:** menciona una diferencia entre una acción escrita y una acción realizada con un botón.

## 4. Shell y Bash

Una **shell** interpreta un lenguaje de órdenes. Puede realizar acciones internas o ejecutar otros programas. **Bash** es una implementación de shell; existen otras, con diferencias de sintaxis y comportamiento.

**Para qué sirve distinguirlas:** una receta válida en Bash no tiene por qué funcionar sin cambios en todas las shells. Tampoco debe asumirse que `/bin/sh` es Bash. [GNU: qué es una shell](https://www.gnu.org/software/bash/manual/html_node/What-is-a-shell_003f.html).

Ejemplo: `cd` necesita cambiar el directorio de trabajo de la shell; Bash ofrece esa operación como orden interna. Un programa externo es un ejecutable separado que la shell puede iniciar. Más adelante estudiarás alias y funciones, que también pueden intervenir al resolver un nombre.

| Concepto | Papel |
|---|---|
| Terminal | Facilita entrada y salida textual |
| CLI | Forma de interacción mediante órdenes |
| Shell | Interpreta órdenes |
| Bash | Una shell concreta |
| Kernel | Núcleo del sistema, presentado en el Módulo 1 |

**Error típico:** utilizar `bash --version` como prueba de que la shell actual es Bash. Esa orden ejecuta el Bash encontrado y consulta su versión; no identifica por sí sola el intérprete desde el que la lanzaste. Tampoco el contenido de la variable `SHELL` garantiza identificar la shell que está ejecutándose ahora.

Para esta práctica utiliza una sesión que sepas que está configurada con Bash. Si no está confirmado, pide ayuda para identificarla; no cambies la shell predeterminada ni edites archivos de inicio. [GNU: invocación de Bash](https://www.gnu.org/software/bash/manual/html_node/Invoking-Bash.html).

**Ejercicio corto:** explica por qué una misma aplicación de terminal podría mostrar sesiones con shells diferentes.

## 5. Prompt: la invitación para escribir

El prompt es texto que muestra la shell para indicar que espera entrada. Este ejemplo es ilustrativo:

```text
estudiante@equipo:~/linux-lab$ 
```

Puede mostrar una etiqueta de usuario, equipo y directorio. Su contenido es configurable; no todas las terminales muestran esta estructura. El símbolo `$` suele usarse en ejemplos de usuario normal y `#` en ejemplos de administrador. **No prueban por sí solos los privilegios de una sesión.**

En la línea ilustrativa siguiente, solo `pwd` es la orden:

```text
estudiante@equipo:~/linux-lab$ pwd
```

Escribe únicamente:

```bash
pwd
```

`pwd` consulta el directorio de trabajo. No copies `estudiante@equipo`, el signo `$` ni una salida del ejemplo. Reconocerás esta orden del Módulo 1.

Bash diferencia el prompt principal de otro que solicita continuar una orden incompleta. Este último suele aparecer como `>`, por ejemplo cuando falta cerrar una comilla. Ese símbolo mostrado por Bash no es una orden que debas copiar. [GNU: comportamiento interactivo](https://www.gnu.org/software/bash/manual/html_node/Interactive-Shell-Behavior.html).

**Error típico:** interpretar cualquier `>` de un tutorial como parte de un comando. Su significado depende del contexto: prompt de continuación o carácter escrito en la orden. Las redirecciones se explican en el Módulo 8.

**Ejercicio corto:** en el ejemplo anterior, separa la invitación, la orden y la información que esperas recibir.

## 6. Primera interacción: escribir, ejecutar y leer

En Bash, ejecuta esta línea y pulsa Enter:

```bash
echo "Estoy aprendiendo a usar la terminal"
```

- `echo` muestra sus argumentos en la salida.
- Las comillas dobles agrupan este texto con espacios; no forman parte del mensaje mostrado.
- El ejemplo utiliza texto literal sencillo, sin opciones ni barras invertidas. No se presenta `echo` como herramienta universal para cualquier dato; más adelante se estudiará `printf`.

Salida esperada:

```text
Estoy aprendiendo a usar la terminal
```

Después normalmente reaparece el prompt. No confundas la salida con una segunda orden. Esta salida es ilustrativa, no una captura de tu equipo. [GNU: órdenes internas](https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html).

**Ejercicio corto:** muestra otra frase sencilla. Antes de pulsar Enter, señala dónde comienza y termina el texto entre comillas.

### Recuperarte de una línea incompleta

Si olvidaste cerrar una comilla y Bash espera más texto, pulsa **Ctrl+C** para cancelar esa entrada y volver a intentarlo. No añadas comandos nuevos a una línea cuyo estado no comprendes. No provoques el error con órdenes de modificación: basta observarlo si ocurre en esta práctica de texto.

Ctrl+C no deshace efectos ya producidos. Mientras corre un programa, normalmente solicita una interrupción y el programa puede reaccionar de distintas formas. Tampoco es equivalente a cerrar la ventana. Si no sabes qué se está ejecutando, lee primero la pantalla. [GNU: señales](https://www.gnu.org/software/bash/manual/html_node/Signals.html).

**Ctrl+D** puede terminar una shell si se pulsa con la línea vacía en la configuración habitual; no lo uses como sustituto de «borrar un carácter». En esta lección no necesitas cerrar la sesión para corregir una orden.

## 7. Ayuda: elegir el punto de consulta

No hace falta adivinar ni instalar software ante cada duda. Empieza por la documentación disponible en tu propio entorno. Estas tres vías se complementan:

| Necesidad | Primera consulta | Condición |
|---|---|---|
| Una orden interna de Bash | `help cd` | Estar usando Bash |
| Ayuda breve de GNU `ls` | `ls --help` | Tener esa implementación disponible |
| Página de manual instalada | `man ls` | Disponer de `man` y de esa página |

`--help` no es una opción universal. No se añade automáticamente a cualquier orden. Si una ayuda falta, usa la referencia oficial enlazada, sin instalar nada todavía.

### A. Ayuda integrada de Bash

```bash
help cd
```

`help` consulta ayuda integrada; `cd` es el tema. Leer esa ayuda no cambia de carpeta. Busca la descripción inicial y una opción, sin intentar memorizar todo.

```bash
type cd
```

`type` indica cómo se interpreta un nombre de orden; aquí examina `cd`, sin ejecutarlo. En una sesión Bash habitual dirá que es una orden interna. Si aparece un alias o función, registra la diferencia y consulta antes de asumir el comportamiento. [GNU: help y type](https://www.gnu.org/s/bash/manual/html_node/Bash-Builtins.html).

### B. Ayuda de una utilidad

```bash
ls --help
```

`ls` es la utilidad; `--help` solicita su ayuda en GNU Coreutils. Lee la descripción y localiza `-a`. No necesitas usarla todavía: el objetivo es encontrar información. El texto y el idioma pueden variar. [GNU: opciones comunes](https://www.gnu.org/software/coreutils/manual/html_node/Common-options.html).

### C. Página de manual

```bash
man ls
```

`man` busca documentación instalada; `ls` es el tema. No ejecuta un listado de archivos. Busca `NAME` (nombre), `SYNOPSIS` (forma de uso) y `DESCRIPTION` (descripción). Si el visualizador es `less`, Espacio avanza, `/palabra` busca y `q` sale; con otro visualizador las teclas pueden variar.

En un esquema como `orden [opción]... archivo`, los corchetes de la sinopsis señalan elementos opcionales y los puntos indican repetición. No copies esa notación literalmente. Esta convención documental no explica todas las apariciones de corchetes en código.

Si aparece «No manual entry» o falta `man`, registra el mensaje y utiliza la ayuda anterior o la documentación oficial. La ausencia de la página no demuestra que el programa esté ausente. [Manual de man-db](https://man7.org/linux/man-pages/man1/man.1.html).

**Ejercicio corto:** elige la ayuda para `cd`, lee su descripción y explica qué aprendiste. Después consulta `ls` mediante otra vía y compara la presentación.

## 8. Práctica guiada en el laboratorio

No se crea ni sobrescribe ningún archivo en esta práctica. El directorio debe existir desde el Módulo 1. Ejecuta una línea cada vez:

```bash
cd ~/linux-lab
pwd
```

1. `cd` cambia la ubicación de trabajo de la shell al laboratorio. Si falla, detente y vuelve a la preparación del Módulo 1.
2. `pwd` comprueba esa ubicación. No se espera una ruta idéntica entre personas.

Luego completa estas acciones por separado:

1. Reconoce el prompt y explica qué parte no debes copiar.
2. Muestra una frase con `echo`.
3. Consulta `help cd` y explica una línea que entiendas.
4. Consulta `type cd`; distingue consultar de ejecutar `cd`.
5. Lee `ls --help` y, si está disponible, `man ls`.
6. Sal del visualizador con su tecla correspondiente y comprueba que vuelve el prompt.

No publiques una captura completa: el prompt puede revelar nombres personales o de equipos. Basta describir el resultado sin esos datos.

## 9. Errores y corrección mínima

| Error o confusión | Por qué puede ocurrir | Corrección |
|---|---|---|
| Escribir `$ pwd` copiando el prompt | Se confundió presentación con orden | Escribir solo `pwd` |
| `help` no se reconoce | Puede ser otra shell o entorno | Comprobar el entorno; no instalar un paquete al azar |
| Bash muestra `>` tras una frase incompleta | Puede faltar una comilla | Cancelar la entrada con Ctrl+C y escribir la frase completa |
| `man ls` no encuentra la página | Documentación no instalada o no localizada | Usar `ls --help` o la referencia oficial |
| Pulsar `q` en el prompt esperando salir del manual | El manual ya no estaba abierto | Distinguir pantalla del visualizador y prompt antes de pulsar teclas |
| Interpretar `$` como prueba de usuario normal | El prompt se puede personalizar | No deducir privilegios solo por su aspecto |
| Pensar que Ctrl+C restaura cambios anteriores | Interrumpir no es deshacer | Revisar el efecto de cada orden antes de ejecutarla |

## 10. Evaluación sin copiar

1. Explica terminal, CLI, shell y Bash con tus palabras.
2. En una línea que contiene un prompt seguido de `help cd`, identifica qué escribirías realmente.
3. Elige cómo consultar una orden interna de Bash y cómo consultar una utilidad GNU.
4. Explica qué harías si `man ls` no encuentra una página.
5. Corrige esta afirmación: «El resultado de `bash --version` demuestra qué shell estoy usando ahora».
6. Muestra una frase nueva sin copiar el ejemplo y explica sus partes.

Pistas: una interfaz y un intérprete no cumplen el mismo papel; consultar una página no ejecuta el programa documentado. Antes de pedir la solución completa, señala qué parte de la pregunta no entiendes.

En otra sesión repite la distinción conceptual con un ejemplo diferente y detecta un error sin ayuda. Se considera **PRACTICADO** después de realizar la actividad; **DOMINADO** requiere evidencia repetida. La redacción terminada del módulo no significa que el estudiante ya lo domine.

## 11. Revisión de esta entrega

Se revisaron progresión, sintaxis de ejemplos, comillas, coherencia con M1, advertencias y fuentes oficiales. Las referencias GNU se contrastaron mediante documentación oficial indexada; no se infiere una versión instalada a partir de ellas. La práctica interactiva en el Linux del estudiante sigue pendiente.

Decisiones de precisión: prompt configurable; `help` específico del entorno Bash; `--help` no universal; documentación ausente distinta de ejecutable ausente; interrupción distinta de deshacer; consulta de versión distinta de identificación de la shell actual.

---

**Siguiente:** [Módulo 3 — Navegación inicial: pwd, ls y cd](modulo-03-navegacion-pwd-ls-cd.md) · [Volver al índice](README.md)

## Anexo editorial — Criterios de evaluación y fuentes

**Qué se conserva:** todas las explicaciones, prácticas y preguntas originales de esta entrega.

**Evaluación formativa:** el estudiante debe explicar los conceptos con sus palabras, ejecutar una práctica segura en su propio entorno cuando corresponda, interpretar la salida y reconocer al menos un error sin copiar la solución. Una respuesta correcta aislada no acredita dominio.

**Registro:** EN APRENDIZAJE / PRACTICADO / DOMINADO (solo tras varias evidencias revisadas). La revisión documental del texto no equivale a práctica realizada.

**Fuentes primarias para contrastar esta lección:**
- GNU Bash Reference Manual: https://www.gnu.org/software/bash/manual/
- GNU Coreutils Manual: https://www.gnu.org/software/coreutils/manual/
- Debian Reference: https://www.debian.org/doc/manuals/debian-reference/
- Linux kernel documentation: https://docs.kernel.org/

Las fuentes se consultan según el tema tratado; no se presume que todos los enlaces respalden cada afirmación del módulo.
