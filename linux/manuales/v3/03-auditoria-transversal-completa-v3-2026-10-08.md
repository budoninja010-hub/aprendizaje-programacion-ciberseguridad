# Auditoría transversal completa — Manual Maestro de Linux y Shell Scripting — Edición 2026 v3

**Fecha de auditoría:** 8 de octubre de 2026  
**Repositorio auditado:** `budoninja010-hub/aprendizaje-programacion-ciberseguridad`  
**Ruta:** `linux/manuales/v3/`  
**Alcance:** arquitectura, README, auditoría histórica y los 35 módulos del núcleo.

## 1. Dictamen independiente

**Resultado: APTO CON CORRECCIONES IMPORTANTES.**

No se identificaron errores críticos que, por sí solos, obliguen a detener el estudio completo del manual. La estructura general, el contrato de seguridad, la progresión y la mayoría de las explicaciones técnicas son sólidas.

Sin embargo, antes de denominar esta v3 **edición consolidada final**, deben corregirse varios puntos técnicos y editoriales. Los hallazgos más importantes afectan:

1. precisión de la explicación de direcciones privadas RFC1918;
2. interpretación del estado de salida de `dnf check-update`;
3. semántica de recuperación de ejecuciones perdidas con `systemd.timer` y `Persistent=true`;
4. endurecimiento de la sección de extracción de archivos `tar` no confiables;
5. procedimiento posterior a la exposición accidental de secretos en Git/GitHub;
6. una precisión de globbing respecto de enlaces simbólicos rotos;
7. trazabilidad hacia fuentes originales/upstream en varios módulos;
8. uniformidad editorial de M1–M4 frente al formato usado desde M5.

## 2. Qué se auditó

Se revisaron directamente:

- `00-indice-arquitectura.md`;
- `01-gnu-linux-kernel-distribuciones.md`;
- `02-auditoria-fuentes.md`;
- `README.md`;
- Módulos 2–35;
- continuidad entre módulos;
- ejemplos de órdenes y scripts;
- bloques de código Markdown;
- advertencias de seguridad;
- ejercicios y evaluaciones;
- secciones de fuentes;
- afirmaciones dependientes de versión o distribución;
- comandos potencialmente destructivos o administrativos;
- políticas de Git/GitHub y secretos.

## 3. Qué NO significa esta auditoría

Esta es una auditoría **documental, técnica, pedagógica y de seguridad**.

No significa que:

- los 35 módulos hayan sido ejecutados en el Linux real del estudiante;
- todos los comandos hayan sido probados en cada distribución compatible;
- el estudiante ya domine los temas;
- el manual sustituya documentación de la distribución instalada;
- se hayan realizado cambios administrativos sobre discos, firewall, servicios o `/etc/fstab`.

La validación práctica sigue siendo una fase separada.

## 4. Fuentes originales y primarias utilizadas

Se priorizaron fuentes del proyecto o proveedor original:

- GNU Bash Reference Manual: https://www.gnu.org/software/bash/manual/
- GNU Coreutils 9.11: https://www.gnu.org/software/coreutils/manual/coreutils.html
- GNU tar: https://www.gnu.org/software/tar/manual/tar.html
- GNU gzip: https://www.gnu.org/software/gzip/manual/gzip.html
- GNU Findutils: https://www.gnu.org/software/findutils/manual/html_mono/find.html
- Linux kernel documentation: https://docs.kernel.org/
- Linux man-pages project: https://www.kernel.org/doc/man-pages/
- Filesystem Hierarchy Standard 3.0: https://refspecs.linuxfoundation.org/FHS_3.0/
- Debian: https://www.debian.org/
- Ubuntu documentation: https://documentation.ubuntu.com/ y https://ubuntu.com/server/docs/
- Fedora documentation: https://docs.fedoraproject.org/
- Red Hat Enterprise Linux 10: https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10
- systemd upstream: https://github.com/systemd/systemd/
- util-linux upstream: https://github.com/util-linux/util-linux/
- Cronie upstream: https://github.com/cronie-crond/cronie/
- iproute2 upstream: https://git.kernel.org/pub/scm/network/iproute2/iproute2.git/
- Netfilter/nftables: https://www.netfilter.org/ y https://wiki.nftables.org/
- OpenSSH upstream manual pages: https://man.openbsd.org/
- RFC Editor / IETF: https://www.rfc-editor.org/ y https://datatracker.ietf.org/
- rsync: https://rsync.samba.org/
- Git: https://git-scm.com/docs/
- GitHub Docs: https://docs.github.com/
- XZ Utils: https://tukaani.org/xz/
- ShellCheck: https://www.shellcheck.net/

