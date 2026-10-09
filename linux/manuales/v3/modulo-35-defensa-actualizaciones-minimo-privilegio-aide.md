# Módulo 35 — Defensa, actualizaciones, mínimo privilegio, auditoría y AIDE

Manual Maestro de Linux y Shell Scripting — Edición 2026 · v3 · Trigésima quinta entrega.

[Índice del manual](README.md) · [← Módulo 34](modulo-34-almacenamiento-lsblk-df-du-montaje-fstab.md) · [Arquitectura](00-indice-arquitectura.md)

## 1. Propósito del módulo

Este módulo cierra el núcleo inicial del manual.

Su objetivo no es convertir Linux en un sistema “invulnerable”, sino enseñarte una rutina defensiva verificable:

```text
conocer el sistema
    ↓
reducir privilegios
    ↓
mantener software actualizado
    ↓
revisar logs y estado
    ↓
crear una línea base
    ↓
detectar cambios
    ↓
documentar evidencia y recuperación
```

Objetivo de evidencia de la arquitectura:

> **Documentar un laboratorio propio con evidencia y recuperación.**

## 2. Qué aprenderás

Al terminar este módulo podrás:

- explicar el principio de mínimo privilegio;
- consultar tu identidad, grupos y privilegios permitidos;
- distinguir operación de consulta de operación administrativa;
- revisar actualizaciones disponibles sin instalarlas automáticamente;
- diferenciar actualización general de actualización de seguridad;
- reconocer que actualizar puede requerir reinicio de procesos o kernel;
- revisar servicios fallidos y logs locales;
- identificar procesos que escuchan puertos en tu propio equipo;
- crear una línea base de integridad dentro de `~/linux-lab`;
- detectar cambios mediante hashes;
- explicar qué es AIDE y cómo funciona;
- distinguir inicialización, comprobación y actualización de una base AIDE;
- reconocer falsos positivos después de cambios legítimos;
- documentar evidencia antes y después de una modificación;
- definir un procedimiento de recuperación;
- evitar automatizaciones defensivas que cambien el sistema sin revisión.

## 3. Alcance de seguridad

Todas las prácticas son sobre:

- tu propio equipo;
- una máquina virtual propia;
- un laboratorio;
- o un sistema expresamente autorizado.

No se incluyen:

- exploración de equipos ajenos;
- persistencia;
- evasión;
- explotación;
- robo de credenciales;
- movimiento lateral;
- técnicas para ocultar actividad.

## 4. Defensa no significa ejecutar todo como root

Una mala práctica defensiva es usar privilegios máximos por costumbre.

El principio correcto es:

```text
usar el menor privilegio necesario
durante el menor tiempo necesario
para una tarea concreta
```

## 5. Consultar identidad

```bash
id
```

muestra información como UID, GID y grupos.

También:

```bash
whoami
groups
```

Son operaciones de consulta.

## 6. Usuario normal frente a root

`root` tiene privilegios administrativos muy amplios.

Un usuario normal tiene un alcance más limitado.

Para aprendizaje diario:

> trabaja como usuario normal y eleva privilegios solo cuando la tarea lo requiera explícitamente.

## 7. Qué es `sudo`

`sudo` permite ejecutar órdenes autorizadas con otra identidad, normalmente root, según reglas definidas por administración.

No significa:

```text
“hacer cualquier cosa como administrador”
```

Las reglas pueden limitar usuarios, hosts y comandos.

## 8. Consultar tus permisos sudo

```bash
sudo -l
```

muestra qué órdenes tienes autorizadas según la configuración aplicable.

Puede solicitar autenticación.

No modifica configuración.

## 9. No editar `sudoers` directamente como práctica

Los archivos principales son:

```text
/etc/sudoers
/etc/sudoers.d/
```

Una regla incorrecta puede romper acceso administrativo o ampliar privilegios indebidamente.

Este módulo se limita a **consulta y concepto**.

## 10. Actualizaciones como medida defensiva

Las vulnerabilidades conocidas suelen corregirse mediante actualizaciones.

Pero actualizar también es un cambio del sistema.

Flujo responsable:

```text
consultar
revisar
entender impacto
planificar ventana
aplicar
verificar
recuperar si fuera necesario
```

