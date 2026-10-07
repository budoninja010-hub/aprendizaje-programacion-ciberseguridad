# Módulo 5 — Árbol de archivos, FHS, /etc, /usr, /var, /tmp, /proc, /sys y enlaces

Manual Maestro de Linux y Shell Scripting — Edición 2026 · v3 · Quinta entrega.

[Estado actual](README.md) · [Módulo anterior](modulo-04-rutas-absolutas-relativas-espacios.md) · [Arquitectura](00-indice-arquitectura.md)

## 1. Qué aprenderás

Al terminar este módulo podrás:

- explicar qué significa que Linux presente un árbol de archivos con raíz `/`;
- distinguir la función general de `/etc`, `/usr`, `/var`, `/tmp`, `/proc` y `/sys`;
- reconocer que una distribución puede organizar algunos directorios de forma distinta sin dejar de ser GNU/Linux;
- diferenciar un directorio real de una vista virtual proporcionada por el kernel;
- reconocer un enlace simbólico y explicar que puede apuntar a otro nombre o ruta;
- inspeccionar estos elementos sin modificar la configuración del sistema.

Conocimientos previos: Módulo 3 (`pwd`, `ls`, `cd`) y Módulo 4 (rutas absolutas, relativas, `~`, `.`, `..` y espacios).

**Seguridad:** este módulo es principalmente de lectura. No editarás archivos de `/etc`, no escribirás en `/proc` ni `/sys`, no borrarás nada y no usarás `sudo`. Algunas entradas de `/proc` y `/sys` pueden ser escribibles y modificar el sistema; por eso aquí solo se consultan rutas y metadatos.

## 2. Un solo árbol que empieza en /

En GNU/Linux, los archivos y directorios se presentan dentro de un árbol jerárquico. La parte superior se llama **raíz** y se representa con:

```text
/
```

No confundas:

- `/` = raíz del árbol;
- `~` = abreviatura de Bash para el directorio personal;
- `.` = directorio actual.

Ejemplo conceptual simplificado:

```text
/
├── etc/
├── home/
├── tmp/
├── usr/
├── var/
├── proc/
└── sys/
```

El esquema no muestra todos los directorios posibles ni garantiza que tu sistema tenga exactamente esa presentación. Una distribución, un contenedor o un entorno especializado puede diferir.

**Para qué sirve este modelo:** cuando una orden usa una ruta como `/etc/os-release`, sabes que comienza desde la raíz y no desde tu carpeta actual.

**Error típico:** pensar que `/` significa “mi carpeta personal”. El directorio personal suele estar en otra ubicación y se representa cómodamente con `~` en Bash.

**Ejercicio:** explica con tus palabras la diferencia entre `/` y `~`.

## 3. Qué es FHS

**FHS** significa *Filesystem Hierarchy Standard*. Es una especificación que describe propósitos y ubicaciones convencionales dentro de jerarquías de sistemas tipo Unix/Linux.

La versión publicada de referencia de la serie 3 es **FHS 3.0**, publicada en 2015. Sigue siendo útil como mapa conceptual, pero no debes interpretarla como una fotografía exacta de todas las distribuciones actuales.

La FHS describe, entre otros, directorios como:

- `/etc`: configuración específica del sistema;
- `/usr`: jerarquía secundaria con programas y datos de usuario del sistema;
- `/var`: datos variables;
- `/tmp`: archivos temporales.

También contempla que ciertos nombres de la raíz puedan ser enlaces a otros directorios.

**Regla del manual:** aprenderemos primero el propósito general y después comprobaremos cómo lo implementa la distribución real. No memorizaremos una lista completa como si fuera universal.

Referencia: [Filesystem Hierarchy Standard 3.0](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html).

## 4. /etc — configuración del sistema

La FHS define `/etc` como ubicación para **configuración específica del sistema anfitrión**.

Ejemplos que ya has visto:

