# Auditoría post-corrección — Primera pasada parcial

**Fecha:** 2026-10-08. **Estado:** EN CURSO; no equivale a aprobación final.

## Alcance realizado

- Se consultaron M13, M19, M21, M25, M27, M30, M34, M35 y el informe transversal anterior.
- Se constató la presencia de referencias upstream en M19/M21/M30/M34/M35, sin verificar aún HTTP ni la correspondencia de cada enlace con cada afirmación.
- Se corrigió la numeración duplicada de la pregunta 9 y se amplió la ficha de aprendizaje sobre load average en M13. Commit `8871140614ce9c9f6badce3bac75b97785c09119`.
- No se detectaron encabezados numerados exactamente duplicados en M19/M21/M30/M34/M35.

## Dictamen provisional

**NO CONGELAR LA EDICIÓN FINAL.** Falta lectura íntegra de los 35 módulos, validación de enlaces y pruebas de los ejercicios. No se afirma que las prácticas se hayan ejecutado en el equipo del estudiante.

## Pendientes

1. Verificar enlaces oficiales individualmente y relación fuente-afirmación.
2. Revisar numeración de evaluaciones y fichas en módulos modificados.
3. Revisar pertinencia y redundancias del anexo M1–M4.
4. Revisar calendario, suspensión y cambios de reloj en M30.
5. Revisar afirmaciones de versión fechadas en M16/M32 y bibliografía.
6. Continuar la auditoría transversal del resto de módulos.

**Revisión documental ≠ ejecución práctica ≠ dominio del estudiante.**

## Segunda pasada — consistencia de evaluaciones

- **M13:** preguntas consecutivas 1–12 tras el commit correctivo `88711406`.
- **M25:** mini evaluación consecutiva 1–14; la pregunta 11 comienza con «Por defecto» y debe incluirse al contar, aunque no comience con «¿».
- **M27:** mini evaluación consecutiva 1–17; se mantienen las preguntas nuevas sobre `-e` y `-L`.
- **M30:** mini evaluación consecutiva 1–18; la pregunta 7 empieza «si DOM...» y debe incluirse al contar.
- **M35:** mini evaluación consecutiva 1–17. Hay otras listas numeradas anteriores en el módulo; la numeración reiniciada en una sección diferente no es un defecto.

**Resultado de este alcance:** no se identificó un nuevo error de numeración en las cinco mini evaluaciones revisadas. El análisis no valida automáticamente la corrección de las respuestas ni las evaluaciones de los otros treinta módulos.

## Tercera pasada — comprobación directa de fuentes originales (2026-10-08)

Se abrieron y consultaron las páginas originales de: espejo público de iproute2 (GitHub), proyecto Netfilter/nftables, repositorio Cronie, repositorio util-linux, sitio AIDE y archivo upstream `systemd.timer.xml`. Las seis referencias fueron accesibles durante la consulta. **Esto no equivale a verificar todos los enlaces del manual ni cada afirmación técnica.**

**Hallazgos y correcciones:**
- M19: el propio repositorio GitHub de iproute2 se presenta como espejo de solo publicación; se corrigió la etiqueta para distinguirlo del repositorio principal en kernel.org. Commit `f7c4e00e73138755ed98aac6570de74fbe00948a`.
- M21: la URL `https://wiki.nftables.org/` aparecía dos veces en la bibliografía; se retiró la repetición. Commit `48982c1cc34e82ff202088ff4b985af5401675f3`.

**Pendiente:** revisión fuente-afirmación en cada módulo, enlaces restantes y validación técnica de ejercicios.

## Cuarta pasada — matriz afirmación–fuente M19 y M21

**Alcance:** comparación del contenido actual de M19 y M21 con las referencias primarias ya registradas. Esta matriz es una comprobación de trazabilidad documental; no sustituye una prueba de ejecución ni una nueva lectura en línea de cada sección de las fuentes.

