# Módulo 29 — Manejo de errores, `trap`, `mktemp`, límites de `set -e`/`set -u` y ShellCheck

Manual Maestro de Linux y Shell Scripting — Edición 2026 · v3 · Vigesimonovena entrega.

[Índice del manual](README.md) · [← Módulo 28](modulo-28-funciones-parametros-ambito.md) · [Arquitectura](00-indice-arquitectura.md) · [Módulo 30 →](modulo-30-cron-temporizadores-systemd.md)

## 1. Qué aprenderás

Al terminar este módulo podrás:

- explicar qué significa manejar errores en un script;
- diferenciar detectar un fallo, informarlo, recuperarse y terminar;
- validar explícitamente operaciones importantes;
- usar `trap` de forma básica con `EXIT`;
- crear archivos temporales de forma segura con `mktemp`;
- explicar por qué `mktemp -u` no debe usarse para crear después un archivo;
- comprender qué hace `set -e` y por qué no es un detector universal de errores;
- reconocer contextos donde `errexit` se ignora o tiene semántica especial;
- comprender qué hace `set -u` y cómo afecta variables no definidas;
- usar valores predeterminados cuando correspondan;
- comprender qué cambia `set -o pipefail`;
- separar limpieza, diagnóstico y lógica principal;
- usar `bash -n` para comprobar sintaxis;
- usar ShellCheck como análisis estático complementario;
- interpretar una advertencia de ShellCheck antes de aplicar cambios;
- evitar el patrón de “activar opciones estrictas y confiar ciegamente”.

Conocimientos previos:

- estados de salida;
- `if`, `&&`, `||`;
- tuberías;
- variables y expansiones;
- funciones;
- redirecciones;
- archivos y rutas.

**Seguridad:** las prácticas se limitan a `~/linux-lab/modulo-29-errores`. No se usan privilegios para los ejercicios. La limpieza automatizada solo eliminará archivos temporales creados expresamente por el propio ejercicio y comprobará primero la ruta guardada.

## 2. Qué significa manejar errores

Un script robusto no se limita a “seguir ejecutando”.

Debe decidir qué hacer cuando algo falla.

Modelo:

```text
operación
   ↓
¿tuvo éxito?
   ├─ sí → continuar
   └─ no → informar / recuperar / limpiar / terminar
```

## 3. Cuatro acciones distintas

Ante un fallo puedes necesitar:

1. **detectar** el estado;
2. **informar** qué ocurrió;
3. **recuperar o limpiar** recursos temporales;
4. **terminar** con un estado apropiado.

No todos los errores requieren las cuatro acciones.

## 4. Validación explícita

Una forma clara:

```bash
if ! cd ~/linux-lab; then
    printf 'Error: no pude entrar al laboratorio\n' >&2
    exit 1
fi
```

Ventaja: la intención queda visible.

## 5. Variante con `||`

También puedes escribir:

```bash
cd ~/linux-lab || {
    printf 'Error: no pude entrar al laboratorio\n' >&2
    exit 1
}
```

Las llaves agrupan varias órdenes en la rama de fallo.

Para aprendizaje inicial, usa la forma que puedas explicar sin ambigüedad.

## 6. Mensajes de error por `stderr`

```bash
printf 'Error: falta un archivo\n' >&2
```

`>&2` envía el diagnóstico a la salida de error estándar.

Esto permite mantener `stdout` disponible para datos útiles.

## 7. Estados de error documentados

Puedes definir una convención interna:

```text
0 → éxito
1 → fallo general
2 → uso incorrecto
```

Pero esos significados pertenecen a tu script; no son universales para todos los programas.

## 8. Función de error sencilla

```bash
error() {
    printf 'Error: %s\n' "$1" >&2
}
```

Uso:

```bash
error 'falta el archivo de entrada'
```

Una función así evita repetir formato de diagnóstico.

## 9. Qué es `trap`

`trap` permite indicar a Bash que ejecute una acción cuando ocurre un evento determinado, como:

