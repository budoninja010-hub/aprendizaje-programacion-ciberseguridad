# Módulo 27 — Bucles, lectura de líneas y nombres de archivo seguros

Manual Maestro de Linux y Shell Scripting — Edición 2026 · v3 · Vigesimoséptima entrega.

[Estado actual](README.md) · [Módulo anterior](modulo-26-if-test-condicionales-case-aritmetica.md) · [Arquitectura](00-indice-arquitectura.md)

## 1. Qué aprenderás

Al terminar este módulo podrás:

- explicar para qué sirve un bucle;
- escribir bucles `for`, `while` y `until`;
- usar `break` y `continue` conscientemente;
- recorrer argumentos con `for argumento in "$@"`;
- recorrer nombres de archivo mediante globbing sin analizar la salida de `ls`;
- explicar por qué `for archivo in $(ls)` es un patrón frágil;
- leer un archivo línea por línea con `while IFS= read -r linea`;
- explicar qué hacen `IFS=` y `read -r`;
- evitar el patrón innecesario `cat archivo | while read ...`;
- reconocer el efecto de una tubería sobre el entorno de un bucle;
- usar un contador aritmético sencillo;
- reconocer cuándo un bucle puede convertirse accidentalmente en infinito;
- procesar datos de laboratorio con espacios sin romper sus límites;
- distinguir una práctica Bash de una solución estrictamente POSIX.

Conocimientos previos:

- variables y quoting;
- `"$@"`;
- códigos de salida;
- `if`, `[[ ... ]]` y aritmética `(( ... ))`;
- expansión de nombres de archivo;
- archivos, rutas y redirecciones.

**Seguridad:** todas las prácticas se limitan a `~/linux-lab`. Los bucles pueden repetir una acción muchas veces, así que aquí solo repetiremos operaciones de lectura, impresión y creación controlada de archivos de práctica. No se usan bucles para borrar, cambiar permisos, administrar servicios, discos, usuarios, red o cortafuegos.

## 2. Qué es un bucle

Un bucle permite repetir una acción.

Modelo:

```text
datos o condición
       ↓
repetir una o más órdenes
       ↓
detenerse cuando corresponda
```

Los bucles principales de este módulo son:

- `for`: recorrer elementos;
- `while`: repetir mientras una condición tenga éxito;
- `until`: repetir mientras una condición no tenga éxito.

## 3. Primer `for`

```bash
for palabra in uno dos tres; do
    printf '%s\n' "$palabra"
done
```

Resultado:

```text
uno
dos
tres
```

## 4. Explicación línea por línea

```bash
for palabra in uno dos tres; do
```

`for` inicia el bucle. `palabra` es la variable que recibe cada elemento. `in` introduce la lista. `do` inicia el cuerpo.

```bash
    printf '%s\n' "$palabra"
```

usa el valor actual de la variable. Las comillas dobles preservan el elemento como un solo argumento.

```bash
done
```

cierra el bucle.

## 5. Una iteración

Cada repetición del cuerpo se llama **iteración**.

En:

```bash
for n in 1 2 3; do
    printf '%s\n' "$n"
done
```

hay tres iteraciones.

## 6. Elementos con espacios

```bash
for nombre in 'Ana María' 'Luis Pérez'; do
    printf '<%s>\n' "$nombre"
done
```

Cada texto citado es un elemento independiente, aunque contenga espacios.

## 7. Recorrer argumentos con `"$@"`

Este patrón conecta con el Módulo 24:

```bash
for argumento in "$@"; do
    printf '<%s>\n' "$argumento"
done
```

`"$@"` conserva cada argumento recibido por el script como un elemento separado.

Si ejecutas:

```bash
bash argumentos.sh uno 'dos palabras' tres
```

el bucle realiza tres iteraciones, no cuatro.

## 8. Forma abreviada de `for` con parámetros posicionales

En Bash, si omites `in ...`, `for nombre; do` recorre los parámetros posicionales como si usara `"$@"`.

```bash
for argumento; do
    printf '<%s>\n' "$argumento"
done
```

En este manual seguiremos mostrando `in "$@"` durante el aprendizaje porque hace la intención más visible.

## 9. Globbing para recorrer archivos

Si el directorio contiene archivos `.txt`, Bash puede expandir:

```bash
./*.txt
```

Ejemplo:

```bash
for archivo in ./*.txt; do
    printf 'Archivo: %s\n' "$archivo"
done
```

