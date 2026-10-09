# Módulo 18 — Logs y diagnóstico inicial con journalctl

Manual Maestro de Linux y Shell Scripting — Edición 2026 · v3 · Decimoctava entrega.

[Índice del manual](README.md) · [← Módulo 17](modulo-17-systemd-unidades-servicios-init.md) · [Arquitectura](00-indice-arquitectura.md) · [Módulo 19 →](modulo-19-redes-ip-dns-rutas-ip-ss.md)

## 1. Qué aprenderás

Al terminar este módulo podrás:

- explicar qué es un log;
- distinguir evento, mensaje y registro;
- explicar qué hace `systemd-journald`;
- usar `journalctl` para consultar el journal sin modificar el sistema;
- limitar resultados por arranque, unidad, prioridad y tiempo;
- seguir mensajes nuevos con `journalctl -f`;
- diferenciar journal de archivos tradicionales en `/var/log`;
- reconocer que la persistencia del journal depende de configuración y distribución;
- aplicar un método básico de diagnóstico antes de reiniciar o modificar servicios;
- reconocer que los logs pueden contener datos sensibles.

Conocimientos previos:
- procesos;
- systemd y unidades;
- `systemctl status`;
- pipes, `grep`, `less`, `head` y `tail`.

**Seguridad y privacidad:** las prácticas son de lectura. No borraremos logs, no cambiaremos retención, no modificaremos `journald.conf`, no reiniciaremos servicios y no usaremos `sudo` para ampliar acceso. No publiques logs completos: pueden contener nombres de usuario, hostnames, rutas, direcciones IP, identificadores, comandos, errores de aplicaciones o datos privados.

## 2. Qué es un log

Un **log** es un registro de eventos generado por un sistema, servicio o aplicación.

Puede registrar, por ejemplo:

- inicio y detención de servicios;
- errores;
- advertencias;
- autenticaciones;
- eventos del kernel;
- actividad de aplicaciones;
- arranque del sistema.

Un log no es automáticamente “un archivo de texto”. En systemd, el journal puede almacenarse en un formato estructurado administrado por `systemd-journald`.

## 3. Evento, mensaje y entrada

Modelo simple:

```text
evento → genera información → entrada de log
```

Una entrada puede incluir campos como:

- fecha y hora;
- host;
- proceso;
- PID;
- unidad systemd;
- prioridad;
- mensaje;
- otros metadatos.

La cantidad exacta de campos depende de la fuente y del sistema de logging.

## 4. systemd-journald

`systemd-journald` es el servicio de systemd que recopila y almacena datos de logging.

Puede recibir mensajes de fuentes como:

- kernel;
- servicios systemd;
- stdout/stderr de determinados servicios;
- syslog;
- otras interfaces de logging.

En algunas distribuciones, journald trabaja junto con un sistema tradicional como rsyslog.

No asumas que “journal” reemplaza siempre todos los archivos de `/var/log`.

## 5. journalctl

`journalctl` consulta el journal.

Ejemplo:

```bash
journalctl
```

Puede producir una gran cantidad de salida.

En muchos entornos se abre mediante un paginador.

Para salir:

```text
q
```

Para principiantes, es mejor aplicar filtros que leer todo el journal.

## 6. No confundir consulta con modificación

Comandos como:

```bash
journalctl -b
journalctl -u nombre.service
journalctl -p err
journalctl --since today
```

son consultas.

En cambio, acciones relacionadas con:

- vaciado;
- rotación forzada;
- límites de tamaño;
- configuración de almacenamiento;
- cambio de permisos;

pueden modificar el sistema y no pertenecen a esta práctica inicial.

## 7. Journal del arranque actual con -b

Consulta:

```bash
journalctl -b
```

`-b` limita la consulta al arranque actual.

Esto es útil cuando quieres responder:

> ¿qué ocurrió desde que arrancó este sistema?

No significa que el journal tenga necesariamente datos de arranques anteriores.

## 8. Listar arranques conocidos

Consulta:

```bash
journalctl --list-boots
```

Si el journal conserva información de varios arranques, puede mostrarlos con identificadores e índices.

Ejemplo conceptual:

```text
-1 → arranque anterior
 0 → arranque actual
```

La disponibilidad de arranques anteriores depende de la persistencia y retención del journal.