- salida del shell mediante `EXIT`;
- determinadas señales;
- otros eventos soportados por Bash.

En este módulo nos concentraremos principalmente en **`EXIT`** para limpieza controlada.

## 10. Primer `trap` con `EXIT`

```bash
al_salir() {
    printf 'El script está terminando\n'
}

trap al_salir EXIT
```

Cuando el shell termina, ejecuta la función registrada.

## 11. `trap` no significa “capturar todos los errores”

`trap` no convierte automáticamente cualquier fallo en una excepción.

**Límite:** la limpieza configurada con `trap ... EXIT` no está garantizada ante una terminación forzada o un apagado repentino. No dependas únicamente de esta limpieza para proteger información sensible.

Debes distinguir:

```text
trap EXIT → acción al salir
trap ERR  → evento relacionado con determinadas órdenes fallidas
```

`ERR` tiene excepciones y reglas relacionadas con las mismas construcciones que `set -e`; no lo usaremos como detector universal.

## 12. Consultar traps

Puedes inspeccionar traps instalados con:

```bash
trap -p
```

Esto es una operación de consulta.

## 13. Eliminar un trap

```bash
trap - EXIT
```

restaura la disposición original de `EXIT` para el shell actual.

No lo necesitas en la mayoría de scripts pequeños, pero debes reconocer la sintaxis.

## 14. Qué es un archivo temporal

Un archivo temporal guarda datos que solo necesitas durante una ejecución.

Un nombre fijo como:

```text
/tmp/datos.txt
```

puede colisionar con otro proceso o usuario y no es una estrategia segura para creación temporal.

## 15. `mktemp`

GNU `mktemp` crea de forma segura un archivo o directorio temporal basado en una plantilla.

Ejemplo dentro de nuestro laboratorio:

```bash
temporal=$(mktemp "$HOME/linux-lab/modulo-29-errores/tmp.XXXXXXXXXX") || exit 1
```

`mktemp` crea realmente el archivo y escribe su nombre.

## 16. Plantilla con `X`

Una plantilla incluye una secuencia de `X` que `mktemp` sustituye.

Ejemplo:

```text
tmp.XXXXXXXXXX
```

No inventes tú mismo un nombre “aleatorio” con `$RANDOM` como sustituto de `mktemp` para seguridad.

## 17. No usar `mktemp -u` para crear después

`mktemp -u` genera un nombre pero **no crea el objeto**.

Entre generar ese nombre y utilizarlo, otro proceso podría crear algo allí.

Por eso este manual no usa:

```text
nombre=$(mktemp -u ...)
crear "$nombre" después
```

para archivos temporales.

## 18. Comprobar que `mktemp` funcionó

```bash
temporal=$(mktemp "$HOME/linux-lab/modulo-29-errores/tmp.XXXXXXXXXX") || {
    printf 'Error: no se pudo crear el temporal\n' >&2
    exit 1
}
```

No uses una variable de ruta temporal si la creación falló.

## 19. Limpieza controlada con una función

```bash
temporal=''

limpiar() {
    if [[ -n $temporal && -f $temporal ]]; then
        rm -f -- "$temporal"
    fi
}

trap limpiar EXIT
```

Esta práctica sí usa `rm`, pero con límites explícitos:

- solo sobre una variable creada por este script;
- solo si no está vacía;
- solo si actualmente es un archivo regular;
- con `--` para finalizar opciones;
- sin `-r`;
- dentro de la carpeta de laboratorio.

## 20. Crear después del trap

Orden recomendado:

```bash
temporal=''

limpiar() {
    if [[ -n $temporal && -f $temporal ]]; then
        rm -f -- "$temporal"
    fi
}

trap limpiar EXIT

temporal=$(mktemp "$HOME/linux-lab/modulo-29-errores/tmp.XXXXXXXXXX") || exit 1
```

Si algo falla después de la creación, el trap sigue teniendo una ruta conocida que limpiar.

## 21. No construyas limpieza peligrosa

