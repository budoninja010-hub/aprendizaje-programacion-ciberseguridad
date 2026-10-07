# Módulo 17 — systemd, unidades y servicios; otros sistemas init en contexto

Manual Maestro de Linux y Shell Scripting — Edición 2026 · v3 · Decimoséptima entrega.

[Estado actual](README.md) · [Módulo anterior](modulo-16-debian-ubuntu-fedora-rhel.md) · [Arquitectura](00-indice-arquitectura.md)

## 1. Qué aprenderás

Al terminar este módulo podrás:

- explicar qué función cumple un sistema init;
- reconocer a systemd como sistema y gestor de servicios ampliamente usado en distribuciones Linux actuales;
- explicar qué es una unidad de systemd;
- distinguir una unidad `.service` de otros tipos de unidad;
- usar `systemctl` para consultar estado sin modificar servicios;
- distinguir `start` de `enable`;
- distinguir `stop` de `disable`;
- comprender `restart`, `reload` y `daemon-reload`;
- comprender qué significa que una unidad esté `masked`;
- reconocer que SysV init, OpenRC, runit y otros sistemas existen y que systemd no es universal;
- evitar modificar servicios sin identificar antes la unidad, el impacto y la distribución.

Conocimientos previos:
- procesos;
- usuarios y privilegios;
- paquetes y distribuciones;
- lectura de archivos;
- comandos de consulta.

**Seguridad:** las prácticas obligatorias son de lectura. No iniciaremos, detendremos, reiniciaremos, habilitaremos, deshabilitaremos ni enmascararemos servicios del sistema. No editaremos archivos de unidades. No usaremos `sudo` en los ejercicios de consulta.

## 2. Qué problema resuelve un sistema init

Durante el arranque del sistema, después de que el kernel inicia el espacio de usuario, debe existir un proceso encargado de coordinar servicios y otras tareas del sistema.

Tradicionalmente ese papel se asocia al sistema **init**.

En un sistema Linux con systemd como init del sistema, systemd normalmente ocupa:

```text
PID 1
```

Puedes consultar PID 1 sin modificar nada:

```bash
ps -p 1 -o pid,comm,args
```

No asumas que todos los sistemas Linux usan systemd. Contenedores, sistemas embebidos y distribuciones específicas pueden usar otros diseños.

## 3. systemd es más que “arrancar servicios”

systemd funciona como un **system and service manager**.

Entre sus responsabilidades puede incluir:

- gestión de servicios;
- dependencias entre unidades;
- sockets;
- timers;
- puntos de montaje;
- sesiones y scopes;
- seguimiento de procesos mediante cgroups;
- integración con logging mediante journald;
- objetivos de arranque.

No necesitas dominar todas estas funciones en una sola lección.

## 4. Qué es una unidad

systemd organiza recursos y tareas mediante **units**.

Una unidad se identifica mediante un nombre como:

```text
ssh.service
cron.service
systemd-journald.service
multi-user.target
example.timer
example.socket
```

Los nombres reales dependen del sistema.

Modelo:

```text
nombre.tipo
```

La extensión indica el tipo de unidad.

## 5. Tipos frecuentes de unidad

Algunos tipos comunes:

```text
.service   → servicio/proceso administrado
.socket    → socket para activación
.timer     → temporizador
.target    → agrupación/sincronización de unidades
.path      → observa cambios en rutas
.mount     → punto de montaje
.automount → automontaje
.swap      → swap
.device    → dispositivo
.scope     → procesos creados externamente agrupados por systemd
.slice     → agrupación jerárquica de recursos
```

No memorices todos ahora. Para empezar debes reconocer sobre todo:

```text
.service
.target
.timer
```

## 6. systemctl

`systemctl` permite consultar y controlar el gestor systemd.

Consulta:

```bash
systemctl --version
```

Puede mostrar:

- versión de systemd;
- características compiladas.

Esto no demuestra por sí solo que systemd sea PID 1. Para verificar el init real puedes consultar:

```bash
ps -p 1 -o comm=
```

## 7. Ver estado general

Consulta:

```bash
systemctl status
```

Puede mostrar un resumen del estado del sistema systemd.

En algunos entornos, la salida puede abrirse en un paginador.

Para salir del paginador:

```text
q
```

No confundas un estado degradado con una instrucción automática de reiniciar o reparar; primero identifica qué unidad falló.

## 8. Listar unidades cargadas

