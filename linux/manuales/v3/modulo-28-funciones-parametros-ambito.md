# Módulo 28 — Funciones, parámetros y ámbito en Bash

Manual Maestro de Linux y Shell Scripting — Edición 2026 · v3 · Vigesimoctava entrega.

[Índice del manual](README.md) · [← Módulo 27](modulo-27-bucles-lectura-lineas-nombres-seguros.md) · [Arquitectura](00-indice-arquitectura.md) · [Módulo 29 →](modulo-29-manejo-errores-trap-mktemp-shellcheck.md)

## 1. Qué aprenderás

Al terminar este módulo podrás:

- explicar qué es una función de shell y para qué sirve;
- definir y llamar funciones Bash;
- distinguir definir una función de ejecutarla;
- pasar argumentos a una función;
- usar `$1`, `$2`, `$#` y `"$@"` dentro de una función;
- reconocer que los parámetros posicionales de una función son temporales;
- usar `local` para reducir efectos laterales sobre variables externas;
- explicar el ámbito dinámico de Bash a nivel introductorio;
- diferenciar `return` de imprimir o producir un resultado;
- usar el estado de retorno de una función con `if`, `&&` y `||`;
- producir texto por salida estándar y capturarlo cuando sea apropiado;
- evitar depender innecesariamente de variables globales;
- validar argumentos básicos antes de trabajar con ellos;
- separar una tarea grande en funciones pequeñas y comprensibles.

Conocimientos previos:

- variables y quoting;
- argumentos posicionales;
- códigos de salida;
- condicionales;
- bucles;
- sustitución de comandos;
- redirecciones.

**Seguridad:** las prácticas son locales, sin `sudo` y dentro de `~/linux-lab`. Las funciones pueden concentrar automatización; por eso no se usarán para borrados masivos, cambios de permisos, administración de servicios, usuarios, discos, red o cortafuegos.

## 2. Qué es una función

Una función agrupa una serie de órdenes bajo un nombre.

Modelo:

```text
nombre de función
       ↓
varias órdenes relacionadas
       ↓
una tarea reutilizable
```

Sirve para evitar repetir código y para dividir un script en partes pequeñas.

## 3. Primera función

```bash
saludar() {
    printf 'Hola desde una función\n'
}
```

Esto **define** la función. Todavía no la ejecuta.

Para llamarla:

```bash
saludar
```

## 4. Explicación línea por línea

```bash
saludar() {
```

`saludar` es el nombre. `()` forma parte de esta sintaxis de definición. `{` inicia el cuerpo.

```bash
    printf 'Hola desde una función\n'
```

es una orden perteneciente al cuerpo.

```bash
}
```

cierra la función.

Después:

```bash
saludar
```

ejecuta la función como una orden de shell.

## 5. El espacio y los separadores alrededor de `{` y `}`

Esta forma es correcta:

```bash
saludar() {
    printf 'Hola\n'
}
```

En una forma de una sola línea necesitas separar correctamente las órdenes:

```bash
saludar() { printf 'Hola\n'; }
```

El `;` antes de `}` termina la orden `printf`.

## 6. Sintaxis que prioriza este manual

Bash admite más de una forma de declarar funciones.

Este manual prioriza:

```bash
nombre() {
    órdenes
}
```

porque es clara y ampliamente reconocible.

No necesitamos usar la palabra reservada `function` para aprender el concepto.

## 7. Define antes de llamar

En un script secuencial, la definición debe haberse ejecutado antes de llamar la función.

Correcto:

```bash
saludar() {
    printf 'Hola\n'
}

saludar
```

No coloques una llamada inicial a una función cuya definición todavía no ha sido procesada por el script.

## 8. Las funciones reciben argumentos

Ejemplo:

```bash
saludar() {
    printf 'Hola, %s\n' "$1"
}

saludar 'Ana María'
```

Dentro de la función:

```text
$1 → Ana María
```

## 9. Parámetros posicionales temporales

Cuando una función se ejecuta, sus argumentos sustituyen temporalmente los parámetros posicionales `$1`, `$2`, etc. durante esa llamada.

Al terminar la función, los parámetros posicionales del contexto llamador vuelven a estar disponibles.

