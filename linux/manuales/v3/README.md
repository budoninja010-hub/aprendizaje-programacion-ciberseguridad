# Estado actual — Auditoría transversal v3 completada

Los **35 módulos** del núcleo están redactados. La auditoría documental transversal completa del 8 de octubre de 2026 está disponible en [03 — Auditoría transversal completa v3](03-auditoria-transversal-completa-v3-2026-10-08.md).

**Dictamen:** APTO CON CORRECCIONES IMPORTANTES. No se detectaron errores críticos que obliguen a detener el estudio. Ya están corregidos los cinco hallazgos de prioridad alta: RFC1918 (M19), estados `0/100/1` de `dnf check-update` (M15/M35), semántica de `Persistent=true` (M30), extracción `tar` no confiable (M31) y respuesta ante secretos ya expuestos en Git/GitHub (M33).

La auditoría [02 — Registro de auditoría y fuentes](02-auditoria-fuentes.md) se conserva como **registro histórico de la primera entrega**; no representa ya el estado completo del núcleo.

Las prácticas en el Linux del estudiante siguen pendientes de ejecutar y validar. Redacción completa no equivale a dominio demostrado.

**Progreso de correcciones de prioridad alta:** ✅ **5/5 aplicadas.** A01–A05 están corregidas y registradas en commits separados.

**Progreso de mejoras de prioridad media:** M13 (`load average`) ✅ corregido. M25 (precisión de estados no-cero) ✅ corregido. M27 (globbing y symlink roto) ✅ corregido. Pendiente: trazabilidad upstream en M19/M21/M30/M34/M35.

**Siguiente fase:** continuar con mejoras de trazabilidad upstream; luego homogeneización editorial y auditoría post-corrección.

---

## Registro histórico — Núcleo v3 completo y entregas anteriores
# Estado actual — Núcleo v3 completo: 35 de 35 módulos

Los **Módulos 1–35** del Manual Maestro de Linux y Shell Scripting — Edición 2026 v3 están redactados y revisados documentalmente. Las prácticas en el Linux del estudiante siguen pendientes de ejecutar, explicar y validar durante las clases.

**Nueva lección:** [Módulo 35 — Defensa, actualizaciones, mínimo privilegio, auditoría y AIDE](modulo-35-defensa-actualizaciones-minimo-privilegio-aide.md).

Esta entrega cierra el núcleo con mínimo privilegio, consulta segura de actualizaciones, revisión de servicios/logs/listeners locales, evidencia defensiva, línea base con SHA-256, detección y recuperación de cambios, y el modelo de integridad de AIDE. La práctica principal es local, reversible, no requiere `sudo` y no modifica servicios ni configuración del sistema.

La v2 y los Módulos 1–34 se conservan intactos.

**Siguiente fase editorial:** auditoría transversal completa de los Módulos 1–35, corrección de inconsistencias y referencias cruzadas, revisión de seguridad y progresión pedagógica, y preparación de una edición consolidada.

---

## Registro histórico — Trigésima cuarta entrega y anteriores
# Estado actual — Trigésima cuarta entrega de v3

Módulos 1–34 redactados y revisados documentalmente. Módulo 35 pendiente. Las prácticas en el Linux del estudiante siguen pendientes de comprobar.

**Nueva lección:** [Módulo 34 — Almacenamiento: `lsblk`, `df`, `du`, montaje y `fstab`](modulo-34-almacenamiento-lsblk-df-du-montaje-fstab.md).

Esta entrega separa dispositivos de bloque, sistemas de archivos y puntos de montaje; introduce `lsblk`, `lsblk --fs`, `findmnt`, `df`, `du`, lectura de los seis campos de `fstab`, UUID y opciones básicas. La práctica de `fstab` usa una tabla independiente validada con `findmnt --verify --tab-file`; no se monta ningún disco real ni se modifica `/etc/fstab`.

La v2 y los Módulos 1–33 se conservan intactos.

Siguiente paso editorial: **Módulo 35 — Defensa, actualizaciones, mínimo privilegio, auditoría y AIDE**.

---

## Registro histórico — Trigésima tercera entrega y anteriores
# Estado actual — Trigésima tercera entrega de v3

Módulos 1–33 redactados y revisados documentalmente. Módulos 34–35 pendientes. Las prácticas en el Linux del estudiante siguen pendientes de comprobar.

**Nueva lección:** [Módulo 33 — Git y GitHub para scripts; puente al itinerario específico de Git](modulo-33-git-github-para-scripts.md).

