# Módulo 31 — Archivos y compresión con `tar`, `gzip` y `xz`

Manual Maestro de Linux y Shell Scripting — Edición 2026 · v3 · Trigésima primera entrega.

[Índice del manual](README.md) · [← Módulo 30](modulo-30-cron-temporizadores-systemd.md) · [Arquitectura](00-indice-arquitectura.md) · [Módulo 32 →](modulo-32-rsync-copias-restauracion.md)

## 1. Qué aprenderás

Al terminar este módulo podrás:

- distinguir **archivar** de **comprimir**;
- explicar qué hace `tar` y qué hacen `gzip` y `xz`;
- crear un archivo `.tar` sin borrar los originales;
- listar el contenido de un `.tar` antes de extraerlo;
- crear y consultar archivos `.tar.gz` y `.tar.xz`;
- usar `gzip` y `xz` directamente sobre archivos individuales;
- conservar los archivos originales con `-k/--keep` en las primeras prácticas;
- comprobar archivos comprimidos con `gzip -t` y `xz -t`;
- consultar información con `gzip -l` y `xz -l` cuando corresponda;
- extraer en una carpeta nueva y vacía;
- evitar sobrescribir archivos existentes mediante `--keep-old-files`;
- reconocer el propósito de `--one-top-level`;
- explicar por qué no debemos usar `--absolute-names` (`-P`) sin comprender sus implicaciones;
- comparar tamaño original y comprimido sin asumir que “más compresión” siempre es mejor;
- reconocer `.tar`, `.tar.gz`, `.tgz` y `.tar.xz` como convenciones distintas.

Conocimientos previos:

- sistema de archivos y rutas;
- creación, copia y borrado seguro;
- permisos;
- pipes y redirecciones;
- estados de salida;
- Bash básico.

**Seguridad:** todas las prácticas se realizan dentro de `~/linux-lab/modulo-31-archivos`. No se extraen archivos descargados de Internet en directorios personales reales ni del sistema. No se usa `sudo`. Antes de extraer se inspecciona el contenido y se utiliza un destino vacío.

## 2. Archivar no es comprimir

Estos conceptos son distintos.

**Archivar** significa reunir varios archivos y directorios en un solo archivo contenedor.

**Comprimir** significa representar los datos con menos espacio cuando es posible.

Modelo:

```text
varios archivos
      ↓
     tar
      ↓
archivo.tar
      ↓
gzip o xz
      ↓
archivo.tar.gz o archivo.tar.xz
```

## 3. Qué hace `tar`

`tar` crea y manipula archivos de archivo.

Operaciones fundamentales:

```text
-c / --create   → crear
-t / --list     → listar
-x / --extract  → extraer
-f / --file     → indicar el archivo de archivo
```

En este manual escribiremos las opciones de forma explícita y consistente.

## 4. Qué hace `gzip`

`gzip` comprime datos y utiliza normalmente la extensión:

```text
.gz
```

Puede comprimir un archivo individual, pero no reemplaza la función de `tar` para agrupar una jerarquía completa en un solo archivo.

## 5. Qué hace `xz`

`xz` es otra herramienta de compresión.

Su formato nativo usa:

```text
.xz
```

También comprime archivos individuales. Para agrupar primero varios archivos o directorios, normalmente se combina con `tar`.

## 6. Extensiones comunes

| Extensión | Significado habitual |
|---|---|
| `.tar` | archivo tar sin compresión externa |
| `.tar.gz` | archivo tar comprimido con gzip |
| `.tgz` | abreviatura convencional de `.tar.gz` |
| `.tar.xz` | archivo tar comprimido con xz |
| `.gz` | archivo comprimido con gzip |
| `.xz` | archivo comprimido con xz |

Una extensión es una convención; no garantiza por sí sola el contenido real.

## 7. Preparar el laboratorio