Esto permite que una función tenga sus propios argumentos sin destruir permanentemente los argumentos originales del script.

## 10. `$#` dentro de una función

Dentro de una función:

```text
$#
```

indica cuántos argumentos recibió **esa función**.

```bash
contar_argumentos() {
    printf 'La función recibió %s argumentos\n' "$#"
}

contar_argumentos uno 'dos palabras' tres
```

El resultado esperado es `3`.

## 11. `"$@"` dentro de una función

```bash
mostrar_argumentos() {
    for argumento in "$@"; do
        printf '<%s>\n' "$argumento"
    done
}
```

`"$@"` conserva cada argumento de la función como una unidad independiente.

## 12. Parámetros mayores que 9

Para el décimo parámetro y posteriores usa llaves:

```text
${10}
${11}
```

`$10` no debe interpretarse como una forma segura de referirse al décimo parámetro.

Para la mayoría de nuestras funciones iniciales no necesitaremos tantos argumentos.

## 13. Validar que llegó un argumento

Ejemplo:

```bash
saludar() {
    if (( $# < 1 )); then
        printf 'Error: falta el nombre\n' >&2
        return 1
    fi

    printf 'Hola, %s\n' "$1"
}
```

La función comprueba primero su cantidad de argumentos.

## 14. Qué significa `return`

`return` termina una función y establece su estado de salida.

```bash
return 0
```

indica éxito.

```bash
return 1
```

indica fallo.

`return` no es la forma general de devolver una cadena, una ruta o un número arbitrario como dato.

## 15. `return` y `exit` no son lo mismo

Dentro de una función:

```bash
return 1
```

termina la función y devuelve control al llamador.

En cambio:

```bash
exit 1
```

termina la shell/script actual.

Regla inicial:

```text
quiero salir de la función → return
quiero terminar el script   → exit
```

## 16. Estado implícito de una función

Si no ejecutas `return n` explícitamente, el estado de la función es normalmente el estado de la última orden ejecutada en su cuerpo.

Ejemplo:

```bash
funcion_ok() {
    printf 'Todo bien\n'
}
```

Si `printf` termina con éxito, la función también tendrá estado `0`.

Cuando el significado importa, un `return` explícito puede hacer la intención más clara.

## 17. Usar una función con `if`

```bash
es_directorio() {
    [[ -d $1 ]]
}

if es_directorio ~/linux-lab; then
    printf 'El laboratorio existe como directorio\n'
fi
```

La última expresión `[[ -d $1 ]]` determina el estado de la función.

## 18. Usar una función con `&&` y `||`

```bash
comprobar_archivo() {
    [[ -f $1 ]]
}

comprobar_archivo ./nota.txt && printf 'Existe\n'
```

o:

```bash
comprobar_archivo ./nota.txt || printf 'No existe como archivo regular\n'
```

Las funciones participan en la lógica de estados igual que otras órdenes.

## 19. Resultado como texto: salida estándar

Si una función necesita producir texto, puede escribirlo por salida estándar:

```bash
obtener_saludo() {
    printf 'Hola, %s\n' "$1"
}
```

Puedes llamarla directamente:

```bash
obtener_saludo 'Ana'
```

## 20. Capturar la salida de una función

```bash
obtener_saludo() {
    printf 'Hola, %s\n' "$1"
}

mensaje=$(obtener_saludo 'Ana')
printf '%s\n' "$mensaje"
```

`$(...)` captura la salida estándar.

Recuerda que la sustitución de comandos elimina los saltos de línea finales de la salida capturada.

## 21. No mezcles datos con mensajes de diagnóstico

Si una función produce un dato por salida estándar y además imprime mensajes informativos por el mismo canal, la captura puede mezclar ambos.

Ejemplo problemático:

```text
funcion → imprime 'Procesando...' y también imprime el resultado
```

Si el texto es diagnóstico, puede enviarse a `stderr`:

```bash
printf 'Aviso: falta un argumento\n' >&2
```

Así la salida estándar puede reservarse para el dato cuando ese diseño sea apropiado.

## 22. Variables globales por defecto

En Bash, una variable creada fuera de una función puede ser visible dentro de ella.

Además, si asignas una variable dentro de una función sin declararla local, puedes modificar una variable del ámbito exterior.

