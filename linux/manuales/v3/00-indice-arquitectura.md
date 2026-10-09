# Manual Maestro de Linux y Shell Scripting — Edición 2026

## v3 auditada · Primera entrega: arquitectura y Módulo 1

Fecha editorial: 6 de octubre de 2026. Estado: trabajo en progreso. La revisión de esta entrega no equivale a validar los 35 módulos ni a certificar un sistema.

**Empieza aquí:** [Módulo 1 — GNU, Linux, kernel y distribuciones](modulo-01-gnu-linux-kernel-distribuciones.md). Consulta después el [registro de auditoría y fuentes](02-auditoria-fuentes.md).

### 1. Propósito y alcance

Aprender desde cero a entender, utilizar y administrar GNU/Linux y escribir scripts de Bash. Cada práctica debe poder explicarse, repetirse sin copiar y revisarse ante errores. No se presupone experiencia con terminal, programación ni administración.

Esta entrega contiene el diseño completo y únicamente el primer módulo desarrollado. Los módulos 2–35 son un plan de trabajo; sus títulos no implican que sus lecciones o prácticas ya estén redactadas o probadas.

La base documental es la v2 del repositorio y el informe de NotebookLM adjunto a la conversación «Analizar enlace NotebookLM». Se conserva la intención pedagógica del informe y se corrigen sus generalizaciones. No se importan como evidencia sus referencias numéricas sin una bibliografía identificable.

### 2. Conservación y organización

La v2 permanece en `linux/manuales/manual-maestro-linux-shell-scripting-2026-v2.md`. Esta edición se guarda en otra carpeta: `linux/manuales/v3/`.

| Archivo nuevo | Función |
|---|---|
| `00-indice-arquitectura.md` | Alcance, índice, progresión y reglas editoriales |
| `modulo-01-gnu-linux-kernel-distribuciones.md` | Primera lección completa, práctica y evaluación |
| `02-auditoria-fuentes.md` | Correcciones, fuentes, límites de verificación y pendientes |

Se recomienda esta organización modular: facilita estudiar una lección y revisar commits pequeños. Un archivo único facilita imprimir, pero crece rápidamente y dificulta revisar cambios. La compilación integral se preparará cuando existan más módulos; no se duplican hoy contenidos en dos versiones que puedan divergir.

La numeración cambia: el Módulo 0 conceptual de v2 pasa a ser Módulo 1 de v3. El Módulo 1 de v2, dedicado a terminal, corresponde al Módulo 2 de v3. La navegación de v2 se desglosa en los módulos 3–5. No se interpreta esta renumeración como eliminación del original.

### 3. Método de cada lección

1. Objetivo observable y conocimientos previos.
2. Qué es el concepto y para qué sirve.
3. Una forma de uso y un ejemplo pequeño.
4. Explicación de cada línea, opción y argumento nuevo.
5. Resultado esperado, distinguiendo ejemplo ilustrativo de salida real.
6. Errores frecuentes: causa, corrección mínima y comprobación.
7. Ejercicio guiado, variante independiente y detección de un error.
8. Mini evaluación sin conceptos nuevos y recuperación posterior.
9. Fuentes, entorno compatible y riesgos de la práctica.

Estados del aprendizaje: **NO VISTO → EN APRENDIZAJE → PRACTICADO → DOMINADO**. Una respuesta correcta no basta: se requiere explicación propia, resolución autónoma y detección de errores en más de una ocasión. El estado de redacción de un módulo se registra por separado del aprendizaje del estudiante.

### 4. Índice v3

Los resultados de la última columna son metas de evaluación, no logros ya obtenidos.

#### Fase I — Fundamentos y línea de comandos