```bash
test -d ~/linux-lab && \
cd ~/linux-lab && \
mkdir -p modulo-31-archivos/origen && \
cd modulo-31-archivos && pwd
```

Etiqueta: **creación en laboratorio**.

## 8. Crear datos de práctica

```bash
printf 'línea uno\n' > origen/uno.txt
printf 'línea dos con espacios\n' > 'origen/dos palabras.txt'
mkdir -p origen/subcarpeta
printf 'dato interno\n' > origen/subcarpeta/tres.txt
```

Estas redirecciones sobrescriben únicamente los archivos de práctica con esos nombres dentro del laboratorio.

## 9. Revisar antes de archivar

```bash
find origen -maxdepth 3 -print
```

Comprueba que solo aparecen los objetos que esperas.

## 10. Crear un `.tar`

```bash
tar -cf practica.tar origen
```

Interpretación:

```text
-c → crear archivo
-f → el siguiente argumento es el nombre del archivo tar
practica.tar → archivo de salida
origen → objeto que se archiva
```

Los archivos originales permanecen en `origen`.

## 11. Listar antes de extraer

```bash
tar -tf practica.tar
```

`-t` lista miembros del archivo.

Esta operación **no extrae** el contenido.

Regla del manual:

> Antes de extraer un archivo, inspecciona primero sus miembros.

## 12. Lista detallada

```bash
tar -tvf practica.tar
```

`-v` muestra información adicional como permisos, tamaños y nombres.

Esta vista ayuda a reconocer:

- archivos;
- directorios;
- enlaces;
- rutas inesperadas.

## 13. Crear un tar comprimido con gzip

GNU tar puede invocar gzip mediante `-z`:

```bash
tar -czf practica.tar.gz origen
```

Ahora tienes un archivo tar y compresión gzip en una sola operación.

## 14. Listar un `.tar.gz`

```bash
tar -tzf practica.tar.gz
```

De nuevo: primero listar, después decidir si extraer.

## 15. Crear un tar comprimido con xz

GNU tar puede usar xz mediante `-J`:

```bash
tar -cJf practica.tar.xz origen
```

## 16. Listar un `.tar.xz`

```bash
tar -tJf practica.tar.xz
```

Comprueba que los miembros sean los mismos que esperabas.

## 17. `--auto-compress` como alternativa

GNU tar también dispone de `-a/--auto-compress` para elegir compresión a partir del sufijo al crear ciertos archivos.

Ejemplo:

```bash
tar -caf practica-auto.tar.xz origen
```

Para aprender, seguiremos mostrando `-z` y `-J` porque dejan visible qué compresor interviene.

## 18. Comparar tamaños

```bash
ls -lh practica.tar practica.tar.gz practica.tar.xz
```

No esperes siempre grandes diferencias.

Archivos muy pequeños o ya comprimidos pueden reducirse poco o incluso crecer por la sobrecarga del formato.

## 19. `gzip` sobre un archivo individual

Primero crea una copia de práctica:

```bash
cp origen/uno.txt gzip-prueba.txt
```

Para conservar el original:

```bash
gzip -k gzip-prueba.txt
```

Después deberían existir:

```text
gzip-prueba.txt
gzip-prueba.txt.gz
```

## 20. Por qué usamos `gzip -k`

Sin `-k/--keep`, gzip normalmente reemplaza el archivo de entrada por su versión comprimida cuando la operación tiene éxito.

En las primeras prácticas conservamos el original para poder comparar y evitar pérdidas accidentales.

## 21. Probar integridad gzip

```bash
gzip -t gzip-prueba.txt.gz
estado=$?
printf 'Estado gzip -t: %s\n' "$estado"
```

`gzip -t` comprueba la integridad del archivo comprimido.

Un estado `0` indica que la prueba terminó correctamente.

## 22. Consultar información gzip

```bash
gzip -l gzip-prueba.txt.gz
```

Muestra información de tamaño y relación de compresión cuando está disponible.