Los enlaces a `man7.org` encontrados en el manual se consideran útiles como representación de páginas de manual, pero cuando existe un repositorio/manual upstream claramente identificable se recomienda enlazar primero la fuente original y dejar `man7.org` como referencia complementaria.

## 5. Resultado estructural

### 5.1 Núcleo completo

Se verificó la presencia de los **35 módulos**.

### 5.2 Continuidad

Los módulos M2–M34 apuntan al siguiente módulo esperado y M35 contiene el cierre del núcleo.

### 5.3 Bloques de código

En el pase mecánico realizado sobre los 35 archivos no se detectaron bloques Markdown con triple acento grave abiertos sin cierre.

### 5.4 Seguridad pedagógica

El contrato de seguridad se mantiene de manera consistente:

- usuario normal como punto de partida;
- `~/linux-lab` como laboratorio, sin presentarlo como una sandbox real;
- no añadir `sudo` automáticamente;
- no practicar `rm -rf`;
- no modificar firewall durante el módulo introductorio;
- no practicar montaje real ni edición de `/etc/fstab`;
- `--delete` de rsync solo en simulación;
- secretos excluidos de Git/GitHub;
- ciberseguridad limitada a sistemas propios o autorizados.

Este es uno de los puntos más fuertes de la v3.

## 6. Hallazgos de prioridad ALTA

### A01 — M19: formulación imprecisa sobre direcciones RFC1918

**Texto actual aproximado:** las direcciones privadas «no son directamente enrutables como direcciones públicas en Internet».

**Problema:** puede interpretarse como si una dirección RFC1918 fuera intrínsecamente no enrutable. Sí puede ser enrutada dentro de redes privadas y entre redes coordinadas mediante túneles/encapsulación. Lo que RFC1918 establece es que esas direcciones no tienen significado global y su información de ruteo no debe propagarse por enlaces inter-empresa del Internet público.

**Corrección recomendada:**

> Las direcciones RFC1918 son privadas y no son globalmente únicas. Pueden enrutarse dentro de redes privadas, pero sus rutas no deben propagarse por el Internet público. Para acceso externo se emplean mecanismos como gateways/NAT según el diseño de la red.

**Fuente primaria:** RFC 1918 — RFC Editor/IETF.

**Estado:** pendiente de corregir en M19.

### A02 — M15 y M35: documentar explícitamente el estado `100` de `dnf check-update`

M15 ya advierte que `dnf check-update` puede devolver un estado especial, pero no fija su significado. M35 vuelve a usarlo después de que el estudiante ya aprendió códigos de salida.

**Problema:** un estudiante puede interpretar cualquier estado no cero como «error» y tratar `100` como fallo genérico.

**Corrección recomendada:** añadir una caja:

```text
dnf check-update
0   → no hay actualizaciones disponibles
100 → hay actualizaciones disponibles
1   → ocurrió un error
```

Aclarar que los códigos son específicos de la herramienta y que este es un excelente ejemplo de por qué un valor no cero no debe interpretarse sin consultar la documentación del comando.

**Fuente primaria:** documentación de DNF, comando `check-update`; RHEL 10 confirma el uso de `dnf check-update`.

**Estado:** pendiente de corregir en M15 y referenciar desde M35/M25.

### A03 — M30: precisar `Persistent=true`

El texto actual explica correctamente que `Persistent=true` puede recuperar una activación perdida de un timer `OnCalendar=`.

**Falta importante:** si el timer habría vencido varias veces mientras estuvo inactivo, `Persistent=true` no reproduce necesariamente una ejecución por cada periodo perdido. El manual upstream indica que se dispara inmediatamente si habría vencido al menos una vez.

