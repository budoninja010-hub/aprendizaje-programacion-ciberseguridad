# Módulo 24 — Variables, entrada, argumentos, expansiones y quoting en Bash

Manual Maestro de Linux y Shell Scripting — Edición 2026 · v3 · Vigesimocuarta entrega.

[Índice del manual](README.md) · [← Módulo 23](modulo-23-primer-script-bash-shebang.md) · [Arquitectura](00-indice-arquitectura.md) · [Módulo 25 →](modulo-25-codigos-salida-composicion-ordenes.md)

## 1. Qué aprenderás

Al terminar este módulo podrás:

- crear variables en Bash;
- diferenciar asignación y expansión;
- usar `${variable}`;
- entender por qué una asignación no lleva espacios alrededor de `=`;
- leer entrada con `read -r`;
- recibir argumentos posicionales;
- reconocer `$0`, `$1`, `$2`, `$#`, `"$@"` y `$?`;
- explicar la diferencia entre comillas simples, dobles y ausencia de comillas;
- evitar errores por espacios y expansión de nombres de archivo;
- distinguir `"$@"` de `"$*"`;
- usar sustitución de comandos `$(...)` de forma básica;
- mantener datos separados de código.

Conocimientos previos:
- primer script Bash;
- shebang;
- `printf`;
- archivos;
- permisos;
- pipes y redirecciones.

**Seguridad:** las prácticas son locales y no usan privilegios. No colocaremos contraseñas, tokens, claves ni otros secretos en variables, argumentos o scripts. Los argumentos de línea de comandos pueden quedar visibles en procesos, historial o logs según el entorno.

## 2. Qué es una variable

Una variable asocia un nombre con un valor.

Ejemplo:

```bash
nombre='Ana'
```

Aquí:

- `nombre` = nombre de la variable;
- `=` = asignación;
- `'Ana'` = valor.

Después puedes consultar su valor mediante expansión:

```bash
printf '%s\n' "$nombre"
```

## 3. Asignar no es expandir

Estas dos operaciones son distintas:

```bash
nombre='Ana'
```

asigna.

En cambio:

```bash
printf '%s\n' "$nombre"
```

expande el valor.

Modelo:

```text
asignación → guardar
expansión  → obtener/usar
```

## 4. No hay espacios alrededor de =

Correcto:

```bash
edad=15
```

Incorrecto:

```text
edad = 15
```

Bash interpretaría eso como palabras de una orden, no como una asignación.

Regla inicial:

```text
nombre=valor
```

sin espacios alrededor de `=`.

## 5. Nombres de variables

Un nombre sencillo puede contener:

- letras;
- números;
- guion bajo.

Pero no debe comenzar con número.

Ejemplos válidos:

```text
nombre
edad2
nombre_usuario
```

Ejemplos no válidos como nombres simples de variables:

```text
2edad
nombre-usuario
```

Para aprender, usa nombres descriptivos.

## 6. Convención de nombres

En scripts educativos usaremos:

```text
nombre_usuario
archivo_salida
contador
```

y reservaremos MAYÚSCULAS principalmente para variables de entorno o constantes convencionales:

```text
HOME
PATH
USER
```

No es una regla sintáctica absoluta, sino una convención útil.

## 7. Expansión con $

Si:

```bash
nombre='Ana'
```

entonces:

```bash
printf '%s\n' "$nombre"
```

expande a:

```text
Ana
```

El símbolo `$` indica que Bash debe realizar una expansión de parámetro en este contexto.

## 8. Forma con llaves

También puedes escribir:

```bash
printf '%s\n' "${nombre}"
```

Las llaves ayudan a delimitar el nombre.

Ejemplo:

```bash
archivo='reporte'
printf '%s\n' "${archivo}.txt"
```

Salida:

```text
reporte.txt
```

## 9. Comillas dobles

Las comillas dobles:

```text
" "
```

permiten varias expansiones de Bash dentro del texto.

Ejemplo:

```bash
nombre='Ana'
printf '%s\n' "Hola, $nombre"
```

Salida:

```text
Hola, Ana
```

## 10. Comillas simples

Las comillas simples:

```text
' '
```

preservan el contenido de forma literal dentro de ellas.

Ejemplo:

```bash
nombre='Ana'
printf '%s\n' 'Hola, $nombre'
```

Salida:

```text
Hola, $nombre
```

La variable no se expande.

## 11. Sin comillas

Ejemplo:

```bash
texto='uno dos'
printf '%s\n' $texto
```