## 23. Descomprimir gzip conservando el `.gz`

```bash
mkdir -p restauracion-gzip
cp gzip-prueba.txt.gz restauracion-gzip/
cd restauracion-gzip
gzip -dk gzip-prueba.txt.gz
```

`-d` descomprime.

`-k` conserva el archivo comprimido.

Después vuelve al módulo:

```bash
cd ..
```

## 24. `xz` sobre un archivo individual

```bash
cp origen/uno.txt xz-prueba.txt
xz -k xz-prueba.txt
```

Deberían quedar:

```text
xz-prueba.txt
xz-prueba.txt.xz
```

## 25. Por qué usamos `xz -k`

Por defecto, xz elimina el archivo de entrada después de una compresión exitosa en los casos normales.

`-k/--keep` conserva el original.

## 26. Probar integridad xz

```bash
xz -t xz-prueba.txt.xz
estado=$?
printf 'Estado xz -t: %s\n' "$estado"
```

## 27. Consultar información xz

```bash
xz -l xz-prueba.txt.xz
```

`-l/--list` muestra información del archivo `.xz` sin descomprimirlo a un archivo normal.

## 28. Descomprimir xz conservando el `.xz`

```bash
mkdir -p restauracion-xz
cp xz-prueba.txt.xz restauracion-xz/
cd restauracion-xz
xz -dk xz-prueba.txt.xz
cd ..
```

## 29. Niveles de compresión

`gzip` y `xz` permiten seleccionar niveles/presets de compresión.

De forma general:

```text
nivel menor → suele usar menos tiempo/recursos
nivel mayor → puede buscar mejor relación de compresión
```

Pero un nivel mayor no garantiza una mejora proporcional.

En xz, presets altos también pueden requerir bastante más memoria.

Para aprendizaje inicial usa los valores predeterminados.

## 30. Extraer no es una operación de solo lectura

Crear o listar un archivo es distinto de extraerlo.

Al extraer:

- se crean archivos y directorios;
- pueden existir conflictos con nombres ya presentes;
- se restauran metadatos según las reglas y opciones;
- un archivo no confiable puede contener una estructura inesperada.

Por eso la extracción requiere más precauciones.

## 31. Regla para archivos externos o no confiables

Antes de extraer:

1. identifica el archivo y su procedencia;
2. lista su contenido;
3. revisa rutas y tipos de miembros;
4. recuerda que **listar no certifica que el archivo sea seguro**;
5. crea un directorio nuevo y vacío;
6. asegúrate de que ese directorio y su directorio padre no puedan ser modificados por usuarios no confiables;
7. extrae un archivo no confiable **por separado**, sin mezclarlo con otros archivos no confiables;
8. revisa diagnósticos y estado de salida de `tar`;
9. inspecciona el resultado, incluidos enlaces y permisos, antes de mover o ejecutar nada.

GNU tar recomienda extraer archivos no confiables en un directorio vacío y controlado cuyo directorio y padre sean accesibles únicamente por usuarios de confianza.

### Listar ayuda, pero no prueba seguridad

```bash
tar -tvf archivo.tar
```

permite observar nombres y tipos de miembros, pero no demuestra por sí solo que la extracción sea segura.

Un archivo puede contener, entre otras cosas:

- enlaces simbólicos;
- permisos inesperados;
- rutas diseñadas para causar conflictos;
- archivos ejecutables;
- estructuras que solo muestran su efecto real al extraerse.

Por eso:

```text
listar → inspeccionar
extraer aislado → observar resultado real
ejecutar contenido → decisión separada
```

### Un directorio distinto por cada archivo no confiable

GNU tar advierte que dos archivos no confiables no deben extraerse secuencialmente en el mismo árbol de trabajo. Un archivo extraído primero podría dejar enlaces u otra estructura que cambie el efecto de la extracción posterior.

Regla del manual:

> **un archivo no confiable → un directorio vacío y aislado propio**

