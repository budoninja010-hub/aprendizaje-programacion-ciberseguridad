# Módulo 13 — Procesos: ps, top y htop opcional

Manual Maestro de Linux y Shell Scripting — Edición 2026 · v3 · Decimotercera entrega.

[Índice del manual](README.md) · [← Módulo 12](modulo-12-permisos-chmod-chown-umask-sudo-acl.md) · [Arquitectura](00-indice-arquitectura.md) · [Módulo 14 →](modulo-14-jobs-fg-bg-senales-kill.md)

## 1. Qué aprenderás

Al terminar este módulo podrás:

- explicar qué es un proceso;
- distinguir programa de proceso;
- reconocer PID y PPID;
- consultar procesos con `ps`;
- seleccionar columnas útiles con `ps -o`;
- interpretar de forma inicial usuario, estado, CPU, memoria y comando;
- usar `top` para observar procesos en tiempo real;
- salir correctamente de `top`;
- reconocer `htop` como herramienta opcional, sin instalarla si no está disponible;
- diferenciar observar procesos de administrarlos o terminarlos.

Conocimientos previos:
- usuarios e identidad;
- permisos básicos;
- lectura de comandos y salidas;
- tuberías y búsqueda.

**Seguridad:** este módulo es de observación. No terminaremos procesos, no cambiaremos prioridades y no usaremos `sudo`. Los comandos `kill`, `pkill`, `killall`, `renice` y señales se reservan para el Módulo 14.

## 2. Programa y proceso no son lo mismo

Un **programa** es código almacenado que puede ejecutarse.

Un **proceso** es una instancia de un programa que está ejecutándose y tiene estado asociado por el sistema.

Ejemplo conceptual:

```text
programa: /usr/bin/bash
proceso: una ejecución concreta de Bash
```

Puedes tener varias instancias del mismo programa ejecutándose al mismo tiempo; cada una será un proceso distinto.

## 3. PID — identificador de proceso

Cada proceso tiene un identificador numérico llamado:

```text
PID
```

PID significa **Process ID**.

Ejemplo ilustrativo:

```text
PID 4231
```

Ese número no es permanente. Puede cambiar entre ejecuciones y reutilizarse después de que un proceso termine.

**Regla:** nunca memorices un PID como si identificara para siempre a una aplicación.

## 4. PPID — proceso padre

Muchos procesos se crean a partir de otro proceso.

El identificador del proceso padre se denomina:

```text
PPID
```

Ejemplo conceptual:

```text
terminal
  └─ shell
      └─ ps
```

Cuando ejecutas `ps` desde una shell, el proceso de `ps` normalmente tiene como padre a la shell que lo inició.

No necesitas estudiar todavía `fork()`, `exec()` ni creación de procesos a nivel de programación.

## 5. El usuario de un proceso

Cada proceso ejecuta con identidades asociadas.

Esto importa porque los permisos y decisiones de acceso dependen de la identidad con la que actúa.

En una salida de procesos puedes encontrar una columna como:

```text
USER
```

No asumas que todos los procesos pertenecen a tu cuenta. Los servicios del sistema suelen usar otras identidades.

## 6. ps — fotografía de procesos

`ps` muestra información sobre procesos.

Ejecuta:

```bash
ps
```

La salida habitual, sin opciones, suele limitarse a procesos asociados a la terminal/sesión según la implementación y entorno.

Una salida ilustrativa:

```text
PID TTY          TIME CMD
1234 pts/0    00:00:00 bash
5678 pts/0    00:00:00 ps
```

No copies esos números como si fueran los de tu sistema.

Referencia principal: `ps(1)` de procps-ng.

## 7. Columnas básicas de ps

En una salida sencilla puedes ver:

- `PID`: identificador del proceso;
- `TTY`: terminal asociada, cuando existe;
- `TIME`: tiempo de CPU acumulado según el formato mostrado;
- `CMD` o `COMMAND`: nombre o comando asociado.

La selección exacta de columnas depende de las opciones y del estilo usado.

## 8. ps -f — formato más completo

Ejecuta:

```bash
ps -f
```

Puede añadir columnas como:

- UID o usuario;
- PID;
- PPID;
- hora de inicio;
- comando.

El objetivo no es memorizar cada encabezado hoy, sino reconocer PID y PPID.

