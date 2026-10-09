# Módulo 26 — Decisiones con `if`, `test`, `[ ]`, `[[ ]]`, `case` y aritmética

Manual Maestro de Linux y Shell Scripting — Edición 2026 · v3 · Vigesimosexta entrega.

[Estado actual](README.md) · [Módulo anterior](modulo-25-codigos-salida-composicion-ordenes.md) · [Arquitectura](00-indice-arquitectura.md)

## 1. Qué aprenderás

Al terminar este módulo podrás:

- explicar cómo Bash toma decisiones usando estados de salida;
- escribir un `if` mínimo y explicar cada palabra;
- añadir `else` y `elif`;
- entender que `if` no exige obligatoriamente `[ ... ]`;
- usar `test` y `[ ... ]` con cadenas, números y archivos;
- reconocer que `[` es una orden y que `]` debe ser un argumento separado;
- usar `[[ ... ]]` cuando el script depende de Bash;
- distinguir portabilidad POSIX de características específicas de Bash;
- comparar cadenas sin confundirlas con números;
- comparar enteros con `-eq`, `-ne`, `-lt`, `-le`, `-gt` y `-ge`;
- comprobar archivos con pruebas como `-e`, `-f` y `-d`;
- usar `case` para elegir entre varios patrones;
- diferenciar `(( ... ))` de `$(( ... ))`;
- evitar errores frecuentes de espacios, quoting y comparaciones.

Conocimientos previos:

- scripts Bash;
- variables y expansión;
- quoting;
- parámetros posicionales;
- códigos de salida;
- `&&`, `||` y `exit`.

**Seguridad:** todas las prácticas se realizan dentro de `~/linux-lab`. No se usa `sudo`, no se modifican servicios, permisos del sistema, discos, red ni cortafuegos. Las pruebas de archivo son de consulta o sobre archivos creados por el estudiante.

## 2. La idea central: una condición en Bash es una orden

En Bash, `if` no pregunta necesariamente por un valor booleano como en otros lenguajes.

Su modelo básico es:

```text
ejecutar una orden
        ↓
leer su estado de salida
        ↓
0       → condición verdadera
no-cero → condición falsa
```

Esto conecta directamente con el Módulo 25.

## 3. Primer `if`

```bash
if true; then
    printf 'La condición tuvo éxito\n'
fi
```

Línea por línea:

- `if` inicia la decisión;
- `true` es la orden cuya salida se evalúa;
- `;` termina esa lista en la misma línea;
- `then` inicia el bloque que se ejecuta si el estado fue `0`;
- `printf` es la acción;
- `fi` cierra el `if`.

`fi` es `if` escrito al revés; es la palabra de cierre de esta estructura.

## 4. Forma en varias líneas

También puedes escribir:

```bash
if true
then
    printf 'Éxito\n'
fi
```

Ambas formas son válidas. En este manual usaremos normalmente:

```bash
if condición; then
    acción
fi
```

## 5. `if` evalúa el estado, no el texto mostrado

```bash
if false; then
    printf 'No debe aparecer\n'
fi
```

`false` no necesita imprimir la palabra `false`. Su estado no-cero basta para que Bash omita el bloque.

## 6. `if` puede evaluar una orden normal

No necesitas escribir siempre `[ ... ]`.

Ejemplo:

```bash
if cd ~/linux-lab; then
    printf 'Pude entrar al laboratorio\n'
fi
```

`if` evalúa directamente el estado de `cd`.

Esto es una idea esencial: **`if` decide según el resultado de órdenes**.

## 7. Añadir `else`

```bash
if true; then
    printf 'Éxito\n'
else
    printf 'Fallo\n'
fi
```

`else` se ejecuta cuando la condición anterior produce un estado distinto de cero.

## 8. Añadir `elif`

`elif` significa conceptualmente “si no, prueba esta otra condición”.