Evita patrones genéricos como:

```text
rm -rf "$variable"
```

en una rutina de aprendizaje.

Una variable vacía, equivocada o manipulada puede convertir una limpieza en una operación de gran impacto.

En este módulo usamos únicamente eliminación de un archivo temporal individual controlado.

## 22. Qué hace `set -e`

`set -e`, también llamado `errexit`, hace que Bash salga ante determinados estados de fallo.

```bash
set -e
```

Suena simple, pero su comportamiento depende del contexto sintáctico.

## 23. `set -e` no significa “cualquier comando no-cero mata el script”

Hay contextos donde Bash no sale por un estado no-cero, porque ese estado se está usando para tomar una decisión.

Entre ellos existen condiciones relacionadas con:

- pruebas de `if`;
- condiciones de `while` y `until`;
- listas `&&` y `||` salvo posiciones específicas;
- comandos de tuberías salvo las reglas aplicables al estado de la tubería;
- comandos negados con `!`.

Por eso no debes memorizar `set -e` como un `try/catch` universal.

## 24. Ejemplo: fallo usado por `if`

```bash
set -e

if false; then
    printf 'No aparece\n'
fi

printf 'El script sigue\n'
```

`false` forma parte de la condición de `if`, por lo que su fallo es información para la decisión.

## 25. Ejemplo: fallo usado por `||`

```bash
set -e

false || printf 'El fallo fue gestionado\n'
printf 'Continuación\n'
```

El estado de `false` participa en una lista OR.

## 26. Funciones y `set -e`: una interacción importante

Si una función o comando compuesto se ejecuta en un contexto donde `-e` está siendo ignorado, los comandos de su cuerpo también pueden quedar afectados por esa regla.

Esto hace que mover una función a un contexto distinto pueda cambiar cómo se comporta `errexit`.

Conclusión pedagógica:

> usa comprobaciones explícitas para fallos que sean críticos para la lógica del script.

## 27. `set -e` dentro de sustitución de comandos

Las sustituciones de comandos:

```bash
resultado=$(comando)
```

se ejecutan en un entorno de subshell.

En Bash fuera de modo POSIX, `-e` normalmente se limpia en subshells creadas para sustitución de comandos, salvo configuraciones como `inherit_errexit`.

Esto es otra razón para no construir la robustez del script únicamente alrededor de `set -e`.

## 28. Qué hace `set -u`

`set -u`, también llamado `nounset`, trata como error determinadas expansiones de variables o parámetros no definidos.

```bash
set -u
printf '%s\n' "$variable_no_definida"
```

En un script no interactivo, Bash escribe un error y sale.

## 29. Variable vacía no es variable no definida

```bash
variable=''
```

está definida, aunque su contenido sea vacío.

Con `set -u`, debes distinguir:

```text
unset → no definida
''    → definida pero vacía
```

## 30. Valor predeterminado con expansión de parámetros

Si una variable puede faltar y existe un valor razonable por defecto:

```bash
nombre=${1:-Invitado}
```

Esto evita depender de una expansión directa de un parámetro ausente.

No uses valores predeterminados para ocultar errores que deberían detectarse explícitamente.

## 31. Comprobar si una variable está definida

En Bash moderno puedes usar:

```bash
if [[ -v variable ]]; then
    printf 'Está definida\n'
fi
```

`-v` comprueba si la variable tiene un valor asignado.

## 32. `set -u` tampoco reemplaza validación

`nounset` puede detectar referencias accidentales a variables no definidas.

Pero no puede determinar por ti si:

- el dato tiene el formato correcto;
- una ruta es segura;
- un número está en un rango permitido;
- un argumento pertenece al usuario correcto;
- el contenido tiene sentido lógico.

## 33. Qué hace `pipefail`

Por defecto, el estado de una tubería es el estado de su último comando.

Con:

```bash
set -o pipefail
```

el estado de la tubería será el del comando situado más a la derecha que haya terminado con estado no-cero, o `0` si todos tuvieron éxito.