**Corrección recomendada:**

> `Persistent=true` sirve para detectar que se perdió al menos una activación de un timer `OnCalendar=` mientras estaba inactivo y disparar la unidad al activarse. No debe interpretarse como una cola que reproduce una por una todas las ejecuciones perdidas.

También diferenciar apagado/inactividad de la compensación de timers de calendario durante suspensión.

**Fuente primaria:** `systemd.timer(5)` del repositorio upstream de systemd.

**Estado:** pendiente de matiz en M30.

### A04 — M31: reforzar extracción de archivos `tar` no confiables

M31 ya hace algo correcto y valioso: listar primero y extraer en una carpeta vacía.

**Problema de completitud:** listar los miembros no demuestra por sí solo que el archivo sea seguro. GNU tar advierte también sobre enlaces simbólicos, permisos y carreras en árboles accesibles por usuarios no confiables.

**Corrección recomendada:**

- indicar que `tar -t...` es inspección, no certificación de seguridad;
- para material no confiable, usar una carpeta vacía cuyo directorio y padre no sean modificables por usuarios no confiables;
- mantener la prohibición rutinaria de `-P/--absolute-names`, `--overwrite`, `--recursive-unlink`, `--remove-files` y `--dereference`;
- no ejecutar automáticamente contenido extraído.

**Fuente primaria:** GNU tar, capítulo *Reliability and Security*.

**Estado:** pendiente de endurecimiento textual en M31.

### A05 — M33: falta el procedimiento inmediato si un secreto YA fue expuesto

M33 correctamente enseña que `.gitignore` no afecta automáticamente archivos ya rastreados y que no deben subirse tokens, contraseñas o claves.

**Problema:** falta una instrucción crítica para el caso en que el secreto ya llegó a un commit/repositorio.

**Corrección recomendada:**

> Si una contraseña, token o clave real fue confirmada o publicada, detener el flujo y **revocar/rotar primero la credencial**. Después retirar el secreto del código y, si es necesario, sanear el historial siguiendo el procedimiento de GitHub. Añadirlo a `.gitignore` no invalida una credencial ya expuesta.

**Fuente primaria:** GitHub Docs — *Removing sensitive data from a repository* y documentación de push protection.

**Estado:** pendiente de añadir en M33.

## 7. Hallazgos de prioridad MEDIA

### M01 — M27: patrón de glob y enlaces simbólicos rotos

El patrón:

```bash
for archivo in ./*.txt; do
    [[ -e $archivo ]] || continue
    ...
done
```

es adecuado para evitar procesar el patrón literal cuando no hay coincidencias. Sin embargo, `-e` es falso para un enlace simbólico roto.

**Recomendación:** si el objetivo declarado es recorrer *pathnames* coincidentes incluyendo symlinks rotos, usar una condición como `[[ -e $archivo || -L $archivo ]]` o enseñar `nullglob` en una ampliación. Si el objetivo son solo objetos existentes como archivos utilizables, mantener el ejemplo pero explicitar esa limitación.

### M02 — M30: diferenciar tareas perdidas por apagado de saltos de reloj/DST

La afirmación de que cron tradicional no recupera normalmente una tarea perdida con la máquina apagada es correcta.

**Mejora:** añadir que implementaciones como Cronie tienen tratamiento específico de ciertos cambios de reloj/DST. Eso no equivale a una política general de recuperación de trabajos perdidos por apagado.

### M03 — M16 y M32: afirmaciones de versión deben seguir fechadas

Debian 13, Ubuntu 26.04 LTS y rsync 3.5.1 son correctos para la fecha de esta auditoría.

**Recomendación:** conservar siempre la forma:

```text
A fecha de 8 de octubre de 2026...
```

y no transformar esas frases en afirmaciones atemporales durante maquetación.

### M04 — M13: añadir una definición breve de load average

M13 evita diagnosticar por un único número, lo cual es correcto.

**Mejora pedagógica:** añadir que, en Linux, la carga media incluye tareas ejecutables/running y tareas en estado no interrumpible (habitualmente asociadas a espera de I/O), promediadas en 1, 5 y 15 minutos. Evita que el alumno la confunda con porcentaje de CPU.