```bash
numero=2

if (( numero == 1 )); then
    printf 'uno\n'
elif (( numero == 2 )); then
    printf 'dos\n'
else
    printf 'otro valor\n'
fi
```

Las comparaciones aritméticas se explicarán más adelante en este mismo módulo.

## 9. Qué es `test`

`test` es un builtin de Bash que evalúa una expresión condicional y devuelve:

```text
0 → verdadera
1 → falsa
```

Ejemplo:

```bash
test 'Ana' = 'Ana'
printf 'Estado: %s\n' "$?"
```

## 10. Qué es `[ ... ]`

En Bash, `[` es también un builtin.

Esta forma:

```bash
[ 'Ana' = 'Ana' ]
```

es una forma alternativa de utilizar una prueba condicional.

El `]` final es obligatorio cuando usas la forma `[`. No es decoración visual.

## 11. Los espacios en `[ ... ]` son parte de la sintaxis práctica

Correcto:

```bash
[ "$nombre" = 'Ana' ]
```

Incorrecto:

```text
["$nombre" = 'Ana']
```

Como `[` recibe argumentos, necesitas separar cada operador y operando.

Regla inicial:

```text
[ ESPACIO expresión ESPACIO ]
```

## 12. Comparar cadenas con `test` o `[ ]`

```bash
nombre='Ana'

if [ "$nombre" = 'Ana' ]; then
    printf 'Coincide\n'
fi
```

Para igualdad de cadenas con `[ ... ]`, usa aquí `=`.

Para desigualdad:

```bash
[ "$nombre" != 'Ana' ]
```

## 13. Por qué citamos variables en `[ ... ]`

Con la forma clásica `[ ... ]`, una expansión sin comillas puede cambiar el número de argumentos.

Por eso preferimos:

```bash
[ "$nombre" = 'Ana' ]
```

y no:

```text
[ $nombre = 'Ana' ]
```

Especialmente mientras estás aprendiendo, cita las expansiones de texto dentro de `[ ... ]`.

## 14. Cadena vacía y no vacía

Prueba de cadena no vacía:

```bash
[ -n "$texto" ]
```

Prueba de cadena vacía:

```bash
[ -z "$texto" ]
```

Ejemplo:

```bash
texto=''

if [ -z "$texto" ]; then
    printf 'La cadena está vacía\n'
fi
```

## 15. Comparaciones numéricas con `[ ... ]`

Para enteros:

| Operador | Significado |
|---|---|
| `-eq` | igual |
| `-ne` | distinto |
| `-lt` | menor que |
| `-le` | menor o igual |
| `-gt` | mayor que |
| `-ge` | mayor o igual |

Ejemplo:

```bash
numero=8

if [ "$numero" -gt 5 ]; then
    printf 'El número es mayor que 5\n'
fi
```

## 16. No uses comparación de texto como si fuera comparación numérica

Esto:

```bash
[ "$a" = "$b" ]
```

compara cadenas.

Esto:

```bash
[ "$a" -eq "$b" ]
```

compara enteros.

Son operaciones distintas.

## 17. Pruebas básicas de archivos

Algunas pruebas útiles:

| Prueba | Pregunta |
|---|---|
| `-e ruta` | ¿existe? |
| `-f ruta` | ¿es archivo regular? |
| `-d ruta` | ¿es directorio? |
| `-r ruta` | ¿es legible para el proceso actual? |
| `-w ruta` | ¿es escribible para el proceso actual? |
| `-x ruta` | ¿es ejecutable/buscable según el tipo y permisos? |

Ejemplo dentro del laboratorio:

```bash
archivo=~/linux-lab/modulo-26-condiciones/nota.txt

if [ -f "$archivo" ]; then
    printf 'Existe como archivo regular\n'
fi
```

## 18. `-e` y `-f` no preguntan exactamente lo mismo

`-e` pregunta si la ruta existe.

`-f` pregunta si existe y es un archivo regular.

Un directorio puede cumplir `-e` y no cumplir `-f`.

