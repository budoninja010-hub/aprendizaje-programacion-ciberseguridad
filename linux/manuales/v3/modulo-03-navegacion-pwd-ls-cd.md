# Módulo 3 — Navegación inicial: pwd, ls y cd

Manual Maestro de Linux y Shell Scripting — Edición 2026 · v3 · Tercera entrega.

[Estado del manual](README.md) · [Módulo anterior](modulo-02-terminal-cli-shell-bash-ayuda.md) · [Arquitectura](00-indice-arquitectura.md)

## 1. Objetivo y preparación

Aprenderás a responder tres preguntas: **¿dónde estoy?, ¿qué hay aquí?, ¿cómo cambio de carpeta?** Usarás una orden para cada pregunta y comprobarás el resultado antes de continuar.

Requisitos: distinguir prompt y orden, utilizar Bash en un entorno Linux preparado y tener el directorio normal `~/linux-lab` del Módulo 1. Si falta, vuelve a su preparación; no crees carpetas del sistema ni añadas `sudo` para resolver un error.

Diagnóstico breve: explica qué hace la shell y cómo consultarías ayuda sobre `cd`. Si no lo recuerdas, repasa el Módulo 2 antes de ejecutar la práctica.

**Alcance:** solo consultas y cambios del directorio de trabajo de la shell. No se crean, mueven, modifican ni borran archivos. La shell puede guardar las órdenes en su historial. No practiques con nombres o datos secretos. El laboratorio no es una barrera de aislamiento.

## 2. Directorio de trabajo: tu ubicación actual

Un directorio es una carpeta. La shell mantiene una ubicación de trabajo desde la cual interpreta muchas de las rutas que escribes. Cambiar esa ubicación no mueve físicamente los archivos.

Imagina este árbol ilustrativo, no una descripción de tu equipo:

```text
directorio personal
└── linux-lab
```

Si la shell está en `linux-lab`, esa es su ubicación de trabajo. Otra terminal puede estar en una carpeta diferente: cambiar de directorio en una sesión no cambia automáticamente las demás.

**Para qué sirve:** permite entender a qué carpeta te refieres cuando una orden no incluye una ruta completa.

**Error típico:** pensar que «estar en una carpeta» significa que todos los comandos solo pueden afectar esa carpeta. Una orden puede recibir otra ruta como argumento.

**Ejercicio:** explica la diferencia entre cambiar tu ubicación y mover una carpeta a otro lugar.

## 3. pwd: preguntar dónde estás

Escribe únicamente la orden y pulsa Enter:

```bash
pwd
```

`pwd` muestra la ruta del directorio de trabajo. No necesita un nombre de archivo. Una respuesta ilustrativa podría ser `/home/estudiante/linux-lab`; no tiene que coincidir con tu equipo.

Lee la ruta antes de actuar. No basta con reconocer la última palabra: comprueba que se refiere al laboratorio de tu usuario.

**Error típico:** ejecutar `pwd` y no mirar la salida. La comprobación útil consiste en interpretar el resultado, no solo en escribir la orden.

**Ejercicio:** consulta tu ubicación y explica qué información obtuviste. No publiques la ruta completa si contiene datos personales.

### Nota de precisión: qué versión de pwd consultas