## 9. Elegir columnas con ps -o

Una forma clara de aprender es pedir exactamente las columnas que quieres:

```bash
ps -o pid,ppid,user,stat,comm
```

Esto solicita:

- `pid`: PID;
- `ppid`: PPID;
- `user`: usuario;
- `stat`: estado resumido;
- `comm`: nombre del ejecutable/comando.

Esta forma evita depender de una salida predeterminada diferente entre opciones.

## 10. Estado de un proceso

Una columna como `STAT` resume el estado y posibles indicadores adicionales.

Estados comunes pueden incluir letras como:

```text
R = running/runnable
S = sleeping interrumpible
D = espera no interrumpible
T = detenido o trazado
Z = zombie
```

No memorices todavía todos los modificadores.

**Importante:** “sleeping” no significa necesariamente un problema. Muchos procesos esperan eventos la mayor parte del tiempo.

## 11. Qué es un proceso zombie

Un proceso en estado `Z` es un proceso que ya terminó, pero cuya información de terminación todavía no ha sido recogida por su padre.

No significa que esté “ejecutándose muerto” ni que debas intentar eliminarlo con comandos al azar.

Este tema se retomará con señales y procesos padre.

Por ahora solo reconoce la letra `Z` si aparece.

## 12. ps -e — más procesos

```bash
ps -e
```

solicita una vista de todos los procesos accesibles en ese contexto, no solo los asociados a tu terminal.

Puede producir bastante salida.

Puedes combinar una selección de columnas:

```bash
ps -e -o pid,ppid,user,stat,comm
```

No necesitas usar `sudo` para esta práctica.

## 13. ps aux — estilo BSD, útil pero diferente

También verás frecuentemente:

```bash
ps aux
```

Es una sintaxis muy extendida que usa opciones de estilo BSD sin guion para esas letras.

Puede mostrar columnas como:

- USER;
- PID;
- %CPU;
- %MEM;
- VSZ;
- RSS;
- STAT;
- START;
- COMMAND.

No mezcles opciones de distintos estilos sin saber qué significan. Para aprender de forma gradual, este manual prioriza `ps -o` cuando queremos columnas concretas.

## 14. CPU y memoria: no confundir métricas

En listados de procesos puedes encontrar:

```text
%CPU
%MEM
VSZ
RSS
```

Interpretación inicial:

- `%CPU`: uso de CPU según el cálculo de la herramienta;
- `%MEM`: proporción de memoria física según el cálculo mostrado;
- `VSZ`: tamaño del espacio de memoria virtual del proceso;
- `RSS`: memoria residente aproximada en RAM.

No interpretes VSZ como “RAM realmente consumida” sin contexto.

La memoria de procesos incluye conceptos compartidos, virtuales y residentes que se estudiarán más adelante.

## 15. Filtrar ps con grep: cuidado con la coincidencia

Un ejemplo educativo:

```bash
ps -e -o pid,user,comm | grep 'bash'
```

Puede mostrar procesos cuyo texto coincida con `bash`.

Pero `grep` también puede aparecer en ciertos patrones de búsqueda, y buscar texto no es igual que consultar procesos de forma estructurada.

En módulos posteriores conocerás herramientas como `pgrep`.

Por ahora usa `grep` solo para practicar lectura, no para automatizar decisiones sobre procesos.

## 16. top — vista dinámica

`top` muestra una vista interactiva que se actualiza periódicamente.

Ejecuta:

```bash
top
```

Puedes observar:

- carga del sistema;
- número de tareas/procesos;
- CPU;
- memoria;
- tabla de procesos.

Para salir:

```text
q
```

No cierres la terminal por la fuerza para salir.

## 17. top no modifica procesos solo por abrirlo

Abrir `top` para observar no cambia automáticamente procesos.

Sin embargo, `top` también posee funciones interactivas capaces de enviar señales o cambiar prioridades.

**En este módulo no usamos esas funciones.**

Solo observamos y salimos con `q`.

## 18. Interpretar la zona superior de top

La cabecera de `top` puede mostrar información como:

- tiempo de actividad;
- carga promedio;
- número de tareas;
- distribución de CPU;
- memoria.

El formato y etiquetas pueden variar entre versiones.

### Qué significa `load average`

En Linux, los tres valores de carga promedio representan promedios de **1, 5 y 15 minutos**.

