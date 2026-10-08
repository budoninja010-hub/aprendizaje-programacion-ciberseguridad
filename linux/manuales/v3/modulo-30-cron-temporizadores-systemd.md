# Módulo 30 — Automatización con `cron` y temporizadores de systemd

Manual Maestro de Linux y Shell Scripting — Edición 2026 · v3 · Trigésima entrega.

[Estado actual](README.md) · [Módulo anterior](modulo-29-manejo-errores-trap-mktemp-shellcheck.md) · [Arquitectura](00-indice-arquitectura.md)

## 1. Qué aprenderás

Al terminar este módulo podrás:

- explicar qué significa programar una tarea;
- distinguir ejecución manual de ejecución programada;
- aplicar la regla «probar primero, programar después»;
- reconocer `cron`, `crond` y `crontab`;
- leer los cinco campos temporales de una entrada de crontab;
- diferenciar el crontab de usuario de archivos de cron del sistema;
- reconocer diferencias de entorno entre tu terminal y cron;
- evitar comandos complejos directamente dentro del crontab;
- consultar tareas sin borrarlas accidentalmente;
- explicar qué ocurre con una ejecución perdida en cron;
- reconocer qué es una unidad `.timer` de systemd;
- entender la relación entre una unidad `.timer` y una `.service`;
- diferenciar `OnCalendar=` de temporizadores monotónicos como `OnActiveSec=`;
- usar `systemd-analyze calendar` para validar expresiones de calendario;
- explicar `Persistent=true`, `AccuracySec=` y `RandomizedDelaySec=` a nivel básico;
- consultar temporizadores con `systemctl list-timers`;
- crear una práctica de temporizador de usuario sin privilegios cuando el entorno lo soporte;
- documentar y retirar una automatización de prueba.

Conocimientos previos:

- scripts Bash;
- permisos de ejecución;
- rutas absolutas y relativas;
- variables de entorno;
- systemd y servicios;
- logs y `journalctl`;
- estados de salida y manejo de errores.

**Seguridad:** una tarea programada repite acciones sin que estés mirando. Por eso este módulo solo automatiza la escritura de una marca de tiempo dentro de `~/linux-lab/modulo-30-automatizacion`. No se automatizan borrados, actualizaciones del sistema, cambios de permisos, paquetes, usuarios, discos, red ni cortafuegos.

## 2. Qué es automatizar una tarea

Automatizar significa indicar que una acción se ejecute sin iniciarla manualmente cada vez.

Modelo:

```text
script probado manualmente
        ↓
programador de tareas
        ↓
momento o intervalo
        ↓
ejecución automática
```

## 3. Regla principal del módulo

> **Primero prueba la tarea manualmente. Después prográmala.**

Si un script falla cuando lo ejecutas tú, programarlo no corrige el problema; solo hace que falle automáticamente.

## 4. Qué es cron

`cron` es una familia tradicional de servicios para ejecutar órdenes de forma programada.

En sistemas que usan Cronie, el daemon suele llamarse:

```text
crond
```

y las tablas de tareas se administran con:

```text
crontab
```

No todas las distribuciones instalan o habilitan exactamente la misma implementación.

## 5. Comprobar qué existe

Consultas seguras:

```bash
command -v crontab
command -v systemctl
```

Si `crontab` no está disponible, no instales nada automáticamente solo para completar el ejercicio. Primero identifica la distribución y el paquete correspondiente.

## 6. Consultar tu crontab

```bash
crontab -l
```

`-l` lista las tareas del usuario actual.

Si no existe una tabla todavía, la implementación puede informar que no hay crontab.

Esta es una operación de consulta.

## 7. Editar el crontab del usuario

```bash
crontab -e
```

abre la tabla del usuario actual en un editor.

**Esto sí modifica configuración.** Después de guardar, las nuevas entradas pueden comenzar a ejecutarse según su horario.

Por eso no añadiremos una línea hasta haber probado manualmente el script.

## 8. No usar `crontab -r` como práctica

`crontab -r` elimina la tabla del usuario.

Este manual no lo usa para limpiar un ejercicio porque podría borrar tareas ajenas a la práctica.

Para retirar una tarea, vuelve a:

```bash
crontab -e
```

y elimina únicamente la línea que tú añadiste.

## 9. Los cinco campos de tiempo

Una entrada de crontab de usuario tiene, de forma simplificada:

```text
minuto hora día_del_mes mes día_de_la_semana comando
```

