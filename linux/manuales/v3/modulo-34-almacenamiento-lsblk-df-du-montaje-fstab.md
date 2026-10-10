# Módulo 34 — Almacenamiento: `lsblk`, `df`, `du`, montaje y `fstab`

Manual Maestro de Linux y Shell Scripting — Edición 2026 · v3 · Trigésima cuarta entrega.

[Índice del manual](README.md) · [← Módulo 33](modulo-33-git-github-para-scripts.md) · [Arquitectura](00-indice-arquitectura.md) · [Módulo 35 →](modulo-35-defensa-actualizaciones-minimo-privilegio-aide.md)

## 1. Propósito del módulo

Este módulo introduce almacenamiento desde una regla central:

> **primero inspeccionar; después comprender; solo entonces modificar.**

El objetivo de evidencia definido por la arquitectura es:

> **Separar inspección de cambios de alto impacto.**

Durante esta lección **no montaremos discos reales, no desmontaremos sistemas de archivos reales y no editaremos `/etc/fstab`**.

## 2. Qué aprenderás

Al terminar este módulo podrás:

- distinguir dispositivo de bloque, partición, sistema de archivos y punto de montaje;
- usar `lsblk` para inspeccionar dispositivos de bloque;
- usar `lsblk --fs` para consultar sistemas de archivos, UUID y puntos de montaje;
- usar `findmnt` para consultar montajes actuales;
- usar `df` para consultar espacio del sistema de archivos;
- usar `du` para estimar espacio utilizado por archivos/directorios;
- explicar por qué `df` y `du` pueden mostrar cifras diferentes;
- explicar qué significa montar un sistema de archivos;
- explicar qué ocurre con el contenido previo de un directorio usado como punto de montaje;
- reconocer opciones como `ro`, `rw`, `noauto`, `nofail`, `user` y `defaults`;
- leer los seis campos de una línea de `/etc/fstab`;
- explicar por qué se prefieren identificadores persistentes como `UUID=`;
- consultar `/etc/fstab` sin modificarlo;
- crear una **copia de práctica** con sintaxis tipo fstab;
- validar esa copia con `findmnt --verify --tab-file` sin montarla;
- reconocer por qué `mount -a`, edición real de `fstab`, particionado y formateo son operaciones de alto impacto.

## 3. Modelo mental del almacenamiento

Un modelo inicial:

```text
dispositivo de bloque
        ↓
partición o volumen
        ↓
sistema de archivos
        ↓
punto de montaje
        ↓
archivos y directorios visibles
```

No todos los sistemas usan exactamente una relación uno-a-uno entre estas capas.

## 4. Qué es un dispositivo de bloque

Es un dispositivo que Linux maneja mediante acceso por bloques.

Ejemplos frecuentes:

```text
discos
SSD
particiones
volúmenes lógicos
dispositivos de almacenamiento virtuales
```

Los nombres concretos dependen del sistema.

## 5. Qué es una partición

Una partición es una división lógica de un dispositivo de almacenamiento.

Una partición **puede** contener un sistema de archivos, pero también puede tener otros usos.

No confundas:

```text
partición ≠ sistema de archivos
```

## 6. Qué es un sistema de archivos

Es la estructura utilizada para organizar datos y metadatos.

Ejemplos habituales en Linux:

```text
ext4
xfs
btrfs
vfat
tmpfs
```

Cada tipo tiene características y reglas propias.

## 7. Qué es un punto de montaje

Es el directorio del árbol Linux donde un sistema de archivos se hace accesible.

Ejemplo conceptual:

```text
dispositivo/sistema de archivos → /datos
```

Al montarse, sus archivos aparecen bajo `/datos`.

## 8. Qué ocurre si el directorio ya tenía contenido

Cuando otro sistema de archivos se monta sobre un directorio, el contenido previo de ese directorio deja de ser accesible por esa ruta mientras el montaje permanece activo.

