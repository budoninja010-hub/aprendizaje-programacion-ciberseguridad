# Registro de auditoría y fuentes — v3, primera entrega

[Índice](00-indice-arquitectura.md) · [Módulo 1](modulo-01-gnu-linux-kernel-distribuciones.md)

Fecha editorial: 6 de octubre de 2026. Alcance: arquitectura, primer módulo y decisiones de integración del informe. No constituye una auditoría de capítulos aún no escritos ni de todos los libros que NotebookLM menciona.

## 1. Resumen ejecutivo

Se revisaron la v2 alojada en GitHub y el archivo adjunto «Markdown pegado.md», cuyo encabezado es «Informe Maestro de Investigación y Auditoría». Se conserva la propuesta de 35 módulos, el aprendizaje gradual y el laboratorio personal. Se sustituyen afirmaciones absolutas por explicaciones que distinguen versión, distribución, contexto sintáctico y límites de seguridad.

La v2 es una base breve de 15 módulos numerados del 0 al 14. La v3 desarrolla una arquitectura más amplia; esta entrega incluye solo el primer módulo completo. No se copian los capítulos restantes de v2 para aparentar una migración terminada.

La v2 se identificó antes de trabajar mediante su blob Git `8dc703ec2dfd5aa1023bc7961085794a9d29fdf4`. No se solicita actualizarla ni eliminarla. La creación remota de esta entrega se limita a tres archivos nuevos bajo `linux/manuales/v3/`.

## 2. Evidencia y límites

- **Contenido inspeccionado directamente:** texto completo del informe adjunto y contenido de la v2; páginas oficiales recuperables y resultados indexados de documentación oficial.
- **No disponible para cotejo:** los PDF individuales del inventario de NotebookLM y una exportación completa de sus 26 supuestas fuentes. No se certifican esos archivos ni sus versiones por el nombre.
- **Acceso web parcial:** varias aperturas directas de GNU y la wiki Debian fallaron. Se contrastaron mediante resultados indexados del dominio oficial y, cuando se obtuvo, documentación oficial alternativa. Esto no equivale a haber leído completos todos esos manuales.
- **Versiones:** Coreutils 9.11 se corrobora con el anuncio oficial y la documentación indexada. No se afirma que sea la última versión disponible ni la instalada en el equipo del estudiante.
- **Ejecución:** la revisión de comandos es documental. La consulta local de distribuciones WSL devolvió acceso denegado; no se ejecutó la práctica en Linux ni se cambió la configuración del estudiante. Su validación práctica queda pendiente.

## 3. Hallazgos CRÍTICOS del informe

Se usa CRÍTICO cuando una generalización puede inducir una práctica insegura. Las correcciones siguientes se aplican como reglas editoriales de v3; no representan capítulos técnicos ya desarrollados.