Ejemplo:

```bash
nombre='global'

cambiar() {
    nombre='modificado'
}

cambiar
printf '%s\n' "$nombre"
```

El valor exterior puede quedar modificado.

## 23. `local`

Dentro de una función puedes declarar una variable local:

```bash
saludar() {
    local nombre='Ana'
    printf '%s\n' "$nombre"
}
```

Esa variable local existe en el ámbito de la función y de las funciones que esta llame, según las reglas de ámbito dinámico de Bash.

## 24. Evitar modificar accidentalmente una global

```bash
nombre='global'

mostrar() {
    local nombre='local'
    printf 'Dentro: %s\n' "$nombre"
}

mostrar
printf 'Fuera: %s\n' "$nombre"
```

Resultado conceptual:

```text
Dentro: local
Fuera: global
```

`local` oculta temporalmente la variable exterior del mismo nombre.

## 25. Ámbito dinámico de Bash

Bash usa **ámbito dinámico** para variables locales de funciones.

Ejemplo:

```bash
segunda() {
    printf 'segunda ve: %s\n' "$dato"
}

primera() {
    local dato='local de primera'
    segunda
}

primera
```

`segunda` puede ver el `dato` local de `primera` porque fue llamada desde ese contexto.

Esto es diferente del ámbito léxico que probablemente encontrarás en otros lenguajes.

Para empezar, la regla práctica es: **mantén funciones pequeñas y pasa datos como argumentos en vez de depender demasiado de variables visibles implícitamente**.

## 26. `local` solo tiene sentido dentro de una función

Usaremos `local` únicamente dentro del cuerpo de funciones.

Ejemplo:

```bash
procesar() {
    local archivo=$1
    printf '%s\n' "$archivo"
}
```

## 27. Citar al asignar desde argumentos

En una asignación simple de Bash:

```bash
local archivo=$1
```

el contexto de asignación no realiza el mismo word splitting y globbing que una expansión ordinaria de comando.

Aun así, cuando una expansión pase posteriormente a una orden, mantenemos el patrón seguro:

```bash
printf '%s\n' "$archivo"
```

## 28. Una función, una responsabilidad clara

Evita funciones que hagan demasiadas cosas.

Mejor:

```text
validar_ruta
mostrar_archivo
contar_lineas
```

que una única función gigantesca que valide, modifique, copie, borre y genere informes.

Las funciones pequeñas son más fáciles de probar y explicar.

## 29. Nombres de funciones

Usa nombres descriptivos:

```text
mostrar_ayuda
validar_archivo
contar_argumentos
```

Evita nombres ambiguos como:

```text
hacer
cosa
x
```

## 30. No sobrescribas nombres de órdenes sin necesidad

Bash permite que una función tenga el mismo nombre que una orden.

Eso puede cambiar qué se ejecuta cuando escribes ese nombre.

Para aprendizaje inicial, no definas funciones llamadas:

```text
cd
ls
printf
test
```

Usa nombres propios y claros.

## 31. Función de validación básica

```bash
validar_archivo() {
    if (( $# != 1 )); then
        printf 'Uso: validar_archivo RUTA\n' >&2
        return 2
    fi

    if [[ ! -f $1 ]]; then
        printf 'No es un archivo regular: %s\n' "$1" >&2
        return 1
    fi

    return 0
}
```

Esta función separa dos casos:

- uso incorrecto;
- ruta que no es archivo regular.

Los significados `1` y `2` son convenciones internas de este ejemplo; no son universales.

## 32. Llamar a otra función

```bash
mostrar_archivo() {
    local ruta=$1
    printf 'Archivo: %s\n' "$ruta"
}

procesar_archivo() {
    local ruta=$1
    mostrar_archivo "$ruta"
}
```

Una función puede llamar a otra igual que llama una orden.

## 33. Pasar argumentos al llamar otra función

Correcto:

```bash
mostrar_archivo "$ruta"
```

Si necesitas reenviar todos los argumentos:

```bash
otra_funcion "$@"
```

Esto preserva sus límites.

## 34. Funciones y bucles

Puedes combinar lo aprendido:

```bash
mostrar_txt() {
    local archivo

    for archivo in ./*.txt; do
        [[ -e $archivo ]] || continue
        printf '<%s>\n' "$archivo"
    done
}
```

La variable de trabajo se declara local para no alterar accidentalmente otra variable `archivo` del script.

## 35. Funciones y sustitución de comandos: efecto de subshell

Cuando llamas una función dentro de:

```bash
resultado=$(mi_funcion)
```

la sustitución de comandos se ejecuta en un entorno de subshell.

Por eso no debes depender de que cambios de variables realizados dentro de esa llamada modifiquen después el shell exterior.

Usa la sustitución de comandos para capturar salida, no como mecanismo para cambiar estado global externo.

## 36. Función que calcula y produce un dato

```bash
sumar() {
    local a=$1
    local b=$2
    printf '%s\n' "$(( a + b ))"
}

resultado=$(sumar 4 7)
printf 'Resultado: %s\n' "$resultado"
```

Resultado:

```text
Resultado: 11
```

Aquí `return` no se usa para transportar el número `11`; el dato viaja por salida estándar.

## 37. Validar cantidad antes de usar `$1` o `$2`

```bash
sumar() {
    if (( $# != 2 )); then
        printf 'Error: se requieren dos enteros\n' >&2
        return 2
    fi

    local a=$1
    local b=$2
    printf '%s\n' "$(( a + b ))"
}
```

La validación completa de que ambos argumentos sean enteros se ampliará después; aquí validamos primero la cantidad.

## 38. `return` sin número

Si escribes:

```bash
return
```

sin un argumento explícito, el estado retornado depende del estado de la última orden ejecutada antes de `return`.

Para ramas de validación importantes, preferimos estados explícitos como:

```bash
return 1
```

## 39. No uses `return` fuera de su contexto

`return` está diseñado para volver desde una función o desde un archivo ejecutado mediante `source`/`.`.

Para terminar un script ejecutado normalmente se usa `exit`.

## 40. Preparar el laboratorio

```bash
test -d ~/linux-lab && \
cd ~/linux-lab && \
mkdir -p modulo-28-funciones && \
cd modulo-28-funciones && pwd
```

Etiqueta: **creación en laboratorio**.

## 41. Práctica A — primera función

Crea `funcion_basica.sh`:

```bash
#!/usr/bin/env bash

saludar() {
    printf 'Hola desde Bash\n'
}

saludar
```

Valida:

```bash
bash -n funcion_basica.sh
```

Después ejecútalo.

## 42. Práctica B — argumento de función

Crea `funcion_argumento.sh`:

```bash
#!/usr/bin/env bash

saludar() {
    if (( $# != 1 )); then
        printf 'Uso: saludar NOMBRE\n' >&2
        return 2
    fi

    local nombre=$1
    printf 'Hola, %s\n' "$nombre"
}

saludar 'Ana María'
```

Explica por qué `Ana María` sigue siendo un solo argumento.

## 43. Práctica C — variable local

Crea `funcion_local.sh`:

```bash
#!/usr/bin/env bash

valor='global'

demostrar_local() {
    local valor='local'
    printf 'Dentro: %s\n' "$valor"
}

demostrar_local
printf 'Fuera: %s\n' "$valor"
```

Predice las dos líneas antes de ejecutar.

## 44. Práctica D — estado de retorno

Crea `funcion_estado.sh`:

```bash
#!/usr/bin/env bash

es_txt() {
    [[ $1 == *.txt ]]
}

if es_txt 'informe.txt'; then
    printf 'Sí termina en .txt\n'
else
    printf 'No termina en .txt\n'
fi
```

La función produce una decisión mediante su estado, no mediante el texto `true` o `false`.

## 45. Práctica E — capturar un dato

Crea `funcion_dato.sh`:

```bash
#!/usr/bin/env bash

sumar() {
    local a=$1
    local b=$2
    printf '%s\n' "$(( a + b ))"
}

resultado=$(sumar 8 5)
printf 'Suma: %s\n' "$resultado"
```

Explica por qué usamos `printf` para el dato y no `return 13` como mecanismo general de resultado.

## 46. Práctica F — recorrer argumentos dentro de función

Crea `funcion_argumentos.sh`:

```bash
#!/usr/bin/env bash

mostrar_argumentos() {
    local argumento

    for argumento in "$@"; do
        printf '<%s>\n' "$argumento"
    done
}

mostrar_argumentos uno 'dos palabras' tres
```

Debe mostrar tres argumentos.

## 47. Errores frecuentes

| Error | Problema | Corrección |
|---|---|---|
| definir una función y esperar que se ejecute sola | definición y llamada son operaciones distintas | llama la función después |
| llamar antes de que la definición haya sido procesada | la función aún no existe en ese punto | define antes de llamar |
| usar `$@` sin comillas para reenviar | puede romper límites | usa `"$@"` |
| usar `exit` queriendo salir solo de una función | termina el script/shell | usa `return` |
| usar `return` para devolver texto | `return` comunica un estado | usa stdout u otro diseño |
| asignar variables sin `local` dentro de funciones | puedes modificar estado exterior | usa `local` cuando la variable sea interna |
| depender demasiado de globales | crea acoplamiento difícil de probar | pasa argumentos explícitos |
| mezclar diagnóstico y dato en stdout | rompe capturas con `$(...)` | usa stderr para diagnósticos |
| olvidar validar `$#` | puedes usar argumentos ausentes | valida cantidad primero |
| asumir ámbito léxico | Bash usa ámbito dinámico | diseña funciones pequeñas y explícitas |
| esperar que una función en `$(...)` cambie variables externas | la sustitución usa subshell | captura salida y evita ese efecto lateral |

## 48. Detección de error 1

Analiza:

```bash
nombre='global'

cambiar() {
    nombre='local temporal'
}

cambiar
printf '%s\n' "$nombre"
```

Problema: la función modifica la variable exterior.

Corrección mínima:

```bash
cambiar() {
    local nombre='local temporal'
}
```

## 49. Detección de error 2

Analiza:

```bash
obtener_nombre() {
    return 'Ana'
}
```

Problema: `return` no transporta cadenas.

Corrección:

```bash
obtener_nombre() {
    printf '%s\n' 'Ana'
}
```

Si necesitas capturarlo:

```bash
nombre=$(obtener_nombre)
```

## 50. Detección de error 3

Analiza:

```bash
reenviar() {
    otra_funcion $@
}
```

Problema: se pueden perder los límites de los argumentos.

Corrección:

```bash
reenviar() {
    otra_funcion "$@"
}
```

## 51. Método para diseñar una función

Antes de escribirla:

1. define una sola responsabilidad;
2. elige un nombre descriptivo;
3. decide qué datos recibe como argumentos;
4. valida la cantidad mínima necesaria;
5. usa variables locales para trabajo interno;
6. preserva argumentos con quoting;
7. decide si el resultado será un estado o un dato;
8. usa `return` para estados;
9. usa stdout con disciplina si produces un dato capturable;
10. prueba la función de forma aislada antes de integrarla en un script mayor.

## 52. Práctica independiente

Crea `analizar_ruta.sh`.

Debe incluir al menos tres funciones:

```text
validar_argumentos
clasificar_ruta
mostrar_resultado
```

Requisitos:

1. usar Bash;
2. recibir exactamente una ruta como argumento del script;
3. pasar esa ruta explícitamente a las funciones;
4. usar `local` para variables internas;
5. distinguir al menos archivo regular, directorio y otro/no existente;
6. usar estados de retorno para indicar éxito/fallo cuando corresponda;
7. no modificar la ruta;
8. no usar `sudo`;
9. pasar `bash -n`;
10. poder explicar qué datos entran y salen de cada función.

## 53. Mini evaluación