Ejemplo conceptual:

```text
30 18 * * * comando
```

significa ejecutar el comando a las 18:30 cada día.

## 10. Rangos básicos

En Cronie:

```text
minuto          0–59
hora            0–23
día del mes     1–31
mes             1–12
día semana      0–7
```

En día de semana, `0` y `7` representan domingo en esta implementación.

## 11. El asterisco `*`

`*` significa «cualquier valor permitido de este campo».

Ejemplo:

```text
0 * * * *
```

coincide en el minuto `0` de cada hora.

## 12. Listas, rangos y pasos

Ejemplos de sintaxis común de Cronie:

```text
1,15,30
1-5
*/10
```

Interpretación:

- `1,15,30` → valores concretos;
- `1-5` → rango;
- `*/10` → cada 10 unidades **dentro de ese campo**.

## 13. `*/N` no siempre significa «cada N horas desde ahora»

Ejemplo:

```text
*/23
```

en el campo hora selecciona valores dentro del rango diario; no crea automáticamente un intervalo continuo de 23 horas desde el momento actual.

Interpreta cada paso dentro del campo donde aparece.

## 14. Día del mes y día de la semana: detalle importante

En Cronie, si restringes tanto:

- día del mes;
- día de la semana;

la tarea se ejecuta cuando **cualquiera de esos dos campos coincide**, no únicamente cuando coinciden ambos.

Es una fuente frecuente de errores de calendario.

## 15. Ejemplo de horario

```text
0 18 * * 1-5
```

se interpreta como:

```text
minuto: 0
hora: 18
día del mes: cualquiera
mes: cualquiera
día de semana: lunes a viernes
```

## 16. Cron y el entorno

Una tarea ejecutada por cron no hereda necesariamente el mismo entorno interactivo de tu terminal.

En Cronie, entre otras cosas:

- `SHELL` suele inicializarse como `/bin/sh`;
- `HOME` y `LOGNAME` se establecen para el propietario de la tabla;
- `PATH` puede no coincidir con el que ves en una terminal interactiva.

Por eso un script que depende de aliases, funciones interactivas o rutas implícitas puede fallar bajo cron.

## 17. Estrategia recomendada: programa un script, no una línea enorme

En lugar de poner lógica compleja dentro del crontab:

```text
muchas órdenes && redirecciones && sustituciones ...
```

crea un script probado:

```text
registro.sh
```

y programa únicamente su ruta.

Ventajas:

- puedes probarlo manualmente;
- puede pasar `bash -n` y ShellCheck;
- conserva su shebang;
- es más fácil de versionar;
- reduce problemas de quoting dentro del crontab.

## 18. El carácter `%` tiene significado especial en Cronie

En la parte de comando de una entrada de Cronie, un `%` sin escapar tiene tratamiento especial.

Esto es otra razón para mantener comandos complejos dentro de un script y dejar el crontab lo más simple posible.

## 19. Cambios de horario y DST

Los relojes civiles pueden saltar hacia adelante o repetirse por cambios de horario.

En Cronie, una hora que no existe puede no ejecutarse y una hora repetida puede provocar una coincidencia adicional según la situación.

Si una tarea es crítica, debes considerar zona horaria y cambios de reloj, no solo escribir cinco campos.

## 20. Cron no recupera automáticamente cualquier ejecución perdida

El daemon comprueba horarios mientras está funcionando.

Si el equipo está apagado en el instante programado, la ejecución tradicional de cron normalmente no ocurre después solo por haber encendido el equipo.

Existen herramientas complementarias como `anacron` para ciertos trabajos periódicos; no las desarrollaremos todavía.

## 21. Preparar el script seguro de laboratorio

```bash
cd ~/linux-lab
mkdir -p modulo-30-automatizacion
cd modulo-30-automatizacion
pwd
```

Crea `registro.sh`:

```bash
#!/usr/bin/env bash

archivo="$HOME/linux-lab/modulo-30-automatizacion/ejecuciones.log"
printf '%(%F %T)T\n' -1 >> "$archivo"
```

Este script solo añade una marca de tiempo a un archivo del laboratorio.

## 22. Validar antes de programar

```bash
bash -n registro.sh
bash registro.sh
cat ejecuciones.log
```

Si ShellCheck está disponible:

```bash
shellcheck registro.sh
```

No continúes con programación automática hasta comprobar que el archivo se actualiza correctamente.