Esta entrega formaliza la autonomía del estudiante para conservar scripts: working tree, staging area, `git status`, `git diff`, `git add`, `git diff --staged`, commits pequeños, `.gitignore`, revisión de secretos, `git restore --staged`, remotos, ramas y `git push`. Se mantiene separado del itinerario completo de Git/GitHub para evitar duplicación.

La v2 y los Módulos 1–32 se conservan intactos.

Siguiente paso editorial: **Módulo 34 — Almacenamiento: `lsblk`, `df`, `du`; montaje y `fstab`**.

---

## Registro histórico — Trigésima segunda entrega y anteriores
# Estado actual — Trigésima segunda entrega de v3

Módulos 1–32 redactados y revisados documentalmente. Módulos 33–35 pendientes. Las prácticas en el Linux del estudiante siguen pendientes de comprobar.

**Nueva lección:** [Módulo 32 — Copias, sincronización y restauración con `rsync`](modulo-32-rsync-copias-restauracion.md).

Esta entrega introduce transferencia incremental, diferencia entre copia/sincronización/espejo/backup, semántica de la barra final, `-a`, `--dry-run`, `-i`, `--stats`, exclusiones, checksums, restauración de prueba y riesgos de `--delete`. La opción `--delete` se limita a simulación en el laboratorio y se explican las limitaciones de `-a` respecto a ACL, xattrs y hardlinks.

La v2 y los Módulos 1–31 se conservan intactos.

Siguiente paso editorial: **Módulo 33 — Git y GitHub para scripts; enlace al itinerario específico de Git**.

---

## Registro histórico — Trigésima primera entrega y anteriores
# Estado actual — Trigésima primera entrega de v3

Módulos 1–31 redactados y revisados documentalmente. Módulos 32–35 pendientes. Las prácticas en el Linux del estudiante siguen pendientes de comprobar.

**Nueva lección:** [Módulo 31 — Archivos y compresión con `tar`, `gzip` y `xz`](modulo-31-tar-gzip-xz-archivos-compresion.md).

Esta entrega separa archivar de comprimir, introduce creación/listado/extracción con GNU tar, compresión individual con gzip y xz, verificación con `-t`, conservación de originales con `-k`, extracción en carpetas vacías, `--keep-old-files`, `--one-top-level` y precauciones frente a opciones como `--absolute-names` y `--overwrite`.

La v2 y los Módulos 1–30 se conservan intactos.

Siguiente paso editorial: **Módulo 32 — Copias y restauración con `rsync`**.

---

## Registro histórico — Trigésima entrega y anteriores
# Estado actual — Trigésima entrega de v3

Módulos 1–30 redactados y revisados documentalmente. Módulos 31–35 pendientes. Las prácticas en el Linux del estudiante siguen pendientes de comprobar.

**Nueva lección:** [Módulo 30 — Automatización con `cron` y temporizadores de systemd](modulo-30-cron-temporizadores-systemd.md).

Esta entrega introduce programación segura de tareas con cron y systemd timers. Incluye los cinco campos de crontab, entorno reducido, regla DOM/DOW de Cronie, pruebas manuales previas, separación script/programador, unidades `.timer` y `.service`, `OnCalendar=`, temporizadores monotónicos, `Persistent=true`, `AccuracySec=`, `RandomizedDelaySec=` y prácticas de usuario sin privilegios.

La v2 y los Módulos 1–29 se conservan intactos.

Siguiente paso editorial: **Módulo 31 — Archivos y compresión con `tar`, `gzip` y `xz`**.

---

## Registro histórico — Vigesimonovena entrega y anteriores
# Estado actual — Vigesimonovena entrega de v3

Módulos 1–29 redactados y revisados documentalmente. Módulos 30–35 pendientes. Las prácticas en el Linux del estudiante siguen pendientes de comprobar.

**Nueva lección:** [Módulo 29 — Manejo de errores, `trap`, `mktemp`, límites de `set -e`/`set -u` y ShellCheck](modulo-29-manejo-errores-trap-mktemp-shellcheck.md).

Esta entrega introduce validación explícita de errores, stderr, `trap ... EXIT`, creación segura de temporales con `mktemp`, límites de `set -e`, semántica de `set -u`, `pipefail`, validación con `bash -n` y análisis estático con ShellCheck. Se documenta que `set -euo pipefail` no es una receta universal y que `mktemp -u` no debe usarse como patrón para crear después un archivo.

La v2 y los Módulos 1–28 se conservan intactos.

Siguiente paso editorial: **Módulo 30 — Automatización con `cron` y temporizadores de systemd**.

---

## Registro histórico — Vigesimoctava entrega y anteriores
# Estado actual — Vigesimoctava entrega de v3