En nuestras prácticas normales usamos archivos creados por nosotros mismos. No necesitamos descargar contenido externo para aprender esta regla.

## 32. Crear destino vacío

Para nuestra práctica **con un archivo creado por nosotros**:

```bash
mkdir -p extraccion-segura
```

Comprueba:

```bash
ls -la extraccion-segura
```

Debe estar vacío salvo `.` y `..`.

Si el archivo fuera realmente no confiable, además del directorio vacío tendrías que confirmar que usuarios no confiables no puedan modificar ese directorio ni su padre mientras ocurre la extracción. Esa verificación de permisos se estudia aquí como concepto; no necesitamos practicarla con contenido externo.

## 33. Extraer con `-C`

```bash
tar -xzf practica.tar.gz -C extraccion-segura
```

`-C` cambia el directorio de extracción para esa operación.

Después:

```bash
find extraccion-segura -maxdepth 4 -print
```

## 34. Extraer `.tar.xz`

En otra carpeta vacía:

```bash
mkdir -p extraccion-xz
tar -xJf practica.tar.xz -C extraccion-xz
```

## 35. Evitar reemplazar archivos existentes

GNU tar ofrece:

```bash
--keep-old-files
```

o su forma corta:

```text
-k
```

durante extracción.

Si un miembro intentaría reemplazar un archivo existente, tar se niega y lo trata como error.

Ejemplo:

```bash
tar -xzf practica.tar.gz --keep-old-files -C extraccion-segura
```

## 36. `--skip-old-files`

También existe:

```bash
--skip-old-files
```

que omite archivos ya existentes sin tratarlos como error.

Para aprendizaje inicial preferimos `--keep-old-files` porque hace visible el conflicto.

## 37. `--one-top-level`

GNU tar dispone de:

```bash
--one-top-level
```

para crear una carpeta superior durante extracción y reducir el riesgo de un archivo tipo “tarbomb” que disperse muchos miembros en el directorio actual.

Ejemplo conceptual:

```bash
tar -xzf archivo.tar.gz --one-top-level
```

Seguimos prefiriendo además una carpeta de destino dedicada y vacía.

## 38. No usar `--absolute-names` (`-P`) por rutina

GNU tar normalmente aplica protecciones respecto a nombres absolutos.

`--absolute-names` (`-P`) cambia ese comportamiento y puede permitir que miembros del archivo se refieran a rutas fuera del directorio previsto.

Este manual **no lo usa** en prácticas.

## 39. Opciones de alto riesgo que no usamos como rutina

Evita copiar sin comprender opciones como:

```text
--absolute-names
--overwrite
--recursive-unlink
--remove-files
--dereference
```

Pueden cambiar significativamente qué archivos se leen, eliminan o sobrescriben.

## 40. Archivos y enlaces simbólicos

Un archivo tar puede contener enlaces simbólicos.

Por eso:

```bash
tar -tvf archivo.tar
```

no sirve solo para ver nombres; también ayuda a reconocer tipos de miembros.

Con archivos externos, inspecciona enlaces antes de confiar en el resultado extraído.

**Importante:** revisar la lista no elimina todos los riesgos asociados a enlaces. GNU tar advierte que, durante extracción en un árbol que otros usuarios puedan modificar, un directorio podría cambiar por un enlace simbólico y alterar el destino efectivo de escritura.

La defensa principal no es “mirar mejor la lista”, sino combinar:

```text
directorio vacío
+ padre controlado por usuarios de confianza
+ una extracción aislada por archivo no confiable
+ revisión posterior
```

No extraigas material no confiable como administrador si no existe una necesidad concreta y un entorno preparado para ello.

## 41. Seleccionar un miembro concreto

Después de listar el nombre exacto, puedes extraer un miembro específico.

Ejemplo dentro de una carpeta vacía:

```bash
mkdir -p extraccion-selectiva
tar -xzf practica.tar.gz -C extraccion-selectiva origen/uno.txt
```

Esto evita extraer miembros que no necesitas.

## 42. Extraer no significa «abrir»

Un archivo comprimido o archivado puede contener código, documentos, imágenes o cualquier otro dato.

Extraerlo solo restaura los miembros.

No ejecutes automáticamente archivos obtenidos de un archivo comprimido.

## 43. Práctica A — crear y listar `.tar`

```bash
tar -cf practica-a.tar origen
tar -tf practica-a.tar
```

Explica qué hace cada opción.

## 44. Práctica B — gzip con original conservado

```bash
cp origen/uno.txt ejercicio-gzip.txt
gzip -k ejercicio-gzip.txt
gzip -t ejercicio-gzip.txt.gz
ls -lh ejercicio-gzip.txt ejercicio-gzip.txt.gz
```

## 45. Práctica C — xz con original conservado

```bash
cp origen/uno.txt ejercicio-xz.txt
xz -k ejercicio-xz.txt
xz -t ejercicio-xz.txt.xz
ls -lh ejercicio-xz.txt ejercicio-xz.txt.xz
```

## 46. Práctica D — crear `.tar.gz` y `.tar.xz`

```bash
tar -czf copia.tar.gz origen
tar -cJf copia.tar.xz origen
```

Después:

```bash
tar -tzf copia.tar.gz
tar -tJf copia.tar.xz
```

## 47. Práctica E — extraer en destino vacío

```bash
mkdir -p restaurar-practica
tar -xzf copia.tar.gz --keep-old-files -C restaurar-practica
find restaurar-practica -maxdepth 4 -print
```

No extraigas encima de `origen`.

## 48. Práctica F — comprobar conflicto

Dentro de una carpeta de laboratorio separada, primero extrae una vez.

Después intenta repetir:

```bash
tar -xzf copia.tar.gz --keep-old-files -C restaurar-practica
```

Ahora tar debe advertir de miembros existentes en vez de reemplazarlos silenciosamente.

Esto es un fallo **controlado** de aprendizaje.

## 49. Errores frecuentes

| Error | Problema | Corrección |
|---|---|---|
| creer que tar comprime por sí solo en todos los casos | archivar y comprimir son conceptos distintos | identifica tar + compresor |
| extraer antes de listar | no sabes qué se intentará escribir | usa `tar -t...` primero |
| creer que listar certifica seguridad | la lista no revela todas las consecuencias posibles | inspecciona, pero extrae aislado y revisa después |
| extraer en tu directorio personal | puede mezclar/sobrescribir archivos | usa carpeta vacía y controlada |
| reutilizar la misma carpeta para varios archivos no confiables | una extracción anterior puede afectar la siguiente | usa un directorio aislado distinto por archivo |
| usar gzip/xz sin saber que modifican entrada | puedes perder el original | usa `-k` durante aprendizaje |
| asumir extensión = formato real | nombres pueden engañar | inspecciona y prueba |
| usar `-P` por copiar un ejemplo | desactiva protecciones de nombres | no usar sin motivo y archivo confiable |
| usar `--overwrite` por defecto | permite reemplazos | usa destino vacío / `--keep-old-files` |
| comprimir un directorio directamente con gzip | gzip no crea archivo jerárquico | tar primero, luego gzip |
| creer que nivel 9 siempre es mejor | puede gastar tiempo/memoria por poco beneficio | usa predeterminado salvo necesidad |
| ejecutar contenido recién extraído | aumenta riesgo | inspecciona antes |

## 50. Detección de error 1

Analiza:

```bash
tar -xzf descarga.tar.gz
```

si `descarga.tar.gz` es externa y estás en tu carpeta personal.

Problemas:

- no se inspeccionó;
- destino no está aislado;
- podrían existir conflictos.

Flujo recomendado:

```text
tar -tzf descarga.tar.gz
recordar que listar no certifica seguridad
crear carpeta nueva/vacía y controlada
usar una carpeta distinta para cada archivo no confiable
extraer sin opciones de alto riesgo
revisar diagnósticos y estado de salida
inspeccionar enlaces, permisos y contenido
no ejecutar automáticamente nada extraído
```

## 51. Detección de error 2

Analiza:

```bash
gzip documento.txt
```

Si necesitabas conservar `documento.txt`, el comando no expresa esa intención.

Para práctica:

```bash
gzip -k documento.txt
```

## 52. Detección de error 3

Analiza:

```bash
tar -xPf archivo.tar
```

`-P` permite nombres absolutos y cambia protecciones importantes.

Corrección inicial:

```bash
tar -tf archivo.tar
```

y, si decides extraer, hacerlo en un destino controlado sin `-P`.

## 53. Método seguro para trabajar con archivos comprimidos

1. identifica el archivo y su procedencia;
2. conserva el original cuando estés aprendiendo;
3. lista el contenido de archivos tar;
4. recuerda que listar no certifica seguridad;
5. verifica integridad cuando la herramienta lo permita;
6. crea un destino nuevo, vacío y controlado;
7. usa un destino distinto por cada archivo no confiable;
8. evita sobrescrituras;
9. no uses opciones peligrosas por copiar recetas;
10. revisa diagnósticos y estado de salida;
11. inspecciona enlaces, permisos y contenido extraído;
12. no ejecutes contenido automáticamente.

## 54. Práctica independiente

Crea un script `empaquetar_practica.sh` que:

1. use Bash;
2. reciba como argumento un directorio existente dentro del laboratorio;
3. valide que sea directorio;
4. cree un `.tar.gz` en la carpeta del módulo;
5. no borre ni modifique el directorio original;
6. liste el archivo creado con `tar -tzf`;
7. devuelva estado no-cero si falla la creación o el listado;
8. use quoting correcto;
9. pase `bash -n`;
10. pase ShellCheck si está disponible;
11. pueda explicarse línea por línea.

## 55. Mini evaluación

1. ¿archivar y comprimir son exactamente lo mismo? A) Sí B) No
2. ¿`tar -c` crea un archivo? A) Sí B) No
3. ¿`tar -t` lista miembros? A) Sí B) No
4. ¿`tar -x` extrae? A) Sí B) No
5. ¿debes listar un archivo externo antes de extraerlo? A) Sí B) No
6. ¿`gzip` agrupa por sí solo un árbol completo como tar? A) Sí B) No
7. ¿`gzip -k` conserva el original? A) Sí B) No
8. ¿`xz -k` conserva el original? A) Sí B) No
9. ¿`gzip -t` comprueba integridad? A) Sí B) No
10. ¿`xz -t` comprueba integridad? A) Sí B) No
11. ¿es mejor extraer un archivo no confiable en una carpeta vacía? A) Sí B) No
12. ¿listar con `tar -t...` demuestra por sí solo que el archivo sea seguro? A) Sí B) No
13. ¿conviene extraer dos archivos no confiables distintos en el mismo directorio? A) Sí B) No
14. ¿el directorio de extracción y su padre deben estar protegidos frente a modificaciones de usuarios no confiables? A) Sí B) No
15. ¿`--keep-old-files` evita reemplazar archivos existentes? A) Sí B) No
16. ¿`--one-top-level` ayuda frente a tarbombs? A) Sí B) No
17. ¿`-P/--absolute-names` debe usarse por defecto? A) Sí B) No
18. ¿una extensión garantiza completamente el formato real? A) Sí B) No

## 56. Registro de aprendizaje