La expansión sin comillas puede sufrir:

- división en palabras;
- expansión de nombres de archivo (*globbing*).

Eso puede cambiar el número de argumentos que recibe el comando.

Por eso la regla inicial será:

> Si una expansión representa texto o una ruta, normalmente protégela con comillas dobles.

## 12. Quoting contextual, no regla ciega

No diremos:

> “toda expansión siempre debe llevar comillas dobles”.

Hay contextos donde las reglas son distintas, por ejemplo:

- dentro de `[[ ... ]]`;
- en contextos aritméticos `(( ... ))`;
- determinadas asignaciones.

Pero para comandos normales y rutas, `"$variable"` es la opción inicial segura.

## 13. Ejemplo con espacios

```bash
archivo='mi documento.txt'
printf '%s\n' "$archivo"
```

se trata como un solo argumento.

Sin comillas:

```bash
printf '%s\n' $archivo
```

Bash puede dividirlo en:

```text
mi
documento.txt
```

Eso es un error frecuente.

## 14. Globbing accidental

Supón:

```bash
patron='*.txt'
```

Si usas:

```bash
printf '%s\n' $patron
```

Bash puede expandir `*.txt` a nombres reales del directorio.

Si quieres imprimir literalmente el valor:

```bash
printf '%s\n' "$patron"
```

## 15. Unquoted expansion no “ejecuta texto como código” por sí sola

Este punto es importante.

Si una variable contiene:

```text
; algo
```

una expansión normal no vuelve a analizar automáticamente ese texto como nueva sintaxis de shell.

Los riesgos típicos de expansión sin comillas son principalmente:

- word splitting;
- pathname expansion;
- opciones inesperadas.

Construcciones como `eval` sí pueden introducir una nueva interpretación y se posponen.

## 16. Variable vacía

```bash
dato=''
```

Con:

```bash
printf '<%s>\n' "$dato"
```

obtienes:

```text
<>
```

La variable existe y su valor es vacío.

No confundas:

- variable vacía;
- variable no definida.

Esa diferencia será importante al estudiar validaciones.

## 17. Variables de entorno

Bash hereda variables del entorno.

Ejemplos comunes:

```bash
printf '%s\n' "$HOME"
printf '%s\n' "$PATH"
```

No compartas `PATH`, `HOME` u otras variables completas si revelan rutas privadas innecesarias.

## 18. export

Una variable normal de shell no se exporta automáticamente a procesos hijos.

Ejemplo conceptual:

```bash
nombre='Ana'
```

Para marcar una variable para exportación:

```bash
export nombre
```

También puede escribirse:

```bash
export nombre='Ana'
```

No exportes secretos como práctica.

## 19. Variables no son tipos estrictos

Bash trata gran parte de los valores como cadenas de caracteres.

Ejemplo:

```bash
numero='12'
```

No es equivalente al sistema de tipos de Python o Java.

Más adelante veremos contextos aritméticos.

## 20. read — recibir entrada

Un script puede leer entrada del usuario.

Ejemplo:

```bash
read -r nombre
printf 'Hola, %s\n' "$nombre"
```

`read` lee una línea, pero normalmente la divide según `IFS`. Con un solo nombre de variable puede eliminar espacios iniciales y finales.

`-r` evita que las barras invertidas se interpreten como escapes por `read`, **pero no desactiva la separación por `IFS`**. Para conservar los espacios de una línea completa, utiliza:

```bash
IFS= read -r linea
printf '%s\n' "$linea"
```

`IFS=` aplica el valor vacío solo a esa invocación de `read`.

Para aprendizaje general preferiremos:

```text
read -r
```

## 21. Prompt con read -p

En Bash:

```bash
read -r -p 'Escribe tu nombre: ' nombre
printf 'Hola, %s\n' "$nombre"
```

`-p` muestra el mensaje **solo cuando la entrada procede de una terminal**; si se redirige la entrada desde un archivo o una tubería, no debe esperarse ese prompt.

Es una opción de Bash; no debes asumir que todos los shells POSIX tienen exactamente la misma opción.

## 22. No leer contraseñas como ejercicio

No pediremos contraseñas ni tokens.

Incluso cuando herramientas permiten entrada oculta, el manejo de secretos exige más cuidado.

Para practicar `read`, usa datos no sensibles:

- nombre ficticio;
- color;
- ciudad ficticia;
- número de laboratorio.

## 23. Argumentos posicionales

Si ejecutas:

```bash
./saludo.sh Ana
```

el script puede acceder al primer argumento mediante:

```text
$1
```

Ejemplo:

```bash
#!/usr/bin/env bash

printf 'Hola, %s\n' "$1"
```

## 24. $0

Dentro del script:

```text
$0
```

representa cómo fue invocado el script/comando.

Ejemplo:

```bash
printf 'Programa: %s\n' "$0"
```

No asumas que siempre contiene una ruta absoluta.

## 25. $1, $2, ...

Los primeros parámetros posicionales:

```text
$1
$2
$3
...
```

corresponden a argumentos.

Ejemplo:

```bash
./datos.sh Ana 15
```

Dentro:

```text
$1 → Ana
$2 → 15
```

Cítalos normalmente:

```bash
printf '%s\n' "$1"
```

## 26. $#

```text
$#
```

indica cuántos argumentos posicionales recibió el script.

Ejemplo:

```bash
printf 'Recibí %s argumentos\n' "$#"
```

Si ejecutas:

```bash
./script.sh uno dos tres
```

el valor será:

```text
3
```

## 27. "$@"

```text
"$@"
```

expande todos los argumentos posicionales preservándolos como argumentos separados.

Ejemplo:

```bash
./script.sh 'uno dos' tres
```

Conceptualmente:

```text
"$@" →
argumento 1: "uno dos"
argumento 2: "tres"
```

Esto es fundamental para scripts robustos.

## 28. "$*" no es igual a "$@"

Dentro de comillas dobles:

```text
"$*"
```

combina los argumentos en una sola cadena, separada normalmente por el primer carácter de `IFS`.

Mientras:

```text
"$@"
```

mantiene cada argumento separado.

Por eso, cuando quieres reenviar argumentos preservando sus límites, normalmente necesitas:

```text
"$@"
```

## 29. Ejemplo seguro para ver argumentos

Script:

```bash
#!/usr/bin/env bash

printf 'Cantidad: %s\n' "$#"

for argumento in "$@"; do
    printf '<%s>\n' "$argumento"
done
```

El bucle `for` se explicará formalmente más adelante.

Aquí solo sirve para visualizar que cada argumento permanece separado.

## 30. $* sin comillas

Evita aprender patrones como:

```text
$*
```

sin comillas para reenviar argumentos.

Puede sufrir división en palabras y globbing.

La forma recomendada para preservar argumentos es:

```text
"$@"
```

## 31. $? — estado del último comando

```text
$?
```

contiene el estado de salida del último comando ejecutado.

Ejemplo:

```bash
printf 'Hola\n'
printf 'Estado: %s\n' "$?"
```

El valor `0` normalmente indica éxito.

Los estados de salida se estudiarán en profundidad en el Módulo 25.

## 32. No sobrescribas $? accidentalmente antes de consultarlo

`$?` cambia después de cada comando.

Ejemplo:

```bash
comando
estado=$?
```

es una forma de guardar el valor.

Si ejecutas otro comando antes, `$?` ya corresponderá a ese comando posterior.

## 33. Sustitución de comandos

```text
$(comando)
```

ejecuta un comando y sustituye por su salida estándar, eliminando saltos finales según las reglas de Bash.

Ejemplo:

```bash
directorio=$(pwd)
printf 'Estoy en: %s\n' "$directorio"
```

No uses sustitución de comandos con operaciones que no comprendes.

## 34. Preferir $(...) frente a backticks

También existe la sintaxis histórica:

```text
`comando`
```

Pero este manual prioriza:

```text
$(comando)
```

porque es más legible y se anida mejor.

## 35. Expansión de parámetro con valor predeterminado

Una forma útil:

```bash
nombre=${1:-Invitado}
```

Significa conceptualmente:

- usa `$1` si tiene un valor adecuado;
- en caso contrario usa `Invitado`.

Ejemplo:

```bash
printf 'Hola, %s\n' "$nombre"
```

No estudiaremos todavía todas las formas de expansión de parámetros.

## 36. Diferencia entre unset y empty con :- 

La forma:

```text
${variable:-valor}
```

usa el valor alternativo cuando la variable está no definida o vacía.

Existen variantes con semánticas diferentes.

No las memorices todavía.

## 37. IFS — introducción

`IFS` significa **Internal Field Separator**.

Influye en determinadas operaciones de separación de palabras y en `"$*"`.

No modificaremos `IFS` en este módulo.

Solo debes saber que existe para entender por qué `"$*"` y `"$@"` no son equivalentes.

## 38. Datos no son código

Una regla central:

> trata la entrada del usuario como datos.