Bash tiene una orden interna `pwd`; también existe una utilidad externa de GNU con ese nombre. No se deben trasladar sus valores predeterminados sin comprobarlos. En Bash, `help pwd` explica la orden interna. Cuando hay enlaces simbólicos, una ruta lógica y una física pueden diferir. Se estudiará esa distinción después; si una ruta sorprende, pausa la práctica en lugar de asumir que es un error que requiere mover archivos. [GNU: pwd](https://www.gnu.org/s/coreutils/manual/html_node/pwd-invocation.html).

## 4. ls: observar sin cambiar de carpeta

```bash
ls
```

`ls` lista las entradas no ocultas del directorio de trabajo con su comportamiento habitual. Puede mostrar nombres en columnas. Una salida vacía no demuestra que la carpeta no contenga entradas ocultas.

**Para qué sirve:** orientarte antes de decidir qué quieres consultar. No abre cada archivo ni entra en las carpetas que muestra. El color depende de la configuración; no lo uses como única prueba del tipo de objeto.

**Ejercicio:** consulta el contenido del laboratorio. Explica qué puedes concluir si no aparece ningún nombre y qué todavía no puedes concluir.

### Mostrar entradas ocultas

```bash
ls -a
```

`ls` sigue siendo la orden; `-a` es una opción que incluye nombres que comienzan por punto. También muestra normalmente `.` y `..`: representan el directorio actual y su padre. No se han creado archivos por añadir esta opción. [GNU: selección de entradas](https://www.gnu.org/software/coreutils/manual/html_node/Which-files-are-listed.html).

**Error típico:** creer que oculto equivale a protegido. Un nombre que empieza por punto afecta su presentación habitual, no establece por sí solo permisos de seguridad.

**Ejercicio:** compara `ls` y `ls -a`. Si solo aparecen `.` y `..`, explica por qué eso no es un fallo.

### Pedir detalles

```bash
ls -l
```

La letra de `-l` es una ele minúscula, no el número uno. Pide un listado largo con datos de cada entrada. Hoy solo necesitas reconocer el primer carácter: `d` señala un directorio, `-` un archivo ordinario y `l` un enlace simbólico. Los permisos y demás campos se estudiarán después.

```bash
ls -la
```

Aquí se combinan las opciones anteriores: detalles e inclusión de entradas ocultas. No memorices todas las columnas ni supongas que el tamaño mostrado para una carpeta es la suma del contenido de sus archivos. [GNU: información del listado](https://www.gnu.org/software/coreutils/manual/html_node/What-information-is-listed.html).

**Ejercicio:** identifica una entrada de directorio sin depender del color. No hace falta abrirla ni cambiar permisos.

### Consultar otra carpeta sin entrar

```bash
ls ~/linux-lab
```

`ls` consulta y `~/linux-lab` indica el destino de la consulta. Esa ruta del Módulo 1 utiliza `~` para tu directorio personal. Ejecuta `pwd` después: verás que listar otra carpeta no ha cambiado tu ubicación.

Si quieres inspeccionar la entrada de la carpeta misma:

```bash
ls -ld ~/linux-lab
```

`-l` pide detalles y `-d` muestra el directorio como entrada, en vez de listar su interior. Si aparece como enlace, detente antes de usarlo como laboratorio y revisa su destino con ayuda. Esta orden ya se presentó en M1.

## 5. cd: cambiar tu ubicación de trabajo

```bash
cd ~/linux-lab
```

`cd` cambia el directorio de trabajo de la shell; `~/linux-lab` indica a dónde quieres ir. Si tiene éxito, normalmente no muestra texto. Comprueba la ubicación con `pwd`: silencio no es una comprobación suficiente.

No escribe dentro de los archivos del directorio ni los mueve. Si falla, no asumas que llegaste al destino: normalmente sigues en la ubicación anterior. Lee el error y detén la secuencia.

### Volver al directorio personal

```bash
cd ~
```

Este uso de `~` ya se explicó en M1. No es la raíz `/`: es el directorio personal de tu usuario. No encierres literalmente `~` entre comillas esperando la misma expansión.

### Subir un nivel

```bash
cd ..
```

Hay un espacio entre `cd` y los dos puntos. `..` indica el padre en la navegación habitual. Desde un laboratorio normal dentro de tu directorio personal, vuelve al personal. En la raíz no hay un nivel superior al que seguir subiendo. Las rutas y los enlaces se explicarán con más detalle en los módulos 4 y 5.

### Regresar a la ubicación anterior

```bash
cd -
```

El guion solicita a Bash volver al directorio anterior registrado. Normalmente también muestra la ruta al cambiar. Si todavía no existe ese registro, puede aparecer un error sobre `OLDPWD`. No es una lista de todas las carpetas visitadas ni significa subir un nivel.

**Ejercicio:** explica la diferencia entre volver al directorio personal, subir al padre y volver al anterior. Puedes apoyarte en un dibujo de dos carpetas. [GNU Bash: cd y directorios de trabajo](https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html).

## 6. Práctica guiada: predecir, ejecutar, comprobar

Realiza cada paso por separado. Antes de pulsar Enter, di qué esperas que ocurra. Ante un error, detente. No pegues toda la tabla como si fuera un script.

| Paso | Orden | Explicación y comprobación |
|---|---|---|
| 1 | `cd ~` | Ir al directorio personal conocido |
| 2 | `pwd` | Confirmar dónde estás antes de continuar |
| 3 | `ls -ld ~/linux-lab` | Revisar que el laboratorio existente es un directorio normal |
| 4 | `ls ~/linux-lab` | Ver su contenido sin entrar |
| 5 | `pwd` | Confirmar que el paso 4 no cambió la ubicación |
| 6 | `cd ~/linux-lab` | Entrar; detenerse si falla |
| 7 | `pwd` | Confirmar que estás en el laboratorio |
| 8 | `ls -a` | Observar también las entradas ocultas |
| 9 | `cd ..` | Volver al padre del laboratorio |
| 10 | `pwd` | Comprobar el retorno esperado al directorio personal |
| 11 | `cd -` | Regresar al laboratorio, que acaba de ser la ubicación anterior |
| 12 | `pwd` | Comprobar el destino final |

Si el directorio personal o el laboratorio incluyen enlaces y las rutas no coinciden con tus expectativas, no intentes «arreglar» el equipo. Conserva la observación y pide ayuda. La práctica presupone el laboratorio normal preparado en M1.

**Resultado esperado:** has realizado consultas y navegación, sin crear ni borrar materiales de práctica. No se exige que tu carpeta esté vacía ni que la salida coincida palabra por palabra con otra persona.

## 7. Errores frecuentes: entender antes de corregir

| Situación | Explicación | Corrección mínima |
|---|---|---|
| Escribes `cd..` | Falta el espacio que separa la orden del argumento | Escribir `cd ..` y después comprobar con `pwd` |
| Escribes `CD` esperando `cd` | En el entorno habitual, los nombres de órdenes distinguen mayúsculas | Usar la escritura documentada |
| Escribes `ls -1` esperando detalles | El uno pide una entrada por línea en GNU ls; no es la ele | Usar `ls -l` para el formato largo |
| «No such file or directory» | No se encontró la ruta indicada | Revisar escritura y existencia; no crear ni borrar para ocultar el error |
| «Not a directory» | El destino puede ser un archivo | Inspeccionar la entrada; `cd` requiere un directorio |
| «Permission denied» | No tienes el acceso necesario | Detenerse; no usar `sudo` ni cambiar permisos en esta lección |
| Esperabas que `ls carpeta` entrara en ella | Listar y navegar son operaciones distintas | Usar `cd` solo después de comprobar el destino |
| `cd -` vuelve a un lugar inesperado | Anterior no es lo mismo que padre | Reconstruir los cambios recientes y consultar `pwd` |

Si tu sesión tiene alias, funciones o configuraciones de navegación personalizadas, puede diferir de los ejemplos. Puedes usar `type ls` o `type cd`, aprendidos en M2, para pedir información antes de continuar. No modifiques esa configuración como parte del ejercicio.

## 8. Práctica independiente

Sin copiar la tabla anterior:

1. Consulta dónde estás.
2. Lista el laboratorio sin cambiar de carpeta y demuestra que no cambió tu ubicación.
3. Entra en él y verifica el resultado.
4. Muestra también sus entradas ocultas.
5. Vuelve al directorio personal y regresa a la ubicación anterior.
6. Explica en qué momentos comprobarías un fallo antes de continuar.

Si necesitas una pista: una orden informa, otra lista y otra cambia la ubicación. Si recurres a la tabla, anota qué paso te costó y vuelve a intentarlo más tarde con otro punto de partida conocido.

## 9. Mini evaluación y corrección de errores

- ¿Qué cambia después de un `cd` correcto y qué no cambia?
- ¿Una salida vacía de `ls` demuestra que no hay entradas ocultas?
- ¿Por qué `ls -1` y `ls -l` no son intercambiables?
- ¿Qué diferencia existe entre `cd ..` y `cd -`?
- ¿Qué harías si `cd ~/linux-lab` devuelve un error?
- Detecta el problema en esta explicación: «Ya ejecuté `ls ~/linux-lab`, así que cualquier orden posterior se ejecutará desde el laboratorio».

Responde antes de pedir soluciones. El tutor señalará primero tus aciertos, explicará cada error y propondrá una variante. En otra sesión, repite la navegación sin copiar y explica una situación distinta. Una sola respuesta correcta no acredita dominio.

## 10. Ficha de aprendizaje

Puedes responder en el chat; no hace falta crear archivos:

```text
La diferencia entre pwd, ls y cd es:
Cómo comprobé que listar no cambió mi ubicación:
Qué significa ..:
Qué significa el guion en cd -:
Un error que reconocí y cómo lo corregí:
Qué necesito repetir:
Estado: EN APRENDIZAJE / PRACTICADO
```

No pegues nombres de usuario, rutas personales, archivos privados ni capturas completas sin revisarlos. La redacción del manual y el aprendizaje del estudiante se registran por separado.

## 11. Revisión y fuentes

Esta entrega tiene revisión documental de sintaxis, orden pedagógico, fuentes, errores y alcance. Se contrastaron referencias oficiales de GNU mediante resultados indexados. No se afirma haber ejecutado la práctica en la distribución del estudiante. La comparación lógica/física y las reglas completas de rutas quedan para módulos posteriores.

Las referencias están enlazadas junto a sus explicaciones: GNU Coreutils para `ls` y la utilidad externa `pwd`; GNU Bash para las órdenes internas. Coreutils 9.11 sigue siendo la referencia editorial, sin exigir esa versión instalada.

Siguiente módulo por redactar: **Módulo 4 — Rutas absolutas y relativas; ~, ., .. y nombres con espacios**.

## Anexo editorial — Criterios de evaluación y fuentes

**Qué se conserva:** todas las explicaciones, prácticas y preguntas originales de esta entrega.

**Evaluación formativa:** el estudiante debe explicar los conceptos con sus palabras, ejecutar una práctica segura en su propio entorno cuando corresponda, interpretar la salida y reconocer al menos un error sin copiar la solución. Una respuesta correcta aislada no acredita dominio.

**Registro:** EN APRENDIZAJE / PRACTICADO / DOMINADO (solo tras varias evidencias revisadas). La revisión documental del texto no equivale a práctica realizada.

**Fuentes primarias para contrastar esta lección:**
- GNU Bash Reference Manual: https://www.gnu.org/software/bash/manual/
- GNU Coreutils Manual: https://www.gnu.org/software/coreutils/manual/
- Debian Reference: https://www.debian.org/doc/manuals/debian-reference/
- Linux kernel documentation: https://docs.kernel.org/

Las fuentes se consultan según el tema tratado; no se presume que todos los enlaces respalden cada afirmación del módulo.
