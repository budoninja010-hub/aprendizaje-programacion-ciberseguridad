# Módulo 32 — Copias, sincronización y restauración con `rsync`

Manual Maestro de Linux y Shell Scripting — Edición 2026 · v3 · Trigésima segunda entrega.

[Índice del manual](README.md) · [← Módulo 31](modulo-31-tar-gzip-xz-archivos-compresion.md) · [Arquitectura](00-indice-arquitectura.md) · [Módulo 33 →](modulo-33-git-github-para-scripts.md)

## 1. Qué aprenderás

Al terminar este módulo podrás:

- explicar qué hace `rsync` y qué no hace;
- distinguir copia, sincronización, espejo y respaldo con historial;
- comprobar si `rsync` está instalado y conocer su versión;
- realizar copias locales seguras;
- explicar la diferencia entre `origen` y `origen/`;
- usar `-a` comprendiendo qué conserva y qué no;
- usar `-v`, `-i`, `--stats` y `--dry-run` para revisar operaciones;
- excluir archivos mediante `--exclude`;
- entender cómo decide rsync si un archivo necesita actualizarse;
- reconocer cuándo `--checksum` puede ser útil y su coste;
- verificar una restauración en una carpeta separada;
- comprender el riesgo de `--delete` y simularlo antes de cualquier uso real;
- explicar por qué sincronización no sustituye automáticamente una política de backups;
- reconocer el uso remoto de rsync sobre SSH únicamente en equipos propios o autorizados;
- diseñar una copia reproducible sin sobrescribir datos de práctica innecesariamente.

Conocimientos previos:

- rutas absolutas y relativas;
- archivos y permisos;
- SSH en sistemas autorizados;
- compresión y restauración;
- estados de salida;
- Bash y quoting.

**Seguridad:** las prácticas se realizan únicamente dentro de `~/linux-lab/modulo-32-rsync`. No se sincronizan carpetas personales reales, unidades externas, servidores, configuraciones del sistema ni rutas remotas. `--delete` se estudia primero y se practica únicamente con `--dry-run` en este módulo.

## 2. Qué es `rsync`

`rsync` es una herramienta para transferir y sincronizar archivos de forma incremental.

Puede trabajar:

- entre dos rutas locales;
- entre una máquina local y otra remota;
- mediante un daemon rsync;
- mediante un shell remoto como SSH.

En este módulo la práctica principal será **local**.

## 3. Qué significa transferencia incremental

Después de una primera copia, rsync intenta evitar transferir de nuevo archivos que considera ya actualizados.

Modelo:

```text
primera ejecución → copia inicial
segunda ejecución → compara
                 → transfiere solo lo necesario
```

Eso puede ahorrar tiempo y transferencia.

## 4. Copia no es lo mismo que respaldo histórico

Si sincronizas:

```text
origen → destino
```

el destino puede terminar reflejando el estado actual del origen.

Pero un respaldo con historial suele necesitar además:

- versiones anteriores;
- snapshots;
- retención;
- protección frente a borrados accidentales;
- pruebas de restauración.

`rsync` puede formar parte de un sistema de backups, pero por sí solo no garantiza esas propiedades.

## 5. Sincronización y espejo

Una **sincronización** puede copiar cambios del origen al destino.

Un **espejo** intenta que el destino se parezca aún más al origen, incluyendo eventualmente eliminar elementos sobrantes mediante opciones como `--delete`.

Esa diferencia es crítica.

## 6. Comprobar si `rsync` está instalado

```bash
command -v rsync
```

Después:

```bash
rsync --version
```

En octubre de 2026, la versión oficial más reciente publicada por el proyecto rsync es 3.5.1. Eso **no significa** que tu distribución tenga que usar esa misma versión; primero revisa la versión instalada y el soporte de tu distribución.

## 7. Preparar el laboratorio

```bash
test -d ~/linux-lab && \
cd ~/linux-lab && \
mkdir -p modulo-32-rsync/origen && \
mkdir -p modulo-32-rsync/destino && \
mkdir -p modulo-32-rsync/restauracion && \
cd modulo-32-rsync && pwd
pwd
```

