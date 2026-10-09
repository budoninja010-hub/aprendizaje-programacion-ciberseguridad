# Guía permanente de trabajo

Esta guía define cómo organizar todo el material de aprendizaje relacionado con programación, Linux, redes y ciberseguridad.

## Ruta principal de aprendizaje

1. Python
2. Java y Programación Orientada a Objetos
3. Linux
4. Redes
5. Ciberseguridad ética

La progresión debe ser gradual. No se avanzará a contenidos complejos si los fundamentos previos no están suficientemente dominados.

## Dónde guardar cada material

### Python
- Apuntes de clase: `python/clases/`
- Ejercicios cortos: `python/ejercicios/`
- Mini evaluaciones: `python/examenes/`
- Proyectos completos: `python/proyectos/`

### Java
- Fundamentos: `java/ejercicios/`
- POO: `java/poo/`
- Proyectos: `java/proyectos/`

### Linux
- Manual Maestro de Linux: `linux/manuales/` (la versión vigente es `v3/`)
- Comandos y notas: `linux/comandos/`
- Bash: `linux/bash/`
- Prácticas: `linux/laboratorios/`

### Redes
- Conceptos, ejercicios y apuntes: `redes/`

### Ciberseguridad
- Fundamentos: `ciberseguridad/fundamentos/`
- Defensa y Blue Team: `ciberseguridad/blue-team/`
- Seguridad web: `ciberseguridad/web-security/`
- CTF y laboratorios con autorización: `ciberseguridad/laboratorios-autorizados/`

### Notas y proyectos integradores
- Notas generales: `notas/`
- Proyectos que mezclen varias áreas: `proyectos/`

### Manuales
- Cada área guarda sus manuales y revisiones en `<área>/manuales/`.
- Las versiones anteriores se conservan; nunca se sobrescriben.

## Reglas de guardado

1. No dejar archivos de aprendizaje sueltos en la raíz salvo documentación general.
2. Cada ejercicio nuevo debe ir en la carpeta de su tecnología y categoría.
3. Usar nombres descriptivos, por ejemplo:
   - `variables_01.py`
   - `condicionales_02.py`
   - `clases_objetos_01.java`
   - `permisos_archivos_linux.md`
4. Cada proyecto relevante debe incluir un `README.md` con:
   - objetivo;
   - requisitos;
   - cómo ejecutarlo;
   - conceptos practicados;
   - errores y correcciones importantes.
5. No guardar contraseñas, tokens, claves API, claves privadas ni credenciales.
6. No subir datos personales o información sensible.
7. En ciberseguridad, trabajar únicamente con sistemas propios, CTF, laboratorios o entornos con autorización explícita.
8. Conservar el historial de Git como registro del progreso: las correcciones importantes deben quedar documentadas mediante commits claros.

## Convención para commits

Formato: `área: verbo en infinitivo + qué cambia`, en minúsculas y sin punto final.

- `python:`, `java:`, `linux:`, `redes:`, `security:` → material de esa área.
- `docs:` → documentación general del repositorio.
- `chore:` → mantenimiento (`.gitignore`, estructura de carpetas).

Si el cambio es una corrección, dilo con el verbo: `python: corregir condición del ejercicio if`.

Ejemplos:
- `python: agregar ejercicio de variables`
- `python: corregir condición del ejercicio if`
- `linux: añadir resumen de permisos`
- `docs: actualizar ruta de aprendizaje`

> Nota: una versión anterior de esta guía proponía prefijos `feat:`/`fix:`. Se unificó con el formato por área porque es el que usa todo el historial.

## Objetivo

Mantener un repositorio limpio, seguro y útil como portafolio de aprendizaje, donde pueda verse claramente la evolución desde fundamentos hasta proyectos más avanzados.