Módulos 1–28 redactados y revisados documentalmente. Módulos 29–35 pendientes. Las prácticas en el Linux del estudiante siguen pendientes de comprobar.

**Nueva lección:** [Módulo 28 — Funciones, parámetros y ámbito en Bash](modulo-28-funciones-parametros-ambito.md).

Esta entrega introduce definición y llamada de funciones, parámetros posicionales temporales, `"$@"`, validación de argumentos, `local`, ámbito dinámico, `return`, diferencia entre estados y datos, uso de stdout/stderr, captura con sustitución de comandos y composición de funciones pequeñas. Se advierte sobre efectos laterales de variables globales y sobre el uso de funciones dentro de subshells.

La v2 y los Módulos 1–27 se conservan intactos.

Siguiente paso editorial: **Módulo 29 — Manejo de errores, `trap`, `mktemp`, límites de `set -e`/`set -u` y ShellCheck**.

---

## Registro histórico — Vigesimoséptima entrega y anteriores
# Estado actual — Vigesimoséptima entrega de v3

Módulos 1–27 redactados y revisados documentalmente. Módulos 28–35 pendientes. Las prácticas en el Linux del estudiante siguen pendientes de comprobar.

**Nueva lección:** [Módulo 27 — Bucles, lectura de líneas y nombres de archivo seguros](modulo-27-bucles-lectura-lineas-nombres-seguros.md).

Esta entrega introduce `for`, `while`, `until`, `break`, `continue`, recorrido seguro de `"$@"`, globbing para pathnames, lectura con `while IFS= read -r`, efectos de tuberías y subshells, contadores y tratamiento de nombres con espacios. Se prohíbe como patrón pedagógico `for archivo in $(ls)` y se documentan alternativas seguras.

La v2 y los Módulos 1–26 se conservan intactos.

Siguiente paso editorial: **Módulo 28 — Funciones, parámetros y ámbito en Bash**.

---

## Registro histórico — Vigesimosexta entrega y anteriores
# Estado actual — Vigesimosexta entrega de v3

Módulos 1–26 redactados y revisados documentalmente. Módulos 27–35 pendientes. Las prácticas en el Linux del estudiante siguen pendientes de comprobar.

**Nueva lección:** [Módulo 26 — Decisiones con `if`, `test`, `[ ]`, `[[ ]]`, `case` y aritmética](modulo-26-if-test-condicionales-case-aritmetica.md).

Esta entrega conecta los códigos de salida del Módulo 25 con estructuras explícitas de decisión. Introduce `if`, `then`, `else`, `elif`, `fi`, `test`, `[ ]`, `[[ ]]`, pruebas de cadenas, números y archivos, `case`, patrones, `(( ... ))` y `$(( ... ))`. Se diferencia portabilidad POSIX de sintaxis específica de Bash y se explican errores de quoting, espacios y comparación de tipos.

La v2 y los Módulos 1–25 se conservan intactos.

Siguiente paso editorial: **Módulo 27 — Bucles, lectura de líneas y nombres de archivo seguros**.

---

## Registro histórico — Vigesimoquinta entrega y anteriores
# Estado actual — Vigesimoquinta entrega de v3

Módulos 1–25 redactados y revisados documentalmente. Módulos 26–35 pendientes. Las prácticas en el Linux del estudiante siguen pendientes de comprobar.

**Nueva lección:** [Módulo 25 — Códigos de salida y composición de órdenes en Bash](modulo-25-codigos-salida-composicion-ordenes.md).

Esta entrega explica estados de salida, `$?`, `true`, `false`, `;`, `&&`, `||`, `exit`, los usos especiales de `126` y `127`, la relación con señales y el estado de tuberías. Se documenta expresamente por qué `A && B || C` no debe memorizarse como sustituto general de `if/else` y se pospone `pipefail` como política hasta el módulo de manejo de errores.

La v2 y los Módulos 1–24 se conservan intactos.

Siguiente paso editorial: **Módulo 26 — Decisiones con `if`, `test`, `[ ]`, `[[ ]]`, `case` y aritmética**.

---

## Registro histórico — Vigesimocuarta entrega y anteriores
# Estado actual — Vigesimocuarta entrega de v3

Módulos 1–24 redactados y revisados documentalmente. Módulos 25–35 pendientes. Las prácticas en el Linux del estudiante siguen pendientes de comprobar.

**Nueva lección:** [Módulo 24 — Variables, entrada, argumentos, expansiones y quoting en Bash](modulo-24-variables-entrada-argumentos-quoting.md).