Para listar unidades actualmente cargadas:

```bash
systemctl list-units
```

Para limitar a servicios:

```bash
systemctl list-units --type=service
```

Esto muestra unidades que systemd tiene cargadas según los filtros y estado.

No es lo mismo que listar todos los archivos de unidades instalados.

## 9. list-unit-files

Para consultar archivos de unidades conocidos:

```bash
systemctl list-unit-files
```

Solo servicios:

```bash
systemctl list-unit-files --type=service
```

Puede mostrar estados como:

```text
enabled
disabled
masked
static
indirect
generated
```

No todos esos estados significan “está ejecutándose” o “está detenido”.

## 10. Estado activo y estado de habilitación son conceptos distintos

Dos preguntas diferentes:

```text
¿está activo ahora?
¿está configurado para activarse según enlaces/dependencias al arranque u otros mecanismos?
```

Herramientas:

```bash
systemctl is-active NOMBRE.service
systemctl is-enabled NOMBRE.service
```

Una unidad puede estar:

- activa pero disabled;
- inactiva pero enabled;
- activa y enabled;
- inactiva y disabled.

No deduzcas una condición a partir de la otra.

## 11. start frente a enable

Conceptualmente:

```text
systemctl start servicio.service
```

intenta iniciar la unidad **ahora**.

En cambio:

```text
systemctl enable servicio.service
```

configura la habilitación según la sección `[Install]` y las relaciones definidas para futuras activaciones, habitualmente relacionadas con el arranque.

**start no implica enable.**
**enable no implica necesariamente start inmediato.**

Existen combinaciones como `enable --now`, pero no las practicaremos todavía.

## 12. stop frente a disable

Conceptualmente:

```text
systemctl stop servicio.service
```

intenta detener la unidad **ahora**.

```text
systemctl disable servicio.service
```

retira la habilitación configurada para futuras activaciones según su instalación.

**stop no implica disable.**
**disable no implica necesariamente detener un servicio que ya está corriendo.**

Esta diferencia es fundamental.

## 13. restart

```text
systemctl restart servicio.service
```

detiene e inicia de nuevo según el comportamiento de la unidad.

Un restart puede:

- interrumpir conexiones;
- provocar una breve indisponibilidad;
- afectar aplicaciones dependientes;
- reinicializar estado.

Por eso no se ejecuta sin entender el servicio.

## 14. reload

```text
systemctl reload servicio.service
```

solicita al servicio que recargue su configuración sin realizar necesariamente un reinicio completo.

**No todos los servicios soportan reload.**

Por eso `reload` no es un sustituto universal de `restart`.

## 15. daemon-reload no reinicia servicios

```text
systemctl daemon-reload
```

hace que el gestor systemd vuelva a cargar archivos de unidad y regenere ciertas dependencias internas.

No significa:

```text
reiniciar todos los servicios
```

Puede ser necesario después de modificar archivos de unidades, pero en esta lección no editaremos unidades ni ejecutaremos `daemon-reload`.

## 16. status de una unidad

Una de las consultas más útiles:

```bash
systemctl status NOMBRE.service
```

Puede mostrar:

- estado cargado;
- estado activo;
- PID principal;
- información reciente;
- fragmento de logs;
- ruta de la unidad.

No pegues la salida completa en GitHub si contiene nombres de host, rutas privadas o información sensible.

## 17. systemctl show

Para datos estructurados:

```bash
systemctl show NOMBRE.service
```

Puede producir muchas propiedades.

Puedes pedir solo una:

```bash
systemctl show -p ActiveState NOMBRE.service
```

o varias:

```bash
systemctl show -p ActiveState -p SubState -p FragmentPath NOMBRE.service
```

Esto es útil para aprender a separar propiedades concretas.

## 18. systemctl cat

Para ver la definición efectiva de una unidad y sus fragmentos:

```bash
systemctl cat NOMBRE.service
```

Es preferible para principiantes a adivinar dónde vive el archivo.

Los archivos de unidades pueden proceder de ubicaciones como:

```text
/etc/systemd/system/
/run/systemd/system/
/usr/lib/systemd/system/
```

y, según distribución/compatibilidad, pueden encontrarse rutas relacionadas como:

```text
/lib/systemd/system/
```

No edites directamente archivos del proveedor para “probar”.

## 19. /etc frente a archivos del proveedor

Regla conceptual:

