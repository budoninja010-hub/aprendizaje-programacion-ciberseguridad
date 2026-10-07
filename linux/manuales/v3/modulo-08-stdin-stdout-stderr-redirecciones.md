# Módulo 8 — stdin, stdout, stderr y redirecciones

Manual Maestro de Linux y Shell Scripting — Edición 2026 · v3 · Octava entrega.

[Estado actual](README.md) · [Módulo anterior](modulo-07-cat-less-head-tail.md) · [Arquitectura](00-indice-arquitectura.md)

## 1. Qué aprenderás

Al terminar este módulo podrás:

- explicar qué son la entrada estándar, la salida estándar y la salida de error;
- reconocer los descriptores 0, 1 y 2;
- distinguir mostrar salida en pantalla de guardarla en un archivo;
- usar `>`, `>>` y `2>` dentro del laboratorio;
- explicar por qué `>` puede truncar o reemplazar el contenido previo de un archivo;
- separar la salida normal de los mensajes de error;
- comprobar el destino antes de redirigir.

Conocimientos previos:
- navegación con `pwd`, `ls` y `cd`;
- creación y lectura de archivos;
- uso básico de `cat`, `head`, `tail` y `less`.

**Seguridad:** todas las prácticas se limitan a `~/linux-lab`. No se redirigirá hacia `/etc`, `/usr`, `/var`, `/proc` ni `/sys`. No uses `sudo` para forzar una redirección. Antes de usar `>`, verifica la ruta y decide si puedes perder el contenido existente del archivo destino.

## 2. La idea central: los programas reciben y producen datos

Muchos programas trabajan con flujos.

Modelo simplificado:

```text
entrada ──► programa ──► salida
                    └──► errores
```

En Unix y GNU/Linux se utilizan tres flujos estándar:

- **stdin**: entrada estándar;
- **stdout**: salida estándar;
- **stderr**: salida estándar de error.

No todos los programas usan los tres de la misma manera, pero este modelo es fundamental para comprender la shell.

## 3. stdin — entrada estándar

**stdin** es el flujo de entrada estándar.

Su descriptor tradicional es:

```text
0
```

En muchos comandos interactivos, stdin recibe lo que escribes con el teclado.

Ejemplo conceptual:

```bash
cat
```

Si ejecutas `cat` sin indicar un archivo, puede leer desde la entrada estándar y mostrar lo recibido.

Para terminar una entrada interactiva de este tipo suele usarse una señal de fin de archivo desde la terminal, por ejemplo `Ctrl+D` en Bash/terminales tipo Unix.

No necesitamos practicar esto todavía si te resulta confuso; lo importante es entender que un programa puede leer datos sin que provengan necesariamente de un archivo.

## 4. stdout — salida estándar

**stdout** es la salida estándar.

Descriptor:

```text
1
```

Ejemplo:

```bash
printf 'hola\n'
```

Normalmente verás:

```text
hola
```

El programa escribió en stdout y la terminal mostró ese flujo.

**Importante:** que algo aparezca en pantalla no significa que se haya guardado en un archivo.

## 5. stderr — salida de error

**stderr** es un flujo separado para diagnósticos y errores.

Descriptor:

```text
2
```

Ejemplo dentro del laboratorio, usando un nombre que no exista:

```bash
ls archivo-que-no-existe
```

Puedes recibir un mensaje de error.

Ese mensaje normalmente va a stderr, no al mismo flujo lógico que la salida normal.

**Para qué sirve separarlos:** permite guardar o procesar la salida correcta sin mezclarla necesariamente con los errores.

## 6. Los tres descriptores básicos

Memoriza este mapa:

```text
0 = stdin
1 = stdout
2 = stderr
```

No significa que un proceso solo pueda abrir tres archivos. Significa que esos tres descriptores tienen funciones estándar convencionales.

**Ejercicio:** explica qué descriptor usarías para referirte a la salida de error.