| Módulo | Contenido | Evidencia de aprendizaje |
|---|---|---|
| 1 | GNU, Linux, kernel y distribuciones; laboratorio seguro | Distinguir núcleo, distribución y herramienta; identificar el entorno |
| 2 | Terminal, CLI, shell, Bash, prompt y ayuda | Diferenciar interfaz e intérprete; leer un error sin improvisar |
| 3 | Navegación inicial: `pwd`, `ls`, `cd` | Ubicarse y cambiar de carpeta conscientemente |
| 4 | Rutas absolutas y relativas; `~`, `.`, `..`; nombres con espacios | Predecir qué ruta se utilizará antes de ejecutar |
| 5 | Árbol de archivos y FHS; `/etc`, `/usr`, `/var`, `/tmp`, `/proc`, `/sys` | Separar datos, configuración y vistas del kernel; reconocer enlaces |
| 6 | Crear, copiar, mover y renombrar; `rm` y `rmdir` | Trabajar en el laboratorio sin sobrescribir originales |
| 7 | Lectura: `cat`, `less`, `head`, `tail` | Elegir una herramienta según tamaño y propósito |
| 8 | Flujos estándar y redirecciones | Explicar `>`, `>>`, `2>` y el riesgo de truncamiento |
| 9 | Tuberías y procesamiento de texto | Conectar salida y entrada sin confundirlas con archivos |
| 10 | `grep`, `find`, `locate`; introducción a patrones | Distinguir búsqueda de texto, recorrido e índice |

#### Fase II — Identidad, permisos y procesos

| Módulo | Contenido | Evidencia de aprendizaje |
|---|---|---|
| 11 | Usuarios y grupos; `whoami`, `id` | Interpretar identidad y pertenencia a grupos |
| 12 | Permisos, propietarios, `chmod`, `chown`, `umask`, `sudo`; introducción a ACL | Explicar los permisos de un objeto antes de cambiarlos |
| 13 | Procesos; `ps`, `top`; `htop` opcional | Identificar un proceso propio y sus recursos |
| 14 | Trabajos, `jobs`, `fg`, `bg` y señales | Distinguir suspender, continuar y terminar |

#### Fase III — Sistemas, servicios y redes

| Módulo | Contenido | Evidencia de aprendizaje |
|---|---|---|
| 15 | Paquetes, repositorios y actualizaciones | Identificar el gestor adecuado y revisar una operación |
| 16 | Diferencias Debian, Ubuntu, Fedora y RHEL | Seleccionar instrucciones para la distribución y versión reales |
| 17 | Servicios y arranque: systemd como itinerario principal; otros init | Separar consulta, inicio, habilitación y configuración |
| 18 | Registros: `journalctl`, archivos de log; introducción a auditoría | Buscar un evento sin publicar datos sensibles |
| 19 | Redes básicas: IP, DNS, rutas, `ip`, `ss` | Distinguir problemas de dirección, resolución y conectividad |
| 20 | SSH en equipos propios o autorizados | Explicar identidad del servidor, autenticación y cuidado de claves |
| 21 | Cortafuegos: nftables, UFW y firewalld según entorno | Diseñar reglas y recuperación antes de aplicarlas |
| 22 | Edición con vi/Vim desde cero | Guardar una copia de práctica y salir sin perder trabajo |

#### Fase IV — Shell scripting con Bash

| Módulo | Contenido | Evidencia de aprendizaje |
|---|---|---|
| 23 | Primer script, intérprete, shebang y ejecución | Explicar `bash archivo.sh` y ejecución directa |
| 24 | Variables, entrada, argumentos, expansiones y comillas | Preservar texto y límites de argumentos, incluido `"$@"` |
| 25 | Códigos de salida y composición de órdenes | Interpretar éxito y fallo según el comando |
| 26 | Decisiones: `if`, `test`, `[ ]`, `[[ ]]`, `case` y aritmética | Elegir Bash o portabilidad POSIX y justificarlo |
| 27 | Bucles, lectura de líneas y nombres de archivo | Recorrer datos con espacios sin analizar la salida de `ls` |
| 28 | Funciones, parámetros y ámbito | Separar tareas y validar entradas |
| 29 | Errores, `trap`, `mktemp`, límites de `set -e/-u` y ShellCheck | Probar fallos controlados y explicar límites de la limpieza |

#### Fase V — Automatización y administración defensiva

| Módulo | Contenido | Evidencia de aprendizaje |
|---|---|---|
| 30 | `cron` y temporizadores de systemd | Probar manualmente antes de programar una tarea |
| 31 | Archivos y compresión: `tar`, `gzip`, `xz` | Inspeccionar un archivo antes de extraerlo |
| 32 | Copias y restauración con `rsync` | Verificar una restauración y explicar riesgos de sincronizar |
| 33 | Git y GitHub para scripts; enlace al itinerario específico de Git | Revisar diferencias y guardar commits sin secretos |
| 34 | Almacenamiento: `lsblk`, `df`, `du`; montaje y `fstab` | Separar inspección de cambios de alto impacto |
| 35 | Defensa, actualizaciones, mínimo privilegio, auditoría y AIDE | Documentar un laboratorio propio con evidencia y recuperación |