```text
/usr/lib o /lib → unidades proporcionadas por paquetes/proveedor
/etc/systemd    → configuración administrativa local y overrides
/run/systemd    → unidades/configuración de tiempo de ejecución
```

La disposición exacta depende de la distribución.

Cuando llegue el módulo avanzado, aprenderás a usar overrides en lugar de modificar archivos del paquete.

## 20. Qué significa masked

Una unidad **masked** queda impedida de iniciarse normalmente mediante el mecanismo de systemd porque su nombre se enlaza a `/dev/null` o se aplica una máscara equivalente según el contexto.

Conceptualmente:

```text
disabled → no habilitada para activación configurada al arranque
masked   → inicio bloqueado de forma más fuerte
```

No enmascares unidades para experimentar.

## 21. static no significa “rota”

Una unidad marcada como:

```text
static
```

normalmente no contiene instrucciones de instalación para habilitarla directamente con el mecanismo estándar de `enable`.

Puede ser activada por:

- dependencias;
- sockets;
- timers;
- otras unidades;
- activación explícita.

No intentes “arreglarla” porque no diga enabled.

## 22. Targets

Los `.target` agrupan y sincronizan unidades.

Ejemplos comunes:

```text
multi-user.target
graphical.target
rescue.target
```

Cumplen un papel conceptual parecido a puntos de sincronización o agrupación del estado del sistema.

No los confundas de forma simplista con los antiguos runlevels: existen relaciones de compatibilidad, pero systemd usa un modelo de dependencias más amplio.

## 23. Target predeterminado

Consulta:

```bash
systemctl get-default
```

Puede devolver algo como:

```text
graphical.target
```

o:

```text
multi-user.target
```

No cambies el target predeterminado en esta lección.

## 24. Timers

Una unidad:

```text
algo.timer
```

puede activar otra unidad según un horario o evento temporal.

Consulta segura:

```bash
systemctl list-timers
```

Los timers se estudiarán con detalle en el Módulo 30 junto con cron.

## 25. Sockets

Una unidad:

```text
algo.socket
```

puede permitir activación de servicios al recibir actividad en un socket.

Consulta:

```bash
systemctl list-units --type=socket
```

No necesitas entender todavía todos los mecanismos de socket activation.

## 26. Dependencias

Las unidades pueden declarar relaciones como:

```text
Requires=
Wants=
After=
Before=
```

Estas relaciones no son todas equivalentes.

Por ejemplo:

- `After=` describe orden;
- `Requires=` expresa una dependencia más fuerte;
- `Wants=` expresa una dependencia más débil.

No reduzcas todo a “A depende de B” sin distinguir orden y requisito.

## 27. systemctl list-dependencies

Consulta:

```bash
systemctl list-dependencies NOMBRE.service
```

Permite observar relaciones.

No modifiques unidades después de ver una dependencia inesperada.

La relación puede existir por razones de arranque, montaje, sockets, targets u otros mecanismos.

## 28. Un servicio puede estar active (exited)

No todos los servicios activos tienen un proceso principal ejecutándose continuamente.

Puedes encontrar:

```text
active (running)
active (exited)
```

Una unidad `oneshot`, por ejemplo, puede ejecutar una tarea y permanecer considerada activa según su configuración.

Por eso:

> active no equivale siempre a “hay un daemon corriendo”.

## 29. Estado failed

Para consultar unidades fallidas:

```bash
systemctl --failed
```

Que una unidad aparezca como failed no implica automáticamente que debas:

```text
restart
reset-failed
reinstall
disable
```

Primero debes investigar el motivo.

El Módulo 18 enseñará `journalctl` para logs.

## 30. systemctl --user

systemd también puede gestionar unidades a nivel del usuario:

```bash
systemctl --user
```

Estas unidades no son lo mismo que los servicios del gestor de sistema.

Consulta:

```bash
systemctl --user list-units --type=service
```

En algunos entornos sin una sesión de usuario systemd completa puede no funcionar.

No es un error universal del sistema.

## 31. Práctica A — identificar PID 1

Ejecuta:

```bash
ps -p 1 -o pid,comm,args
```

Pregunta:

> ¿el proceso 1 de tu entorno es systemd?

Si estás en un contenedor, WSL u otro entorno, el resultado puede ser diferente.

No intentes cambiar el init.

## 32. Práctica B — versión

Si systemd está disponible:

```bash
systemctl --version
```

Anota:

- versión;
- no todas las características.