## 9. Arranque anterior

Si existe información persistida:

```bash
journalctl -b -1
```

consulta el arranque anterior.

Si no devuelve datos útiles, no significa necesariamente que el sistema esté roto. Puede deberse a:

- journal no persistente;
- rotación;
- limpieza;
- instalación reciente;
- configuración particular.

## 10. Filtrar por unidad con -u

Ejemplo:

```bash
journalctl -u NOMBRE.service
```

Muestra entradas asociadas a una unidad.

Para limitar al arranque actual:

```bash
journalctl -u NOMBRE.service -b
```

Este patrón es muy útil para investigar un servicio que falló al arrancar.

## 11. Elegir primero una unidad real

No inventes nombres.

Primero:

```bash
systemctl list-units --type=service
```

Elige una unidad que exista en tu sistema.

Después consulta:

```bash
systemctl status NOMBRE.service
```

y solo entonces:

```bash
journalctl -u NOMBRE.service -b
```

## 12. Prioridades

Los mensajes pueden usar niveles de prioridad compatibles con syslog.

Niveles comunes, de más grave a menos grave:

```text
emerg
alert
crit
err
warning
notice
info
debug
```

No necesitas memorizar todos inmediatamente.

Para comenzar:

```text
err     → errores y más graves
warning → advertencias y más graves
info    → información y más graves
```

## 13. Filtrar por prioridad

Ejemplo:

```bash
journalctl -p err -b
```

muestra mensajes del arranque actual con prioridad `err` y, según la semántica del filtro, niveles más importantes.

Otra consulta:

```bash
journalctl -p warning -b
```

Puede producir más resultados.

**Advertencia:** un mensaje de prioridad alta no demuestra por sí solo que exista un problema actual. Debes interpretar contexto y tiempo.

## 14. Filtrar por tiempo con --since

Ejemplos:

```bash
journalctl --since today
```

```bash
journalctl --since "1 hour ago"
```

```bash
journalctl --since "2026-10-07 10:00:00"
```

Las expresiones aceptadas dependen del parser temporal de systemd.

Para diagnóstico real, usa intervalos lo bastante estrechos para no mezclar eventos irrelevantes.

## 15. --until

Puedes limitar el final del intervalo:

```bash
journalctl --since "10:00" --until "10:15"
```

Esto ayuda a investigar:

> ¿qué ocurrió durante esos 15 minutos?

No necesitas consultar horas de datos si el fallo ocurrió en un intervalo pequeño y conocido.

## 16. Seguir mensajes con -f

```bash
journalctl -f
```

muestra entradas recientes y continúa esperando mensajes nuevos.

Se parece conceptualmente a:

```bash
tail -f archivo.log
```

pero consulta el journal.

Para detener el seguimiento y volver al prompt:

```text
Ctrl+C
```

No modifica el journal.

## 17. Seguir una unidad concreta

Ejemplo:

```bash
journalctl -u NOMBRE.service -f
```

Esto puede ser útil mientras reproduces un problema controlado.

No reinicies o fuerces fallos de servicios solo para generar mensajes.

## 18. Mostrar mensajes recientes

Puedes limitar por cantidad:

```bash
journalctl -n 20
```

Muestra las últimas entradas según el filtro aplicado.

Combinación:

```bash
journalctl -u NOMBRE.service -n 20
```

Esto suele ser más manejable que abrir miles de entradas.

## 19. Kernel con -k

Consulta:

```bash
journalctl -k -b
```

muestra mensajes del kernel para el arranque actual cuando están disponibles en el journal.

No confundas cada mensaje del kernel con un fallo.

Muchos son informativos.

## 20. Formatos de salida

`journalctl` admite varios formatos.

Ejemplo:

```bash
journalctl -n 5 -o short
```

Otros formatos pueden mostrar más metadatos o datos estructurados.

En esta etapa usaremos la salida predeterminada o `short`.

No necesitas JSON todavía.

## 21. Buscar texto dentro de la salida

Puedes combinar con herramientas conocidas:

```bash
journalctl -b | grep -i 'error'
```

Pero esta técnica tiene límites:

- “error” puede aparecer en mensajes no críticos;
- errores reales pueden no contener la palabra `error`;
- pierdes campos estructurados si solo buscas texto.

Siempre que exista un filtro nativo adecuado, priorízalo.