## 11. Consultar actualizaciones en RHEL 10

```bash
dnf check-update
```

consulta paquetes instalados que tienen actualizaciones disponibles.

Puede contactar repositorios configurados.

En esta práctica **no instalamos nada**.

Recuerda la semántica específica documentada por DNF:

```text
0   → no hay actualizaciones disponibles
100 → hay actualizaciones disponibles
1   → ocurrió un error
```

Esto importa especialmente en un script defensivo. No debes escribir una regla genérica del tipo:

```text
si estado != 0 → error
```

para `dnf check-update`, porque interpretarías incorrectamente el estado `100`.

Este punto conecta con el **Módulo 25 — Códigos de salida** y con el **Módulo 15 — Paquetes, repositorios y actualizaciones**: el significado de un código debe consultarse en la documentación de la herramienta concreta.

**Equivalentes de consulta en otras distribuciones:** en Debian y Ubuntu, `apt list --upgradable` muestra paquetes con actualizaciones disponibles según el índice local; para actualizar ese índice normalmente se utiliza `apt update`, operación que consulta repositorios y puede requerir privilegios. No instales ni actualices paquetes en esta práctica. En Fedora reciente con DNF5, la comprobación se documenta como `dnf5 check-upgrade`; revisa la distinción entre DNF4 y DNF5 del Módulo 15. Para AIDE, consulta los procedimientos y rutas de configuración propios de Debian/Ubuntu o Fedora antes de administrar una base real.

## 12. Consultar avisos de seguridad

En RHEL 10 puede usarse:

```bash
dnf updateinfo list updates security
```

para listar actualizaciones de seguridad disponibles cuando el sistema y sus repositorios lo soportan.

## 13. Consultar una advisory concreta

Forma general:

```text
dnf updateinfo info ID_DE_ADVISORY
```

Sirve para revisar severidad, paquetes y CVE asociados antes de aplicar cambios.

## 14. Aplicar actualizaciones es otra fase

Órdenes como:

```text
dnf upgrade
dnf upgrade --security
```

**modifican el sistema**.

No las ejecutaremos en este laboratorio.

Antes de hacerlo en un equipo real debes considerar:

- compatibilidad;
- dependencias;
- espacio disponible;
- servicios afectados;
- kernel;
- ventana de mantenimiento;
- copia/rollback apropiado.

## 15. Kernel y reinicios

Una actualización puede instalar un kernel nuevo o actualizar bibliotecas utilizadas por procesos en ejecución.

Por eso:

```text
actualización instalada ≠ cambio plenamente activo en todos los procesos
```

Después de actualizaciones reales puede ser necesario revisar reinicios.

## 16. No automatizar actualizaciones sin política

RHEL puede automatizar actualizaciones mediante herramientas como `dnf-automatic`.

Eso puede ser apropiado en ciertos entornos, pero requiere una política:

- qué se actualiza;
- cuándo;
- cómo se prueba;
- cómo se notifica;
- qué ocurre si falla;
- cómo se recupera.

No activaremos timers de actualización en este módulo.

## 17. Estado general de systemd

Consulta:

```bash
systemctl --failed
```

muestra unidades que están en estado fallido.

Es una buena comprobación defensiva inicial.

## 18. Consultar una unidad concreta

```text
systemctl status NOMBRE.service
```

Primero identifica una unidad real.

No reinicies ni habilites servicios solo porque aparezcan mensajes que no comprendas.

## 19. Logs con `journalctl`

Consulta general del arranque actual:

```bash
journalctl -b
```

Puede contener mucha información.

No publiques logs completos sin revisar datos privados.

## 20. Prioridades de log

Puedes filtrar por prioridad:

```bash
journalctl -p warning..alert -b
```

Esto ayuda a concentrarse en eventos más importantes del arranque actual.

Una advertencia no prueba por sí sola un incidente de seguridad.

## 21. Logs de una unidad

```text
journalctl -u NOMBRE.service -b
```

Permite correlacionar eventos con una unidad concreta.

## 22. Buscar antes de concluir

Un log puede representar:

- configuración normal;
- fallo de hardware;
- error de software;
- permiso insuficiente;
- cambio administrativo;
- o actividad maliciosa.

No saltes directamente a la última explicación.