No compares versiones de distintas distribuciones como si “más alto” significara automáticamente “mejor”.

## 33. Práctica C — servicios cargados

```bash
systemctl list-units --type=service
```

No pegues toda la lista.

Identifica para ti:

- una unidad active/running;
- una active/exited, si existe;
- una inactiva, si utilizas `--all`.

## 34. Práctica D — archivos de unidades

```bash
systemctl list-unit-files --type=service
```

Localiza ejemplos de:

```text
enabled
disabled
static
masked
```

Puede que no estén presentes todos.

No cambies sus estados.

## 35. Práctica E — consultar una unidad conocida

Elige una unidad que **ya aparezca** en tu listado.

No inventes el nombre.

Después:

```bash
systemctl status NOMBRE.service
```

y:

```bash
systemctl show -p ActiveState -p SubState -p FragmentPath NOMBRE.service
```

Solo lectura.

## 36. Práctica F — definición de la unidad

Sobre la misma unidad:

```bash
systemctl cat NOMBRE.service
```

Identifica:

- nombre;
- secciones como `[Unit]`, `[Service]` o `[Install]` si existen;
- ruta del fragmento.

No edites el archivo.

## 37. Práctica G — target predeterminado

```bash
systemctl get-default
```

Explica con tus palabras qué target aparece.

No uses `set-default`.

## 38. Práctica H — timers

```bash
systemctl list-timers
```

Observa:

- próxima ejecución;
- última ejecución;
- timer;
- unidad activada.

No crees ni modifiques timers todavía.

## 39. start, stop, enable y disable: clasificación

Clasifica sin ejecutar:

```text
systemctl start demo.service
systemctl stop demo.service
systemctl enable demo.service
systemctl disable demo.service
systemctl status demo.service
systemctl is-active demo.service
systemctl is-enabled demo.service
```

Debes separar:

```text
consultas
cambios de estado actual
cambios de habilitación
```

## 40. No uses sudo systemctl por reflejo

Algunas operaciones de sistema requieren privilegios y mecanismos de autorización.

Pero:

```text
Permission denied
```

o una solicitud de autenticación no significa que debas elevar privilegios sin analizar el cambio.

Primero pregunta:

- ¿qué unidad es?;
- ¿qué hace?;
- ¿quién depende de ella?;
- ¿se perderán conexiones?;
- ¿afectará el arranque?;
- ¿tengo autorización?.

## 41. Otros sistemas init

systemd no es el único sistema init existente.

Otros ejemplos:

```text
SysV init
OpenRC
runit
s6
```

También existen sistemas minimalistas o diseños propios en entornos embebidos y contenedores.

Este manual se centra en systemd porque es dominante en Debian, Ubuntu, Fedora y RHEL actuales, pero mantiene contexto de otros sistemas.

## 42. SysV init en contexto histórico y de compatibilidad

SysV init utilizaba tradicionalmente:

- scripts de inicio;
- runlevels;
- directorios como `/etc/init.d/`.

Muchas distribuciones modernas usan systemd, pero pueden conservar compatibilidad con algunos scripts SysV.

No enseñaremos SysV como mecanismo principal para administración nueva, pero sí debes reconocerlo cuando aparezca en sistemas heredados.

## 43. OpenRC

OpenRC es un sistema init y supervisor de servicios usado por algunas distribuciones, especialmente asociado a Gentoo y otras opciones.

Sus herramientas y conceptos no son iguales a `systemctl`.

No intentes traducir automáticamente:

```text
systemctl start
```

a una orden OpenRC sin consultar su documentación.

## 44. runit

runit utiliza un enfoque distinto basado en supervisión de servicios y directorios de servicio.

De nuevo:

> “Linux” no implica automáticamente “systemctl”.

Primero identifica el init real.

## 45. Contenedores y WSL

Dentro de un contenedor, PID 1 puede ser:

- la aplicación;
- un shell;
- un init mínimo;
- systemd si el contenedor fue diseñado para ello.

En WSL moderno, systemd puede estar habilitado según configuración y versión, pero no debes asumirlo sin verificar.

Por eso:

```bash
ps -p 1 -o comm=
```

es más fiable que asumir.

## 46. Errores frecuentes