## 19. Introducción a `[[ ... ]]`

Bash ofrece el comando compuesto:

```bash
[[ expresión ]]
```

Ejemplo:

```bash
nombre='Ana María'

if [[ $nombre == 'Ana María' ]]; then
    printf 'Coincide\n'
fi
```

Dentro de `[[ ... ]]`, las palabras no sufren *word splitting* ni expansión de nombres de archivo como en una expansión normal de comando.

## 20. `[[ ... ]]` no es POSIX `sh`

`[[ ... ]]` es una característica de Bash y otros shells compatibles, pero no pertenece a la sintaxis POSIX básica de `sh`.

Si el script declara:

```bash
#!/usr/bin/env bash
```

puedes usar características de Bash conscientemente.

Si necesitas portabilidad estricta a `/bin/sh`, debes diseñar con otras construcciones.

## 21. `[ ... ]` frente a `[[ ... ]]`

| Característica | `[ ... ]` | `[[ ... ]]` |
|---|---|---|
| Forma | builtin `test` | comando compuesto de Bash |
| Requiere `]` separado | sí | usa `]]` como sintaxis |
| Word splitting de expansiones | requiere cuidado/quoting | no dentro de la expresión |
| Globbing accidental de expansiones | requiere cuidado/quoting | no |
| Portabilidad POSIX | mucho mayor | no POSIX |
| Patrones con `==` | no es la razón principal para usarlo | sí, RHS sin citar puede ser patrón |

Recomendación del manual:

- si escribes específicamente para Bash, `[[ ... ]]` suele ofrecer semántica más segura y clara para cadenas;
- si el objetivo es portabilidad POSIX, aprende `test`/`[ ... ]` correctamente.

## 22. Igualdad literal dentro de `[[ ... ]]`

```bash
nombre='Ana'

if [[ $nombre == 'Ana' ]]; then
    printf 'Coincide literalmente\n'
fi
```

Cuando el lado derecho se cita, se trata literalmente.

## 23. Patrones dentro de `[[ ... ]]`

Cuando el lado derecho de `==` no está citado, Bash puede tratarlo como patrón.

```bash
archivo='reporte.txt'

if [[ $archivo == *.txt ]]; then
    printf 'Termina en .txt\n'
fi
```

Aquí `*.txt` es un patrón, no el nombre literal de un archivo.

No confundas este patrón con una expansión de nombres de archivo del directorio: dentro de `[[ ... ]]` tiene semántica de comparación de patrón.

## 24. Operadores lógicos dentro de `[[ ... ]]`

Puedes combinar condiciones:

```bash
numero=8

if [[ $numero -ge 1 && $numero -le 10 ]]; then
    printf 'Está entre 1 y 10\n'
fi
```

También existe `||` para OR y `!` para negación.

Estas operaciones están dentro de la expresión condicional de `[[ ... ]]`, no son exactamente la misma lista de comandos estudiada en el módulo anterior, aunque el significado lógico resulte relacionado.

## 25. Evitar `-a` y `-o` en expresiones complejas de `test`

`test` y `[` admiten formas históricas con `-a` y `-o`, pero su análisis depende del número de argumentos y puede ser confuso.

Para código Bash nuevo, este manual prefiere:

```bash
[[ condición1 && condición2 ]]
```

o varias pruebas combinadas a nivel de comandos cuando corresponda.

## 26. Qué es `case`

`case` selecciona una acción según el valor de una palabra y patrones.

Estructura:

```bash
case "$valor" in
    patron1)
        acciones
        ;;
    patron2)
        acciones
        ;;
    *)
        acciones_por_defecto
        ;;
esac
```

`esac` es `case` escrito al revés.

## 27. Primer `case`

```bash
opcion='ver'

case "$opcion" in
    ver)
        printf 'Elegiste ver\n'
        ;;
    salir)
        printf 'Elegiste salir\n'
        ;;
    *)
        printf 'Opción desconocida\n'
        ;;
esac
```