```text
/etc/os-release
/etc/passwd
/etc/group
```

Eso no significa que debas editar esos archivos.

### Consulta segura

Puedes observar los nombres del directorio con:

```bash
ls /etc
```

Esta orden lista entradas; no modifica la configuración.

Para volver a consultar la identidad de la distribución:

```bash
cat /etc/os-release
```

Ya estudiaste esta lectura en el Módulo 1.

**Error típico:** pensar que, porque un archivo está en `/etc`, debes abrirlo con privilegios de administrador. Leer y modificar son operaciones distintas. En este módulo no hacemos cambios.

**Ejercicio:** ¿por qué `/etc/os-release` es más apropiado para identificar la distribución que para conocer únicamente la versión del kernel?

## 5. /usr — programas y datos de la jerarquía de usuario del sistema

En FHS, `/usr` es una jerarquía secundaria que contiene gran parte de los programas, bibliotecas y datos distribuidos con el sistema.

Subdirectorios frecuentes:

```text
/usr/bin
/usr/lib
/usr/share
```

No confundas `/usr` con el directorio personal de un usuario. El nombre es histórico; no significa “tu carpeta de usuario”.

En sistemas modernos puede existir un diseño llamado **merged-/usr**, donde nombres históricos como `/bin` o `/sbin` son enlaces hacia ubicaciones dentro de `/usr`. No asumas que todos los sistemas tienen exactamente la misma forma: primero inspecciona.

### Consulta segura

```bash
ls -ld /usr
ls -ld /bin
```

- `-l` muestra detalles.
- `-d` muestra la entrada nombrada en vez de listar su interior.
- Si el primer carácter es `d`, observas un directorio.
- Si es `l`, observas un enlace simbólico.

No importa si `/bin` es directorio o enlace en tu equipo; el objetivo es reconocer el resultado sin cambiar nada.

## 6. /var — datos que cambian durante el funcionamiento

`/var` contiene **datos variables**: información cuyo contenido puede cambiar mientras el sistema funciona.

Dependiendo de la distribución y los servicios instalados, puedes encontrar zonas relacionadas con:

- registros;
- cachés;
- colas;
- estado de aplicaciones;
- datos de servicios.

Ejemplos comunes:

```text
/var/log
/var/cache
```

No todas las distribuciones ni aplicaciones almacenan exactamente lo mismo en cada subdirectorio.

### Consulta segura

```bash
ls -ld /var
ls /var
```

No necesitas abrir registros privados ni copiar su contenido al chat. Más adelante, en el módulo de logs, aprenderás a consultar eventos sin exponer datos sensibles.

**Error típico:** pensar que “variable” significa una variable de programación. Aquí significa que son datos que pueden cambiar con el uso del sistema.

## 7. /tmp — archivos temporales

`/tmp` es una ubicación convencional para archivos temporales.

No debes utilizarla para guardar algo irremplazable. La política de limpieza depende del sistema y de su configuración: algunos entornos eliminan contenido al reiniciar o después de cierto tiempo; otros aplican reglas distintas.

### Consulta segura

```bash
ls -ld /tmp
```

En muchos sistemas verás permisos especiales, pero todavía no necesitas interpretarlos. Los permisos y el **sticky bit** se estudiarán en el Módulo 12.

**Regla:** temporal no significa “seguro para guardar secretos”. Un archivo temporal debe diseñarse con cuidado. Más adelante aprenderás `mktemp`.

**Error típico:** asumir que todo lo almacenado en `/tmp` se elimina inmediatamente o siempre en cada reinicio. No existe esa garantía universal.

## 8. /proc — una vista del kernel y de los procesos

`/proc` normalmente es un **pseudo-sistema de archivos** proporcionado por el kernel. No debe imaginarse simplemente como una carpeta ordinaria llena de documentos almacenados en disco.

Incluye, entre otras cosas:

- información del sistema;
- datos asociados a procesos;
- subdirectorios cuyo nombre puede ser un PID;
- parámetros del kernel bajo determinadas rutas.

Ejemplo:

```bash
ls -ld /proc
ls /proc
```

La segunda salida puede cambiar mientras el sistema está funcionando porque los procesos aparecen y desaparecen.

Otra consulta de lectura:

```bash
cat /proc/version
```

La salida depende del kernel y de cómo fue construido. No necesitas memorizarla.

**Advertencia importante:** algunas rutas bajo `/proc/sys` permiten modificar parámetros del kernel. En este curso no escribirás ahí durante los módulos iniciales.

Referencia: [Linux Kernel Documentation — The /proc Filesystem](https://docs.kernel.org/filesystems/proc.html).

**Error típico:** creer que cada entrada de `/proc` corresponde a un archivo permanente guardado en el disco.

## 9. /sys — objetos y dispositivos expuestos por el kernel

`/sys` suele ser el punto de montaje de **sysfs**, una interfaz que expone objetos del kernel, dispositivos y atributos relacionados.

Puedes inspeccionar su estructura:

```bash
ls -ld /sys
ls /sys
```

Es común encontrar categorías como:

```text
/sys/class
/sys/devices
/sys/bus
```

Su presencia exacta depende del entorno.

**Advertencia:** algunas entradas de sysfs son escribibles y pueden cambiar el comportamiento de dispositivos o del sistema. En este módulo solo observamos nombres y rutas.

**Error típico:** pensar que todo lo visible como “archivo” dentro de `/sys` es un archivo de texto normal almacenado en el disco.

Referencia general: [Linux Kernel Documentation — sysfs](https://docs.kernel.org/filesystems/sysfs.html).

## 10. Directorio real, pseudo-sistema de archivos y punto de montaje

Ya puedes separar tres ideas:

1. Un directorio como `~/linux-lab` pertenece al árbol normal de tu espacio de archivos.
2. `/proc` y `/sys` suelen presentar información dinámica mediante sistemas de archivos virtuales.
3. Un directorio puede funcionar como **punto de montaje**, donde se integra otro sistema de archivos dentro del árbol.

No aprenderás todavía a montar discos. Esa operación puede afectar el acceso a datos y se reserva para el Módulo 34.

**Ejercicio:** explica por qué `/proc` puede cambiar aunque no hayas creado ni borrado archivos manualmente.

## 11. Qué es un enlace simbólico

Un **enlace simbólico** (*symbolic link* o *symlink*) es un tipo especial de archivo que contiene una ruta hacia otro nombre.

Modelo mental:

```text
enlace  ─────►  destino
```

No es una copia del destino.

Un enlace simbólico puede:

- apuntar a un archivo;
- apuntar a un directorio;
- cruzar entre sistemas de archivos;
- quedar “colgando” si su destino ya no existe.

Referencia: [Linux man-pages — symlink(7)](https://man7.org/linux/man-pages/man7/symlink.7.html).

### Reconocer un enlace

```bash
ls -l nombre
```

Una salida ilustrativa puede verse así:

```text
lrwxrwxrwx ... acceso -> destino
```

Lo importante ahora:

- el primer carácter `l` indica enlace simbólico;
- la flecha muestra el texto del destino en una salida típica de `ls -l`.

No copies la salida ilustrativa como si fuera la de tu equipo.

## 12. Enlace simbólico y enlace duro: diferencia inicial

Linux también tiene **enlaces duros** (*hard links*), pero no los practicaremos todavía.

Idea mínima:

- un enlace simbólico apunta mediante un nombre o ruta;
- un enlace duro es otra entrada de directorio que referencia el mismo objeto subyacente dentro de las restricciones del sistema de archivos.

Un enlace duro ordinario no cruza sistemas de archivos. Los enlaces simbólicos sí pueden hacerlo.

No necesitas aprender inodos todavía. Solo recuerda que “enlace simbólico” y “enlace duro” no son sinónimos.

## 13. Práctica guiada — reconocer y crear un symlink dentro del laboratorio

Esta práctica modifica únicamente tu carpeta de ejercicios. No utiliza `sudo`, no borra nada y no toca `/etc`, `/proc` ni `/sys`.

### Paso A. Entrar al laboratorio

Ejecuta una línea cada vez:

```bash
cd ~/linux-lab
pwd
ls -la
```

Si `cd` falla, detente.

### Paso B. Crear la carpeta del módulo

Comprueba primero si existe:

```bash
ls -ld ./modulo-05-fhs
```

Si responde que no existe, crea únicamente esa carpeta:

```bash
mkdir modulo-05-fhs
```

Si ya existe, inspecciónala. No borres ni sobrescribas su contenido para repetir la práctica.

Después:

```bash
cd ./modulo-05-fhs
pwd
ls -la
```

### Paso C. Crear un destino de práctica

Si el nombre está libre:

```bash
mkdir destino
```

Comprueba:

```bash
ls -ld destino
```

El primer carácter debería corresponder a un directorio.

### Paso D. Crear el enlace simbólico

Solo si no existe una entrada llamada `acceso-destino`:

```bash
ln -s destino acceso-destino
```

Explicación:

- `ln` crea enlaces;
- `-s` solicita un enlace simbólico;
- `destino` es el texto del objetivo;
- `acceso-destino` es el nombre nuevo del enlace.

Ahora inspecciona:

```bash
ls -ld destino acceso-destino
```

Debes poder distinguir cuál es el directorio y cuál es el enlace.

### Paso E. Comprobar que el enlace se puede recorrer

```bash
cd acceso-destino
pwd
```

Bash puede conservar una ruta lógica que incluya el nombre del enlace. Para observar la ruta física resuelta:

```bash
pwd -P
```

No necesitas memorizar `-P` todavía. Solo observa que un enlace puede cambiar cómo se expresa el camino lógico y físico.

Regresa al laboratorio:

```bash
cd ~/linux-lab
pwd
```

**No borres la práctica al terminar.** La conservaremos para ejercicios posteriores.

## 14. Recorrido de inspección del sistema

Ahora harás únicamente consultas.

Ejecuta una línea, observa y explica antes de pasar a la siguiente:

```bash
ls -ld /etc
ls -ld /usr
ls -ld /var
ls -ld /tmp
ls -ld /proc
ls -ld /sys
ls -ld /bin
```

Preguntas:

1. ¿Cuáles aparecen como directorios?
2. ¿Alguno aparece como enlace simbólico?
3. ¿Puedes saber solo con esos resultados qué distribución usas? No necesariamente.
4. ¿Cuál de esas rutas no usarías para guardar tus ejercicios personales? Todas; tus ejercicios siguen en `~/linux-lab`.

No ejecutes `sudo`, no cambies permisos y no intentes “arreglar” un enlace del sistema.

## 15. Errores frecuentes y corrección mínima

| Situación | Problema | Corrección |
|---|---|---|
| “`/usr` es mi carpeta personal” | Confusión por el nombre | El directorio personal se consulta con `~` o `pwd`; `/usr` cumple otra función |
| “Todo lo de `/proc` está guardado en disco” | Se ignora que procfs es virtual | Tratar `/proc` como interfaz dinámica del kernel |
| “Puedo escribir en `/sys` porque parece una carpeta” | Apariencia no implica operación segura | En módulos iniciales, solo lectura |
| “`/tmp` siempre se borra al reiniciar” | Generalización dependiente de política | No guardar ahí información irremplazable |
| “Un symlink es una copia” | El enlace apunta a otro nombre | Verificar el destino; no asumir duplicación de datos |
| “Si `/bin` es un enlace, Linux está dañado” | Sistemas modernos pueden usar merged-/usr | Inspeccionar y documentar; no modificar |
| “FHS obliga a que todos los sistemas sean idénticos” | FHS es un estándar de jerarquía, no una clonación exacta | Consultar distribución y versión reales |

## 16. Práctica independiente

Sin copiar los párrafos anteriores, responde:

1. ¿Qué tipo de información esperarías encontrar en `/etc`?
2. ¿Por qué `/var` recibe ese nombre?
3. ¿Qué precaución debes tener con `/tmp`?
4. ¿Qué diferencia conceptual existe entre `~/linux-lab` y `/proc`?
5. ¿Qué indica el primer carácter `l` en una salida larga de `ls`?
6. ¿Por qué un enlace simbólico puede quedar colgando?
7. Si `/bin` aparece como enlace, ¿debes reemplazarlo por un directorio? Explica por qué no.

Después dibuja un árbol pequeño con:

```text
/
├── etc
├── usr
├── var
├── tmp
├── proc
└── sys
```

y escribe una frase al lado de cada nombre indicando su función general.

## 17. Mini evaluación

1. ¿Cuál es la raíz del árbol de archivos?
   - A) `~`
   - B) `/`
   - C) `.`
   - D) `/home`