## 7. Redirección: cambiar el destino de un flujo

La shell puede redirigir un flujo.

Ejemplo:

```bash
printf 'hola\n' > saludo.txt
```

Aquí stdout ya no se muestra principalmente en pantalla: la shell abre `saludo.txt` como destino de la salida.

Después:

```bash
cat saludo.txt
```

verás:

```text
hola
```

## 8. > — escribir reemplazando el contenido previo

El operador:

```text
>
```

redirige stdout hacia un archivo.

Ejemplo:

```bash
printf 'primera versión\n' > ejemplo.txt
```

Después:

```bash
printf 'segunda versión\n' > ejemplo.txt
```

El contenido previo puede quedar reemplazado.

Eso se denomina **truncamiento** del archivo destino en este contexto.

### Regla crítica

Antes de usar `>`:

1. comprueba dónde estás con `pwd`;
2. comprueba si el destino ya existe;
3. decide si puedes perder su contenido;
4. solo entonces ejecuta la redirección.

No uses `>` sobre archivos importantes para “probar”.

## 9. >> — agregar al final

El operador:

```text
>>
```

agrega stdout al final del archivo en lugar de reemplazar todo su contenido.

Ejemplo:

```bash
printf 'línea 1\n' > lista.txt
printf 'línea 2\n' >> lista.txt
```

Después:

```bash
cat lista.txt
```

Salida esperada:

```text
línea 1
línea 2
```

**Diferencia clave:**

```text
>  = reemplazar/truncar el destino
>> = agregar al final
```

## 10. > no significa “guardar de forma segura”

El hecho de usar redirección no crea automáticamente una copia de seguridad.

Si escribes:

```bash
comando > archivo-importante.txt
```

y el destino existe, puedes perder su contenido anterior.

Por eso en este curso las primeras prácticas usan nombres creados específicamente para el laboratorio.

## 11. 2> — redirigir stderr

Puedes redirigir la salida de error con:

```bash
comando 2> errores.txt
```

Ejemplo seguro:

```bash
ls archivo-inexistente 2> errores.txt
```

Después:

```bash
cat errores.txt
```

Deberías ver el diagnóstico que antes aparecía en pantalla.

Explicación:

- `2` identifica stderr;
- `>` indica redirección;
- `errores.txt` es el destino.

## 12. 1> y > suelen representar stdout

Puedes escribir explícitamente:

```bash
printf 'hola\n' 1> salida.txt
```

En estos ejemplos, equivale a:

```bash
printf 'hola\n' > salida.txt
```

porque `>` sin descriptor explícito redirige stdout.

Para principiantes usaremos normalmente `>` para stdout y `2>` para stderr.

## 13. Separar salida normal y errores

Supón que una orden produce:
- información válida;
- mensajes de error.

Puedes enviarlos a archivos distintos:

```bash
comando > salida.txt 2> errores.txt
```

Modelo:

```text
stdout ──► salida.txt
stderr ──► errores.txt
```

Esto es especialmente útil en scripts y diagnósticos.

## 14. El orden de las redirecciones puede importar

Las redirecciones se procesan en el orden escrito por la shell.

Esto se vuelve importante con construcciones como:

```text
2>&1
```

Todavía no necesitas dominarla.

Solo conserva esta idea:

> Redirigir stdout y stderr no siempre es intercambiable si se cambia el orden.

La combinación avanzada de flujos se estudiará más adelante, después de dominar cada descriptor por separado.

## 15. stdin desde un archivo con <

También existe la redirección de entrada:

```text
<
```

Ejemplo conceptual:

```bash
comando < datos.txt
```

La shell conecta el contenido del archivo con stdin del programa.

Un ejemplo simple:

```bash
cat < notas.txt
```

puede mostrar el contenido, aunque para `cat` es más sencillo escribir:

```bash
cat notas.txt
```

El objetivo es comprender el flujo, no complicar una tarea simple.