La documentación de `/proc/loadavg` los describe a partir del número de tareas que están:

- en estado `R`: ejecutándose o listas para ejecutarse;
- en estado `D`: espera no interrumpible, normalmente asociada a I/O.

Ejemplo conceptual:

```text
load average: 0.40, 0.25, 0.20
              └─1m   └─5m   └─15m
```

Esto **no es un porcentaje de CPU**.

```text
load average ≠ %CPU
```

Un valor de carga tampoco puede interpretarse correctamente sin contexto. Debes considerar, entre otras cosas:

- cuántas CPU lógicas tiene el sistema;
- cuánto tiempo dura la carga;
- si existen tareas en espera no interrumpible;
- uso de memoria;
- I/O;
- contexto de la aplicación.

Por ejemplo, una carga de `4.0` no significa automáticamente «400 % de CPU» ni demuestra por sí sola que exista un problema.

También evita una simplificación opuesta:

> «load average solo cuenta procesos usando CPU».

En Linux puede incluir tareas en estado `D`, por lo que una carga elevada puede estar relacionada con espera de I/O y no únicamente con trabajo activo de CPU.

No conviertas un solo número alto observado durante un instante en un diagnóstico.

El diagnóstico de rendimiento en profundidad queda fuera de esta introducción.

## 19. Ordenar en top

`top` suele permitir ordenar procesos por diferentes métricas mediante teclas interactivas.

No necesitamos memorizar todas.

Para esta lección:

1. abre `top`;
2. observa columnas;
3. identifica PID, usuario, CPU, memoria y comando;
4. pulsa `q`.

Más adelante aprenderás navegación avanzada.

## 20. htop — herramienta opcional

`htop` es un visor interactivo de procesos con una interfaz diferente.

Comprueba si existe:

```bash
command -v htop
```

Si muestra una ruta, puedes ejecutarlo:

```bash
htop
```

Normalmente puedes salir con:

```text
q
```

o la tecla indicada por su interfaz.

Si no está instalado, **no instales nada solo para completar este módulo**.

`htop` es opcional; `ps` y `top` son suficientes para los objetivos básicos.

## 21. /proc y los procesos

En el Módulo 5 aprendiste que `/proc` expone información del kernel y procesos.

Muchos directorios numéricos bajo `/proc` corresponden a PID existentes.

Ejemplo conceptual:

```text
/proc/1234/
```

No abras archivos sensibles de procesos ajenos ni recorras `/proc` sin necesidad.

Las herramientas `ps` y `top` presentan información de forma más adecuada para esta etapa.

## 22. Un proceso puede terminar entre dos consultas

Si ejecutas:

```bash
ps -e
```

y unos segundos después repites la orden, la lista puede cambiar.

Esto es normal:

- procesos terminan;
- procesos nuevos aparecen;
- PID se asignan y eventualmente se reutilizan.

Por eso una “fotografía” de procesos envejece rápidamente.

## 23. Preparar la práctica

En este módulo no necesitas crear archivos, pero puedes conservar notas dentro de:

```text
~/linux-lab/modulo-13-procesos
```

Comprueba primero:

```bash
cd ~/linux-lab
pwd
ls -ld ./modulo-13-procesos
```

Si no existe:

```bash
mkdir modulo-13-procesos
```

Después:

```bash
cd ./modulo-13-procesos
pwd
```

No guardes automáticamente listados completos de procesos en GitHub porque pueden contener nombres de usuario, rutas o comandos privados.

## 24. Práctica A — ps básico

Ejecuta:

```bash
ps
```

Identifica:

- el proceso de tu shell, si aparece;
- el propio proceso de `ps`;
- sus PID.

No memorices los PID.

## 25. Práctica B — PID y PPID

Ejecuta:

```bash
ps -o pid,ppid,user,stat,comm
```

Busca la fila de tu shell y la de `ps`.

Pregunta:

> ¿Qué relación observas entre el PPID de `ps` y el PID de la shell desde la que lo ejecutaste?

En una situación normal, el padre de `ps` será la shell que lo lanzó.

## 26. Práctica C — lista amplia

Ejecuta:

```bash
ps -e -o pid,ppid,user,stat,comm
```

No pegues toda la salida en el chat.

Observa:

- procesos de distintos usuarios;
- variedad de estados;
- nombres de comandos.

Si aparecen procesos que no reconoces, no los termines.

## 27. Práctica D — buscar Bash

Ejecuta:

```bash
ps -e -o pid,user,comm | grep 'bash'
```

Interpreta el resultado.

Si no aparece nada, no significa necesariamente que el sistema esté mal: tu shell puede ser otra o el nombre mostrado puede variar según entorno.

Consulta tu shell actual según lo aprendido en módulos anteriores si necesitas contexto.

## 28. Práctica E — top

Ejecuta:

```bash
top
```

Observa durante unos segundos:

- PID;
- USER;
- %CPU;
- %MEM;
- COMMAND.

Después sal con:

```text
q
```

No envíes señales ni cambies prioridades desde `top`.

## 29. Práctica F — htop opcional

```bash
command -v htop
```

Si existe:

```bash
htop
```

Solo observa y sal.

Si no existe:

```text
htop no disponible; práctica omitida
```

Eso es suficiente.

## 30. Práctica G — observar un proceso temporal de forma segura

Abre una primera terminal y ejecuta:

```bash
sleep 60
```

`sleep` espera durante aproximadamente 60 segundos.

Mientras sigue ejecutándose, abre una segunda terminal y usa:

```bash
ps -e -o pid,ppid,user,stat,comm | grep 'sleep'
```

Observa el proceso.

Cuando termine el tiempo desaparecerá por sí mismo.

Si quieres terminar la espera antes, vuelve a la primera terminal y pulsa:

```text
Ctrl+C
```

No uses `kill` todavía; se estudiará en el Módulo 14.

## 31. Qué significa “sleeping”

Mientras `sleep 60` espera, puede aparecer en un estado de espera como `S`.

Eso no significa que el proceso esté dañado.

Un proceso puede estar esperando:

- tiempo;
- entrada;
- red;
- disco;
- eventos.

El estado debe interpretarse según el propósito del proceso.

## 32. No terminar procesos desconocidos

Si ves un proceso con mucho CPU o memoria:

**no lo termines solo por ese dato**.

Primero se necesita:

- identificar qué es;
- confirmar quién lo inició;
- entender su función;
- comprobar si el valor es sostenido;
- saber el impacto de detenerlo.

El Módulo 14 enseñará señales con un proceso creado expresamente para laboratorio.

## 33. Errores frecuentes

| Error | Problema | Corrección |
|---|---|---|
| Confundes programa con proceso | Archivo ejecutable e instancia en ejecución no son lo mismo | Distingue código almacenado de ejecución |
| Memorizas un PID | Los PID cambian y pueden reutilizarse | Consulta el PID actual |
| Crees que `S` significa fallo | Muchos procesos esperan normalmente | Interpreta estado según contexto |
| Lees VSZ como RAM real exacta | Memoria virtual y residente son métricas distintas | Usa contexto; no simplifiques |
| Confundes load average con %CPU | Son métricas diferentes | Interpreta carga como tareas R/D promediadas en 1, 5 y 15 min |
| Crees que load average solo refleja CPU | También puede incluir tareas en espera no interrumpible | Considera I/O y estado D |
| Terminas procesos desconocidos | Puedes afectar servicios o datos | Solo observa en este módulo |
| Usas `sudo top` | Privilegios innecesarios | Ejecuta como usuario normal |
| Instalas `htop` solo por la práctica | Es opcional | Omite si no está disponible |
| Pegas todo `ps -e` en GitHub | Puede exponer datos del sistema | Comparte solo fragmentos revisados |

## 34. Método para analizar un proceso

Cuando encuentres un proceso:

1. anota su PID actual;
2. identifica USER;
3. identifica COMMAND/COMM;
4. observa STAT;
5. observa CPU y memoria solo como indicadores;
6. no actúes todavía;
7. busca contexto antes de tomar una decisión.

Diagnóstico antes que intervención.

## 35. Práctica independiente

Sin copiar exactamente los ejemplos:

1. muestra tus procesos asociados a la sesión;
2. pide columnas PID, PPID, usuario, estado y comando;
3. amplía la consulta a más procesos;
4. identifica al menos un proceso de tu usuario;
5. abre `top`, localiza PID y CPU y sal correctamente;
6. comprueba si `htop` está disponible;
7. explica por qué no debes terminar un proceso que no reconoces.

