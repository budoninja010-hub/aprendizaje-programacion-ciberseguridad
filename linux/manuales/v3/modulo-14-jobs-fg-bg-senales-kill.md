# Módulo 14 — jobs, fg, bg, señales y kill

Manual Maestro de Linux y Shell Scripting — Edición 2026 · v3 · Decimocuarta entrega.

[Índice del manual](README.md) · [← Módulo 13](modulo-13-procesos-ps-top-htop.md) · [Arquitectura](00-indice-arquitectura.md) · [Módulo 15 →](modulo-15-paquetes-repositorios-actualizaciones.md)

## 1. Qué aprenderás

Al terminar este módulo podrás:

- explicar qué es un trabajo (*job*) de la shell;
- distinguir foreground y background;
- usar `jobs` para consultar trabajos de la shell actual;
- suspender temporalmente un trabajo de laboratorio con `Ctrl+Z`;
- reanudarlo con `bg` o devolverlo al primer plano con `fg`;
- distinguir número de job de PID;
- explicar qué es una señal;
- usar `kill -TERM` sobre un proceso propio creado expresamente para la práctica;
- comprobar si el proceso terminó;
- explicar por qué SIGKILL no debe ser la primera opción.

Conocimientos previos:
- procesos, PID y PPID;
- `ps`;
- terminal y Bash;
- señales de interrupción vistas con `Ctrl+C`.

**Seguridad:** solo controlaremos procesos creados por nosotros, como `sleep`. No enviaremos señales a procesos del sistema, servicios, procesos de otros usuarios ni aplicaciones con trabajo no guardado. No usaremos `sudo`. No practicaremos `kill -9`.

## 2. Foreground y background

Un proceso en **foreground** está asociado al primer plano de la terminal y normalmente recibe la interacción del teclado.

Ejemplo:

```bash
sleep 120
```

Mientras está en primer plano, esa shell queda esperando a que `sleep` termine o sea interrumpido.

Un proceso en **background** puede seguir ejecutándose mientras la shell vuelve a aceptar órdenes.

Modelo:

```text
foreground → ocupa el primer plano de la shell
background → continúa mientras recuperas el prompt
```

## 3. El símbolo &

En Bash puedes iniciar un comando en background agregando:

```text
&
```

Ejemplo:

```bash
sleep 120 &
```

La shell suele mostrar algo parecido a:

```text
[1] 4321
```

Esto ilustra dos identificadores distintos:

- `[1]` = número de job de esa shell;
- `4321` = PID del proceso, ejemplo ilustrativo.

No memorices esos números.

## 4. Job no es lo mismo que proceso

Un **job** es la forma en que una shell interactiva agrupa y controla una pipeline o comando lanzado desde esa shell.

Un job puede estar asociado a uno o varios procesos.

Por eso:

```text
job number ≠ PID
```

Ejemplo:

```text
%1     → job 1 de la shell
4321   → PID
```

No intercambies uno por otro sin saber qué herramienta espera cada forma.

## 5. jobs — trabajos de la shell actual

Ejecuta:

```bash
jobs
```

Puede mostrar trabajos:

- ejecutándose;
- detenidos;
- terminados recientemente.

`jobs` se refiere a la shell interactiva actual. No es un listado global de todos los procesos del sistema.

## 6. Suspender con Ctrl+Z

Si tienes en foreground:

```bash
sleep 120
```

puedes pulsar:

```text
Ctrl+Z
```

El **controlador de terminal** envía **SIGTSTP** al grupo de procesos en primer plano cuando pulsas `Ctrl+Z`; después, la shell recupera el prompt. **SIGTSTP** puede gestionarse por el programa, a diferencia de **SIGSTOP**, que no puede capturarse ni ignorarse.

Después:

```bash
jobs
```

puede mostrar el trabajo como detenido.

**Importante:** suspender no es lo mismo que terminar. El proceso sigue existiendo, pero está detenido.

## 7. bg — continuar en background

Si el trabajo suspendido es el job actual, puedes ejecutar:

```bash
bg
```

o de forma explícita:

```bash
bg %1
```

si el trabajo es `%1`.

Esto reanuda el trabajo en background.

Después:

```bash
jobs
```

debería mostrarlo como ejecutándose.

## 8. fg — traer al foreground

Para devolver un trabajo al primer plano:

```bash
fg %1
```

La shell vuelve a asociarlo al foreground.