## 23. Puertos locales en escucha

En tu propio equipo:

```bash
ss -lntup
```

puede mostrar sockets locales en escucha y procesos cuando los permisos lo permiten.

Esta práctica es de **inventario local**, no de escaneo de otras máquinas.

## 24. Preguntas defensivas sobre un listener

Si aparece un puerto:

1. ¿qué proceso lo abrió?;
2. ¿qué servicio corresponde?;
3. ¿lo esperabas?;
4. ¿escucha solo en localhost o en interfaces externas?;
5. ¿es necesario?;
6. ¿está actualizado?;
7. ¿qué logs produce?

No detengas procesos por intuición.

## 25. Procesos

Consulta:

```bash
ps -ef
```

o una vista acotada:

```bash
ps -eo pid,user,comm,args --sort=user
```

La presencia de un proceso desconocido no demuestra que sea malicioso.

## 26. Permisos dentro del laboratorio

Busca archivos escribibles por cualquiera únicamente dentro del laboratorio:

```bash
find ~/linux-lab -type f -perm -0002 -print
```

Esto no modifica nada.

Si aparece un archivo, revisa por qué tiene ese permiso antes de cambiarlo.

## 27. `umask`

Consulta:

```bash
umask
```

`umask` influye en permisos iniciales de nuevos archivos/directorios.

No reemplaza una revisión explícita de permisos.

## 28. Auditoría: qué significa

Auditar no significa únicamente “buscar ataques”.

Significa reunir evidencia sobre:

- quién;
- qué;
- cuándo;
- dónde;
- estado anterior;
- cambio;
- resultado.

## 29. `auditd` como concepto

RHEL incluye un subsistema de auditoría que puede registrar eventos definidos por políticas.

Configurar reglas de auditoría es una tarea administrativa.

En este módulo solo comprobaremos si el servicio existe:

```bash
systemctl status auditd
```

No añadiremos reglas al sistema.

## 30. Evidencia mínima de laboratorio

Para una práctica técnica, registra:

```text
fecha
objetivo
equipo/laboratorio autorizado
estado inicial
comandos ejecutados
resultado esperado
resultado observado
archivos modificados
cómo volver al estado anterior
```

## 31. Preparar el laboratorio final

```bash
test -d ~/linux-lab && \
cd ~/linux-lab && \
mkdir -p modulo-35-defensa/evidencia && \
mkdir -p modulo-35-defensa/integridad && \
cd modulo-35-defensa && pwd
pwd
```

**Antes de ejecutar:** `cat > archivo <<'EOF'` utiliza un *here-document*: envía a `cat` las líneas siguientes hasta el delimitador `EOF`. Las comillas impiden expansiones de variables y comandos dentro del bloque. La redirección `>` **crea o sobrescribe** el destino; verifica que estás en el laboratorio y que el archivo no existe antes de continuar. Si ya existe, revísalo y edítalo con Vim o conserva una copia.

## 32. Crear archivo de evidencia inicial

```bash
cat > evidencia/registro.md <<'EOF'
# Laboratorio defensivo — Módulo 35

## Objetivo
Crear una línea base y detectar cambios controlados.

## Alcance
Solo ~/linux-lab/modulo-35-defensa

## Recuperación
Restaurar desde copia de laboratorio creada antes del cambio.
EOF
```

## 33. Crear datos de integridad

```bash
printf 'configuracion=original\n' > integridad/config.txt
printf 'dato estable\n' > integridad/datos.txt
```

## 34. Crear copia de recuperación

```bash
mkdir -p recuperacion
cp -a integridad recuperacion/integridad-inicial
```

Esta copia existe solo dentro del laboratorio.

## 35. Qué es una línea base

Una línea base representa un estado conocido contra el cual se comparan estados posteriores.

Ejemplo:

```text
archivo
tamaño
permisos
propietario
hash
fecha
```

## 36. Línea base con SHA-256

```bash
find integridad -type f -print0 \
  | sort -z \
  | xargs -0 sha256sum \
  > evidencia/baseline.sha256
```

Esta práctica calcula hashes solo de nuestros archivos de laboratorio.

## 37. Revisar la línea base

```bash
cat evidencia/baseline.sha256
```

Guarda también el estado:

```bash
stat integridad/config.txt integridad/datos.txt > evidencia/stat-inicial.txt
```

## 38. Verificar sin modificar

```bash
sha256sum -c evidencia/baseline.sha256
```

Si no hubo cambios, los archivos deben validar correctamente.

## 39. Crear un cambio controlado

```bash
printf 'configuracion=modificada\n' > integridad/config.txt
```

Este cambio afecta únicamente un archivo creado por la práctica.

## 40. Detectar el cambio

```bash
sha256sum -c evidencia/baseline.sha256
```

Ahora la comprobación debe informar que `config.txt` cambió.

Eso demuestra detección de integridad.

## 41. Hash distinto no explica la causa

Un hash diferente indica:

```text
el contenido ya no coincide
```

No indica automáticamente:

- quién cambió el archivo;
- por qué;
- si fue autorizado;
- si fue un ataque.

Para atribución necesitas evidencia adicional.

## 42. Recuperación del archivo de práctica

Primero revisa la copia:

```bash
cat recuperacion/integridad-inicial/config.txt
```

Después restaura únicamente el archivo de laboratorio:

```bash
cp recuperacion/integridad-inicial/config.txt integridad/config.txt
```

## 43. Verificar recuperación

```bash
sha256sum -c evidencia/baseline.sha256
```

El archivo debe volver a coincidir con la línea base.

## 44. Qué es AIDE

AIDE significa **Advanced Intrusion Detection Environment**.

Su modelo es:

```text
configuración
    ↓
base de datos inicial
    ↓
estado posterior del filesystem
    ↓
comparación
    ↓
informe de archivos añadidos/cambiados/eliminados
```

## 45. AIDE no bloquea cambios

AIDE es principalmente una herramienta de **detección de integridad**.

No impide por sí sola que un archivo cambie.

Su valor está en detectar diferencias respecto de una línea base.

## 46. Comprobar si AIDE existe

```bash
command -v aide
```

Si existe:

```bash
aide --version
```

Estas son consultas.

Si no está instalado, no lo instalaremos automáticamente en esta práctica.

## 47. Flujo administrativo AIDE en RHEL 10

En un sistema RHEL administrado, el flujo documentado incluye:

```text
instalar aide
configurar /etc/aide.conf
inicializar base
activar base inicial
ejecutar comprobaciones
actualizar la base después de cambios legítimos
```

Este flujo normalmente requiere privilegios administrativos.

## 48. Inicialización del sistema

La documentación de RHEL muestra:

```text
aide --init
```

para generar una base inicial conforme a `/etc/aide.conf`.

**No ejecutes esa inicialización sobre todo tu sistema como parte de este laboratorio.**

Puede recorrer una gran cantidad de archivos y escribir la base del sistema.

## 49. Comprobación AIDE

Una vez correctamente inicializado por un administrador:

```text
aide --check
```

compara el estado actual con la base configurada.

Los resultados pueden incluir:

- añadidos;
- eliminados;
- modificados.

## 50. Actualizar la base después de cambios legítimos

Instalar paquetes, aplicar actualizaciones o cambiar configuración de forma autorizada puede producir diferencias.

Después de verificar que esos cambios son legítimos, la base de AIDE debe actualizarse según el procedimiento de la distribución.

No actualices una línea base solo para hacer desaparecer una alerta.

## 51. Proteger la línea base

Si un atacante pudiera modificar al mismo tiempo:

- archivos del sistema;
- configuración de AIDE;
- base de referencia;
- binario de AIDE;

la confianza de la comprobación disminuiría.

Por eso Red Hat recomienda proteger base, configuración y herramienta en una ubicación segura cuando el nivel de riesgo lo justifique.

## 52. Falsos positivos y cambios legítimos

Una detección de AIDE puede corresponder a:

- actualización autorizada;
- edición administrativa;
- cambio normal de una aplicación;
- instalación;
- o modificación no autorizada.

La herramienta detecta diferencia; el analista interpreta contexto.

## 53. AIDE no reemplaza backups

AIDE puede decirte que algo cambió.

No necesariamente conserva la versión anterior.

Necesitas una estrategia de respaldo y recuperación aparte.

## 54. AIDE no reemplaza logs

Integridad responde principalmente:

```text
¿cambió?
```