### M05 — M25: reforzar que el significado numérico es específico de cada programa

El módulo ya enseña correctamente `0` frente a no-cero, `126`, `127` y `128+N`.

**Mejora:** en cualquier tabla `1–255`, escribir «estado no cero; significado concreto definido por el programa o por convenciones de la shell», no «error» como significado universal.

### M06 — M34: validar fuentes upstream de util-linux

El contenido técnico auditado sobre `findmnt` es correcto: upstream confirma que `--verify` puede combinarse con `--tab-file`.

**Mejora de trazabilidad:** sustituir `man7.org` como fuente principal de `lsblk`, `findmnt`, `mount` y `fstab` por el repositorio/manual upstream de util-linux; dejar man7 como espejo complementario.

### M07 — M19/M35: fuentes upstream de iproute2

`ip` y `ss` están correctamente usados como herramientas de consulta.

**Mejora de trazabilidad:** enlazar primero al proyecto iproute2 upstream (kernel.org) y dejar copias HTML de terceros como apoyo.

### M08 — M30: fuentes originales de Cronie/systemd

Las afirmaciones auditadas sobre cinco campos, entorno de cron, `OnCalendar=`, `Persistent=true`, `AccuracySec=` y `RandomizedDelaySec=` son esencialmente correctas.

**Mejora:** usar como referencias principales el repositorio upstream de Cronie y `systemd.timer(5)`/`systemd.time(7)` del repositorio systemd.

## 8. Hallazgos editoriales y pedagógicos

### E01 — Formato desigual en M1–M4

M5 en adelante usa con mayor regularidad:

- `Qué aprenderás`;
- seguridad;
- prácticas;
- errores frecuentes;
- mini evaluación;
- registro de aprendizaje;
- puerta de dominio;
- fuentes y límites.

M1–M4 contienen esas ideas, pero con encabezados diferentes (`Revisión de esta entrega`, `Evaluación sin copiar`, etc.).

**Recomendación:** normalizar M1–M4 al contrato visual de M5–M35 sin eliminar contenido.

### E02 — El README acumula demasiados estados históricos

El README conserva cada entrega anterior dentro del mismo archivo.

**Problema:** dificulta encontrar el estado actual.

**Recomendación:** dejar en README:

- estado actual;
- índice de módulos;
- auditoría vigente;
- siguiente fase.

Trasladar el historial cronológico a `CHANGELOG.md` o `HISTORIAL.md`, conservando todos los datos.

### E03 — `02-auditoria-fuentes.md` ya es histórica

Su propio texto dice que solo auditaba la primera entrega y que M2–M35 seguían pendientes.

**Recomendación:** no borrarla. Añadir una nota al inicio:

> Auditoría histórica de la primera entrega. Para la auditoría transversal del núcleo completo, consultar `03-auditoria-transversal-completa-v3-2026-10-08.md`.

### E04 — Homogeneizar nomenclatura de fuente primaria

Usar una jerarquía editorial:

```text
1. upstream/proyecto original
2. documentación oficial de distribución/proveedor
3. estándar/RFC
4. mirror de páginas man
5. fuente secundaria, solo si aporta contexto
```

### E05 — Añadir fecha de verificación a afirmaciones cambiantes

Especialmente:

- versiones de distribuciones;
- versión latest de rsync;
- ciclo de soporte;
- defaults de seguridad;
- herramientas predeterminadas.

## 9. Confirmaciones importantes — contenido correcto

Durante la auditoría se confirmaron, entre otros, estos puntos:

- GNU Coreutils 9.11 es una referencia editorial válida para 2026;
- Bash distingue correctamente `test`/`[ ]` de `[[ ]]` y el manual lo enseña;
- el modelo de `umask` como eliminación de bits, no resta decimal, es correcto;
- `set -e` no es un detector universal de fallos; M29 lo explica correctamente;
- `mktemp -u` no debe usarse como patrón de «nombre y luego crear»; M29 lo trata correctamente;
- `pipefail` está explicado correctamente;
- RHEL 10 documenta journal volátil por defecto en `/run/log/journal` salvo configuración de persistencia; M18 lo presenta con cautela adecuada;
- Ubuntu documenta AppArmor cargado por defecto; M16 es correcto;
- Ubuntu documenta UFW como frontend y deshabilitado inicialmente; M21 lo contextualiza sin generalizar a Debian;
- RHEL 10 documenta firewalld/nftables; M21 es correcto;
- Debian 13 `trixie` es la stable vigente en la fecha auditada;
- Ubuntu 26.04 LTS existe y la explicación LTS/interim es esencialmente correcta;
- `A && B || C` no es sustituto universal de `if/else`; M25 es correcto;
- `[[ ... ]]` evita word splitting y pathname expansion de sus palabras; M26 es correcto;
- `IFS= read -r` es el patrón adecuado enseñado en M27;
- Bash usa ámbito dinámico para variables locales de funciones; M28 es correcto;
- GNU tar recomienda extraer material no confiable en un directorio vacío; M31 va en la dirección correcta;
- rsync 3.5.1 es la versión upstream publicada vigente en la fecha de auditoría y `--delete` merece `--dry-run`; M32 es correcto;
- `.gitignore` no deja de rastrear automáticamente archivos ya tracked; M33 es correcto;
- util-linux confirma `findmnt --verify --tab-file`; la práctica de M34 es válida;
- `/etc/fstab` tiene seis campos principales y RHEL 10 recomienda identificadores persistentes como UUID para montajes persistentes;
- RHEL 10 documenta `dnf check-update`, `dnf upgrade --security`, AIDE `--init` y `--check`; M35 usa correctamente el modelo de integridad;
- AIDE no sustituye backups ni atribuye por sí solo la causa de un cambio; M35 lo explica correctamente.

## 10. Auditoría módulo por módulo

| Módulo | Dictamen | Acción principal |
|---:|---|---|
| 1 | 🟢 Correcto | Normalizar formato/fuentes en consolidación |
| 2 | 🟡 Correcto con mejora editorial | Normalizar `Fuentes y límites` y formato de evaluación |
| 3 | 🟢 Correcto | Sin corrección técnica prioritaria |
| 4 | 🟡 Correcto con mejora editorial | Normalizar formato y fuente primaria de pathname lookup |
| 5 | 🟢 Correcto | Mantener FHS + kernel como referencias |
| 6 | 🟢 Correcto | Mantener política de borrado seguro |
| 7 | 🟢 Correcto | Sin corrección técnica prioritaria |
| 8 | 🟢 Correcto | Mantener énfasis en orden de redirecciones |
| 9 | 🟢 Correcto | Sin corrección técnica prioritaria |
| 10 | 🟢 Correcto | Mantener tratamiento seguro de nombres |
| 11 | 🟢 Correcto | Sin corrección técnica prioritaria |
| 12 | 🟢 Correcto | `umask` y ACL bien diferenciados |
| 13 | 🟡 Mejora pedagógica | Definir load average para evitar confusión con CPU% |
| 14 | 🟢 Correcto | Mantener SIGTERM antes de SIGKILL |
| 15 | 🟠 Corrección importante | Documentar `dnf check-update` = 0/100/1 |
| 16 | 🟡 Correcto con mantenimiento temporal | Conservar fecha en versiones actuales |
| 17 | 🟢 Correcto | Sin corrección técnica prioritaria |
| 18 | 🟢 Correcto | Default RHEL 10 de journal volátil confirmado |
| 19 | 🟠 Corrección importante | Reformular RFC1918 y mejorar fuente iproute2 |
| 20 | 🟢 Correcto | Mantener host-key verification y alcance autorizado |
| 21 | 🟡 Correcto con mejora de fuentes | Priorizar Netfilter/nftables upstream |
| 22 | 🟢 Correcto | Sin corrección técnica prioritaria |
| 23 | 🟢 Correcto | Mantener advertencia de PATH con `/usr/bin/env` |
| 24 | 🟢 Correcto | Quoting y `"$@"` correctamente explicados |
| 25 | 🟡 Precisión menor | Reforzar significado command-specific de no-cero |
| 26 | 🟢 Correcto | `[ ]`, `[[ ]]`, patrones y aritmética correctos |
| 27 | 🟡 Mejora de robustez | Aclarar broken symlink/nullglob |
| 28 | 🟢 Correcto | Ámbito dinámico y `return` bien tratados |
| 29 | 🟢 Correcto | `set -e`, `pipefail`, `mktemp` y ShellCheck bien delimitados |
| 30 | 🟠 Corrección importante | Precisar `Persistent=true`; upstream Cronie/systemd |
| 31 | 🟠 Endurecimiento importante | Añadir límites de inspección y aislamiento de extracción |
| 32 | 🟢 Correcto | `rsync --delete` solo dry-run; restauración incluida |
| 33 | 🟠 Corrección importante | Añadir revocación/rotación tras secreto expuesto |
| 34 | 🟡 Correcto con mejora de fuentes | Upstream util-linux como referencia principal |
| 35 | 🟠 Corrección importante transversal | Añadir semántica 0/100/1 de DNF y enlazar M15/M25 |