## 34. Ejemplo conceptual de `pipefail`

Sin `pipefail`:

```text
comando_que_falla | comando_que_tiene_exito
```

la tubería puede terminar con éxito si el último comando devuelve `0`.

Con `pipefail`, el fallo anterior puede reflejarse en el estado global de la tubería.

## 35. `pipefail` no vuelve segura una tubería

`pipefail` mejora la visibilidad del estado, pero no:

- valida datos;
- evita efectos laterales;
- evita pérdida de información;
- corrige quoting;
- garantiza que todos los programas produzcan estados adecuados.

Es una herramienta, no una garantía.

## 36. La combinación conocida `set -euo pipefail`

Es frecuente encontrar:

```bash
set -euo pipefail
```

Este manual **no** la presenta como una receta mágica.

Significa aproximadamente:

```text
-e       → salir en determinados fallos
-u       → error en determinadas variables no definidas
pipefail → reflejar fallos anteriores de tuberías
```

Puede ser útil en scripts diseñados y probados para esas semánticas, pero debes conocer sus límites antes de adoptarla.

## 37. No activar opciones por copiar una plantilla

Antes de habilitar una opción global debes saber:

- qué código cambia;
- qué condiciones son deliberadamente no-cero;
- qué funciones dependen de ese comportamiento;
- qué tuberías existen;
- cómo manejarás errores esperados.

En ejercicios iniciales priorizamos lógica explícita y luego añadimos opciones deliberadamente.

## 38. Comprobar sintaxis con `bash -n`

Ya lo hemos usado:

```bash
bash -n script.sh
```

`-n` lee el script sin ejecutar las órdenes y puede detectar errores sintácticos.

Pero no detecta todos los errores lógicos.

Un script puede pasar `bash -n` y aun así fallar durante su ejecución.

## 39. Qué es ShellCheck

ShellCheck es una herramienta de análisis estático para scripts `sh`/Bash y otros shells compatibles.

Busca patrones problemáticos como:

- expansiones sin comillas;
- errores semánticos frecuentes;
- construcciones no portables;
- errores de lógica detectables estáticamente;
- usos sospechosos de comandos.

## 40. ShellCheck no ejecuta el script para entender todo

Análisis estático significa que estudia el código.

No puede saber siempre:

- qué archivos existirán;
- qué contenido real recibirás;
- qué resultado producirá un sistema remoto;
- qué intención humana tenías.

Una advertencia debe leerse y entenderse; no se corrige ciegamente.

## 41. Comprobar si ShellCheck está instalado

```bash
command -v shellcheck
```

Si devuelve una ruta, está disponible.

Esta es una operación de consulta.

## 42. Usar ShellCheck

```bash
shellcheck script.sh
```

Si no produce diagnósticos, eso no certifica que el script sea perfecto.

Solo significa que no encontró problemas dentro de las reglas aplicables.

## 43. Ejemplo típico: SC2086

ShellCheck suele advertir sobre expansiones sin comillas que pueden sufrir word splitting o globbing.

Ejemplo problemático:

```text
printf '%s\n' $archivo
```

Corrección habitual:

```bash
printf '%s\n' "$archivo"
```

Antes de aplicar una corrección automática, confirma que coincide con la intención del script.

## 44. Instalación opcional de ShellCheck

Instalar un paquete modifica el sistema, así que primero identifica la distribución y revisa la operación.

Si no está instalado, consulta el gestor de paquetes correspondiente.

Ejemplos habituales:

```text
Debian/Ubuntu → paquete shellcheck
Fedora/RHEL   → comprobar disponibilidad del paquete ShellCheck en repositorios habilitados
```

No es obligatorio instalarlo para continuar leyendo el manual. También existe el analizador en el sitio oficial de ShellCheck.

## 45. Orden de revisión recomendado

Para un script de práctica:

```text
1. leer el código
2. bash -n script.sh
3. ShellCheck, si está disponible
4. corregir solo lo entendido
5. probar en el laboratorio
6. comprobar estados y resultados
7. guardar en Git
```