No construyas nuevas órdenes concatenando texto recibido para volver a interpretarlo.

Por eso no utilizaremos `eval` para procesar entrada.

`eval` se pospone porque puede reinterpretar texto como código shell.

## 39. Opciones que empiezan con -

Otro riesgo no relacionado con “ejecutar código”:

si un valor empieza por:

```text
-
```

algunos comandos pueden tratarlo como una opción.

Muchas herramientas permiten usar:

```text
--
```

para marcar el fin de opciones.

Ejemplo conceptual:

```text
comando -- "$archivo"
```

No todas las herramientas usan `--`, así que debes consultar documentación.

## 40. Preparar el laboratorio

```bash
cd ~/linux-lab
pwd
```

**Si `cd` falla, detente.** Comprueba que la ruta mostrada por `pwd` sea tu laboratorio antes de crear nada.

Primero comprueba si el nombre está ocupado:

```bash
ls -ld ./modulo-24-bash-datos
```

Si el resultado indica que no existe, crea la carpeta desde `~/linux-lab` y entra en ella:

```bash
mkdir ./modulo-24-bash-datos
cd ./modulo-24-bash-datos
pwd
```

Si la carpeta ya existe, **no la sobrescribas ni la recrees**; inspecciona su contenido antes de continuar. Detente ante cualquier error.

## 41. Práctica A — variable simple

Crea:

```text
variables.sh
```

Contenido:

```bash
#!/usr/bin/env bash

nombre='Ana'
printf 'Hola, %s\n' "$nombre"
```

Valida:

```bash
bash -n variables.sh
```

Ejecuta:

```bash
bash variables.sh
```

## 42. Explicación línea por línea

```bash
#!/usr/bin/env bash
```

selecciona Bash al ejecutar directamente.

```bash
nombre='Ana'
```

asigna texto.

```bash
printf 'Hola, %s\n' "$nombre"
```

expande la variable dentro de comillas dobles y la pasa como argumento a `printf`.

## 43. Práctica B — espacios

Modifica:

```bash
nombre='Ana María'
```

Mantén:

```bash
printf '<%s>\n' "$nombre"
```

Debe aparecer como un solo valor.

Después compara conceptualmente con la expansión sin comillas.

No necesitas adoptar la forma insegura en scripts reales.

## 44. Práctica C — read

Crea `leer_nombre.sh`:

```bash
#!/usr/bin/env bash

read -r -p 'Escribe un nombre ficticio: ' nombre
printf 'Recibí: %s\n' "$nombre"
```

Usa únicamente datos no sensibles.

## 45. Práctica D — primer argumento

Crea `argumento.sh`:

```bash
#!/usr/bin/env bash

printf 'Primer argumento: %s\n' "$1"
```

Ejecuta:

```bash
bash argumento.sh prueba
```

Después:

```bash
bash argumento.sh 'dos palabras'
```

Observa que las comillas de la shell hacen que `dos palabras` sea un solo argumento.

## 46. Práctica E — contar argumentos

Crea `contar.sh`:

```bash
#!/usr/bin/env bash

printf 'Cantidad: %s\n' "$#"
```

Ejecuta con:

- cero argumentos;
- uno;
- tres.

Predice antes el resultado.

## 47. Práctica F — "$@"

Crea `todos.sh`:

```bash
#!/usr/bin/env bash

printf 'Cantidad: %s\n' "$#"

for argumento in "$@"; do
    printf '<%s>\n' "$argumento"
done
```

Ejecuta:

```bash
bash todos.sh uno 'dos palabras' tres
```

Debe conservar tres argumentos.

No necesitas dominar aún la sintaxis del bucle; el Módulo 27 la enseñará formalmente.

## 48. Práctica G — sustitución de comandos

Crea `directorio.sh`:

```bash
#!/usr/bin/env bash

directorio=$(pwd)
printf 'Directorio: %s\n' "$directorio"
```

Ejecuta dentro del laboratorio.

No guardes rutas privadas en GitHub si contienen información personal innecesaria.

## 49. Práctica H — valor predeterminado

Crea `predeterminado.sh`:

```bash
#!/usr/bin/env bash

nombre=${1:-Invitado}
printf 'Hola, %s\n' "$nombre"
```

Ejecuta:

```bash
bash predeterminado.sh
```

y después:

```bash
bash predeterminado.sh Ana
```

Compara.

## 50. Errores frecuentes