| Error | Problema | Corrección |
|---|---|---|
| “systemd = servicio” | systemd gestiona muchos tipos de unidad | Distingue gestor y unidad |
| “unit = service” | Hay timers, sockets, targets, mounts, etc. | Mira la extensión |
| `start` = `enable` | Estado actual y habilitación son diferentes | Aprende cada acción |
| `stop` = `disable` | Detener ahora no cambia necesariamente el arranque | Separa conceptos |
| `reload` = `restart` | No son equivalentes | Revisa soporte del servicio |
| `daemon-reload` reinicia servicios | Recarga definición del gestor | No confundir con restart |
| `static` = roto | Puede activarse por dependencia | No intentes habilitarlo a ciegas |
| `disabled` = detenido | Puede estar activo aunque disabled | Consulta is-active |
| “Linux siempre usa systemd” | Existen otros init | Comprueba PID 1 |
| Reinicias servicios desconocidos | Puedes interrumpir funciones | Investiga antes |

## 47. Método seguro antes de controlar un servicio

Antes de cualquier cambio:

1. identifica distribución y entorno;
2. confirma que systemd sea el gestor relevante;
3. identifica la unidad exacta;
4. consulta `status`;
5. consulta `cat` o propiedades relevantes;
6. identifica dependencias;
7. entiende impacto de start/stop/restart;
8. determina si necesitas habilitación al arranque;
9. revisa logs si existe un fallo;
10. solo entonces realiza cambios con autorización.

## 48. Práctica independiente

Sin modificar servicios:

1. identifica PID 1;
2. consulta versión de systemd si aplica;
3. lista servicios cargados;
4. lista archivos de unidades de servicio;
5. elige una unidad existente y consulta su estado;
6. consulta ActiveState, SubState y FragmentPath;
7. muestra su definición con `systemctl cat`;
8. consulta el target predeterminado;
9. lista timers;
10. explica la diferencia entre start y enable.

No uses `sudo`, `start`, `stop`, `restart`, `enable`, `disable`, `mask` ni `unmask`.

## 49. Mini evaluación

1. ¿systemd puede actuar como PID 1?
   - A) Sí.
   - B) No.

2. ¿toda unidad systemd es un servicio?
   - A) Sí.
   - B) No.

3. ¿qué extensión identifica normalmente un servicio?
   - A) `.service`
   - B) `.txt`
   - C) `.deb`

4. ¿`systemctl start` equivale a `systemctl enable`?
   - A) Sí.
   - B) No.

5. ¿`systemctl stop` equivale a `systemctl disable`?
   - A) Sí.
   - B) No.

6. ¿`daemon-reload` significa reiniciar todos los servicios?
   - A) Sí.
   - B) No.

7. ¿una unidad static está necesariamente rota?
   - A) Sí.
   - B) No.

8. ¿un servicio disabled puede estar activo ahora?
   - A) Sí.
   - B) No.

9. ¿systemd es el único init posible en Linux?
   - A) Sí.
   - B) No.

10. Antes de reiniciar un servicio, ¿debes conocer su función e impacto?
   - A) Sí.
   - B) No.

## 50. Registro de aprendizaje

Puedes responder:

```text
Un sistema init sirve para:
systemd es:
Una unidad es:
.service significa:
start hace:
enable hace:
stop hace:
disable hace:
reload hace:
daemon-reload hace:
masked significa:
¿Por qué systemd no es el único init?:
Algo que todavía confundo:
Estado: EN APRENDIZAJE / PRACTICADO
```

## 51. Fuentes y límites

Fuentes principales verificadas:

- systemd / systemctl manual:
  https://www.freedesktop.org/software/systemd/man/latest/systemctl.html
- systemd unit manual:
  https://www.freedesktop.org/software/systemd/man/latest/systemd.unit.html
- Debian systemd documentation:
  https://wiki.debian.org/systemd/documentation
- Debian systemd overview:
  https://wiki.debian.org/systemd/
- RHEL 10 — Managing system services with systemctl:
  https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_systemd_unit_files_to_customize_and_optimize_your_system/managing-system-services-with-systemctl

Se posponen:

- edición de unit files;
- overrides con `systemctl edit`;
- creación de servicios propios;
- `daemon-reload` práctico;
- start/stop/restart reales;
- enable/disable/mask/unmask reales;
- dependencias avanzadas;
- journald;
- timers prácticos;
- resource control;
- cgroups;
- boot troubleshooting.

**Estado de la lección:** redactada y revisada documentalmente. Las prácticas son de consulta; no cambian servicios ni configuración.

Siguiente módulo por redactar: **Módulo 18 — Logs y diagnóstico inicial con journalctl**.