No uses `sudo`, `kill`, `pkill`, `killall` ni cambios de prioridad.

## 36. Mini evaluación

1. ¿Qué es un proceso?
   - A) Una instancia de un programa en ejecución.
   - B) Un directorio.
   - C) Un permiso.

2. ¿Qué significa PID?
   - A) Process ID.
   - B) Program Installation Directory.
   - C) Permission Identity Data.

3. ¿Qué significa PPID?
   - A) PID del proceso padre.
   - B) Permiso privado.
   - C) Puerto de red.

4. ¿`ps` muestra una fotografía del estado de procesos?
   - A) Sí.
   - B) No.

5. ¿`top` actualiza la vista periódicamente?
   - A) Sí.
   - B) No.

6. ¿Cómo sales de `top` en la práctica?
   - A) `q`
   - B) `rm`
   - C) `sudo`

7. ¿Debes instalar `htop` obligatoriamente?
   - A) Sí.
   - B) No.

8. ¿Debes terminar un proceso desconocido solo porque usa CPU?
   - A) Sí.
   - B) No.

9. ¿`load average` es lo mismo que porcentaje de CPU?
   - A) Sí.
   - B) No.

10. ¿los tres valores de load average representan aproximadamente 1, 5 y 15 minutos?
   - A) Sí.
   - B) No.

11. ¿en Linux la carga puede incluir tareas en estado `D` además de tareas `R`?
   - A) Sí.
   - B) No.

12. ¿VSZ equivale siempre a RAM física realmente ocupada?
   - A) Sí.
   - B) No.

## 37. Registro de aprendizaje

Puedes responder:

```text
Un proceso es:
PID significa:
PPID significa:
ps sirve para:
top sirve para:
load average significa:
Sus intervalos son:
¿Por qué no equivale a %CPU?:
htop es:
STAT representa:
Un estado S puede significar:
¿Por qué no debo terminar procesos desconocidos?:
Algo que todavía confundo:
Estado: EN APRENDIZAJE / PRACTICADO
```

No compartas listados completos de procesos si contienen nombres, rutas o comandos privados.

## 38. Fuentes y límites

Clasificación y estado de los enlaces de esta sección: [catálogo de fuentes](auditorias/06-catalogo-fuentes.md) (jerarquía E04, comprobación del 9 de octubre de 2026).

Fuentes principales:

- procps-ng / `ps(1)`:
  https://man7.org/linux/man-pages/man1/ps.1.html
- procps-ng upstream — `top(1)`:
  https://gitlab.com/procps-ng/procps/-/blob/master/man/top.1
- Linux man-pages project — `proc_loadavg(5)`, en el libro PDF de la edición 6.17 (el 9 de octubre de 2026 la edición más reciente publicada es la 6.19):
  https://www.kernel.org/pub/linux/docs/man-pages/book/man-pages-6.17.pdf
- Linux kernel documentation — `/proc` filesystem:
  https://docs.kernel.org/filesystems/proc.html
- Linux man-pages — `proc(5)`:
  https://man7.org/linux/man-pages/man5/proc.5.html
- htop:
  https://htop.dev/

Puntos verificados documentalmente:

- `top` muestra la carga media del sistema para 1, 5 y 15 minutos;
- `/proc/loadavg` define sus tres primeros campos a partir de tareas en cola de ejecución (estado `R`) o en espera no interrumpible de I/O (estado `D`) promediadas en 1, 5 y 15 minutos;
- `load average` no es un porcentaje de CPU;
- una carga elevada requiere contexto de CPU, duración, I/O, memoria y aplicación antes de diagnosticar un problema.

Se posponen:

- señales;
- `kill`, `pkill`, `killall`;
- jobs, `fg` y `bg`;
- prioridades, nice y renice;
- cgroups;
- namespaces;
- afinidad de CPU;
- diagnóstico profundo de memoria;
- procesos zombie y huérfanos en profundidad.

**Estado de la lección:** redactada y revisada documentalmente. La práctica real del estudiante sigue pendiente.

---

**Siguiente:** [Módulo 14 — jobs, fg, bg, señales y kill](modulo-14-jobs-fg-bg-senales-kill.md) · [Volver al índice](README.md)
