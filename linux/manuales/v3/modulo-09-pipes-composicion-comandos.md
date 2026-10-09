# Módulo 9 — Tuberías (pipes) y composición de comandos

Manual Maestro de Linux y Shell Scripting — Edición 2026 · v3 · Novena entrega.

[Índice del manual](README.md) · [← Módulo 8](modulo-08-stdin-stdout-stderr-redirecciones.md) · [Arquitectura](00-indice-arquitectura.md) · [Módulo 10 →](modulo-10-grep-find-locate.md)

## 1. Qué aprenderás

Al terminar este módulo podrás:

- explicar qué hace una tubería `|`;
- conectar la salida estándar de un comando con la entrada estándar de otro;
- distinguir una tubería de una redirección hacia archivo;
- construir cadenas pequeñas de comandos sin crear archivos intermedios;
- reconocer que stderr no entra automáticamente en la tubería normal;
- leer una tubería de izquierda a derecha;
- detectar cuándo una tubería añade complejidad innecesaria.

Conocimientos previos:
- stdin, stdout y stderr;
- descriptores 0, 1 y 2;
- `>`, `>>` y `2>`;
- lectura con `cat`, `head`, `tail` y `less`.

**Seguridad:** las prácticas se realizan en `~/linux-lab` y usan datos creados por nosotros. No canalices a una shell código descargado o desconocido. Una tubería puede encadenar operaciones rápidamente; por eso debes comprender cada comando por separado antes de unirlos.

## 2. Qué es una tubería

Una tubería, o **pipe**, conecta la salida estándar de un comando con la entrada estándar del siguiente.

Símbolo:

```text
|
```

Modelo:

```text
comando A stdout ──► stdin comando B
```

Ejemplo:

```bash
printf 'uno\ndos\ntres\n' | head -n 2
```

Aquí:

1. `printf` produce tres líneas en stdout.
2. `|` conecta esa salida con stdin de `head`.
3. `head -n 2` conserva las primeras dos líneas que recibe.

Salida esperada:

```text
uno
dos
```

## 3. La tubería no guarda automáticamente en un archivo

Compara:

```bash
printf 'hola\n' | cat
```

con:

```bash
printf 'hola\n' > saludo.txt
```

En el primer caso, stdout de `printf` pasa a stdin de `cat`.

En el segundo, stdout se redirige a un archivo.

Modelo:

```text
|  = conectar programas
>  = enviar salida a un archivo y puede truncarlo
>> = agregar salida a un archivo
```

**Error típico:** pensar que una tubería crea un archivo. No lo hace por sí sola.

## 4. Leer una tubería de izquierda a derecha

Ejemplo:

```bash
printf 'rojo\nverde\nazul\n' | tail -n 1
```

Léelo así:

> “Genera tres líneas y entrega esa salida a `tail`, que conserva la última.”

Salida:

```text
azul
```

No intentes entender una cadena larga de golpe. Separa cada etapa.

## 5. Cada comando debe tener sentido por separado

Antes de unir:

```bash
comandoA | comandoB
```

pregunta:

- ¿qué produce `comandoA` en stdout?;
- ¿qué espera `comandoB` en stdin?;
- ¿el formato producido por A tiene sentido para B?

Una tubería no “traduce” automáticamente datos incompatibles.

## 6. Un ejemplo con un archivo

Supón que `lectura.txt` contiene muchas líneas.

Puedes escribir:

```bash
cat lectura.txt | head -n 3
```

Esto funciona como demostración del flujo:

```text
archivo → cat → stdout → pipe → head
```

Pero para esta tarea concreta existe una forma más simple:

```bash
head -n 3 lectura.txt
```

**Lección:** que una tubería funcione no significa que sea la solución más clara.

Evita añadir comandos que no aportan valor.

## 7. Contar líneas con wc -l

`wc` significa *word count*. Una de sus opciones es:

```text
-l
```

que cuenta líneas.

Ejemplo:

```bash
printf 'a\nb\nc\n' | wc -l
```

Salida esperada:

```text
3
```

No necesitas dominar todavía todas las funciones de `wc`. Aquí se usa para mostrar cómo un programa puede consumir el flujo producido por otro.

Referencia: GNU Coreutils — `wc`.

## 8. Varias etapas

Una tubería puede tener más de dos comandos.

Ejemplo:

```bash
printf 'uno\ndos\ntres\ncuatro\n' | head -n 3 | tail -n 1
```

Paso a paso:

1. `printf` produce cuatro líneas.
2. `head -n 3` deja:
   `uno`, `dos`, `tres`.
3. `tail -n 1` toma la última de esas tres.
4. Resultado:

```text
tres
```

### Regla pedagógica

Empieza con dos etapas.

Añade una tercera solo cuando puedas explicar las dos anteriores.

## 9. stdout sí; stderr no entra por defecto en |

La tubería normal conecta **stdout** del comando izquierdo con stdin del derecho.

Ejemplo conceptual:

```text
stdout ──► |
stderr ──► terminal
```