Si `sleep` sigue esperando, la terminal quedará ocupada por ese trabajo hasta que:

- termine;
- lo suspendas;
- lo interrumpas de forma normal.

## 9. Ctrl+C y SIGINT

En una terminal interactiva, `Ctrl+C` normalmente provoca que el terminal entregue una señal de interrupción al grupo de procesos en foreground.

La señal suele ser:

```text
SIGINT
```

No todos los programas reaccionan exactamente igual: una aplicación puede manejar o ignorar ciertas señales.

Para nuestro `sleep` de práctica, `Ctrl+C` normalmente lo termina.

## 10. Qué es una señal

Una **señal** es un mecanismo mediante el cual el sistema puede notificar a un proceso sobre un evento.

Ejemplos comunes:

```text
SIGINT  → interrupción
SIGTERM → solicitud de terminación
SIGKILL → terminación forzada por el kernel
SIGSTOP → detener (no se puede capturar ni ignorar)
SIGTSTP → suspensión desde el teclado (Ctrl+Z)
SIGCONT → continuar
```

No necesitas memorizar todos los números de señal.

En este manual preferimos los nombres, porque son más claros.

## 11. SIGTERM — primera opción para terminar

Cuando necesitas solicitar a un proceso propio que termine, la primera señal que estudiaremos es:

```text
SIGTERM
```

Ejemplo:

```bash
kill -TERM PID
```

Sustituye `PID` por el PID real de un proceso **creado por ti para la práctica**.

SIGTERM permite que un programa tenga oportunidad de realizar limpieza si está preparado para manejarla.

Por eso se prefiere antes que una terminación forzada.

## 12. kill no significa siempre “matar”

El nombre `kill` puede confundir.

La utilidad envía una señal.

Ejemplo:

```bash
kill -TERM 4321
```

significa:

> enviar SIGTERM al proceso con PID 4321.

La señal predeterminada de muchas implementaciones de `kill` es TERM, pero en este manual la escribimos explícitamente al aprender.

## 13. Verificar antes de enviar una señal

Antes de ejecutar:

```bash
kill -TERM PID
```

haz tres comprobaciones:

1. confirma el PID;
2. confirma el usuario;
3. confirma el comando.

Ejemplo:

```bash
ps -o pid,user,stat,comm -p PID
```

Solo después decide si es el proceso de laboratorio correcto.

## 14. Comprobar después

Después de SIGTERM:

```bash
ps -p PID
```

Si el proceso terminó, normalmente ya no aparecerá como proceso activo en esa consulta.

No envíes señales repetidamente sin comprobar el resultado.

## 15. SIGKILL — último recurso

SIGKILL fuerza la terminación y el proceso no puede capturarla ni ejecutar su manejo normal de esa señal.

Eso significa que puede perder la oportunidad de:

- guardar estado;
- cerrar archivos de forma ordenada;
- liberar recursos de aplicación;
- retirar archivos temporales propios.

Por eso:

> SIGKILL no es la primera opción.

En este módulo **no practicamos**:

```text
kill -9
kill -KILL
```

Solo debes reconocer que existe para situaciones donde una terminación normal no funciona y el contexto justifica una acción forzada.

## 16. Por qué kill -9 no es “más profesional”

Usar `kill -9` inmediatamente no demuestra mayor dominio.

El enfoque correcto es:

1. identificar el proceso;
2. entender su función;
3. solicitar terminación normal;
4. esperar y comprobar;
5. escalar solo si existe una razón técnica.

La fuerza sin diagnóstico aumenta el riesgo de pérdida de trabajo o estado inconsistente.

## 17. SIGSTOP y SIGCONT

Conceptualmente:

```text
SIGSTOP → detener
SIGCONT → continuar
```

El control de jobs de la shell utiliza mecanismos relacionados para suspender y continuar trabajos.

No enviaremos manualmente estas señales en la práctica inicial porque `Ctrl+Z`, `bg` y `fg` permiten comprender el flujo con menos complejidad.

## 18. Jobspec con %

Bash permite referirse a jobs mediante sintaxis como:

```text
%1
%2
```

Ejemplo:

```bash
fg %1
```

Esto no significa “PID 1”.

El símbolo `%` indica que estás usando una referencia de job para la shell.

## 19. jobs -l

Puedes solicitar que `jobs` muestre PID además de información del job:

```bash
jobs -l
```

Esto ayuda a relacionar:

- número de job;
- PID;
- estado;
- comando.

Aun así, recuerda que una pipeline puede implicar más de un proceso.

## 20. Un job puede ser una pipeline

Ejemplo conceptual:

```bash
comandoA | comandoB &
```

Eso es una pipeline lanzada como job en background.

Puede involucrar más de un proceso.

No practicaremos señales sobre pipelines en este módulo. Trabajaremos con un único `sleep`.

## 21. Preparar el laboratorio

Entra:

```bash
cd ~/linux-lab
pwd
```

Comprueba:

```bash
ls -ld ./modulo-14-jobs-senales
```

Si no existe:

```bash
mkdir modulo-14-jobs-senales
```

Después:

```bash
cd ./modulo-14-jobs-senales
pwd
```

No necesitas crear archivos para esta práctica.

## 22. Práctica A — job en background

Ejecuta:

```bash
sleep 120 &
```

Observa la línea que devuelve la shell.

Después:

```bash
jobs -l
```

Identifica:

- job number;
- PID;
- estado;
- comando.

No envíes ninguna señal todavía.

## 23. Práctica B — foreground

Si tu job es `%1`:

```bash
fg %1
```

Ahora `sleep` está en foreground.

Pulsa:

```text
Ctrl+Z
```

Después:

```bash
jobs
```

Debe aparecer detenido si la suspensión funcionó.

## 24. Práctica C — bg

Reanuda:

```bash
bg %1
```

Después:

```bash
jobs -l
```

Comprueba que vuelva a estar ejecutándose en background.

## 25. Práctica D — terminar normalmente desde foreground

Trae el trabajo:

```bash
fg %1
```

Y pulsa:

```text
Ctrl+C
```

Después:

```bash
jobs
```

El trabajo debería haber terminado y puede desaparecer o mostrarse temporalmente como terminado según la shell.

Esta práctica usa la interrupción normal del foreground, no `kill`.

## 26. Práctica E — SIGTERM con PID

Crea un nuevo proceso:

```bash
sleep 180 &
```

Consulta:

```bash
jobs -l
```

Copia **solo el PID de ese sleep de práctica**.

Verifica:

```bash
ps -o pid,user,stat,comm -p PID
```

Sustituye `PID` por el número real.

Si confirma que es tu proceso `sleep`:

```bash
kill -TERM PID
```

Comprueba:

```bash
ps -p PID
jobs
```

No envíes otra señal si ya terminó.

## 27. No practiques con servicios del sistema

No uses como objetivo:

- PID 1;
- gestores de sesión;
- procesos de red;
- procesos gráficos;
- servicios;
- procesos de otros usuarios;
- procesos cuyo propósito desconozcas.

El objetivo pedagógico es aprender señales, no provocar fallos.

## 28. pkill y killall — existen, pero se posponen

Herramientas como:

```text
pkill
killall
```

pueden seleccionar procesos por nombre u otros criterios.

Eso amplía el alcance y puede coincidir con más procesos de lo previsto.

Por ahora no las usamos.

Primero debes dominar:

- PID;
- verificación;
- SIGTERM;
- comprobación posterior.

## 29. Señal no garantiza una acción idéntica

SIGTERM es una solicitud de terminación, pero un programa puede:

- capturarla;
- realizar limpieza;
- retrasar su salida;
- ignorarla en ciertos diseños o condiciones.

SIGKILL, en cambio, no puede ser capturada o ignorada por el proceso.

Esta diferencia es precisamente la razón para intentar TERM primero.

## 30. Procesos detenidos y recursos

Un proceso suspendido deja de ejecutar instrucciones de usuario mientras permanece detenido, pero sigue existiendo y puede conservar:

- memoria;
- archivos abiertos;
- otros recursos.

No confundas “detenido” con “eliminado”.

## 31. Salir de una terminal con jobs activos

Cerrar una shell con trabajos activos puede producir comportamientos que dependen de:

- shell;
- configuración;
- señales;
- job control;
- cómo se lanzó el proceso.

No estudiaremos todavía `nohup`, `disown`, terminal multiplexers ni servicios persistentes.

Para esta práctica termina tus procesos `sleep` de laboratorio antes de cerrar.

## 32. Errores frecuentes