## 16. Preparar la práctica

Entra al laboratorio:

```bash
cd ~/linux-lab
pwd
ls -la
```

Comprueba si existe:

```bash
ls -ld ./modulo-08-redirecciones
```

Si no existe:

```bash
mkdir modulo-08-redirecciones
```

Después:

```bash
cd ./modulo-08-redirecciones
pwd
ls -la
```

No borres prácticas anteriores.

## 17. Práctica A — stdout con >

Primero verifica que el nombre de destino esté libre:

```bash
ls -l salida.txt
```

Si no existe, crea contenido con:

```bash
printf 'uno\n' > salida.txt
```

Comprueba:

```bash
cat salida.txt
```

Ahora ejecuta:

```bash
printf 'dos\n' > salida.txt
```

Comprueba otra vez:

```bash
cat salida.txt
```

Explica qué ocurrió con `uno`.

## 18. Práctica B — agregar con >>

Ahora:

```bash
printf 'tres\n' >> salida.txt
```

Después:

```bash
cat salida.txt
```

Debes ver:

```text
dos
tres
```

Explica por qué `dos` no desapareció esta vez.

## 19. Práctica C — stderr con 2>

Provoca un error seguro:

```bash
ls nombre-que-no-existe 2> errores.txt
```

Comprueba:

```bash
cat errores.txt
```

No importa que el texto exacto del error cambie según idioma o versión. Lo importante es que el diagnóstico se guardó en `errores.txt`.

## 20. Práctica D — separar stdout y stderr

Ejecuta una orden que produzca al menos una salida normal y un error. Una forma segura es pedir a `ls` un archivo que existe y otro que no:

```bash
touch existe.txt
ls existe.txt no-existe.txt > correctos.txt 2> fallos.txt
```

Después:

```bash
cat correctos.txt
cat fallos.txt
```

Debes poder explicar qué flujo terminó en cada archivo.

## 21. Práctica E — entrada con <

Crea un archivo:

```bash
printf 'alpha\nbeta\ngamma\n' > entrada.txt
```

Después:

```bash
cat < entrada.txt
```

Compara con:

```bash
cat entrada.txt
```

La salida puede verse igual, pero el modo en que `cat` recibe los datos no es conceptualmente idéntico.

## 22. Qué pasa si el comando falla

Una redirección puede ocurrir incluso cuando el comando no produce la salida que esperabas.

Por ejemplo, si el archivo destino de stdout se abre antes y el comando después falla, el archivo puede haberse creado o truncado.

Por eso:

> Nunca uses un archivo importante como destino de prueba solo porque “el comando probablemente falle”.

Este detalle es una razón más para trabajar dentro de `~/linux-lab`.

## 23. sudo y redirecciones: error de concepto frecuente

Una construcción como:

```text
sudo echo "dato" > /ruta/protegida
```

no significa que la redirección `>` se ejecute automáticamente con privilegios elevados.

La shell que procesa la redirección intenta abrir el archivo en su propio contexto.

En este curso no usaremos esto para escribir archivos del sistema. Cuando llegue el momento de administración, aprenderás mecanismos apropiados y sus riesgos.

**Regla:** no añadas `sudo` a ciegas para “arreglar” una redirección que falla.

## 24. Redirección y permisos

Si no tienes permiso para escribir en un destino, puedes recibir:

```text
Permission denied
```

No es una invitación automática a usar privilegios.

Primero revisa:
- si estás en la ruta correcta;
- si el archivo pertenece al laboratorio;
- si realmente debes modificarlo;
- si se trata de un archivo del sistema.

## 25. Privacidad

Redirigir salida a un archivo puede guardar datos sensibles que antes solo veías en pantalla.

Antes de conservar o subir un archivo generado, revisa si contiene:

- nombres personales;
- rutas privadas;
- direcciones IP;
- tokens;
- contraseñas;
- cookies;
- claves;
- información de servicios;
- logs con datos sensibles.