## 11. Priorización de correcciones

### Prioridad 1 — antes de edición consolidada

1. M19 RFC1918.
2. M15/M35 estado `100` de DNF.
3. M30 `Persistent=true`.
4. M31 seguridad de tar no confiable.
5. M33 secreto ya expuesto.

### Prioridad 2 — robustez y trazabilidad

6. M27 broken symlink/nullglob.
7. sustituir fuentes espejo por upstream en M19/M21/M30/M34/M35 cuando corresponda.
8. añadir definición breve de load average en M13.
9. precisión textual de estados no-cero en M25.

### Prioridad 3 — consolidación editorial

10. normalizar M1–M4.
11. simplificar README y mover historial.
12. marcar `02-auditoria-fuentes.md` como histórica.
13. homogeneizar fechas de verificación y formato de bibliografía.

## 12. Dictamen de seguridad

**Resultado de seguridad pedagógica: APROBADO CON MEJORAS.**

Aspectos especialmente buenos:

- no se utiliza `sudo` como solución automática;
- los comandos destructivos aparecen como conceptos o advertencias, no como prácticas rutinarias;
- el firewall se observa antes de modificar;
- SSH se limita a sistemas propios/autorizados;
- no se practican ataques ni técnicas de ocultación;
- almacenamiento se mantiene en modo lectura/concepto;
- `fstab` se valida sobre una copia;
- rsync `--delete` permanece en dry-run;
- la evidencia y los secretos se tratan con prudencia;
- M35 separa detección, evidencia y recuperación.

## 13. Dictamen pedagógico

**Resultado pedagógico: ALTO.**

La progresión general es coherente:

```text
terminal
→ rutas/archivos
→ lectura/búsqueda
→ identidad/permisos
→ procesos
→ paquetes
→ systemd/logs
→ red/SSH/firewall
→ Vim
→ Bash
→ automatización
→ archivos/backups
→ Git
→ almacenamiento
→ defensa
```

Una fortaleza clara es que Bash no empieza con `if`: primero enseña estados de salida y solo después decisiones. También introduce quoting antes de bucles y funciones.

## 14. Estado final

**Núcleo redactado:** 35/35.  
**Revisión documental transversal:** completada.  
**Errores críticos detectados:** 0.  
**Correcciones importantes antes de consolidar:** 5 grupos principales.  
**Mejoras medias/editoriales:** pendientes.  
**Validación práctica en el Linux del estudiante:** pendiente.

### Conclusión

El manual ya es una base técnicamente fuerte y segura para continuar el proceso editorial, pero **todavía no debe congelarse como “edición final consolidada”**. Deben aplicarse primero las correcciones A01–A05 y después una segunda pasada de comprobación de los archivos modificados.

## 15. Siguiente acción recomendada

Aplicar las correcciones **una por una**, conservando el historial:

```text
commit 1 → correcciones técnicas de prioridad alta
commit 2 → mejoras de fuentes upstream
commit 3 → homogeneización editorial
commit 4 → auditoría post-corrección
```

No sustituir los módulos originales fuera del historial: cada corrección debe quedar registrada mediante commits nuevos.