Si el comando izquierdo produce un error, ese mensaje puede seguir apareciendo en la terminal aunque stdout esté conectado a otra orden.

No introduciremos todavía combinaciones avanzadas como `2>&1` o `|&`. Primero domina la separación de flujos.

## 10. Tubería frente a archivo intermedio

Sin tubería podrías imaginar:

```text
comando A → archivo temporal → comando B
```

Con pipe:

```text
comando A → comando B
```

Ventaja:
- evita crear un archivo intermedio cuando no hace falta.

Pero no significa que todos los datos existan mágicamente “a la vez”. Los procesos pueden producir y consumir datos conforme avanzan.

No necesitamos estudiar todavía buffers, bloqueos ni detalles internos del kernel.

## 11. La shell participa en la tubería

En Bash, la shell reconoce el operador `|` y crea la conexión entre los procesos o comandos de la pipeline.

Por eso:

```bash
printf 'hola\n' | cat
```

no entrega el carácter `|` como argumento ordinario a `printf`.

La shell interpreta primero la estructura de la orden.

## 12. Pipeline no significa ejecución “segura”

Una tubería puede conectar comandos inocuos, pero también podría conectar una fuente de datos con una operación destructiva o con un intérprete.

Por eso este manual aplica una regla estricta:

> No canalices contenido descargado o desconocido directamente hacia `bash`, `sh`, `python` u otro intérprete.

Primero debes conocer el origen, revisar el contenido y entender qué ejecutaría.

En los laboratorios iniciales usaremos únicamente texto creado por nosotros y comandos de lectura/procesamiento.

## 13. No confundas | con ||

Estos símbolos son distintos:

```text
|   = tubería
||  = operador lógico de control
```

`||` se estudiará más adelante con códigos de salida y control de flujo.

No escribas dos barras cuando solo quieres conectar stdout con stdin.

## 14. Preparar la práctica

Entra al laboratorio:

```bash
cd ~/linux-lab
pwd
ls -la
```

Comprueba si existe:

```bash
ls -ld ./modulo-09-pipes
```

Si no existe:

```bash
mkdir modulo-09-pipes
```

Después:

```bash
cd ./modulo-09-pipes
pwd
ls -la
```

No borres una práctica anterior si ya existe.

## 15. Práctica A — primera tubería

Ejecuta:

```bash
printf 'uno\ndos\ntres\n' | head -n 2
```

Antes de mirar la salida intenta predecirla.

Después explica:

- qué comando produce datos;
- qué comando recibe datos;
- qué hace `|`.

## 16. Práctica B — principio y final

Ejecuta:

```bash
printf '1\n2\n3\n4\n5\n' | tail -n 2
```

Salida esperada:

```text
4
5
```

Ahora cambia solo el consumidor:

```bash
printf '1\n2\n3\n4\n5\n' | head -n 2
```

Explica por qué la fuente es la misma pero el resultado cambia.

## 17. Práctica C — contar líneas

Ejecuta:

```bash
printf 'alpha\nbeta\ngamma\ndelta\n' | wc -l
```

Debes obtener:

```text
4
```

Pregunta:

> ¿`wc -l` leyó un archivo?

En esta práctica, no. Recibió su entrada desde la tubería.

## 18. Práctica D — tres etapas

Ejecuta:

```bash
printf 'a\nb\nc\nd\ne\n' | head -n 4 | tail -n 2
```

Razonamiento:

1. fuente: cinco líneas;
2. primera etapa: quedan cuatro;
3. segunda etapa: quedan las dos últimas de esas cuatro.

Predice el resultado antes de ejecutarlo.

## 19. Práctica E — usar un archivo existente

Crea un archivo de práctica:

```bash
printf 'enero\nfebrero\nmarzo\nabril\nmayo\n' > meses.txt
```

Ya conoces el riesgo de `>`: hazlo solo si `meses.txt` es un nombre destinado a esta práctica y su contenido puede ser reemplazado.

Después:

```bash
cat meses.txt | tail -n 2
```

Comprueba también la versión más simple:

```bash
tail -n 2 meses.txt
```

Las salidas deberían coincidir.

**Conclusión:** la tubería es útil, pero no debe añadirse sin necesidad.

## 20. Práctica F — stderr no se canaliza normalmente

Ejecuta:

```bash
ls archivo-inexistente | wc -l
```

Observa dos cosas:

- el diagnóstico de `ls` puede aparecer en la terminal porque va por stderr;
- `wc -l` recibe stdout de `ls`, que en este caso puede estar vacío.

No necesitas memorizar el número exacto mostrado por `wc`; entiende la separación de flujos.

## 21. Pipes y less

Un caso útil:

```bash
printf 'uno\ndos\ntres\ncuatro\ncinco\n' | less
```

`less` puede recibir datos por stdin.

Pulsa:

```text
q
```

para salir.

Esto muestra que un paginador no necesita obligatoriamente recibir un nombre de archivo.

## 22. Errores frecuentes