## 22. status y journalctl se complementan

`systemctl status NOMBRE.service` ofrece una vista resumida:

- estado;
- PID;
- fragmento de logs reciente.

`journalctl -u NOMBRE.service` permite profundizar.

Método:

```text
status → identifica estado
journalctl → investiga historial
```

No reinicies el servicio antes de leer la evidencia, porque podrías cambiar el contexto del problema.

## 23. Journal persistente y volátil

systemd puede almacenar el journal en ubicaciones como:

```text
/run/log/journal/
```

para almacenamiento volátil, o:

```text
/var/log/journal/
```

para persistencia, según configuración y entorno.

**No generalices un único comportamiento para todas las distribuciones.**

La política real depende de:

- `Storage=`;
- existencia de rutas;
- distribución;
- configuración;
- límites y rotación.

## 24. RHEL 10 y persistencia

La documentación de RHEL 10 describe una configuración predeterminada donde el journal puede ser volátil en `/run/log/journal` y explica cómo configurar persistencia.

Eso es una política de RHEL documentada, no una regla universal de systemd en todas las distribuciones.

Por eso este manual separa:

```text
comportamiento de systemd
```

de:

```text
default de una distribución concreta
```

## 25. /var/log sigue siendo importante

Servicios y sistemas pueden escribir archivos tradicionales bajo:

```text
/var/log/
```

Ejemplos posibles según distribución:

```text
/var/log/messages
/var/log/syslog
/var/log/auth.log
/var/log/secure
```

No todos existen en todas las distribuciones.

No uses una ruta de Ubuntu como si fuera universal para RHEL o viceversa.

## 26. Rsyslog

`rsyslog` es un sistema de logging tradicional/moderno basado en syslog que puede coexistir con journald.

En RHEL, la documentación describe integración donde journald recopila mensajes y rsyslog puede procesarlos y escribir archivos bajo `/var/log`.

No asumiremos esa arquitectura exacta para todas las distribuciones.

## 27. Permisos de lectura de logs

No todos los usuarios pueden ver todas las entradas.

Si una consulta omite mensajes por permisos:

- no añadas `sudo` automáticamente;
- pregunta si necesitas realmente esos datos;
- usa el mínimo acceso requerido.

En un entorno administrado, el acceso al journal puede controlarse por grupos y políticas.

## 28. Logs contienen información sensible

Un log puede revelar:

- nombre de usuario;
- hostname;
- IP;
- rutas;
- nombres de servicios;
- procesos;
- identificadores;
- errores de autenticación;
- nombres de archivos;
- datos introducidos por aplicaciones.

Antes de compartir:

1. recorta solo las líneas relevantes;
2. elimina secretos;
3. oculta identificadores privados cuando no sean necesarios;
4. conserva timestamps si ayudan al diagnóstico;
5. no alteres el significado técnico.

## 29. Nunca publiques secretos

Si un log contiene:

- contraseña;
- token;
- cookie;
- API key;
- clave privada;
- secreto de aplicación;
- credencial;

**no lo subas a GitHub ni lo pegues en el chat**.

Detén la publicación y elimina/rota el secreto según el sistema afectado.

## 30. Diagnóstico: correlación temporal

Una buena investigación comienza preguntando:

> ¿a qué hora ocurrió el problema?

Después:

```text
momento del fallo
↓
unidad afectada
↓
logs del intervalo
↓
mensajes anteriores y posteriores
```

No busques todo el journal sin límite si conoces la hora aproximada.

## 31. Diagnóstico: correlación entre servicio y sistema

Un servicio puede fallar por algo externo:

- red;
- disco;
- permisos;
- dependencia;
- montaje;
- configuración;
- memoria.

Por eso, además de:

```bash
journalctl -u NOMBRE.service
```

puede ser útil revisar el arranque o prioridad correspondiente.

No concluyas demasiado pronto.

## 32. No borres logs para “limpiar el error”

Borrar logs no corrige la causa.

Además, elimina evidencia útil.

En este módulo no practicamos:

- `journalctl --vacuum-*`;
- eliminación manual de archivos de log;
- truncado de logs;
- rotación forzada.

Primero diagnostica.

## 33. No edites logs

Los logs son evidencia del comportamiento del sistema.

No los abras en un editor para “corregir” mensajes.