1. ¿definir una función también la ejecuta? A) Sí B) No
2. ¿cómo llamas una función llamada `saludar`? A) `saludar` B) `call saludar`
3. dentro de una función, ¿`$1` representa su primer argumento? A) Sí B) No
4. ¿`$#` dentro de una función cuenta sus argumentos? A) Sí B) No
5. ¿`"$@"` preserva límites de argumentos? A) Sí B) No
6. ¿`return 0` indica éxito? A) Sí B) No
7. ¿`return` y `exit` tienen el mismo alcance? A) Sí B) No
8. ¿`return` es el mecanismo general para devolver una cadena? A) Sí B) No
9. ¿`local` ayuda a evitar modificar una variable exterior del mismo nombre? A) Sí B) No
10. ¿Bash usa ámbito dinámico para variables locales de funciones? A) Sí B) No
11. ¿una función puede usarse directamente como condición de `if`? A) Sí B) No
12. ¿la salida estándar de una función puede capturarse con `$(...)`? A) Sí B) No
13. ¿los diagnósticos deberían mezclarse sin cuidado con datos capturados por stdout? A) Sí B) No
14. ¿`${10}` es la forma apropiada de referirse al décimo parámetro? A) Sí B) No
15. ¿una función llamada dentro de sustitución de comandos debe usarse para modificar variables del shell exterior? A) Sí B) No

## 54. Registro de aprendizaje

```text
Una función es:
Definir una función significa:
Llamar una función significa:
Dentro de una función `$1` es:
Dentro de una función `$#` es:
`"$@"` sirve para:
`local` sirve para:
Ámbito dinámico significa, de forma básica:
`return 0` significa:
Diferencia entre `return` y `exit`:
¿cómo produzco un dato de texto desde una función?:
¿por qué separo stdout de stderr?:
¿por qué prefiero argumentos explícitos a muchas globales?:
Algo que todavía confundo:
Estado: EN APRENDIZAJE / PRACTICADO
```

## 55. Puerta de dominio

Para considerar este módulo **DOMINADO** deberás poder en más de una sesión:

1. definir y llamar una función sin copiar;
2. pasar un argumento con espacios sin romperlo;
3. explicar por qué `"$@"` es importante;
4. usar `local` y demostrar que la global no cambia;
5. distinguir un resultado de datos de un estado de retorno;
6. usar una función como condición de `if`;
7. detectar un uso incorrecto de `exit` dentro de una función;
8. dividir un script pequeño en dos o más funciones con responsabilidades claras.

## 56. Fuentes y límites

Clasificación y estado de los enlaces de esta sección: [catálogo de fuentes](06-catalogo-fuentes.md) (jerarquía E04, comprobación del 9 de octubre de 2026).

Fuentes principales:

- GNU Bash Reference Manual — Shell Functions: https://www.gnu.org/software/bash/manual/html_node/Shell-Functions.html
- GNU Bash Reference Manual — Positional Parameters: https://www.gnu.org/software/bash/manual/html_node/Positional-Parameters.html
- GNU Bash Reference Manual — Bourne Shell Builtins (`return`): https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html
- GNU Bash Reference Manual — Bash Builtins (`local`, `declare`): https://www.gnu.org/software/bash/manual/html_node/Bash-Builtins.html
- GNU Bash Reference Manual — Command Substitution: https://www.gnu.org/software/bash/manual/html_node/Command-Substitution.html

Puntos verificados documentalmente:

- una función agrupa un comando compuesto bajo un nombre;
- cuando se ejecuta una función, sus argumentos pasan a ser temporalmente sus parámetros posicionales;
- al finalizar la función se restauran los parámetros posicionales anteriores;
- las variables son compartidas con el llamador salvo que se declaren locales;
- las variables locales de funciones siguen las reglas de ámbito dinámico de Bash;
- `return` finaliza una función y establece su estado;
- una función sin `return` explícito usa el estado de la última orden ejecutada como estado de la función;
- la sustitución de comandos ejecuta su contenido en un entorno de subshell y captura la salida estándar.

Se posponen:

- arrays como interfaz de funciones;
- namerefs (`local -n` / `declare -n`);
- `FUNCNAME`, `BASH_SOURCE` y pilas de llamadas;
- recursión;
- funciones exportadas;
- `source` como arquitectura de librerías;
- `getopts`;
- manejo avanzado de errores;
- `trap`, `mktemp`, `set -e`, `set -u` y `pipefail` como política.

**Estado de la lección:** redactada y revisada documentalmente contra GNU Bash. Las prácticas son locales, no destructivas y no requieren privilegios.

---

**Siguiente:** [Módulo 29 — Manejo de errores, `trap`, `mktemp`, límites de `set -e`/`set -u` y ShellCheck](modulo-29-manejo-errores-trap-mktemp-shellcheck.md) · [Volver al índice](README.md)
