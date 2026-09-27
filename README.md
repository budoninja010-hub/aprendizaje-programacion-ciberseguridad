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

## Estructura del repositorio

```text
python/
  ejercicios/
  examenes/
  proyectos/

java/
  ejercicios/
  poo/
  proyectos/

linux/
  comandos/
  bash/
  laboratorios/

redes/

ciberseguridad/
  fundamentos/
  blue-team/
  web-security/
  laboratorios-autorizados/

proyectos/
notas/
```

## Regla de guardado

Todo material nuevo relacionado con código o aprendizaje técnico debe guardarse en la sección correspondiente:

| Material | Destino |
|---|---|
| Ejercicio básico de Python | `python/ejercicios/` |
| Evaluación de Python | `python/examenes/` |
| Proyecto de Python | `python/proyectos/` |
| Ejercicio de Java | `java/ejercicios/` |
| Práctica de POO | `java/poo/` |
| Proyecto Java | `java/proyectos/` |
| Comandos de Linux | `linux/comandos/` |
| Script Bash | `linux/bash/` |
| Laboratorio Linux | `linux/laboratorios/` |
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

Usaremos mensajes claros, por ejemplo:

```text
python: agregar ejercicio de variables
java: practicar clases y objetos
linux: añadir práctica de permisos
redes: agregar notas de TCP/IP
security: documentar laboratorio autorizado
docs: actualizar ruta de aprendizaje
```

## Objetivo

Construir un historial ordenado del aprendizaje, de manera que cada ejercicio, corrección y proyecto permita observar el progreso desde fundamentos hasta temas avanzados.