```text
Archivar significa:
Comprimir significa:
`tar -c` sirve para:
`tar -t` sirve para:
`tar -x` sirve para:
`-f` sirve para:
`-z` relaciona tar con:
`-J` relaciona tar con:
`gzip -k` sirve para:
`xz -k` sirve para:
`gzip -t` sirve para:
`xz -t` sirve para:
¿por qué extraigo en carpeta vacía?:
¿por qué listar no certifica seguridad?:
¿por qué uso una carpeta distinta por archivo no confiable?:
¿por qué también importa proteger el directorio padre?:
`--keep-old-files` hace:
`--one-top-level` ayuda a:
¿por qué evitamos `-P`?:
Algo que todavía confundo:
Estado: EN APRENDIZAJE / PRACTICADO
```

## 57. Puerta de dominio

Para considerar este módulo **DOMINADO** deberás poder en más de una ocasión:

1. explicar sin copiar la diferencia entre archivar y comprimir;
2. crear y listar un `.tar`;
3. crear un `.tar.gz` y un `.tar.xz`;
4. conservar originales al practicar con gzip y xz;
5. verificar un `.gz` y un `.xz`;
6. explicar por qué inspeccionar no equivale a certificar seguridad;
7. extraer a una carpeta vacía y controlada sin sobrescribir originales;
8. explicar por qué archivos no confiables distintos deben aislarse en destinos separados;
9. identificar por qué `-P` o `--overwrite` requieren especial precaución.

## 58. Fuentes y límites

Fuentes principales:

- GNU tar Manual: https://www.gnu.org/software/tar/manual/tar.html
- GNU tar — opciones de extracción y archivos existentes: https://www.gnu.org/software/tar/manual/html_section/extract-options.html
- GNU tar — Reliability and Security: https://www.gnu.org/software/tar/manual/html_chapter/Reliability-and-security.html
- GNU Gzip Manual: https://www.gnu.org/software/gzip/manual/gzip.html
- XZ Utils — `xz(1)`: https://tukaani.org/xz/man/xz.1.html

Puntos verificados documentalmente:

- GNU tar separa operaciones de creación (`--create`), listado (`--list`) y extracción (`--extract`);
- `--keep-old-files` impide reemplazar archivos existentes y trata el conflicto como error;
- `--one-top-level` crea un directorio superior durante extracción y puede proteger frente a tarbombs;
- GNU tar recomienda extraer archivos no confiables en un directorio vacío; ese directorio y su padre deben ser accesibles solo para usuarios de confianza;
- GNU tar recomienda extraer archivos no confiables distintos de forma independiente, en directorios vacíos diferentes;
- listar miembros ayuda a inspeccionar, pero no certifica que la extracción sea segura;
- GNU tar recomienda prestar atención a diagnósticos y estado de salida;
- GNU tar desaconseja opciones de riesgo como `--absolute-names`, `--dereference`, `--overwrite`, `--recursive-unlink` y `--remove-files` salvo comprensión explícita;
- GNU gzip 1.14 documenta compresión y descompresión de archivos y dispone de `--keep` y `--test`;
- XZ Utils documenta `-k/--keep`, `-d/--decompress`, `-l/--list` y `-t/--test`;
- xz utiliza por defecto el formato `.xz` y recomienda `xz -d`/`xz -dc` en scripts en lugar de depender de alias como `unxz` o `xzcat`.

Se posponen:

- archivos incrementales de tar;
- ACL, xattrs y SELinux dentro de tar;
- formatos pax, ustar y GNU en profundidad;
- `--transform` y `--strip-components`;
- cifrado (tar/gzip/xz no proporcionan cifrado por sí solos);
- zstd, bzip2 y zip;
- recuperación forense de archivos dañados;
- procesamiento masivo paralelo.

**Estado de la lección:** redactada y revisada documentalmente contra GNU tar, GNU Gzip y XZ Utils. Las prácticas conservan originales y extraen únicamente en destinos controlados.

---

**Siguiente:** [Módulo 32 — Copias, sincronización y restauración con `rsync`](modulo-32-rsync-copias-restauracion.md) · [Volver al índice](README.md)