No significa necesariamente que se haya borrado.

Esta es una razón para comprobar el punto de montaje antes de realizar cambios.

## 9. `lsblk`: inspeccionar dispositivos

```bash
lsblk
```

`lsblk` lista información sobre dispositivos de bloque.

Es una operación de **consulta**.

## 10. Salida en árbol

La salida predeterminada suele representar relaciones entre dispositivos:

```text
disco
├─ partición
└─ partición
```

Pero configuraciones complejas pueden producir relaciones más elaboradas.

## 11. `lsblk --fs`

```bash
lsblk --fs
```

muestra información orientada a sistemas de archivos.

En util-linux equivale a solicitar columnas como:

```text
NAME
FSTYPE
FSVER
LABEL
UUID
FSAVAIL
FSUSE%
MOUNTPOINTS
```

## 12. UUID

Un UUID identifica de forma persistente un sistema de archivos.

Ejemplo conceptual:

```text
UUID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

Para configuración persistente suele ser preferible a depender exclusivamente de un nombre como `/dev/sdb1`, porque ciertos nombres de dispositivos pueden cambiar entre arranques o según detección.

## 13. `lsblk` para scripts

Cuando una salida vaya a ser procesada por un script, no dependas de las columnas predeterminadas.

Selecciona columnas explícitas:

```bash
lsblk -o NAME,SIZE,FSTYPE,UUID,MOUNTPOINTS
```

La documentación de util-linux advierte que la salida predeterminada puede cambiar.

## 14. No adivines el disco por su nombre

No asumas:

```text
/dev/sda siempre es X
/dev/sdb siempre es USB
```

Antes de cualquier operación administrativa real debes identificar el dispositivo mediante varias evidencias:

- tamaño;
- modelo;
- tipo;
- sistema de archivos;
- UUID;
- punto de montaje;
- contexto del equipo.

## 15. `findmnt`: inspeccionar sistemas montados

```bash
findmnt
```

`findmnt` muestra sistemas de archivos montados y sus relaciones.

Es preferible a parsear la salida histórica de `mount` en scripts.

## 16. Buscar el sistema de archivos de una ruta

```bash
findmnt --target "$HOME"
```

`--target` acepta un archivo o directorio y muestra el sistema de archivos que contiene esa ruta.

## 17. Consultar un punto de montaje concreto

Ejemplo:

```bash
findmnt --mountpoint /
```

consulta si `/` es un punto de montaje y muestra su información.

## 18. Elegir columnas en `findmnt`

```bash
findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS
```

Para automatización, declarar columnas evita depender de la salida predeterminada.

## 19. `df`: espacio del sistema de archivos

```bash
df
```

`df` informa sobre espacio utilizado y disponible en sistemas de archivos.

Versión más legible para humanos:

```bash
df -h
```

## 20. Consultar el sistema de archivos de una ruta con `df`

```bash
df -h "$HOME"
```

Esto responde principalmente:

```text
¿cuánto espacio tiene y cuánto usa el sistema de archivos que contiene esta ruta?
```

## 21. `df -T`

En GNU/Linux:

```bash
df -hT
```

incluye el tipo del sistema de archivos.

No confundas el tipo con el nombre del dispositivo.

## 22. `du`: uso atribuido a archivos y directorios

```bash
du
```

`du` estima espacio utilizado por un conjunto de archivos.

Para una carpeta concreta:

```bash
du -sh ~/linux-lab
```

## 23. `du -s` y `du -h`

```text
-s / --summarize       → un total por argumento
-h / --human-readable  → unidades legibles
```

Por eso:

```bash
du -sh directorio
```

es una consulta muy común.

## 24. `df` y `du` responden preguntas distintas

```text
df → estado del sistema de archivos
du → espacio asociado a archivos/directorios recorridos
```

No esperes que sus cifras sean siempre idénticas.

## 25. Por qué pueden diferir

Entre otras causas:

- archivos eliminados que siguen abiertos por procesos;
- bloques reservados o metadatos del sistema de archivos;
- archivos sparse;
- permisos que impiden a `du` recorrer parte del árbol;
- montajes dentro del árbol;
- diferencias entre espacio lógico y bloques realmente asignados.

Una diferencia no significa automáticamente que una herramienta esté equivocada.

## 26. Consultar primero el laboratorio

```bash
cd ~/linux-lab
pwd
du -sh .
df -h .
findmnt --target .
```

Estas órdenes son de **consulta**.

## 27. Qué significa montar

Montar significa asociar un sistema de archivos a un punto del árbol de directorios.

Forma conceptual:

```text
mount FUENTE DESTINO
```

Esto es una operación de **modificación del estado del sistema**.

En este módulo no la ejecutaremos sobre dispositivos reales.

## 28. Antes de montar: qué debe verificarse

En una administración real, como mínimo:

1. fuente correcta;
2. sistema de archivos correcto;
3. destino correcto;
4. que el destino no tenga un montaje inesperado;
5. contenido previo del destino;
6. opciones de montaje;
7. permisos necesarios;
8. estrategia de recuperación.

## 29. Consultar si una ruta está montada

```bash
findmnt --mountpoint /ruta
```

o para saber qué sistema contiene una ruta:

```bash
findmnt --target /ruta
```

Estas dos preguntas no son exactamente iguales.

## 30. Opciones de montaje básicas

Algunas opciones comunes:

```text
ro       → solo lectura
rw       → lectura y escritura
noauto   → no incluir en montaje automático por `mount -a`
nofail   → no tratar ausencia del dispositivo como error crítico en ciertos flujos
user     → permite determinados montajes por usuario no root
defaults → conjunto de comportamiento por defecto dependiente del sistema/filesystem
```

No memorices `defaults` como una lista universal rígida; consulta la documentación del entorno.

## 31. `ro` no vuelve mágicamente seguro todo

Un montaje de solo lectura reduce la posibilidad de escribir a través de ese montaje.

Pero no:

- valida el contenido;
- vuelve confiables los archivos;
- impide ejecutar todos los tipos de contenido;
- corrige una fuente equivocada.

## 32. Desmontar también modifica el sistema

La orden:

```text
umount PUNTO
```

separa un sistema de archivos del árbol.

Puede fallar si está ocupado y puede afectar aplicaciones que lo estén usando.

No la practicamos sobre sistemas reales en este módulo.

## 33. Qué es `/etc/fstab`

`/etc/fstab` contiene información estática sobre sistemas de archivos que el sistema puede montar.

Es leído por varias herramientas y servicios.

Un error puede afectar montajes durante el arranque.

Por eso **no editaremos el archivo real en esta lección**.

## 34. Consultar `/etc/fstab`

```bash
cat /etc/fstab
```

o:

```bash
findmnt --fstab
```

Son operaciones de consulta.

Antes de compartir su salida públicamente, revisa si contiene UUID, rutas de red u otra información que no quieras divulgar.

## 35. Los seis campos de `fstab`

Una entrada se describe mediante seis campos principales. Los campos quinto y sexto pueden omitirse y, en ese caso, toman el valor 0:

```text
1. fuente
2. punto de montaje
3. tipo de sistema de archivos
4. opciones
5. dump
6. orden de fsck
```

Ejemplo conceptual:

```text
UUID=...  /datos  xfs  defaults  0  0
```

## 36. Campo 1: fuente

Puede identificar la fuente mediante:

- `UUID=`;
- `LABEL=`;
- `PARTUUID=`;
- `PARTLABEL=`;
- ruta de dispositivo;
- otras fuentes según el tipo de montaje.

Para almacenamiento persistente local suele preferirse un identificador persistente.

## 37. Campo 2: punto de montaje

Es la ruta donde aparecerá el sistema de archivos.

Ejemplo:

```text
/datos
```

Si contiene espacios o tabulaciones, `fstab` usa escapes especiales; no debes simplemente escribir espacios literales y esperar que se interpreten como parte del campo.

## 38. Campo 3: tipo

Ejemplos:

```text
xfs
ext4
vfat
tmpfs
nfs
cifs
```

El tipo debe corresponder al recurso.

## 39. Campo 4: opciones

Es una lista separada por comas.

Ejemplo:

```text
defaults,noauto
```

Las opciones válidas dependen también del tipo de sistema de archivos.

## 40. Campo 5: `fs_freq`

Tradicionalmente lo utiliza `dump` para decidir qué sistemas deben respaldarse.

Si no se especifica, su valor predeterminado es `0`.

En muchas configuraciones modernas aparece como `0`.

## 41. Campo 6: `fs_passno`

Se relaciona con el orden de comprobación mediante `fsck` durante el arranque.

Si se omite `fs_passno`, el valor predeterminado es `0`. El significado apropiado depende del sistema de archivos y de la política del sistema.

No cambies este valor por ensayo y error.

## 42. systemd y `fstab`

En sistemas systemd, `systemd-fstab-generator` transforma dinámicamente entradas de `fstab` en unidades de montaje.

Esto explica por qué modificar `fstab` puede tener consecuencias más amplias que una simple línea de texto.

## 43. `mount -a`: operación de alto impacto

`mount -a` intenta montar las entradas aplicables de `fstab`, normalmente excepto las marcadas con `noauto`.

Por eso:

```text
NO se usa como validador inocuo.
```

Para revisar sintaxis y consistencia preferimos primero herramientas de validación.

## 44. `findmnt --verify`

```bash
findmnt --verify
```

puede verificar la parseabilidad y usabilidad de la tabla de montaje.

Pero aplicado sin opciones trabaja sobre la configuración real.

Para el laboratorio utilizaremos:

```text
--tab-file ARCHIVO
```

con una copia creada por nosotros.

## 45. Preparar laboratorio de `fstab` sin tocar `/etc/fstab`

```bash
test -d ~/linux-lab && \
cd ~/linux-lab && \
mkdir -p modulo-34-almacenamiento/origen-bind && \
mkdir -p modulo-34-almacenamiento/punto-bind && \
cd modulo-34-almacenamiento && pwd
pwd
```

Solo creamos directorios ordinarios.

## 46. Crear una tabla de práctica

```bash
printf '%s %s none bind 0 0\n' \
  "$HOME/linux-lab/modulo-34-almacenamiento/origen-bind" \
  "$HOME/linux-lab/modulo-34-almacenamiento/punto-bind" \
  > fstab-practica