| Módulo y afirmación | Fuente original aplicable | Evaluación |
|---|---|---|
| M19 §7: bloques privados `10/8`, `172.16/12`, `192.168/16` y ausencia de unicidad global | RFC 1918, secciones 3 y 4: https://www.rfc-editor.org/rfc/rfc1918 | Coherente con la fuente normativa |
| M19 §7: las direcciones privadas pueden enrutarse internamente; NAT no forma parte obligatoria de RFC 1918 | RFC 1918: https://www.rfc-editor.org/rfc/rfc1918 | Coherente; NAT es un mecanismo adicional, no un requisito del RFC |
| M19 §§11–14: `ip link`, `ip address`, `-br` | iproute2 upstream: https://git.kernel.org/pub/scm/network/iproute2/iproute2.git/ y páginas `ip(8)`/`ip-address(8)` | Referencias pertinentes; comprobar opciones por versión instalada |
| M19 §§19–20: rutas y coincidencia de prefijos | iproute2 `ip-route(8)`: https://man7.org/linux/man-pages/man8/ip-route.8.html | Explicación introductoria válida; se posponen policy routing y métricas |
| M21 §§4–7: Netfilter, nftables, familias `ip`, `ip6`, `inet` | Netfilter: https://www.netfilter.org/projects/nftables/index.html y https://wiki.nftables.org/ | Referencias pertinentes para los conceptos |
| M21 §§13–16: UFW como interfaz de administración y comportamiento inicial documentado para Ubuntu | Ubuntu Security: https://documentation.ubuntu.com/security/security-features/network/firewall/ | Afirmación acotada a Ubuntu; no extender a otras distribuciones |
| M21 §§17–21: zonas, servicios y diferencias runtime/permanent | firewalld: https://firewalld.org/documentation/ y RHEL 10: https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_firewalls_and_packet_filters/ | Referencias pertinentes; los cambios runtime y permanent se mantienen solo conceptuales |

**Resultado provisional:** no se detectó contradicción técnica evidente en las afirmaciones examinadas. No se declara que cada enlace específico o cada versión se haya comprobado exhaustivamente. Las prácticas continúan siendo locales, de consulta y sin cambios de configuración.

**Siguiente revisión:** contraste puntual de M30 y M34, más revisión de las afirmaciones de versión de M16 y M32.

## Quinta pasada — contraste upstream de M30 y M34

**Fecha:** 2026-10-08. Se consultó directamente `systemd.timer.xml` upstream y el manual `findmnt(8)` de util-linux (árbol upstream y copia man7).

| Afirmación del manual | Referencia contrastada | Dictamen |
|---|---|---|
| M30 §37: `Persistent=true` guarda el momento de la última activación del servicio, recupera si hubo al menos un vencimiento de `OnCalendar=` mientras estuvo inactivo y puede estar sujeto a `RandomizedDelaySec=` | https://github.com/systemd/systemd/blob/main/man/systemd.timer.xml | Coincide con la documentación original |
| M30 §37: durante suspensión/hibernación el reloj de tiempo real avanza y varios vencimientos de un mismo timer de calendario durante una suspensión continua producen una sola activación | Misma referencia `systemd.timer.xml` | Coincide con la documentación original; no confundir con apagado |
| M30 §38: `AccuracySec=` tiene valor predeterminado de un minuto | Misma referencia | Coincide con la documentación original |
| M34 §§44–48: `findmnt --verify --verbose --tab-file fstab-practica` permite comprobar una tabla alternativa | https://kernel.googlesource.com/pub/scm/utils/util-linux/util-linux/+/refs/heads/master/misc-utils/findmnt.8.adoc y https://man7.org/linux/man-pages/man8/findmnt.8.html | Combinación de opciones documentada upstream |
| M34 §§45–50: la práctica usa directorios y tabla de usuario, no edita `/etc/fstab` ni monta dispositivos | Lectura del contenido del módulo M34 | Alcance pedagógico seguro en el texto; ejecución real no comprobada |

**Observación:** `findmnt --verify` comprueba parseabilidad/usabilidad de la tabla, pero no garantiza que un futuro montaje sea seguro ni que el arranque funcione en todos los entornos. Se mantiene fuera de la práctica `mount -a`.

**Resultado:** sin contradicciones técnicas detectadas en las afirmaciones examinadas. Esta pasada no equivale a una auditoría completa de los módulos ni de todas sus fuentes. Próximos pendientes: versiones M16/M32, consistencia de referencias y revisión global.

## Sexta pasada — versiones fechadas M16/M32 (8 de octubre de 2026)

| Afirmación | Fuente original comprobada | Dictamen |
|---|---|---|
| M16: Debian 13 «trixie» estable | https://www.debian.org/releases/ ; anuncio 13.7: https://lists.debian.org/debian-announce/2026/msg00009.html | Confirmado; 13.7 publicada el 12-09-2026 |
| M16: Ubuntu 26.04 LTS | https://documentation.ubuntu.com/release-notes/26.04/ | Confirmado; publicada el 23-04-2026 |
| M16: RHEL 10 | https://access.redhat.com/articles/red-hat-enterprise-linux-release-dates | Confirmado; 10.2 figura publicada en mayo de 2026 |
| M32: rsync 3.5.1 | https://rsync.samba.org/ ; https://lists.samba.org/archive/rsync/2026-September/033395.html | Confirmado como versión upstream publicada el 21-09-2026 |

