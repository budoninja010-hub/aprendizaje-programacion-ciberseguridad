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