## 46. Preparar el laboratorio

```bash
test -d ~/linux-lab && \
cd ~/linux-lab && \
mkdir -p modulo-29-errores && \
cd modulo-29-errores && pwd
```

Etiqueta: **creación en laboratorio**.

## 47. Práctica A — error explícito

Crea `validar_ruta.sh`:

```bash
#!/usr/bin/env bash

ruta=${1:-}

if [[ -z $ruta ]]; then
    printf 'Error: falta una ruta\n' >&2
    exit 2
fi

if [[ ! -e $ruta ]]; then
    printf 'Error: la ruta no existe: %s\n' "$ruta" >&2
    exit 1
fi

printf 'Ruta válida: %s\n' "$ruta"
exit 0
```

Prueba únicamente con rutas del laboratorio.

## 48. Práctica B — `mktemp` y limpieza con `trap`

Crea `temporal.sh`:

```bash
#!/usr/bin/env bash

temporal=''

limpiar() {
    if [[ -n $temporal && -f $temporal ]]; then
        rm -f -- "$temporal"
    fi
}

trap limpiar EXIT

temporal=$(mktemp "$HOME/linux-lab/modulo-29-errores/tmp.XXXXXXXXXX") || {
    printf 'Error: no se pudo crear el temporal\n' >&2
    exit 1
}

printf 'Temporal creado: %s\n' "$temporal"
printf 'dato de práctica\n' > "$temporal"
printf 'El trap lo eliminará al terminar\n'
```

Antes de ejecutar, confirma con `pwd` que estás en la carpeta de práctica.

## 49. Qué modifica la práctica B

El script:

1. crea un archivo temporal dentro de `~/linux-lab/modulo-29-errores`;
2. escribe una línea de prueba;
3. al salir, comprueba que la variable no esté vacía y que la ruta sea un archivo regular;
4. elimina únicamente ese archivo.

No utiliza borrado recursivo.

## 50. Práctica C — observar `set -u`

Crea `nounset.sh`:

```bash
#!/usr/bin/env bash

set -u

nombre=${1:-Invitado}
printf 'Hola, %s\n' "$nombre"
```

Prueba con y sin argumento.

Después explica por qué `${1:-Invitado}` evita depender de `$1` sin definir.

## 51. Práctica D — `pipefail` controlado

```bash
#!/usr/bin/env bash

set -o pipefail

if false | true; then
    printf 'La tubería informó éxito\n'
else
    printf 'La tubería informó fallo\n'
fi
```

Con `pipefail`, la tubería informa fallo porque uno de sus componentes devolvió un estado no-cero.

## 52. Práctica E — límite de `set -e`

```bash
#!/usr/bin/env bash

set -e

if false; then
    printf 'No aparece\n'
fi

printf 'El script continúa después de la condición\n'
```

Explica por qué este ejemplo contradice la simplificación “cualquier fallo detiene el script”.

## 53. Práctica F — análisis estático

Si ShellCheck está disponible, crea:

```bash
#!/usr/bin/env bash

archivo='dos palabras.txt'
printf '%s\n' $archivo
```

Primero:

```bash
bash -n ejemplo.sh
```

Después:

```bash
shellcheck ejemplo.sh
```

Lee el diagnóstico.

Finalmente corrige:

```bash
printf '%s\n' "$archivo"
```

## 54. Errores frecuentes

| Error | Problema | Corrección |
|---|---|---|
| creer que `set -e` captura cualquier fallo | tiene excepciones contextuales | valida explícitamente operaciones críticas |
| activar `set -euo pipefail` sin entenderlo | puede cambiar flujo esperado | estudia cada opción por separado |
| usar `mktemp -u` y crear después | ventana de carrera | deja que `mktemp` cree el objeto |
| usar nombre temporal fijo | colisiones/riesgo | usa `mktemp` |
| limpieza con `rm -rf "$variable"` | demasiado impacto ante errores de variable | limita el objeto y valida antes |
| usar `trap ERR` como detector universal | comparte excepciones importantes | úsalo solo entendiendo su semántica |
| mezclar errores con stdout | contamina datos | envía diagnósticos a stderr |
| confiar en `bash -n` para lógica | solo analiza sintaxis | combina revisión y pruebas |
| obedecer ShellCheck sin entender | una regla puede no reflejar tu intención | lee código y documentación |
| asumir que ShellCheck certifica seguridad | es análisis estático limitado | prueba y revisa contexto |