Los nombres resultantes del glob se conservan como elementos separados, incluso si contienen espacios.

## 10. Por qué usamos `./*.txt`

El prefijo `./` tiene dos ventajas pedagógicas:

1. deja claro que buscamos en el directorio actual;
2. un nombre como `-opcion.txt` queda representado como `./-opcion.txt`, por lo que es menos probable que una herramienta lo confunda con una opción.

Aun así, cuando una orden admita `--`, conviene usarlo para marcar el fin de opciones.

## 11. No analices la salida de `ls`

Evita:

```text
for archivo in $(ls)
```

Problemas:

- la sustitución de comandos produce texto, no una colección fiable de nombres de archivo;
- el resultado puede sufrir división en palabras;
- los espacios, tabulaciones y saltos de línea de nombres válidos pueden romper el recorrido;
- la presentación de `ls` fue diseñada principalmente para mostrar información, no como interfaz de datos para scripts.

Para archivos del directorio actual, prefiere globbing:

```bash
for archivo in ./*; do
    ...
done
```

## 12. Qué ocurre si un glob no encuentra coincidencias

Por defecto en Bash, si un patrón como:

```text
./*.txt
```

no encuentra coincidencias y `nullglob` no está activado, el patrón puede permanecer sin expandir.

Por eso una práctica robusta debe comprobar que la ruta exista antes de procesarla.

Ejemplo:

```bash
for archivo in ./*.txt; do
    [[ -e $archivo ]] || continue
    printf '%s\n' "$archivo"
done
```

### Precisión: enlaces simbólicos rotos

`[[ -e $archivo ]]` es falso para un enlace simbólico cuyo destino ya no existe. Si quieres **incluir los nombres de enlaces simbólicos rotos**, utiliza:

```bash
for archivo in ./*.txt; do
    [[ -e $archivo || -L $archivo ]] || continue
    printf '%s\n' "$archivo"
done
```

- `-e` comprueba que la ruta resuelva a un objeto existente.
- `-L` comprueba si la ruta es un enlace simbólico, aunque su destino no exista.
- `|| continue` evita procesar el patrón literal cuando no hubo coincidencias.

Si tu objetivo es trabajar **solo con archivos regulares accesibles**, usa `[[ -f $archivo ]]` en lugar de afirmar que `-e` incluye todos los nombres. El filtro adecuado depende de la tarea.

### Alternativa avanzada: `nullglob`

En Bash, `shopt -s nullglob` hace que un patrón sin coincidencias se expanda a cero palabras, en lugar de quedar literal. Esta opción modifica el comportamiento de expansión en la shell actual; no la actives indiscriminadamente en scripts existentes. La dejamos como alternativa conceptual y conservamos el filtro explícito en las prácticas básicas.

## 13. `continue`

`continue` salta el resto de la iteración actual y pasa a la siguiente.

Ejemplo:

```bash
for n in 1 2 3; do
    if (( n == 2 )); then
        continue
    fi
    printf '%s\n' "$n"
done
```

Salida:

```text
1
3
```

## 14. `break`

`break` termina el bucle actual.

```bash
for n in 1 2 3 4; do
    if (( n == 3 )); then
        break
    fi
    printf '%s\n' "$n"
done
```

Salida:

```text
1
2
```

## 15. Primer `while`

`while` repite su cuerpo mientras la condición produzca estado `0`.

```bash
contador=1

while (( contador <= 3 )); do
    printf '%s\n' "$contador"
    (( contador += 1 ))
done
```

## 16. Explicación del contador

```bash
contador=1
```

establece el valor inicial.

```bash
while (( contador <= 3 )); do
```

comprueba la condición antes de cada iteración.

```bash
(( contador += 1 ))
```

suma uno.

Sin una actualización que permita que la condición cambie, el bucle podría no terminar.

## 17. Riesgo de bucle infinito

Ejemplo conceptual que **no necesitas ejecutar**:

```text
while true; do
    acción
done
```

Puede repetirse indefinidamente.

Antes de ejecutar un `while`, identifica:

- condición inicial;
- qué cambia en cada iteración;
- en qué momento la condición dejará de cumplirse;
- cómo detenerías manualmente la prueba si cometieras un error.

## 18. `until`

`until` repite mientras la condición tenga un estado no-cero y se detiene cuando la condición tiene éxito.

```bash
contador=1

until (( contador > 3 )); do
    printf '%s\n' "$contador"
    (( contador += 1 ))
done
```