2. ¿Qué ruta se asocia principalmente con configuración específica del sistema?
   - A) `/etc`
   - B) `/tmp`
   - C) `/proc`
   - D) `/sys`

3. ¿Qué afirmación sobre `/proc` es correcta?
   - A) Es siempre una carpeta ordinaria de archivos permanentes.
   - B) Suele ser una interfaz virtual hacia información del kernel y procesos.
   - C) Es el directorio personal del administrador.
   - D) Solo contiene programas ejecutables.

4. ¿Un enlace simbólico es una copia completa del destino?
   - A) Sí.
   - B) No.

5. ¿FHS garantiza que todas las distribuciones tengan una estructura idéntica en cada detalle?
   - A) Sí.
   - B) No.

6. ¿Debemos escribir valores en `/proc/sys` o `/sys` durante esta lección?
   - A) Sí.
   - B) No.

No revises las respuestas hasta haber razonado cada punto. El tutor corregirá primero lo acertado y después cada error.

## 18. Registro de aprendizaje

Puedes responder en el chat:

```text
En mis palabras, la raíz / es:
Para mí, /etc sirve principalmente para:
Para mí, /usr sirve principalmente para:
Para mí, /var sirve principalmente para:
Para mí, /tmp sirve principalmente para:
La diferencia entre /proc y una carpeta normal es:
Un enlace simbólico es:
Algo que todavía confundo:
Estado: EN APRENDIZAJE / PRACTICADO
```

No pegues contenidos sensibles de `/etc`, `/proc` o `/sys`. Si una salida contiene nombres privados del equipo, usuarios, rutas personales o datos de red, redáctalos antes de compartirla.

## 19. Fuentes y límites de esta lección

Fuentes principales:

- [Filesystem Hierarchy Standard 3.0](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html).
- [Linux Kernel Documentation — /proc](https://docs.kernel.org/filesystems/proc.html).
- [Linux Kernel Documentation — sysfs](https://docs.kernel.org/filesystems/sysfs.html).
- [Linux man-pages — symlink(7)](https://man7.org/linux/man-pages/man7/symlink.7.html).
- [Linux man-pages — path_resolution(7)](https://man7.org/linux/man-pages/man7/path_resolution.7.html).

FHS 3.0 es una referencia estructural y no se usa para afirmar que cada distribución actual sea idéntica. Las prácticas concretas deben comprobarse en la distribución real del estudiante.

**Estado de la lección:** redactada y revisada documentalmente. La práctica en el equipo del estudiante todavía debe ejecutarse y evaluarse.

Siguiente módulo por redactar: **Módulo 6 — Crear, copiar, mover y renombrar; rm y rmdir con seguridad**.
