# Manual Maestro de Linux y Shell Scripting — v3

Edición 2026, versión vigente. Para registrar lo que ya practicaste usa [linux/PROGRESO.md](../../PROGRESO.md).

## Estado vigente — 9 de octubre de 2026

- **Núcleo:** los 35 módulos están redactados y revisados documentalmente.
- **Auditoría:** la [auditoría transversal completa](03-auditoria-transversal-completa-v3-2026-10-08.md) dio el dictamen *apto con correcciones importantes*. Las cinco correcciones de prioridad alta están aplicadas. El seguimiento posterior está en la [auditoría post-corrección parcial](04-auditoria-postcorreccion-parcial-2026-10-08.md).
- **Fuentes:** hallazgos E02, E04 y E05 aplicados. Los enlaces externos están clasificados y comprobados en el [catálogo de fuentes](06-catalogo-fuentes.md); 55 enlaces de GNU siguen sin verificar.
- **Pendientes editoriales:** verificar los 55 enlaces restantes, leer íntegramente los módulos no revisados en pasadas anteriores, verificar todos los bloques de código y diagramas en el PDF y sincronizar la edición íntegra actualizada a Google Drive.
- **Práctica del estudiante:** pendiente. Redacción completa no equivale a dominio demostrado.
- **Google Drive:** la Entrega 24 es una instantánea histórica; no representa el núcleo vigente y omitía el Módulo 23. La versión vigente del Módulo 20 es la de esta carpeta.
- **Regla de respaldo:** conservar versiones anteriores y generar una copia de cada edición corregida en Google Drive; no afirmar que está sincronizada hasta verificar su contenido.

## Cómo estudiar

1. Lee la [arquitectura del manual](00-indice-arquitectura.md) para entender la ruta.
2. Avanza en orden, empezando por el [Módulo 1](modulo-01-gnu-linux-kernel-distribuciones.md). Cada módulo tiene enlaces al anterior y al siguiente arriba y al final.
3. No pases al siguiente módulo hasta completar su práctica y su mini evaluación.

## Módulos

Las fases son las definidas en la [arquitectura](00-indice-arquitectura.md).

### Fase I — Fundamentos y línea de comandos (módulos 1–10)

| N.º | Módulo |
|---|---|
| 1 | [GNU, Linux, kernel y distribuciones](modulo-01-gnu-linux-kernel-distribuciones.md) |
| 2 | [Terminal, CLI, shell, Bash, prompt y ayuda](modulo-02-terminal-cli-shell-bash-ayuda.md) |
| 3 | [Navegación inicial: pwd, ls y cd](modulo-03-navegacion-pwd-ls-cd.md) |
| 4 | [Rutas absolutas y relativas; ~, ., .. y nombres con espacios](modulo-04-rutas-absolutas-relativas-espacios.md) |
| 5 | [Árbol de archivos, FHS, /etc, /usr, /var, /tmp, /proc, /sys y enlaces](modulo-05-arbol-fhs-proc-sys-enlaces.md) |
| 6 | [Crear, copiar, mover, renombrar y borrar con seguridad](modulo-06-crear-copiar-mover-borrar-seguro.md) |
| 7 | [Leer archivos con cat, less, head y tail](modulo-07-cat-less-head-tail.md) |
| 8 | [stdin, stdout, stderr y redirecciones](modulo-08-stdin-stdout-stderr-redirecciones.md) |
| 9 | [Tuberías (pipes) y composición de comandos](modulo-09-pipes-composicion-comandos.md) |
| 10 | [grep, find y locate: buscar texto y archivos](modulo-10-grep-find-locate.md) |

### Fase II — Identidad, permisos y procesos (módulos 11–14)

| N.º | Módulo |
|---|---|
| 11 | [Usuarios y grupos: whoami, id, UID, GID e identidad](modulo-11-usuarios-grupos-identidad.md) |
| 12 | [Permisos, propietarios, chmod, chown, umask, sudo y ACL básica](modulo-12-permisos-chmod-chown-umask-sudo-acl.md) |
| 13 | [Procesos: ps, top y htop opcional](modulo-13-procesos-ps-top-htop.md) |
| 14 | [jobs, fg, bg, señales y kill](modulo-14-jobs-fg-bg-senales-kill.md) |

### Fase III — Sistemas, servicios y redes (módulos 15–22)