## 23. Hacer ejecutable el script

Después de comprobarlo:

```bash
chmod u+x registro.sh
```

`chmod u+x` modifica solo el permiso de ejecución del archivo de práctica.

Prueba ejecución directa:

```bash
./registro.sh
```

## 24. Obtener la ruta exacta

```bash
realpath registro.sh
```

Guarda mentalmente o copia la ruta que devuelve.

Para tareas programadas, una ruta absoluta evita depender del directorio actual.

## 25. Diseñar una entrada cron de práctica

Ejemplo conceptual para ejecutar cada cinco minutos:

```text
*/5 * * * * /ruta/absoluta/al/registro.sh
```

**No copies literalmente `/ruta/absoluta/...`.** Usa la ruta real obtenida con `realpath`.

## 26. Instalar la práctica cron de forma controlada

Esta parte modifica tu crontab de usuario.

Antes:

```bash
crontab -l
```

Revisa si ya existen tareas.

Después:

```bash
crontab -e
```

añade **una sola línea** con tu script de laboratorio.

No borres ni alteres entradas existentes.

## 27. Verificar la instalación

```bash
crontab -l
```

Comprueba visualmente que:

- la línea aparece una sola vez;
- la ruta es la correcta;
- el horario es el que pretendías.

## 28. Comprobar el resultado

Después de una ejecución programada, consulta:

```bash
cat ~/linux-lab/modulo-30-automatizacion/ejecuciones.log
```

Debes ver una nueva marca de tiempo.

Si no aparece, investiga:

- servicio cron disponible;
- sintaxis;
- ruta;
- permiso de ejecución;
- entorno;
- logs de cron según la distribución.

## 29. Retirar únicamente la línea de práctica

Al terminar el ejercicio:

```bash
crontab -e
```

elimina solo la línea que apunta a `registro.sh`.

Después verifica:

```bash
crontab -l
```

No uses `crontab -r` para esta limpieza.

## 30. Qué es un temporizador systemd

Una unidad `.timer` puede programar la activación de otra unidad, normalmente una `.service` del mismo nombre.

Modelo:

```text
lab-registro.timer
        ↓
momento/intervalo
        ↓
lab-registro.service
        ↓
script probado
```

## 31. Timer y service son responsabilidades diferentes

La unidad `.timer` responde:

```text
¿cuándo?
```

La unidad `.service` responde:

```text
¿qué se ejecuta?
```

Esta separación hace que la tarea pueda probarse manualmente iniciando primero el servicio.

## 32. Consultar timers del sistema

```bash
systemctl list-timers --all
```

muestra timers cargados, última y próxima activación cuando están disponibles.

Es una consulta.

## 33. Consultar timers del usuario

Si existe un administrador systemd de usuario:

```bash
systemctl --user list-timers --all
```

Esto no administra unidades globales del sistema.

Algunos contenedores, sistemas mínimos o entornos especiales pueden no tener disponible un user manager de systemd.

## 34. `OnCalendar=`

`OnCalendar=` programa según el reloj/calendario.

Ejemplos reconocidos por systemd:

```text
hourly
daily
weekly
```

También admite expresiones de calendario más detalladas.

## 35. Validar una expresión sin instalar un timer

```bash
systemd-analyze calendar 'daily'
```

Esta orden analiza, normaliza y muestra la próxima coincidencia.

También puedes pedir varias:

```bash
systemd-analyze calendar --iterations=3 'Mon..Fri 18:00'
```

Esta es una excelente forma de comprobar la intención **antes** de crear el temporizador.

## 36. Temporizadores monotónicos

systemd también puede programar intervalos relativos, por ejemplo:

```text
OnActiveSec=1min
OnUnitActiveSec=5min
```

`OnActiveSec=` cuenta desde que se activa el timer.

`OnUnitActiveSec=` cuenta desde la última activación de la unidad asociada.

Estos intervalos no expresan una hora civil como `18:30`; expresan tiempo relativo.

## 37. `Persistent=true`

Para timers basados en `OnCalendar=`, `Persistent=true` guarda en disco cuándo fue activado por última vez el servicio asociado.

Cuando el timer vuelve a activarse, systemd comprueba si **habría vencido al menos una vez** durante el tiempo en que estuvo inactivo. Si es así, dispara la unidad inmediatamente, sujeto también a retrasos como `RandomizedDelaySec=`.

Esto sirve para recuperar una ejecución perdida, por ejemplo después de que el equipo haya estado apagado.