**Mejoras guardadas:** M16 incorpora fecha de corte y referencias a las versiones puntuales (commit `af9f1370769130f59496e855edf48929ac268cb3`); M32 incorpora el anuncio original y fecha de verificación (commit `4d68c2a792fee321a2f74332f4c901c0e0d55116`). Se preservaron explicaciones anteriores. **Pendiente:** revisión editorial global y validación de todos los enlaces.

## Séptima pasada — normalización editorial de M1–M4 (9 de octubre de 2026)

Se aplicó el hallazgo E01 de la auditoría transversal. Cambios: encabezados alineados con el contrato de M5–M35; anexo integrado en «Fuentes y límites de esta lección»; pie de navegación movido al final en M2–M4; ficha de registro añadida en M2. Una comprobación automática confirmó que ninguna línea de contenido previo se eliminó. Los enlaces internos de los 35 módulos siguen resolviendo y todos los bloques de código cierran.

**Pendiente:** E04 y E05, lectura íntegra de los módulos no revisados en pasadas anteriores, verificación de enlaces externos y sincronización con Google Drive.

## Octava pasada — E02, E04, E05 y enlaces externos (9 de octubre de 2026)

**E02 (README con historial acumulado):** ya resuelto el 9 de octubre al convertir el README en índice y trasladar el historial a [05-historial-entregas.md](05-historial-entregas.md).

**E04 (jerarquía de fuentes):** aplicado mediante el [catálogo de fuentes](06-catalogo-fuentes.md). Clasifica los 182 enlaces externos de los módulos en los cinco niveles de la auditoría. La sección «Fuentes y límites» de los 35 módulos enlaza a ese catálogo con la misma frase. No se reordenaron las listas de fuentes dentro de cada módulo.

**Enlaces externos:** comprobados el 9 de octubre de 2026 desde un servicio externo (código de respuesta y título de la página). Resultado: 127 funcionan; 55 de los manuales de GNU quedaron **sin verificar** porque el servicio agotó sus créditos. Problemas corregidos:

| Módulo | Problema | Corrección |
|---|---|---|
| M22 | `vimhelp.org/reference_toc.txt.html` → 404 | `https://vimhelp.org/#reference_toc` |
| M35 | Enlace «Checking integrity with AIDE» abría la portada de *Security hardening* | Capítulo 7 `…/security_hardening/checking-integrity-with-aide` |
| M16 | `…/fedora-silverblue/` redirige | `…/en-US/atomic-desktops/` |

**E05 (fechas de verificación):** afirmaciones contrastadas con el texto de la fuente original el 9 de octubre de 2026.

| Afirmación | Fuente | Dictamen y acción |
|---|---|---|
| M06: GNU Coreutils 9.11 | Manual de Coreutils en gnu.org | **Desactualizado:** el manual documenta la 9.12. Se quitó «9.11» de cada enlace y se añadió una nota de vigencia |
| M31: GNU gzip 1.14 | Manual de gzip en gnu.org | **Desactualizado:** el manual documenta la 1.15 (3 de enero de 2026). Corregido y fechado |
| M13: libro de man-pages 6.17 | Listado de kernel.org | El PDF existe; la edición más reciente es la 6.19. Se añadió la nota |
| M25: GNU Bash 5.3 | Manual de Bash (edición del 18 de mayo de 2025) | Confirmado; fechado |
| M15: Fedora 41+ usa DNF5 | Fedora Wiki, cambio *SwitchToDnf5* («Targeted release: Fedora Linux 41») | Confirmado; enlace y fecha añadidos |
| M18: journal volátil por defecto en RHEL 10 | RHEL 10, capítulo 13 de *RHEL system roles* | Confirmado; fechado |
| M21: UFW deshabilitado por defecto en Ubuntu | Ubuntu security documentation — Firewall | Confirmado; fechado |

Las auditorías 02 y 03 citan Coreutils 9.11. No se modifican porque registran lo comprobado en su fecha.

**Pendiente:** verificar los 55 enlaces de GNU restantes, lectura íntegra de los módulos no revisados en pasadas anteriores, revisión visual del PDF y sincronización con Google Drive.

## Novena pasada — lectura íntegra de los módulos pendientes (9 de octubre de 2026)