| N.º | Módulo |
|---|---|
| 15 | [Paquetes, repositorios y actualizaciones](modulo-15-paquetes-repositorios-actualizaciones.md) |
| 16 | [Diferencias entre Debian, Ubuntu, Fedora y RHEL](modulo-16-debian-ubuntu-fedora-rhel.md) |
| 17 | [systemd, unidades y servicios; otros sistemas init en contexto](modulo-17-systemd-unidades-servicios-init.md) |
| 18 | [Logs y diagnóstico inicial con journalctl](modulo-18-logs-journalctl-diagnostico.md) |
| 19 | [Redes básicas: IP, DNS, rutas, ip y ss](modulo-19-redes-ip-dns-rutas-ip-ss.md) |
| 20 | [SSH en sistemas propios o expresamente autorizados](modulo-20-ssh-sistemas-autorizados.md) |
| 21 | [Firewall: nftables, UFW y firewalld según el entorno](modulo-21-firewall-nftables-ufw-firewalld.md) |
| 22 | [vi/Vim: edición segura de archivos de texto](modulo-22-vi-vim-edicion-segura.md) |

### Fase IV — Shell scripting con Bash (módulos 23–29)

| N.º | Módulo |
|---|---|
| 23 | [Primer script Bash y shebang](modulo-23-primer-script-bash-shebang.md) |
| 24 | [Variables, entrada, argumentos, expansiones y quoting en Bash](modulo-24-variables-entrada-argumentos-quoting.md) |
| 25 | [Códigos de salida y composición de órdenes en Bash](modulo-25-codigos-salida-composicion-ordenes.md) |
| 26 | [Decisiones con `if`, `test`, `[ ]`, `[[ ]]`, `case` y aritmética](modulo-26-if-test-condicionales-case-aritmetica.md) |
| 27 | [Bucles, lectura de líneas y nombres de archivo seguros](modulo-27-bucles-lectura-lineas-nombres-seguros.md) |
| 28 | [Funciones, parámetros y ámbito en Bash](modulo-28-funciones-parametros-ambito.md) |
| 29 | [Manejo de errores, `trap`, `mktemp`, límites de `set -e`/`set -u` y ShellCheck](modulo-29-manejo-errores-trap-mktemp-shellcheck.md) |

### Fase V — Automatización y administración defensiva (módulos 30–35)

| N.º | Módulo |
|---|---|
| 30 | [Automatización con `cron` y temporizadores de systemd](modulo-30-cron-temporizadores-systemd.md) |
| 31 | [Archivos y compresión con `tar`, `gzip` y `xz`](modulo-31-tar-gzip-xz-archivos-compresion.md) |
| 32 | [Copias, sincronización y restauración con `rsync`](modulo-32-rsync-copias-restauracion.md) |
| 33 | [Git y GitHub para scripts; puente al itinerario específico de Git](modulo-33-git-github-para-scripts.md) |
| 34 | [Almacenamiento: `lsblk`, `df`, `du`, montaje y `fstab`](modulo-34-almacenamiento-lsblk-df-du-montaje-fstab.md) |
| 35 | [Defensa, actualizaciones, mínimo privilegio, auditoría y AIDE](modulo-35-defensa-actualizaciones-minimo-privilegio-aide.md) |

## Documentos de control

No son lecciones; documentan cómo se revisó el manual.

| Archivo | Contenido |
|---|---|
| [00 — Índice y arquitectura](00-indice-arquitectura.md) | Diseño del manual y plan de los 35 módulos (escrito en la primera entrega). |
| [02 — Auditoría y fuentes](02-auditoria-fuentes.md) | Registro histórico de la primera entrega. |
| [03 — Auditoría transversal completa](03-auditoria-transversal-completa-v3-2026-10-08.md) | Revisión de los 35 módulos y hallazgos. |
| [04 — Auditoría post-corrección parcial](04-auditoria-postcorreccion-parcial-2026-10-08.md) | Seguimiento de las correcciones aplicadas. |
| [05 — Historial de entregas](05-historial-entregas.md) | Estado de cada entrega, de la más reciente a la más antigua. |
| [06 — Catálogo de fuentes](06-catalogo-fuentes.md) | Jerarquía de fuentes y estado de cada enlace externo. |

La versión anterior del manual (v2) se conserva en [`../manual-maestro-linux-shell-scripting-2026-v2.md`](../manual-maestro-linux-shell-scripting-2026-v2.md).
