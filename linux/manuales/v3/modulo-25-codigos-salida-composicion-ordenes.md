# Módulo 25 — Códigos de salida y composición de órdenes en Bash

Manual Maestro de Linux y Shell Scripting — Edición 2026 · v3 · Vigesimoquinta entrega.

[Índice del manual](README.md) · [← Módulo 24](modulo-24-variables-entrada-argumentos-quoting.md) · [Arquitectura](00-indice-arquitectura.md) · [Módulo 26 →](modulo-26-if-test-condicionales-case-aritmetica.md)

## 1. Qué aprenderás

Al terminar este módulo podrás:

- explicar qué es un código o estado de salida;
- interpretar `0` como éxito y un valor distinto de `0` como condición no exitosa para la lógica de Bash, sin asumir que siempre indica un error operativo;
- consultar inmediatamente el último estado con `$?`;
- guardar un estado antes de ejecutar otra orden;
- diferenciar `;`, `&&` y `||`;
- predecir qué órdenes se ejecutarán en listas AND y OR;
- usar `true` y `false` para practicar estados de forma segura;
- terminar un script de forma explícita con `exit`;
- reconocer los estados especiales `126` y `127` usados por Bash en determinadas situaciones;
- entender por qué `A && B || C` no debe memorizarse como sustituto general de `if/else`;
- reconocer cómo se determina por defecto el estado de una tubería.

Conocimientos previos: scripts Bash, `printf`, variables, `$?`, redirecciones, pipes y navegación básica.

**Seguridad:** todas las prácticas se realizan en `~/linux-lab`, sin `sudo` y sin operaciones destructivas. `&&` y `||` automatizan decisiones, por lo que no los combinaremos aquí con borrados, cambios de permisos, servicios, discos o cortafuegos.

## 2. Qué es un código de salida

Cuando una orden termina comunica a la shell un número llamado **estado de salida** o **código de salida**.

```text
0       → éxito
1–255   → estado no exitoso para las decisiones de Bash; significado específico según el programa
```

Para empezar no necesitas memorizar todos los números. La pregunta principal es: **¿la orden terminó con éxito o no?**

## 3. Por qué 0 significa éxito

Bash dispone de una forma general de representar éxito: `0`. Los valores distintos de cero hacen que Bash tome la rama «no exitosa», pero pueden representar errores, ausencia de coincidencias, resultados especiales u otras condiciones documentadas por cada herramienta.

No interpretes automáticamente `1`, `2`, `3`, etc. con un significado universal. Muchos programas documentan sus propios códigos.

## 4. Salida visible y estado de salida son cosas distintas

Ejemplo:

```bash
pwd
```

Si `pwd` funciona, normalmente termina con estado `0`. La ruta que ves en pantalla y el código de salida son conceptos diferentes.

Un comando puede mostrar texto y terminar bien, no mostrar nada y terminar bien, o mostrar un mensaje de error y terminar con un estado distinto de cero.

## 5. `$?` contiene el estado de la última orden

```bash
pwd
printf 'Estado: %s\n' "$?"
```

Si `pwd` tuvo éxito, el valor esperado es `0`.

## 6. `$?` cambia después de cada orden

Observa:

```bash
pwd
printf 'Hola\n'
printf 'Estado: %s\n' "$?"
```

El último `printf` ya no consulta el estado de `pwd`; consulta el estado del `printf` anterior.

Regla: **si necesitas conservar un estado, guárdalo inmediatamente**.

## 7. Guardar el estado

```bash
pwd
estado=$?
printf 'Estado de pwd: %s\n' "$estado"
```

`estado=$?` copia el resultado antes de que otro comando lo sustituya.

## 8. `true` y `false` para practicar

`true` termina correctamente y normalmente devuelve `0`.

`false` termina de forma no exitosa y normalmente devuelve `1`.

```bash
true
estado=$?
printf 'true devolvió: %s\n' "$estado"
```

```bash
false
estado=$?
printf 'false devolvió: %s\n' "$estado"
```

El `1` de `false` sirve para practicar; no significa que todos los errores de Linux devuelvan `1`.

## 9. El operador `;`

`;` separa órdenes secuenciales.

```bash
printf 'uno\n'; printf 'dos\n'
```

La segunda orden se ejecuta después de la primera independientemente de que la primera haya tenido éxito.

Ejemplo:

```bash
false; printf 'Esta línea sí se ejecuta\n'
```

## 10. El operador `&&`

Una lista AND tiene esta forma:

```text
orden1 && orden2
```

`orden2` se ejecuta **solo si `orden1` devuelve estado `0`**.

```bash
true && printf 'La primera orden tuvo éxito\n'
```

En cambio:

```bash
false && printf 'Esta línea no debe aparecer\n'
```