| Error | Problema | Corrección |
|---|---|---|
| Confundes `%1` con PID 1 | Job y PID son espacios distintos | `%1` es jobspec de la shell |
| `Ctrl+Z` “terminó” el programa | En realidad lo suspendiste | Consulta `jobs` |
| Usas `bg` esperando verlo en foreground | `bg` reanuda en segundo plano | Usa `fg` para traerlo |
| Ejecutas `kill -9` primero | Fuerzas salida sin oportunidad de limpieza | Usa TERM primero |
| Envías señal sin verificar PID | PID puede ser otro proceso | Usa `ps -p PID` |
| Usas `sudo kill` | Amplías privilegios innecesariamente | Practica solo con procesos propios |
| Usas `pkill` por comodidad | Puede coincidir con más procesos | Selecciona un PID verificado |
| Crees que un job detenido no consume recursos | Sigue existiendo | Reanúdalo o termínalo correctamente |

## 33. Método seguro para terminar un proceso propio

Usa esta secuencia mental:

1. identificar;
2. verificar;
3. solicitar terminación normal;
4. esperar;
5. comprobar;
6. solo escalar con una razón técnica.

Para nuestro laboratorio:

```text
jobs -l
↓
ps -p PID
↓
kill -TERM PID
↓
ps -p PID
```

## 34. Práctica independiente

Solo con procesos `sleep` creados por ti:

1. inicia uno en background;
2. consulta su job y PID;
3. tráelo a foreground;
4. suspéndelo;
5. consulta su estado;
6. reanúdalo en background;
7. verifica su PID con `ps`;
8. termínalo con SIGTERM;
9. confirma que terminó;
10. explica por qué no usaste SIGKILL.

No uses `sudo`, `pkill`, `killall` ni `kill -9`.

## 35. Mini evaluación

1. ¿Qué muestra `jobs`?
   - A) Trabajos de la shell actual.
   - B) Todos los archivos.
   - C) Usuarios.

2. ¿Qué hace `Ctrl+Z` normalmente sobre el job en foreground?
   - A) Lo suspende.
   - B) Lo borra.
   - C) Reinicia Linux.

3. ¿Qué hace `bg`?
   - A) Reanuda un job en background.
   - B) Borra un grupo.
   - C) Cambia permisos.

4. ¿Qué hace `fg`?
   - A) Lleva un job al foreground.
   - B) Finaliza obligatoriamente el proceso.
   - C) Cambia el GID.

5. ¿`%1` es necesariamente PID 1?
   - A) Sí.
   - B) No.

6. ¿Qué señal debemos intentar primero para una terminación normal?
   - A) SIGTERM.
   - B) SIGKILL.

7. ¿Practicamos `kill -9` como rutina?
   - A) Sí.
   - B) No.

8. ¿Debes verificar PID y comando antes de enviar una señal?
   - A) Sí.
   - B) No.

9. ¿Un proceso suspendido deja de existir?
   - A) Sí.
   - B) No.

## 36. Registro de aprendizaje

Puedes responder:

```text
Un job es:
Foreground significa:
Background significa:
jobs sirve para:
Ctrl+Z hace:
bg sirve para:
fg sirve para:
SIGTERM sirve para:
SIGKILL se reserva para:
¿Por qué verifico el PID antes de kill?:
Algo que todavía confundo:
Estado: EN APRENDIZAJE / PRACTICADO
```

## 37. Fuentes y límites

Fuentes principales:

- GNU Bash Reference Manual — Job Control:
  https://www.gnu.org/software/bash/manual/html_node/Job-Control.html
- GNU Bash Reference Manual — Job Control Builtins:
  https://www.gnu.org/software/bash/manual/html_node/Job-Control-Builtins.html
- Linux man-pages — `kill(2)`:
  https://man7.org/linux/man-pages/man2/kill.2.html
- Linux man-pages — `signal(7)`:
  https://man7.org/linux/man-pages/man7/signal.7.html
- Linux man-pages — `kill(1)`:
  https://man7.org/linux/man-pages/man1/kill.1.html

Se posponen:

- `pkill` y `killall` prácticos;
- signal masks;
- signal handlers en programación;
- `nohup`;
- `disown`;
- SIGHUP;
- terminal multiplexers;
- procesos daemon;
- prioridades con nice/renice;
- systemd y servicios.

**Estado de la lección:** redactada y revisada documentalmente. La práctica real del estudiante sigue pendiente.

---

**Siguiente:** [Módulo 15 — Paquetes, repositorios y actualizaciones](modulo-15-paquetes-repositorios-actualizaciones.md) · [Volver al índice](README.md)
