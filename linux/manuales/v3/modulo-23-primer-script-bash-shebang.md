# Módulo 23 — Primer script Bash y shebang

Manual Maestro de Linux y Shell Scripting — Edición 2026 · v3 · Vigesimotercera entrega.

[Índice del manual](README.md) · [← Módulo 22](modulo-22-vi-vim-edicion-segura.md) · [Arquitectura](00-indice-arquitectura.md) · [Módulo 24 →](modulo-24-variables-entrada-argumentos-quoting.md)

## 1. Qué aprenderás

Al terminar este módulo podrás:

- explicar qué es un script;
- crear un archivo `.sh` de práctica;
- escribir un primer script Bash;
- explicar qué es un `shebang`;
- distinguir `bash script.sh` de `./script.sh`;
- comprender por qué un archivo necesita permiso de ejecución para usarse como `./script.sh`;
- aplicar `chmod +x` sobre un archivo propio del laboratorio;
- interpretar errores básicos como `Permission denied` y `command not found`;
- comprobar qué intérprete ejecutará el script;
- mantener el script dentro de un entorno seguro y versionable.

Conocimientos previos:
- terminal;
- rutas y archivos;
- permisos básicos;
- vi/Vim;
- `chmod`;
- ejecución de comandos.

**Seguridad:** todas las prácticas se realizan en `~/linux-lab/modulo-23-bash`. No ejecutaremos scripts descargados de Internet, no usaremos `sudo`, no modificaremos archivos del sistema y no añadiremos comandos destructivos. Antes de ejecutar un script, debes poder leerlo y explicar qué hace.

## 2. Qué es un script

Un **script** es un archivo de texto que contiene instrucciones que un intérprete puede ejecutar.

Ejemplo conceptual:

```text
script.sh
├── línea 1
├── línea 2
└── línea 3
```

En este módulo, el intérprete será Bash.

Un script no es automáticamente “un programa compilado”. Bash lee e interpreta sus instrucciones.

## 3. Extensión .sh: útil, pero no obligatoria

Un archivo Bash puede llamarse:

```text
hola.sh
```

La extensión `.sh` ayuda a reconocer su propósito.

Pero Bash no exige obligatoriamente esa extensión.

Lo importante es:

- contenido válido;
- intérprete correcto;
- permisos apropiados;
- forma de ejecución.

Para aprender, usaremos `.sh` por claridad.

## 4. Primer archivo

Entra al laboratorio:

```bash
cd ~/linux-lab
pwd
```

Comprueba:

```bash
ls -ld ./modulo-23-bash
```

Si no existe:

```bash
mkdir modulo-23-bash
```

Después:

```bash
cd modulo-23-bash
pwd
```

Crea:

```bash
touch hola.sh
```

Comprueba:

```bash
ls -l hola.sh
```

## 5. Editar el script

Abre:

```bash
vim hola.sh
```

o:

```bash
vi hola.sh
```

Escribe:

```bash
#!/usr/bin/env bash

printf 'Hola desde Bash\n'
```

Guarda y sal.

## 6. Línea 1 — shebang

```bash
#!/usr/bin/env bash
```

Esta primera línea se llama **shebang**.

Comienza con:

```text
#!
```

Cuando el sistema ejecuta el archivo directamente como programa, esa línea indica qué intérprete debe utilizar.

En este caso:

```text
/usr/bin/env
```

busca `bash` según el entorno y `PATH`.

## 7. Por qué usamos /usr/bin/env bash en el laboratorio

Ventaja:

- no depende de que Bash esté exactamente en `/bin/bash`.

Ejemplo:

```bash
#!/usr/bin/env bash
```

puede localizar Bash mediante `PATH`.

Pero esto tiene una consecuencia:

> el Bash elegido depende del entorno.

En entornos controlados, scripts administrativos o contextos de seguridad, un intérprete de ruta fija puede ser preferible.

## 8. Alternativa: /bin/bash

También verás:

```bash
#!/bin/bash
```

Esto solicita específicamente:

```text
/bin/bash
```

Ventaja:

- intérprete determinado por una ruta concreta.

Desventaja:

- esa ruta no es universal en todos los sistemas tipo Unix.

En muchas distribuciones Linux existe, pero no debes asumirlo fuera de tu entorno.

## 9. Qué opción usaremos

Para scripts de aprendizaje del usuario:

```bash
#!/usr/bin/env bash
```

Para scripts de sistema o entornos donde necesitas un intérprete exacto:

> verifica primero la ruta y política del entorno.

No existe una única elección perfecta para todos los contextos.

## 10. Línea vacía

Después del shebang usamos una línea vacía:

```text
#!/usr/bin/env bash

printf ...
```

No es obligatoria para ejecutar.

Se utiliza por legibilidad.

Ayuda a separar:

- cabecera;
- cuerpo del script.

## 11. printf

La segunda instrucción real:

```bash
printf 'Hola desde Bash\n'
```

`printf` imprime texto con formato.

Aquí:

```text
'Hola desde Bash\n'
```

contiene:

- texto;
- `\n` = salto de línea.

Salida:

```text
Hola desde Bash
```

## 12. Por qué printf y no echo

`echo` es muy común:

```bash
echo "Hola"
```

Pero su comportamiento con algunas opciones y secuencias puede variar entre implementaciones.

Para scripting didáctico y salida controlada, `printf` suele ser más predecible.

Esto no significa que `echo` esté prohibido.

## 13. Ejecutar mediante Bash

Sin cambiar permisos:

```bash
bash hola.sh
```

Aquí ejecutas:

```text
bash
```

y le entregas:

```text
hola.sh
```

como archivo de instrucciones.

Modelo:

```text
bash → abre hola.sh → interpreta contenido
```

En esta forma, el permiso de ejecución del archivo no es necesario si Bash puede leerlo.

## 14. El shebang no decide esta ejecución

Si escribes:

```bash
bash hola.sh
```

tú ya elegiste Bash explícitamente.

El shebang no es lo que seleccionó al intérprete en esa orden.

Esto es importante.

## 15. Ejecutar directamente

Otra forma:

```bash
./hola.sh
```

Aquí pides al sistema ejecutar el archivo directamente.

Para eso necesitas:

- shebang válido;
- permiso de ejecución;
- permisos sobre el camino/directorio;
- intérprete disponible.

## 16. Por qué usamos ./

Si escribes:

```text
hola.sh
```

la shell normalmente busca el comando en los directorios de `PATH`.

El directorio actual:

```text
.
```

no suele estar en `PATH` por razones prácticas y de seguridad.

Por eso:

```bash
./hola.sh
```

significa:

> ejecuta `hola.sh` desde el directorio actual.

## 17. No añadas . a PATH por comodidad

Agregar el directorio actual globalmente a `PATH` puede hacer que ejecutes accidentalmente un archivo local con el mismo nombre que una herramienta esperada.

Para aprender, usa:

```bash
./hola.sh
```

No cambies `PATH` para evitar escribir `./`.

## 18. Permission denied

Antes de dar permiso de ejecución, prueba:

```bash
./hola.sh
```

Es posible que recibas:

```text
Permission denied
```

Eso no significa que debas usar `sudo`.

Consulta:

```bash
ls -l hola.sh
```

Si no tiene `x`, falta permiso de ejecución.

## 19. chmod +x

Sobre tu archivo de laboratorio:

```bash
chmod u+x hola.sh
```

Esto añade ejecución al propietario.

Comprueba:

```bash
ls -l hola.sh
```

Podrías ver algo como:

```text
-rwxr--r--
```

según permisos previos.

No necesitamos dar ejecución a grupo y otros para esta práctica.

## 20. Ejecutar después del permiso

Ahora:

```bash
./hola.sh
```

Salida esperada:

```text
Hola desde Bash
```

## 21. chmod +x frente a chmod 777

No uses:

```text
chmod 777 hola.sh
```

para “hacerlo ejecutable”.