## 28. Qué significa `*` en `case`

El patrón:

```text
*
```

coincide con cualquier valor que no haya coincidido antes.

Funciona como caso predeterminado.

## 29. Varias alternativas en un patrón

Puedes usar `|` para varias alternativas:

```bash
respuesta='s'

case "$respuesta" in
    s|S)
        printf 'Respuesta afirmativa\n'
        ;;
    n|N)
        printf 'Respuesta negativa\n'
        ;;
    *)
        printf 'Respuesta no reconocida\n'
        ;;
esac
```

En este ejemplo solo clasificamos texto; no ejecutamos acciones de impacto.

## 30. `case` frente a muchos `elif`

Cuando comparas una misma variable contra varias opciones o patrones, `case` suele resultar más legible.

Cuando las condiciones son heterogéneas —por ejemplo, números, archivos y varias pruebas diferentes— `if` puede ser más natural.

No existe una regla de que uno sea siempre mejor que el otro.

## 31. Introducción a aritmética con `(( ... ))`

Bash dispone del comando compuesto aritmético:

```bash
(( expresión ))
```

Ejemplo:

```bash
numero=8

if (( numero > 5 )); then
    printf 'Mayor que 5\n'
fi
```

Dentro de este contexto se utilizan operadores aritméticos como `>`, `<`, `==`, `!=`, `+`, `-`, `*`, `/` y `%`.

## 32. Estado de `(( ... ))`

Este punto puede parecer invertido al principio.

`(( expresión ))` devuelve:

```text
estado 0 → si el valor aritmético de la expresión es distinto de 0
estado 1 → si el valor aritmético de la expresión es 0
```

Ejemplo:

```bash
(( 5 > 2 ))
```

La expresión vale `1`, por lo que el comando termina con éxito.

En cambio:

```bash
(( 2 > 5 ))
```

la expresión vale `0`, por lo que el comando devuelve estado `1`.

## 33. `(( ... ))` frente a `$(( ... ))`

No son lo mismo.

`(( ... ))` evalúa aritmética como comando y produce un estado:

```bash
if (( 4 < 9 )); then
    printf 'verdadero\n'
fi
```

`$(( ... ))` es **expansión aritmética** y produce un valor que puede usarse como texto/argumento:

```bash
resultado=$(( 4 + 9 ))
printf 'Resultado: %s\n' "$resultado"
```

Resultado:

```text
Resultado: 13
```

## 34. Aritmética entera

La aritmética de Bash trabaja con enteros de ancho fijo.

Ejemplo:

```bash
resultado=$(( 7 / 2 ))
printf '%s\n' "$resultado"
```

El resultado aritmético entero es `3`, no `3.5`.

No confundas este comportamiento con Python, donde `/` produce división de punto flotante.

## 35. División entre cero

Una división aritmética entre cero es un error.

No la uses como ejercicio.

Valida el divisor antes de dividir cuando provenga de datos variables.

## 36. Comparación recomendada según el dato

Modelo inicial:

```text
texto portátil                 → [ "$a" = "$b" ]
texto en script Bash           → [[ $a == "$b" ]]
entero con test                → [ "$a" -gt "$b" ]
entero en contexto Bash        → (( a > b ))
archivo/directorio             → [ -f "$ruta" ] o [[ -f $ruta ]]
varias opciones/patrones       → case
```

No es una tabla absoluta; es una guía pedagógica inicial.

## 37. Preparar el laboratorio

```bash
test -d ~/linux-lab && \
cd ~/linux-lab && \
mkdir -p modulo-26-condiciones && \
cd modulo-26-condiciones && pwd
```

Etiqueta de práctica: **creación en laboratorio**.

## 38. Práctica A — primer `if`

Crea `condicion_true.sh`:

```bash
#!/usr/bin/env bash

if true; then
    printf 'La condición fue verdadera\n'
fi
```

Valida:

```bash
bash -n condicion_true.sh
```

Ejecuta:

```bash
bash condicion_true.sh
```

## 39. Práctica B — `if` y `else`

Crea:

```bash
#!/usr/bin/env bash

if false; then
    printf 'Éxito\n'
else
    printf 'La condición devolvió un estado no-cero\n'
fi
```

Antes de ejecutar, predice qué línea aparecerá.

## 40. Práctica C — comparación de texto

```bash
#!/usr/bin/env bash

nombre='Ana María'

if [[ $nombre == 'Ana María' ]]; then
    printf 'El nombre coincide\n'
else
    printf 'No coincide\n'
fi
```

Explica por qué esta práctica usa `[[ ... ]]` y por qué el script declara Bash.

## 41. Práctica D — comparación numérica

```bash
#!/usr/bin/env bash

numero=8

if (( numero > 5 )); then
    printf 'El número es mayor que 5\n'
else
    printf 'El número no es mayor que 5\n'
fi
```

Cambia únicamente `numero` a `3` y predice el resultado.

## 42. Práctica E — probar archivo y directorio

Prepara datos locales:

```bash
printf 'nota de práctica\n' > nota.txt
mkdir -p carpeta_prueba
```

Después:

```bash
if [[ -f nota.txt ]]; then
    printf 'nota.txt es un archivo regular\n'
fi

if [[ -d carpeta_prueba ]]; then
    printf 'carpeta_prueba es un directorio\n'
fi
```

`>` sobrescribe `nota.txt` si ya existe. Por eso esta práctica se realiza únicamente sobre el archivo de laboratorio creado para este módulo.

## 43. Práctica F — `case`

```bash
#!/usr/bin/env bash

opcion=${1:-ayuda}

case "$opcion" in
    ver)
        printf 'Modo: ver\n'
        ;;
    ayuda)
        printf 'Modo: ayuda\n'
        ;;
    *)
        printf 'Opción no reconocida: %s\n' "$opcion"
        ;;
esac
```

Prueba:

```bash
bash opciones.sh
bash opciones.sh ver
bash opciones.sh otra
```

## 44. Práctica G — `elif`

```bash
#!/usr/bin/env bash

numero=${1:-0}

if (( numero > 0 )); then
    printf 'positivo\n'
elif (( numero < 0 )); then
    printf 'negativo\n'
else
    printf 'cero\n'
fi
```

Para esta práctica usa argumentos enteros sencillos: `5`, `-2` y `0`.

La validación de entradas no numéricas se estudiará con mayor profundidad posteriormente.

## 45. Práctica H — usar una orden directamente

```bash
#!/usr/bin/env bash

if cd ~/linux-lab; then
    printf 'Entrada correcta\n'
    pwd
else
    printf 'No se pudo entrar al laboratorio\n' >&2
    exit 1
fi
```

Esta práctica demuestra que `if` no necesita obligatoriamente `test`, `[ ]` o `[[ ]]`.

## 46. Errores frecuentes

| Error | Por qué ocurre | Corrección mínima |
|---|---|---|
| `["$a" = "$b"]` | faltan argumentos separados | `[ "$a" = "$b" ]` |
| olvidar `]` | `[` necesita el cierre como argumento | añade ` ]` |
| usar `=` pensando en números | compara cadenas | usa `-eq` o `(( ... ))` |
| usar `-gt` para texto | operador numérico | usa comparación de cadenas |
| olvidar `fi` | el `if` queda sin cerrar | añade `fi` |
| olvidar `;;` en un `case` básico | la rama no termina como se espera | añade `;;` |
| olvidar `esac` | `case` queda sin cerrar | añade `esac` |
| ejecutar script con `sh` aunque usa `[[ ]]` | `[[ ]]` no es POSIX `sh` | ejecútalo con Bash |
| citar `*.txt` en RHS de `[[ == ]]` esperando patrón | citado se interpreta literalmente | deja el patrón sin citar si buscas patrón |
| dejar expansión sin comillas dentro de `[ ... ]` | puede alterar argumentos | cita variables de texto |
| confundir `(( ... ))` con `$(( ... ))` | uno es comando; otro expansión | elige según necesites estado o valor |
| encadenar una acción peligrosa dentro de una condición | automatiza un cambio sin revisión | practica con consultas/datos de laboratorio |