No subas esos archivos a GitHub.

## 26. Errores frecuentes

| Error | Qué pasó | Corrección |
|---|---|---|
| Usaste `>` pensando que agregaba | Truncaste el archivo | Usa `>>` solo cuando realmente quieras añadir |
| El error sigue apareciendo en pantalla | Solo redirigiste stdout | Usa `2>` si necesitas redirigir stderr |
| `2>` crea un archivo vacío | No hubo error o stderr no produjo contenido | Comprueba la orden y el flujo esperado |
| Pusiste `sudo` delante de `echo` y la redirección falló | La shell procesa `>` fuera del `sudo` del comando | No fuerces; aprende el mecanismo apropiado más adelante |
| Redirigiste hacia el archivo equivocado | Ruta mal verificada | Revisa `pwd`, destino y existencia antes |
| Guardaste un log con secretos | No revisaste la salida | Sanitiza o elimina del flujo de publicación; no lo subas a GitHub |

## 27. Práctica independiente

Dentro de una carpeta nueva del laboratorio:

1. crea un archivo con una línea usando `>`;
2. reemplaza su contenido con otra línea;
3. agrega una tercera línea con `>>`;
4. provoca un error seguro con `ls` sobre un nombre inexistente;
5. guarda ese error con `2>`;
6. muestra ambos archivos con `cat`;
7. explica qué flujo representa cada archivo;
8. no uses `sudo`.

## 28. Mini evaluación

1. ¿Qué descriptor corresponde a stdin?
   - A) 0
   - B) 1
   - C) 2

2. ¿Qué descriptor corresponde a stdout?
   - A) 0
   - B) 1
   - C) 2

3. ¿Qué descriptor corresponde a stderr?
   - A) 0
   - B) 1
   - C) 2

4. ¿Qué hace `>` normalmente en estos ejemplos?
   - A) Agrega al final.
   - B) Redirige stdout y puede truncar el destino.
   - C) Cambia permisos.
   - D) Borra directorios.

5. ¿Qué hace `>>`?
   - A) Agrega al final.
   - B) Redirige stderr.
   - C) Cambia de usuario.
   - D) Reinicia la shell.

6. ¿Qué hace `2>`?
   - A) Redirige stdin.
   - B) Redirige stdout.
   - C) Redirige stderr.

7. ¿Debes usar `sudo` automáticamente si una redirección falla por permisos?
   - A) Sí.
   - B) No.

8. ¿`>` puede crear o truncar el archivo destino aunque el comando no produzca la salida esperada?
   - A) Sí, dependiendo de cómo se procese la orden.
   - B) No, nunca.

## 29. Registro de aprendizaje

Puedes responder:

```text
stdin es:
stdout es:
stderr es:
0 significa:
1 significa:
2 significa:
> sirve para:
>> sirve para:
2> sirve para:
El principal riesgo de > es:
Algo que todavía confundo:
Estado: EN APRENDIZAJE / PRACTICADO
```

## 30. Fuentes y límites

Fuentes principales:

- GNU Bash Reference Manual — Redirections:
  https://www.gnu.org/software/bash/manual/html_node/Redirections.html
- GNU Bash Reference Manual — Shell Operation:
  https://www.gnu.org/software/bash/manual/html_node/Shell-Operation.html
- POSIX / shell conventions for standard file descriptors are reflected in Bash documentation and Unix process semantics.

Esta lección cubre solo los fundamentos. Se posponen:

- `2>&1`;
- `&>`;
- here-documents;
- here-strings;
- process substitution;
- redirecciones avanzadas con descriptores personalizados;
- `noclobber`;
- agrupación compleja de comandos.

**Estado de la lección:** redactada y revisada documentalmente. La práctica real del estudiante sigue pendiente.

Siguiente módulo por redactar: **Módulo 9 — Tuberías (pipes) y composición de comandos**.