Los logs pueden ayudar con:

```text
¿cuándo?
¿qué proceso?
¿qué usuario?
¿qué ocurrió alrededor?
```

Las fuentes se complementan.

## 55. Rutina defensiva básica semanal

Para un laboratorio propio:

1. revisar actualizaciones disponibles;
2. revisar `systemctl --failed`;
3. revisar eventos importantes del journal;
4. revisar listeners locales esperados;
5. verificar cambios de integridad;
6. documentar hallazgos;
7. corregir solo después de comprender;
8. verificar recuperación.

## 56. No reaccionar destruyendo evidencia

Ante algo inesperado no hagas inmediatamente:

```text
borrar archivos
limpiar logs
reiniciar múltiples servicios
reinstalar sin documentar
```

Primero registra el estado y preserva evidencia relevante.

## 57. No compartir evidencia sensible

Antes de subir a GitHub o enviar un informe, revisa que no contenga:

- tokens;
- contraseñas;
- direcciones privadas innecesarias;
- nombres de usuarios reales;
- rutas personales sensibles;
- claves SSH;
- cookies;
- logs con información privada.

## 58. Guardar evidencia en GitHub

Solo se versiona evidencia **sanitizada**.

Ejemplo de archivos apropiados:

```text
README.md
registro.md sin datos sensibles
script de consulta
ejemplo de baseline del laboratorio
```

No subas dumps completos del sistema.

## 59. Script defensivo de consulta

Crea `revision_basica.sh`:

```bash
#!/usr/bin/env bash

printf '%s\n' '=== Identidad ==='
id

printf '%s\n' '=== Unidades fallidas ==='
systemctl --failed --no-pager

printf '%s\n' '=== Espacio del laboratorio ==='
df -h "$HOME/linux-lab"

printf '%s\n' '=== Uso del laboratorio ==='
du -sh "$HOME/linux-lab"
```

No usa `sudo` ni modifica el sistema.

## 60. Validar el script

```bash
bash -n revision_basica.sh
```

Si ShellCheck está disponible:

```bash
shellcheck revision_basica.sh
```

Después:

```bash
bash revision_basica.sh
```

## 61. Errores frecuentes

| Error | Problema | Corrección |
|---|---|---|
| usar root para todo | aumenta impacto | usuario normal primero |
| actualizar sin revisar | puede afectar servicios/kernel | consultar y planificar |
| interpretar una alerta como ataque confirmado | falta contexto | correlacionar evidencia |
| borrar algo sospechoso inmediatamente | destruye evidencia | documentar primero |
| ejecutar AIDE `--init` sin entender configuración | puede escanear/escribir base del sistema | revisar alcance y configuración |
| actualizar baseline ante cualquier alerta | normaliza cambios no investigados | validar legitimidad primero |
| creer que AIDE es backup | no conserva versiones por sí solo | backup separado |
| publicar logs completos | puede filtrar información | sanitizar evidencia |
| detener servicio desconocido por intuición | puede romper sistema | identificar y documentar |
| automatizar remediación sin pruebas | amplifica errores | detectar primero, cambiar después |

## 62. Detección de error 1

Analiza:

```text
veo un proceso que no conozco → lo mato
```

Problema: desconocido no significa malicioso.

Primeros pasos:

```text
identificar proceso
ver propietario
ver servicio asociado
revisar logs
consultar documentación
```

## 63. Detección de error 2

Analiza:

```text
AIDE reporta 200 cambios después de una actualización → intrusión confirmada
```

Problema: una actualización legítima también modifica archivos.

Debes correlacionar con:

- transacción de paquetes;
- fecha/hora;
- advisories;
- logs;
- cambios autorizados.

## 64. Detección de error 3

Analiza:

```text
hay actualizaciones → dnf upgrade -y inmediatamente
```

Problema: aplicar sin revisión elimina una fase importante de gestión del cambio.

En este nivel:

```text
consultar → revisar → planificar → aplicar → verificar
```

## 65. Proyecto final del núcleo

Crea una carpeta:

```text
~/linux-lab/modulo-35-defensa/proyecto-final/
```

Debe contener:

- `README.md`;
- `revision_basica.sh`;
- `evidencia/baseline.sha256` de archivos de práctica;
- explicación de un cambio controlado;
- detección del cambio;
- procedimiento de recuperación;
- resultado después de restaurar.

## 66. README del proyecto final

Debe responder:

```text
¿qué sistema/laboratorio se usó?
¿cuál era el objetivo?
¿qué se consultó?
¿qué se modificó?
¿qué evidencia se guardó?
¿cómo se detectó el cambio?
¿cómo se recuperó?
¿qué comandos NO se ejecutaron por riesgo?
```

## 67. Criterio de aprobación

El proyecto se considera correcto si:

1. todo ocurre en laboratorio autorizado;
2. no requiere `sudo` para la práctica principal;
3. no borra logs;
4. no toca `/etc`;
5. no cambia servicios;
6. crea una línea base;
7. detecta un cambio controlado;
8. restaura el archivo;
9. vuelve a verificar;
10. no contiene secretos;
11. puede guardarse en GitHub con un commit pequeño.

## 68. Commit recomendado

Cuando el ejercicio esté revisado:

```text
linux: laboratorio final de integridad y defensa
```

Antes de guardarlo:

```bash
git status
git diff
git diff --staged
```

y confirma que no hay información sensible.

## 69. Mini evaluación

1. ¿mínimo privilegio significa usar root siempre? A) Sí B) No
2. ¿`sudo -l` consulta tus autorizaciones? A) Sí B) No
3. ¿`dnf check-update` instala automáticamente paquetes? A) Sí B) No
4. ¿un estado `100` de `dnf check-update` significa que hay actualizaciones disponibles? A) Sí B) No
5. ¿un estado `1` de `dnf check-update` representa un error? A) Sí B) No
6. ¿aplicar actualizaciones puede afectar kernel o servicios? A) Sí B) No
7. ¿`systemctl --failed` sirve para revisar unidades fallidas? A) Sí B) No
8. ¿una advertencia del journal prueba por sí sola un ataque? A) Sí B) No
9. ¿`ss -lntup` puede ayudar a inventariar listeners locales? A) Sí B) No
10. ¿un hash distinto demuestra quién cambió el archivo? A) Sí B) No
11. ¿AIDE usa una base de referencia? A) Sí B) No
12. ¿AIDE impide todos los cambios? A) Sí B) No
13. ¿cambios legítimos pueden generar diferencias en AIDE? A) Sí B) No
14. ¿debes actualizar la baseline sin investigar una alerta? A) Sí B) No
15. ¿AIDE reemplaza un sistema de backups? A) Sí B) No
16. ¿la evidencia debe sanitizarse antes de GitHub? A) Sí B) No
17. ¿una defensa responsable incluye recuperación? A) Sí B) No

## 70. Registro de aprendizaje

```text
Mínimo privilegio significa:
`sudo -l` sirve para:
`dnf check-update` sirve para:
Estado 0 de `dnf check-update` significa:
Estado 100 de `dnf check-update` significa:
Estado 1 de `dnf check-update` significa:
¿Por qué no debo tratar todo estado no-cero como error?:
`systemctl --failed` sirve para:
`journalctl` sirve para:
`ss -lntup` sirve para:
Una línea base es:
`sha256sum -c` sirve para:
AIDE es:
`aide --init` conceptualmente hace:
`aide --check` conceptualmente hace:
¿por qué cambia AIDE después de updates?:
¿por qué AIDE no es un backup?:
¿qué evidencia debo guardar?:
¿cómo recupero un cambio?:
Algo que todavía confundo:
Estado: EN APRENDIZAJE / PRACTICADO
```

## 71. Puerta de dominio

Para considerar este módulo **DOMINADO** deberás poder en más de una ocasión:

1. explicar mínimo privilegio con tus palabras;
2. separar consulta de modificación administrativa;
3. revisar actualizaciones sin aplicarlas automáticamente;
4. interpretar un listener local sin asumir que sea malicioso;
5. crear una línea base de integridad;
6. detectar un cambio controlado;
7. restaurar y volver a verificar;
8. explicar el modelo de AIDE;
9. distinguir detección, evidencia y recuperación;
10. producir un informe sanitizado y versionarlo sin secretos.

## 72. Fuentes y límites