| Error | Problema | Corrección |
|---|---|---|
| `nombre = valor` | Bash intenta ejecutar palabras como comando | Usa `nombre=valor` |
| `$variable` sin comillas en una ruta/texto | Puede dividirse o expandir globbing | Usa `"$variable"` |
| Comillas simples y esperas expansión | Preservan texto literal | Usa dobles si necesitas expansión |
| Confundes `"$*"` con `"$@"` | Uno agrupa, otro preserva argumentos | Usa `"$@"` al reenviar |
| Usas argumentos para secretos | Pueden quedar expuestos | No pases secretos por prácticas |
| Consultas `$?` después de otro comando | Ya cambió | Guárdalo inmediatamente |
| Usas `eval` con entrada | Reinterpreta texto como código | No usar en este nivel |
| Variable empieza con número | Nombre inválido | Empieza con letra o guion bajo |
| Modificas IFS sin comprender | Cambia separación | Posponer |

## 51. Método seguro con datos de entrada

1. identifica qué dato recibes;
2. no lo trates como código;
3. conserva sus límites con quoting;
4. valida cuando sea necesario;
5. no almacenes secretos en scripts;
6. no uses `eval`;
7. prueba valores con espacios;
8. prueba valores vacíos;
9. revisa resultados antes de automatizar.

## 52. Práctica independiente

Crea un script que:

1. reciba un nombre ficticio como `$1`;
2. use `${1:-Invitado}`;
3. muestre cuántos argumentos recibió;
4. muestre el directorio actual mediante `$(pwd)`;
5. use comillas dobles correctamente;
6. valide con `bash -n`.

Después explica cada línea sin copiar la explicación del manual.

## 53. Mini evaluación

1. ¿una asignación Bash lleva espacios alrededor de `=`?
   - A) Sí.
   - B) No.

2. ¿qué hace `"$variable"`?
   - A) Expande preservando el valor como una palabra en un contexto normal de comando.
   - B) Convierte el valor en código.

3. ¿las comillas simples expanden `$variable`?
   - A) Sí.
   - B) No.

4. ¿`$1` representa el primer argumento?
   - A) Sí.
   - B) No.

5. ¿`$#` representa la cantidad de argumentos?
   - A) Sí.
   - B) No.

6. ¿`"$@"` preserva argumentos separados?
   - A) Sí.
   - B) No.

7. ¿`"$*"` es idéntico a `"$@"`?
   - A) Sí.
   - B) No.

8. ¿`$(pwd)` es sustitución de comandos?
   - A) Sí.
   - B) No.

9. ¿debes usar `eval` para procesar entrada de usuario en este nivel?
   - A) Sí.
   - B) No.

10. ¿es buena práctica pasar contraseñas como argumentos de línea de comandos?
   - A) Sí.
   - B) No.

## 54. Registro de aprendizaje

```text
Una variable es:
Asignar significa:
Expandir significa:
${nombre} sirve para:
Comillas dobles:
Comillas simples:
$1 representa:
$# representa:
"$@" representa:
"$*" se diferencia porque:
$(...) sirve para:
read -r sirve para:
¿Por qué trato entrada como datos y no como código?:
Algo que todavía confundo:
Estado: EN APRENDIZAJE / PRACTICADO
```

## 55. Fuentes y límites

Clasificación y estado de los enlaces de esta sección: [catálogo de fuentes](06-catalogo-fuentes.md) (jerarquía E04, comprobación del 9 de octubre de 2026).

Fuentes principales:

- GNU Bash Reference Manual — Shell Parameters:
  https://www.gnu.org/software/bash/manual/html_node/Shell-Parameters.html
- GNU Bash — Shell Parameter Expansion:
  https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html
- GNU Bash — Quoting:
  https://www.gnu.org/software/bash/manual/html_node/Quoting.html
- GNU Bash — Command Substitution:
  https://www.gnu.org/software/bash/manual/html_node/Command-Substitution.html
- GNU Bash — Bourne Shell Builtins / read:
  https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html

Se posponen:

- aritmética;
- arrays;
- `[[ ... ]]`;
- condicionales;
- `case`;
- bucles formales;
- funciones;
- `shift`;
- getopt/getopts;
- expansiones avanzadas;
- namerefs;
- indirect expansion;
- `eval`;
- `set -u`.

**Estado de la lección:** redactada y revisada documentalmente. Las prácticas usan datos no sensibles y scripts locales.

---

**Siguiente:** [Módulo 25 — Códigos de salida y composición de órdenes en Bash](modulo-25-codigos-salida-composicion-ordenes.md) · [Volver al índice](README.md)