| Error | Qué ocurre | Corrección |
|---|---|---|
| Crees que `|` crea un archivo | Pipe conecta flujos | Usa redirección solo cuando realmente quieras un archivo |
| Confundes `|` con `||` | Son operadores distintos | Una barra para pipe; `||` se estudiará después |
| Esperas que stderr pase por el pipe | Pipe normal toma stdout | Mantén separados los flujos por ahora |
| Añades `cat` innecesariamente | La tubería funciona pero complica | Usa la forma directa cuando el comando acepta archivo |
| Una cadena larga no se entiende | Hay demasiadas etapas | Prueba y explica cada etapa por separado |
| Canalizas código desconocido a una shell | Ejecutarías contenido sin revisarlo | No lo hagas; inspecciona y comprende antes |
| Un resultado es distinto de lo previsto | Alguna etapa transforma datos de otra forma | Ejecuta etapas por separado y compara |

## 23. Método de diagnóstico de una pipeline

Si esta cadena falla:

```text
A | B | C
```

no cambies opciones al azar.

Haz:

1. ejecuta A y observa stdout;
2. conecta A con B;
3. comprueba el resultado;
4. solo después agrega C;
5. revisa errores por separado.

Este método reduce la cantidad de cosas que intentas depurar al mismo tiempo.

## 24. Práctica independiente

Sin copiar los ejemplos exactos:

1. genera seis líneas con `printf`;
2. usa un pipe para conservar las primeras cuatro;
3. añade una segunda etapa para conservar las últimas dos de esas cuatro;
4. predice el resultado antes de ejecutar;
5. crea otro flujo y cuenta sus líneas con `wc -l`;
6. explica cuál comando fue productor y cuál consumidor en cada caso;
7. identifica una situación donde un pipe sería innecesario.

No uses intérpretes, comandos destructivos ni datos descargados.

## 25. Mini evaluación

1. ¿Qué hace `|`?
   - A) Borra un archivo.
   - B) Conecta stdout del comando izquierdo con stdin del derecho.
   - C) Cambia permisos.
   - D) Crea un usuario.

2. ¿Una tubería normal envía stderr automáticamente al comando siguiente?
   - A) Sí.
   - B) No.

3. ¿Qué diferencia principal existe entre `|` y `>`?
   - A) Ninguna.
   - B) `|` conecta comandos; `>` redirige salida hacia un archivo.
   - C) `|` siempre borra archivos.
   - D) `>` siempre conecta dos programas.

4. ¿Qué hace `wc -l` en los ejemplos?
   - A) Cuenta líneas.
   - B) Borra líneas.
   - C) Cambia de carpeta.
   - D) Reinicia.

5. En:
   `printf 'a\nb\nc\n' | head -n 1`
   ¿qué comando produce los datos?
   - A) `head`
   - B) `printf`

6. ¿Es buena práctica canalizar un script descargado y desconocido directamente hacia `bash`?
   - A) Sí.
   - B) No.

7. Si una pipeline larga falla, ¿qué estrategia es mejor?
   - A) Añadir más comandos.
   - B) Probar cada etapa progresivamente.
   - C) Usar `sudo`.
   - D) Borrar el laboratorio.

## 26. Registro de aprendizaje

Puedes responder:

```text
Una tubería sirve para:
El comando de la izquierda entrega:
El comando de la derecha recibe:
La diferencia entre | y > es:
stderr en una tubería normal:
wc -l sirve para:
Un ejemplo donde no necesito pipe:
Un error que ya sé diagnosticar:
Algo que todavía confundo:
Estado: EN APRENDIZAJE / PRACTICADO
```

No se considera dominado con una sola pipeline correcta. Debes poder predecir resultados, construir una combinación nueva y detectar una etapa incorrecta.

## 27. Fuentes y límites

Clasificación y estado de los enlaces de esta sección: [catálogo de fuentes](06-catalogo-fuentes.md) (jerarquía E04, comprobación del 9 de octubre de 2026).

Fuentes principales:

- GNU Bash Reference Manual — Pipelines:
  https://www.gnu.org/software/bash/manual/html_node/Pipelines.html
- GNU Bash Reference Manual — Redirections:
  https://www.gnu.org/software/bash/manual/html_node/Redirections.html
- GNU Coreutils — `wc`:
  https://www.gnu.org/software/coreutils/manual/html_node/wc-invocation.html
- GNU Coreutils — `head` y `tail`:
  https://www.gnu.org/software/coreutils/manual/html_node/head-invocation.html
  https://www.gnu.org/software/coreutils/manual/html_node/tail-invocation.html

Se posponen para módulos posteriores:

- estado de salida de una pipeline;
- `pipefail`;
- `PIPESTATUS`;
- `||` y `&&`;
- `|&`;
- combinación avanzada de stderr con stdout;
- procesos y concurrencia internos de pipelines.

**Estado de la lección:** redactada y revisada documentalmente. La práctica real del estudiante sigue pendiente.

---

**Siguiente:** [Módulo 10 — grep, find y locate: buscar texto y archivos](modulo-10-grep-find-locate.md) · [Volver al índice](README.md)