Esta entrega introduce variables, asignación, expansión, comillas simples/dobles, `read -r`, parámetros posicionales, `$#`, `"$@"`, `"$*"`, `$?`, sustitución de comandos y valores predeterminados. Se aclara que una expansión sin comillas provoca principalmente word splitting y globbing, no una reinterpretación automática como nueva sintaxis shell.

La v2 y los Módulos 1–23 se conservan intactos.

Siguiente paso editorial: **Módulo 25 — Códigos de salida y composición con && y ||**.

---

## Registro histórico — Vigesimotercera entrega y anteriores

# Estado actual — Vigesimotercera entrega de v3

Módulos 1–23 redactados y revisados documentalmente. Módulos 24–35 pendientes. Las prácticas en el Linux del estudiante siguen pendientes de comprobar.

**Nueva lección:** [Módulo 23 — Primer script Bash y shebang](modulo-23-primer-script-bash-shebang.md).

Esta entrega introduce scripts Bash mínimos, shebang, diferencias entre `bash script.sh` y `./script.sh`, permiso de ejecución, `chmod u+x`, validación con `bash -n`, comentarios y errores básicos. Las prácticas se limitan a `~/linux-lab` y no usan privilegios.

La v2 y los Módulos 1–22 se conservan intactos.

Siguiente paso editorial: **Módulo 24 — Variables, entrada, argumentos, expansiones y quoting en Bash**.

---

## Registro histórico — Vigesimosegunda entrega y anteriores

# Estado actual — Vigesimosegunda entrega de v3

Módulos 1–22 redactados y revisados documentalmente. Módulos 23–35 pendientes. Las prácticas en el Linux del estudiante siguen pendientes de comprobar.

**Nueva lección:** [Módulo 22 — vi/Vim: edición segura de archivos de texto](modulo-22-vi-vim-edicion-segura.md).

Esta entrega introduce el modelo modal de vi/Vim, movimiento, inserción, guardado, salida, deshacer/rehacer, búsqueda, copia/pegado y borrado controlado. Las prácticas se limitan a archivos propios de `~/linux-lab`; `:q!`, `:w!`, `dd` y edición con privilegios se explican con advertencias explícitas antes de usarse.

La v2 y los Módulos 1–21 se conservan intactos.

Siguiente paso editorial: **Módulo 23 — Primer script Bash y shebang**.

---

## Registro histórico — Vigesimoprimera entrega y anteriores

# Estado actual — Vigesimoprimera entrega de v3

Módulos 1–21 redactados y revisados documentalmente. Módulos 22–35 pendientes. Las prácticas en el Linux del estudiante siguen pendientes de comprobar.

**Nueva lección:** [Módulo 21 — Firewall: nftables, UFW y firewalld según el entorno](modulo-21-firewall-nftables-ufw-firewalld.md).

Esta entrega introduce Netfilter, nftables, UFW y firewalld; separa servicio escuchando de exposición real; explica entrada/salida/reenvío, stateful filtering, zonas y runtime/permanent; y limita la práctica a identificación y consulta. Se documenta explícitamente el riesgo de cambiar firewalls en sistemas remotos y se prohíbe usar `nft flush ruleset` como práctica.

La v2 y los Módulos 1–20 se conservan intactos, incluida la revisión pedagógica del Módulo 20.

Siguiente paso editorial: **Módulo 22 — vi/Vim: edición segura de archivos de texto**.

---

## Registro histórico — Vigesimoprimera entrega y anteriores

# Revisión pedagógica — Módulo 20

El Módulo 20 fue revisado para dejar explícito que el itinerario sí incluirá aprendizaje de técnicas ofensivas relacionadas con autenticación SSH, pero únicamente en laboratorios propios, CTF o sistemas expresamente autorizados. La revisión incorpora el enfoque mecanismo de fallo → evidencia → detección → mitigación y evita convertir el material en una receta contra sistemas reales sin permiso.

El estado general permanece en Módulos 1–20 redactados. El siguiente módulo sigue siendo el **Módulo 21 — Firewall: nftables, UFW y firewalld según el entorno**.

---

# Estado actual — Vigésima entrega de v3

Módulos 1–20 redactados y revisados documentalmente. Módulos 21–35 pendientes. Las prácticas en el Linux del estudiante siguen pendientes de comprobar.

**Nueva lección:** [Módulo 20 — SSH en sistemas propios o expresamente autorizados](modulo-20-ssh-sistemas-autorizados.md).