Produce:

```text
1
2
3
```

## 19. `while` y `until` expresan ideas opuestas

```text
while condición  → repite mientras sea verdadera
until condición  → repite hasta que sea verdadera
```

Elige la forma que exprese con mayor claridad la intención.

## 20. Leer un archivo línea por línea

Patrón Bash recomendado para una lectura básica:

```bash
while IFS= read -r linea; do
    printf '<%s>\n' "$linea"
done < datos.txt
```

Este patrón conserva mucho mejor el contenido de cada línea.

## 21. Qué hace `read`

`read` lee datos de la entrada estándar y los asigna a variables.

```bash
read -r linea
```

lee una línea y la guarda en `linea`.

## 22. Por qué usamos `-r`

Sin `-r`, `read` puede tratar la barra invertida `\` como carácter de escape.

Con:

```bash
read -r linea
```

la barra invertida se conserva como parte de los datos.

Para lectura general de texto, este manual prefiere `read -r`.

## 23. Qué hace `IFS=` delante de `read`

`IFS` es el separador interno de campos.

Al escribir:

```bash
IFS= read -r linea
```

asignamos un `IFS` vacío únicamente para esa invocación de `read`, evitando que se eliminen separadores de campo iniciales o finales de la línea de la forma habitual.

Modelo:

```text
IFS=    → no recortar por separadores de campo
read -r → no tratar \ como escape
```

## 24. Redirección del archivo hacia el bucle

```bash
done < datos.txt
```

conecta el archivo con la entrada estándar del bucle.

Así `read` toma una línea en cada iteración.

## 25. No necesitas `cat` para este caso

Evita aprender:

```text
cat datos.txt | while read linea; do
    ...
done
```

Para leer directamente un archivo, es más claro:

```bash
while IFS= read -r linea; do
    ...
done < datos.txt
```

Además evita introducir una tubería innecesaria.

## 26. Bucles dentro de tuberías y subshells

En Bash, los comandos de una tubería normalmente se ejecutan en subshells, con excepciones configurables como `lastpipe`.

Por eso este patrón puede sorprender:

```text
printf ... | while read ...; do
    contador=...
done
printf '%s\n' "$contador"
```

Los cambios de variables realizados dentro del bucle pueden no persistir en la shell exterior.

Para archivos locales sencillos, preferimos redirección:

```bash
while IFS= read -r linea; do
    ...
done < datos.txt
```

## 27. Última línea sin salto final

`read` devuelve un estado no-cero al encontrar EOF. Si necesitas procesar también una última línea que no termina en salto de línea, existe este patrón:

```bash
while IFS= read -r linea || [[ -n $linea ]]; do
    printf '<%s>\n' "$linea"
done < datos.txt
```

No necesitas memorizarlo todavía. Lo incluimos porque evita una pérdida silenciosa en archivos imperfectamente terminados.

## 28. Crear un archivo de práctica

Dentro del laboratorio:

```bash
printf '%s\n' \
    'primera línea' \
    'segunda línea con espacios' \
    'tercera \\ línea' \
    > datos.txt
```

`>` sobrescribe `datos.txt` si ya existe. Por eso se usa únicamente en la carpeta específica de práctica.

## 29. Procesar líneas con contador

```bash
contador=0

while IFS= read -r linea; do
    (( contador += 1 ))
    printf '%s: <%s>\n' "$contador" "$linea"
done < datos.txt
```

El contador queda disponible después del bucle porque usamos redirección y no una tubería para alimentar el `while`.

## 30. Filtrar dentro de un bucle

```bash
while IFS= read -r linea; do
    if [[ -z $linea ]]; then
        continue
    fi
    printf '<%s>\n' "$linea"