Etiqueta: **creación en laboratorio**.

## 8. Crear datos de práctica

```bash
printf 'uno\n' > origen/uno.txt
printf 'dos palabras\n' > 'origen/dos palabras.txt'
mkdir -p origen/subcarpeta
printf 'tres\n' > origen/subcarpeta/tres.txt
```

Comprueba:

```bash
find origen -maxdepth 3 -print
```

## 9. Primera copia simple

```bash
rsync -av origen/ destino/
```

Explicación inicial:

```text
-a → modo archivo
-v → salida más detallada
origen/ → contenido del directorio origen
destino/ → directorio receptor
```

## 10. La barra final cambia el significado

Este es uno de los puntos más importantes de rsync.

Con:

```bash
rsync -a origen/ destino/
```

se copian **los contenidos de `origen`** dentro de `destino`.

Con:

```bash
rsync -a origen destino/
```

se copia el directorio `origen` como un elemento dentro de `destino`.

Conceptualmente:

```text
origen/ → copia contenido
origen  → copia el directorio contenedor
```

## 11. Verificar el resultado

```bash
find destino -maxdepth 3 -print
```

No confíes únicamente en que rsync terminó sin mensajes de error. Revisa la estructura.

## 12. Qué incluye `-a`

`-a/--archive` equivale a:

```text
-r  recursión
-l  enlaces simbólicos
-p  permisos
-t  tiempos de modificación
-g  grupo
-o  propietario
-D  archivos de dispositivo/especiales
```

De forma compacta:

```text
-a = -rlptgoD
```

## 13. Qué NO incluye `-a`

`-a` no implica automáticamente, entre otros:

```text
-A → ACL
-X → atributos extendidos
-H → conservación de relaciones de hardlinks
```

Tampoco implica conservar todos los metadatos posibles de todos los sistemas.

Por eso «usar `-a`» no significa «copia perfecta de cualquier filesystem».

## 14. Usuario normal y propietario/grupo

Opciones como conservación de propietario o grupo están sujetas a permisos y capacidades del sistema.

En nuestras prácticas todos los archivos pertenecen al usuario del laboratorio.

No usaremos `sudo` para forzar metadatos.

## 15. Simular antes de cambiar

`--dry-run` o `-n` realiza una prueba sin aplicar cambios de transferencia.

```bash
rsync -av --dry-run origen/ destino/
```

Es una de las herramientas más importantes antes de una sincronización sensible.

## 16. `--dry-run` no sustituye la revisión

Una simulación muestra qué **pretende** hacer rsync según las opciones actuales.

Aun debes revisar:

- origen;
- destino;
- barra final;
- exclusiones;
- opciones de borrado;
- sistema remoto, si existiera.

## 17. `--itemize-changes` (`-i`)

Para ver cambios con más detalle:

```bash
rsync -ai --dry-run origen/ destino/
```

`-i` muestra una representación compacta de lo que cambiaría.

Para aprendizaje, combínalo con `--dry-run`.

## 18. `--stats`

```bash
rsync -a --stats origen/ destino/
```

muestra estadísticas de la transferencia.

Puede ayudarte a distinguir cuántos archivos se examinaron y transfirieron.

## 19. Segunda ejecución sin cambios

Ejecuta de nuevo:

```bash
rsync -avi origen/ destino/
```

Como el destino ya debería estar actualizado, la transferencia será mínima o nula.

Esto ilustra el comportamiento incremental.

## 20. Modificar un archivo de práctica

```bash
printf 'línea nueva\n' >> origen/uno.txt
```

Después primero simula:

```bash
rsync -avi --dry-run origen/ destino/
```

Revisa qué archivo cambiaría.

## 21. Aplicar la actualización

Si la simulación coincide con tu intención:

```bash
rsync -avi origen/ destino/
```

Después:

```bash
cat destino/uno.txt
```

## 22. Cómo decide normalmente rsync

Sin `--checksum`, rsync normalmente utiliza una comprobación rápida basada principalmente en:

- tamaño;
- tiempo de modificación.

Si esos datos indican que el archivo está actualizado, puede omitirlo sin leer todo su contenido.