Pero hay una precisión importante:

```text
Persistent=true ≠ cola de todas las ejecuciones perdidas
```

Si un trabajo diario habría vencido cinco veces mientras el timer estuvo inactivo, no debes asumir que systemd ejecutará cinco veces el servicio al volver. La documentación upstream establece que basta con que hubiera debido dispararse **al menos una vez** para generar la activación de recuperación.

Además, `Persistent=true` solo tiene efecto sobre timers configurados con `OnCalendar=`; no convierte automáticamente los timers monotónicos en persistentes.

### Apagado/inactividad y suspensión no son exactamente lo mismo

Los timers de calendario usan el reloj de tiempo real. Si el sistema entra en suspensión o hibernación, ese reloj sigue avanzando. Cuando el sistema reanuda, los eventos de calendario que vencieron durante la suspensión pueden procesarse entonces.

La documentación de systemd también aclara que, si el mismo timer de calendario venció varias veces durante una suspensión continua, eso produce **una sola activación del servicio** al reanudarse.

Por tanto:

```text
apagado/inactividad + Persistent=true → recuperación al activar el timer
suspensión + OnCalendar=              → recuperación al reanudar
múltiples vencimientos perdidos       → no asumir una ejecución por cada vencimiento
```

Esto ofrece una diferencia importante frente al cron tradicional para equipos que pueden permanecer apagados.

## 38. `AccuracySec=`

Un timer no necesariamente se dispara en el microsegundo exacto indicado.

`AccuracySec=` define una ventana de precisión y systemd puede agrupar despertares para ahorrar recursos.

El valor predeterminado documentado es de un minuto.

Para tareas normales, no reduzcas la precisión sin una razón real.

## 39. `RandomizedDelaySec=`

`RandomizedDelaySec=` añade un retraso aleatorio dentro de un intervalo.

Sirve para evitar que muchas máquinas ejecuten la misma tarea exactamente al mismo tiempo.

Ejemplo conceptual:

```text
OnCalendar=daily
RandomizedDelaySec=15min
```

No necesitamos activarlo en la práctica local.

## 40. Unidad service de usuario para el laboratorio

Primero crea la carpeta de configuración de usuario si no existe:

```bash
mkdir -p ~/.config/systemd/user
```

Esto modifica únicamente configuración del usuario actual.

Crea:

```text
~/.config/systemd/user/lab-registro.service
```

con:

```ini
[Unit]
Description=Práctica segura de registro automático

[Service]
Type=oneshot
ExecStart=%h/linux-lab/modulo-30-automatizacion/registro.sh
```

`%h` es un especificador de systemd que representa el directorio personal del usuario.

## 41. Probar el servicio antes del timer

Recarga las unidades de usuario:

```bash
systemctl --user daemon-reload
```

Después prueba **solo el servicio**:

```bash
systemctl --user start lab-registro.service
```

Comprueba:

```bash
cat ~/linux-lab/modulo-30-automatizacion/ejecuciones.log
```

Si esto falla, no continúes con el timer.

## 42. Consultar el estado del servicio

```bash
systemctl --user status lab-registro.service
```

Una unidad `Type=oneshot` puede aparecer como inactiva después de terminar correctamente; eso no significa necesariamente que haya fallado.

Revisa el estado/resultados y los logs.

## 43. Logs del servicio de usuario

```bash
journalctl --user -u lab-registro.service
```

Consulta eventos asociados a esa unidad cuando el entorno mantiene journal de usuario.

No publiques logs completos si contienen rutas o datos privados innecesarios.

## 44. Unidad timer de práctica

Crea:

```text
~/.config/systemd/user/lab-registro.timer
```

con:

```ini
[Unit]
Description=Temporizador de práctica para lab-registro

[Timer]
OnActiveSec=1min
OnUnitActiveSec=5min
Unit=lab-registro.service

[Install]
WantedBy=timers.target
```

Esta práctica usa tiempos relativos para poder observarla sin depender de una hora del día.

## 45. Recargar y revisar

```bash
systemctl --user daemon-reload
systemctl --user list-timers --all
```

Todavía no necesitas habilitar el timer para el arranque.

## 46. Iniciar el timer de práctica

```bash
systemctl --user start lab-registro.timer
```

`start` lo activa para la sesión/manager actual.

No usamos `enable` en la práctica principal porque no necesitamos dejarlo configurado para futuras sesiones.