la segunda orden no se ejecuta.

## 11. Uso práctico de `&&`

```bash
mkdir -p ~/linux-lab/modulo-25-status && cd ~/linux-lab/modulo-25-status
```

Primero se intenta crear la carpeta. Solo si esa operación termina con éxito se ejecuta `cd`.

Esto evita continuar ciegamente con una acción que depende de una preparación anterior.

## 12. El operador `||`

Una lista OR tiene esta forma:

```text
orden1 || orden2
```

`orden2` se ejecuta **solo si `orden1` devuelve un estado distinto de `0`**.

```bash
false || printf 'La primera orden falló\n'
```

Con:

```bash
true || printf 'Esta línea no debe aparecer\n'
```

la segunda orden no se ejecuta.

## 13. `||` para reaccionar ante un fallo

Ejemplo local:

```bash
cd ~/linux-lab || printf 'No pude entrar al laboratorio\n'
```

Si `cd` falla, se muestra el aviso. Sin embargo, el script puede continuar después de esa lista.

`||` por sí solo no significa “termina el script”.

## 14. Combinar `||` con `exit`

Si el script no puede continuar cuando falla una preparación:

```bash
cd ~/linux-lab || exit 1
```

Interpretación:

1. intenta entrar a `~/linux-lab`;
2. si `cd` tiene éxito, `exit 1` no se ejecuta;
3. si `cd` falla, se ejecuta `exit 1`;
4. el script termina con estado `1`.

## 15. `exit`

`exit` termina la shell o el script actual.

```bash
exit 0
```

indica terminación exitosa.

```bash
exit 1
```

termina con un estado de fallo.

Si escribes `exit` sin número, Bash utiliza el estado de la última orden ejecutada.

## 16. No inventes significados universales

Un programa puede documentar códigos diferentes a otro. Para códigos específicos, consulta la documentación del programa que los genera.

**Dos niveles de interpretación:**

1. **Bash:** `0` permite continuar por `&&`; un estado no cero permite continuar por `||`.
2. **Programa:** el significado real del número depende de su contrato documentado.

Por ejemplo, `dnf check-update` documenta `0` si no hay actualizaciones, `100` si las hay y `1` cuando ocurre un error. Así, `100` activa la rama de `||` aunque no signifique un error operativo. Esta distinción se desarrolla también en los Módulos 15 y 35.

**Ejercicio de interpretación:** si `dnf check-update` devuelve `100`, responde por separado: ¿qué rama elegiría Bash en `orden && A || B`? ¿Qué significa `100` para DNF? No ejecutes DNF para contestar.

## 17. Estados especiales 126 y 127

En Bash:

- `127` se usa cuando no se encuentra una orden;
- `126` se usa cuando se encuentra la orden pero no puede ejecutarse de la forma solicitada.

No memorices `126` como explicación universal de todos los problemas de permisos.

## 18. Señales y `128 + N`

Si una orden termina por una señal fatal número `N`, Bash representa ese caso mediante `128 + N`.

En este módulo solo conectamos el concepto con lo ya estudiado sobre señales; no realizaremos prácticas para provocar terminaciones de procesos.

## 19. Estado final de listas AND y OR

El estado de una lista AND u OR es el estado de la última orden que realmente se ejecutó.

Ejemplo:

```bash
false || printf 'recuperado\n'
```

Si `printf` termina correctamente, la lista completa puede terminar con estado `0`, aunque la primera orden haya fallado.

## 20. Cortocircuito

`&&` y `||` aplican evaluación con cortocircuito.

Con `&&`, si la izquierda falla, la derecha no se ejecuta.

Con `||`, si la izquierda tiene éxito, la derecha no se ejecuta.

Esta idea será la base del siguiente módulo sobre `if`.

## 21. No memorices `A && B || C` como `if/else`

Este patrón:

```bash
A && B || C
```

parece significar “si A funciona ejecuta B; si no, C”, pero no siempre es equivalente.

Si `A` tiene éxito pero `B` falla, entonces `C` puede ejecutarse.

Por eso no lo usaremos como sustituto general de una estructura `if/else`.

## 22. Asociatividad

Las listas `&&` y `||` se evalúan con asociatividad hacia la izquierda. Las cadenas mixtas pueden resultar menos intuitivas de lo que parecen.

Regla inicial: usa cadenas cortas y claras.

## 23. Diferencia esencial

| Operador | ¿Cuándo se ejecuta la orden de la derecha? |
|---|---|
| `;` | después de la izquierda, independientemente del resultado |
| `&&` | solo si la izquierda devuelve `0` |
| `||` | solo si la izquierda devuelve un valor distinto de `0` |

## 24. Varias órdenes con `&&`