## 23. `--checksum` (`-c`)

Con:

```bash
rsync -ac origen/ destino/
```

rsync decide si necesita actualizar archivos comparando checksums de contenido en lugar de la comprobación rápida habitual.

Esto requiere leer los datos de ambos lados y puede ser mucho más costoso.

No lo uses automáticamente en todas las copias.

## 24. Checksum para decisión vs verificación de transferencia

La opción `--checksum` afecta principalmente la decisión de **si un archivo necesita actualizarse**.

Es distinta de las comprobaciones que rsync usa normalmente para verificar datos que realmente transfirió.

No interpretes `-c` como una garantía universal de backup correcto.

## 25. Excluir archivos

Ejemplo:

```bash
printf 'temporal\n' > origen/no-copiar.tmp
```

Simula:

```bash
rsync -avi --dry-run --exclude='*.tmp' origen/ destino/
```

El archivo `.tmp` debería quedar fuera de la transferencia.

## 26. Las exclusiones también importan con borrado

Las reglas de inclusión/exclusión pueden interactuar con opciones de eliminación.

No mezcles `--delete`, `--delete-excluded` y filtros complejos sin revisar exactamente qué quedará protegido o en riesgo.

En este módulo no usamos `--delete-excluded`.

## 27. Qué hace `--delete`

`--delete` elimina del destino ciertos archivos que ya no existen en el conjunto de origen.

Su propósito es acercar el destino a un espejo.

Eso significa que **puede borrar datos del destino**.

## 28. Regla permanente para `--delete`

Antes de cualquier uso real:

1. confirma origen;
2. confirma destino;
3. confirma la barra final;
4. revisa filtros;
5. usa `--dry-run`;
6. usa `-i`;
7. revisa cada borrado propuesto;
8. conserva otro respaldo si el contenido importa.

## 29. Práctica de `--delete` SOLO en simulación

Crea un archivo únicamente en el destino:

```bash
printf 'solo destino\n' > destino/sobrante.txt
```

Ahora:

```bash
rsync -avi --dry-run --delete origen/ destino/
```

Observa que rsync propondría eliminar `sobrante.txt`.

**No retires `--dry-run` en esta práctica.**

## 30. Variantes de eliminación

rsync ofrece opciones como:

```text
--delete-before
--delete-during
--delete-delay
--delete-after
```

Cambian en qué momento se realizan eliminaciones.

No necesitas memorizarlas todavía.

La opción importante para este nivel es comprender que todas implican riesgo de borrado.

## 31. `--remove-source-files` no es una opción de backup

`--remove-source-files` elimina archivos del lado emisor después de una transferencia exitosa.

Este manual **no la usa** en las prácticas de copia.

Convertir una copia en un movimiento cambia completamente el riesgo.

## 32. Restaurar significa probar el camino inverso

Una copia no está completamente demostrada hasta que puedes recuperar datos.

En lugar de restaurar sobre `origen`, usaremos:

```text
restauracion/
```

## 33. Restauración de prueba

Primero verifica que la carpeta esté vacía:

```bash
ls -la restauracion
```

Después simula:

```bash
rsync -avi --dry-run destino/ restauracion/
```

Si es correcto:

```bash
rsync -avi destino/ restauracion/
```

## 34. Verificar la restauración

```bash
find restauracion -maxdepth 3 -print
```

Después compara un archivo:

```bash
cmp origen/uno.txt restauracion/uno.txt
```

`cmp` termina sin salida cuando los archivos comparados son iguales.

## 35. Comparación con hashes

También puedes calcular:

```bash
sha256sum origen/uno.txt restauracion/uno.txt
```

Si ambos hashes son iguales, el contenido de esos archivos coincide para esta comprobación.

No necesitas usar hashes para cada copia normal, pero son útiles en ejercicios de verificación.

## 36. Verificación del árbol completo: concepto

Comparar únicamente un archivo no demuestra que todo el árbol esté correcto.

Una política real de backup debe definir:

- qué datos se incluyen;
- qué metadatos importan;
- cómo se verifica;
- con qué frecuencia se restaura de prueba;
- cuánto historial se conserva.