## 47. Detección de error 1

Analiza:

```bash
nombre='Ana María'

if [ $nombre = 'Ana María' ]; then
    printf 'Coincide\n'
fi
```

Problema: `$nombre` puede expandirse a más de un argumento.

Corrección mínima:

```bash
if [ "$nombre" = 'Ana María' ]; then
    printf 'Coincide\n'
fi
```

## 48. Detección de error 2

Analiza:

```bash
numero=10

if [ "$numero" > 5 ]; then
    printf 'Mayor\n'
fi
```

Problema: `>` aquí no es la forma numérica adecuada para `test` y, fuera de contextos protegidos, también tiene significado de redirección para la shell.

**No ejecutes el ejemplo incorrecto:** Bash interpreta `> 5` como una redirección y puede crear o vaciar un archivo llamado `5` en el directorio actual. Analízalo únicamente como ejercicio de detección de errores.

Corrección con `[ ... ]`:

```bash
if [ "$numero" -gt 5 ]; then
    printf 'Mayor\n'
fi
```

Corrección Bash aritmética:

```bash
if (( numero > 5 )); then
    printf 'Mayor\n'
fi
```

## 49. Detección de error 3

Analiza:

```bash
if [[ $archivo == '*.txt' ]]; then
    printf 'TXT\n'
fi
```

Si querías un patrón para cualquier nombre terminado en `.txt`, las comillas lo convierten en texto literal.

Corrección:

```bash
if [[ $archivo == *.txt ]]; then
    printf 'TXT\n'
fi
```

## 50. Método para elegir una estructura

Antes de escribir la condición:

1. identifica qué dato estás evaluando;
2. decide si es texto, entero, archivo/directorio o estado de una orden;
3. decide si el script depende específicamente de Bash;
4. usa una sola condición pequeña al principio;
5. predice qué estado debería producir;
6. añade `else` solo si necesitas manejar el caso contrario;
7. usa `case` cuando una misma entrada tiene varias alternativas claras;
8. valida con `bash -n`;
9. prueba primero con datos del laboratorio;
10. explica la condición con tus propias palabras.

## 51. Práctica independiente

Crea `clasificar_entrada.sh`.

Debe:

1. usar Bash;
2. recibir un primer argumento;
3. usar `${1:-ayuda}` como valor predeterminado;
4. usar `case` para reconocer `archivo`, `directorio` y `ayuda`;
5. si recibe `archivo`, comprobar con `[[ -f ... ]]` un archivo de práctica dentro del directorio actual;
6. si recibe `directorio`, comprobar con `[[ -d ... ]]` una carpeta de práctica;
7. usar al menos un `if`;
8. no usar `sudo`;
9. no borrar ni modificar archivos ajenos al laboratorio;
10. pasar `bash -n`;
11. poder explicarse línea por línea.

Primero escribe tu versión. No copies directamente las prácticas anteriores.

## 52. Mini evaluación