Clasificación y estado de los enlaces de esta sección: [catálogo de fuentes](06-catalogo-fuentes.md) (jerarquía E04, comprobación del 9 de octubre de 2026).

Fuentes principales:

- iproute2 upstream (origen de `ss`): https://git.kernel.org/pub/scm/network/iproute2/iproute2.git/
- AIDE (proyecto original): https://aide.github.io/
- systemd upstream (manuales originales de `systemctl` y `journalctl`): https://github.com/systemd/systemd/tree/main/man
- Las guías oficiales RHEL y DNF siguientes respaldan los procedimientos específicos de distribución.
- Red Hat Enterprise Linux 10 — Security hardening: https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/
- RHEL 10 — Checking integrity with AIDE: https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/checking-integrity-with-aide
- RHEL 10 — Managing sudo access: https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/managing-sudo-access
- DNF Project — Command Reference, `check-update`: https://dnf.readthedocs.io/en/latest/command_ref.html#check-update-command
- RHEL 10 — Managing software with DNF: https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_software_with_the_dnf_tool/updating-rhel-content
- RHEL 10 — Managing and monitoring security updates: https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/risk_reduction_and_recovery_operations/managing-and-monitoring-security-updates
- systemd — `systemctl`, `journalctl`: https://www.freedesktop.org/software/systemd/man/latest/
- iproute2 — `ss(8)`: https://man7.org/linux/man-pages/man8/ss.8.html
- GNU Coreutils — `sha256sum`: https://www.gnu.org/software/coreutils/manual/coreutils.html

Puntos verificados documentalmente:

- RHEL 10 recomienda gestionar `sudo` para permitir tareas administrativas específicas sin iniciar sesión directamente como root;
- `dnf check-update` lista actualizaciones disponibles; DNF documenta estado `0` si no hay actualizaciones, `100` si hay actualizaciones y `1` si ocurre un error; RHEL permite consultar advisories de seguridad con `dnf updateinfo`;
- `dnf upgrade --security` instala actualizaciones de seguridad y por tanto es una operación modificadora, no una consulta;
- AIDE crea una base de datos de archivos y luego compara el estado actual para detectar diferencias;
- RHEL documenta `aide --init` para inicializar la base y `aide --check` para realizar comprobaciones;
- después de cambios legítimos, como actualizaciones de software, la base de AIDE debe actualizarse tras validar esos cambios;
- Red Hat recomienda proteger la base/configuración de AIDE cuando el nivel de seguridad lo requiera;
- una detección de integridad no sustituye copias de respaldo ni análisis de logs.

Se posponen para itinerarios posteriores de administración/ciberseguridad defensiva:

- reglas avanzadas de Audit;
- SELinux en profundidad;
- OpenSCAP;
- SCAP Security Guide;
- hardening CIS/STIG;
- gestión centralizada de logs;
- SIEM;
- respuesta a incidentes forense;
- gestión de vulnerabilidades a escala;
- automatización de remediación;
- políticas AIDE complejas;
- administración empresarial de sudo;
- EDR y monitoreo de endpoints.

**Estado de la lección:** redactada y revisada documentalmente contra RHEL 10 y documentación oficial de las herramientas utilizadas. La práctica es local, defensiva, reversible y no requiere privilegios administrativos.

## 73. Cierre del núcleo v3

Con este módulo quedan redactados los **35 módulos del núcleo** del Manual Maestro de Linux y Shell Scripting — Edición 2026 v3.

Esto significa:

```text
contenido redactado ≠ contenido dominado
```

Las prácticas del estudiante todavía deben ejecutarse, explicarse y revisarse durante las clases.

Siguiente fase editorial:

> **auditoría transversal completa de los Módulos 1–35, corrección de inconsistencias, referencias cruzadas, seguridad, progresión pedagógica y preparación de edición consolidada.**

> **Actualización:** esta auditoría se realizó el 8 de octubre de 2026. Ver [03 — Auditoría transversal completa v3](03-auditoria-transversal-completa-v3-2026-10-08.md).

---

**Fin del núcleo v3.** [← Módulo 34 — Almacenamiento: `lsblk`, `df`, `du`, montaje y `fstab`](modulo-34-almacenamiento-lsblk-df-du-montaje-fstab.md) · [Volver al índice](README.md)