## 37. Copia local a otra carpeta no protege de todo

Si origen y destino están en el mismo disco:

- un fallo físico del disco puede afectar ambos;
- ransomware o errores del usuario pueden alcanzar ambos;
- un borrado con privilegios suficientes puede afectar ambos.

El laboratorio enseña la herramienta; no representa por sí mismo una estrategia completa de resiliencia.

## 38. Remoto sobre SSH: concepto

En sistemas propios o expresamente autorizados, rsync puede usar SSH.

Forma general:

```text
rsync opciones origen/ usuario@host:ruta/
```

o en dirección inversa:

```text
rsync opciones usuario@host:ruta/ destino/
```

No practicaremos con hosts externos en este módulo.

## 39. `-e ssh`

Rsync puede especificar el shell remoto:

```text
rsync -a -e ssh origen/ usuario@host:ruta/
```

En muchos usos remotos modernos SSH ya es el transporte esperado.

No insertes contraseñas, tokens ni claves privadas en comandos o scripts.

## 40. `-z` en transferencias

`-z/--compress` comprime datos durante la transferencia.

Puede ayudar en redes lentas con datos compresibles.

Puede aportar poco o incluso consumir recursos innecesarios para:

- archivos ya comprimidos;
- transferencias locales;
- redes muy rápidas.

No confundas `rsync -z` con crear un archivo `.gz` permanente.

## 41. No versionar secretos

Si preparas scripts de rsync para GitHub, no incluyas:

- contraseñas;
- claves SSH privadas;
- tokens;
- cookies;
- archivos `.env`;
- nombres de host privados si revelan información sensible;
- datos personales innecesarios.

## 42. Enlaces simbólicos

`-a` incluye `-l`, por lo que conserva enlaces simbólicos como enlaces.

Otras opciones pueden cambiar cómo se tratan los enlaces.

No uses opciones que sigan enlaces fuera del árbol sin comprender su efecto.

## 43. `--copy-links` y riesgos de alcance

`--copy-links` (`-L`) transforma enlaces simbólicos encontrados en los objetos a los que apuntan.

Eso puede hacer que el conjunto copiado sea distinto del esperado.

Este manual no lo utiliza en las prácticas.

## 44. Hardlinks

`-a` no incluye `-H`.

Si necesitas preservar relaciones de hardlinks, existe:

```text
-H / --hard-links
```

Puede aumentar el uso de memoria y tiempo.

No lo activamos sin una necesidad concreta.

## 45. ACL y atributos extendidos

Si el entorno requiere conservarlos, rsync dispone de:

```text
-A → ACL
-X → xattrs
```

No todas las copias necesitan esos metadatos, pero debes decidirlo explícitamente en backups reales.

## 46. Evitar escribir en el destino equivocado

Antes de ejecutar:

```bash
pwd
find origen -maxdepth 2 -print
find destino -maxdepth 2 -print
```

Después ejecuta primero:

```bash
rsync -avi --dry-run origen/ destino/
```

El nombre `destino` no es una protección: verifica su ruta real.

## 47. Práctica A — copia inicial

```bash
rsync -avi --dry-run origen/ destino/
rsync -avi origen/ destino/
find destino -maxdepth 3 -print
```

## 48. Práctica B — cambio incremental

```bash
printf 'cambio\n' >> origen/uno.txt
rsync -avi --dry-run origen/ destino/
```

Predice qué archivo aparecerá como cambiado.

Después aplica la sincronización.

## 49. Práctica C — exclusión

```bash
printf 'temporal\n' > origen/ignorar.tmp
rsync -avi --dry-run --exclude='*.tmp' origen/ destino/
```

Explica por qué `ignorar.tmp` no se transferiría.

## 50. Práctica D — restauración

```bash
rsync -avi --dry-run destino/ restauracion/
rsync -avi destino/ restauracion/
cmp origen/uno.txt restauracion/uno.txt
```

Si `cmp` no produce salida y devuelve `0`, esos dos archivos coinciden.

## 51. Práctica E — observar `--delete` sin borrar