done < datos.txt
```

Las líneas vacías se omiten.

## 31. Recorrer archivos con espacios

Crea archivos de laboratorio:

```bash
printf 'A\n' > 'uno.txt'
printf 'B\n' > 'dos palabras.txt'
```

Después:

```bash
for archivo in ./*.txt; do
    [[ -e $archivo ]] || continue
    printf 'Procesando: <%s>\n' "$archivo"
done
```

`dos palabras.txt` sigue siendo un solo elemento.

## 32. Evitar expansiones sin comillas en el cuerpo

Incorrecto:

```text
printf '%s\n' $archivo
```

Aunque el glob haya producido cada pathname correctamente, una expansión posterior sin comillas puede volver a introducir división en palabras y globbing.

Correcto:

```bash
printf '%s\n' "$archivo"
```

## 33. Nombres que empiezan con guion

Un nombre puede comenzar con `-`.

Por eso, cuando una herramienta acepta `--`, usa:

```bash
comando -- "$archivo"
```

En nuestras prácticas `./*.txt` produce rutas que comienzan por `./`, lo que también reduce este riesgo.

## 34. Nombres con saltos de línea

Linux permite nombres de archivo que contienen saltos de línea.

Esto explica por qué procesar nombres como texto separado por líneas no es una estrategia universalmente segura.

El globbing de Bash conserva cada pathname como una palabra independiente, aunque su representación visual pueda ser confusa al imprimirla.

## 35. Recorrido recursivo: no usar `ls -R` para parsear

Para recorrer subdirectorios no conviertas la presentación de `ls -R` en datos.

Las herramientas diseñadas para recorrer el árbol, como `find`, son más apropiadas.

El uso completo de `find` ya fue introducido en el Módulo 10; aquí conectamos ese conocimiento con bucles.

## 36. Técnica avanzada GNU: `find -print0`

Cuando sea necesario procesar recursivamente nombres arbitrarios en un entorno GNU, una técnica robusta es separar pathnames con NUL:

```bash
while IFS= read -r -d '' archivo; do
    printf '<%s>\n' "$archivo"
done < <(find . -type f -print0)
```

Esta construcción combina características de Bash (`<(...)`, `read -d`) con `find -print0`. No es una receta POSIX genérica.

No necesitas memorizarla todavía. Se incluye para mostrar cómo se evita usar saltos de línea como separador de nombres.

## 37. Sustitución de proceso `<(...)`

En el ejemplo anterior:

```text
<(comando)
```

es **sustitución de proceso** de Bash.

Permite presentar la salida de un comando mediante un nombre de archivo especial al comando consumidor.

Se menciona aquí solo por su utilidad para un recorrido robusto; no forma parte del núcleo que debes dominar todavía.

## 38. `for (( ... ))` aritmético

Bash también permite un bucle aritmético estilo C:

```bash
for (( i = 1; i <= 3; i += 1 )); do
    printf '%s\n' "$i"
done
```

Es específico de Bash y no es la forma POSIX de `for`.

Para principiantes usaremos esta forma solo cuando el problema sea claramente numérico.

## 39. Elegir el bucle correcto

Guía inicial:

```text
lista de elementos           → for
argumentos del script        → for ... in "$@"
archivos por patrón          → for archivo in ./*.ext
repetir según condición      → while
repetir hasta condición      → until
leer archivo línea por línea → while IFS= read -r
contador numérico Bash       → while (( ... )) o for (( ... ))
```

## 40. Preparar el laboratorio

```bash
cd ~/linux-lab
pwd
ls
mkdir -p modulo-27-bucles
cd modulo-27-bucles
pwd
```

Etiqueta: **creación en laboratorio**.

## 41. Práctica A — `for` básico

Crea `for_basico.sh`:

```bash
#!/usr/bin/env bash

for palabra in Linux Bash Git; do
    printf '%s\n' "$palabra"
done
```

Valida:

```bash
bash -n for_basico.sh
```

Después ejecútalo y explica cuántas iteraciones realiza.

## 42. Práctica B — argumentos seguros

Crea `argumentos.sh`:

```bash
#!/usr/bin/env bash

for argumento in "$@"; do
    printf '<%s>\n' "$argumento"
done
```

Prueba:

```bash
bash argumentos.sh uno 'dos palabras' tres
```

Debes obtener tres elementos.

## 43. Práctica C — `while` con contador

```bash
#!/usr/bin/env bash

contador=1

while (( contador <= 5 )); do
    printf 'Iteración %s\n' "$contador"
    (( contador += 1 ))
done
```

Antes de ejecutar, identifica qué línea evita que el bucle sea infinito.

## 44. Práctica D — `until`

```bash
#!/usr/bin/env bash

contador=1

until (( contador > 3 )); do
    printf '%s\n' "$contador"
    (( contador += 1 ))
done
```

Explica por qué se detiene cuando el contador llega a `4`.

## 45. Práctica E — leer líneas

Crea `datos.txt` dentro del laboratorio y después un script:

```bash
#!/usr/bin/env bash

while IFS= read -r linea; do
    printf '<%s>\n' "$linea"
done < datos.txt
```

Agrega una línea con espacios y otra con una barra invertida para comprobar qué conserva.

## 46. Práctica F — archivos con espacios

Crea únicamente dentro de la carpeta del módulo:

```bash
printf 'uno\n' > 'archivo uno.txt'
printf 'dos\n' > 'archivo dos.txt'
```

Después:

```bash
for archivo in ./*.txt; do
    [[ -e $archivo ]] || continue
    printf '<%s>\n' "$archivo"
done
```

Explica por qué cada nombre continúa siendo una sola unidad.

## 47. Práctica G — `break` y `continue`

```bash
#!/usr/bin/env bash

for n in 1 2 3 4 5; do
    if (( n == 2 )); then
        continue
    fi

    if (( n == 5 )); then
        break
    fi

    printf '%s\n' "$n"
done
```

Predice la salida antes de ejecutar.

## 48. Errores frecuentes

| Error | Problema | Corrección |
|---|---|---|
| `for f in $(ls)` | convierte nombres en texto sujeto a división | usa globbing o una interfaz delimitada correctamente |
| `for f in $@` | pierde límites de argumentos | usa `for f in "$@"` |
| `printf ... $archivo` | vuelve a exponer el nombre a word splitting/globbing | usa `"$archivo"` |
| `while read linea` para texto arbitrario | puede interpretar `\` y tratar IFS | usa `while IFS= read -r linea` |
| contador nunca cambia | el bucle puede no terminar | actualiza la condición |
| `break` donde querías omitir una sola vuelta | termina todo el bucle | usa `continue` |
| `continue` donde querías terminar | solo salta a la siguiente iteración | usa `break` |
| alimentar un `while` con tubería y esperar variables fuera | puede ejecutarse en subshell | usa redirección cuando aplique |
| asumir que `*.txt` sin coincidencias desaparece | por defecto puede quedar literal | filtra el patrón literal o estudia `nullglob` |
| suponer que `-e` incluye enlaces simbólicos rotos | `-e` es falso si el destino no existe | si necesitas incluirlos, combina `-e` con `-L` |
| usar un bucle para cambios destructivos masivos | amplifica errores | prueba solo con acciones seguras y revisables |

## 49. Detección de error 1

Analiza:

```bash
for archivo in $(ls *.txt); do
    printf '%s\n' "$archivo"
done
```

Problema: `$(...)` convierte la salida en texto y después Bash puede dividirlo en palabras.

Corrección mínima para el directorio actual:

```bash
for archivo in ./*.txt; do
    [[ -e $archivo ]] || continue
    printf '%s\n' "$archivo"
done
```

## 50. Detección de error 2

Analiza:

```bash
contador=1

while (( contador <= 3 )); do
    printf '%s\n' "$contador"
done
```

Problema: `contador` nunca cambia.

Corrección:

```bash
contador=1

while (( contador <= 3 )); do
    printf '%s\n' "$contador"
    (( contador += 1 ))
done
```

## 51. Detección de error 3

Analiza:

```bash
cat datos.txt | while read linea; do
    printf '%s\n' "$linea"
done
```

Problemas pedagógicos:

- `cat` es innecesario para leer ese archivo;
- falta `-r`;
- no se controla `IFS`;
- la tubería añade semántica de subshell.

Corrección:

```bash
while IFS= read -r linea; do
    printf '%s\n' "$linea"
done < datos.txt
```

## 52. Práctica independiente

Crea `inventario_txt.sh`.

Debe:

1. usar Bash;
2. trabajar únicamente en el directorio actual del laboratorio;
3. recorrer `./*.txt` sin usar `ls` ni sustitución de comandos;
4. ignorar correctamente el patrón si no hay coincidencias;
5. llevar un contador;
6. imprimir cada pathname entre `< >`;
7. conservar nombres con espacios;
8. terminar mostrando cuántos archivos encontró;
9. no borrar, renombrar ni modificar los archivos;
10. pasar `bash -n`;
11. poder explicarse línea por línea.

## 53. Mini evaluación

1. ¿qué bucle es natural para recorrer una lista? A) `for` B) `if`
2. ¿qué conserva los argumentos separados? A) `$@` sin comillas B) `"$@"`
3. ¿es recomendable `for f in $(ls)` para nombres arbitrarios? A) Sí B) No
4. ¿qué hace `break`? A) termina el bucle B) salta solo la iteración
5. ¿qué hace `continue`? A) termina el script B) pasa a la siguiente iteración
6. ¿`while` repite mientras su condición tenga estado `0`? A) Sí B) No
7. ¿`until` se detiene cuando su condición tiene éxito? A) Sí B) No
8. ¿qué opción de `read` evita tratar `\` como escape? A) `-r` B) `-x`
9. ¿por qué usamos `IFS=` con `read`? A) para evitar el tratamiento habitual de separadores B) para borrar el archivo
10. ¿es necesaria una tubería con `cat` para leer un archivo línea por línea? A) Sí B) No
11. ¿un glob de Bash conserva un pathname con espacios como un elemento? A) Sí B) No
12. ¿un bucle sin cambio de condición puede volverse infinito? A) Sí B) No
13. ¿`./*.txt` puede permanecer literal si no hay coincidencias con la configuración predeterminada? A) Sí B) No
14. ¿las variables cambiadas en un bucle alimentado por una tubería siempre persisten fuera? A) Sí B) No
15. ¿debes usar bucles destructivos para aprender esta parte? A) Sí B) No
16. ¿`-e` es verdadero para un enlace simbólico roto? A) Sí B) No
17. ¿`-L` puede reconocer un enlace simbólico roto? A) Sí B) No

## 54. Registro de aprendizaje

```text
Un bucle sirve para:
`for` sirve para:
`while` repite mientras:
`until` repite hasta:
`break` hace:
`continue` hace:
`"$@"` dentro de for conserva:
¿por qué no debo usar `for f in $(ls)`?:
`read -r` sirve para:
`IFS=` antes de read ayuda a:
¿por qué prefiero `done < archivo` a una tubería innecesaria?:
¿qué puede provocar un bucle infinito?:
Forma segura inicial de recorrer .txt:
¿Por qué `-e` puede omitir un enlace simbólico roto?:
¿Cuándo usaría `-L`?:
Algo que todavía confundo:
Estado: EN APRENDIZAJE / PRACTICADO
```

## 55. Puerta de dominio

Para considerar este módulo **DOMINADO** deberás poder, en más de una práctica:

1. escribir un `for` sin copiar;
2. recorrer `"$@"` conservando un argumento con espacios;
3. explicar por qué no se parsea `ls`;
4. crear un `while` que termine correctamente;
5. leer líneas con `IFS= read -r`;
6. detectar un bucle que no actualiza su condición;
7. distinguir `break` de `continue`;
8. resolver una nueva práctica con nombres de archivo con espacios.

## 56. Fuentes y límites

Fuentes principales:

- GNU Bash Reference Manual — Looping Constructs: https://www.gnu.org/software/bash/manual/html_node/Looping-Constructs.html
- GNU Bash Reference Manual — Bourne Shell Builtins (`read`, `break`, `continue`): https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html
- GNU Bash Reference Manual — Filename Expansion: https://www.gnu.org/software/bash/manual/html_node/Filename-Expansion.html
- GNU Bash Reference Manual — Pipelines: https://www.gnu.org/software/bash/manual/html_node/Pipelines.html
- GNU Bash Reference Manual — Process Substitution: https://www.gnu.org/software/bash/manual/html_node/Process-Substitution.html

Puntos verificados documentalmente:

- `for`, `while` y `until` son construcciones de bucle de Bash;
- `break` termina un bucle y `continue` avanza a la siguiente iteración;
- `read -r` evita que la barra invertida actúe como carácter de escape;
- la expansión de nombres de archivo reemplaza patrones por pathnames coincidentes;
- si `nullglob` está desactivado y no hay coincidencias, el patrón queda sin modificar;
- los componentes de una tubería normalmente se ejecutan en subshells en Bash, con excepciones configurables;
- la sustitución de proceso `<(...)` es una característica de Bash y no una construcción POSIX básica.

Se posponen:

- arrays y `mapfile` como técnica principal;
- `select`;
- bucles anidados complejos;
- control de múltiples niveles con `break n` / `continue n`;
- opciones `nullglob`, `failglob`, `dotglob` como política de scripts;
- `find -exec` en profundidad;
- funciones y ámbito;
- `getopts`;
- manejo avanzado de errores y `trap`.

**Estado de la lección:** redactada y revisada documentalmente contra GNU Bash. Las prácticas son locales, no destructivas y no requieren privilegios.

Siguiente módulo por redactar: **Módulo 28 — Funciones, parámetros y ámbito en Bash**.