Esta entrega introduce cliente/servidor SSH, host keys, fingerprints, known_hosts, configuración efectiva con `ssh -G`, autenticación y claves pública/privada. Las prácticas son locales o sobre infraestructura propia/autorizada; no se desactivan verificaciones de host ni se incluyen intentos de acceso no autorizados.

La v2 y los Módulos 1–19 se conservan intactos.

Siguiente paso editorial: **Módulo 21 — Firewall: nftables, UFW y firewalld según el entorno**.

---

## Registro histórico — Decimonovena entrega y anteriores

# Estado actual — Decimonovena entrega de v3

Módulos 1–19 redactados y revisados documentalmente. Módulos 20–35 pendientes. Las prácticas en el Linux del estudiante siguen pendientes de comprobar.

**Nueva lección:** [Módulo 19 — Redes básicas: IP, DNS, rutas, ip y ss](modulo-19-redes-ip-dns-rutas-ip-ss.md).

Esta entrega introduce interfaces, IPv4/IPv6, prefijos, loopback, rutas y gateway, resolución de nombres, `ip`, `getent`, `resolvectl` opcional y `ss`. Las prácticas son únicamente locales y de lectura; no modifican interfaces, rutas o DNS y no incluyen escaneo de otras máquinas.

La v2 y los Módulos 1–18 se conservan intactos.

Siguiente paso editorial: **Módulo 20 — SSH en sistemas propios o expresamente autorizados**.

---

## Registro histórico — Decimoctava entrega y anteriores

# Estado actual — Decimoctava entrega de v3

Módulos 1–18 redactados y revisados documentalmente. Módulos 19–35 pendientes. Las prácticas en el Linux del estudiante siguen pendientes de comprobar.

**Nueva lección:** [Módulo 18 — Logs y diagnóstico inicial con journalctl](modulo-18-logs-journalctl-diagnostico.md).

Esta entrega introduce logs, systemd-journald y journalctl; filtros por arranque, unidad, prioridad y tiempo; seguimiento con `-f`; diferencias entre journal y archivos tradicionales; persistencia dependiente de configuración; privacidad de logs; diagnóstico antes de reiniciar; y una introducción conceptual a auditd.

La v2 y los Módulos 1–17 se conservan intactos.

Siguiente paso editorial: **Módulo 19 — Redes básicas: IP, DNS, rutas, ip y ss**.

---

## Registro histórico — Decimoséptima entrega y anteriores

# Estado actual — Decimoséptima entrega de v3

Módulos 1–17 redactados y revisados documentalmente. Módulos 18–35 pendientes. Las prácticas en el Linux del estudiante siguen pendientes de comprobar.

**Nueva lección:** [Módulo 17 — systemd, unidades y servicios; otros sistemas init en contexto](modulo-17-systemd-unidades-servicios-init.md).

Esta entrega introduce systemd como gestor principal del currículo sin presentarlo como el único init existente; diferencia unidades y servicios, start/enable, stop/disable, reload/restart y daemon-reload, e incorpora consultas seguras de estado, unidades, targets y timers. SysV init, OpenRC y runit se conservan como contexto de compatibilidad y otros entornos.

La v2 y los Módulos 1–16 se conservan intactos.

Siguiente paso editorial: **Módulo 18 — Logs y diagnóstico inicial con journalctl**.

---

## Registro histórico — Decimosexta entrega y anteriores

# Estado actual — Decimosexta entrega de v3

Módulos 1–16 redactados y revisados documentalmente. Módulos 17–35 pendientes. Las prácticas en el Linux del estudiante siguen pendientes de comprobar.

**Nueva lección:** [Módulo 16 — Diferencias entre Debian, Ubuntu, Fedora y RHEL](modulo-16-debian-ubuntu-fedora-rhel.md).

Esta entrega compara familias DEB y RPM, ciclos de publicación y soporte, APT/dpkg frente a DNF/RPM, Ubuntu LTS/interim, Debian stable/testing/unstable, Fedora tradicional frente a variantes image-based, AppArmor y SELinux, y evita generalizar UFW u otros defaults entre distribuciones.

La v2 y los Módulos 1–15 se conservan intactos.

Siguiente paso editorial: **Módulo 17 — systemd, unidades y servicios; otros sistemas init en contexto**.

---

## Registro histórico — Decimoquinta entrega y anteriores

# Estado actual — Decimoquinta entrega de v3

Módulos 1–15 redactados y revisados documentalmente. Módulos 16–35 pendientes. Las prácticas en el Linux del estudiante siguen pendientes de comprobar.

**Nueva lección:** [Módulo 15 — Paquetes, repositorios y actualizaciones](modulo-15-paquetes-repositorios-actualizaciones.md).