```bash
printf 'solo destino\n' > destino/sobrante.txt
rsync -avi --dry-run --delete origen/ destino/
```

Identifica exactamente qué propondría eliminar.

No ejecutes la misma orden sin `--dry-run` en este ejercicio.

## 52. Errores frecuentes

| Error | Problema | Corrección |
|---|---|---|
| olvidar la barra final del origen | cambia la estructura copiada | predice antes `origen` vs `origen/` |
| usar `--delete` directamente | puede borrar datos del destino | primero `--dry-run -i` |
| creer que sincronización = backup histórico | puede propagar pérdidas | diseña retención/versiones aparte |
| asumir que `-a` conserva todo | no incluye ACL/xattrs/hardlinks | define metadatos requeridos |
| usar `-c` siempre | fuerza lectura de contenido y cuesta más | úsalo cuando haya razón |
| usar `-z` localmente por costumbre | puede añadir CPU sin beneficio | evalúa transporte/datos |
| restaurar encima del origen | puedes reemplazar datos | restaura primero en carpeta separada |
| usar rutas remotas sin autorización | acceso indebido | solo equipos propios/autorizados |
| incluir secretos en scripts | riesgo de exposición | usa gestión segura y no GitHub |
| usar `--remove-source-files` en un backup | elimina el origen | no usar en este módulo |

## 53. Detección de error 1

Analiza:

```bash
rsync -a origen destino/
```

Si pretendías copiar **el contenido** de `origen` directamente dentro de `destino`, falta la barra final.

Corrección:

```bash
rsync -a origen/ destino/
```

## 54. Detección de error 2

Analiza:

```bash
rsync -a --delete ~/Documentos/ /mnt/copia/
```

sin haber verificado rutas ni hecho simulación.

Problema: `--delete` puede eliminar elementos del destino.

Primer paso correcto:

```text
verificar origen y destino
realizar --dry-run -i
revisar cada eliminación propuesta
```

No uses esa ruta real como práctica.

## 55. Detección de error 3

Analiza:

```bash
rsync -a destino/ origen/
```

Si querías hacer backup pero invertiste origen y destino, puedes propagar una versión antigua hacia el lugar equivocado.

Regla:

> lee siempre la orden como «desde ORIGEN hacia DESTINO» antes de ejecutarla.

## 56. Método seguro del manual

1. identifica origen y destino;
2. confirma si quieres el directorio o su contenido;
3. inspecciona ambos lados;
4. usa `--dry-run`;
5. usa `-i` para entender cambios;
6. evita opciones de borrado durante aprendizaje;
7. aplica la copia solo cuando la simulación sea correcta;
8. verifica el resultado;
9. realiza una restauración de prueba;
10. documenta qué metadatos y exclusiones forman parte del diseño.

## 57. Práctica independiente

Crea `copia_laboratorio.sh`.

Debe:

1. usar Bash;
2. aceptar dos argumentos: origen y destino;
3. comprobar que el origen sea un directorio;
4. comprobar que el destino esté dentro de `~/linux-lab/modulo-32-rsync`;
5. mostrar primero la orden en modo `--dry-run`;
6. requerir que el estudiante ejecute la transferencia real por separado, no automáticamente después de la simulación;
7. usar `-a`, `-i` y quoting correcto;
8. no incluir `--delete`;
9. no usar `sudo`;
10. pasar `bash -n`;
11. pasar ShellCheck si está disponible;
12. explicar la diferencia entre `origen` y `origen/`.

## 58. Mini evaluación

1. ¿rsync puede hacer transferencias incrementales? A) Sí B) No
2. ¿`origen/` y `origen` significan exactamente lo mismo? A) Sí B) No
3. ¿`--dry-run` aplica cambios reales? A) Sí B) No
4. ¿`-i` ayuda a identificar cambios? A) Sí B) No
5. ¿`-a` incluye ACL automáticamente? A) Sí B) No
6. ¿`-a` incluye xattrs automáticamente? A) Sí B) No
7. ¿`-a` incluye preservación de hardlinks automáticamente? A) Sí B) No
8. ¿`--checksum` puede requerir leer más datos? A) Sí B) No
9. ¿`--delete` puede borrar archivos del destino? A) Sí B) No
10. ¿debes usar `--delete` sin simulación en este módulo? A) Sí B) No
11. ¿sincronización simple garantiza historial de versiones? A) Sí B) No
12. ¿una restauración de prueba ayuda a validar un backup? A) Sí B) No
13. ¿`-z` crea necesariamente un `.gz` permanente? A) Sí B) No
14. ¿rsync remoto debe limitarse a sistemas propios/autorizados? A) Sí B) No
15. ¿es importante comprobar la dirección origen → destino? A) Sí B) No