| Ubicación y fragmento | Problema y por qué importa | Corrección y evidencia | Estado |
|---|---|---|---|
| §19.C: `trap` garantiza eliminar el temporal «independientemente» de la finalización | Promete una garantía falsa; puede dejar datos sensibles | No hay limpieza garantizada ante SIGKILL o apagado abrupto. Comprobar creación del temporal y diseñar salida y limpieza; no copiar el ejemplo como receta universal. [Señales de Linux](https://man7.org/linux/man-pages/man7/signal.7.html) | corregir: regla incorporada al M29 |
| §15: riesgo y privilegios asignados al nombre del programa | Una consulta y una modificación con el mismo programa pueden tener consecuencias muy distintas | Evaluar orden, opciones, objetivo y permisos. No declarar `systemctl` siempre privilegiado ni todas las búsquedas inocuas. Arquitectura §6 exige evaluación por operación | corregir: aplicado al contrato editorial |
| §18: `pwd` y `ls` tratados como protección suficiente | No validan automáticamente destinos absolutos, enlaces ni expansiones | Verificar también objetivo, tipo y alcance; detenerse si falla una orden. La carpeta del laboratorio no aísla el sistema | corregir: aplicado a arquitectura y M1 |

## 4. Hallazgos IMPORTANTES y decisiones

| ID · Ubicación / fragmento | Problema y relevancia | Redacción o decisión v3; evidencia | Estado |
|---|---|---|---|
| A01 · §1–3: Coreutils 9.12 | Atribución no sustentada al PDF; afecta trazabilidad | Usar **Coreutils 9.11** como referencia editorial. No atribuir versión al PDF ausente. [Anuncio oficial 9.11](https://lists.gnu.org/archive/html/info-gnu/2026-04/msg00006.html) | corregir: aplicado |
| A02 · §2–3: autor Eric Schildt | Error bibliográfico | Autor de *How Linux Works*: **Brian Ward**. La ficha de la tercera edición es de 2021. [Editorial](https://nostarch.com/howlinuxworks3) | corregir: aplicado |
| A03 · §7–9: reemplazo total de CFS en 6.6 | Simplifica la evolución y oculta el contexto de planificación | Linux comenzó la transición hacia **EEVDF en 6.6** dentro de la planificación equitativa; no se infiere desaparición de todos los mecanismos anteriores. [Kernel](https://docs.kernel.org/scheduler/sched-eevdf.html) | corregir: criterio para M13 y ampliación |
| A04 · §9 y §19.B: imponer `[[ ]]` | Confunde una elección de Bash con una regla universal | Enseñar `[ ]`/`test` para portabilidad POSIX y `[[ ]]` como construcción de Bash. Ambas son válidas en su contexto. [Bash](https://www.gnu.org/s/bash/manual/bash.html) | corregir: incluido en M26 |
| A05 · §19.A: todas las expansiones siempre entre comillas | Algunas posiciones tienen reglas distintas; las comillas pueden cambiar patrones | Citar expansiones usadas como argumentos de texto o rutas por defecto. Explicar excepciones en asignaciones y `[[ ]]`; citar el lado derecho de una comparación de patrón o de `=~` altera su interpretación. No citar indiscriminadamente un comodín destinado a expandirse. [Construcciones condicionales](https://www.gnu.org/software/bash/manual/html_node/Conditional-Constructs.html) | corregir: M24–27 y ejemplo de tilde en M1 |
| A06 · §11: UFW común por defecto a Debian/Ubuntu | Confunde familia con configuración concreta | Ubuntu documenta UFW como interfaz y su estado inicial deshabilitado. Debian documenta nftables como infraestructura predeterminada; eso no prueba reglas activas ni UFW instalado. [Ubuntu](https://ubuntu.com/server/docs/how-to/security/firewalls/) · [Debian](https://wiki.debian.org/nftables) | corregir: fichas separadas en M16 y M21 |
| A07 · §15: descripción ambigua de `rm` | Puede inducir selección errónea de una orden destructiva | `rm` sin opciones no elimina directorios; `rmdir` elimina directorios vacíos. GNU `rm -d` acepta directorios vacíos y `rm -r` recorre directorios. Enseñar primero distinción y verificación; no usar borrado en M1. [GNU rm](https://www.gnu.org/s/coreutils/manual/html_node/rm-invocation.html) | corregir: criterio de M6 |
| A08 · §7: enseñar exclusivamente systemd | Borra diversidad y casos de compatibilidad | Itinerario principal systemd; reconocer otros init y entornos sin gestor systemd activo. [systemd](https://systemd.io/) · [Debian Policy, sistemas alternativos](https://www.debian.org/doc/debian-policy/) | corregir: aplicado al índice |
| A09 · §16: Debian Policy como cumplimiento FSF | Confunde políticas técnicas con criterios de otra organización | Debian Policy define requisitos de la distribución y sus paquetes. No constituye certificación ni cumplimiento general de la FSF. [Alcance oficial](https://www.debian.org/doc/debian-policy/ch-scope.html) | corregir: aplicado |
| A10 · §1: RHEL 8 como referencia enterprise general | Una guía oficial puede ser válida solo para una versión | Usar RHEL 10 para prácticas destinadas a RHEL 10; conservar RHEL 8 si ese es el objeto de estudio. [Seguridad RHEL 10](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/index) | corregir: aplicado a arquitectura |
| A11 · §1–2 y §6: 26 fuentes frente a 16 entradas | No permite comprobar cobertura ni duplicados | El informe enumera 16 entradas, pero afirma analizar 26. No declarar inventario completo ni deduplicación realizada sin los originales | verificar: pendiente de exportación de fuentes |
| A12 · §2–3: capítulos 3 y 10 y supuesta obsolescencia de How Linux Works | Atribución no comprobada a archivos ausentes | No inferir edición ni tema por nombre del archivo. La tercera edición documentada incluye systemd; no calificar el libro completo de obsoleto. [Índice editorial](https://nostarch.com/howlinuxworks3) | verificar: pendiente de PDF y portada |
| A13 · §8: «inyección» en redirección con sudo | Nombra mal el mecanismo y sugiere una solución universal | La shell procesa la redirección en su propio contexto de permisos. No es por sí mismo inyección. Enseñar mecanismos de escritura privilegiada solo con alcance y riesgos explícitos; no convertir `sudo tee` en receta automática. [Bash, redirecciones](https://www.gnu.org/s/bash/manual/bash.html) | corregir: criterio para M8 y M12 |
| A14 · §10: expansión sin comillas implica inyección de comandos | Mezcla separación de argumentos con evaluación de código | La expansión ordinaria no reinterpreta automáticamente su contenido como sintaxis de shell. Separar riesgos de división, comodines, opciones y evaluación explícita. [Bash, expansiones](https://www.gnu.org/s/bash/manual/bash.html) | corregir: criterio para M24 y M29 |

No se trasladan sin revisión otras afirmaciones del informe, como valores predeterminados de AppArmor, reglas de auditd supuestamente preconfiguradas, comportamiento universal de comodines ocultos o una fecha de retirada de iptables-nft. Requieren versión, entorno y evidencia específica al redactar el módulo correspondiente.

EEVDF y PREEMPT_RT no se presentan como dos alternativas equivalentes entre las que deba elegirse una tasa de adopción: describen aspectos diferentes. El informe no aporta evidencia suficiente para sus proyecciones. Se difiere esa investigación hasta la ampliación avanzada.

## 5. Mejoras opcionales

**Nivel: MEJORA OPCIONAL. Ubicación: formato de v2.** Su estructura de títulos en texto plano dificulta navegar. La v3 utiliza encabezados Markdown, tablas e hipervínculos internos. Estado: conservar el original y aplicar el formato solo a los archivos nuevos.

**Nivel: MEJORA OPCIONAL. Ubicación: futuras entregas.** Una compilación PDF facilitaría impresión, pero duplicaría trabajo antes de completar los módulos. Estado: verificar la necesidad al alcanzar una fase completa; no se genera una falsa edición integral.

## 6. Registro de fuentes usadas en esta entrega

Estas son las referencias efectivamente usadas para esta entrega, no el inventario de NotebookLM. Las fuentes oficiales indexadas pueden corresponder a una captura anterior al día de consulta. No se asignan puntuaciones de calidad numéricas sin criterios medibles.

| Fuente | Uso y alcance de verificación |
|---|---|
| [GNU Coreutils: anuncio 9.11](https://lists.gnu.org/archive/html/info-gnu/2026-04/msg00006.html) | Anuncio indexado: referencia 9.11, publicada el 20 de abril de 2026 |
| [GNU Coreutils: manual](https://www.gnu.org/s/coreutils/manual/coreutils.html) | Referencia indexada del conjunto de utilidades; no cotejo de un PDF de NotebookLM |
| [GNU: uname](https://www.gnu.org/software/coreutils/manual/html_node/uname-invocation.html) | Documentación indexada para información de núcleo en M1 |
| [GNU: mkdir](https://www.gnu.org/software/coreutils/manual/html_node/mkdir-invocation.html) | Documentación indexada para creación de carpetas en M1 |
| [GNU: rm](https://www.gnu.org/s/coreutils/manual/html_node/rm-invocation.html) | Documentación recuperada en búsqueda, distinción entre opciones de borrado |
| [GNU Bash: manual](https://www.gnu.org/s/bash/manual/bash.html) | Documentación indexada para reglas de shell; versión instalada no comprobada |
| [GNU Bash: condicionales](https://www.gnu.org/software/bash/manual/html_node/Conditional-Constructs.html) | Contexto de patrones, expresiones y comillas; acceso mediante índice de búsqueda |
| [GNU Bash: expansión de tilde](https://www.gnu.org/s/bash/manual/html_node/Tilde-Expansion.html) | Referencia indexada para rutas del laboratorio |
| [GNU: terminología](https://www.gnu.org/prep/maintain/html_node/GNU-and-Linux.html) | Distinción conceptual GNU y Linux, consultada en búsqueda |
| [Debian: acerca de](https://www.debian.org/intro/about) | Página oficial recuperada, núcleo y distribución |
| [systemd: os-release](https://github.com/systemd/systemd/blob/main/man/os-release.xml) | Fuente oficial indexada para identidad del sistema; no prueba de systemd activo |
| [Kernel: EEVDF](https://docs.kernel.org/scheduler/sched-eevdf.html) | Página oficial recuperada, transición a partir de 6.6 |
| [No Starch Press: How Linux Works, tercera edición](https://nostarch.com/howlinuxworks3) | Página editorial recuperada: autor, edición e índice; no acceso a PDF completo |
| [Ubuntu: cortafuegos](https://ubuntu.com/server/docs/how-to/security/firewalls/) | Página recuperada: UFW y estado inicial; no generalización a Debian |
| [Debian: nftables](https://wiki.debian.org/nftables) | Resultado oficial indexado; apertura directa devolvió 403 |
| [Debian Policy: alcance](https://www.debian.org/doc/debian-policy/ch-scope.html) | Página oficial recuperada: políticas de distribución y paquetes |
| [systemd](https://systemd.io/) | Sitio oficial recuperado; referencia principal de servicios |
| [RHEL 10: Security hardening](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/index) | Guía oficial recuperada; selección por versión, sin validar aún sus procedimientos |
| [Linux man-pages: signal(7)](https://man7.org/linux/man-pages/man7/signal.7.html) | Página recuperada para límites de señales y limpieza |

## 7. Validación y pendientes

Aspectos conservados: enseñanza desde cero, explicación paso a paso, ejercicios pequeños, usuario normal, carpeta de laboratorio, revisión previa y protección de secretos. La evaluación distingue redacción terminada, práctica ejecutada y aprendizaje demostrado.

Comprobaciones de esta entrega: coherencia entre los 35 títulos y sus resultados; correspondencia de los enlaces internos; revisión de los bloques de órdenes y de sus advertencias; revisión de información sensible antes de guardar. Los bloques de M1 son ejemplos de una lección, no un script para pegar y ejecutar de principio a fin.

Pendientes reales:

1. Identificar con el estudiante su distribución, shell y entorno de práctica; ejecutar M1 y revisar resultados.
2. Obtener los originales si se necesita certificar el inventario o las ediciones que NotebookLM cita. Esto no impide usar las fuentes oficiales independientes de esta entrega.
3. Redactar y revisar los módulos 2–35 por entregas; comprobar versiones y ejemplos al hacerlo.
4. Validar en laboratorios adecuados los procedimientos posteriores de servicios, redes y seguridad; no basta una revisión textual.

**Estado final de esta primera entrega: APTO CON MEJORAS MENORES**, como material introductorio con revisión documental y limitaciones declaradas. El manual completo permanece en elaboración; no se afirma una validación práctica ni editorial integral.