## 47. Verificar el timer

```bash
systemctl --user status lab-registro.timer
systemctl --user list-timers --all
```

Busca:

- próxima ejecución;
- última ejecución;
- unidad que activa.

## 48. Detener el timer al terminar

```bash
systemctl --user stop lab-registro.timer
```

Después:

```bash
systemctl --user list-timers --all
```

Comprueba que ya no quede activo como práctica.

## 49. Retirar las dos unidades de práctica

Solo después de detener el timer y confirmar los nombres exactos:

```bash
rm -- "$HOME/.config/systemd/user/lab-registro.service" \
      "$HOME/.config/systemd/user/lab-registro.timer"
```

Este `rm` modifica configuración de usuario y elimina **únicamente los dos archivos exactos creados por el ejercicio**.

Después:

```bash
systemctl --user daemon-reload
```

No uses comodines ni borrado recursivo para esta limpieza.

## 50. `start` frente a `enable`

En systemd:

```text
start  → activa ahora
enable → configura activación futura según [Install]
```

`enable --now` hace ambas cosas.

En este laboratorio usamos `start` porque queremos una prueba temporal y reversible.

## 51. No pongas lógica de shell compleja directamente en `ExecStart=`

`ExecStart=` no es una línea de shell interactiva normal.

Operadores como:

```text
>
&&
||
$HOME
```

no deben suponerse interpretados como lo haría Bash.

Por eso nuestra unidad ejecuta un **script Bash ya probado** y deja redirecciones y lógica dentro del script.

## 52. Cron frente a systemd timers

| Característica | cron | systemd timer |
|---|---|---|
| modelo | tabla de horarios | unidades `.timer` + servicio |
| calendario | cinco campos en crontab | `OnCalendar=` |
| intervalos relativos | limitado/depende del diseño | directivas monotónicas |
| tarea perdida con equipo apagado | normalmente no se recupera sola | `Persistent=true` puede recuperar que hubo al menos una activación `OnCalendar` perdida; no reproduce necesariamente cada vencimiento |
| consulta | `crontab -l` | `systemctl list-timers` |
| logs | depende de implementación/configuración | journal de la unidad cuando aplica |
| entorno | cron suele ser reducido | entorno de unidad systemd |
| prueba separada de tarea | llamar script manualmente | iniciar `.service` manualmente |

No existe una regla de que uno sea siempre mejor.

## 53. Cuándo preferir cron

Puede ser apropiado cuando:

- ya está instalado y gestionado en el entorno;
- la tarea es sencilla;
- la portabilidad entre sistemas Unix importa;
- el equipo tiene convenciones existentes basadas en crontab.

## 54. Cuándo preferir systemd timers

Puede ser apropiado en sistemas systemd cuando necesitas:

- integración con servicios;
- estado consultable;
- journal;
- temporizadores monotónicos;
- `Persistent=true` para calendarios;
- dependencias y propiedades de unidades.

## 55. Errores frecuentes

| Error | Problema | Corrección |
|---|---|---|
| programar antes de probar | automatizas un fallo | prueba manualmente primero |
| usar rutas relativas | el directorio de ejecución puede ser distinto | usa rutas absolutas |
| confiar en el PATH interactivo | cron/systemd tienen otro entorno | usa script probado y rutas controladas |
| poner una línea enorme en cron | quoting y `%` complican el comportamiento | programa un script |
| usar `crontab -r` para retirar una línea | elimina toda la tabla | usa `crontab -e` |
| interpretar `*/N` como intervalo universal | opera dentro del campo | analiza cada campo |
| olvidar la regla DOM/DOW de Cronie | puedes ejecutar más días de los esperados | verifica el calendario |
| asumir que cron recupera tareas perdidas | puede no ejecutarlas después | considera diseño apropiado/anacron/systemd |
| asumir que `Persistent=true` reproduce todas las ejecuciones omitidas | puede haber una sola activación de recuperación | interprétalo como detección de al menos un vencimiento perdido |
| confundir apagado con suspensión | systemd trata esos escenarios de forma distinta | distingue inactividad del timer y suspensión del sistema |
| crear timer sin probar service | dificulta diagnóstico | inicia el service manualmente |
| usar `enable --now` solo para probar | deja persistencia innecesaria | usa `start` en práctica temporal |
| escribir shell directamente en `ExecStart=` | systemd no es un shell | llama a un script |
| reducir `AccuracySec` sin motivo | aumenta precisión/costo de wakeups | conserva valores razonables |