Esta entrega introduce paquetes, repositorios, dependencias y metadatos; separa APT/dpkg de DNF/RPM; distingue actualización de índices de actualización de paquetes; y limita las prácticas a consultas. Instalaciones, eliminaciones, actualizaciones y repositorios de terceros se explican sin ejecutarse como práctica básica.

La v2 y los Módulos 1–14 se conservan intactos.

Siguiente paso editorial: **Módulo 16 — Diferencias Debian, Ubuntu, Fedora y RHEL**.

---

## Registro histórico — Decimocuarta entrega y anteriores

# Estado actual — Decimocuarta entrega de v3

Módulos 1–14 redactados y revisados documentalmente. Módulos 15–35 pendientes. Las prácticas en el Linux del estudiante siguen pendientes de comprobar.

**Nueva lección:** [Módulo 14 — jobs, fg, bg, señales y kill](modulo-14-jobs-fg-bg-senales-kill.md).

Esta entrega introduce control de jobs con `jobs`, `fg`, `bg`, suspensión con `Ctrl+Z`, interrupción con `Ctrl+C`, señales y terminación controlada mediante `kill -TERM` sobre procesos `sleep` propios. SIGKILL se explica como último recurso y no se practica como hábito.

La v2 y los Módulos 1–13 se conservan intactos.

Siguiente paso editorial: **Módulo 15 — Paquetes, repositorios y actualizaciones**.

---

## Registro histórico — Decimotercera entrega y anteriores

# Estado actual — Decimotercera entrega de v3

Módulos 1–13 redactados y revisados documentalmente. Módulos 14–35 pendientes. Las prácticas en el Linux del estudiante siguen pendientes de comprobar.

**Nueva lección:** [Módulo 13 — Procesos: ps, top y htop opcional](modulo-13-procesos-ps-top-htop.md).

Esta entrega introduce procesos, PID, PPID, estados, observación con `ps` y `top`, métricas básicas de CPU/memoria y `htop` como herramienta opcional. No se terminan procesos ni se usan privilegios elevados; las señales se reservan para el Módulo 14.

La v2 y los Módulos 1–12 se conservan intactos.

Siguiente paso editorial: **Módulo 14 — jobs, fg, bg, señales y kill**.

---

## Registro histórico — Duodécima entrega y anteriores

# Estado actual — Duodécima entrega de v3

Módulos 1–12 redactados y revisados documentalmente. Módulos 13–35 pendientes. Las prácticas en el Linux del estudiante siguen pendientes de comprobar.

**Nueva lección:** [Módulo 12 — Permisos, propietarios, chmod, chown, umask, sudo y ACL básica](modulo-12-permisos-chmod-chown-umask-sudo-acl.md).

Esta entrega desarrolla permisos tradicionales para archivos y directorios, `chmod` simbólico y numérico, `chown` como concepto administrativo, `umask` mediante máscara de bits, mínimo privilegio con `sudo` y una introducción de lectura a ACL. Las prácticas modifican únicamente objetos propios del laboratorio.

La v2 y los Módulos 1–11 se conservan intactos.

Siguiente paso editorial: **Módulo 13 — Procesos; ps, top y htop opcional**.

---

## Registro histórico — Undécima entrega y anteriores

# Estado actual — Undécima entrega de v3

Módulos 1–11 redactados y revisados documentalmente. Módulos 12–35 pendientes. Las prácticas en el Linux del estudiante siguen pendientes de comprobar.

**Nueva lección:** [Módulo 11 — Usuarios y grupos: whoami, id, UID, GID e identidad](modulo-11-usuarios-grupos-identidad.md).

Esta entrega introduce usuarios, UID, grupos, GID, grupo primario y grupos suplementarios, consultas con `whoami` e `id`, lectura limitada de `/etc/passwd` y `/etc/group`, y reglas de seguridad para no trabajar como root ni exponer archivos de autenticación.

La v2 y los Módulos 1–10 se conservan intactos.

Siguiente paso editorial: **Módulo 12 — Permisos, propietarios, chmod, chown, umask, sudo y ACL básica**.

---

## Registro histórico — Décima entrega y anteriores

# Estado actual — Décima entrega de v3

Módulos 1–10 redactados y revisados documentalmente. Módulos 11–35 pendientes. Las prácticas en el Linux del estudiante siguen pendientes de comprobar.

**Nueva lección:** [Módulo 10 — grep, find y locate](modulo-10-grep-find-locate.md).

