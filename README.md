# Aprendizaje de Programación y Ciberseguridad

Repositorio privado para organizar ejercicios, prácticas, exámenes, apuntes y proyectos de aprendizaje en programación, Linux, redes y ciberseguridad ética.

## Ruta maestra de aprendizaje

La progresión principal será:

1. **Python**
   - Variables, tipos de datos, entrada/salida.
   - Condicionales y ciclos.
   - Funciones.
   - Listas, diccionarios y archivos.
   - Manejo de errores.
   - Programación orientada a objetos básica.
   - Proyectos pequeños.

2. **Java y Programación Orientada a Objetos**
   - Sintaxis y fundamentos.
   - Clases y objetos.
   - Encapsulación.
   - Herencia.
   - Polimorfismo.
   - Abstracción.
   - Colecciones y proyectos.

3. **Linux**
   - Terminal y sistema de archivos.
   - Permisos.
   - Procesos y servicios.
   - Paquetes.
   - Bash.
   - Administración básica.

4. **Redes**
   - Modelos OSI y TCP/IP.
   - IPv4/IPv6.
   - Puertos y protocolos.
   - DNS y DHCP.
   - Subredes.
   - Diagnóstico básico.

5. **Ciberseguridad ética**
   - Fundamentos de seguridad.
   - Hardening y defensa.
   - Registros y análisis.
   - Seguridad web en laboratorios.
   - CTF y entornos autorizados.
   - Automatización defensiva con Python.

> La ciberseguridad práctica se trabajará únicamente en sistemas propios, CTF, laboratorios o entornos con autorización explícita.

## Estado actual

| Área | Estado | Empieza aquí |
|---|---|---|
| Python | En curso: tipos de datos y operadores aritméticos | [python/](python/README.md) · [Progreso](python/PROGRESO.md) |
| Java y POO | Pendiente | [java/](java/README.md) |
| Linux | Manual v3 redactado (35 módulos); práctica del estudiante pendiente | [linux/](linux/README.md) · [Manual v3](linux/manuales/v3/README.md) |
| Redes | Pendiente | [redes/](redes/README.md) |
| Ciberseguridad ética | Pendiente | [ciberseguridad/](ciberseguridad/README.md) |

## Estructura del repositorio

Las carpetas marcadas con `(prevista)` todavía no existen: Git no guarda carpetas vacías, así que se crearán al guardar su primer archivo.

```text
README.md                 Portada y ruta de aprendizaje
GUIA_DE_TRABAJO.md        Reglas permanentes de organización

python/
  PROGRESO.md             Registro de temas trabajados
  clases/                 Apuntes de cada clase
  ejercicios/             Prácticas cortas (.py)
  examenes/               Mini evaluaciones
  proyectos/              Proyectos completos
  manuales/               Revisiones del Manual Maestro de Python

java/
  ejercicios/             (prevista)
  poo/                    (prevista)
  proyectos/              (prevista)

linux/
  manuales/               Manual Maestro de Linux (v2 histórica y v3 vigente)
  comandos/               (prevista)
  bash/                   (prevista)
  laboratorios/           (prevista)

redes/                    Apuntes de redes

ciberseguridad/
  fundamentos/            (prevista)
  blue-team/              (prevista)
  web-security/           (prevista)
  laboratorios-autorizados/  (prevista)

proyectos/                Proyectos multidisciplinarios
notas/                    Resúmenes y apuntes generales
```

## Regla de guardado

Todo material nuevo relacionado con código o aprendizaje técnico debe guardarse en la sección correspondiente:

| Material | Destino |
|---|---|
| Apunte de una clase de Python | `python/clases/` |
| Ejercicio básico de Python | `python/ejercicios/` |
| Evaluación de Python | `python/examenes/` |
| Proyecto de Python | `python/proyectos/` |
| Ejercicio de Java | `java/ejercicios/` |
| Práctica de POO | `java/poo/` |
| Proyecto Java | `java/proyectos/` |
| Comandos de Linux | `linux/comandos/` |
| Script Bash | `linux/bash/` |
| Laboratorio Linux | `linux/laboratorios/` |
| Manual o revisión de manual | `<área>/manuales/` |
| Apuntes de redes | `redes/` |
| Fundamentos de seguridad | `ciberseguridad/fundamentos/` |
| Defensa / Blue Team | `ciberseguridad/blue-team/` |
| Seguridad web autorizada | `ciberseguridad/web-security/` |
| CTF o laboratorio autorizado | `ciberseguridad/laboratorios-autorizados/` |
| Proyecto multidisciplinario | `proyectos/` |
| Resumen o apunte general | `notas/` |

## Reglas de seguridad

- Nunca subir contraseñas, tokens, claves API o claves privadas.
- No subir archivos `.env` reales.
- No almacenar datos personales o información clínica sensible.
- No guardar capturas de red reales con información privada.
- Usar datos de ejemplo o anonimizados cuando sea necesario.
- Revisar el `.gitignore` antes de añadir nuevos tipos de archivos sensibles.

## Convención para commits

Formato: `área: verbo en infinitivo + qué cambia`. Es el formato que ya usa el historial del repositorio.

| Área | Uso |
|---|---|
| `python:` `java:` `linux:` `redes:` `security:` | Material de esa área |
| `docs:` | Documentación general (README, guía, ruta) |
| `chore:` | Mantenimiento (`.gitignore`, estructura) |

```text
python: agregar ejercicio de variables
java: practicar clases y objetos
linux: añadir práctica de permisos
redes: agregar notas de TCP/IP
security: documentar laboratorio autorizado
docs: actualizar ruta de aprendizaje
```

Detalle completo en [GUIA_DE_TRABAJO.md](GUIA_DE_TRABAJO.md).

## Objetivo

Construir un historial ordenado del aprendizaje, de manera que cada ejercicio, corrección y proyecto permita observar el progreso desde fundamentos hasta temas avanzados.