Eso también concede escritura/lectura/ejecución a clases que probablemente no lo necesitan.

Usamos:

```bash
chmod u+x hola.sh
```

porque modifica solo el permiso necesario para el propietario.

## 22. Verificar el shebang

Puedes consultar la primera línea:

```bash
head -n 1 hola.sh
```

Debe mostrar:

```text
#!/usr/bin/env bash
```

Comprueba también:

```bash
command -v bash
```

Esto indica qué Bash encontraría tu shell actual mediante `PATH`.

## 23. env y PATH

`/usr/bin/env bash` utiliza el entorno para localizar `bash`.

Por eso:

```text
PATH
```

influye.

En un laboratorio de usuario es práctico.

En contextos privilegiados no debes depender de un `PATH` no confiable.

No ejecutaremos scripts Bash con `sudo` en este módulo.

## 24. Comentarios

En Bash:

```bash
# Esto es un comentario
```

Bash ignora el comentario durante la ejecución.

Ejemplo:

```bash
#!/usr/bin/env bash

# Primer script del laboratorio.
printf 'Hola desde Bash\n'
```

## 25. ¿El shebang es un comentario?

Para Bash, una línea que comienza con `#` normalmente tiene comportamiento de comentario.

Pero:

```text
#!
```

al inicio de un archivo ejecutado directamente tiene significado especial para el mecanismo de ejecución del sistema.

Por eso el shebang debe estar en la primera línea.

## 26. No poner espacios antes del shebang

Correcto:

```text
#!/usr/bin/env bash
```

Evita:

```text
  #!/usr/bin/env bash
```

El reconocimiento del shebang depende de que aparezca al inicio del archivo.

## 27. Saltos de línea Windows

Un script creado en Windows puede usar terminaciones CRLF.

Eso puede producir errores como:

```text
/usr/bin/env: 'bash\r': No such file or directory
```

o mensajes parecidos.

La causa no es necesariamente que Bash falte.

Puede existir un carácter `\r` oculto.

## 28. Consultar el tipo de archivo

Puedes usar:

```bash
file hola.sh
```

La salida puede ayudar a detectar:

- texto;
- codificación;
- terminaciones CRLF en algunos casos.

No cambia el archivo.

## 29. Bash -n

Antes de ejecutar un script Bash puedes revisar su sintaxis:

```bash
bash -n hola.sh
```

`-n` hace que Bash lea las órdenes sin ejecutarlas, comprobando sintaxis.

Si no imprime errores:

> no garantiza que el programa haga lo correcto.

Solo significa que no detectó determinados errores sintácticos.

## 30. Bash -x

Existe:

```text
bash -x script.sh
```

que muestra trazas de órdenes durante la ejecución.

No lo usaremos todavía porque en scripts reales podría mostrar datos sensibles como argumentos o variables.

Se estudiará cuando veamos depuración.

## 31. Error command not found dentro del script

Ejemplo:

```bash
#!/usr/bin/env bash

prinf 'Hola\n'
```

Tiene un error:

```text
prinf
```

en lugar de:

```text
printf
```

Bash puede responder:

```text
command not found
```

La corrección no es instalar un paquete.

Primero revisa la ortografía.

## 32. Error de sintaxis

Ejemplo conceptual:

```bash
printf 'Hola\n
```

falta cerrar la comilla.

`bash -n` puede detectar este tipo de problema.

Cuando llegue el momento de corregir scripts:

1. localiza línea;
2. identifica la estructura abierta;
3. haz la corrección mínima;
4. vuelve a validar.

## 33. No ejecutar scripts descargados sin revisar

No hagas:

```bash
bash archivo-descargado.sh
```

solo porque una guía diga “ejecútalo”.

Primero:

1. identifica procedencia;
2. abre el archivo;
3. comprende comandos;
4. busca cambios destructivos;
5. busca credenciales;
6. revisa red;
7. comprueba si solicita privilegios.

En este curso los scripts iniciales los escribimos nosotros.

## 34. curl | bash

No utilizaremos:

```text
curl ... | bash
```

como método de aprendizaje.

Ese patrón descarga contenido y lo ejecuta sin revisión previa.

Primero descarga, inspecciona y comprende si alguna vez un entorno autorizado lo requiere.

## 35. No ejecutar con sudo

Evita:

```text
sudo ./hola.sh
```

No hace falta.

Nuestro script solo imprime texto.

Ejecutar un script con privilegios amplía el impacto de cualquier error.

## 36. Primera estructura recomendada

Para los primeros scripts:

```bash
#!/usr/bin/env bash

# Descripción breve.
printf 'Mensaje\n'
```

Mantén el script:

- corto;
- legible;
- sin privilegios;
- sin operaciones destructivas.

## 37. Práctica A — crear el script

Dentro del laboratorio:

```bash
touch saludo.sh
vim saludo.sh
```

Contenido:

```bash
#!/usr/bin/env bash

printf 'Bienvenido al laboratorio Bash\n'
```

Guarda.

## 38. Práctica B — validación

```bash
bash -n saludo.sh
```

Si no aparece error:

```bash
bash saludo.sh
```

Debes ver:

```text
Bienvenido al laboratorio Bash
```

## 39. Práctica C — permiso

Consulta:

```bash
ls -l saludo.sh
```

Después:

```bash
chmod u+x saludo.sh
```

Comprueba otra vez:

```bash
ls -l saludo.sh
```

Explica qué permiso cambió.

## 40. Práctica D — ejecución directa

```bash
./saludo.sh
```

Explica:

- qué significa `./`;
- qué función cumple el shebang;
- por qué ahora puede ejecutarse.

## 41. Práctica E — comentario

Edita:

```bash
#!/usr/bin/env bash

# Muestra un saludo.
printf 'Bienvenido al laboratorio Bash\n'
```

Ejecuta otra vez.

El comentario no debe imprimirse.

## 42. Práctica F — error intencional y corrección

En una copia del script:

```bash
cp saludo.sh saludo-error.sh
```

Edita la copia y cambia temporalmente:

```text
printf
```

por:

```text
prinf
```

Ejecuta:

```bash
bash saludo-error.sh
```

Observa el error.

Después corrige **solo** esa palabra.

No borres el script original.

## 43. Práctica G — sintaxis rota

En otra copia:

```bash
cp saludo.sh sintaxis-error.sh
```

Quita deliberadamente la comilla final del texto.

Después:

```bash
bash -n sintaxis-error.sh
```

Lee el error.

Corrige la comilla y vuelve a validar.

## 44. GitHub y scripts de aprendizaje

Los scripts de esta lección sí tienen valor educativo y deben conservarse en GitHub.

Antes de subir:

- revisa que no haya contraseñas;
- revisa que no haya tokens;
- revisa rutas privadas;
- revisa claves;
- revisa datos personales.

Ejemplo de ruta:

```text
linux/bash/
```

Ejemplo de commit:

```text
linux: añadir primer script Bash con shebang
```

No se hará commit de archivos con secretos.

## 45. Errores frecuentes

| Error | Problema | Corrección |
|---|---|---|
| `./script.sh: Permission denied` | Puede faltar permiso de ejecución; también pueden intervenir permisos de directorios, un montaje `noexec` u otros controles | Revisar ruta y permisos; añadir `chmod u+x` solo si falta ese permiso en el archivo propio |
| `script.sh: command not found` | Directorio actual no está en PATH | Usa `./script.sh` |
| Shebang no funciona | No está en primera línea o intérprete no existe | Revisa primera línea |
| `bash\r` no encontrado | Posible CRLF | Revisa formato del archivo |
| Usas `chmod 777` | Das permisos excesivos | Añade solo `u+x` |
| Usas sudo | Privilegios innecesarios | Ejecuta como usuario normal |
| Script descargado se ejecuta sin leer | Riesgo de cambios no entendidos | Inspecciona antes |
| `bash -n` no da error y asumes que todo está bien | Solo verifica sintaxis | Prueba lógica por separado |
| Escribes mal un comando | Bash no lo encuentra | Revisa ortografía antes de instalar nada |