Esta entrega distingue búsqueda de contenido con `grep`, búsqueda de rutas actuales con `find` y búsqueda indexada con `locate`. Añade `grep -i`, `grep -n`, `find -type`, `find -name`, uso correcto de patrones citados y la advertencia de que `locate` puede no estar instalado o tener un índice desactualizado.

La v2 y los Módulos 1–9 se conservan intactos.

Siguiente paso editorial: **Módulo 11 — Usuarios y grupos; whoami, id y conceptos de identidad**.

---

## Registro histórico — Novena entrega y anteriores

# Estado actual — Novena entrega de v3

Módulos 1–9 redactados y revisados documentalmente. Módulos 10–35 pendientes. Las prácticas en el Linux del estudiante siguen pendientes de comprobar.

**Nueva lección:** [Módulo 9 — Tuberías (pipes) y composición de comandos](modulo-09-pipes-composicion-comandos.md).

Esta entrega introduce `|` como conexión entre stdout e stdin, diferencia pipes de redirecciones, explica por qué stderr no entra por defecto en la tubería normal y añade una regla explícita de no canalizar código descargado o desconocido directamente a intérpretes.

La v2 y los Módulos 1–8 se conservan intactos.

Siguiente paso editorial: **Módulo 10 — grep, find y locate; búsqueda de texto y archivos**.

---

## Registro histórico — Octava entrega y anteriores

# Estado actual — Octava entrega de v3

Módulos 1–8 redactados y revisados documentalmente. Módulos 9–35 pendientes. Las prácticas en el Linux del estudiante siguen pendientes de comprobar.

**Nueva lección:** [Módulo 8 — stdin, stdout, stderr y redirecciones](modulo-08-stdin-stdout-stderr-redirecciones.md).

Esta entrega introduce los flujos estándar 0/1/2, las redirecciones `>`, `>>`, `2>` y `<`, el riesgo de truncamiento con `>`, la separación entre stdout y stderr y el error conceptual de anteponer `sudo` sin entender quién procesa la redirección.

La v2 y los Módulos 1–7 se conservan intactos.

Siguiente paso editorial: **Módulo 9 — Tuberías (pipes) y composición de comandos**.

---

## Registro histórico — Séptima entrega y anteriores

# Estado actual — Séptima entrega de v3

Módulos 1–7 redactados y revisados documentalmente. Módulos 8–35 pendientes. Las prácticas en el Linux del estudiante siguen pendientes de comprobar.

**Nueva lección:** [Módulo 7 — Leer archivos con cat, less, head y tail](modulo-07-cat-less-head-tail.md).

Esta entrega añade selección de herramientas de lectura según tamaño y objetivo, navegación con `less`, lectura parcial con `head` y `tail`, seguimiento básico con `tail -f`, y reglas de privacidad para no compartir archivos o logs completos sin revisión.

La v2 y los Módulos 1–6 se conservan intactos.

Siguiente paso editorial: **Módulo 8 — stdin, stdout, stderr y redirecciones**.

---

## Registro histórico — Sexta entrega y anteriores

# Estado actual — Sexta entrega de v3

Módulos 1–6 redactados y revisados documentalmente. Módulos 7–35 pendientes. Las prácticas en el Linux del estudiante siguen pendientes de comprobar.

**Nueva lección:** [Módulo 6 — Crear, copiar, mover, renombrar y borrar con seguridad](modulo-06-crear-copiar-mover-borrar-seguro.md).

Esta entrega añade `touch`, `mkdir`, `cp`, `mv`, `rm` y `rmdir` con énfasis en verificación de ubicación, objetivo y alcance. `rm -rf` queda fuera de las prácticas rutinarias de principiante.

La v2 y los Módulos 1–5 se conservan intactos.

Siguiente paso editorial: **Módulo 7 — Lectura de archivos con cat, less, head y tail**.

---

## Registro histórico — Quinta entrega y anteriores

# Estado actual — Quinta entrega de v3

Módulos 1–5 redactados y revisados documentalmente. Módulos 6–35 pendientes. Las prácticas en el Linux del estudiante siguen pendientes de comprobar.

**Nueva lección:** [Módulo 5 — Árbol de archivos, FHS, /proc, /sys y enlaces](modulo-05-arbol-fhs-proc-sys-enlaces.md).

Esta entrega añade el modelo del árbol con raíz `/`, FHS, las funciones generales de `/etc`, `/usr`, `/var`, `/tmp`, `/proc` y `/sys`, y una introducción segura a enlaces simbólicos. Las consultas del sistema son de lectura; cualquier modificación de `/proc`, `/sys` o configuración queda fuera de esta práctica.

La v2 y los Módulos 1–4 se conservan intactos.