Si necesitas guardar una copia de laboratorio, copia solo un fragmento ya revisado y sin datos sensibles.

## 34. journalctl --disk-usage

Consulta segura:

```bash
journalctl --disk-usage
```

muestra cuánto espacio ocupa el journal accesible para la consulta.

No uses esta cifra como razón automática para borrar logs.

Primero revisa:

- políticas de retención;
- espacio del sistema;
- configuración;
- necesidad de auditoría.

## 35. Preparar la práctica

No necesitas crear archivos.

Comprueba primero:

```bash
ps -p 1 -o comm=
```

Si systemd es relevante:

```bash
command -v journalctl
```

Si `journalctl` no existe o systemd no es el init del entorno, registra esa condición y no fuerces la práctica.

## 36. Práctica A — journal del arranque

```bash
journalctl -b -n 20
```

Objetivo:

- ver solo 20 entradas;
- reconocer timestamps;
- reconocer proceso/unidad;
- no compartir toda la salida.

## 37. Práctica B — mensajes de prioridad alta

```bash
journalctl -b -p err -n 20
```

No asumas que cualquier resultado requiere reparación.

Elige una entrada y responde para ti:

- ¿cuándo ocurrió?;
- ¿qué componente la generó?;
- ¿sigue ocurriendo?;
- ¿está relacionada con un síntoma real?.

## 38. Práctica C — unidad existente

Primero:

```bash
systemctl list-units --type=service
```

Elige una unidad real.

Después:

```bash
systemctl status NOMBRE.service
```

y:

```bash
journalctl -u NOMBRE.service -b -n 20
```

No reinicies la unidad.

## 39. Práctica D — tiempo

Consulta:

```bash
journalctl --since "30 minutes ago" -n 30
```

Si tu versión acepta la expresión, revisa solo ese intervalo.

Si no la acepta, usa un timestamp explícito documentado por tu sistema.

## 40. Práctica E — kernel

```bash
journalctl -k -b -n 20
```

Identifica mensajes informativos sin asumir que son errores.

## 41. Práctica F — seguimiento

```bash
journalctl -f
```

Observa unos segundos.

Después:

```text
Ctrl+C
```

No necesitas provocar errores para ver actividad.

## 42. Práctica G — arranques conocidos

```bash
journalctl --list-boots
```

Si solo aparece el arranque actual, explica al menos dos razones posibles sin concluir que existe un fallo.

## 43. Método inicial de diagnóstico

Cuando un servicio falla:

1. registra hora aproximada;
2. consulta `systemctl status UNIDAD`;
3. consulta `journalctl -u UNIDAD -b`;
4. limita por tiempo si es necesario;
5. busca mensajes inmediatamente anteriores al fallo;
6. distingue error raíz de errores secundarios;
7. revisa dependencias;
8. no reinicies todavía;
9. formula una hipótesis;
10. cambia una sola cosa cuando llegue el momento de intervenir.

## 44. Error raíz frente a error secundario

Ejemplo conceptual:

```text
archivo de configuración inválido
↓
servicio no inicia
↓
aplicación dependiente pierde conexión
↓
aparecen más errores
```

El último error visible no siempre es la causa inicial.

Por eso es útil leer cronológicamente alrededor del primer fallo.

## 45. auditd — introducción conceptual

Algunas distribuciones utilizan el subsistema de auditoría de Linux y un servicio como `auditd` para registrar eventos de seguridad y cumplimiento.

Esto **no es lo mismo que journald**.

Modelo:

```text
journald → logging general de systemd y sistema
audit    → auditoría de eventos según reglas/políticas
```

No configuraremos reglas de auditoría en este módulo.

## 46. No asumir auditd en todos los sistemas

La presencia, configuración y uso de auditd depende de:

- distribución;
- instalación;
- política;
- entorno;
- requisitos de cumplimiento.

Consulta únicamente:

```bash
command -v ausearch
systemctl status auditd.service
```

solo si la unidad existe.

No habilites ni modifiques auditd para completar la lección.

## 47. Errores frecuentes