## 46. Método antes de ejecutar un script

1. identifica quién lo creó;
2. abre el archivo;
3. lee cada línea;
4. comprueba rutas;
5. identifica operaciones que modifican/borran;
6. comprueba llamadas de red;
7. identifica privilegios;
8. valida sintaxis;
9. ejecuta en entorno adecuado;
10. revisa resultado.

## 47. Práctica independiente

Crea:

```text
mi-primer-script.sh
```

Debe contener:

- shebang;
- un comentario;
- dos líneas `printf`.

Después:

1. valida con `bash -n`;
2. ejecuta con `bash archivo`;
3. consulta permisos;
4. añade `u+x`;
5. ejecuta con `./archivo`;
6. explica la diferencia entre ambas formas.

No copies el ejemplo exacto.

## 48. Mini evaluación

1. ¿qué es un script?
   - A) Archivo de instrucciones interpretables.
   - B) Solo un binario compilado.

2. ¿qué es un shebang?
   - A) Línea que indica intérprete al ejecutar directamente.
   - B) Un permiso.

3. ¿debe estar en la primera línea?
   - A) Sí.
   - B) No.

4. ¿`bash script.sh` necesita obligatoriamente permiso `x` en el archivo?
   - A) Sí.
   - B) No, si Bash puede leerlo.

5. ¿`./script.sh` normalmente requiere permiso de ejecución?
   - A) Sí.
   - B) No.

6. ¿qué significa `./`?
   - A) Directorio actual.
   - B) Directorio raíz.

7. ¿es recomendable `chmod 777` para ejecutar un script?
   - A) Sí.
   - B) No.

8. ¿`bash -n` ejecuta normalmente las órdenes?
   - A) Sí.
   - B) No.

9. ¿una validación sintáctica garantiza lógica correcta?
   - A) Sí.
   - B) No.

10. ¿debes ejecutar scripts descargados sin revisarlos?
   - A) Sí.
   - B) No.

## 49. Registro de aprendizaje

Puedes responder:

```text
Un script es:
Un shebang sirve para:
#!/usr/bin/env bash significa:
bash script.sh hace:
./script.sh hace:
./ significa:
chmod u+x hace:
bash -n sirve para:
¿Por qué no uso chmod 777?:
¿Por qué no ejecuto scripts sin leerlos?:
Algo que todavía confundo:
Estado: EN APRENDIZAJE / PRACTICADO
```

## 50. Fuentes y límites

Clasificación y estado de los enlaces de esta sección: [catálogo de fuentes](auditorias/06-catalogo-fuentes.md) (jerarquía E04, comprobación del 9 de octubre de 2026).

Fuentes principales:

- GNU Bash Reference Manual:
  https://www.gnu.org/software/bash/manual/
- GNU Bash — Shell Scripts:
  https://www.gnu.org/software/bash/manual/html_node/Shell-Scripts.html
- GNU Bash — Invoking Bash:
  https://www.gnu.org/software/bash/manual/html_node/Invoking-Bash.html
- Linux man-pages — `execve(2)`:
  https://man7.org/linux/man-pages/man2/execve.2.html
- GNU Coreutils — `chmod`:
  https://www.gnu.org/software/coreutils/manual/html_node/chmod-invocation.html

Se posponen:

- variables;
- `read`;
- parámetros;
- `$@`;
- expansión;
- quoting avanzado;
- condicionales;
- bucles;
- funciones;
- exit codes avanzados;
- `set -e`;
- traps;
- ShellCheck;
- debugging con `set -x`.

**Estado de la lección:** redactada y revisada documentalmente. Las prácticas usan scripts propios, cortos y sin privilegios.

---

**Siguiente:** [Módulo 24 — Variables, entrada, argumentos, expansiones y quoting en Bash](modulo-24-variables-entrada-argumentos-quoting.md) · [Volver al índice](README.md)