## 55. Detección de error 1

Analiza:

```bash
set -e

if grep -q 'texto' archivo.txt; then
    printf 'Encontrado\n'
fi
```

¿un resultado no-cero de `grep` necesariamente termina el script por `set -e`?

No en este contexto: `grep` está siendo usado como condición del `if`.

## 56. Detección de error 2

Analiza:

```bash
temporal=$(mktemp -u)
printf 'dato\n' > "$temporal"
```

Problema: se genera un nombre sin crear el archivo, dejando una ventana entre elección y creación.

Corrección conceptual:

```bash
temporal=$(mktemp "$HOME/linux-lab/modulo-29-errores/tmp.XXXXXXXXXX") || exit 1
```

## 57. Detección de error 3

Analiza:

```bash
limpiar() {
    rm -rf "$temporal"
}
```

Problema: la acción es demasiado amplia para una ruta variable y no verifica qué está eliminando.

En nuestro laboratorio solo necesitamos:

```bash
limpiar() {
    if [[ -n $temporal && -f $temporal ]]; then
        rm -f -- "$temporal"
    fi
}
```

## 58. Método de robustez del manual

Para scripts nuevos:

1. valida entradas;
2. cita expansiones;
3. comprueba operaciones críticas explícitamente;
4. separa datos y diagnósticos;
5. usa temporales creados de forma segura;
6. registra limpieza limitada con `trap` cuando exista un recurso temporal;
7. comprende una opción antes de habilitarla globalmente;
8. valida sintaxis con `bash -n`;
9. analiza con ShellCheck cuando esté disponible;
10. prueba fallos controlados además del camino exitoso.

## 59. Práctica independiente

Crea `procesar_temporal.sh`.

Debe:

1. usar Bash;
2. aceptar un argumento de texto no sensible;
3. validar que exista el argumento;
4. crear un temporal dentro de la carpeta del módulo usando `mktemp`;
5. registrar una función de limpieza mediante `trap ... EXIT`;
6. escribir únicamente el texto de práctica en el temporal;
7. leerlo y mostrarlo;
8. eliminar automáticamente solo ese archivo al terminar;
9. enviar errores a stderr;
10. pasar `bash -n`;
11. pasar ShellCheck si está disponible;
12. no usar `sudo`, `rm -r`, `rm -rf` ni rutas fuera del laboratorio.

## 60. Mini evaluación

1. ¿manejar errores significa solo usar `set -e`? A) Sí B) No
2. ¿`stderr` es apropiado para diagnósticos? A) Sí B) No
3. ¿`trap ... EXIT` puede usarse para limpieza al terminar? A) Sí B) No
4. ¿`mktemp` crea el objeto temporal? A) Sí B) No
5. ¿es seguro usar `mktemp -u` y crear después como patrón general? A) Sí B) No
6. ¿`set -e` sale ante absolutamente cualquier estado no-cero? A) Sí B) No
7. ¿una condición de `if` es uno de los contextos especiales de `set -e`? A) Sí B) No
8. ¿`set -u` detecta determinadas expansiones de variables no definidas? A) Sí B) No
9. ¿variable vacía y variable no definida son lo mismo? A) Sí B) No
10. ¿`pipefail` cambia el estado calculado de una tubería? A) Sí B) No
11. ¿`pipefail` valida automáticamente los datos? A) Sí B) No
12. ¿`bash -n` ejecuta todo el script? A) Sí B) No
13. ¿ShellCheck es análisis estático? A) Sí B) No
14. ¿una advertencia de ShellCheck debe entenderse antes de corregir? A) Sí B) No
15. ¿`rm -rf "$variable"` es una buena práctica de limpieza para este módulo? A) Sí B) No