```

Este archivo **no es `/etc/fstab`**.

No cambia montajes.

## 47. Leer la tabla de práctica

```bash
cat fstab-practica
```

Identifica sus seis campos.

## 48. Validar la tabla de práctica

```bash
findmnt --verify --verbose --tab-file fstab-practica
```

Esta práctica verifica la tabla indicada sin instalarla como `/etc/fstab`.

Si informa un error, detente y entiende el diagnóstico antes de cambiar nada.

## 49. Crear un error deliberado y seguro

Haz una segunda copia:

```bash
cp fstab-practica fstab-error
```

Edita **solo `fstab-error`** para introducir una línea mal formada; por ejemplo, deja una línea con únicamente el nombre de la fuente, sin punto de montaje ni tipo. Omitir únicamente el quinto o sexto campo no constituye por sí solo un error: sus valores predeterminados son `0`.

Después:

```bash
findmnt --verify --verbose --tab-file fstab-error
```

El objetivo es aprender a detectar una configuración incorrecta sin afectar el sistema.

## 50. No copies la práctica a `/etc/fstab`

El archivo de laboratorio usa rutas del usuario y existe solo con fines pedagógicos.

No debes hacer:

```text
sudo cp fstab-practica /etc/fstab
```

Esa acción reemplazaría configuración crítica del sistema.

## 51. Por qué una copia previa importa

Antes de una modificación real de `fstab`, una administración responsable necesita:

- copia verificable del archivo anterior;
- identificar exactamente el sistema de archivos;
- confirmar UUID;
- comprobar punto de montaje;
- validar sintaxis;
- plan de recuperación si el arranque falla.

Esta lección se detiene antes de esa fase administrativa.

## 52. No formatear para aprender este módulo

Órdenes como:

```text
mkfs
wipefs
fdisk
parted
```

pueden alterar o destruir estructuras de almacenamiento.

No son necesarias para alcanzar los objetivos del Módulo 34.

Se mantienen fuera de las prácticas.

## 53. No usar `dd` para preparar dispositivos aquí

`dd` puede sobrescribir grandes cantidades de datos con una orden equivocada.

No necesitamos usarlo para aprender `lsblk`, `df`, `du`, montajes y `fstab`.

## 54. Práctica A — mapa del almacenamiento

Ejecuta únicamente consultas:

```bash
lsblk
lsblk --fs
findmnt
df -h
```

Después explica:

```text
qué es dispositivo
qué es filesystem
qué está montado
qué espacio está disponible
```

## 55. Práctica B — una ruta concreta

```bash
findmnt --target "$HOME/linux-lab"
df -h "$HOME/linux-lab"
du -sh "$HOME/linux-lab"
```

Explica por qué las tres órdenes responden preguntas distintas.

## 56. Práctica C — columnas explícitas

```bash
lsblk -o NAME,SIZE,FSTYPE,UUID,MOUNTPOINTS
findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS
```

Identifica qué columnas pertenecen al dispositivo y cuáles al montaje.

## 57. Práctica D — leer `fstab` real sin modificar

```bash
findmnt --fstab
```

Después:

```bash
cat /etc/fstab
```

Compara cómo presenta la información cada herramienta.

No edites el archivo.

## 58. Práctica E — validar archivo de laboratorio

```bash
findmnt --verify --verbose --tab-file fstab-practica
```

Explica:

- qué archivo se validó;
- por qué no fue `/etc/fstab`;
- por qué esto es más seguro que probar cambios reales.

## 59. Errores frecuentes

| Error | Problema | Corrección |
|---|---|---|
| confundir disco con filesystem | son capas distintas | construir modelo dispositivo → filesystem → mountpoint |
| creer que `df` y `du` miden exactamente lo mismo | responden preguntas distintas | usar cada herramienta según objetivo |
| asumir `/dev/sdb` por memoria | nombres pueden cambiar | identificar con `lsblk`, UUID y contexto |
| editar `/etc/fstab` para «probar» | puede afectar arranque | usar copia de laboratorio |
| usar `mount -a` como simple prueba | puede montar muchas entradas | validar primero con `findmnt --verify` |
| montar sobre directorio con datos | oculta temporalmente contenido previo | revisar destino antes |
| copiar UUID de otro equipo | identifica otro filesystem | obtenerlo del sistema correcto |
| usar `sudo` innecesariamente | aumenta impacto | consultas normales primero |
| probar `mkfs`/`wipefs` en un disco | riesgo de pérdida de datos | no usar en este módulo |
| parsear salida predeterminada de `lsblk` en script | columnas pueden cambiar | definir `-o` explícitamente |

## 60. Detección de error 1

Analiza:

```text
UUID=abc /datos ext4 defaults 0
```

La ausencia del sexto campo no demuestra por sí sola un error: si se omite, `fs_passno` toma el valor `0`. El ejemplo tampoco demuestra que `UUID=abc` identifique un sistema de archivos existente. Hay que distinguir una entrada parseable de una fuente y un destino utilizables.

No lo pruebes instalándolo.

Colócalo en una copia de laboratorio y valida con:

```bash
findmnt --verify --verbose --tab-file archivo-prueba
```

## 61. Detección de error 2

Analiza:

```text
quiero montar un USB y supongo que siempre es /dev/sdb1
```

Problema: el nombre no constituye identificación suficiente.

Primero:

```bash
lsblk --fs
```

y verifica tamaño, filesystem, UUID, montaje y contexto.

## 62. Detección de error 3

Analiza:

```bash
sudo mount -a
```

después de editar varias líneas de `fstab` sin validarlas.

Problema: intenta aplicar múltiples montajes y puede afectar el sistema.

El flujo correcto empieza con:

```text
copia
revisión
identificación
validación
plan de recuperación
```

## 63. Método seguro del manual

1. consulta con `lsblk`, `findmnt`, `df` y `du`;
2. identifica la capa que estás observando;
3. no adivines dispositivos;
4. prefiere identificadores persistentes para configuraciones permanentes;
5. revisa el punto de montaje;
6. no edites `fstab` durante exploración;
7. prueba sintaxis en una copia;
8. valida antes de aplicar;
9. documenta procedimiento de recuperación;
10. aumenta privilegios solo cuando una tarea real lo requiera y comprendas el efecto.

## 64. Práctica independiente

Crea `informe_almacenamiento.sh`.

Debe:

1. usar Bash;
2. ejecutar solo operaciones de consulta;
3. mostrar `lsblk` con columnas explícitas;
4. mostrar `df -h` para `~/linux-lab`;
5. mostrar `du -sh` para `~/linux-lab`;
6. usar `findmnt --target` para esa ruta;
7. no usar `sudo`;
8. no montar ni desmontar;
9. no leer dispositivos con herramientas destructivas;
10. pasar `bash -n`;
11. pasar ShellCheck si está disponible;
12. poder explicar qué pregunta responde cada comando.

## 65. Mini evaluación

1. ¿dispositivo de bloque y sistema de archivos son exactamente lo mismo? A) Sí B) No
2. ¿`lsblk` sirve para listar dispositivos de bloque? A) Sí B) No
3. ¿`lsblk --fs` muestra información de filesystem/UUID? A) Sí B) No
4. ¿`findmnt` sirve para consultar montajes? A) Sí B) No
5. ¿`df` y `du` responden exactamente la misma pregunta? A) Sí B) No
6. ¿`du -sh directorio` resume uso de ese árbol? A) Sí B) No
7. ¿montar puede ocultar temporalmente contenido previo del punto de montaje? A) Sí B) No
8. ¿`/etc/fstab` tiene seis campos principales por entrada? A) Sí B) No
9. ¿UUID suele ser más persistente que un nombre `/dev/sdX`? A) Sí B) No
10. ¿`mount -a` es una operación puramente de consulta? A) Sí B) No
11. ¿`findmnt --verify --tab-file` permite validar otra tabla? A) Sí B) No
12. ¿editaremos `/etc/fstab` real en esta práctica? A) Sí B) No
13. ¿`mkfs` es necesario para aprender este módulo? A) Sí B) No
14. ¿debes confirmar el punto de montaje antes de montar? A) Sí B) No
15. ¿salida predeterminada de `lsblk` debe asumirse estable en scripts? A) Sí B) No

## 66. Registro de aprendizaje

```text
Dispositivo de bloque significa:
Partición significa:
Sistema de archivos significa:
Punto de montaje significa:
`lsblk` responde:
`lsblk --fs` añade:
`findmnt` responde:
`df` responde:
`du` responde:
¿por qué pueden diferir df y du?:
UUID sirve para:
Los seis campos de fstab son:
`noauto` significa:
`findmnt --verify` sirve para:
¿por qué no usamos mount -a para probar?:
Algo que todavía confundo:
Estado: EN APRENDIZAJE / PRACTICADO
```

## 67. Puerta de dominio

Para considerar este módulo **DOMINADO** deberás poder en más de una práctica:

1. distinguir dispositivo, filesystem y punto de montaje;
2. leer una salida básica de `lsblk --fs`;
3. explicar `df` frente a `du`;
4. localizar el filesystem de una ruta con `findmnt`;
5. enumerar los seis campos de `fstab`;
6. explicar por qué UUID es útil;
7. validar una tabla de práctica sin editar `/etc/fstab`;
8. identificar por qué `mount -a`, `mkfs` y edición de `fstab` son cambios de mayor impacto.

## 68. Fuentes y límites

Clasificación y estado de los enlaces de esta sección: [catálogo de fuentes](06-catalogo-fuentes.md) (jerarquía E04, comprobación del 9 de octubre de 2026).

Fuentes principales:

- util-linux upstream (código fuente y manuales de `lsblk`, `findmnt`, `mount`, `fstab`): https://github.com/util-linux/util-linux
- util-linux upstream (documentación del proyecto): https://www.kernel.org/pub/linux/utils/util-linux/
- Las páginas man7 siguientes se mantienen como copias HTML prácticas, no como fuente upstream.
- util-linux — `lsblk(8)`: https://man7.org/linux/man-pages/man8/lsblk.8.html
- util-linux — `findmnt(8)`: https://man7.org/linux/man-pages/man8/findmnt.8.html
- util-linux — `mount(8)`: https://man7.org/linux/man-pages/man8/mount.8.html
- util-linux — `fstab(5)`: https://man7.org/linux/man-pages/man5/fstab.5.html
- GNU Coreutils — `df` y `du`: https://www.gnu.org/software/coreutils/manual/coreutils.html
- Red Hat Enterprise Linux 10 — Mounting file systems: https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_file_systems/mounting-file-systems
- Red Hat Enterprise Linux 10 — Persistently mounting file systems: https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_file_systems/persistently-mounting-file-systems

Puntos verificados documentalmente:

- `lsblk` lista dispositivos de bloque y `--fs` solicita información de sistemas de archivos;
- util-linux recomienda columnas explícitas cuando la salida se procesa en scripts;
- `findmnt` consulta sistemas de archivos montados y puede buscar por target/mountpoint;
- `findmnt --verify` puede comprobar una tabla y `--tab-file` permite indicar un archivo distinto de `/etc/fstab`;
- `df` informa espacio de sistemas de archivos y `du` estima espacio utilizado por archivos;
- montar un filesystem sobre un directorio hace inaccesible por esa ruta el contenido anterior mientras el montaje está activo;
- `fstab` describe fuente, punto de montaje, tipo, opciones, campo dump y orden de fsck;
- RHEL 10 documenta el uso de UUID para montajes persistentes y la generación de unidades systemd a partir de `fstab`;
- `mount -a` intenta aplicar las entradas correspondientes de `fstab` y por eso no es una operación de validación inocua.

Se posponen:

- particionado real con `fdisk`/`parted`;
- creación de filesystems con `mkfs`;
- borrado de firmas con `wipefs`;
- LVM;
- RAID;
- LUKS;
- cuotas;
- montaje NFS/CIFS real;
- recuperación de filesystems;
- edición administrativa real de `/etc/fstab`;
- montaje de imágenes mediante loop devices;
- tuning de opciones específicas de ext4/xfs/btrfs.

**Estado de la lección:** redactada y revisada documentalmente contra util-linux, GNU Coreutils y RHEL 10. Todas las prácticas son de consulta o utilizan archivos/directorios ordinarios dentro de `~/linux-lab`; no se modifican discos ni la tabla real `/etc/fstab`.

---

**Siguiente:** [Módulo 35 — Defensa, actualizaciones, mínimo privilegio, auditoría y AIDE](modulo-35-defensa-actualizaciones-minimo-privilegio-aide.md) · [Volver al índice](README.md)