**Alcance:** lectura completa de los 22 módulos que las pasadas anteriores no habían contrastado a fondo: M5–M12, M14, M15, M17, M18, M20, M22–M24, M26, M28, M29, M31 y M33.

**Comprobaciones automáticas sobre los 35 módulos:**

- 1120 bloques `bash` extraídos y analizados con `bash -n` (Bash 5.2) y ShellCheck 0.11.0. Los 7 errores de sintaxis son fragmentos explicativos intencionales; los avisos restantes corresponden a fragmentos sueltos o a ejemplos marcados como «Detección de error».
- Prácticas ejecutadas en carpetas temporales: permisos y `umask` (M12), scripts y CRLF (M23), `read`/`IFS`/`"$@"` (M24), `mktemp` + `trap`, `set -e`, `set -u` y `pipefail` (M29), `tar`/`gzip`/`xz` y `--keep-old-files` (M31), flujo Git (M33). Los resultados coincidieron con lo descrito, salvo lo indicado abajo.
- M20 se contrastó con `ssh(1)` y `ssh_config(5)` del repositorio original openssh-portable (commit `6a46ea6`, 9-oct-2026).

**Resultado:** 0 hallazgos críticos, 7 importantes y 15 mejoras opcionales. Todos aplicados.

| Id | Nivel | Módulo | Hallazgo | Acción |
|---|---|---|---|---|
| H1 | IMPORTANTE | M05 §7 | Prometía estudiar el sticky bit en M12, que lo pospone | Texto corregido: se pospone |
| H10 | IMPORTANTE | M11 §5 | Prometía estudiar el SGID de directorios en M12, que lo pospone | Texto corregido: se pospone |
| H5 | IMPORTANTE | M07 §18 | Ordenaba `tail -f` antes de crear el archivo | Orden corregido |
| H9 | IMPORTANTE | M10 §31 | «no necesariamente `app.log`» sugería una duda inexistente | Precisado |
| H14 | IMPORTANTE | M20 §10 | Con el valor por defecto, OpenSSH rechaza la conexión ante una host key cambiada; el texto solo mencionaba desactivar la contraseña | Precisado con `ssh_config(5)` |
| H17 | IMPORTANTE | M23 §44 | Ruta de guardado `linux/ejercicios/bash/` distinta de la del repositorio (`linux/bash/`) | Corregida |
| H22 | IMPORTANTE | M33 §52 | Siguiendo el orden, la Práctica A fallaba con «nothing added to commit» | Práctica en un repositorio nuevo |
| H2 | MEJORA | M31 §23, §28 | Órdenes con `cd` sin encadenar | Encadenadas con `&&` |
| H4 | MEJORA | M06 | Ejemplos con `rm`/`mv` antes de crear la carpeta de práctica | Aviso de lectura añadido |
| H6 | MEJORA | M07 §13 | Contradicción sobre `>` y sin comprobar el nombre | Redactado y con comprobación |
| H7 | MEJORA | M07 §22 | «20,000» | «20 000» |
| H8 | MEJORA | M08 §21 | `>` sin comprobación previa | Comprobación añadida |
| H11 | MEJORA | M11 §25 | Primer uso de `$(…)` sin explicar | Explicación breve y remisión a M24 |
| H12 | MEJORA | M15 §32 | Aviso de `apt` en tuberías no anticipado | Nota y alternativa `apt-cache search` |
| H13 | MEJORA | M17 §33 | Pedía `--all` sin mostrarlo | Orden completa |
| H15 | MEJORA | M20 §21 | Generación de clave duplicada con §41 | §21 marcada como explicación |
| H16 | MEJORA | M22 §20 | Nota de compatibilidad fuera de lugar | Movida tras §22 |
| H18 | MEJORA | M23, M33, M35 | Ejemplos de commit fuera del formato del repositorio | Alineados con `área: verbo + qué` |
| H19 | MEJORA | M24 §2–3 | Nombre real en ejemplos | Sustituido por «Ana» |
| H20 | MEJORA | M24, M26, M28, M29 | Prácticas sin nombre de archivo | Nombres indicados |
| H21 | MEJORA | M31 §35 | Conflicto `File exists` no anticipado | Aviso añadido |
| H23 | MEJORA | M33 | `pwd` duplicado y here-document explicado dos veces | Simplificado |

Un hallazgo provisional (bloque de M27 marcado como código) se descartó al comprobar que ya estaba marcado como texto.

**Pendiente:** verificar los 55 enlaces de GNU restantes, revisión visual del PDF y sincronización con Google Drive. La práctica real del estudiante sigue pendiente.