| Error | Problema | Corrección |
|---|---|---|
| Lees todo `journalctl` sin filtros | Exceso de ruido | Filtra por boot, unidad, tiempo o prioridad |
| Reinicias antes de revisar logs | Cambias evidencia y contexto | Lee primero |
| “err = causa raíz” | Puede ser consecuencia | Correlaciona eventos |
| Publicas logs completos | Expones datos sensibles | Comparte solo fragmentos sanitizados |
| Asumes persistencia universal | Depende de configuración | Comprueba `--list-boots` y entorno |
| Asumes rutas de `/var/log` universales | Cambian por distro | Verifica documentación |
| Usas sudo automáticamente | Amplías acceso | Aplica mínimo privilegio |
| Borras logs para liberar espacio | Pierdes evidencia | Investiga retención antes |
| Confundes journald y auditd | Objetivos distintos | Separa logging y auditoría |
| Grep “error” = diagnóstico completo | Busca texto, no contexto estructurado | Usa filtros nativos y tiempo |

## 48. Práctica independiente

Sin modificar el sistema:

1. muestra las últimas 15 entradas del arranque actual;
2. consulta errores del arranque;
3. elige una unidad real;
4. muestra 15 entradas de esa unidad;
5. limita una consulta por tiempo;
6. consulta 10 mensajes del kernel;
7. lista arranques conocidos;
8. consulta uso en disco del journal;
9. explica si tu journal parece persistente o no, sin cambiarlo;
10. explica qué datos eliminarías antes de compartir un fragmento.

## 49. Mini evaluación

1. ¿Qué hace `journalctl`?
   - A) Consulta el journal.
   - B) Instala paquetes.
   - C) Cambia permisos.

2. ¿Qué hace `journalctl -b`?
   - A) Limita al arranque seleccionado/actual.
   - B) Borra logs.
   - C) Reinicia.

3. ¿Qué hace `journalctl -u servicio.service`?
   - A) Filtra por unidad.
   - B) Actualiza el servicio.
   - C) Desinstala el servicio.

4. ¿Qué hace `journalctl -f`?
   - A) Sigue entradas nuevas.
   - B) Fuerza un reinicio.
   - C) Filtra archivos.

5. ¿La persistencia del journal es idéntica en todas las distribuciones?
   - A) Sí.
   - B) No.

6. ¿Debes reiniciar un servicio antes de revisar sus logs?
   - A) Siempre.
   - B) No.

7. ¿Los logs pueden contener datos sensibles?
   - A) Sí.
   - B) No.

8. ¿Borrar logs corrige la causa de un fallo?
   - A) Sí.
   - B) No.

9. ¿journald y auditd son exactamente lo mismo?
   - A) Sí.
   - B) No.

10. ¿Un mensaje `err` demuestra siempre la causa raíz?
   - A) Sí.
   - B) No.

## 50. Registro de aprendizaje

Puedes responder:

```text
Un log es:
journald sirve para:
journalctl sirve para:
-b significa:
-u sirve para:
-p sirve para:
-f sirve para:
--since sirve para:
La persistencia depende de:
¿Por qué no reinicio antes de leer logs?:
¿Qué datos no compartiría?:
auditd se diferencia de journald porque:
Algo que todavía confundo:
Estado: EN APRENDIZAJE / PRACTICADO
```

## 51. Fuentes y límites

Fuentes principales:

- systemd journalctl manual:
  https://www.freedesktop.org/software/systemd/man/latest/journalctl.html
- systemd-journald manual:
  https://www.freedesktop.org/software/systemd/man/latest/systemd-journald.service.html
- RHEL 10 — Troubleshooting problems by using log files:
  https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/risk_reduction_and_recovery_operations/troubleshooting-problems-by-using-log-files
- RHEL 10 — systemd journal configuration:
  https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/configuring-the-systemd-journal-by-using-rhel-system-roles

Se posponen:

- configuración de `journald.conf`;
- persistencia práctica;
- límites de almacenamiento;
- vacuum/rotación;
- forwarding remoto;
- rsyslog avanzado;
- auditd y reglas de auditoría;
- logrotate;
- observabilidad centralizada;
- SIEM.

**Estado de la lección:** redactada y revisada documentalmente. Las prácticas son de consulta y diagnóstico; no modifican logs ni servicios.

---

**Siguiente:** [Módulo 19 — Redes básicas: IP, DNS, rutas, ip y ss](modulo-19-redes-ip-dns-rutas-ip-ss.md) · [Volver al índice](README.md)