## 56. Detección de error 1

Analiza:

```text
*/5 * * * * cd proyecto && ./tarea.sh > salida.log
```

Problemas:

- directorio relativo/implícito;
- varias operaciones dentro del crontab;
- resultado dependiente del entorno;
- más difícil probar y versionar.

Mejor diseño:

```text
*/5 * * * * /ruta/absoluta/tarea_programada.sh
```

y dentro del script haces la validación, cambio de directorio y redirección de forma explícita.

## 57. Detección de error 2

Analiza:

```text
0 4 1,15 * 5 comando
```

Si creías que significa «solo los días 1 o 15 que además sean viernes», tu interpretación es incorrecta para Cronie.

Al restringir ambos campos de día, Cronie ejecuta cuando coincide **día del mes o día de la semana**.

## 58. Detección de error 3

Analiza:

```ini
[Service]
ExecStart=echo hola >> $HOME/archivo.log
```

Problema: se escribió una línea como si `ExecStart=` fuera interpretado automáticamente por un shell.

Mejor:

```ini
[Service]
Type=oneshot
ExecStart=%h/linux-lab/modulo-30-automatizacion/registro.sh
```

## 59. Método seguro para automatizar

1. define exactamente la tarea;
2. limita su alcance;
3. ejecútala manualmente;
4. revisa su estado y salida;
5. usa rutas conocidas;
6. decide cron o systemd según el entorno;
7. valida el horario;
8. programa una tarea no destructiva primero;
9. verifica que realmente se ejecutó;
10. documenta cómo detenerla y retirarla.

## 60. Práctica independiente

Diseña una automatización llamada `estado_laboratorio`.

Debe:

1. usar un script Bash separado;
2. añadir fecha/hora a un archivo dentro de `~/linux-lab/modulo-30-automatizacion`;
3. pasar `bash -n`;
4. probarse manualmente antes de programarse;
5. tener una propuesta de horario cron;
6. tener una propuesta equivalente con timer systemd;
7. indicar cómo verificar que se ejecutó;
8. indicar cómo detenerla;
9. indicar cómo retirarla sin afectar otras tareas;
10. no usar `sudo`, borrados, paquetes, red, servicios del sistema ni datos sensibles.

## 61. Mini evaluación

1. ¿debes programar un script antes de probarlo manualmente? A) Sí B) No
2. ¿`crontab -l` consulta la tabla? A) Sí B) No
3. ¿usaremos `crontab -r` para retirar una sola práctica? A) Sí B) No
4. ¿una entrada cron de usuario tiene cinco campos de tiempo antes del comando? A) Sí B) No
5. ¿`*` significa cualquier valor permitido del campo? A) Sí B) No
6. ¿`*/10` significa necesariamente cada diez horas desde ahora? A) Sí B) No
7. si DOM y DOW están restringidos en Cronie, ¿basta que coincida uno? A) Sí B) No
8. ¿cron garantiza el mismo PATH de tu terminal interactiva? A) Sí B) No
9. ¿es mejor programar un script probado que una línea cron enorme? A) Sí B) No
10. ¿cron tradicional recupera automáticamente toda ejecución perdida por apagado? A) Sí B) No
11. ¿un `.timer` suele activar una `.service`? A) Sí B) No
12. ¿`OnCalendar=` usa expresiones de calendario? A) Sí B) No
13. ¿`systemd-analyze calendar` puede validar una expresión antes de instalar el timer? A) Sí B) No
14. ¿`Persistent=true` aplica a recuperación de activaciones `OnCalendar` perdidas? A) Sí B) No
15. Si un timer habría vencido cinco veces mientras estuvo inactivo, ¿`Persistent=true` obliga a ejecutar cinco veces el servicio al volver? A) Sí B) No
16. Si un timer `OnCalendar=` vence varias veces durante una suspensión continua, ¿debes asumir varias activaciones al reanudar? A) Sí B) No
17. ¿`systemctl --user start` y `enable` significan exactamente lo mismo? A) Sí B) No
18. ¿`ExecStart=` debe tratarse como una línea de Bash interactiva? A) Sí B) No

## 62. Registro de aprendizaje