## 61. Registro de aprendizaje

```text
Manejar un error significa:
`stderr` sirve para:
`trap` sirve para:
`EXIT` en trap significa:
`mktemp` sirve para:
¿por qué no usamos `mktemp -u` para crear después?:
`set -e` hace:
¿por qué `set -e` no es universal?:
`set -u` hace:
Diferencia entre unset y vacío:
`pipefail` cambia:
`bash -n` comprueba:
ShellCheck sirve para:
¿por qué no sigo una advertencia automáticamente?:
Algo que todavía confundo:
Estado: EN APRENDIZAJE / PRACTICADO
```

## 62. Puerta de dominio

Para considerar este módulo **DOMINADO** deberás poder en más de una práctica:

1. detectar explícitamente un fallo y devolver un estado;
2. explicar al menos dos excepciones conceptuales de `set -e`;
3. distinguir `set -u` de validación de contenido;
4. explicar qué resuelve `pipefail` y qué no;
5. crear un temporal con `mktemp` sin `-u`;
6. limpiar únicamente el temporal propio mediante `trap EXIT`;
7. interpretar una advertencia sencilla de ShellCheck;
8. explicar por qué un script que pasa `bash -n` aún puede contener errores.

## 63. Fuentes y límites

Fuentes principales:

- GNU Bash Reference Manual — The Set Builtin: https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html
- GNU Bash Reference Manual — Bourne Shell Builtins (`trap`): https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html
- GNU Bash Reference Manual — Pipelines: https://www.gnu.org/software/bash/manual/html_node/Pipelines.html
- GNU Bash Reference Manual — Command Execution Environment: https://www.gnu.org/software/bash/manual/html_node/Command-Execution-Environment.html
- GNU Coreutils — `mktemp`: https://www.gnu.org/software/coreutils/manual/html_node/mktemp-invocation.html
- ShellCheck: https://www.shellcheck.net/
- ShellCheck Wiki: https://www.shellcheck.net/wiki/

Puntos verificados documentalmente:

- `set -e` tiene excepciones asociadas a condiciones, listas y otros contextos; no equivale a “fallar ante cualquier no-cero”;
- si `-e` está siendo ignorado en el contexto de un comando compuesto o función, las órdenes del cuerpo pueden verse afectadas por esa misma regla;
- `set -u` trata determinadas expansiones de variables no definidas como error;
- `pipefail` devuelve el estado del comando no-cero situado más a la derecha en la tubería, o `0` si todos tienen éxito;
- por defecto, una tubería usa el estado de su último comando;
- `mktemp` crea de forma segura el archivo o directorio temporal;
- GNU Coreutils advierte que `mktemp -u` es inseguro para generar un nombre y crear el objeto posteriormente;
- ShellCheck es un analizador estático para scripts de shell y documenta sus diagnósticos mediante códigos como `SC2086`.

Se posponen:

- `ERR`, `DEBUG` y `RETURN` traps en profundidad;
- herencia de traps con `errtrace` y `functrace`;
- `inherit_errexit`;
- limpieza de árboles temporales complejos;
- archivos de bloqueo y concurrencia;
- señales y cleanup avanzado;
- `mktemp -d` con recursos múltiples;
- configuración avanzada de ShellCheck y directivas de exclusión;
- pruebas automatizadas de shell.

**Estado de la lección:** redactada y revisada documentalmente contra GNU Bash, GNU Coreutils y la documentación oficial de ShellCheck. Las prácticas son locales y limitan cualquier borrado al archivo temporal creado por el propio ejercicio.

---

**Siguiente:** [Módulo 30 — Automatización con `cron` y temporizadores de systemd](modulo-30-cron-temporizadores-systemd.md) · [Volver al índice](README.md)