Siguiente paso editorial: **Módulo 6 — Crear, copiar, mover y renombrar; rm y rmdir con seguridad**.

---

## Registro histórico — Cuarta entrega y anteriores

# Estado actual — Cuarta entrega de v3

Módulos 1–4 redactados y revisados documentalmente. Módulos 5–35 pendientes. Las prácticas en el Linux del estudiante siguen pendientes de comprobar.

**Nueva lección:** [Módulo 4 — Rutas absolutas, relativas y nombres con espacios](modulo-04-rutas-absolutas-relativas-espacios.md).

Incluye interpretación de rutas, tilde, punto y doble punto, comillas y un recorrido guiado entre carpetas de práctica. La v2 y las lecciones anteriores se conservan intactas. La nueva instantánea Markdown para Drive reúne siete archivos y conserva las copias de entregas anteriores; no constituye sincronización automática.

Siguiente paso editorial: Módulo 5, árbol de archivos, FHS y enlaces.

---

## Registro histórico — Tercera entrega y anteriores

El contenido siguiente se conserva íntegro y refleja el estado de cada entrega pasada.

# Estado actual — Tercera entrega de v3

Módulos 1, 2 y 3 redactados y revisados documentalmente. Módulos 4–35 pendientes. Las prácticas en el Linux del estudiante siguen pendientes de comprobar.

**Nueva lección:** [Módulo 3 — Navegación inicial: pwd, ls y cd](modulo-03-navegacion-pwd-ls-cd.md).

Esta entrega añade consultas de ubicación, listados y navegación, con explicación paso a paso, errores y evaluación. La v2 y las lecciones anteriores permanecen intactas. La nueva copia para Drive reúne los seis archivos actuales y conserva la copia de la segunda entrega; es una instantánea, no sincronización automática.

Siguiente paso editorial: Módulo 4, rutas absolutas y relativas.

---

## Registro histórico — Segunda entrega

Todo el contenido que sigue corresponde a la segunda entrega y se conserva íntegro. Sus pendientes y su recuento de archivos describen ese momento.

# Manual Maestro de Linux y Shell Scripting — v3 · Estado actual

## Segunda entrega

Este es el punto de entrada actualizado de la v3. Se conservan intactos los tres archivos de la primera entrega: sus referencias a «Módulos 2–35 pendientes» describen aquel corte histórico, no el estado actual.

| Contenido | Estado | Archivo |
|---|---|---|
| Arquitectura de 35 módulos | Definida | [Índice original](00-indice-arquitectura.md) |
| Módulo 1 | Redactado y revisado documentalmente | [GNU, Linux, kernel y distribuciones](01-gnu-linux-kernel-distribuciones.md) |
| Módulo 2 | Redactado y revisado documentalmente | [Terminal, CLI, shell, Bash, prompt y ayuda](modulo-02-terminal-cli-shell-bash-ayuda.md) |
| Auditoría de la primera entrega | Conservada | [Registro de auditoría y fuentes](02-auditoria-fuentes.md) |
| Módulos 3–35 | Pendientes de redacción | Consultar el índice |
| Prácticas en el Linux del estudiante | Pendientes de comprobar | No equivalen a revisión documental |

## Orden de lectura

Lee M1 y después M2. La arquitectura sirve de mapa y la auditoría documenta decisiones y límites. El prefijo `02` de `02-auditoria-fuentes.md` es el nombre histórico del registro, **no el Módulo 2**. Para evitar confusión sin renombrar archivos existentes, las nuevas lecciones usan `modulo-NN-tema.md`.

## Conservación y copias

La v2 permanece separada en `linux/manuales/manual-maestro-linux-shell-scripting-2026-v2.md`. Los archivos originales no se eliminan ni se reemplazan en esta entrega.

La copia para Drive es una instantánea Markdown de estos cinco archivos, con este estado actual al inicio y las secciones históricas claramente identificadas. No es un manual de 35 módulos terminados ni una sincronización automática. Los enlaces de la instantánea apuntan a los archivos de GitHub para mantener la navegación fuera de una carpeta local.

El resultado y enlace de la subida se confirman en el chat después de verificar el archivo remoto. La existencia de este README no acredita por sí sola una publicación en Drive.

## Cambios de esta entrega

- Nueva lección de terminal y ayuda, con ejemplos explicados, recuperación de errores y evaluación.
- Distinción entre prompt, privilegios, shell actual y versión de Bash consultada.
- Estado actualizado mediante un archivo nuevo, preservando los documentos anteriores.
- Siguiente paso editorial: Módulo 3. El avance del estudiante sigue dependiendo de sus ejercicios.