Ampliaciones posteriores, fuera del núcleo inicial: namespaces, cgroups, contenedores, eBPF, Rust en el kernel y EEVDF en profundidad. Las herramientas `rg`, `fd`, `bat` o `eza` serán complementarias, sin exigir instalaciones al principiante.

### 5. Dependencias y ajustes pedagógicos

Las fases se cursan en orden. Cada módulo parte del anterior, con estas precisiones:

- El Módulo 1 incluye una preparación guiada mínima del laboratorio. No exige dominar todos sus comandos; los módulos 2–6 retoman cada uno con práctica más amplia.
- Las rutas anteceden a la descripción extensa del árbol para reducir abstracción antes de trabajar con archivos.
- El Módulo 6 podrá introducir un editor gráfico disponible para crear notas; el dominio de Vim se reserva al 22.
- Los códigos de salida anteceden a `if`, porque las condiciones de la shell se apoyan en el resultado de comandos.
- La conservación en GitHub empieza desde esta entrega, gestionada por el tutor. El estudiante no necesita dominar Git para que se conserve su trabajo. El Módulo 33 formaliza su autonomía.
- La lectura precede siempre a cambios en servicios, red, almacenamiento y seguridad.

### 6. Contrato de seguridad

Las prácticas se limitan a equipos propios o expresamente autorizados. Se usa un usuario normal y el laboratorio `~/linux-lab`. Esa carpeta **no es una barrera de aislamiento**: una ruta absoluta, un enlace o un comando mal escrito puede alcanzar otros lugares.

Antes de modificar: explicar efecto, comprobar ubicación con `pwd`, inspeccionar con `ls` y comprobar también el destino exacto. Esos dos comandos ayudan, pero no garantizan por sí solos seguridad. Si una orden falla, detenerse antes de continuar con la siguiente.

No se exige `sudo` en prácticas iniciales. No se usa `rm -rf` como rutina. No se editan archivos del sistema ni se cambian discos, servicios o cortafuegos en el Módulo 1. Las prácticas posteriores con impacto necesitan copia o instantánea, alcance explícito y procedimiento de recuperación.

Cada práctica llevará una etiqueta: **consulta**, **creación en laboratorio**, **modificación** o **borrado**. El riesgo se evalúa por orden y opciones: un nombre de programa no basta. Un comando de consulta puede revelar información privada si se comparte su salida.

### 7. Compatibilidad y referencias de versión

- GNU Coreutils **9.11** es la referencia editorial solicitada y corroborada. No se afirma que esa sea la versión instalada ni que deba actualizarse el equipo para empezar. [Anuncio oficial](https://lists.gnu.org/archive/html/info-gnu/2026-04/msg00006.html).
- Bash se enseña indicando qué construcciones son propias de Bash y cuáles pertenecen a POSIX. No se asume que `/bin/sh` sea Bash. [Manual GNU Bash](https://www.gnu.org/s/bash/manual/bash.html).
- Para prácticas de RHEL 10 se prioriza la documentación de **RHEL 10**; RHEL 8 se mantiene como referencia contextual si ese es el sistema estudiado. No se trasladan recetas entre versiones automáticamente. [Guía oficial de seguridad de RHEL 10](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/index).
- Debian y Ubuntu tienen fichas separadas para cortafuegos y configuración. Fedora y RHEL también requieren verificar su versión; pertenecer a una familia no vuelve idénticos todos los procedimientos.
- systemd será el recorrido principal de servicios; se explicará que existen otros sistemas de inicio y entornos donde no actúa como gestor del sistema.

### 8. Puerta de revisión antes de cada entrega

Comprobar fuentes, versión y aplicabilidad; revisar cada ejemplo y su explicación; verificar enlaces internos; buscar contradicciones con módulos anteriores; comprobar que no se incluyen credenciales ni datos personales; conservar originales; guardar cambios pequeños. La prueba documental, la ejecución real y el dominio del estudiante se informan por separado.

Siguiente entrega prevista: Módulo 2, después de recibir el diagnóstico del estudiante. No se declara completado ni se redacta anticipadamente en este archivo.
