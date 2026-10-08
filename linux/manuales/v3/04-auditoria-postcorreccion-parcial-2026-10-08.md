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