```bash
mkdir -p ~/linux-lab/modulo-25-status \
    && cd ~/linux-lab/modulo-25-status \
    && pwd
```

Cada orden depende del éxito de la anterior. Si alguna falla, las posteriores de esa cadena AND ya no se ejecutan.

## 25. Tuberías y estado de salida

Ya conoces:

```text
orden1 | orden2
```

En Bash, por defecto, el estado de una tubería es el estado de la **última orden** de la tubería.

Eso significa que un fallo anterior puede no quedar reflejado en el estado final.

## 26. `pipefail`

Bash dispone de la opción `pipefail`, que cambia cómo se calcula el estado de una tubería.

No la activaremos todavía como política del manual. Se estudiará junto con manejo de errores en el Módulo 29.

Por ahora recuerda: **sin `pipefail`, normalmente manda el estado de la última orden de la tubería**.

## 27. La negación `!`

Bash puede negar lógicamente el estado de una tubería:

```bash
! true
```

No la necesitamos todavía para nuestras prácticas principales; se incluye para reconocerla cuando aparezca en ejemplos posteriores.

## 28. Preparar el laboratorio

```bash
test -d ~/linux-lab && \
cd ~/linux-lab && \
mkdir -p modulo-25-status && \
cd modulo-25-status && pwd
```

Etiqueta de práctica: **creación en laboratorio**. No uses `sudo`.

## 29. Práctica A — observar éxito

```bash
true
estado=$?
printf 'true devolvió: %s\n' "$estado"
```

Predice el resultado antes de ejecutar.

## 30. Práctica B — observar fallo

```bash
false
estado=$?
printf 'false devolvió: %s\n' "$estado"
```

Resultado esperado: `1`.

## 31. Práctica C — comprobar que `$?` cambia

```bash
false
printf 'Este printf se ejecutó\n'
estado=$?
printf 'Estado guardado: %s\n' "$estado"
```

Pregunta: ¿ese estado corresponde a `false` o al primer `printf`?

Respuesta: corresponde al `printf`, porque fue la orden más reciente.

## 32. Práctica D — conservar correctamente el estado

```bash
false
estado=$?
printf 'Estado de false: %s\n' "$estado"
```

## 33. Práctica E — `&&`

```bash
true && printf 'segunda orden ejecutada\n'
```

```bash
false && printf 'esta línea no debe aparecer\n'
```

Explica con tus palabras por qué cambia el resultado.

## 34. Práctica F — `||`

```bash
false || printf 'se ejecutó la alternativa\n'
```

```bash
true || printf 'esta línea no debe aparecer\n'
```

## 35. Práctica G — comparar operadores

Predice antes de ejecutar:

```bash
false; printf 'A\n'
false && printf 'B\n'
false || printf 'C\n'
```

Debes poder explicar por qué aparecen unas letras y otras no.

## 36. Práctica H — script con salida explícita

Crea `estado.sh`:

```bash
#!/usr/bin/env bash

printf 'El script terminó correctamente\n'
exit 0
```

Valida:

```bash
bash -n estado.sh
```

Ejecuta:

```bash
bash estado.sh
printf 'Estado del script: %s\n' "$?"
```

## 37. Práctica I — dependencia obligatoria

Crea `entrar_laboratorio.sh`:

```bash
#!/usr/bin/env bash

cd ~/linux-lab || exit 1
printf 'Estoy dentro del laboratorio\n'
pwd
```

Si `cd` falla, el script termina. Si tiene éxito, continúa.

## 38. Errores frecuentes

| Error | Problema | Corrección |
|---|---|---|
| Consultar `$?` después de otra orden | El estado anterior ya se perdió | Guárdalo inmediatamente |
| Usar `;` esperando dependencia | La derecha se ejecuta aunque falle la izquierda | Usa `&&` si depende del éxito |
| Usar `&&` esperando reacción a fallo | La derecha solo corre con `0` | Usa `||` para una alternativa por fallo |
| Usar `||` como si terminara el script | Puede ejecutar una alternativa y continuar | Usa `exit` cuando corresponda |
| Memorizar `A && B || C` como `if/else` | `C` puede ejecutarse si `B` falla | Usa `if` cuando lo estudies |
| Interpretar texto visible como estado | Son conceptos separados | Consulta el código de salida |
| Tratar todo estado no cero como error operativo | Algunos programas usan estados especiales esperados | Consulta la documentación del comando y separa semántica de Bash de semántica del programa |
| Encadenar cambios de alto impacto | Reduce oportunidades de revisar | Mantén pasos controlados |
| Asumir que una tubería refleja todos los fallos | Por defecto usa la última orden | Estudiaremos `pipefail` en el Módulo 29 |

## 39. Método seguro para componer órdenes

