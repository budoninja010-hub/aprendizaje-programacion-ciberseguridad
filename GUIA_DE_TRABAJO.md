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
- Ejercicios cortos: `python/ejercicios/`
- Mini evaluaciones: `python/examenes/`
- Proyectos completos: `python/proyectos/`

### Java
- Fundamentos: `java/ejercicios/`
- POO: `java/poo/`
- Proyectos: `java/proyectos/`

### Linux
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

## Convención recomendada para commits

- `feat:` nueva práctica o proyecto
- `fix:` corrección de código
- `docs:` documentación o apuntes
- `test:` pruebas
- `refactor:` mejora interna sin cambiar funcionalidad
- `chore:` mantenimiento del repositorio

Ejemplos:
- `feat: agregar ejercicio de variables en Python`
- `fix: corregir condición del ejercicio if`
- `docs: añadir resumen de permisos Linux`

## Objetivo

Mantener un repositorio limpio, seguro y útil como portafolio de aprendizaje, donde pueda verse claramente la evolución desde fundamentos hasta proyectos más avanzados.