```text
Automatizar significa:
Regla antes de programar:
`crontab -l` sirve para:
`crontab -e` sirve para:
Los cinco campos cron son:
`*` significa:
¿por qué una ruta absoluta ayuda?:
¿por qué no conviene una línea cron enorme?:
Una unidad `.timer` sirve para:
Una unidad `.service` sirve para:
`OnCalendar=` significa:
`OnActiveSec=` significa:
`Persistent=true` sirve para:
¿reproduce todas las ejecuciones perdidas?:
Diferencia entre apagado/inactividad y suspensión para timers de calendario:
`AccuracySec=` afecta:
`systemctl --user list-timers` muestra:
Diferencia entre `start` y `enable`:
Algo que todavía confundo:
Estado: EN APRENDIZAJE / PRACTICADO
```

## 63. Puerta de dominio

Para considerar este módulo **DOMINADO** deberás poder en más de una ocasión:

1. leer correctamente una expresión cron sencilla;
2. detectar el error conceptual de `*/N` fuera de su campo;
3. explicar el entorno reducido de cron;
4. probar un script antes de programarlo;
5. retirar solo tu propia entrada cron;
6. explicar la pareja timer/service;
7. validar un `OnCalendar=` con `systemd-analyze calendar`;
8. distinguir `start`, `enable` y `Persistent=true`;
9. diagnosticar una automatización que no se ejecutó sin realizar cambios destructivos.

## 64. Fuentes y límites

Fuentes principales:

- Cronie upstream (código y manuales del proyecto): https://github.com/cronie-crond/cronie
- systemd upstream (código y manuales): https://github.com/systemd/systemd/tree/main/man
- Las páginas man7 siguientes son copias consultables de manuales; para contrastar cambios de versión, revisar upstream.
- Cronie `crontab(5)`: https://man7.org/linux/man-pages/man5/crontab.5.html
- Cronie `crond(8)`: https://man7.org/linux/man-pages/man8/crond.8.html
- systemd upstream — `systemd.timer(5)`: https://github.com/systemd/systemd/blob/main/man/systemd.timer.xml
- systemd upstream — `systemd.time(7)`: https://github.com/systemd/systemd/blob/main/man/systemd.time.xml
- systemd `systemd-analyze(1)`: https://man7.org/linux/man-pages/man1/systemd-analyze.1.html
- systemd `systemctl(1)`: https://man7.org/linux/man-pages/man1/systemctl.1.html
- Red Hat Enterprise Linux 10 — systemd unit files: https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_systemd_unit_files_to_customize_and_optimize_your_system/

Puntos verificados documentalmente:

- Cronie utiliza cinco campos de tiempo y revisa tareas por minuto;
- los comandos del crontab se ejecutan mediante `/bin/sh` por defecto salvo configuración de `SHELL`; `HOME` y `LOGNAME` se preparan para el usuario;
- `%` posee significado especial en la parte de comando de Cronie;
- cuando día del mes y día de semana están ambos restringidos, Cronie ejecuta si coincide cualquiera de ellos;
- `systemd.timer` admite `OnCalendar=` y temporizadores monotónicos como `OnActiveSec=` y `OnUnitActiveSec=`;
- `Persistent=true` solo afecta timers `OnCalendar=` y, al activarse el timer, dispara el servicio si habría vencido al menos una vez mientras estuvo inactivo; no debe interpretarse como una cola que reproduce todos los vencimientos perdidos;
- los timers `OnCalendar=` que vencen durante suspensión se procesan al reanudar; varios vencimientos durante una suspensión continua producen una sola activación del servicio;
- `AccuracySec=` tiene un valor predeterminado documentado de un minuto;
- `systemd-analyze calendar` analiza y normaliza la misma sintaxis utilizada por `OnCalendar=`;
- `systemctl list-timers` muestra temporizadores y sus próximas/últimas activaciones.

Se posponen:

- `anacron` en profundidad;
- `/etc/crontab` y `/etc/cron.d` como práctica administrativa;
- timers systemd globales con privilegios;
- `WakeSystem=`;
- calendarios avanzados y zonas horarias complejas;
- dependencias avanzadas de unidades;
- sandboxing de servicios systemd;
- `systemd-run` y timers transitorios;
- monitoreo centralizado de trabajos.

**Estado de la lección:** redactada y revisada documentalmente contra Cronie, systemd y documentación vigente de RHEL 10. La práctica principal usa scripts no destructivos; la parte de systemd se limita a unidades de usuario y se incluye un procedimiento de retirada explícito.

Siguiente módulo por redactar: **Módulo 31 — Archivos y compresión con `tar`, `gzip` y `xz`**.