## 59. Registro de aprendizaje

```text
`rsync` sirve para:
Transferencia incremental significa:
Diferencia entre copia y backup histórico:
`origen/` significa:
`origen` sin barra significa:
`-a` incluye:
`-a` NO incluye:
`--dry-run` sirve para:
`-i` sirve para:
`--checksum` cambia:
`--exclude` sirve para:
`--delete` hace:
¿por qué `--delete` es peligroso?:
¿por qué restauramos en otra carpeta?:
Dirección de una orden rsync:
Algo que todavía confundo:
Estado: EN APRENDIZAJE / PRACTICADO
```

## 60. Puerta de dominio

Para considerar este módulo **DOMINADO** deberás poder en más de una ocasión:

1. predecir la diferencia entre `origen` y `origen/`;
2. realizar una simulación y explicar sus cambios;
3. ejecutar una sincronización local sin opciones de borrado;
4. explicar qué conserva `-a` y qué no;
5. usar una exclusión sencilla;
6. explicar por qué `--delete` requiere revisión especial;
7. restaurar hacia una carpeta separada;
8. verificar al menos un archivo restaurado;
9. explicar por qué rsync solo no constituye necesariamente un sistema completo de backups.

## 61. Fuentes y límites

Fuentes principales:

- Sitio oficial de rsync: https://rsync.samba.org/
- Anuncio original de rsync 3.5.1, 21 de septiembre de 2026: https://lists.samba.org/archive/rsync/2026-September/033395.html

**Fecha de verificación de la versión:** 8 de octubre de 2026. La página oficial publica 3.5.1 (21-09-2026). No confundir versión upstream con la disponible en repositorios de Debian, Ubuntu, Fedora o RHEL; comprobar siempre `rsync --version` y los avisos de seguridad de la distribución.
- Manual oficial `rsync(1)`: https://rsync.samba.org/ftp/rsync/rsync.1

Puntos verificados documentalmente:

- rsync proporciona transferencia incremental de archivos;
- `--dry-run` realiza una simulación sin efectuar cambios;
- `-a/--archive` equivale a `-rlptgoD` y no incluye `-A`, `-X` ni `-H`;
- la barra final en una ruta de origen cambia si se transfiere el directorio contenedor o su contenido;
- `--delete` elimina archivos sobrantes del lado receptor según el conjunto y reglas aplicables;
- `--checksum` cambia la selección de archivos hacia comprobación por checksum en lugar de la comprobación rápida habitual;
- `-z/--compress` comprime datos durante la transferencia y no significa crear automáticamente un archivo `.gz`;
- la versión oficial más reciente publicada al 8 de octubre de 2026 es rsync 3.5.1, mientras que la versión instalada depende de la distribución.

Se posponen:

- daemon rsync y `rsyncd.conf`;
- `--link-dest` para snapshots basados en hardlinks;
- backups incrementales con retención;
- `--backup` y `--backup-dir` como estrategia;
- filtros avanzados y archivos de reglas;
- `--files-from`;
- límites de filesystem y dispositivos con `-x`;
- seguridad avanzada de symlinks;
- automatización remota;
- pruebas de recuperación ante desastre.

**Estado de la lección:** redactada y revisada documentalmente contra el manual oficial de rsync 3.5.1. Las prácticas son locales y `--delete` se limita a simulación con `--dry-run`.

---

**Siguiente:** [Módulo 33 — Git y GitHub para scripts; puente al itinerario específico de Git](modulo-33-git-github-para-scripts.md) · [Volver al índice](README.md)