1. ¿qué interpreta `if` como verdadero en Bash? A) estado `0` B) cualquier texto impreso
2. ¿`if` necesita obligatoriamente `[ ... ]`? A) Sí B) No
3. ¿`[` es una orden/builtin en Bash? A) Sí B) No
4. ¿el `]` final de `[ ... ]` puede omitirse? A) Sí B) No
5. ¿qué operador compara enteros por igualdad con `test`? A) `-eq` B) `=`
6. ¿qué comprueba `-d`? A) directorio B) cadena vacía
7. ¿qué comprueba `-f`? A) archivo regular B) número
8. ¿`[[ ... ]]` pertenece a la sintaxis POSIX básica de `sh`? A) Sí B) No
9. dentro de `[[ ... ]]`, ¿una expansión sufre word splitting normal? A) Sí B) No
10. en `[[ $archivo == *.txt ]]`, ¿`*.txt` actúa como patrón? A) Sí B) No
11. ¿`case` es útil para varias alternativas de una misma entrada? A) Sí B) No
12. ¿`(( 5 > 2 ))` termina normalmente con estado `0`? A) Sí B) No
13. ¿`$(( 5 + 2 ))` devuelve el valor aritmético para expansión? A) Sí B) No
14. ¿Bash realiza división entera en su aritmética? A) Sí B) No
15. ¿`[ "$a" = "$b" ]` y `(( a == b ))` expresan exactamente el mismo tipo de comparación? A) Sí B) No

## 53. Registro de aprendizaje

```text
`if` decide usando:
`then` significa:
`else` sirve para:
`elif` sirve para:
`fi` cierra:
`test` devuelve:
`[` es:
¿por qué necesito espacios en `[ ... ]`?:
`-eq` significa:
`-gt` significa:
`-f` comprueba:
`-d` comprueba:
`[[ ... ]]` se diferencia de `[ ... ]` porque:
`case` sirve para:
`esac` cierra:
`(( ... ))` sirve para:
`$(( ... ))` sirve para:
Algo que todavía confundo:
Estado: EN APRENDIZAJE / PRACTICADO
```

## 54. Puerta de dominio

Este módulo no se considera dominado por contestar una sola evaluación.

Para avanzar como **DOMINADO** deberás poder:

1. explicar con tus palabras por qué `if` trabaja con estados;
2. escribir un `if/else` sin copiar;
3. detectar un error de espacios en `[ ... ]`;
4. elegir correctamente entre comparación de texto y numérica;
5. escribir un `case` pequeño sin copiar;
6. explicar la diferencia entre `(( ... ))` y `$(( ... ))`;
7. resolver otra práctica en una sesión posterior.

## 55. Fuentes y límites

Fuentes principales:

- GNU Bash Reference Manual — Conditional Constructs: https://www.gnu.org/software/bash/manual/html_node/Conditional-Constructs.html
- GNU Bash Reference Manual — Bash Conditional Expressions: https://www.gnu.org/software/bash/manual/html_node/Bash-Conditional-Expressions.html
- GNU Bash Reference Manual — Bourne Shell Builtins (`test` y `[`): https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html
- GNU Bash Reference Manual — Shell Arithmetic: https://www.gnu.org/software/bash/manual/html_node/Shell-Arithmetic.html

Puntos verificados documentalmente:

- `test` y `[` devuelven `0` para una expresión verdadera y `1` para una falsa;
- con `[`, el último argumento debe ser `]`;
- `[[ ... ]]` es un comando compuesto de Bash;
- dentro de `[[ ... ]]` no se realizan word splitting ni filename expansion sobre sus palabras;
- con `[[ ... ]]`, el lado derecho sin citar de `==` puede actuar como patrón;
- `(( expresión ))` devuelve estado `0` cuando la expresión aritmética evalúa a un valor distinto de cero y estado `1` cuando evalúa a cero;
- la aritmética de Bash utiliza enteros de ancho fijo y detecta división entre cero.

Se posponen:

- expresiones regulares con `=~` en profundidad;
- `BASH_REMATCH`;
- `select`;
- bucles formales;
- validación completa de entrada numérica;
- funciones y `return`;
- arrays;
- `set -e`, `set -u` y `pipefail` como políticas;
- `trap`.

**Estado de la lección:** redactada y revisada documentalmente contra el GNU Bash Reference Manual disponible en 2026. Las prácticas son locales, no destructivas y no requieren privilegios.

Siguiente módulo por redactar: **Módulo 27 — Bucles, lectura de líneas y nombres de archivo seguros**.
