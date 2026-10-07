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