1. comprende cada orden por separado;
2. identifica cuál depende de cuál;
3. decide si la derecha debe ejecutarse siempre, solo con éxito o solo con fallo;
4. elige `;`, `&&` o `||`;
5. evita cadenas largas;
6. verifica ruta y entorno;
7. no introduzcas operaciones destructivas para practicar;
8. conserva estados importantes inmediatamente;
9. prueba primero con `true`, `false` y `printf`.

## 40. Práctica independiente

Crea `comprobar_laboratorio.sh` que:

1. use Bash;
2. intente entrar a `~/linux-lab`;
3. termine con fallo si no puede entrar;
4. muestre el directorio actual si tuvo éxito;
5. cree o entre en `modulo-25-status` usando una dependencia con `&&`;
6. termine explícitamente con `exit 0`;
7. pase `bash -n`;
8. no use `sudo` ni borre archivos;
9. pueda explicarse línea por línea.

No se considerará dominado solo porque funcione: también debes explicar por qué elegiste `&&` o `||`.

## 41. Mini evaluación

1. ¿qué valor representa éxito para Bash? A) `0` B) `1`
2. ¿todo valor distinto de `0` tiene exactamente el mismo significado? A) Sí B) No
3. ¿qué contiene `$?`? A) Estado de la última orden B) PID del script
4. ¿qué operador ejecuta la derecha solo si la izquierda tuvo éxito? A) `&&` B) `||`
5. ¿qué operador ejecuta la derecha solo si la izquierda falló? A) `&&` B) `||`
6. ¿`;` impide ejecutar la segunda orden si falla la primera? A) Sí B) No
7. ¿`false` devuelve normalmente un estado distinto de cero? A) Sí B) No
8. ¿`exit 0` indica éxito? A) Sí B) No
9. ¿Bash usa `127` cuando no encuentra una orden? A) Sí B) No
10. ¿`A && B || C` es siempre equivalente a `if/else`? A) Sí B) No
11. Por defecto, ¿qué orden determina el estado de una tubería? A) Primera B) Última
12. ¿debes consultar la documentación para interpretar códigos específicos? A) Sí B) No
13. Si `dnf check-update` devuelve `100`, ¿significa necesariamente un error? A) Sí B) No
14. ¿un estado `100` hace que Bash considere exitosa la condición de `&&`? A) Sí B) No

## 42. Registro de aprendizaje

```text
Un código de salida es:
0 significa:
Un valor no-cero significa para el control de flujo de Bash:
¿Por qué no siempre equivale a un error operativo?:
¿Qué significa 100 para dnf check-update?:
$? contiene:
¿Por qué debo guardar $? inmediatamente?:
; significa:
&& significa:
|| significa:
exit sirve para:
127 en Bash puede indicar:
126 en Bash puede indicar:
¿Por qué A && B || C no es un if/else general?:
Estado por defecto de una tubería:
Algo que todavía confundo:
Estado: EN APRENDIZAJE / PRACTICADO
```

## 43. Conexión con el siguiente módulo

El modelo aprendido es:

```text
orden → estado 0/no-cero → decisión
```

El Módulo 26 añadirá `if`, `test`, `[ ]`, `[[ ]]`, `case` y aritmética.

## 44. Fuentes y límites

Fuentes principales:

- DNF Project — check-update: https://dnf.readthedocs.io/en/latest/command_ref.html#check-update-command
- GNU Bash Reference Manual — Exit Status: https://www.gnu.org/software/bash/manual/html_node/Exit-Status.html
- GNU Bash Reference Manual — Lists of Commands: https://www.gnu.org/software/bash/manual/html_node/Lists.html
- GNU Bash Reference Manual — Pipelines: https://www.gnu.org/software/bash/manual/html_node/Pipelines.html
- GNU Bash Reference Manual — Bourne Shell Builtins: https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html

Puntos verificados documentalmente: `0` representa éxito; `$?` contiene el estado de la última orden; `&&` depende de éxito; `||` depende de fallo; `126` y `127` tienen usos especiales; una señal fatal `N` se representa como `128 + N`; y por defecto una tubería toma el estado de su última orden.

Se posponen: `if`, `test`, `[ ]`, `[[ ]]`, `case`, comparaciones, `set -e`, `set -u`, `pipefail` como política, `trap`, funciones y `return`.

**Estado de la lección:** redactada y revisada documentalmente contra GNU Bash 5.3. Las prácticas son locales, no destructivas y no requieren privilegios.

---

**Siguiente:** [Módulo 26 — Decisiones con `if`, `test`, `[ ]`, `[[ ]]`, `case` y aritmética](modulo-26-if-test-condicionales-case-aritmetica.md) · [Volver al índice](README.md)
